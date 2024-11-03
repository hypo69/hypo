## \file ../header.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""! Absolute path to modules and GTK bin directory setup """

import sys
from pathlib import Path

# Корневой путь к проекту
__root__: Path = Path.cwd().resolve().parents[Path.cwd().parts.index('hypotez')]
sys.path.append(str(__root__))

# Пути к bin-директориям
gtk_bin_path = __root__ / "bin" / "gtk" / "gtk-nsis-pack" / "bin"
ffmpeg_bin_path = __root__ / "bin" / "ffmpeg" / "bin"
graphviz_bin_path = __root__ / "bin" / "graphviz" / "bin"

# Обновление переменной PATH, если пути отсутствуют
paths_to_add = [gtk_bin_path, ffmpeg_bin_path, graphviz_bin_path]
current_paths = set(Path(p) for p in sys.path)

for bin_path in paths_to_add:
    if bin_path not in current_paths:
        sys.path.insert(0, str(bin_path))

# Установка переменной для WeasyPrint
sys_path_env_var = "WEASYPRINT_DLL_DIRECTORIES"
if sys_path_env_var not in sys.path:
    sys.path.insert(0, str(gtk_bin_path))

"""Подавление вывода GTK логов в консоль"""

import warnings
warnings.filterwarnings("ignore", category=UserWarning)
