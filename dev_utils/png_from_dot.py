## \file hypotez/dev_utils/png_from_dot.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: dev_utils """
# /path/to/interpreter/python
""" HERE MUST BE DESCRIPTION OF MODULE """
import os

def generate_image_links(folder_path):
    """!
    Генерирует список изображений в Markdown для всех файлов из указанной папки.

    Args:
        folder_path (str): Путь к папке с изображениями.

    Returns:
        str: Строка с изображениями в формате Markdown.
    """
    markdown_images = ""
    for filename in os.listdir(folder_path):
        if filename.endswith((".png", ".jpg", ".jpeg", ".gif")):  # Указываем нужные расширения
            markdown_images += f"![Описание {filename}]({folder_path}/{filename})\n"
    return markdown_images

# Укажите путь к папке dia
folder_path = "__root__/dia"
markdown_output = generate_image_links(folder_path)
print(markdown_output)