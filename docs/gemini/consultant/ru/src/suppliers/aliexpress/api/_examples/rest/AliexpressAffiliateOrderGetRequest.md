# Received Code

```python
## \file hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderGetRequest.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~\n""" module: src.suppliers.aliexpress.api._examples.rest """
'''
Created by auto_sdk on 2021.03.05
'''
from ..base import RestApi
class AliexpressAffiliateOrderGetRequest(RestApi):
	def __init__(self, domain="api-sg.aliexpress.com", port=80):
		RestApi.__init__(self,domain, port)
		self.app_signature = None
		self.fields = None
		self.order_ids = None

	def getapiname(self):
		return 'aliexpress.affiliate.order.get'
```

# Improved Code

```python
## \file hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderGetRequest.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~\n""" module: src.suppliers.aliexpress.api._examples.rest """
'''
Created by auto_sdk on 2021.03.05
'''
from ..base import RestApi
from src.utils.jjson import j_loads, j_loads_ns
from src.logger import logger

class AliexpressAffiliateOrderGetRequest(RestApi):
    """
    Класс для запроса данных о заказах AliExpress.

    Этот класс наследуется от :class:`RestApi` и предоставляет методы для взаимодействия с API.
    """

    def __init__(self, domain="api-sg.aliexpress.com", port=80):
        """
        Инициализирует объект запроса.

        :param domain: Домен API.
        :param port: Порт API.
        """
        super().__init__(domain, port)  # Вызов конструктора родительского класса
        self.app_signature = None
        self.fields = None
        self.order_ids = None

    def getapiname(self) -> str:
        """
        Возвращает имя API-метода.

        :return: Имя API-метода.
        """
        return 'aliexpress.affiliate.order.get'
```

# Changes Made

*   Добавлен импорт `j_loads` и `j_loads_ns` из `src.utils.jjson`.
*   Добавлен импорт `logger` из `src.logger`.
*   Добавлена документация RST к классу `AliexpressAffiliateOrderGetRequest` и методу `getapiname` в формате Sphinx.
*   Метод `__init__` теперь использует `super().__init__` для вызова конструктора родительского класса.
*   Добавлены типы возвращаемых значений (`-> str`) для большей ясности.

# FULL Code

```python
## \file hypotez/src/suppliers/aliexpress/api/_examples/rest/AliexpressAffiliateOrderGetRequest.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~\n""" module: src.suppliers.aliexpress.api._examples.rest """
'''
Created by auto_sdk on 2021.03.05
'''
from ..base import RestApi
from src.utils.jjson import j_loads, j_loads_ns
from src.logger import logger

class AliexpressAffiliateOrderGetRequest(RestApi):
    """
    Класс для запроса данных о заказах AliExpress.

    Этот класс наследуется от :class:`RestApi` и предоставляет методы для взаимодействия с API.
    """

    def __init__(self, domain="api-sg.aliexpress.com", port=80):
        """
        Инициализирует объект запроса.

        :param domain: Домен API.
        :param port: Порт API.
        """
        super().__init__(domain, port)  # Вызов конструктора родительского класса
        self.app_signature = None
        self.fields = None
        self.order_ids = None

    def getapiname(self) -> str:
        """
        Возвращает имя API-метода.

        :return: Имя API-метода.
        """
        return 'aliexpress.affiliate.order.get'