import os
from parser import pdf_parser, docx_parser


def load_resume(filepath: str) -> str:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".pdf":
        return pdf_parser.extract_text(filepath)
    elif ext in (".docx", ".doc"):
        return docx_parser.extract_text(filepath)
    else:
        raise ValueError(f"Unsupported format: {ext}. Use PDF or DOCX.")
