import fitz  # PyMuPDF
import os
import sys

def save_pages_as_svg(pdf_path, output_folder):
    doc = fitz.open(pdf_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        svg_filename = f"page_{page_num + 1}.svg"
        svg_full_path = os.path.join(output_folder, svg_filename)
        svg_content = page.get_svg_image()

        with open(svg_full_path, "w") as svg_file:
            svg_file.write(svg_content)
        print(f"Saved {svg_full_path}")

def main(pdf_path, output_folder):
    print(f"Processing PDF: {pdf_path}")
    save_pages_as_svg(pdf_path, output_folder)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 pdf_extractor.py [pdf_file_path] [output_folder_path]")
    else:
        pdf_path = sys.argv[1]
        output_folder = sys.argv[2]
        main(pdf_path, output_folder)
