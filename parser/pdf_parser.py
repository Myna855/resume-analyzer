import re
from pypdf import PdfReader


def extract_text(filepath: str) -> str:
    reader = PdfReader(filepath)
    pages = [page.extract_text() or "" for page in reader.pages]
    text = "\n".join(pages)
    return re.sub(r"\n{3,}", "\n\n", text).strip()
