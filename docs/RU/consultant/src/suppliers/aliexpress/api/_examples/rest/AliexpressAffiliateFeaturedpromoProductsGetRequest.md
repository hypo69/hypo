# Received Code

```python
## \file hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateFeaturedpromoProductsGetRequest.py
# -*- coding: utf-8 -*-\
 # <- venv win
## ~~~~~~~~~~~~~~~
""" module: src.suppliers.aliexpress.api._examples.rest """
'''
Created by auto_sdk on 2021.05.17
'''
from ..base import RestApi
class AliexpressAffiliateFeaturedpromoProductsGetRequest(RestApi):
	def __init__(self, domain="api-sg.aliexpress.com", port=80):
		RestApi.__init__(self,domain, port)
		self.app_signature = None
		self.category_id = None
		self.country = None
		self.fields = None
		self.page_no = None
		self.page_size = None
		self.promotion_end_time = None
		self.promotion_name = None
		self.promotion_start_time = None
		self.sort = None
		self.target_currency = None
		self.target_language = None
		self.tracking_id = None

	def getapiname(self):
		return 'aliexpress.affiliate.featuredpromo.products.get'
```

# Improved Code

```python
## \file hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateFeaturedpromoProductsGetRequest.py
# -*- coding: utf-8 -*-\
 # <- venv win
## ~~~~~~~~~~~~~~~
""" Модуль для запроса списка продуктов с выделенными промоакциями на AliExpress. """
'''
Создан автоматически 2021.05.17
'''
from ..base import RestApi
from src.logger import logger
from src.utils.jjson import j_loads, j_loads_ns # Импорт функций для работы с JSON

class AliexpressAffiliateFeaturedpromoProductsGetRequest(RestApi):
    """ Класс для запроса списка продуктов с выделенными промоакциями. """

    def __init__(self, domain="api-sg.aliexpress.com", port=80):
        """
        Инициализирует объект запроса.

        :param domain: Домен API.
        :param port: Порт API.
        """
        super().__init__(domain, port) # Использование super() для вызова конструктора родительского класса
        self.app_signature = None
        self.category_id = None
        self.country = None
        self.fields = None
        self.page_no = None
        self.page_size = None
        self.promotion_end_time = None
        self.promotion_name = None
        self.promotion_start_time = None
        self.sort = None
        self.target_currency = None
        self.target_language = None
        self.tracking_id = None

    def getapiname(self) -> str:
        """
        Возвращает имя API-метода.

        :return: Имя API-метода.
        """
        return 'aliexpress.affiliate.featuredpromo.products.get'
```

# Changes Made

*   Добавлен импорт `logger` из `src.logger`.
*   Добавлен импорт `j_loads` и `j_loads_ns` из `src.utils.jjson`.
*   Комментарии переписаны в формате RST.
*   Добавлены docstring к методам и классу в формате RST.
*   Использование `super()` для инициализации родительского класса.
*   Добавлены типы возвращаемых значений.
*   Комментарии с использованием правильного стиля RST.
*   Изменён стиль импорта, для удобства чтения.


# FULL Code

```python
## \file hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateFeaturedpromoProductsGetRequest.py
# -*- coding: utf-8 -*-\
 # <- venv win
## ~~~~~~~~~~~~~~~
""" Модуль для запроса списка продуктов с выделенными промоакциями на AliExpress. """
'''
Создан автоматически 2021.05.17
'''
from ..base import RestApi
from src.logger import logger
from src.utils.jjson import j_loads, j_loads_ns # Импорт функций для работы с JSON

class AliexpressAffiliateFeaturedpromoProductsGetRequest(RestApi):
    """ Класс для запроса списка продуктов с выделенными промоакциями. """

    def __init__(self, domain="api-sg.aliexpress.com", port=80):
        """
        Инициализирует объект запроса.

        :param domain: Домен API.
        :param port: Порт API.
        """
        super().__init__(domain, port) # Использование super() для вызова конструктора родительского класса
        self.app_signature = None
        self.category_id = None
        self.country = None
        self.fields = None
        self.page_no = None
        self.page_size = None
        self.promotion_end_time = None
        self.promotion_name = None
        self.promotion_start_time = None
        self.sort = None
        self.target_currency = None
        self.target_language = None
        self.tracking_id = None

    def getapiname(self) -> str:
        """
        Возвращает имя API-метода.

        :return: Имя API-метода.
        """
        return 'aliexpress.affiliate.featuredpromo.products.get'