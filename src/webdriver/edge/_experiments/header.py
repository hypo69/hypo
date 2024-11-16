## \file hypotez/src/webdriver/edge/_experiments/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.webdriver.edge._experiments """
MODE = 'debug'
""" module: src.webdriver.edge._experiments """
MODE = 'debug'
import sys
import os
path = os.getcwd()[:os.getcwd().rfind(r'hypotez')+7]
sys.path.append(path)  # Добавляю корневую папку в sys.path

from src.webdriver.edge.edge import Edge, EdgeOptions, EdgeService, WebDriverExceptionn