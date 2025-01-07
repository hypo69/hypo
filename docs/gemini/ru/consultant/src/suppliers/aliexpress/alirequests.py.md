# Анализ кода модуля `alirequests.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован, разбит на классы и функции.
    - Используется `logger` для логирования ошибок.
    - Применяется `fake_useragent` для генерации `User-Agent`.
    - Использование `requests.Session` для управления сессией.
    - Обработка кукисов.
    - Учтены разные случаи при загрузке кукис.
 -  Минусы
    -  Не все функции и методы снабжены комментариями в формате RST.
    -  В некоторых функциях избыточное использование try-except, можно использовать `logger.error` с `return False`
    -  Метод `_handle_session_id` можно упростить.
    -  Отсутствуют docstring к модулю.

**Рекомендации по улучшению**
- Добавить docstring к модулю в формате RST.
- Все функции и методы должны иметь docstring в формате RST.
- Избегать избыточного использования try-except, в основном через `logger.error` и `return False`.
- Упростить метод `_handle_session_id`.
- Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson`, если это необходимо, но в данном случае нет прямого использования json.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для работы с запросами к AliExpress.
=====================================================

Этот модуль содержит класс :class:`AliRequests`, который используется
для выполнения HTTP-запросов к AliExpress с использованием
сессий и обработки cookies.
"""
import pickle
import requests
from pathlib import Path
from typing import List, Optional, Dict
from requests.cookies import RequestsCookieJar
from urllib.parse import urlparse
from fake_useragent import UserAgent

from src import gs
from src.utils.jjson import j_dumps
from src.logger.logger import logger

class AliRequests:
    """
    Класс для управления запросами к AliExpress.

    Использует библиотеку `requests` для выполнения HTTP-запросов,
    управляет сессиями, обрабатывает cookies и генерирует
    короткие партнерские ссылки.
    """

    def __init__(self, webdriver_for_cookies: str = 'chrome'):
        """
        Инициализирует класс AliRequests.

        :param webdriver_for_cookies: Имя вебдрайвера для загрузки cookies.
        :type webdriver_for_cookies: str
        """
        self.cookies_jar = RequestsCookieJar()
        self.session_id = None
        self.headers = {'User-Agent': UserAgent().random}
        self.session = requests.Session()
        # Загружает куки из файла
        self._load_webdriver_cookies_file(webdriver_for_cookies)

    def _load_webdriver_cookies_file(self, webdriver_for_cookies: str = 'chrome') -> bool:
        """
        Загружает куки из файла вебдрайвера.

        :param webdriver_for_cookies: Имя вебдрайвера.
        :type webdriver_for_cookies: str
        :return: True, если куки успешно загружены, False в противном случае.
        :rtype: bool
        """
        cookie_file_path = Path(gs.dir_cookies, 'aliexpress.com', webdriver_for_cookies, 'cookie')
        
        try:
            # код исполняет открытие файла кукис в бинарном режиме для чтения
            with open(cookie_file_path, 'rb') as file:
                # код исполняет десериализацию кукис
                cookies_list = pickle.load(file)
                for cookie in cookies_list:
                    # код исполняет установку кукис в jar
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
                # Обновляет куки сессии после загрузки
                self._refresh_session_cookies()
                return True
        except FileNotFoundError as ex:
            logger.error(f"Failed to load cookies from {cookie_file_path}", ex)
            return False
        except (ValueError, Exception) as ex:
            logger.error("An error occurred while loading cookies", ex)
            return False
    
    def _refresh_session_cookies(self):
        """
        Обновляет куки сессии.

        Выполняет GET-запрос для обновления куки сессии,
        используя текущие cookies.
        """
        url = 'https://portals.aliexpress.com'
        try:
            # код исполняет отправку GET-запроса для обновления кукис
            resp = self.session.get(url, headers=self.headers, cookies=self.cookies_jar) if self.cookies_jar else self.session.get(url, headers=self.headers)
            self._handle_session_id(resp.cookies)
        except requests.RequestException as ex:
            logger.error(f"Failed to refresh session cookies from {url}", ex)
        except Exception as ex:
            logger.error("An error occurred while refreshing session cookies", ex)
    
    def _handle_session_id(self, response_cookies: RequestsCookieJar):
        """
        Обрабатывает JSESSIONID в cookies ответа.

        :param response_cookies: Cookies, полученные в ответе.
        :type response_cookies: requests.cookies.RequestsCookieJar
        """
        
        session_id = next((cookie.value for cookie in response_cookies if cookie.name == 'JSESSIONID'), None)
        if session_id:
            if self.session_id != session_id:
                self.session_id = session_id
                for cookie in response_cookies:
                    if cookie.name == 'JSESSIONID':
                        self.cookies_jar.set(
                        cookie.name,
                        cookie.value,
                        domain=cookie.domain,
                        path=cookie.path,
                        secure=cookie.secure,
                        rest={'HttpOnly': cookie._rest.get('HttpOnly', 'false'), 'SameSite': cookie._rest.get('SameSite', 'unspecified')},
                        expires=cookie.expires
                        )
                return
        logger.warning("JSESSIONID not found in response cookies")
       

    def make_get_request(self, url: str, cookies: Optional[List[Dict]] = None, headers: Optional[Dict] = None) -> Optional[requests.Response]:
        """
        Выполняет GET-запрос с cookies.

        :param url: URL для выполнения GET-запроса.
        :type url: str
        :param cookies: Список cookies для использования в запросе.
        :type cookies: Optional[List[Dict]]
        :param headers: Заголовки для включения в запрос.
        :type headers: Optional[Dict]
        :return: Объект requests.Response в случае успеха, False в противном случае.
        :rtype: Optional[requests.Response]
        """
        headers = headers or self.headers
        try:
            # Обновляет cookies сессии перед выполнением запроса
            self.session.cookies.update(self.cookies_jar)
            # код исполняет отправку GET-запроса
            resp = self.session.get(url, headers=headers)
            resp.raise_for_status()
            self._handle_session_id(resp.cookies)
            return resp
        except requests.RequestException as ex:
            logger.error(f"Request to {url} failed", ex)
            return False
        except Exception as ex:
            logger.error(f"An error occurred while making a GET request to {url}", ex)
            return False

    def short_affiliate_link(self, link_url: str) -> Optional[requests.Response]:
        """
        Генерирует короткую партнерскую ссылку.

        :param link_url: URL для сокращения.
        :type link_url: str
        :return: Объект requests.Response в случае успеха, False в противном случае.
        :rtype: Optional[requests.Response]
        """
        base_url = 'https://portals.aliexpress.com/affiportals/web/link_generator.htm'
        track_id = 'default'
        url = f"{base_url}?trackId={track_id}&targetUrl={link_url}"
        return self.make_get_request(url)
```