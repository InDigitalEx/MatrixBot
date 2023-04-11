import os
import time

from aiogram.types.input_file import InputFile

from bot.parser.download import download_matrix
from bot.misc import get_root_dir, convert_pdf_to_image


def parse_matrix(user_name: str, user_date: str, user_gender: str) -> None:
    download_matrix(user_name, user_date, user_gender)
    time.sleep(3)
    convert_pdf_to_image(f"{get_root_dir()}/temp", "диаграмма.pdf", "output")
    os.remove(f"{get_root_dir()}/temp/диаграмма.pdf")


def get_matrix_photo(user_name: str, user_date: str, user_gender: str) -> InputFile:
    parse_matrix(user_name, user_date, user_gender)
    return InputFile(f"{get_root_dir()}/temp/output.jpg", 'rb')


async def delete_matrix_temp() -> None:
    os.remove(f"{get_root_dir()}/temp/output.jpg")

