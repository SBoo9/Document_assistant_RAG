import faiss
import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

EMBEDDINGS = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") # If you have issues try locally downloading the model and adding its path


FAISS_ID={}
CHUNKS_ID={}

def save_index(index, path="storage/vector.index"):
    faiss.write_index(index, path)

def load_index(path="storage/vector.index"):
    if os.path.exists(path):
        return faiss.read_index(path)
    return None

def add_document(doc_id, index, chunks):
    FAISS_ID[doc_id]= index
    CHUNKS_ID[doc_id]= chunks

def get_document(doc_id):
    return FAISS_ID.get[doc_id], CHUNKS_ID.get[doc_id]

def create_faiss_index(chunks, index_path: str)-> FAISS:
    db = FAISS.from_documents(chunks, EMBEDDINGS)
    db.save_local(index_path)
    return db

def load_faiss_index(index_path: str)-> FAISS:
    return FAISS.load_local(index_path,EMBEDDINGS)