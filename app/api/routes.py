from fastapi import APIRouter, UploadFile, File, Form
import os, shutil
from app.services.document import load_and_split_pdf
from app.services.vector_store import create_faiss_index, load_faiss_index
from app.services.rag_chain import build_qa_chain

router = APIRouter()
UPLOAD_FOLDER = "uploaded_docs/"
INDEX_FOLDER = "faiss_indexes/"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(INDEX_FOLDER, exist_ok=True)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    chunks = load_and_split_pdf(file_path)
    index_path = os.path.join(INDEX_FOLDER, file.filename.replace(".pdf", ""))
    create_faiss_index(chunks, index_path)

    return {"message": "Document uploaded and indexed.", "doc_id": file.filename}

@router.post("/ask")
async def ask_question(doc_id: str = Form(...), query: str = Form(...)):
    index_path = os.path.join(INDEX_FOLDER, doc_id.replace(".pdf", ""))
    vector_store = load_faiss_index(index_path)

    qa_chain = build_qa_chain(vector_store)
    response = qa_chain.run(query)

    return {
        "doc_id": doc_id,
        "question": query,
        "answer": response
    }
