import fitz


def extract_pdf_data(contents: bytes):

    document = fitz.open(
        stream=contents,
        filetype="pdf"
    )

    lines = []

    for page_number, page in enumerate(document):

        blocks = page.get_text("dict")["blocks"]

        for block in blocks:

            if "lines" not in block:
                continue

            for line in block["lines"]:

                spans = line["spans"]

                if not spans:
                    continue

                text = "".join(
                    span["text"]
                    for span in spans
                ).strip()

                if not text:
                    continue

                font_size = max(
                    span["size"]
                    for span in spans
                )

                fonts = [
                    span["font"]
                    for span in spans
                ]

                is_bold = any(
                    "bold" in font.lower()
                    for font in fonts
                )

                lines.append({
                    "text": text,
                    "font_size": font_size,
                    "fonts": fonts,
                    "is_bold": is_bold,
                    "page": page_number
                })

    document.close()

    return lines