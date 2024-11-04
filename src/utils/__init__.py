## \file src/utils/__init__.py
## \file src/utils/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""
# tiny_utils Module

The `tiny_utils` module is a collection of small, useful utilities designed to simplify common programming tasks. 
It includes tools for data conversion, file handling, and formatted output. 
This module helps streamline coding by providing straightforward and reusable functions.
"""

from packaging.version import Version
from .version import __version__, __doc__, __details__

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
    text2png,
    text2speech,
    webp2png,
    xls2dict,
)

from .csv import (
    read_csv_as_dict,
    read_csv_as_ns,
    read_csv_file,
    save_csv_file,
)

from .date_time import TimeoutCheck

from .file import (
    get_directory_names,
    get_filenames,
    read_text_file,
    recursive_get_filenames,
    recursive_read_text_files,
    save_text_file,
)

from .image import (
    save_png,
    save_png_from_url,
)

from .jjson import (
    j_dumps,
    j_loads,
    j_loads_ns,
    replace_key_in_json,
)

from .pdf import save_pdf

from .printer import pprint

from .string import (
    ProductFieldsValidator,
    StringFormatter,
    StringNormalizer,
    extract_url_params,
    is_url,
)

from .video import save_video_from_url
