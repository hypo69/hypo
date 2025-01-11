# Анализ кода модуля `alirequests.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разбит на логические блоки.
    - Используется `logger` для логирования ошибок.
    - Применяется `requests.Session()` для повторного использования сессий.
    -  Используются f-строки для форматирования строк.
    -  Присутствует документация для классов и методов.
-  Минусы
    - Не все функции имеют docstring в формате RST (не указаны параметры, возвращаемые значения, исключения)
    - Есть дублирование кода в блоках `except` (вывод в logger), это можно упростить.
    - Метод `_handle_session_id` имеет лишнюю проверку `if self.session_id == cookie.value`
    -  Использование `logger.success` является не стандартным, лучше использовать `logger.info`.
    - Не везде соблюдается использование одинарных кавычек.

**Рекомендации по улучшению**

1.  Добавить подробные docstring в формате RST для всех методов, с описанием параметров, возвращаемых значений и возможных исключений.
2.  Упростить обработку исключений в методах, вынеся повторяющийся код в отдельную функцию или используя более общую обработку.
3.  Убрать лишнюю проверку в `_handle_session_id`, если нужно обновить `JSESSIONID`, то нужно его всегда обновлять, иначе не обновлять.
4.  Заменить `logger.success` на `logger.info` для логирования успешных операций.
5.  Унифицировать использование кавычек (использовать одинарные кавычки везде, кроме операций вывода).
6. Добавить описание модуля в начале файла

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для обработки запросов к AliExpress.
===========================================
Этот модуль содержит класс :class:`AliRequests`, который используется для отправки HTTP-запросов к AliExpress,
управления куки и получения коротких ссылок.
"""
import pickle
import requests
from pathlib import Path
from typing import List, Optional
from requests.cookies import RequestsCookieJar
from urllib.parse import urlparse
from fake_useragent import UserAgent

from src import gs
# from src.utils.jjson import j_dumps # не используется
from src.logger.logger import logger


class AliRequests:
    """
    Класс для отправки запросов к AliExpress.

    Этот класс управляет куки, сессиями и отправляет GET запросы к AliExpress.
    """

    def __init__(self, webdriver_for_cookies: str = 'chrome'):
        """
        Инициализация класса AliRequests.

        Args:
            webdriver_for_cookies (str, optional): Имя вебдрайвера для загрузки куки. По умолчанию 'chrome'.
        """
        self.cookies_jar = RequestsCookieJar()
        self.session_id = None
        self.headers = {'User-Agent': UserAgent().random}
        self.session = requests.Session()

        self._load_webdriver_cookies_file(webdriver_for_cookies)

    def _load_webdriver_cookies_file(self, webdriver_for_cookies: str = 'chrome') -> bool:
        """
        Загружает куки из файла вебдрайвера.

        Args:
            webdriver_for_cookies (str): Имя вебдрайвера.

        Returns:
            bool: True, если куки успешно загружены, False в противном случае.

        Raises:
            FileNotFoundError: Если файл куки не найден.
            ValueError: Если возникают ошибки при чтении файла куки.
            Exception: При возникновении других ошибок.
        """
        cookie_file_path = Path(gs.dir_cookies, 'aliexpress.com', webdriver_for_cookies, 'cookie')

        try:
            with open(cookie_file_path, 'rb') as file:
                cookies_list = pickle.load(file)
                for cookie in cookies_list:
                    self.cookies_jar.set(
                        cookie['name'],
                        cookie['value'],
                        domain=cookie.get('domain', ''),
                        path=cookie.get('path', '/'),
                        secure=bool(cookie.get('secure', False)),
                        rest={'HttpOnly': cookie.get('HttpOnly', 'false'), 'SameSite': cookie.get('SameSite', 'unspecified')},
                        expires=cookie.get('expirationDate')
                    )
                logger.info(f"Cookies loaded from {cookie_file_path}")
                self._refresh_session_cookies()
                return True
        except FileNotFoundError as ex:
            logger.error(f"Failed to load cookies from {cookie_file_path}", exc_info=ex)
            return False
        except ValueError as ex:
            logger.error(f"Failed to load cookies from {cookie_file_path}", exc_info=ex)
            return False
        except Exception as ex:
            logger.error("An error occurred while loading cookies", exc_info=ex)
            return False

    def _refresh_session_cookies(self):
        """Обновляет куки сессии."""
        url = 'https://portals.aliexpress.com'
        try:
            if self.cookies_jar:
                resp = self.session.get(url, headers=self.headers, cookies=self.cookies_jar)
            else:
                resp = self.session.get(url, headers=self.headers)

            self._handle_session_id(resp.cookies)
        except requests.RequestException as ex:
            logger.error(f"Failed to refresh session cookies from {url}", exc_info=ex)
        except Exception as ex:
            logger.error("An error occurred while refreshing session cookies", exc_info=ex)

    def _handle_session_id(self, response_cookies):
        """
        Обрабатывает JSESSIONID в куки ответа.

        Args:
            response_cookies (requests.cookies.RequestsCookieJar): Куки ответа.
        """
        session_id_found = False
        for cookie in response_cookies:
            if cookie.name == 'JSESSIONID':
                # Обновляет session_id и куки, если JSESSIONID найден
                self.session_id = cookie.value
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

        if not session_id_found:
            logger.warning("JSESSIONID not found in response cookies")


    def make_get_request(self, url: str, cookies: Optional[List[dict]] = None, headers: Optional[dict] = None) -> Optional[requests.Response]:
        """
        Выполняет GET запрос с куки.

        Args:
            url (str): URL для отправки GET запроса.
            cookies (List[dict], optional): Список куки для использования в запросе.
            headers (dict, optional): Дополнительные заголовки для запроса.

        Returns:
            requests.Response: Объект requests.Response, если запрос успешен, иначе None.
        Raises:
            requests.RequestException: При ошибке HTTP запроса
            Exception: При возникновении других ошибок.
        """
        headers = headers or self.headers
        try:
            self.session.cookies.update(self.cookies_jar)
            resp = self.session.get(url, headers=headers)
            resp.raise_for_status()

            self._handle_session_id(resp.cookies)

            return resp
        except requests.RequestException as ex:
            logger.error(f"Request to {url} failed", exc_info=ex)
            return None
        except Exception as ex:
            logger.error(f"An error occurred while making a GET request to {url}", exc_info=ex)
            return None

    def short_affiliate_link(self, link_url: str) -> Optional[requests.Response]:
        """
        Получает короткую партнерскую ссылку.

        Args:
            link_url (str): URL для сокращения.

        Returns:
            requests.Response: Объект requests.Response, если запрос успешен, иначе None.
        """
        base_url = 'https://portals.aliexpress.com/affiportals/web/link_generator.htm'
        track_id = 'default'
        url = f"{base_url}?trackId={track_id}&targetUrl={link_url}"
        return self.make_get_request(url)

```