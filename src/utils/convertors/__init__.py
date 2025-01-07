# ## \file /src/utils/convertors/__init__.py
# # -*- coding: utf-8 -*-
# 
# #! venv/bin/python/python3.12

# """
# .. module:: src.utils.convertors 
#     :platform: Windows, Unix
#     :synopsis:


    
# Модуль для конвертации различных форматов данных
# =========================================================================================

# Этот модуль содержит функции для конвертации между различными форматами данных, такими как
# CSV, JSON, XML, HTML, MD, Base64, а также для работы с изображениями и текстом. Он предоставляет
# утилиты для преобразования данных в словари, списки, форматы для работы с таблицами и т.д.

# Пример использования
# --------------------

# Пример использования функций модуля `src.utils.convertors`:

# .. code-block:: python

#     from src.utils.convertors import csv2dict, json2xls

#     # Преобразование CSV в словарь
#     csv_data = csv2dict('data.csv')

#     # Преобразование JSON в XLSX
#     json_data = json2xls('data.json')

# Функции модуля охватывают широкий спектр конвертаций, включая работу с изображениями (например,
# сгенерировать PNG изображение из текста), работу с аудио (речь в текст и наоборот), а также конвертацию
# между различными кодировками и форматами, такими как Base64.

# Доступные функции
# -----------------
# - Работа с CSV: конвертация из CSV в словарь или в пространство имен.
# - Работа с JSON: конвертация из JSON в другие форматы (CSV, XLSX, XML).
# - Работа с HTML: преобразование HTML в текст, создание словаря из HTML.
# - Работа с Base64: кодирование и декодирование данных в формат Base64.
# - Работа с изображениями: генерация изображений, конвертация PNG в WebP.
# - Работа с текстом: преобразование текста в речь и наоборот.

# Включенные форматы
# -------------------
# - CSV
# - JSON
# - XML
# - HTML
# - Markdown
# - Base64
# - PNG
# - WebP


# """
# 


# import json
# import os
# import sys
# import warnings
# from pathlib import Path

# from .base64 import (
#                     base64_to_tmpfile,
#                     base64encode,
#                     )

# from .csv import (
#                     csv2dict, 
#                     csv2ns,
#                     )

# from .dict import ( dict2ns, 
#                     dict2csv,
#                     dict2html,
#                     dict2xls, 
#                     dict2xml,
#                     replace_key_in_dict
#                     )

# from .dot import dot2png

# from .html import (
#                     html2escape, 
#                     html2ns, 
#                     html2dict, 
#                     escape2html,
#                     ) 

# from .html2text import (
#                     html2text,
#                     html2text_file,
#                     google_fixed_width_font,
#                     google_has_height,
#                     google_list_style,
#                     google_nest_count,
#                     google_text_emphasis,
#                     dumb_css_parser,
#                     dumb_property_dict,
#                     )

# from .json import (
#                     json2csv, 
#                     json2ns, 
#                     json2xls, 
#                     json2xml
#                     )

# from .md2dict import (
#                     md2dict, 
#                     )

# from .ns import (
#                     ns2csv, 
#                     ns2dict, 
#                     ns2xls, 
#                     ns2xml
#                     )

# from .png import (TextToImageGenerator, 
#                   webp2png, 
#                     )

# from .tts import (
#                     speech_recognizer, 
#                     text2speech,
#                 )

# from .unicode import decode_unicode_escape

# from .xml2dict import xml2dict  
# from .xls import xls2dict
