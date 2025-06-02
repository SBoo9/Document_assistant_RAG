from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List

def load_and_split_pdf(filepath: str)-> List[str]:
    doc= PyPDFLoader(filepath)
    splitter= RecursiveCharacterTextSplitter(
        chunks_size=500,
        chunk_overlap=64
    )

    split_docs = splitter.split_documents(doc)
    return split_docs