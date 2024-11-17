## \file hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateFeaturedpromoGetRequest.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.suppliers.aliexpress.api._examples.rest """
MODE = 'development'


'''
Created by auto_sdk on 2020.09.25
'''
from ..base import RestApi
class AliexpressAffiliateFeaturedpromoGetRequest(RestApi):
	def __init__(self, domain="api-sg.aliexpress.com", port=80):
		RestApi.__init__(self,domain, port)
		self.app_signature = None
		self.fields = None

	def getapiname(self):
		return 'aliexpress.affiliate.featuredpromo.get'

