## \file hypotez/src/suppliers/chat_gpt/__init__.py
# -*- coding: utf-8 -*-

""" module: src.suppliers.chat_gpt """
MODE = 'debug'
""" module: src.suppliers.chat_gpt """
MODE = 'debug'

""" Веб интерфейс взаимодействия с chatGPT.
реализует логику получения диалога, радакцию в гугл таблицах и обучение модели
"""
...
from packaging.version import Version
from .version import __version__, __doc__, __details__ 

from .gsheet import GptGs
