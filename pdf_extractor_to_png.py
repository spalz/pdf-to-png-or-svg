import fitz  # PyMuPDF
import os
import sys

def save_pages_as_png(pdf_path, output_folder, dpi=300):
    doc = fitz.open(pdf_path)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), alpha=True)
        png_filename = f"page_{page_num + 1}.png"
        png_full_path = os.path.join(output_folder, png_filename)

        pix.save(png_full_path)
        print(f"Saved {png_full_path}")

def main(pdf_path, output_folder):
    print(f"Processing PDF: {pdf_path}")
    save_pages_as_png(pdf_path, output_folder)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 pdf_to_png_converter.py [pdf_file_path] [output_folder_path]")
    else:
        pdf_path = sys.argv[1]
        output_folder = sys.argv[2]
        main(pdf_path, output_folder)