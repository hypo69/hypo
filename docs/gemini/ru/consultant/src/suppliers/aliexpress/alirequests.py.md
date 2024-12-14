# Анализ кода модуля `alirequests`

**Качество кода**
7
-  Плюсы
    - Код структурирован в класс `AliRequests`, что обеспечивает инкапсуляцию логики работы с запросами к AliExpress.
    - Используется библиотека `requests` для HTTP-запросов и `pickle` для работы с cookies.
    - Присутствует логирование ошибок и информационных сообщений с помощью `logger`.
    - Код использует `fake_useragent` для генерации случайных User-Agent.
    - Используется `RequestsCookieJar` для управления куками.
    - Есть обработка исключений.
-  Минусы
    - Отсутствуют docstring для модуля, не все функции и методы имеют полные описания.
    - Некоторые docstring содержат `@param`, что не является стандартом RST.
    - Не везде используются f-строки для форматирования строк, что снижает читаемость.
    - Избыточное использование блоков `try-except`, можно сократить до одного с использованием `logger.error`.
    - Не хватает обработки ситуации, когда не удается обновить куки сессии.
    - Необходимо добавить обработку ситуации, когда не удается найти куки.
    - `webdriver_for_cookies` параметр используется без проверки его существования в файловой системе.
    - Не все переменные имеют docstring.
    - В методе `_handle_session_id` можно упростить логику проверки.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля, переменных класса и всех методов в формате RST.
2.  Заменить `@param` на `:param:` в docstring.
3.  Использовать f-строки для форматирования.
4.  Упростить блоки `try-except` и использовать `logger.error` для обработки ошибок.
5.  Добавить проверку на существование `webdriver_for_cookies` в файловой системе.
6.  Добавить логирование, если не получилось обновить куки сессии.
7.  Улучшить метод `_handle_session_id` с проверкой на наличие `JSESSIONID`.
8.  Уточнить тип `cookies` в параметрах метода `make_get_request` как `List[dict]`.
9.  Добавить проверку на существование файла куки и его корректности.
10. Сделать более явным использование `self.headers` и `self.cookies_jar`.
11. Улучшить обработку исключений в методе `_load_webdriver_cookies_file`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с запросами к AliExpress.
=========================================================================================

Этот модуль содержит класс :class:`AliRequests`, который используется для отправки запросов к AliExpress,
обработки cookies и генерации партнерских ссылок.

Пример использования
--------------------

Пример использования класса `AliRequests`:

.. code-block:: python

    ali_requests = AliRequests(webdriver_for_cookies='chrome')
    response = ali_requests.make_get_request('https://example.com')
    if response:
        print(response.text)

"""
import pickle
import requests
from pathlib import Path
from typing import List, Optional
from requests.cookies import RequestsCookieJar
from urllib.parse import urlparse
from fake_useragent import UserAgent

from src import gs
from src.utils.jjson import j_dumps
from src.logger.logger import logger


MODE = 'dev'


class AliRequests:
    """
    Класс для обработки запросов к AliExpress.

    Использует библиотеку `requests` для выполнения HTTP-запросов,
    а также управляет cookies и генерирует партнерские ссылки.
    """

    def __init__(self, webdriver_for_cookies: str = 'chrome'):
        """
        Инициализирует класс AliRequests.

        :param webdriver_for_cookies: Имя вебдрайвера для загрузки куки.
        :type webdriver_for_cookies: str
        """
        self.cookies_jar: RequestsCookieJar = RequestsCookieJar()
        """Куки для запросов."""
        self.session_id: Optional[str] = None
        """Идентификатор сессии."""
        self.headers: dict = {'User-Agent': UserAgent().random}
        """Заголовки для запросов."""
        self.session: requests.Session = requests.Session()
        """Сессия для запросов."""

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

        if not cookie_file_path.exists():
            logger.error(f"Файл куки не найден: {cookie_file_path}")
            return False

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
                logger.success(f"Куки успешно загружены из {cookie_file_path}")
                self._refresh_session_cookies()  # Обновление куки сессии после загрузки
                return True
        except (FileNotFoundError, ValueError) as ex:
            logger.error(f"Не удалось загрузить куки из {cookie_file_path}", exc_info=ex)
            return False
        except Exception as ex:
            logger.error("Произошла ошибка при загрузке куки", exc_info=ex)
            return False

    def _refresh_session_cookies(self):
        """Обновляет куки сессии."""
        url = 'https://portals.aliexpress.com'
        try:
            resp = self.session.get(url, headers=self.headers, cookies=self.cookies_jar)
            resp.raise_for_status()
            self._handle_session_id(resp.cookies)
        except requests.RequestException as ex:
            logger.error(f"Не удалось обновить куки сессии из {url}", exc_info=ex)
        except Exception as ex:
            logger.error("Произошла ошибка при обновлении куки сессии", exc_info=ex)

    def _handle_session_id(self, response_cookies):
        """
        Обрабатывает JSESSIONID в куки ответа.

        :param response_cookies: Куки из ответа сервера.
        :type response_cookies: requests.cookies.RequestsCookieJar
        """
        session_id_found = False
        for cookie in response_cookies:
            if cookie.name == 'JSESSIONID':
                if self.session_id == cookie.value:
                   return
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
            logger.warning("JSESSIONID не найден в куки ответа")

    def make_get_request(self, url: str, cookies: Optional[List[dict]] = None, headers: Optional[dict] = None) -> Optional[requests.Response]:
        """
        Выполняет GET-запрос с использованием куки.

        :param url: URL для GET-запроса.
        :type url: str
        :param cookies: Список куки для использования в запросе.
        :type cookies: Optional[List[dict]]
        :param headers: Дополнительные заголовки для включения в запрос.
        :type headers: Optional[dict]
        :return: Объект requests.Response в случае успеха, False в противном случае.
        :rtype: Optional[requests.Response]
        """
        headers = headers or self.headers
        try:
            self.session.cookies.update(self.cookies_jar)
            resp = self.session.get(url, headers=headers)
            resp.raise_for_status()
            self._handle_session_id(resp.cookies)
            return resp
        except requests.RequestException as ex:
            logger.error(f"Запрос к {url} не удался", exc_info=ex)
            return False
        except Exception as ex:
            logger.error(f"Произошла ошибка при выполнении GET-запроса к {url}", exc_info=ex)
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