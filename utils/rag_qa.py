import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Configure Gemini with API key from .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

def generate_answer(query, context_chunks):
    """
    Generates an answer using Gemini based on the query and relevant document chunks.
    """
    context = "\n".join(context_chunks)
    prompt = f"""You are a helpful assistant. Use the context below to answer the question.

Context:
{context}

Question: {query}
Answer:"""

    response = model.generate_content(prompt)
    return response.text.strip()
