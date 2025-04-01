# Модуль для взаимодействия с PrestaShop
=================================================

Модуль предназначен для интеграции и взаимодействия с PrestaShop, обеспечивая возможность автоматизированной загрузки и обновления данных, например, информации о продуктах.

## Обзор

Данный модуль предоставляет инструменты для взаимодействия с PrestaShop. Он может использоваться для автоматизации процесса загрузки и обновления данных в PrestaShop, таких как информация о продуктах.

## Подробнее

Модуль предназначен для работы с API PrestaShop, чтобы автоматизировать процесс загрузки и обновления данных. 
Он является частью системы автоматизации, разработанной для упрощения управления данными в PrestaShop.

## Классы

### `Presta`

**Описание**: Класс `Presta` предназначен для взаимодействия с PrestaShop API.

**Принцип работы**:
Класс предоставляет методы для аутентификации и выполнения запросов к PrestaShop API. 
Он использует библиотеку `requests` для отправки HTTP-запросов и обрабатывает ответы от сервера.

**Атрибуты**:
- `url` (str): URL API PrestaShop.
- `key` (str): Ключ API для аутентификации.

**Методы**:
- `__init__(self, url: str, key: str)`: Конструктор класса, инициализирует URL и ключ API.
- `get(self, url: str)`: Выполняет GET-запрос к API.
- `post(self, url: str, data: dict)`: Выполняет POST-запрос к API.
- `put(self, url: str, data: dict)`: Выполняет PUT-запрос к API.
- `delete(self, url: str)`: Выполняет DELETE-запрос к API.
- `head(self, url: str)`: Выполняет HEAD-запрос к API.
- `options(self, url: str)`: Выполняет OPTIONS-запрос к API.

```python
class Presta:
    """
    Args:
        url (str): URL API PrestaShop.
        key (str): Ключ API для аутентификации.
    """

    def __init__(self, url: str, key: str):
        """Конструктор класса Presta.

        Args:
            url (str): URL API PrestaShop.
            key (str): Ключ API для аутентификации.
        """
        self.url = url
        self.key = key

    def get(self, url: str):
        """Выполняет GET-запрос к API.

        Args:
            url (str): URL для запроса.

        Returns:
            Response: Объект ответа.
        """
        ...

    def post(self, url: str, data: dict):
        """Выполняет POST-запрос к API.

        Args:
            url (str): URL для запроса.
            data (dict): Данные для отправки в теле запроса.

        Returns:
            Response: Объект ответа.
        """
        ...

    def put(self, url: str, data: dict):
        """Выполняет PUT-запрос к API.

        Args:
            url (str): URL для запроса.
            data (dict): Данные для отправки в теле запроса.

        Returns:
            Response: Объект ответа.
        """
        ...

    def delete(self, url: str):
        """Выполняет DELETE-запрос к API.

        Args:
            url (str): URL для запроса.

        Returns:
            Response: Объект ответа.
        """
        ...

    def head(self, url: str):
        """Выполняет HEAD-запрос к API.

        Args:
            url (str): URL для запроса.

        Returns:
            Response: Объект ответа.
        """
        ...

    def options(self, url: str):
        """Выполняет OPTIONS-запрос к API.

        Args:
            url (str): URL для запроса.

        Returns:
            Response: Объект ответа.
        """
        ...