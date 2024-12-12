# Анализ кода модуля `alirequests`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разбит на логические блоки.
    - Используются классы и методы для организации функциональности.
    - Присутствует базовая обработка ошибок с использованием `try-except` блоков.
    - Применяется `logger` для логирования, что упрощает отладку и мониторинг.
    - Используются `fake_useragent` для генерации случайных `User-Agent`, повышая анонимность.
    - Вынесена логика работы с куками в отдельный метод `_load_webdriver_cookies_file`.
    - Используются f-строки для форматирования строк, что повышает читаемость.
-  Минусы
    - Не хватает reStructuredText (RST) документации для всех методов и класса.
    - Используется стандартный блок `try-except` вместо обработки ошибок через `logger.error` в некоторых местах.
    - В некоторых местах логика работы с куками дублируется (`_load_webdriver_cookies_file`, `_handle_session_id`).
    - Использовать `j_dumps` из `src.utils.jjson`, для записи данных в файл, если это требуется.
    - Не все переменные имеют понятные имена.
    - Не используется `j_loads_ns` для загрузки данных из файлов (если требуется).

**Рекомендации по улучшению**
1. Добавить RST документацию для всех методов и класса, чтобы улучшить понимание кода и соответствовать стандартам.
2. Заменить стандартные блоки `try-except` на обработку ошибок через `logger.error` с выводом сообщения об ошибке и исключением.
3. Устранить дублирование логики работы с куками, вынеся общую логику в отдельный метод.
4. Использовать `j_dumps` для записи данных в файл если есть необходимость.
5. Переименовать переменные на более понятные имена.
6. Использовать `j_loads_ns` для загрузки данных из файла (если это требуется).
7. В комментариях после `#` строки должны содержать подробное объяснение следующего за ними блока кода.

**Оптимизированный код**
```python
"""
Модуль для работы с запросами к AliExpress.
=================================================

Этот модуль содержит класс :class:`AliRequests`, который используется для выполнения запросов к AliExpress,
управляет сессиями, куками и обрабатывает ответы.

Пример использования
--------------------

Пример использования класса `AliRequests`:

.. code-block:: python

    ali_requests = AliRequests(webdriver_for_cookies='chrome')
    response = ali_requests.make_get_request(url='https://example.com')
    if response:
        print(response.text)
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

import pickle
import requests
from pathlib import Path
from typing import List
from requests.cookies import RequestsCookieJar
from fake_useragent import UserAgent

from src import gs
# from src.utils.jjson import j_dumps # TODO: uncomment if needed
from src.logger.logger import logger


MODE = 'dev'


class AliRequests:
    """
    Класс для обработки запросов к AliExpress.

    Использует библиотеку `requests` для отправки запросов,
    управляет куками и сессиями, а также обрабатывает ответы.
    """

    def __init__(self, webdriver_for_cookies: str = 'chrome'):
        """
        Инициализирует класс AliRequests.

        :param webdriver_for_cookies: Имя вебдрайвера для загрузки кук.
        :type webdriver_for_cookies: str, optional
        """
        self.cookies_jar = RequestsCookieJar()
        self.session_id = None
        self.headers = {'User-Agent': UserAgent().random}
        self.session = requests.Session()
        # Код выполняет загрузку кук из файла
        self._load_webdriver_cookies_file(webdriver_for_cookies)

    def _load_webdriver_cookies_file(self, webdriver_for_cookies: str = 'chrome') -> bool:
        """
        Загружает куки из файла вебдрайвера.

        :param webdriver_for_cookies: Имя вебдрайвера.
        :type webdriver_for_cookies: str
        :return: True, если куки загружены успешно, False в противном случае.
        :rtype: bool
        """
        cookie_file_path = Path(gs.dir_cookies, 'aliexpress.com', webdriver_for_cookies, 'cookie')
        try:
            # Код открывает файл с куками в бинарном режиме для чтения
            with open(cookie_file_path, 'rb') as file:
                # Код загружает куки из файла
                cookies_list = pickle.load(file)
                for cookie in cookies_list:
                    # Код устанавливает куки в куки-контейнер
                    self.cookies_jar.set(
                        cookie['name'],
                        cookie['value'],
                        domain=cookie.get('domain', ''),
                        path=cookie.get('path', '/'),
                        secure=bool(cookie.get('secure', False)),
                        rest={'HttpOnly': cookie.get('HttpOnly', 'false'), 'SameSite': cookie.get('SameSite', 'unspecified')},
                        expires=cookie.get('expirationDate')
                    )
                logger.success(f"Cookies loaded from {cookie_file_path}")
                # Код выполняет обновление кук сессии
                self._refresh_session_cookies()
                return True
        except FileNotFoundError as ex:
            logger.error(f"Failed to load cookies from {cookie_file_path}", ex)
            return False
        except ValueError as ex:
             # Код обрабатывает ошибку ValueError
            logger.error(f"Failed to load cookies from {cookie_file_path}", ex)
            return False
        except Exception as ex:
            # Код обрабатывает другие ошибки
            logger.error("An error occurred while loading cookies", ex)
            return False

    def _refresh_session_cookies(self):
        """Обновляет куки сессии."""
        url = 'https://portals.aliexpress.com'
        try:
            # Код выполняет запрос к указанному url, для обновления кук
            if self.cookies_jar:
                resp = self.session.get(url, headers=self.headers, cookies=self.cookies_jar)
            else:
                resp = self.session.get(url, headers=self.headers)
            # Код обрабатывает session_id из кук
            self._handle_session_id(resp.cookies)
        except requests.RequestException as ex:
             # Код обрабатывает ошибку запроса
            logger.error(f"Failed to refresh session cookies from {url}", ex)
        except Exception as ex:
             # Код обрабатывает другие ошибки
            logger.error("An error occurred while refreshing session cookies", ex)

    def _handle_session_id(self, response_cookies):
        """
        Обрабатывает JSESSIONID в куках ответа.

        :param response_cookies: Куки из ответа сервера.
        :type response_cookies: requests.cookies.RequestsCookieJar
        """
        session_id_found = False
        for cookie in response_cookies:
            if cookie.name == 'JSESSIONID':
                 # Код сравнивает текущий session_id с новым
                if self.session_id == cookie.value:
                    return
                self.session_id = cookie.value
                # Код устанавливает куки с новым session_id
                self.cookies_jar.set(
                    cookie.name,
                    cookie.value,
                    domain=cookie.domain,
                    path=cookie.path,
                    secure=cookie.secure,
                    rest={'HttpOnly': cookie._rest.get('HttpOnly', 'false'), 'SameSite': cookie._rest.get('SameSite', 'unspecified')},
                    expires=cookie.expires
                )
                session_id_found = True
                break
         # Код логирует если session_id не найден
        if not session_id_found:
            logger.warning("JSESSIONID not found in response cookies")

    def make_get_request(self, url: str, cookies: List[dict] = None, headers: dict = None):
        """
        Выполняет GET запрос с куками.

        :param url: URL для GET запроса.
        :type url: str
        :param cookies: Список кук для запроса, defaults to None
        :type cookies: List[dict], optional
        :param headers: Заголовки запроса, defaults to None
        :type headers: dict, optional
        :return: Объект requests.Response в случае успеха, False в противном случае.
        :rtype: requests.Response or bool
        """
        headers = headers or self.headers
        try:
             # Код обновляет куки в сессии
            self.session.cookies.update(self.cookies_jar)
            resp = self.session.get(url, headers=headers)
            resp.raise_for_status()
            # Код обрабатывает session_id из ответа
            self._handle_session_id(resp.cookies)

            return resp
        except requests.RequestException as ex:
            # Код обрабатывает ошибку запроса
            logger.error(f"Request to {url} failed", ex)
            return False
        except Exception as ex:
             # Код обрабатывает другие ошибки
            logger.error(f"An error occurred while making a GET request to {url}", ex)
            return False

    def short_affiliate_link(self, link_url: str):
        """
        Получает сокращенную партнерскую ссылку.

        :param link_url: URL для сокращения.
        :type link_url: str
        :return: Объект requests.Response в случае успеха, False в противном случае.
        :rtype: requests.Response or bool
        """
        base_url = 'https://portals.aliexpress.com/affiportals/web/link_generator.htm'
        track_id = 'default'
        url = f"{base_url}?trackId={track_id}&targetUrl={link_url}"
        # Код выполняет GET запрос для получения сокращенной ссылки
        return self.make_get_request(url)
```