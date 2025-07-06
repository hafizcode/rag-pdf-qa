# 📘 DocuBot RAG – Gemini-Powered PDF Q&A App

A lightweight, fully free, Retrieval-Augmented Generation (RAG) app built with **Streamlit**, **FAISS**, **Sentence Transformers**, and **Gemini** by Google. Upload a PDF, ask questions, and get intelligent answers from the document.

---

## 🔍 Features

- ✅ Upload and parse any PDF
- ✅ Chunk and embed content using `sentence-transformers`
- ✅ Store vector embeddings in a local FAISS index
- ✅ Retrieve the most relevant chunks based on your question
- ✅ Generate a natural language answer using **Gemini 1.5 Flash**
- ✅ All tools used are free and open for personal/academic use

---

## 🧠 Tech Stack

| Component             | Tool                                      |
|----------------------|-------------------------------------------|
| Frontend UI          | Streamlit                                |
| PDF Parsing          | PyMuPDF (`fitz`)                          |
| Embedding Model      | `sentence-transformers` (`all-MiniLM-L6-v2`) |
| Vector Search        | FAISS                                     |
| LLM for Response     | Gemini 1.5 Flash (via `google-generativeai`) |
| Env Management       | `python-dotenv`                           |

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/docubot-rag
cd docubot-rag
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If you don’t have a `requirements.txt`, use this:

```bash
pip install streamlit sentence-transformers faiss-cpu PyMuPDF google-generativeai python-dotenv
```

---

## 🔐 Setup API Key

1. Go to [https://makersuite.google.com/app](https://makersuite.google.com/app)
2. Generate a Gemini API key
3. Create a `.env` file in your project root:

```env
GEMINI_API_KEY=your-api-key-here
```

---

## 🚀 Run the App

```bash
streamlit run app.py
```

It will open in your browser at `http://localhost:8501`.

---

## 🧪 How It Works (RAG Flow)

```text
          ┌────────────┐
          │  PDF File  │
          └────┬───────┘
               │
     Extract text using PyMuPDF
               │
               ▼
     Chunk & Embed with MiniLM
               │
               ▼
     Store in FAISS vector index
               │
               ▼
Ask a Question ──► Search Relevant Chunks
               │
               ▼
     Combine chunks as context
               │
               ▼
   Query Gemini 1.5 Flash for Answer
               │
               ▼
        Show response in Streamlit
```

---

## 🧰 File Structure

```
docubot_rag/
├── app.py
├── .env
├── requirements.txt
└── utils/
    ├── pdf_loader.py
    ├── embedder.py
    └── rag_qa.py
```

---

## 📚 Example Use Cases

* 📄 Ask questions about resumes or research papers
* 🧑‍🎓 Query academic syllabi or notes
* 🧾 Analyze business reports or invoices

---

## 📌 Limitations

* Gemini API usage depends on free tier limits
* Limited to English and simple PDFs (no scanned images/OCR yet)
* Only supports single PDF at a time

---

## ✅ To-Do (Future Ideas)

* [ ] Add support for multiple documents
* [ ] Add OCR for scanned PDFs
* [ ] Use local LLM (like `Gemma`) for offline mode
* [ ] Streamlit cloud deployment with download/export feature

---

## 🙋‍♂️ Author

Built by **\[Your Name]** for learning, showcasing RAG, and AI interview preparation.

---

## 🧠 Key Learning Topics

* Retrieval-Augmented Generation (RAG)
* FAISS and vector search
* Gemini and LLM prompting
* Practical LLM app using free tools

---

## 🆓 License

Free for educational use. Not for production or commercial use without appropriate model and API terms.



---

### ✅ Want the `requirements.txt` too?

Here it is:

- streamlit
- sentence-transformers
- faiss-cpu
- PyMuPDF
- google-generativeai
- python-dotenv