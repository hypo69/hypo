## \file hypotez/src/suppliers/aliexpress/_experiments/affiliate_links_shortener.py
# -*- coding: utf-8 -*-

""" module: src.suppliers.aliexpress._experiments """
MODE = 'debug'
""" module: src.suppliers.aliexpress._experiments """
MODE = 'debug'

""" Short affiliate links """

import header
from src.suppliers.aliexpress import AffiliateLinksShortener

a = AffiliateLinksShortener()
url = 'https://aliexpress.com'
link = a.short_affiliate_link(url)
...