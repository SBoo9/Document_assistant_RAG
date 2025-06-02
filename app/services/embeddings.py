from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_chunks(chunks: list) -> np.ndarray:
    embeddings = model.encode(chunks, show_progress_bar= True)
    return np.array(embeddings).astype("float32")

def create_faiss_index(embeddings: np.array) -> faiss.IndexFlatL2:
    dim = embeddings.shape[1]
    index= faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index
