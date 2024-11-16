## \file hypotez/src/endpoints/kazarinov/resources/compile.ps1
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.endpoints.kazarinov.resources """
MODE = 'debug'
pyinstaller --onefile --name kazarinov_bot --add-data "../resources/*;."  --distpath "..\..\.." "..\bot.py"
