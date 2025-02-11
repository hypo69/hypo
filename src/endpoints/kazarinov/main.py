## \file /src/endpoints/kazarinov/main.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: src.endpoints.kazarinov 
	:platform: Windows, Unix
	:synopsis:

"""
import asyncio
import header
from src.endpoints.kazarinov.minibot import main, MODE # <- Определяет режим разработчика. Если MODE=='PRODUCTION' будет запущен kazarionaov бот, иначе тестбот

if __name__ == "__main__":
	main()