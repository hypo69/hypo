## \file hypotez/launchers/discord.ps1
# -*- coding: utf-8 -*-

""" module: launchers """
MODE = 'debug'
# Укажите путь к файлу Python, который вы хотите запустить
$pythonScriptPath = "src\openai\bots\discord_bot_trainger.py"


# Запустите Python скрипт
python $pythonScriptPath