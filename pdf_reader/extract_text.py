import pdfplumber
import os


def extract_text_from_pdf(pdf_path, threshold=1.5):
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")

    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            prev_x = None
            prev_top = None
            line = ""
            for char in page.chars:
                x0 = char["x0"]
                top = char["top"]
                c = char["text"]

                # New line if vertical position changes significantly
                if prev_top is not None and abs(top - prev_top) > 3:
                    text += line.strip() + "\n"
                    line = ""

                # Add space if the horizontal gap exceeds threshold
                if prev_x is not None and (x0 - prev_x) > threshold:
                    line += " "
                line += c

                prev_x = char["x1"]
                prev_top = top

            text += line.strip() + "\n"
    return text


def save_text_to_file(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"Text saved to: {output_path}")
