﻿## \file ../src/suppliers/aliexpress/campaign/__init__.py
## \file ../src/suppliers/aliexpress/campaign/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" модули управления рекламной кампанией Aliexpress:
"""

from packaging.version import Version
from .version import __version__, __doc__, __details__ 

from .ali_campaign_editor import AliCampaignEditor
#from .gsheet import AliCampaignGoogleSheet
from .prepare_campaigns import  process_campaign, process_campaign_category, process_all_campaigns
#from .ali_campaign_editor_jupyter_widgets import JupyterCampaignEditorWidgets
from .html_generators import CategoryHTMLGenerator, ProductHTMLGenerator
