## \file src/utils/convertors/__init__.py
## \file src/utils/convertors/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" Convertors
"""
...
from packaging.version import Version
from .version import __version__, __doc__, __details__  

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
from .webp2png import webp2png

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
from .text2png import TextToImageGenerator
from .tts import (
                    speech_recognizer, 
                    text2speech,
                )


