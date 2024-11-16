## \file hypotez/src/suppliers/aliexpress/api/skd/api/rest/AliexpressAffiliateProductdetailGetRequest.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.suppliers.aliexpress.api.skd.api.rest """
MODE = 'debug'
""" module: src.suppliers.aliexpress.api.skd.api.rest """
MODE = 'debug'
"""
Created by auto_sdk on 2021.05.17
"""
from ..base import RestApi


class AliexpressAffiliateProductdetailGetRequest(RestApi):
    def __init__(self, domain="api-sg.aliexpress.com", port=80):
        RestApi.__init__(self, domain, port)
        self.app_signature = None
        self.country = None
        self.fields = None
        self.product_ids = None
        self.target_currency = None
        self.target_language = None
        self.tracking_id = None

    def getapiname(self):
        return "aliexpress.affiliate.productdetail.get"

