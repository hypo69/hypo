# # -*- coding: utf-8 -*-
# 
# #! venv/bin/python/python3.12

# """
# Модуль для работы с утилитами
# =========================================================================================

# Этот модуль содержит набор небольших, полезных утилит, предназначенных для упрощения 
# повседневных задач программирования. Модуль включает инструменты для конвертации данных, 
# работы с файлами и формата вывода. Это позволяет ускорить разработку, предоставляя 
# простые и переиспользуемые функции.

# Пример использования
# --------------------

# Пример использования функций модуля `src.utils`:

# .. code-block:: python

#     from src.utils import csv2dict, json2xls, save_text_file

#     # Конвертация CSV в словарь
#     csv_data = csv2dict('data.csv')

#     # Конвертация JSON в XLSX
#     json_data = json2xls('data.json')

#     # Сохранение текста в файл
#     save_text_file('output.txt', 'Hello, World!')
# """

# 

# """ 
# Коллекция небольших утилит, предназначенных для упрощения часто выполняемых задач программирования.
# Включает инструменты для конвертации данных, работы с файлами и форматированного вывода.
# """

# # Импорты утилит в алфавитном порядке
# from .convertors import (
#     TextToImageGenerator,
#     base64_to_tmpfile,
#     base64encode,
#     csv2dict,
#     csv2ns,
#     decode_unicode_escape,
#     dict2csv,
#     dict2html,
#     dict2ns,
#     dict2xls,
#     dict2xml,
#     dot2png,
#     escape2html,
#     html2dict,
#     html2escape,
#     html2ns,
#     html2text,
#     html2text_file,
#     json2csv,
#     json2ns,
#     json2xls,
#     json2xml,
#     md2dict,
#     ns2csv,
#     ns2dict,
#     ns2xls,
#     ns2xml,
#     replace_key_in_dict,
#     speech_recognizer,
#     text2speech,
#     webp2png,
#     xls2dict
# )

# from .csv import (
#     read_csv_as_dict,
#     read_csv_as_ns,
#     read_csv_file,
#     save_csv_file
# )

# from .date_time import (
#     TimeoutCheck
# )

# from .file import (
#     get_directory_names,
#     get_filenames,
#     read_text_file,
#     recursively_get_file_path,
#     recursively_read_text_files,
#     recursively_yield_file_path,  
#     remove_bom,
#     save_text_file
# )

# from .image import (
#     save_image,
#     save_image_from_url,
#       random_image,
# )

# from .jjson import (
#     j_dumps,
#     j_loads,
#     j_loads_ns
# )

# from .pdf import (
#     PDFUtils
# )

# from .printer import (
#     pprint
# )

# from .string import (
#     ProductFieldsValidator,
#     StringFormatter,
#     normalize_string,
#     normalize_int,
#     normalize_float,
#     normalize_boolean
# )

# from .url import (
#     extract_url_params, 
#     is_url
# )

# from .video import (
#     save_video_from_url
# )

# from .path import get_relative_path
