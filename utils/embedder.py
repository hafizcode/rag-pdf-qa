from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

# Load the Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text_chunks(text, chunk_size=500):
    """
    Splits the input text into chunks and returns the chunks and their embeddings.
    """
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    embeddings = model.encode(chunks)
    return chunks, embeddings

def create_vector_store(embeddings):
    """
    Creates a FAISS index from the embeddings.
    """
    dim = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index

def search_similar_chunks(query, chunks, index, top_k=3):
    """
    Finds top_k chunks most similar to the query using FAISS.
    """
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)
    return [chunks[i] for i in indices[0]]
