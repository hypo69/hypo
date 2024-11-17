


...

import sys
import os
import json
import warnings
from pathlib import Path


# Suppress GTK log output to the console
warnings.filterwarnings("ignore", category=UserWarning)

def get_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """!
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    current_path = Path(__file__).resolve().parent
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            return parent
    return current_path


# Define project root
__root__: Path = get_project_root()

# Add project root to `sys.path`
if str(__root__) not in sys.path:
    sys.path.append(str(__root__))

# Get the root directory of the project
__root__: Path = get_project_root()
"""__root__ (Path): Path to the root directory of the project"""

# Define the path to the GTK binary directory
gtk_bin_path: Path = __root__ / 'bin' / 'gtk' / 'gtk-nsis-pack' / 'bin'
"""gtk (Path): Path to the GTK binaries directory"""

# Define the path to the FFmpeg binary directory
ffmpeg_bin_path: Path = __root__ / 'bin' / 'ffmpeg' / 'bin'
"""ffmpeg (Path): Path to the FFmpeg binaries directory"""

# Define the path to the Graphviz binary directory
graphviz_bin_path: Path = __root__ / 'bin' / 'graphviz' / 'bin'
"""graphviz (Path): Path to the Graphviz binaries directory"""

# Define the path to the wkhtmltopdf binary directory
wkhtmltopdf_bin_path: Path = __root__ / 'bin' / 'wkhtmltopdf' / 'files' / 'bin'
"""wkhtmltopdf (Path): Path to the wkhtmltopdf binaries directory"""

# Update the PATH variable if the paths are missing
paths_to_add = [__root__, gtk_bin_path, ffmpeg_bin_path, graphviz_bin_path, wkhtmltopdf_bin_path]

for bin_path in paths_to_add:
    if bin_path not in sys.path:
        sys.path.insert(0, str(bin_path))

# Set environment variables
os.environ['WEASYPRINT_DLL_DIRECTORIES'] = str(gtk_bin_path)

from packaging.version import Version
#from .version import __version__, __doc__, __details__  

from .csv import (
                    csv2dict, 
                    csv2ns,
                    )

from .dict import ( dict2ns, 
                    dict2xls, 
                    dict2xml, 
                    dict2csv,
                    dict2html
                    )

from .html import (
                    html2escape, 
                    html2ns, 
                    html2dict, 
                    escape2html,
                    ) 

from .html2text import (
                    html2text,
                    html2text_file,
                    google_fixed_width_font,
                    google_has_height,
                    google_list_style,
                    google_nest_count,
                    google_text_emphasis,
                    dumb_css_parser,
                    dumb_property_dict,
                    dumb_property_dict,
                    
                    )

from .json import (
                    json2csv, 
                   json2ns, 
                   json2xls, 
                   json2xml
                    )

from .ns import (
                    ns2csv, 
                    ns2dict, 
                    ns2json, 
                    ns2xls, 
                    ns2xml
                    )

from .md2dict import (
                    md2dict, 
                    
                      )

from .xls import xls2dict
from .xml2dict import xml2dict  

from .base64 import (
                    base64_to_tmpfile,
                    base64encode,
                    )

from .png import (TextToImageGenerator, 
                  webp2png, 
                    )

from .tts import (
                    speech_recognizer, 
                    text2speech,
                )
from .dot import dot2png


