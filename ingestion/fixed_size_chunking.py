from io import BytesIO
import re
from PyPDF2 import PdfReader


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> list:

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def load_file(content: bytes, filename: str) -> str:

    if filename.endswith(".pdf"):
        reader = PdfReader(BytesIO(content))
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    elif filename.endswith(".txt"):
        return content.decode("utf-8")

    else:
        raise ValueError("Unsupported file type (only PDF/TXT allowed)")
