🧠 Document Assistant RAG
A lightweight, local-first Retrieval-Augmented Generation (RAG) document assistant powered by FastAPI, LangChain, and FAISS. Upload PDF documents, process them into embeddings, and ask natural language questions with LLM-powered answers—all while maintaining local control over your data.

🚀 Features
✅ Upload & process multiple PDF documents

📄 Automatic text extraction, cleaning, and chunking

🧠 Embedding via HuggingFace models (all-MiniLM-L6-v2)

🔍 FAISS vector store for efficient semantic retrieval

🗨️ Question answering via open-source LLMs (e.g., Mistral 7B)

🧱 Modular FastAPI backend (LLM, chunking, RAG, etc.)

🧩 LangChain integration for scalable pipelines

💾 Local persistence of vectors + metadata

🎛️ Optional: Streamlit UI frontend for real-time QA

🛠 Tech Stack
FastAPI – RESTful backend

LangChain – RAG orchestration & scaling

FAISS – Fast vector similarity search

HuggingFace – Text embeddings

PyMuPDF / pdfminer.six – PDF parsing

Mistral or HuggingFace models – LLM QA

Streamlit – Optional web frontend

📦 Installation
bash
Copy
Edit
git clone https://github.com/SBoo9/Document_assistang_RAG.git
cd Document_assistang_RAG
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
▶️ Run the FastAPI Backend
bash
Copy
Edit
uvicorn app.main:app --reload
Visit: http://localhost:8000/docs

🌐 Streamlit Frontend (Optional)
bash
Copy
Edit
streamlit run frontend/app.py
🧩 Coming Soon / Roadmap
✅ Multi-document memory

✅ Chunk/embedding persistence

🔄 Streaming answers

🔌 Switchable LLM support

🌐 HuggingFace/Mistral integration

☁️ S3 / DB support for production deployment