## \file hypotez/src/suppliers/aliexpress/_experiments/test_iop_get.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.suppliers.aliexpress._experiments 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""MODE = 'dev'
  
""" module: src.suppliers.aliexpress._experiments """



import iop

# http://api-sg.aliexpress.com/sync?method=aliexpress.solution.product.schema.get&app_key=12345678&aliexpress_category_id=200135143&access_token=test&timestamp=1517820392000&sign_method=sha256&sign=4190D32361CFB9581350222F345CB77F3B19F0E31D162316848A2C1FFD5FAB4A


# params 1 : gateway url
# params 2 : appkey
# params 3 : appSecret
client = iop.IopClient('https://api-sg.aliexpress.com/sync', '345846782', 'e1b26aac391d1bc3987732af93eb26aabc391d187732af93')
client.log_level = iop.P_LOG_LEVEL_DEBUG
## create a api request set GET mehotd
## default http method is POST
#requests = ['aliexpress.affiliate.link.generate',
#            'global.seller.brands.list',
#            'global.category.tree.list',
#            'aliexpress.affiliate.category.get',
#            'aliexpress.logistics.redefining.getlogisticsselleraddresses',
#            'aliexpress.solution.product.schema.get']

#request = iop.IopRequest(requests[0], 'GET')
##request.source_values = 'https://www.aliexpress.com/item/1005002376759769.html'
#request.set_simplify()
## simple type params ,Number ,String
##request.add_api_param('seller_address_query','pickup')
##request.add_api_param('aliexpress_category_id','200000346')
#request.add_api_param('locale', 'en-US')
#request.add_api_param('aliexpress_category_id', '100003070')


##access_token = "test"
#access_token = "default"
##response = client.execute(request,access_token)
#response = client.execute(request)

# response type nil,ISP,ISV,SYSTEM
# nil ：no error
# ISP : API Service Provider Error
# ISV : API Request Client Error
# SYSTEM : Iop platform Error
#client = iop.IopClient(url, appkey ,appSecret)
request = iop.IopRequest('aliexpress.affiliate.link.generate')
#request.add_api_param('app_signature', 'asdasdas')
request.add_api_param('promotion_link_type', '0')
request.add_api_param('source_values', 'https://www.aliexpress.com/item/1005005058280371.html')
request.add_api_param('tracking_id', 'default')
response = client.execute(request)

print(response.body)
print(response.type)

# response code, 0 is no error
print(response.code)

# response error message
print(response.message)

# response unique id
print(response.request_id)

# full response
print(response.body)
...
    

