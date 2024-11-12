## \file hypotez/src/endpoints/bots/discord/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.endpoints.bots.discord """


from packaging.version import Version
from .version import __version__, __doc__, __details__ 

from .telegram_bot import TelegramBot



