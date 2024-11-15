## \file hypotez/src/suppliers/aliexpress/api/skd/api/rest/AliexpressAffiliateLinkGenerateRequest.py
# -*- coding: utf-8 -*-

""" module: src.suppliers.aliexpress.api.skd.api.rest """
MODE = 'debug'
""" module: src.suppliers.aliexpress.api.skd.api.rest """
MODE = 'debug'
"""
Created by auto_sdk on 2020.03.09
"""
from ..base import RestApi


class AliexpressAffiliateLinkGenerateRequest(RestApi):
    def __init__(self, domain="api-sg.aliexpress.com", port=80):
        RestApi.__init__(self, domain, port)
        self.app_signature = None
        self.promotion_link_type = None
        self.source_values = None
        self.tracking_id = None

    def getapiname(self):
        return "aliexpress.affiliate.link.generate"

