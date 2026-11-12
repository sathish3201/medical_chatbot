
# MedNexus AI 🩺

### Medical Intelligence • Knowledge Base + Web Research

MedNexus AI is an AI-powered medical education assistant that helps users understand medical topics through an interactive conversational interface. It combines a medical knowledge base, Retrieval-Augmented Generation (RAG), and web research to generate context-aware educational responses.

The application features a modern medical-tech interface with support for text conversations, image uploads, camera capture, voice input, and audio responses.

> **Disclaimer:** MedNexus AI is designed for medical education and informational purposes only. It does not provide medical diagnoses or replace professional medical advice. Always consult a qualified healthcare professional for medical concerns.

---

## ✨ Features

### 🤖 AI Medical Assistant
- Interactive medical question-and-answer experience.
- Context-aware responses using an AI-powered backend.
- Medical knowledge retrieval using RAG.
- Web research support for additional information.

### 📚 Medical Knowledge Base
- Retrieves relevant information from medical reference documents.
- Uses vector embeddings and similarity search.
- Generates knowledge-grounded responses.
- Reduces reliance on unsupported model-generated information.

### 🔎 Web Research
- Optional web search integration for additional medical information.
- Combines retrieved knowledge with external research.
- Provides broader context for medical topics.

### 🖼️ Image Input
- Upload medical-related images through the chat interface.
- Preview and remove selected images before sending.
- Capture images directly using the camera.
- AI-powered image observation support through the backend.

### 🎙️ Voice Interaction
- Voice input using speech recognition or Whisper-based transcription.
- Audio response support using text-to-speech.
- Listen to generated assistant responses.

### 🔐 API Configuration
- Secure backend API communication.
- API token configuration through the interface.
- Backend connectivity status indicator.

### 🎨 Modern User Interface
- MedNexus AI branding with a medical-tech design.
- Responsive desktop and mobile layout.
- Interactive chat interface.
- Image preview, camera controls, and voice interaction.
- Medical education disclaimer.

---

## 🏗️ Project Architecture

```text
MedNexus-AI/
│
├── app.py / main.py
│
├── backend/
│   ├── agents/
│   ├── tools/
│   ├── graph/
│   └── ...
│
├── static/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── data/
│   └── medical_documents/
│
├── .env
├── requirements.txt
└── README.md
```

*Note: Update the directory structure according to your actual repository.*

---

## 🧠 Technology Stack

| Component | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI |
| Agent Orchestration | LangGraph |
| LLM Integration | Groq / Configured LLM Provider |
| RAG Framework | LangChain |
| Vector Database | Pinecone |
| Embeddings | FastEmbed / Configured Embedding Model |
| Web Research | Tavily (Optional) |
| Speech Processing | Whisper (If Configured) |
| Text-to-Speech | Configured TTS Provider |
| Application Server | Uvicorn |

---

## 🔄 Application Workflow

```text
                 User
                  |
                  v
          MedNexus AI Interface
                  |
       +----------+-----------+
       |          |           |
       v          v           v
     Text       Image        Voice
       |          |           |
       +----------+-----------+
                  |
                  v
               FastAPI
                  |
                  v
           LangGraph Agent
                  |
          +-------+-------+
          |               |
          v               v
       Medical RAG    Web Research
          |               |
          v               v
       Pinecone       Search Tool
          |               |
          +-------+-------+
                  |
                  v
             LLM Response
                  |
                  v
          MedNexus AI Chat UI
                  |
                  v
             User Response
```

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd MedNexus-AI
```

### 2. Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv venv
venv\Scripts\activate
```

**Linux / WSL:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key

PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_pinecone_index

TAVILY_API_KEY=your_tavily_api_key
```

Add other provider-specific variables required by your backend.

**Important:** Never commit your `.env` file or expose API credentials in frontend JavaScript.

### 5. Run the Application

If your FastAPI entry point is `main.py`:

```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

Replace `main:app` with your actual module path if different.

Open the application:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 📁 Frontend Files

| File | Responsibility |
|---|---|
| `index.html` | MedNexus AI page structure and interface |
| `style.css` | Responsive styling and medical-tech theme |
| `app.js` | Chat interactions, API requests, image preview, camera, and voice controls |

### Important HTML Element IDs

The frontend uses the following element IDs to connect with `app.js`:

| Element ID | Purpose |
|---|---|
| `status` | Backend connection status |
| `messages` | Chat conversation container |
| `chatForm` | Chat submission form |
| `message` | User message input |
| `image` | Image upload input |
| `preview` | Image preview container |
| `thumbnail` | Selected image preview |
| `camera` | Camera activation |
| `mic` | Voice input |
| `listen` | Audio response control |
| `token` | API token configuration |

**Note:** Keep these IDs unchanged unless you also update the corresponding JavaScript selectors in `app.js`.

---

## 🔒 Security Considerations

- Store API credentials in environment variables.
- Add `.env` and other sensitive files to `.gitignore`.
- Perform LLM and external API requests through the backend.
- Validate uploaded files and restrict accepted file types.
- Apply authentication and authorization when exposing the application publicly.
- Avoid storing sensitive medical information unnecessarily.

---

## 🚀 Future Enhancements

- Medical document upload and personalized knowledge retrieval.
- Source citations and references in generated responses.
- Improved medical image analysis.
- Multi-agent medical research workflow.
- Human review for sensitive or high-risk medical content.
- Conversation history and user authentication.
- Improved response verification and safety guardrails.

---

## ⚠️ Medical Disclaimer

MedNexus AI is an educational AI application. Its responses may contain inaccuracies or incomplete information. It must not be used as a substitute for professional medical diagnosis, treatment, emergency care, or clinical decision-making.

For medical emergencies, contact local emergency services or seek immediate professional medical care.

---

## 👨‍💻 Author

**Sathish Chakali**

- **GitHub:** [sathish3201](https://github.com/sathish3201)
- **Portfolio:** [My Portfolio](https://sathish3201.github.io/portfolio/)
- **LinkedIn:** [Sathish Chakali](https://linkedin.com/in/sathish-chakali-91221b320)

---

<p align="center">
  <strong>MedNexus AI — Understand health. Make informed decisions.</strong>
</p>
