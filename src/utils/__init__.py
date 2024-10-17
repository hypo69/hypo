## \file ../src/utils/__init__.py
## \file ../src/utils/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""
# tiny_utils Module

The `tiny_utils` module is a collection of small, useful utilities designed to simplify common programming tasks. It includes tools for data conversion, file handling, and formatted output. This module helps streamline coding by providing straightforward and reusable functions.
"""

from packaging.version import Version
from .version import __version__, __doc__, __details__

from .convertors import (xml2dict, 
                        base64_to_tmpfile,
                        base64encode,
                        csv2dict, 
                        csv2ns, 
                        dict2csv, 
                        dict2html, 
                        dict2ns, 
                        dict2xls, 
                        dict2xml, 
                        html2dict, 
                        html2ns, 
                        html2escape, 
                        html2text,
                        html2text_file,
                        escape2html, 
                        extract_json_from_md,
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
                        xls2dict,
                        webp2png,
                        ) 


from .printer import  pprint

from .jjson import (j_loads, 
                    j_loads_ns, 
                    j_dumps,
                    )

from .file import (get_directory_names, 
                    get_filenames, 
                    read_text_file, 
                    save_text_file, 
                    recursive_get_filenames,
                    recursive_read_text_files,
                    )

from .image import (save_png, 
                    save_png_from_url
                    )

from .input import input

from .video import save_video_from_url
from .date_time import TimeoutCheck

from .csv import (read_csv_file, 
                  read_csv_as_dict, 
                  read_csv_as_ns, 
                  save_csv_file,
                    )
from .string import (extract_url_params, 
                     is_url,
                    )

