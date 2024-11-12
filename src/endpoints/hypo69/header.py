## \file hypotez/src/endpoints/hypo69/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.endpoints.hypo69 """
"""module: `src.endpoints.hypo69`"""
from pathlib import Path
import sys

src_path = str(Path(__file__).resolve().parent.parent.parent.parent)

if src_path not in sys.path:
    sys.path.append(src_path)
