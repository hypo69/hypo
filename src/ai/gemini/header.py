## \file ./src/ai/gemini/header.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
#! /usr/bin/python
# /path/to/interpreter/python
from pathlib import Path
import sys

__root__ = Path('../../..').resolve()  # Получаем абсолютный путь к корню

if str(__root__) not in sys.path:
    sys.path.insert(0, str(__root__)) 


# Paths to bin directories
gtk_bin_path = __root__ / "bin" / "gtk" / "gtk-nsis-pack" / "bin"
ffmpeg_bin_path = __root__ / "bin" / "ffmpeg" / "bin"
graphviz_bin_path = __root__ / "bin" / "graphviz" / "bin"

# Update the PATH variable if the paths are missing
paths_to_add = [gtk_bin_path, ffmpeg_bin_path, graphviz_bin_path]
current_paths = set(Path(p) for p in sys.path)

for bin_path in paths_to_add:
    if bin_path not in current_paths:
        sys.path.insert(0, str(bin_path))

# Set the variable for WeasyPrint
sys_path_env_var = "WEASYPRINT_DLL_DIRECTORIES"


"""Suppress GTK log output to the console"""
import warnings
warnings.filterwarnings("ignore", category=UserWarning)