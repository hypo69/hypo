#! /usr/bin/python
﻿## \file src/bots/__init__.py
## \file /src/endpoints/bots/discord/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

from packaging.version import Version
from .version import __version__, __doc__, __details__ 

from .telegram_bot import TelegramBot



