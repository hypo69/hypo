## \file /src/endpoints/hypo69/code_assistant/pdf2html.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3
"""
Конвертация pdf 2 html
=========================================================================================
"""
import header
from src import gs
from src.utils.pdf import PDFUtils

def pdf2html(pdf_file,html_file):
    """ """
    PDFUtils.pdf_to_html(pdf_file, html_file)

pdf_file = gs.path.root / 'assets' / 'materials' / '101_BASIC_Computer_Games_Mar75.pdf'
html_file = gs.path.root / 'assets' / 'materials' / '101_BASIC_Computer_Games_Mar75.html'


pdf2html(pdf_file, html_file)

