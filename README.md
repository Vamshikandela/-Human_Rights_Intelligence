# -Human_Rights_Intelligence
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B)
![LangChain](https://img.shields.io/badge/Framework-LangChain-green)
![Gemini](https://img.shields.io/badge/LLM-Google_Gemini-orange)
![FAISS](https://img.shields.io/badge/VectorDB-FAISS-purple)
![RAG](https://img.shields.io/badge/AI-RAG-critical)

# (AI-Powered Legal RAG Assistant for Human Rights & Constitutional Law)
📌 Overview

## Human Rights Intelligence is a Retrieval-Augmented Generation (RAG) based legal assistant designed to answer questions related to:

Human Rights
Indian Constitutional Rights
Legal Articles
International Law Documents

Users can upload legal PDF documents and ask questions in natural language.
The system retrieves relevant legal context from documents and generates accurate responses using Google's Gemini LLM.

## 🎯 Key Features
* 📄 Upload legal PDF documents
* 🔍 Semantic legal document retrieval
* 🤖 AI-powered legal question answering
* ⚖️ Human Rights focused legal assistant
* 🇮🇳 Indian Constitution article support
* 🌍 UDHR (Universal Declaration of Human Rights) support
* 🧠 Gemini-powered response generation
* 📚 FAISS vector database integration
* 🎨 Interactive Streamlit UI
## 🧠 How It Works
    User Uploads PDF
            ↓
    Text Extraction & Chunking
            ↓
    Generate Embeddings
            ↓
    Store in FAISS Vector DB
            ↓
    User Query
            ↓
    Semantic Retrieval
            ↓
    Gemini LLM Generates Answer
            ↓
    Final Legal Response
    🏗️ Project Structure
    Human_Rights_Intelligence/
    │
    ├── app.py                    # Streamlit application
    ├── requirements.txt          # Dependencies
    ├── .env                      # API keys
    │
    ├── data/                     # Uploaded PDFs
    ├── vectorstore/              # FAISS database
    ├── utils/                    # Helper functions
    │
    ├── pdf_loader.py             # PDF processing
    ├── embeddings.py             # Embedding generation
    ├── rag_pipeline.py           # Retrieval pipeline
    └── README.md                 # Documentation
## ⚙️ Tech Stack
* Python
* Streamlit
* LangChain
* Google Gemini
* FAISS
## RAG Architecture
* 🚀 Setup & Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/human-rights-intelligence.git
cd human-rights-intelligence
2️⃣ Create Virtual Environment
* Windows
python -m venv venv
venv\Scripts\activate
* Linux/Mac
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
* pip install -r requirements.txt
* 🔑 Environment Variables

* Create a .env file:

GOOGLE_API_KEY=your_gemini_api_key

Get API key from:

        Google AI Studio
        ▶️ Run the Application
        streamlit run app.py
        📚 Recommended Legal Documents
        Human Rights Resources
        Universal Declaration of Human Rights (UDHR)
        United Nations Human Rights Office
        Indian Constitution Official Website
        National Human Rights Commission India
🧪 Example Queries
✅ Constitutional Rights
What is Article 14 of the Indian Constitution?

✔ Explains equality before law

✅ Right to Life
Explain Article 21 and protection of life and personal liberty.

✔ Retrieves legal interpretation and explanation

✅ Comparative Legal Analysis
Compare UDHR and Indian Constitutional Rights.

✔ Generates comparative legal response

✅ Human Rights Protection
What laws protect children against child labour?

✔ Retrieves relevant constitutional and human rights laws

## 🧱 RAG Pipeline Flow

The application follows a standard Retrieval-Augmented Generation workflow:

documents → embeddings → FAISS → retrieval → Gemini → answer
## ⚠️ Limitations
Supports mainly PDF documents
No multilingual legal translation
No real-time legal database integration
Responses are AI-generated and may require verification
## 🔮 Future Improvements
Multi-document querying
OCR support for scanned PDFs
Legal citation generation
Voice-enabled legal assistant
Case law recommendation system
Multi-language support
Cloud deployment
## 🧠 Key Learnings
RAG pipeline implementation
Vector databases and embeddings
Legal document retrieval
Streamlit application development
Gemini LLM integration
Semantic search systems
## 📌 Conclusion

Human Rights Intelligence demonstrates a practical implementation of an AI-powered legal assistant using Retrieval-Augmented Generation (RAG). The system combines semantic retrieval, vector databases, and large language models to provide intelligent responses for legal and human rights related queries.

🙌 Author
Kandela Vamshi

B.Sc (Data Science) | AI & Data Science Enthusiast

GitHub
LinkedIn
