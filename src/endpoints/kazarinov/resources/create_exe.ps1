## \file hypotez/src/endpoints/kazarinov/resources/create_exe.ps1
# -*- coding: utf-8 -*-

""" module: src.endpoints.kazarinov.resources """
MODE = 'debug'
#pyinstaller --onefile --name kazarinov_bot --add-data "../resources/*;." --add-data "icons/*;icons" --distpath ".." "..\bot.py"
pyinstaller --onefile --name kazarinov_bot --add-data "../resources/*;."  --distpath "..\..\..\exe\kazarinov" "..\bot.py"
