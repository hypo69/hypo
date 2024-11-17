


"""
module: `src.utils`
# tiny_utils Module

The `tiny_utils` module is a collection of small, useful utilities designed to simplify common programming tasks. 
It includes tools for data conversion, file handling, and formatted output. 
This module helps streamline coding by providing straightforward and reusable functions.
"""

import sys
import os
import json
import warnings
from pathlib import Path
import sys
from pathlib import Path
def get_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """!
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Get the root directory of the project
__root__: Path = get_project_root()
"""__root__ (Path): Path to the root directory of the project"""
#from src import gs

from packaging.version import Version
from .version import (
    __version__,
    __doc__,
    __details__
)



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

# Import utilities
from .convertors import (
    base64_to_tmpfile,
    base64encode,
    csv2dict,
    csv2ns,
    dict2csv,
    dict2html,
    dict2ns,
    dict2xls,
    dict2xml,
    dot2png,
    escape2html,
    html2dict,
    html2escape,
    html2ns,
    html2text,
    html2text_file,
    json2csv,
    json2ns,
    json2xls,
    json2xml,
    md2dict,
    ns2csv,
    ns2dict,
    ns2json,
    ns2xls,
    ns2xml,
    speech_recognizer,
    TextToImageGenerator,
    text2speech,
    webp2png,
    xls2dict
)

from .csv import (
    read_csv_as_dict,
    read_csv_as_ns,
    read_csv_file,
    save_csv_file
)

from .date_time import (
    TimeoutCheck
)

from .file import (
    get_directory_names,
    get_filenames,
    read_text_file,
    recursively_get_filenames,
    recursively_read_text_files,
    save_text_file,
    recursively_yield_file_path,  
    remove_bom
)


from .image import (
    save_png_from_url,
    save_png,
  )

from .jjson import (
    j_dumps,
    j_loads,
    j_loads_ns,
    replace_key_in_json
)

from .pdf import (
    PDFUtils
)

from .printer import (
    pprint
)

from .string import (
    ProductFieldsValidator,
    StringFormatter,
    StringNormalizer,
    extract_url_params,
    is_url
)

from .video import (
    save_video_from_url
)
