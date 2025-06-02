import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import io
from pdf2image import convert_from_bytes
from app.services.text_cleaner import clean_text
from app.services.text_splitter import split_text

def extract_text_from_images(images):
    """Perform OCR on a list of PIL images."""
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image) + "\n"
    return text

def process_pdf(file_bytes: bytes) -> str:
    # Try extracting text normally
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    extracted_text = ""
    
    for page in doc:
        text = page.get_text()
        if text.strip():
            extracted_text += text
        else:
            # If no text, use OCR on the page image
            pix = page.get_pixmap()
            image = Image.open(io.BytesIO(pix.tobytes()))
            extracted_text += pytesseract.image_to_string(image) + "\n"
    
    # If the whole document is image-based (no text at all)
    if not extracted_text.strip():
        # Use pdf2image to convert all pages and OCR them
        images = convert_from_bytes(file_bytes)
        extracted_text = extract_text_from_images(images)

    raw_text = extracted_text  # from PyMuPDF or OCR

    cleaned = clean_text(raw_text)
    chunks = split_text(cleaned)

    return chunks
