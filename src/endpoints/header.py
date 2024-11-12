## \file hypotez/src/endpoints/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.endpoints """
""" module `src.endpoints` """
...

from pathlib import Path
import sys

src_path = str(Path().resolve().parent.parent.parent)

if src_path not in sys.path:
    sys.path.append(src_path)

from src import gs
