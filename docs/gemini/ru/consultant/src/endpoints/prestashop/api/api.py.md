# Анализ кода модуля `api.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован, используется объектно-ориентированный подход.
    - Присутствует базовая обработка ошибок.
    - Используются `logger` для логирования.
    - Есть документация в формате docstring.
    - Используются перечисления `Enum`.
- Минусы
    -  Не все docstring соответствуют стандарту reStructuredText (RST).
    -  Используется старый формат docstring, где @param и @return не являются стандартом.
    - Некоторые docstring не полные и не информативные.
    -  Есть избыточное использование try-except блоков.
    -  Дублирование кода в методах `upload_image_async` и `upload_image`.
    -  Импорт `header` не используется в коде, что говорит о его ненужности.
    - В функции `_exec` открывается файл для записи `stderr.log` но он не закрывается.
    - В функции `_parse` не обрабатывается исключение, если `response` не содержит метод `json()`.

**Рекомендации по улучшению**

1.  **Документация:**
    *   Переписать все docstring в соответствии со стандартом reStructuredText (RST), используя `:param:` и `:return:` для описания параметров и возвращаемых значений.
    *   Уточнить и расширить описание для всех функций и методов.
2.  **Обработка ошибок:**
    *   Упростить обработку ошибок, заменив избыточные `try-except` блоки на использование `logger.error`.
    *   Убедиться, что все исключения обрабатываются корректно и логируются.
3.  **Рефакторинг:**
    *   Удалить дублирование кода в методах `upload_image_async` и `upload_image`.
    *   Удалить неиспользуемый импорт `header`.
    *   В функции `_exec` необходимо закрывать файл `stderr.log`.
    *   Добавить проверку наличия метода `json()` у `response` в функции `_parse`.
    *   Использовать форматированные строки (f-strings) для улучшения читаемости и производительности, где это применимо.
4.  **Производительность:**
    *   Убрать неиспользуемый импорт `sys` в `_exec`.
5. **Общее**
     *   Необходимо добавлять комментарии к каждому блоку кода, объясняющие его работу.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для взаимодействия с API PrestaShop.
=========================================================================================

Этот модуль предоставляет класс :class:`PrestaShop`, который используется для взаимодействия с API PrestaShop.
Он обеспечивает методы для выполнения CRUD-операций, поиска и загрузки изображений.

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
"""

import os
from enum import Enum
from http.client import HTTPConnection
from requests import Session
from requests.models import PreparedRequest
from typing import Dict, List, Any
from pathlib import Path
from xml.etree import ElementTree
from xml.parsers.expat import ExpatError

from src import gs
from src.utils.file import save_text_file
from src.utils.convertors.base64 import  base64_to_tmpfile
from src.utils.convertors.dict import dict2xml
from src.utils.convertors.xml2dict import xml2dict
from src.utils.image import save_png_from_url
from src.utils.printer import pprint
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger.logger import logger
from src.logger.exceptions import PrestaShopException, PrestaShopAuthenticationError


class Format(Enum):
    """
    Перечисление для определения формата данных (JSON, XML).

    :param Enum (int): 1 => JSON, 2 => XML
    :deprecated: Предпочитается JSON
    """
    JSON = 'JSON'
    XML = 'XML'


class PrestaShop:
    """
    Класс для взаимодействия с веб-сервисом API PrestaShop, используя JSON и XML для сообщений.

    Предоставляет методы для CRUD-операций, поиска и загрузки изображений, а также обработку ошибок.

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

    :raises PrestaShopAuthenticationError: Если API ключ неверен или не существует.
    :raises PrestaShopException: Для общих ошибок PrestaShop WebServices.

    Пример использования:

    .. code-block:: python

        from src.endpoints.prestashop.api.api import PrestaShop, Format

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

        # Создание новой записи налога
        rec = api.create('taxes', data)

        # Обновление записи налога
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

        # Удаление налога
        api.unlink('taxes', str(rec['id']))

        # Поиск первых 3 налогов с '5' в имени
        import pprint
        recs = api.search('taxes', filter='[name]=%[5]%', limit='3')

        for rec in recs:
            pprint(rec)

        # Создание бинарных данных (изображения продукта)
        api.create_binary('images/products/22', 'img.jpeg', 'image')

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
        Инициализирует класс PrestaShop.

        :param data_format: Формат данных по умолчанию ('JSON' или 'XML'). По умолчанию 'JSON'.
        :type data_format: str
        :param default_lang: ID языка по умолчанию. По умолчанию 1.
        :type default_lang: int
        :param debug: Активировать режим отладки. По умолчанию True.
        :type debug: bool

        :return: None
        """
        # Извлекаем API_DOMAIN из настроек и формируем полный URL
        self.API_DOMAIN = gs.credentials.presta.client.api_key.rstrip('/') + '/api/'
        # Извлекаем API_KEY из настроек
        self.API_KEY = gs.credentials.presta.client.api_key
        # Устанавливаем режим отладки
        self.debug = debug
        # Устанавливаем язык по умолчанию
        self.language = default_lang
        # Устанавливаем формат данных по умолчанию
        self.data_format = data_format

        # Устанавливаем аутентификацию для сессии
        if not self.client.auth:
            self.client.auth = (self.API_KEY, '')
        
        # Выполняем HEAD запрос для получения версии PrestaShop
        response = self.client.request(
            method='HEAD',
            url=self.API_DOMAIN
        )
        # Сохраняем версию PrestaShop из заголовков ответа
        self.ps_version = response.headers.get('psws-version')

    def ping(self) -> bool:
        """
        Проверяет, работает ли веб-сервис.

        :return: True, если веб-сервис работает, иначе False.
        :rtype: bool
        """
        # Выполняем HEAD запрос к API_DOMAIN
        response = self.client.request(
            method='HEAD',
            url=self.API_DOMAIN
        )
        # Проверяем статус ответа
        return self._check_response(response.status_code, response)

    def _check_response(self, status_code: int, response: Any, method: str = None, url: str = None, headers: dict = None, data: dict = None) -> bool:
        """
        Проверяет статус ответа и обрабатывает ошибки.

        :param status_code: HTTP код ответа.
        :type status_code: int
        :param response: Объект HTTP ответа.
        :type response: requests.Response
        :param method: HTTP метод запроса.
        :type method: str, optional
        :param url: URL запроса.
        :type url: str, optional
        :param headers: Заголовки запроса.
        :type headers: dict, optional
        :param data: Данные запроса.
        :type data: dict, optional

        :return: True, если код ответа 200 или 201, иначе False.
        :rtype: bool
        """
        # Проверяем, является ли статус код успешным
        if status_code in (200, 201):
            return True
        else:
            # Обрабатываем ошибку, если код ответа не успешный
            self._parse_response_error(response, method, url, headers, data)
            return False

    def _parse_response_error(self, response: Any, method: str = None, url: str = None, headers: dict = None, data: dict = None):
        """
        Разбирает ответ об ошибке от API PrestaShop.

        :param response: Объект HTTP ответа.
        :type response: requests.Response
        :param method: HTTP метод запроса.
        :type method: str, optional
        :param url: URL запроса.
        :type url: str, optional
        :param headers: Заголовки запроса.
        :type headers: dict, optional
        :param data: Данные запроса.
        :type data: dict, optional
        """
        # Если формат данных JSON
        if self.data_format == 'JSON':
            status_code = response.status_code
            # Логируем критическую ошибку если статус код не 200 или 201
            if not status_code in (200, 201):
                logger.critical(f"""response status code: {status_code}\n
                    url: {response.request.url}\n
                    --------------\n
                    headers: {response.headers}\n
                    --------------\n
                    response text: {response.text}""")
            # Возвращаем объект response
            return response
        else:
             # Если формат данных XML
            error_answer = self._parse(response.text)
            # Проверяем тип error_answer, если это словарь
            if isinstance(error_answer, dict):
                # Извлекаем детали ошибки из словаря
                error_content = (error_answer
                                 .get('PrestaShop', {})
                                 .get('errors', {})
                                 .get('error', {}))
                # Если error_content это список, то берем первый элемент
                if isinstance(error_content, list):
                    error_content = error_content[0]
                # Извлекаем код и сообщение об ошибке
                code = error_content.get('code')
                message = error_content.get('message')
            # Проверяем тип error_answer, если это XML Element
            elif isinstance(error_answer, ElementTree.Element):
                 # Извлекаем детали ошибки из XML
                error = error_answer.find('errors/error')
                code = error.find('code').text
                message = error.find('message').text
            # Логируем ошибку
            logger.error(f"XML response error: {message} \\n Code: {code}")
            # Возвращаем кортеж с кодом и сообщением об ошибке
            return code, message

    def _prepare(self, url: str, params: dict) -> str:
        """
        Подготавливает URL для запроса.

        :param url: Базовый URL.
        :type url: str
        :param params: Параметры для запроса.
        :type params: dict

        :return: Подготовленный URL с параметрами.
        :rtype: str
        """
        # Создаем объект PreparedRequest
        req = PreparedRequest()
        # Подготавливаем URL с параметрами
        req.prepare_url(url, params)
        # Возвращаем сформированный URL
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
        Выполняет HTTP-запрос к API PrestaShop.

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

        :return: Ответ от API или False при неудаче.
        :rtype: dict | None
        """
        # Включаем дебаг режим, если self.debug = True
        if self.debug:
            # Открываем файл для записи ошибок
            f = open('stderr.log', 'w')
            import sys
            # Сохраняем стандартный stderr
            original_stderr = sys.stderr
            # Перенаправляем stderr в файл
            sys.stderr = f
             
            # Выполняем запрос с учетом дебага
            response = self.client.request(
                 method=method,
                 url=self._prepare(
                     f'{self.API_DOMAIN}{resource}/{resource_id}' if resource_id else f'{self.API_DOMAIN}{resource}',
                     {'filter': search_filter,
                      'display': display,
                      'schema': schema,
                      'sort': sort,
                      'limit': limit,
                      'language': language,
                      'output_format': io_format}
                 ),
                 data=dict2xml(data) if data and io_format == 'XML' else data,
                 headers=headers,
            )
            # Возвращаем stderr в исходное состояние
            sys.stderr = original_stderr
            # Закрываем файл
            f.close()
        # Проверяем статус ответа
        if not self._check_response(response.status_code, response, method, url, headers, data):
            return False
        # Возвращаем данные в JSON или XML
        if io_format == 'JSON':
            # Обрабатываем JSON
            return response.json()
        else:
            # Обрабатываем XML
            return self._parse(response.text)


    def _parse(self, text: str) -> dict | ElementTree.Element | bool:
        """
        Разбирает XML или JSON ответ от API.

        :param text: Текст ответа.
        :type text: str

        :return: Разобранные данные или False при неудаче.
        :rtype: dict | ElementTree.Element | bool
        """
        try:
            # Обрабатываем JSON
            if self.data_format == 'JSON':
                try:
                    data = response.json()
                except AttributeError as ex:
                     logger.error(f'Parsing Error: {str(ex)}')
                     return False
                return data.get('PrestaShop', {}) if 'PrestaShop' in data else data
            else:
                # Обрабатываем XML
                tree = ElementTree.fromstring(text)
                return tree
        except (ExpatError, ValueError) as ex:
            # Логируем ошибки разбора
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
        # Выполняем POST запрос для создания нового ресурса
        return self._exec(resource=resource, method='POST', data=data, io_format=self.data_format)

    def read(self, resource: str, resource_id: int | str, **kwargs) -> dict:
        """
        Читает ресурс из API PrestaShop.

        :param resource: API ресурс (например, 'products').
        :type resource: str
        :param resource_id: ID ресурса.
        :type resource_id: int | str
        :param kwargs: Дополнительные параметры для запроса.

        :return: Ответ от API.
        :rtype: dict
        """
        # Выполняем GET запрос для чтения ресурса
        return self._exec(resource=resource, resource_id=resource_id, method='GET', io_format=self.data_format, **kwargs)

    def write(self, resource: str, data: dict) -> dict:
        """
        Обновляет существующий ресурс в API PrestaShop.

        :param resource: API ресурс (например, 'products').
        :type resource: str
        :param data: Данные для ресурса.
        :type data: dict

        :return: Ответ от API.
        :rtype: dict
        """
        # Выполняем PUT запрос для обновления ресурса
        return self._exec(resource=resource, resource_id=data.get('id'), method='PUT', data=data, io_format=self.data_format)

    def unlink(self, resource: str, resource_id: int | str) -> bool:
        """
        Удаляет ресурс из API PrestaShop.

        :param resource: API ресурс (например, 'products').
        :type resource: str
        :param resource_id: ID ресурса.
        :type resource_id: int | str

        :return: True, если удаление успешно, иначе False.
        :rtype: bool
        """
        # Выполняем DELETE запрос для удаления ресурса
        return self._exec(resource=resource, resource_id=resource_id, method='DELETE', io_format=self.data_format)

    def search(self, resource: str, filter: str | dict = None, **kwargs) -> List[dict]:
        """
        Ищет ресурсы в API PrestaShop.

        :param resource: API ресурс (например, 'products').
        :type resource: str
        :param filter: Фильтр для поиска.
        :type filter: str | dict, optional
        :param kwargs: Дополнительные параметры для запроса.

        :return: Список ресурсов, соответствующих критериям поиска.
        :rtype: List[dict]
        """
        # Выполняем GET запрос для поиска ресурсов
        return self._exec(resource=resource, search_filter=filter, method='GET', io_format=self.data_format, **kwargs)

    def create_binary(self, resource: str, file_path: str, file_name: str) -> dict:
         """
        Загружает бинарный файл в API PrestaShop.

        :param resource: API ресурс (например, 'images/products/22').
        :type resource: str
        :param file_path: Путь к бинарному файлу.
        :type file_path: str
        :param file_name: Имя файла.
        :type file_name: str

        :return: Ответ от API.
        :rtype: dict
        """
         # Открываем файл для чтения в бинарном виде
         with open(file_path, 'rb') as file:
            # Устанавливаем заголовки для запроса
            headers = {'Content-Type': 'application/octet-stream'}
            # Выполняем POST запрос для загрузки файла
            response = self.client.post(
                url=f'{self.API_DOMAIN}{resource}',
                headers=headers,
                data=file.read()
            )
            # Возвращаем JSON ответ
            return response.json()

    def _save(self, file_name: str, data: dict):
         """
        Сохраняет данные в файл.

        :param file_name: Имя файла.
        :type file_name: str
        :param data: Данные для сохранения.
        :type data: dict
        """
        # Сохраняем данные в файл
        save_text_file(file_name, j_dumps(data, indent=4, ensure_ascii=False))

    def get_data(self, resource: str, **kwargs) -> dict | None:
        """
        Получает данные из API PrestaShop и сохраняет их в файл.

        :param resource: API ресурс (например, 'products').
        :type resource: str
        :param kwargs: Дополнительные параметры для запроса.

        :return: Данные от API или False при неудаче.
        :rtype: dict | None
        """
        # Выполняем GET запрос для получения данных
        data = self._exec(resource=resource, method='GET', io_format=self.data_format, **kwargs)
        # Если данные получены, сохраняем их в файл
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
        try:
            # Удаляем файл
            os.remove(file_path)
        except Exception as e:
            # Логируем ошибку удаления файла
            logger.error(f"Error removing file {file_path}: {e}")

    def get_apis(self) -> dict:
        """
        Получает список всех доступных API.

        :return: Список доступных API.
        :rtype: dict
        """
        # Выполняем GET запрос для получения списка API
        return self._exec('apis', method='GET', io_format=self.data_format)

    def get_languages_schema(self) -> dict:
        """
        Получает схему для языков.

        :return: Схема языков или None при неудаче.
        :rtype: dict
        """
        try:
            # Выполняем GET запрос для получения схемы языков
            response = self._exec('languages', display='full', io_format='JSON')
            return response
        except Exception as ex:
             # Логируем ошибку получения схемы языков
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

        :return: Ответ от API или None при неудаче.
        :rtype: dict | None
        """
        # Разделяем URL на имя и расширение
        url_parts = img_url.rsplit('.', 1)
        url_without_extension = url_parts[0]
        extension = url_parts[1] if len(url_parts) > 1 else ''
        # Формируем имя файла
        filename = str(resource_id) + f'_{img_name}.{extension}'
         # Сохраняем изображение в формате png
        png_file_path = save_png_from_url(img_url, filename)
         # Загружаем бинарное изображение
        response = self.create_binary(resource, png_file_path, img_name)
        # Удаляем временный файл
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

        :return: Ответ от API или None при неудаче.
        :rtype: dict | None
        """
        # Вызываем метод _upload_image для загрузки изображения
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

        :return: Ответ от API или None при неудаче.
        :rtype: dict | None
        """
        # Вызываем метод _upload_image для загрузки изображения
        return self._upload_image(resource, resource_id, img_url, img_name)

    def get_product_images(self, product_id: int) -> dict | None:
        """
        Получает изображения продукта.

        :param product_id: ID продукта.
        :type product_id: int

        :return: Список изображений продукта или False при неудаче.
        :rtype: dict | None
        """
        # Выполняем GET запрос для получения изображений продукта
        return self._exec(f'products/{product_id}/images', method='GET', io_format=self.data_format)