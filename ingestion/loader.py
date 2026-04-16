from io import BytesIO
from PyPDF2 import PdfReader


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