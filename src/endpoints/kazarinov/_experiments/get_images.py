## \file hypotez/src/endpoints/kazarinov/_experiments/get_images.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.endpoints.kazarinov._experiments """
MODE = 'debug'
""" module: src.endpoints.kazarinov._experiments """
MODE = 'debug'
"""! HERE SHOULD BE A DESCRIPTION OF THE MODULE OPERATION ! """

import header
from src import gs
from src.utils.file import read_text_file, save_text_file, recursively_get_filepath
from src.utils.printer import pprint

images_path = recursively_get_filepath(gs.path.google_drive / 'kazarinov' / 'converted_images' / 'pastel', ['*.jpeg','*.jpg','*.png'])
pprint(images_path)
...