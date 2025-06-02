import re

def clean_text(text: str) -> str:
    # Remove excessive whitespace and empty lines
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\n+', '\n', text)
    return text.strip()
