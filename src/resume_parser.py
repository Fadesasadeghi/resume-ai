from pypdf import PdfReader


def extract_text_from_pdf(pdf_file):
    """
    Extract text from an uploaded PDF resume.
    """

    reader = PdfReader(pdf_file)

    text = []

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text.append(page_text)

    return "\n".join(text).strip()
