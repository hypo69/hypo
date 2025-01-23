## \file /src/endpoints/kazarinov/_experiments/get_images.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3
"""
Список картинок, сгенерированный ИИ
====================================

.. module:: src.endpoints.kazarinov._experiments 
	:platform: Windows, Unix
	:synopsis:

"""


import header
from src import gs
from src.utils.file import read_text_file, save_text_file, recursively_get_filepath
from src.utils.printer import pprint

images_path = recursively_get_filepath(gs.path.external_data / 'kazarinov' / 'converted_images' / 'pastel', ['*.jpeg','*.jpg','*.png'])
pprint(images_path)
...