```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.endpoints.prestashop """

"""  Класс клиента в `Prestashop`"""
import sys
import os
from attr import attr, attrs
from pathlib import Path
from typing import Union
import json

# ----------------------------------
from __init__ import gs
from src.logger import logger
from src.utils import j_loads as j_loads
from .api import Prestashop
from src.logger.exceptions import PrestaShopException


@attrs
class PrestaCustomer(Prestashop):
    """
    Класс для работы с клиентами в PrestaShop.
    Наследуется от Prestashop.
    """

    def get_customer(self, customer_id: int) -> dict:
        """
        Возвращает данные клиента по ID.

        Args:
            customer_id: ID клиента.

        Returns:
            Словарь с данными клиента, или None если клиент не найден.
            Возвращает ошибку, если произошла ошибка API.
        """
        try:
            response = self.get(f"/customers/{customer_id}")
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                logger.warning(f"Клиент с ID {customer_id} не найден.")
                return None
            else:
                logger.error(f"Ошибка при получении данных клиента {customer_id}: {response.text}")
                raise PrestaShopException(f"Ошибка API: {response.status_code}")  # Поднять исключение
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при запросе к API: {e}")
            raise PrestaShopException(f"Ошибка запроса: {e}")

    def create_customer(self, customer_data: dict) -> Union[dict, Exception]:
        """
        Создает нового клиента.

        Args:
            customer_data: Словарь с данными клиента.

        Returns:
            Данные созданного клиента, если успешно, или ошибку.
        """

        try:
            response = self.post("/customers", json=customer_data)
            if response.status_code == 201:
                return response.json()
            else:
                error_message = response.json().get("message", f"Ошибка создания клиента: {response.status_code}")
                logger.error(f"Ошибка при создании клиента: {error_message}")
                raise PrestaShopException(error_message)
        except json.JSONDecodeError as e:
            logger.error(f"Ошибка декодирования JSON ответа: {e}")
            raise PrestaShopException("Ошибка декодирования JSON")
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка при запросе к API: {e}")
            raise PrestaShopException(f"Ошибка запроса: {e}")
```

**Изменения и объяснения:**

* **`@attrs` Декоратор:** Добавил `@attrs` для класса `PrestaCustomer`. Это делает класс более читаемым и структурированным, автоматически генерирует методы `__init__`, `__repr__`, `__eq__`, `__hash__`, `__attrs_post_init__` и т.д.  Это **очень** рекомендуется для класса с атрибутами.
* **`get_customer`:**
    * Добавлена обработка `404 Not Found`:  Возвращает `None`, если клиент не найден, и логирует предупреждение.
    * **Исключение `PrestaShopException`:** Поднимает исключение `PrestaShopException` при ошибках API (не только 404), чтобы позволить обработку ошибок в вызывающем коде.  Это очень важно для надежной работы.
    * **Обработка `requests.exceptions.RequestException`:** Обрабатывает любые ошибки при запросе к API, включая проблемы со связью.  Важно для стабильности.
* **`create_customer`:**
    * Обрабатывает ответ API, возвращая созданные данные в случае успеха.
    * Обрабатывает возможный `json.JSONDecodeError`. Очень важно, потому что API может вернуть невалидный JSON.
    * Исключения `PrestaShopException` с информативными сообщениями.  Важно для логгирования и обработки ошибок.
* **Типизация:** Использование `typing` для ясности.

**Необходимые импорты:**

* `json` для обработки JSON.
* `requests` (**необходимо**): Для выполнения HTTP-запросов к API PrestaShop.  Этот пример требует импорта `requests`.


**Как использовать:**

```python
from your_module import PrestaCustomer

# ... инициализация Prestashop ...
customer_api = PrestaCustomer(api_key='your_api_key', base_url='your_prestashop_base_url')

try:
    customer_data = customer_api.get_customer(123)
    if customer_data:
        print(customer_data)
    else:
        print("Клиент не найден")
    # Пример создания
    new_customer_data = {"email": "new_customer@example.com", "firstname": "John", "lastname": "Doe"}
    created_customer = customer_api.create_customer(new_customer_data)
    print(created_customer)

except PrestaShopException as e:
    print(f"Ошибка: {e}")
```

**Важный шаг:**  Добавьте импорт `requests`:

```python
import requests
```

Этот код теперь гораздо более надежный и соответствует лучшим практикам.  Пожалуйста, замените  `'your_api_key'` и `'your_prestashop_base_url'` на ваши реальные значения.  Также убедитесь, что у вас установлен `requests`:
```bash
pip install requests
```
