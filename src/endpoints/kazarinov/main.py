## \file /src/endpoints/kazarinov/main.py
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

"""
.. module:: src.endpoints.kazarinov 
	:platform: Windows, Unix
	:synopsis:

"""
import asyncio
import header
from src.endpoints.kazarinov.kazarinov_bot import KazarinovTelegramBot

if __name__ == "__main__":
	bot = KazarinovTelegramBot()
	asyncio.run(bot.run())