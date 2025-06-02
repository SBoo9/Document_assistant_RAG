import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000"

st.title("🧠 LangChain RAG Assistant (Mistral)")

# Upload PDF
st.header("📄 Upload Document")
uploaded_file = st.file_uploader("Choose a PDF", type="pdf")

if uploaded_file:
    with st.spinner("Uploading and indexing..."):
        files = {"file": uploaded_file.getvalue()}
        res = requests.post(f"{BACKEND_URL}/upload", files={"file": uploaded_file})
        if res.status_code == 200:
            st.success("File uploaded successfully!")
            doc_id = res.json()["doc_id"]
        else:
            st.error(res.json()["error"])
else:
    doc_id = None

# Ask Questions
st.header("❓ Ask a Question")
query = st.text_input("Enter your question")

if query and doc_id:
    with st.spinner("Thinking..."):
        data = {"doc_id": doc_id, "query": query}
        res = requests.post(f"{BACKEND_URL}/ask", data=data)
        if res.status_code == 200:
            st.markdown(f"**Answer:** {res.json()['answer']}")
        else:
            st.error("Error: " + res.text)
