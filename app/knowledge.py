
from functools import lru_cache

from pinecone import Pinecone, ServerlessSpec
from langchain_groq import ChatGroq
from langchain_community.embeddings import FastEmbedEmbeddings

from app.config import settings


EMBEDDING_DIMENSION = 384


@lru_cache(maxsize=1)
def clients():

    if not settings.groq_api_key or not settings.pinecone_api_key:
        raise ValueError("Groq and Pinecone API keys must be configured.")

    llm = ChatGroq(
        api_key=settings.groq_api_key,
        model=settings.groq_chat_model,
        temperature=0
    )

    pc = Pinecone(api_key=settings.pinecone_api_key)

    return llm, pc


@lru_cache(maxsize=1)
def embedding_model():

    return FastEmbedEmbeddings(
        model_name=settings.fast_embed_model
    )


# def ensure_index():

#     _, pc = clients()

#     if not pc.has_index(settings.pinecone_index):
#         pc.create_index(
#             name=settings.pinecone_index,
#             dimension=EMBEDDING_DIMENSION,
#             metric="cosine",
#             spec=ServerlessSpec(
#                 cloud="aws",
#                 region="us-east-1"
#             )
#         )

#     return pc.Index(settings.pinecone_index)

def ensure_index():
    _, pc = clients()

    try:
        print("Pinecone index:", settings.pinecone_index)

        if not pc.has_index(settings.pinecone_index):
            print("Creating new Pinecone index...")

            pc.create_index(
                name=settings.pinecone_index,
                dimension=EMBEDDING_DIMENSION,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                )
            )

        index = pc.Index(settings.pinecone_index)

        description = pc.describe_index(settings.pinecone_index)

        print("Pinecone index dimension:", description.dimension)
        print("Pinecone index status:", description.status)

        return index

    except Exception:
        import traceback
        traceback.print_exc()
        raise


def embed(texts):

    model = embedding_model()

    return model.embed_documents(texts)


def search_kb(query, top_k=5):

    index = ensure_index()

    vector = embedding_model().embed_query(query)

    result = index.query(
        vector=vector,
        top_k=top_k,
        include_metadata=True
    )

    return [
        {
            "page": match.metadata.get("page"),
            "text": match.metadata.get("text", ""),
            "score": round(match.score, 3),
            "source": "Gale Encyclopedia (2002)"
        }
        for match in result.matches
        if match.score >= 0.30
    ]
