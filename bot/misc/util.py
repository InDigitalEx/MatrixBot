import os
import sys

from pdf2image import convert_from_path


def get_root_dir():
    try:
        file = os.path.abspath(sys.modules['__main__'].__file__)
    except:
        file = sys.executable
    return os.path.dirname(file)


def convert_pdf_to_image(path: str, file_name: str, output_name: str):
    pages = convert_from_path(f"{path}/{file_name}", 500, single_file=True)

    for page in pages:
        page.save(f"{path}/{output_name}.jpg", 'JPEG')
