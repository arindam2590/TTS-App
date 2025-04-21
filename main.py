import os
from pdf_reader.extract_text import extract_text_from_pdf, save_text_to_file


def main():
    filename = "sample"
    input_dir = "input/"
    output_dir = "output/"

    filename_ext = filename + ".pdf"
    input_pdf = input_dir + filename_ext
    output_txt = output_dir + filename + "_output.txt"

    if os.path.isfile(input_pdf):
        try:
            print(f"Reading PDF from: {filename_ext}")
            extracted_text = extract_text_from_pdf(input_pdf)

            print("Saving text to file...")
            save_text_to_file(extracted_text, output_txt)

        except Exception as e:
            print(f"Error during processing: {e}")
    else:
        print(f"File does not exist: {input_pdf}")


if __name__ == "__main__":
    main()
