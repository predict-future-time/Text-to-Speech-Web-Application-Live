import fitz  # PyMuPDF
import docx

# Extract text from PDF using PyMuPDF
def extract_text_from_pdf(filepath):
    text = ''
    with fitz.open(filepath) as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()

# Extract text from Word (docx) file
def extract_text_from_docx(filepath):
    doc = docx.Document(filepath)
    return '\n'.join(para.text for para in doc.paragraphs)
