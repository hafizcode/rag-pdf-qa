import fitz  # PyMuPDF

def load_pdf_text(uploaded_file):
    """
    Extracts and returns all text from the uploaded PDF file.
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text
