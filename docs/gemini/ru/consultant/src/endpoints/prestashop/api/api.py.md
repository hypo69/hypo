# Анализ кода модуля `api.py`

**Качество кода**
7
-   Плюсы
    -   Код структурирован в класс `PrestaShop`, что облегчает его использование и поддержку.
    -   Используется `requests.Session` для управления HTTP-соединениями.
    -   Обработка ошибок присутствует, хотя и требует доработки.
    -   Используются `Enum` для определения форматов данных.
    -   Код содержит docstrings для большинства методов, что облегчает понимание его функциональности.
-   Минусы
    -   Не все комментарии и docstring соответствуют стандарту RST.
    -   Не все импорты необходимые, к примеру `header`.
    -   Используется `try-except` для обработки ошибок, что не всегда эффективно.
    -   Логирование ошибок не всегда достаточно информативно.
    -   Дублирование кода при загрузке изображений.
    -   Не все методы и переменные имеют docstring.
    -   Импорт `sys` внутри метода, что не является хорошей практикой.
    -   Использования `open('stderr.log', 'w')` в `debug=True`, лучше логировать в файл через `logger`.

**Рекомендации по улучшению**

1.  **Форматирование документации**:
    -   Необходимо переписать все комментарии и docstring в формате reStructuredText (RST), чтобы соответствовать стандарту.
    -   Примеры:
        -   Заменить `@param` на `:param:`
        -   Заменить `@return` на `:return:`
        -   Заменить `@throws` на `:raises:`
        -   Добавить описание для модуля в начале файла.
        -   Добавить более подробные описания для параметров функций.
        -   Привести все docstring к общему виду.
        -   Удалить неиспользуемые комментарии.
2.  **Использование `j_loads` и `j_loads_ns`**:
    -   В данном коде `j_loads` и `j_loads_ns` не используются, но они должны быть использованы вместо `json.load` при необходимости.
3.  **Анализ структуры**:
    -   Импорт `header` не используется и его нужно удалить.
    -   Необходимо унифицировать импорты по алфавиту и группам.
    -   Проверить все имена переменных и функций на соответствие стилю кода.
4.  **Рефакторинг и улучшения**:
    -   Заменить использование `try-except` на проверку статуса ответа и логирование через `logger.error` в методе `_exec`.
    -   Удалить дублирование кода в методах `upload_image_async` и `upload_image`.
    -   Перенести логику сохранения в `debug` режиме в `logger.debug` с форматированием сообщения.
    -   Пересмотреть метод `_parse`, он не должен вызывать исключение.
    -   Добавить обработку ошибок в методах `_parse`, `create`, `read`, `write`, `unlink`, `search`, `create_binary`.
    -   Добавить docstring для переменных класса.
    -   Добавить docstring для `__init__` класса.
    -   Избавиться от `if self.data_format == 'JSON': ... else:` используя try/except при парсинге JSON, XML.
5.  **Дополнительные улучшения**:
    -   Добавить комментарии в формате RST ко всем функциям и методам.
    -   Улучшить обработку ошибок и логирование.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для взаимодействия с API PrestaShop
=========================================================================================

Этот модуль предоставляет класс :class:`PrestaShop`, который позволяет взаимодействовать с API PrestaShop,
выполняя операции CRUD, поиск и загрузку изображений.

Пример использования
--------------------

Пример использования класса `PrestaShop`:

.. code-block:: python

    from src.endpoints.prestashop.api.api import PrestaShop

    api = PrestaShop(
        API_DOMAIN = "https://myPrestaShop.com",
        API_KEY="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        default_lang=1,
        debug=True,
        data_format='JSON',
    )

    api.ping()

    data = {
        'tax': {
            'rate': 3.000,
            'active': '1',
            'name': {
                'language': {
                    'attrs': {'id': '1'},
                    'value': '3% tax'
                }
            }
        }
    }

    # Create tax record
    rec = api.create('taxes', data)

    # Update the same tax record
    update_data = {
        'tax': {
            'id': str(rec['id']),
            'rate': 3.000,
            'active': '1',
            'name': {
                'language': {
                    'attrs': {'id': '1'},
                    'value': '3% tax'
                }
            }
        }
    }

    update_rec = api.write('taxes', update_data)

    # Remove this tax
    api.unlink('taxes', str(rec['id']))

    # Search the first 3 taxes with '5' in the name
    import pprint
    recs = api.search('taxes', filter='[name]=%[5]%', limit='3')

    for rec in recs:
        pprint(rec)

    # Create binary (product image)
    api.create_binary('images/products/22', 'img.jpeg', 'image')
"""
import os
import sys
from enum import Enum
from http.client import HTTPConnection
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union
from xml.etree import ElementTree
from xml.parsers.expat import ExpatError

from requests import Session
from requests.models import PreparedRequest

from src import gs
from src.logger.exceptions import PrestaShopAuthenticationError, PrestaShopException
from src.logger.logger import logger
from src.utils.convertors.base64 import base64_to_tmpfile
from src.utils.convertors.dict import dict2xml
from src.utils.convertors.xml2dict import xml2dict
from src.utils.file import save_text_file
from src.utils.image import save_png_from_url
from src.utils.jjson import j_dumps, j_loads, j_loads_ns
from src.utils.printer import pprint

MODE = 'dev'


class Format(Enum):
    """
    Тип возвращаемых данных (JSON, XML)

    :param Enum (int): 1 => JSON, 2 => XML
    :deprecated: Я предпочитаю JSON 👍 :))
    """

    JSON = 'JSON'
    XML = 'XML'


class PrestaShop:
    """
    Класс для взаимодействия с API PrestaShop, используя JSON и XML для сообщений.

    :param API_KEY: API ключ, сгенерированный в PrestaShop.
    :type API_KEY: str
    :param API_DOMAIN: Домен магазина PrestaShop (например, https://myPrestaShop.com).
    :type API_DOMAIN: str
    :param data_format: Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
    :type data_format: str
    :param default_lang: ID языка по умолчанию. По умолчанию 1.
    :type default_lang: int
    :param debug: Активировать режим отладки. По умолчанию True.
    :type debug: bool
    :raises PrestaShopAuthenticationError: Если API ключ неверный или не существует.
    :raises PrestaShopException: Для общих ошибок веб-сервисов PrestaShop.

    Пример использования:
    .. code-block:: python

        from src.endpoints.prestashop.api.api import PrestaShop, Format

        api = PrestaShop(
            API_DOMAIN="https://myPrestaShop.com",
            API_KEY="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            default_lang=1,
            debug=True,
            data_format='JSON',
        )

        api.ping()

        data = {
            'tax': {
                'rate': 3.000,
                'active': '1',
                'name': {
                    'language': {
                        'attrs': {'id': '1'},
                        'value': '3% tax'
                    }
                }
            }
        }

        # Create tax record
        rec = api.create('taxes', data)

        # Update the same tax record
        update_data = {
            'tax': {
                'id': str(rec['id']),
                'rate': 3.000,
                'active': '1',
                'name': {
                    'language': {
                        'attrs': {'id': '1'},
                        'value': '3% tax'
                    }
                }
            }
        }

        update_rec = api.write('taxes', update_data)

        # Remove this tax
        api.unlink('taxes', str(rec['id']))

        # Search the first 3 taxes with '5' in the name
        import pprint
        recs = api.search('taxes', filter='[name]=%[5]%', limit='3')

        for rec in recs:
            pprint(rec)

        # Create binary (product image)
        api.create_binary('images/products/22', 'img.jpeg', 'image')
    """
    client: Session = Session()
    """Сессия HTTP запросов"""
    debug: bool = True
    """Флаг режима отладки"""
    language: int = None
    """ID языка"""
    data_format: str = 'JSON'
    """Формат данных"""
    ps_version: str = ''
    """Версия PrestaShop"""

    def __init__(self, data_format: str = 'JSON', default_lang: int = 1, debug: bool = True) -> None:
        """
        Инициализирует класс PrestaShop.

        :param API_DOMAIN: Домен API вашего магазина PrestaShop (например, https://myPrestaShop.com).
        :type API_DOMAIN: str
        :param API_KEY: API ключ, сгенерированный в PrestaShop.
        :type API_KEY: str
        :param data_format: Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
        :type data_format: str
        :param default_lang: ID языка по умолчанию. По умолчанию 1.
        :type default_lang: int
        :param debug: Активировать режим отладки. По умолчанию True.
        :type debug: bool
        :return: None
        :rtype: None
        """
        self.API_DOMAIN = gs.credentials.presta.client.api_key.rstrip('/') + '/api/'
        self.API_KEY = gs.credentials.presta.client.api_key
        self.debug = debug
        self.language = default_lang
        self.data_format = data_format

        if not self.client.auth:
            self.client.auth = (self.API_KEY, '')

        response = self.client.request(method='HEAD', url=self.API_DOMAIN)
        self.ps_version = response.headers.get('psws-version')

    def ping(self) -> bool:
        """
        Проверяет работоспособность веб-сервиса.

        :return: Результат проверки. Возвращает `True`, если веб-сервис работает, иначе `False`.
        :rtype: bool
        """
        response = self.client.request(method='HEAD', url=self.API_DOMAIN)
        return self._check_response(response.status_code, response)

    def _check_response(self, status_code: int, response: Any, method: str = None, url: str = None,
                       headers: Dict = None, data: Dict = None) -> bool:
        """
        Проверяет код ответа и обрабатывает ошибки.

        :param status_code: Код статуса HTTP ответа.
        :type status_code: int
        :param response: Объект HTTP ответа.
        :type response: requests.Response
        :param method: HTTP метод, использованный для запроса.
        :type method: str
        :param url: URL запроса.
        :type url: str
        :param headers: Заголовки запроса.
        :type headers: dict
        :param data: Данные запроса.
        :type data: dict
        :return: `True`, если код статуса 200 или 201, иначе `False`.
        :rtype: bool
        """
        if status_code in (200, 201):
            return True
        else:
            self._parse_response_error(response, method, url, headers, data)
            return False

    def _parse_response_error(self, response: Any, method: str = None, url: str = None, headers: Dict = None,
                              data: Dict = None) -> Tuple[str, str] | None:
        """
        Разбирает ответ об ошибке от API PrestaShop.

        :param response: Объект HTTP ответа от сервера.
        :type response: requests.Response
        :param method: HTTP метод, использованный для запроса.
        :type method: str
        :param url: URL запроса.
        :type url: str
        :param headers: Заголовки запроса.
        :type headers: dict
        :param data: Данные запроса.
        :type data: dict
        :return: Код и сообщение об ошибке или None, если ошибка не распознана.
        :rtype: tuple[str, str] | None
        """
        try:
            if self.data_format == 'JSON':
                status_code = response.status_code
                if not status_code in (200, 201):
                    logger.critical(f"""response status code: {status_code}\n
                        url: {response.request.url}\n
                        --------------\n
                        headers: {response.headers}\n
                        --------------\n
                        response text: {response.text}""")
                return response
            else:
                error_answer = self._parse(response.text)
                if isinstance(error_answer, dict):
                    error_content = (error_answer
                                     .get('PrestaShop', {})
                                     .get('errors', {})
                                     .get('error', {}))
                    if isinstance(error_content, list):
                        error_content = error_content[0]
                    code = error_content.get('code')
                    message = error_content.get('message')
                elif isinstance(error_answer, ElementTree.Element):
                    error = error_answer.find('errors/error')
                    code = error.find('code').text
                    message = error.find('message').text
                logger.error(f"XML response error: {message} \\n Code: {code}")
                return code, message
        except Exception as ex:
            logger.error(f'Ошибка при разборе ответа об ошибке: {ex}')
            return None

    def _prepare(self, url: str, params: Dict) -> str:
        """
        Подготавливает URL для запроса.

        :param url: Базовый URL.
        :type url: str
        :param params: Параметры запроса.
        :type params: dict
        :return: Подготовленный URL с параметрами.
        :rtype: str
        """
        req = PreparedRequest()
        req.prepare_url(url, params)
        return req.url

    def _exec(self, resource: str, resource_id: Union[int, str] = None, resource_ids: Union[int, tuple] = None,
              method: str = 'GET', data: Dict = None, headers: Dict = {}, search_filter: str = None,
              display: Union[str, list] = 'full', schema: str = None, sort: str = None, limit: str = None,
              language: int = None, io_format: str = 'JSON') -> Union[Dict, bool, None]:
        """
        Выполняет HTTP запрос к API PrestaShop.

        :param resource: Ресурс API (например, 'products', 'categories').
        :type resource: str
        :param resource_id: ID ресурса.
        :type resource_id: int | str
        :param resource_ids: ID нескольких ресурсов.
        :type resource_ids: int | tuple
        :param method: HTTP метод (GET, POST, PUT, DELETE).
        :type method: str
        :param data: Данные для отправки с запросом.
        :type data: dict
        :param headers: Дополнительные заголовки для запроса.
        :type headers: dict
        :param search_filter: Фильтр для запроса.
        :type search_filter: str | dict
        :param display: Поля для отображения в ответе.
        :type display: str | list
        :param schema: Схема данных.
        :type schema: str | None
        :param sort: Параметр сортировки для запроса.
        :type sort: str
        :param limit: Лимит результатов для запроса.
        :type limit: str
        :param language: ID языка для запроса.
        :type language: int
        :param io_format: Формат данных ('JSON' или 'XML').
        :type io_format: str
        :return: Ответ от API или `False` при ошибке.
        :rtype: dict | bool | None
        """
        url = f'{self.API_DOMAIN}{resource}/{resource_id}' if resource_id else f'{self.API_DOMAIN}{resource}'
        params = {
            'filter': search_filter,
            'display': display,
            'schema': schema,
            'sort': sort,
            'limit': limit,
            'language': language,
            'output_format': io_format
        }
        if self.debug:
            logger.debug(f"Request: {method=}, {url=}, {params=}, {data=}, {headers=}")

        response = self.client.request(
            method=method,
            url=self._prepare(url, params),
            data=dict2xml(data) if data and io_format == 'XML' else data,
            headers=headers,
        )

        if not self._check_response(response.status_code, response, method, url, headers, data):
            return False

        try:
            if io_format == 'JSON':
                return response.json()
            else:
                return self._parse(response.text)
        except Exception as ex:
            logger.error(f'Ошибка при получении ответа: {ex}')
            return False

    def _parse(self, text: str) -> Union[Dict, ElementTree.Element, bool]:
        """
        Разбирает XML или JSON ответ от API.

        :param text: Текст ответа.
        :type text: str
        :return: Разобранные данные или `False` при ошибке.
        :rtype: dict | ElementTree.Element | bool
        """
        try:
            if self.data_format == 'JSON':
                data = j_loads(text)
                return data.get('PrestaShop', {}) if 'PrestaShop' in data else data
            else:
                tree = ElementTree.fromstring(text)
                return tree
        except (ExpatError, ValueError) as ex:
            logger.error(f'Ошибка при разборе: {ex}')
            return False

    def create(self, resource: str, data: Dict) -> Union[Dict, bool]:
        """
        Создает новый ресурс в API PrestaShop.

        :param resource: Ресурс API (например, 'products').
        :type resource: str
        :param data: Данные для нового ресурса.
        :type data: dict
        :return: Ответ от API или `False` при ошибке.
        :rtype: dict | bool
        """
        return self._exec(resource=resource, method='POST', data=data, io_format=self.data_format)

    def read(self, resource: str, resource_id: Union[int, str], **kwargs) -> Union[Dict, bool, None]:
        """
        Читает ресурс из API PrestaShop.

        :param resource: Ресурс API (например, 'products').
        :type resource: str
        :param resource_id: ID ресурса.
        :type resource_id: int | str
        :param kwargs: Дополнительные аргументы для запроса.
        :type kwargs: dict
        :return: Ответ от API или `False` при ошибке.
        :rtype: dict | bool | None
        """
        return self._exec(resource=resource, resource_id=resource_id, method='GET', io_format=self.data_format,
                          **kwargs)

    def write(self, resource: str, data: Dict) -> Union[Dict, bool, None]:
        """
        Обновляет существующий ресурс в API PrestaShop.

        :param resource: Ресурс API (например, 'products').
        :type resource: str
        :param data: Данные для ресурса.
        :type data: dict
        :return: Ответ от API или `False` при ошибке.
        :rtype: dict | bool | None
        """
        return self._exec(resource=resource, resource_id=data.get('id'), method='PUT', data=data,
                          io_format=self.data_format)

    def unlink(self, resource: str, resource_id: Union[int, str]) -> Union[bool, None]:
        """
        Удаляет ресурс из API PrestaShop.

        :param resource: Ресурс API (например, 'products').
        :type resource: str
        :param resource_id: ID ресурса.
        :type resource_id: int | str
        :return: `True`, если успешно, `False` в противном случае.
        :rtype: bool | None
        """
        return self._exec(resource=resource, resource_id=resource_id, method='DELETE', io_format=self.data_format)

    def search(self, resource: str, filter: Union[str, Dict] = None, **kwargs) -> Union[List[Dict], bool, None]:
        """
        Поиск ресурсов в API PrestaShop.

        :param resource: Ресурс API (например, 'products').
        :type resource: str
        :param filter: Фильтр для поиска.
        :type filter: str | dict
        :param kwargs: Дополнительные аргументы для запроса.
        :type kwargs: dict
        :return: Список ресурсов, соответствующих критериям поиска, или `False` при ошибке.
        :rtype: list[dict] | bool | None
        """
        return self._exec(resource=resource, search_filter=filter, method='GET', io_format=self.data_format,
                          **kwargs)

    def create_binary(self, resource: str, file_path: str, file_name: str) -> Union[Dict, bool]:
        """
        Загружает бинарный файл в ресурс API PrestaShop.

        :param resource: Ресурс API (например, 'images/products/22').
        :type resource: str
        :param file_path: Путь к бинарному файлу.
        :type file_path: str
        :param file_name: Имя файла.
        :type file_name: str
        :return: Ответ от API или `False` при ошибке.
        :rtype: dict | bool
        """
        try:
            with open(file_path, 'rb') as file:
                headers = {'Content-Type': 'application/octet-stream'}
                response = self.client.post(
                    url=f'{self.API_DOMAIN}{resource}',
                    headers=headers,
                    data=file.read()
                )
                return response.json()
        except Exception as ex:
            logger.error(f'Ошибка при загрузке бинарного файла: {ex}')
            return False

    def _save(self, file_name: str, data: Dict) -> None:
        """
        Сохраняет данные в файл.

        :param file_name: Имя файла.
        :type file_name: str
        :param data: Данные для сохранения.
        :type data: dict
        :return: None
        :rtype: None
        """
        save_text_file(file_name, j_dumps(data, indent=4, ensure_ascii=False))

    def get_data(self, resource: str, **kwargs) -> Union[Dict, bool, None]:
        """
        Получает данные из ресурса API PrestaShop и сохраняет их.

        :param resource: Ресурс API (например, 'products').
        :type resource: str
        :param kwargs: Дополнительные аргументы для запроса API.
        :type kwargs: dict
        :return: Данные от API или `False` при ошибке.
        :rtype: dict | bool | None
        """
        data = self._exec(resource=resource, method='GET', io_format=self.data_format, **kwargs)
        if data:
            self._save(f'{resource}.json', data)
            return data
        return False

    def remove_file(self, file_path: str) -> None:
        """
        Удаляет файл из файловой системы.

        :param file_path: Путь к файлу.
        :type file_path: str
        :return: None
        :rtype: None
        """
        try:
            os.remove(file_path)
        except Exception as e:
            logger.error(f"Ошибка при удалении файла {file_path}: {e}")

    def get_apis(self) -> Union[Dict, bool, None]:
        """
        Получает список всех доступных API.

        :return: Список доступных API.
        :rtype: dict | bool | None
        """
        return self._exec('apis', method='GET', io_format=self.data_format)

    def get_languages_schema(self) -> Union[Dict, None]:
        """
        Получает схему для языков.

        :return: Схема языков или None при ошибке.
        :rtype: dict | None
        """
        try:
            return self._exec('languages', display='full', io_format='JSON')
        except Exception as ex:
            logger.error(f"Ошибка при получении схемы языков: {ex}")
            return None

    def _upload_image(self, resource: str, resource_id: int, img_url: str, img_name: str = None) -> Union[Dict, bool, None]:
        """
        Загружает изображение в API PrestaShop.

        :param resource: Ресурс API (например, 'images/products/22').
        :type resource: str
        :param resource_id: ID ресурса.
        :type resource_id: int
        :param img_url: URL изображения.
        :type img_url: str
        :param img_name: Имя файла изображения.
        :type img_name: str, optional
        :return: Ответ от API или `False` при ошибке.
        :rtype: dict | bool | None
        """
        try:
            url_parts = img_url.rsplit('.', 1)
            extension = url_parts[1] if len(url_parts) > 1 else ''
            filename = f'{resource_id}_{img_name}.{extension}'
            png_file_path = save_png_from_url(img_url, filename)
            response = self.create_binary(resource, png_file_path, img_name)
            self.remove_file(png_file_path)
            return response
        except Exception as ex:
            logger.error(f"Ошибка при загрузке изображения: {ex}")
            return False

    def upload_image_async(self, resource: str, resource_id: int, img_url: str, img_name: str = None) -> Union[Dict, bool, None]:
         """
         Асинхронно загружает изображение в API PrestaShop.

         :param resource: Ресурс API (например, 'images/products/22').
         :type resource: str
         :param resource_id: ID ресурса.
         :type resource_id: int
         :param img_url: URL изображения.
         :type img_url: str
         :param img_name: Имя файла изображения.
         :type img_name: str, optional
         :return: Ответ от API или `False` при ошибке.
         :rtype: dict | bool | None
         """
         return self._upload_image(resource, resource_id, img_url, img_name)

    def upload_image(self, resource: str, resource_id: int, img_url: str, img_name: str = None) ->  Union[Dict, bool, None]:
        """
        Загружает изображение в API PrestaShop.

        :param resource: Ресурс API (например, 'images/products/22').
        :type resource: str
        :param resource_id: ID ресурса.
        :type resource_id: int
        :param img_url: URL изображения.
        :type img_url: str
        :param img_name: Имя файла изображения.
        :type img_name: str, optional
        :return: Ответ от API или `False` при ошибке.
        :rtype: dict | bool | None
        """
        return self._upload_image(resource, resource_id, img_url, img_name)

    def get_product_images(self, product_id: int) ->  Union[Dict, bool, None]:
        """
        Получает изображения для продукта.

        :param product_id: ID продукта.
        :type product_id: int
        :return: Список изображений продукта или `False` при ошибке.
        :rtype: dict | bool | None
        """
        return self._exec(f'products/{product_id}/images', method='GET', io_format=self.data_format)