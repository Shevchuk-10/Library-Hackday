from PyPDF2 import PdfReader

def get_pdf_metadata(path):
    reader = PdfReader(path)
    return reader.metadata
