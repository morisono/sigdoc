import os
import argparse
import tempfile
import fitz
from rich.progress import track
from PIL import Image

def convert_pdf_to_images(input_path, output_folder, dpi=300, page_range=None):
    images = []
    pdf_document = fitz.open(input_path)
    zoom = dpi / 72
    mat = fitz.Matrix(zoom, zoom)
    
    if page_range:
        page_numbers = parse_page_range(page_range, pdf_document.page_count)
    else:
        page_numbers = range(pdf_document.page_count)
    
    for page_number in track(page_numbers, description="Converting to images"):
        page = pdf_document[page_number]
        image = page.get_pixmap(matrix=mat)
        image_path = os.path.join(output_folder, f"page_{page_number + 1}.png")

        print(f"Converting page {page_number + 1} to {image_path}")

        pil_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
        pil_image.save(image_path)

        images.append(image_path)
    return images

def combine_images_to_pdf(image_paths, output_path):
    pdf_document = fitz.open()

    for image_path in track(image_paths, description="Combining images to PDF"):
        with fitz.open(image_path) as img:
            rect = img[0].rect
            pdfbytes = img.convert_to_pdf()
        page = pdf_document.new_page(width=rect.width, height=rect.height)
        page.show_pdf_page(rect, fitz.open('pdf', pdfbytes), 0)

        pdf_document.save(output_path)

def parse_page_range(page_range, total_pages):
    pages = set()
    for part in page_range.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            pages.update(range(start - 1, end))
        else:
            pages.add(int(part) - 1)
    return sorted(pages.intersection(range(total_pages)))

def main(input_path, output_path, dpi=300, page_range=None):
    temp_folder = tempfile.mkdtemp()

    image_paths = convert_pdf_to_images(input_path, temp_folder, dpi=dpi, page_range=page_range)
    combine_images_to_pdf(image_paths, output_path)

    for image_path in image_paths:
        os.remove(image_path)
    os.rmdir(temp_folder)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF to images and combine back to PDF.")
    parser.add_argument("input_path", help="Path to the input PDF file")
    parser.add_argument("output_path", help="Path to the output PDF file")
    parser.add_argument("--dpi", type=int, default=300, help="DPI (dots per inch), default is 300")
    parser.add_argument("--range", help="Page range to process, e.g., 1,2,4-7")
    args = parser.parse_args()

    main(args.input_path, args.output_path, dpi=args.dpi, page_range=args.range)
