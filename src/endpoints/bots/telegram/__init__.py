## \file hypotez/src/bots/telegram/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.bots.telegram 
	:platform: Windows, Unix
	:synopsis:

"""


from .bot_long_polling import TelegramBot  as TelegamLongPoolingBot
from .bot_web_hooks import TelegramBot as TelegramWebHooksBot
