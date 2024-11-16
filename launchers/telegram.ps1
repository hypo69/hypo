## \file hypotez/launchers/telegram.ps1
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: launchers """
MODE = 'debug'
# Укажите путь к файлу Python, который вы хотите запустить
$pythonScriptPath = "src\openai\bots\telegram_bot_trainger.py"


# Запустите Python скрипт
python $pythonScriptPath