from typing import List

def split_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50
) -> List[str]:
    words = text.split()
    chunks = []
    i = 0

    while i < len(words):
        chunk = words[i:i+chunk_size]
        chunks.append(' '.join(chunk))
        i += chunk_size - overlap  # slide with overlap

    return chunks
