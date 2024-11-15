## \file hypotez/src/gui/context_menu/run.ps1
# -*- coding: utf-8 -*-

""" module: src.gui.context_menu """
MODE = 'debug'
# Определяем текущий путь
$currentPath = (Get-Location).Path


# Путь к Python-скрипту (в корне 'hypotez')
$scriptPath = Join-Path -Path $currentPath -ChildPath "main.py"

# Запускаем скрипт с правами администратора
Start-Process powershell -Verb runAs -ArgumentList "python `"$scriptPath`""
