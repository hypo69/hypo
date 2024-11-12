## \file hypotez/src/endpoints/kazarinov/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.endpoints.kazarinov """

...
from packaging.version import Version
from .version import __version__, __doc__, __details__  

from .hypo69_kazarinov_bot import KazarinovTelegramBot
from .gemini_chat import chat
from .scenarios import  Mexiron
from .react import ReportGenerator

