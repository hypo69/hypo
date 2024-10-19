## \file ../src/utils/convertors/_experiments/html2text.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! HERE SHOULD BE A DESCRIPTION OF THE MODULE OPERATION ! """

import header
from src import gs
from src.utils.convertors import html2text, html2text_file
from src.utils.file import read_text_file, save_text_file

html = read_text_file(gs.path.data / 'html2text' / 'index.html')
text_from_html = html2text(html)
save_text_file(text_from_html, gs.path.data / 'html2text' / 'index.txt')
...