## \file /src/gs.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3
"""
.. module:: src.gs
    Загрузка параметров программы, если флаг USE_ENV
    ======================================================
    Этот модуль используется когде не требуется полная загрузка параметров из kepass.
    Ключи, пароли и т.п. загружаются переменные окружения из файлов .env
    объект `gs` идентичен тому, котроый создается в файле `credentials.py` но без параметра `credntilas`.  

"""
import header
from header import __root__
from src.utils.jjson import j_loads_ns
from pathlib import Path

gs = j_loads_ns(__root__ / 'src' / 'config.json')
"""Загружаю конфигурацию из файла.
Применяется тогда, когда нет файла credentials.kdbx
"""