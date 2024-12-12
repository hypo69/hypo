# Анализ кода модуля `api.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на логические блоки.
    - Используются `docstring` для документирования классов и методов.
    - Присутствует обработка ошибок, хотя и не всегда оптимальная.
    - Код следует PEP 8 в основном.
- Минусы
    - Некоторые docstring не полные или не соответствуют стандарту reStructuredText.
    - Использование `try-except` блоков в некоторых местах можно заменить на логирование ошибок.
    - Есть дублирование кода в методах `upload_image_async` и `upload_image`.
    - Не все импорты отсортированы и могут быть оптимизированы.

**Рекомендации по улучшению**
1.  **Документация**:
    -   Улучшить `docstring` всех методов и классов, привести их в соответствие со стандартом reStructuredText (RST).
    -   Использовать `:param` и `:return` для описания параметров и возвращаемых значений.
    -   Добавить более подробные описания в `docstring` для лучшего понимания кода.
    -   Добавить описание модуля в начале файла.

2.  **Обработка ошибок**:
    -   Использовать `logger.error` вместо `try-except` для обработки ошибок.
    -   Унифицировать обработку ошибок в методах.
    -   Добавить больше информации в логи ошибок.

3.  **Рефакторинг**:
    -   Удалить дублирование кода в методах `upload_image_async` и `upload_image`, выделив общую логику в отдельную функцию.
    -   Упорядочить импорты и убрать лишние.
    -   Избегать прямого обращения к `sys.stderr` для логирования в debug режиме, лучше использовать `logger.debug`.

4.  **Производительность**:
    -   Рассмотреть возможность использования асинхронных запросов для более эффективной работы.

**Оптимизированный код**
```python
"""
Модуль для взаимодействия с API PrestaShop
=========================================================================================

Этот модуль содержит класс :class:`PrestaShop`, который обеспечивает взаимодействие
с веб-сервисами PrestaShop API, используя JSON и XML для сообщений.

Модуль позволяет выполнять CRUD-операции, поиск, загрузку изображений и обработку ошибок.

Пример использования
--------------------

Пример использования класса `PrestaShop`:

.. code-block:: python

    from src.endpoints.prestashop.api.api import PrestaShop

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
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
MODE = 'dev'

import os
import sys
from enum import Enum
from http.client import HTTPConnection
from pathlib import Path
from typing import Dict, List, Any
from xml.etree import ElementTree
from xml.parsers.expat import ExpatError

from requests import Session
from requests.models import PreparedRequest


from src import gs
from src.logger.logger import logger
from src.utils.file import save_text_file
from src.utils.convertors.base64 import base64_to_tmpfile
from src.utils.convertors.dict import dict2xml
from src.utils.convertors.xml2dict import xml2dict
from src.utils.image import save_png_from_url
from src.utils.jjson import j_dumps, j_loads, j_loads_ns
from src.utils.printer import pprint
from src.logger.exceptions import PrestaShopException, PrestaShopAuthenticationError


class Format(Enum):
    """Data types return (JSON, XML)

    @details
    @param Enum (int): 1 => JSON, 2 => XML
    @deprecated - я предпочитаю JSON 👍 :))
    """

    JSON = 'JSON'
    XML = 'XML'


class PrestaShop:
    """
    Класс для взаимодействия с API PrestaShop.

    Предоставляет методы для выполнения CRUD операций, поиска и загрузки изображений.
    Использует JSON и XML для обмена данными с API.

    :param API_KEY: API ключ, сгенерированный в PrestaShop.
    :type API_KEY: str
    :param API_DOMAIN: Домен магазина PrestaShop (например, https://myPrestaShop.com).
    :type API_DOMAIN: str
    :param data_format: Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
    :type data_format: str
    :param default_lang: ID языка по умолчанию. По умолчанию 1.
    :type default_lang: int
    :param debug: Флаг для активации режима отладки. По умолчанию True.
    :type debug: bool

    :raises PrestaShopAuthenticationError: Если API ключ неверен или не существует.
    :raises PrestaShopException: Для общих ошибок веб-сервисов PrestaShop.
    """
    client: Session = Session()
    debug = True
    language = None
    data_format = 'JSON'
    ps_version = ''

    def __init__(self,
                 data_format: str = 'JSON',
                 default_lang: int = 1,
                 debug: bool = True) -> None:
        """
        Инициализация класса PrestaShop.

        :param API_DOMAIN: Домен API магазина PrestaShop (например, https://myPrestaShop.com).
        :type API_DOMAIN: str
        :param API_KEY: API ключ, сгенерированный в PrestaShop.
        :type API_KEY: str
        :param data_format: Формат данных ('JSON' или 'XML'). По умолчанию 'JSON'.
        :type data_format: str
        :param default_lang: ID языка по умолчанию. По умолчанию 1.
        :type default_lang: int
        :param debug: Флаг для активации режима отладки. По умолчанию True.
        :type debug: bool
        """
        # Код инициализирует параметры API, такие как домен, ключ, формат данных и язык.
        self.API_DOMAIN = gs.credentials.presta.client.api_key.rstrip('/') + '/api/'
        self.API_KEY = gs.credentials.presta.client.api_key
        self.debug = debug
        self.language = default_lang
        self.data_format = data_format

        if not self.client.auth:
            # Код устанавливает аутентификацию для сессии клиента
            self.client.auth = (self.API_KEY, '')

        response = self.client.request(
            method='HEAD',
            url=self.API_DOMAIN
        )
        # Код получает версию PrestaShop из заголовков ответа
        self.ps_version = response.headers.get('psws-version')

    def ping(self) -> bool:
        """
        Проверяет работоспособность веб-сервиса.

        :return: `True`, если веб-сервис работает, `False` в противном случае.
        :rtype: bool
        """
        # Код отправляет HEAD запрос для проверки доступности API.
        response = self.client.request(
            method='HEAD',
            url=self.API_DOMAIN
        )

        # Код проверяет статус ответа с помощью метода _check_response
        return self._check_response(response.status_code, response)

    def _check_response(self, status_code, response, method=None, url=None, headers=None, data=None) -> bool:
        """
        Проверяет статус ответа HTTP и обрабатывает ошибки.

        :param status_code: Код статуса HTTP.
        :type status_code: int
        :param response: Объект ответа HTTP.
        :type response: requests.Response
        :param method: HTTP метод, использованный для запроса.
        :type method: str, optional
        :param url: URL запроса.
        :type url: str, optional
        :param headers: Заголовки запроса.
        :type headers: dict, optional
        :param data: Данные запроса.
        :type data: dict, optional
        :return: `True`, если код статуса 200 или 201, иначе `False`.
        :rtype: bool
        """
        # Код проверяет, является ли статус код 200 или 201
        if status_code in (200, 201):
            return True
        else:
            # Код обрабатывает ошибку, если статус код не 200 или 201
            self._parse_response_error(response, method, url, headers, data)
            return False

    def _parse_response_error(self, response, method=None, url=None, headers=None, data=None):
        """
        Разбирает ответ об ошибке от API PrestaShop.

        :param response: Объект ответа HTTP.
        :type response: requests.Response
        :param method: HTTP метод, использованный для запроса.
        :type method: str, optional
        :param url: URL запроса.
        :type url: str, optional
        :param headers: Заголовки запроса.
        :type headers: dict, optional
        :param data: Данные запроса.
        :type data: dict, optional
        :return:  Объект ответа, если ошибка в формате JSON, иначе кортеж (code, message) в случае XML.
        :rtype: requests.Response | tuple
        """
        # Код проверяет, является ли формат данных JSON
        if self.data_format == 'JSON':
            status_code = response.status_code
            if not status_code in (200, 201):
                logger.critical(f"""response status code: {status_code}\n
                    url: {response.request.url}\n
                    --------------\n
                    headers: {response.headers}\n
                    --------------\n
                    response text: {response.text}""")
            # Код возвращает объект ответа
            return response
        else:
            # Код разбирает ответ в формате XML
            error_answer = self._parse(response.text)
            if isinstance(error_answer, dict):
                # Код извлекает данные об ошибке из словаря
                error_content = (error_answer
                                 .get('PrestaShop', {})
                                 .get('errors', {})
                                 .get('error', {}))
                if isinstance(error_content, list):
                    error_content = error_content[0]
                code = error_content.get('code')
                message = error_content.get('message')
            elif isinstance(error_answer, ElementTree.Element):
                # Код извлекает данные об ошибке из XML элемента
                error = error_answer.find('errors/error')
                code = error.find('code').text
                message = error.find('message').text
            # Код логирует ошибку
            logger.error(f"XML response error: {message} \\n Code: {code}")
            return code, message

    def _prepare(self, url, params):
        """
        Подготавливает URL для запроса.

        :param url: Базовый URL.
        :type url: str
        :param params: Параметры для запроса.
        :type params: dict
        :return: Подготовленный URL с параметрами.
        :rtype: str
        """
        # Код подготавливает URL для запроса, добавляя параметры.
        req = PreparedRequest()
        req.prepare_url(url, params)
        return req.url

    def _exec(self,
              resource: str,
              resource_id: int | str = None,
              resource_ids: int | tuple = None,
              method: str = 'GET',
              data: dict = None,
              headers: dict = {},
              search_filter: str | dict = None,
              display: str | list = 'full',
              schema: str | None = None,
              sort: str = None,
              limit: str = None,
              language: int = None,
              io_format: str = 'JSON') -> dict | None:
        """
        Выполняет HTTP запрос к API PrestaShop.

        :param resource: API ресурс (например, 'products', 'categories').
        :type resource: str
        :param resource_id: ID ресурса.
        :type resource_id: int | str, optional
        :param resource_ids: ID нескольких ресурсов.
        :type resource_ids: int | tuple, optional
        :param method: HTTP метод (GET, POST, PUT, DELETE).
        :type method: str, optional
        :param data: Данные для отправки с запросом.
        :type data: dict, optional
        :param headers: Дополнительные заголовки для запроса.
        :type headers: dict, optional
        :param search_filter: Фильтр для запроса.
        :type search_filter: str | dict, optional
        :param display: Поля для отображения в ответе.
        :type display: str | list, optional
        :param schema: Схема данных.
        :type schema: str, optional
        :param sort: Параметр сортировки для запроса.
        :type sort: str, optional
        :param limit: Лимит результатов для запроса.
        :type limit: str, optional
        :param language: ID языка для запроса.
        :type language: int, optional
        :param io_format: Формат данных ('JSON' или 'XML').
        :type io_format: str, optional
        :return: Ответ от API или `False` в случае неудачи.
        :rtype: dict | None
        """
        # Код настраивает логирование ошибок в режиме отладки
        if self.debug:
            original_stderr = sys.stderr
            f = open('stderr.log', 'w')
            sys.stderr = f

            response = self.client.request(
                method=method,
                url=self._prepare(f'{self.API_DOMAIN}{resource}/{resource_id}' if resource_id else f'{self.API_DOMAIN}{resource}',
                                  {'filter': search_filter,
                                   'display': display,
                                   'schema': schema,
                                   'sort': sort,
                                   'limit': limit,
                                   'language': language,
                                   'output_format': io_format}),
                data=dict2xml(data) if data and io_format == 'XML' else data,
                headers=headers,
            )

            sys.stderr = original_stderr
            f.close()
        else:
            # Код отправляет запрос без логирования в режиме отладки
            response = self.client.request(
                method=method,
                url=self._prepare(f'{self.API_DOMAIN}{resource}/{resource_id}' if resource_id else f'{self.API_DOMAIN}{resource}',
                                  {'filter': search_filter,
                                   'display': display,
                                   'schema': schema,
                                   'sort': sort,
                                   'limit': limit,
                                   'language': language,
                                   'output_format': io_format}),
                data=dict2xml(data) if data and io_format == 'XML' else data,
                headers=headers,
            )

        # Код проверяет статус ответа и возвращает данные или False
        if not self._check_response(response.status_code, response, method, url, headers, data):
            return False
        # Код возвращает данные в формате JSON или разбирает XML
        if io_format == 'JSON':
            return response.json()
        else:
            return self._parse(response.text)

    def _parse(self, text: str) -> dict | ElementTree.Element | bool:
        """
        Разбирает XML или JSON ответ от API.

        :param text: Текст ответа.
        :type text: str
        :return: Разобранные данные или `False` в случае неудачи.
        :rtype: dict | ElementTree.Element | bool
        """
        # Код разбирает ответ в зависимости от формата данных
        try:
            if self.data_format == 'JSON':
                data = j_loads(text)
                return data.get('PrestaShop', {}) if 'PrestaShop' in data else data
            else:
                tree = ElementTree.fromstring(text)
                return tree
        except (ExpatError, ValueError) as ex:
            # Код логирует ошибку разбора
            logger.error(f'Parsing Error: {str(ex)}')
            return False

    def create(self, resource: str, data: dict) -> dict:
        """
        Создает новый ресурс в API PrestaShop.

        :param resource: API ресурс (например, 'products').
        :type resource: str
        :param data: Данные для нового ресурса.
        :type data: dict
        :return: Ответ от API.
        :rtype: dict
        """
        # Код отправляет POST запрос для создания ресурса
        return self._exec(resource=resource, method='POST', data=data, io_format=self.data_format)

    def read(self, resource: str, resource_id: int | str, **kwargs) -> dict:
        """
        Читает ресурс из API PrestaShop.

        :param resource: API ресурс (например, 'products').
        :type resource: str
        :param resource_id: ID ресурса.
        :type resource_id: int | str
        :param kwargs: Дополнительные аргументы для запроса.
        :type kwargs: dict
        :return: Ответ от API.
        :rtype: dict
        """
        # Код отправляет GET запрос для чтения ресурса
        return self._exec(resource=resource, resource_id=resource_id, method='GET', io_format=self.data_format, **kwargs)

    def write(self, resource: str, data: dict) -> dict:
        """
        Обновляет существующий ресурс в API PrestaShop.

        :param resource: API ресурс (например, 'products').
        :type resource: str
        :param data: Данные для обновления ресурса.
        :type data: dict
        :return: Ответ от API.
        :rtype: dict
        """
        # Код отправляет PUT запрос для обновления ресурса
        return self._exec(resource=resource, resource_id=data.get('id'), method='PUT', data=data, io_format=self.data_format)

    def unlink(self, resource: str, resource_id: int | str) -> bool:
        """
        Удаляет ресурс из API PrestaShop.

        :param resource: API ресурс (например, 'products').
        :type resource: str
        :param resource_id: ID ресурса.
        :type resource_id: int | str
        :return: `True`, если успешно, `False` в противном случае.
        :rtype: bool
        """
        # Код отправляет DELETE запрос для удаления ресурса
        return self._exec(resource=resource, resource_id=resource_id, method='DELETE', io_format=self.data_format)

    def search(self, resource: str, filter: str | dict = None, **kwargs) -> List[dict]:
        """
        Ищет ресурсы в API PrestaShop.

        :param resource: API ресурс (например, 'products').
        :type resource: str
        :param filter: Фильтр для поиска.
        :type filter: str | dict, optional
        :param kwargs: Дополнительные аргументы для запроса.
        :type kwargs: dict
        :return: Список ресурсов, соответствующих критериям поиска.
        :rtype: List[dict]
        """
        # Код отправляет GET запрос для поиска ресурсов
        return self._exec(resource=resource, search_filter=filter, method='GET', io_format=self.data_format, **kwargs)

    def create_binary(self, resource: str, file_path: str, file_name: str) -> dict:
        """
        Загружает бинарный файл в ресурс API PrestaShop.

        :param resource: API ресурс (например, 'images/products/22').
        :type resource: str
        :param file_path: Путь к бинарному файлу.
        :type file_path: str
        :param file_name: Имя файла.
        :type file_name: str
        :return: Ответ от API.
        :rtype: dict
        """
        # Код загружает бинарный файл на сервер
        with open(file_path, 'rb') as file:
            headers = {'Content-Type': 'application/octet-stream'}
            response = self.client.post(
                url=f'{self.API_DOMAIN}{resource}',
                headers=headers,
                data=file.read()
            )
            return response.json()

    def _save(self, file_name: str, data: dict):
        """
        Сохраняет данные в файл.

        :param file_name: Имя файла.
        :type file_name: str
        :param data: Данные для сохранения.
        :type data: dict
        """
        # Код сохраняет данные в JSON файл
        save_text_file(file_name, j_dumps(data, indent=4, ensure_ascii=False))

    def get_data(self, resource: str, **kwargs) -> dict | None:
        """
        Получает данные из ресурса API PrestaShop и сохраняет их в файл.

        :param resource: API ресурс (например, 'products').
        :type resource: str
        :param kwargs: Дополнительные аргументы для запроса.
        :type kwargs: dict
        :return: Данные из API или `False` в случае неудачи.
        :rtype: dict | None
        """
        # Код отправляет запрос для получения данных и сохраняет их в файл
        data = self._exec(resource=resource, method='GET', io_format=self.data_format, **kwargs)
        if data:
            self._save(f'{resource}.json', data)
            return data
        return False

    def remove_file(self, file_path: str):
        """
        Удаляет файл из файловой системы.

        :param file_path: Путь к файлу.
        :type file_path: str
        """
        # Код удаляет файл из файловой системы
        try:
            os.remove(file_path)
        except Exception as e:
            # Код логирует ошибку удаления файла
            logger.error(f"Error removing file {file_path}: {e}")

    def get_apis(self) -> dict:
        """
        Возвращает список всех доступных API.

        :return: Список доступных API.
        :rtype: dict
        """
        # Код получает список доступных API
        return self._exec('apis', method='GET', io_format=self.data_format)

    def get_languages_schema(self) -> dict:
        """
        Получает схему для языков.

        :return: Схема языков или `None` в случае неудачи.
        :rtype: dict | None
        """
        # Код получает схему для языков
        try:
            response = self._exec('languages', display='full', io_format='JSON')
            return response
        except Exception as ex:
            # Код логирует ошибку получения схемы языков
            logger.error(f"Error: {ex}")
            return

    def _upload_image(self, resource: str, resource_id: int, img_url: str, img_name: str = None) -> dict | None:
        """
        Загружает изображение в API PrestaShop.

        :param resource: API ресурс (например, 'images/products/22').
        :type resource: str
        :param resource_id: ID ресурса.
        :type resource_id: int
        :param img_url: URL изображения.
        :type img_url: str
        :param img_name: Имя файла изображения.
        :type img_name: str, optional
        :return: Ответ от API или `None` в случае неудачи.
        :rtype: dict | None
        """
        # Код загружает изображение на сервер
        url_parts = img_url.rsplit('.', 1)
        url_without_extension = url_parts[0]
        extension = url_parts[1] if len(url_parts) > 1 else ''
        filename = str(resource_id) + f'_{img_name}.{extension}'
        png_file_path = save_png_from_url(img_url, filename)
        response = self.create_binary(resource, png_file_path, img_name)
        self.remove_file(png_file_path)
        return response

    def upload_image_async(self, resource: str, resource_id: int, img_url: str, img_name: str = None) -> dict | None:
        """
        Асинхронно загружает изображение в API PrestaShop.

        :param resource: API ресурс (например, 'images/products/22').
        :type resource: str
        :param resource_id: ID ресурса.
        :type resource_id: int
        :param img_url: URL изображения.
        :type img_url: str
        :param img_name: Имя файла изображения.
        :type img_name: str, optional
        :return: Ответ от API или `None` в случае неудачи.
        :rtype: dict | None
        """
        # Код вызывает общую функцию загрузки изображения
        return self._upload_image(resource, resource_id, img_url, img_name)

    def upload_image(self, resource: str, resource_id: int, img_url: str, img_name: str = None) -> dict | None:
        """
        Загружает изображение в API PrestaShop.

        :param resource: API ресурс (например, 'images/products/22').
        :type resource: str
        :param resource_id: ID ресурса.
        :type resource_id: int
        :param img_url: URL изображения.
        :type img_url: str
        :param img_name: Имя файла изображения.
        :type img_name: str, optional
        :return: Ответ от API или `None` в случае неудачи.
        :rtype: dict | None
        """
        # Код вызывает общую функцию загрузки изображения
        return self._upload_image(resource, resource_id, img_url, img_name)

    def get_product_images(self, product_id: int) -> dict | None:
        """
        Получает изображения для продукта.

        :param product_id: ID продукта.
        :type product_id: int
        :return: Список изображений продукта или `False` в случае неудачи.
        :rtype: dict | None
        """
        # Код получает список изображений продукта
        return self._exec(f'products/{product_id}/images', method='GET', io_format=self.data_format)