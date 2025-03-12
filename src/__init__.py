## \file /src/__init__.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: src 
	:platform: Windows, Unix
	:synopsis:

Root of the project.
========================================================================================
•	USE_ENV:bool: Переменная, которая определяет, откуда читать секреты: API-ключи и т.д. 
•	Если USE_ENV равно True, модуль gs будет импортирован из gs.py, а секреты будут читаться из файлов .env.
•	Если USE_ENV равно False, модуль gs будет импортирован из credentials.py. и секреты будут читаться из объекта gs. (например, `token = gs.path.telegram.kazarinov_bot`)
"""


USE_ENV:bool = False

if USE_ENV:
	from .gs import gs
else:
	from .credentials import gs