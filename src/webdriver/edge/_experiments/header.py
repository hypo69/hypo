## \file ../src/webdriver/edge/_experiments/header.py
## \file src/webdriver/edge/_experiments/header.py
import sys
import os
path = os.getcwd()[:os.getcwd().rfind(r'hypotez')+7]
sys.path.append(path)  # Добавляю корневую папку в sys.path

from src.webdriver.edge.edge import Edge, EdgeOptions, EdgeService, WebDriverExceptionn