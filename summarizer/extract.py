import pdfplumber

def extract_text_from_pdf(file_path: str) -> str:
    """Extracts text from a PDF file using pdfplumber."""
    text = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return "\n".join(text)

