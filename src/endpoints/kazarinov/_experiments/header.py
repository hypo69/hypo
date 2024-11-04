## \file header.py
## \file ../src/endpoints/kazarinov/_experiments/header.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""! Absolute path to modules and GTK bin directory setup """

import sys
import os
from pathlib import Path

#  корневой путь к проекту
__root__: Path = Path(os.getcwd()[:os.getcwd().rfind(r'hypotez') + 7])
sys.path.append(str(__root__))


gtk_bin_path = fr"{__root__}/bin/gtk/gtk-nsis-pack/bin" 
ffmpeg_bin_path = fr"{__root__}/bin/ffmpeg/bin" 
graphviz_bin_path = fr"{__root__}/bin/graphviz/bin" 

if gtk_bin_path not in os.environ["PATH"]:
    os.environ["PATH"] = gtk_bin_path + os.pathsep + os.environ["PATH"]

if ffmpeg_bin_path not in os.environ["PATH"]:
    os.environ["PATH"] = ffmpeg_bin_path + os.pathsep + os.environ["PATH"]

if graphviz_bin_path not in os.environ["PATH"]:
    os.environ["PATH"] = graphviz_bin_path + os.pathsep + os.environ["PATH"]

os.environ['WEASYPRINT_DLL_DIRECTORIES'] = gtk_bin_path
