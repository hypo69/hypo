#! /usr/bin/python
﻿""" Темплейты даля создания новых сущностей (новый поставщик) 

@todo
    1. получить данные:
        - имя поставщика. Например, `aliexpress`
        - вебсайт поставщика. 
        - имя/пароль (если требуются для входа на сайт)
    1. создать диркторию поставщика в директории `src.suppliers`
обновить записи в престашоп и гугл таблице
"""
...
## \file /src/ai/openai/model/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

from packaging.version import Version
from .version import __version__, __doc__, __details__ 

from .training import OpenAIModel



