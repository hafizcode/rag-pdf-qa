import streamlit as st
from utils.pdf_loader import load_pdf_text
from utils.embedder import embed_text_chunks, create_vector_store, search_similar_chunks
from utils.rag_qa import generate_answer

st.title("📄 DocuBot - RAG-based Q&A System")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
query = st.text_input("Ask a question from your document")

if uploaded_file:
    with st.spinner("Reading PDF..."):
        raw_text = load_pdf_text(uploaded_file)

    with st.spinner("Embedding text and creating vector store..."):
        chunks, embeddings = embed_text_chunks(raw_text)
        index = create_vector_store(embeddings)

    if query:
        with st.spinner("Searching and generating answer..."):
            relevant_chunks = search_similar_chunks(query, chunks, index)
            answer = generate_answer(query, relevant_chunks)
            st.markdown("### 📌 Answer")
            st.success(answer)

### File: utils/pdf_loader.py
import fitz  # PyMuPDF

def load_pdf_text(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

### File: utils/embedder.py
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text_chunks(text, chunk_size=500):
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    embeddings = model.encode(chunks)
    return chunks, embeddings

def create_vector_store(embeddings):
    dim = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index

def search_similar_chunks(query, chunks, index, top_k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)
    return [chunks[i] for i in indices[0]]

### File: utils/rag_qa.py
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-pro')

def generate_answer(query, context_chunks):
    context = "\n".join(context_chunks)
    prompt = f"""You are a helpful assistant. Use the context below to answer the question.

Context:
{context}

Question: {query}
Answer:"""

    response = model.generate_content(prompt)
    return response.text.strip()
