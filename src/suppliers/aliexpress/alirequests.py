## \file hypotez/src/suppliers/aliexpress/alirequests.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.suppliers.aliexpress """
MODE = 'debug'
""" module: src.suppliers.aliexpress """
MODE = 'debug'
""" AliExpress requests handling.
alirequests.py
│
├── pickle
│
├── requests
│   ├── requests.sessions.Session
│   ├── requests.cookies.RequestsCookieJar
│   ├── requests.RequestException
│
├── pathlib.Path
│
├── typing.List
│
├── urllib.parse.urlparse
│
├── fake_useragent.UserAgent
│
├── src.settings.gs
│   └── gs.dir_cookies
│
├── src.utils.j_dumps
│
├── src.logger.logger
│   ├── logger.success()
│   ├── logger.error()
│   ├── logger.warning()
│
└── src.suppliers.supplier.Supplier
    ├── Supplier
    ├── Supplier.__init__()

"""

import pickle
import requests
from pathlib import Path
from typing import List
from requests.cookies import RequestsCookieJar
from urllib.parse import urlparse
from fake_useragent import UserAgent

from header import gs
from src.utils import j_dumps
from src.logger import logger

class AliRequests:
    """Handles requests to AliExpress using the requests library."""

    def __init__(self, webdriver_for_cookies: str = 'chrome'):
        """ Initializes the AliRequests class.

        @param webdriver_for_cookies The name of the webdriver for loading cookies.
        """
        self.cookies_jar = RequestsCookieJar()
        self.session_id = None
        self.headers = {'User-Agent': UserAgent().random}
        self.session = requests.Session()
        
        self._load_webdriver_cookies_file(webdriver_for_cookies)

    def _load_webdriver_cookies_file(self, webdriver_for_cookies: str = 'chrome') -> bool:
        """ Loads cookies from a webdriver file.

        @param webdriver_for_cookies The name of the webdriver.
        @returns True if cookies loaded successfully, False otherwise.
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
                logger.success(f"Cookies loaded from {cookie_file_path}")
                self._refresh_session_cookies()  # Refresh session cookies after loading
                return True
        except (FileNotFoundError, ValueError) as ex:
            logger.error(f"Failed to load cookies from {cookie_file_path}", ex)
            return False
        except Exception as ex:
            logger.error("An error occurred while loading cookies", ex)
            return False

    def _refresh_session_cookies(self):
        """ Refreshes session cookies."""
        url = 'https://portals.aliexpress.com'
        try:
            if self.cookies_jar:
                resp = self.session.get(url, headers=self.headers, cookies=self.cookies_jar)
            else:
                resp = self.session.get(url, headers=self.headers)

            self._handle_session_id(resp.cookies)
        except requests.RequestException as ex:
            logger.error(f"Failed to refresh session cookies from {url}", ex)
        except Exception as ex:
            logger.error("An error occurred while refreshing session cookies", ex)

    def _handle_session_id(self, response_cookies):
        """ Handles the JSESSIONID in response cookies."""
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
            logger.warning("JSESSIONID not found in response cookies")

    def make_get_request(self, url: str, cookies: List[dict] = None, headers: dict = None):
        """ Makes a GET request with cookies.

        @param url The URL to make the GET request to.
        @param cookies List of cookies to use for the request.
        @param headers Optional headers to include in the request.

        @returns requests.Response object if successful, False otherwise.
        """
        headers = headers or self.headers
        try:
            self.session.cookies.update(self.cookies_jar)
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

    def short_affiliate_link(self, link_url: str):
        """ Get a short affiliate link.

        @param link_url The URL to shorten.

        @returns requests.Response object if successful, False otherwise.
        """
        base_url = 'https://portals.aliexpress.com/affiportals/web/link_generator.htm'
        track_id = 'default'
        url = f"{base_url}?trackId={track_id}&targetUrl={link_url}"
        return self.make_get_request(url)

