## \file ./src/endpoints/prestashop/_experiments/suppliers/hb/header.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
#! /usr/bin/python
# /path/to/interpreter/python
import json
from pathlib import Path
import sys
import os
from attr import attr, attrs
from typing import Union
hypotez_root_path = os.getcwd()[:os.getcwd().rfind(r'hypotez')+7]
sys.path.append(hypotez_root_path)  # Добавляю корневую папку в sys.path

# ---------------------------------
from src import gs
from src.utils import  pprint


# ------------------------------------