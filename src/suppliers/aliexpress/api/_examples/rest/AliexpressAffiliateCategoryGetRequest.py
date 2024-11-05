#! /usr/bin/python
## \file /src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateCategoryGetRequest.py
## \file src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateCategoryGetRequest.py
'''
Created by auto_sdk on 2020.03.09
'''
from ..base import RestApi
class AliexpressAffiliateCategoryGetRequest(RestApi):
	def __init__(self, domain="api-sg.aliexpress.com", port=80):
		RestApi.__init__(self,domain, port)
		self.app_signature = None

	def getapiname(self):
		return 'aliexpress.affiliate.category.get'

