## \file hypotez/src/suppliers/aliexpress/_experiments/affiliate_links_shortener.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.suppliers.aliexpress._experiments """
MODE = 'development'



""" Short affiliate links """

import header
from src.suppliers.aliexpress import AffiliateLinksShortener

a = AffiliateLinksShortener()
url = 'https://aliexpress.com'
link = a.short_affiliate_link(url)
...