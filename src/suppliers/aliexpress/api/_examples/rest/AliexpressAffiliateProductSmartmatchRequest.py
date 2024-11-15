## \file hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateProductSmartmatchRequest.py
# -*- coding: utf-8 -*-

""" module: src.suppliers.aliexpress.api._examples.rest """
MODE = 'debug'
""" module: src.suppliers.aliexpress.api._examples.rest """
MODE = 'debug'
'''
Created by auto_sdk on 2021.05.17
'''
from ..base import RestApi
class AliexpressAffiliateProductSmartmatchRequest(RestApi):
	def __init__(self, domain="api-sg.aliexpress.com", port=80):
		RestApi.__init__(self,domain, port)
		self.app = None
		self.app_signature = None
		self.country = None
		self.device = None
		self.device_id = None
		self.fields = None
		self.keywords = None
		self.page_no = None
		self.product_id = None
		self.site = None
		self.target_currency = None
		self.target_language = None
		self.tracking_id = None
		self.user = None

	def getapiname(self):
		return 'aliexpress.affiliate.product.smartmatch'

