## \file hypotez/src/db/_experiments/ide_experiments_connection.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.db._experiments """
""" @namespace src.db._experiments """
import header
from header import gs

credentials = gs.db_translations_credentials

connection_string = {
        "user": credentials['username'],
        "password": credentials['password'],
        "server": credentials['server'],
        "port": credentials['port'],
        "database": credentials['db_name']
  }}