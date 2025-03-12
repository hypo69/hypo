## \file /src/gs.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3
"""
.. module:: gemini_simplechat.src.gs
    :platform: Windows, Unix
    :synopsis: Загрузка параметров программы, если флаг USE_ENV, то загружаются переменные окружения из файлов .env

"""
import header
from header import __root__
from src.utils.jjson import j_loads_ns
from pathlib import Path

gs = j_loads_ns(__root__ / 'src' / 'config.json')