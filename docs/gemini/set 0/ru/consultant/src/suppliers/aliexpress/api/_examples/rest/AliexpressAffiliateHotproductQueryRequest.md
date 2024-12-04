# Received Code

```python
## \file hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateHotproductQueryRequest.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~~~
""" module: src.suppliers.aliexpress.api._examples.rest """

'''
Created by auto_sdk on 2021.05.20
'''
from ..base import RestApi
class AliexpressAffiliateHotproductQueryRequest(RestApi):
	def __init__(self, domain="api-sg.aliexpress.com", port=80):
		RestApi.__init__(self,domain, port)
		self.app_signature = None
		self.category_ids = None
		self.delivery_days = None
		self.fields = None
		self.keywords = None
		self.max_sale_price = None
		self.min_sale_price = None
		self.page_no = None
		self.page_size = None
		self.platform_product_type = None
		self.ship_to_country = None
		self.sort = None
		self.target_currency = None
		self.target_language = None
		self.tracking_id = None

	def getapiname(self):
		return 'aliexpress.affiliate.hotproduct.query'

```

# Improved Code

```python
## \file hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateHotproductQueryRequest.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~~~
""" Модуль для запроса горячих товаров на AliExpress через API. """

from ..base import RestApi
from src.utils.jjson import j_loads, j_loads_ns
from src.logger import logger

class AliexpressAffiliateHotproductQueryRequest(RestApi):
    """
    Класс для отправки запроса на получение горячих товаров на AliExpress.

    :param domain: Домен API. По умолчанию "api-sg.aliexpress.com".
    :param port: Порт API. По умолчанию 80.
    """
    def __init__(self, domain="api-sg.aliexpress.com", port=80):
        """
        Инициализирует запрос к API AliExpress.
        
        :param domain: Домен API.
        :param port: Порт API.
        """
        RestApi.__init__(self, domain, port)
        # Параметры запроса
        self.app_signature = None
        self.category_ids = None
        self.delivery_days = None
        self.fields = None
        self.keywords = None
        self.max_sale_price = None
        self.min_sale_price = None
        self.page_no = None
        self.page_size = None
        self.platform_product_type = None
        self.ship_to_country = None
        self.sort = None
        self.target_currency = None
        self.target_language = None
        self.tracking_id = None

    def getapiname(self) -> str:
        """
        Возвращает имя API-метода.

        :return: Имя API-метода.
        """
        return 'aliexpress.affiliate.hotproduct.query'
```

# Changes Made

*   Добавлен импорт `j_loads` и `j_loads_ns` из `src.utils.jjson`.
*   Добавлен импорт `logger` из `src.logger`.
*   Добавлена документация в формате RST к классу `AliexpressAffiliateHotproductQueryRequest` и методу `__init__`, `getapiname`.
*   Комментарии переписаны в формате RST.
*   Переменные `domain` и `port` теперь имеют описания в комментариях.
*   Изменен стиль комментариев.
*   Убраны лишние комментарии.

# FULL Code

```python
## \file hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateHotproductQueryRequest.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~~~
""" Модуль для запроса горячих товаров на AliExpress через API. """

from ..base import RestApi
from src.utils.jjson import j_loads, j_loads_ns
from src.logger import logger

class AliexpressAffiliateHotproductQueryRequest(RestApi):
    """
    Класс для отправки запроса на получение горячих товаров на AliExpress.

    :param domain: Домен API. По умолчанию "api-sg.aliexpress.com".
    :param port: Порт API. По умолчанию 80.
    """
    def __init__(self, domain="api-sg.aliexpress.com", port=80):
        """
        Инициализирует запрос к API AliExpress.
        
        :param domain: Домен API.
        :param port: Порт API.
        """
        RestApi.__init__(self, domain, port)
        # Параметры запроса
        self.app_signature = None
        self.category_ids = None
        self.delivery_days = None
        self.fields = None
        self.keywords = None
        self.max_sale_price = None
        self.min_sale_price = None
        self.page_no = None
        self.page_size = None
        self.platform_product_type = None
        self.ship_to_country = None
        self.sort = None
        self.target_currency = None
        self.target_language = None
        self.tracking_id = None

    def getapiname(self) -> str:
        """
        Возвращает имя API-метода.

        :return: Имя API-метода.
        """
        return 'aliexpress.affiliate.hotproduct.query'