## \file hypotez/src/endpoints/kazarinov/parser_onetab.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.endpoints.kazarinov """
MODE = 'development'

"""Модуль для парсинга URL из страницы OneTab."""


import requests
from bs4 import BeautifulSoup
from typing import Optional, List, Tuple
from src.utils import pprint
from src.logger import logger
from src import gs




