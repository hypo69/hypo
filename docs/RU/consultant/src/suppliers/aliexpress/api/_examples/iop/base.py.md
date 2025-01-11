## Анализ кода модуля `base.py`

**Качество кода**
8/10
- Плюсы:
    - Код хорошо структурирован и разбит на классы `IopRequest`, `IopResponse` и `IopClient`, что способствует его пониманию и поддержке.
    - Присутствует логирование ошибок с помощью модуля `logging`.
    - Используются константы для параметров API, что облегчает сопровождение.
- Минусы:
    -  Не используется `from src.logger.logger import logger` для логирования.
    -  Смешение использования `logging` и `logger`, в проекте используется единый `logger`.
    -  Используются двойные кавычки в коде, в то время как требуется использовать одинарные.
    -  Не хватает документации в формате RST для классов и методов.
    -  Код содержит устаревший импорт `unicode`.
    -  Отсутствует обработка ошибок при чтении JSON.
    -  Форматирование строк с помощью `%` является устаревшим, рекомендуется использовать f-strings.
    -  Используется `str().join()` для конкатенации строк, что менее эффективно, чем f-strings.

**Рекомендации по улучшению**

1. **Импорты**:
   - Заменить `import logging` на `from src.logger.logger import logger`.
   - Удалить импорт `unicode`.
2.  **Форматирование**:
    - Заменить двойные кавычки на одинарные в коде.
    - Использовать f-strings для форматирования строк.
3.  **Логирование**:
    - Использовать `logger.error` вместо `logging.error`.
    - Избегать избыточного использования `try-except` и обрабатывать ошибки с помощью `logger.error`.
4.  **Документация**:
    - Добавить docstrings в формате RST для классов и методов.
5.  **Обработка JSON**:
    - Использовать `j_loads` из `src.utils.jjson` для обработки JSON.
6. **Улучшения**:
     - Использовать `os.path.join` для корректного создания путей.
     - Упростить форматирование строк в методе `__str__` класса `IopResponse` с использованием f-strings.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
# <- venv win
"""
Модуль для работы с API AliExpress через IOP.
=========================================================================================

Этот модуль содержит классы для выполнения запросов к API AliExpress,
обработки ответов и управления параметрами запроса.

Пример использования
--------------------

Пример создания и выполнения запроса:

.. code-block:: python

    client = IopClient(server_url='https://api.example.com/rest', app_key='your_app_key', app_secret='your_app_secret')
    request = IopRequest(api_pame='example.api.method')
    request.add_api_param('param1', 'value1')
    response = client.execute(request)
    print(response.body)
"""
import time
import hmac
import hashlib
import mimetypes
import itertools
import random
import os
from os.path import expanduser, join
import socket
import platform
import requests
from src.logger.logger import logger
from src.utils.jjson import j_loads


dir = expanduser('~')
logs_dir = join(dir, 'logs')
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

log_file = join(logs_dir, f'iopsdk.log.{time.strftime("%Y-%m-%d", time.localtime())}')

# from src.logger import logger
# logger = logging.getLogger(__name__) # Заменено на from src.logger.logger import logger
logger.setLevel(level=logger.ERROR)  # Заменено на from src.logger.logger import logger
handler = logger.FileHandler(log_file)  # Заменено на from src.logger.logger import logger
handler.setLevel(logger.ERROR)  # Заменено на from src.logger.logger import logger
formatter = logger.Formatter('%(message)s')  # Заменено на from src.logger.logger import logger
handler.setFormatter(formatter)  # Заменено на from src.logger.logger import logger
logger.addHandler(handler)  # Заменено на from src.logger.logger import logger

P_SDK_VERSION = 'iop-sdk-python-20220609'

P_APPKEY = 'app_key'
P_ACCESS_TOKEN = 'session'
P_TIMESTAMP = 'timestamp'
P_SIGN = 'sign'
P_SIGN_METHOD = 'sign_method'
P_PARTNER_ID = 'partner_id'
P_METHOD = 'method'
P_DEBUG = 'debug'
P_SIMPLIFY = 'simplify'
P_FORMAT = 'format'

P_CODE = 'code'
P_TYPE = 'type'
P_MESSAGE = 'message'
P_REQUEST_ID = 'request_id'

P_LOG_LEVEL_DEBUG = 'DEBUG'
P_LOG_LEVEL_INFO = 'INFO'
P_LOG_LEVEL_ERROR = 'ERROR'


def sign(secret, api, parameters):
    """Генерирует подпись запроса.

    Args:
        secret (str): Секретный ключ приложения.
        api (str): Название API метода.
        parameters (dict): Параметры запроса.

    Returns:
        str: Подпись запроса.
    """
    sort_dict = sorted(parameters)
    if '/' in api:
        parameters_str = f'{api}{"".join(f"{key}{parameters[key]}" for key in sort_dict)}'
    else:
        parameters_str = ''.join(f'{key}{parameters[key]}' for key in sort_dict)

    h = hmac.new(secret.encode(encoding='utf-8'), parameters_str.encode(encoding='utf-8'), digestmod=hashlib.sha256)

    return h.hexdigest().upper()


def mixStr(pstr):
    """Преобразует значение в строку.

    Args:
        pstr (Any): Значение для преобразования.

    Returns:
        str: Строковое представление значения.
    """
    if isinstance(pstr, str):
        return pstr
    else:
        return str(pstr)


def logApiError(appkey, sdkVersion, requestUrl, code, message):
    """Логирует ошибку API запроса.

    Args:
        appkey (str): Ключ приложения.
        sdkVersion (str): Версия SDK.
        requestUrl (str): URL запроса.
        code (str): Код ошибки.
        message (str): Сообщение об ошибке.
    """
    localIp = socket.gethostbyname(socket.gethostname())
    platformType = platform.platform()
    logger.error(f'{appkey}^_{sdkVersion}^_{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}^_{localIp}^_{platformType}^_{requestUrl}^_{code}^_{message}')


class IopRequest(object):
    """
    Класс для представления запроса к IOP API.

    Args:
        api_pame (str): Имя API метода.
        http_method (str, optional): HTTP метод запроса. Defaults to 'POST'.
    """
    def __init__(self, api_pame, http_method='POST'):
        """Инициализация объекта запроса."""
        self._api_params = {}
        self._file_params = {}
        self._api_pame = api_pame
        self._http_method = http_method
        self._simplify = 'false'
        self._format = 'json'

    def add_api_param(self, key, value):
        """Добавляет параметр API запроса.

        Args:
            key (str): Ключ параметра.
            value (Any): Значение параметра.
        """
        self._api_params[key] = value

    def add_file_param(self, key, value):
        """Добавляет файл к запросу.

        Args:
            key (str): Ключ параметра.
            value (Any): Значение параметра.
        """
        self._file_params[key] = value

    def set_simplify(self):
        """Устанавливает флаг упрощенного ответа."""
        self._simplify = 'true'

    def set_format(self, value):
        """Устанавливает формат ответа.

        Args:
            value (str): Формат ответа.
        """
        self._format = value


class IopResponse(object):
    """Класс для представления ответа от IOP API."""
    def __init__(self):
        """Инициализация объекта ответа."""
        self.type = None
        self.code = None
        self.message = None
        self.request_id = None
        self.body = None

    def __str__(self, *args, **kwargs):
        """Возвращает строковое представление ответа.

        Returns:
            str: Строковое представление ответа.
        """
        sb = f'type={mixStr(self.type)} code={mixStr(self.code)} message={mixStr(self.message)} requestId={mixStr(self.request_id)}'
        return sb


class IopClient(object):
    """
    Класс для выполнения запросов к IOP API.

    Args:
        server_url (str): URL сервера API.
        app_key (str): Ключ приложения.
        app_secret (str): Секретный ключ приложения.
        timeout (int, optional): Время ожидания запроса. Defaults to 30.
    """
    log_level = P_LOG_LEVEL_ERROR

    def __init__(self, server_url, app_key, app_secret, timeout=30):
        """Инициализация клиента API."""
        self._server_url = server_url
        self._app_key = app_key
        self._app_secret = app_secret
        self._timeout = timeout

    def execute(self, request, access_token=None):
        """Выполняет запрос к API.

        Args:
            request (IopRequest): Объект запроса.
            access_token (str, optional): Токен доступа. Defaults to None.

        Returns:
             IopResponse: Объект ответа.
        """
        sys_parameters = {
            P_APPKEY: self._app_key,
            P_SIGN_METHOD: 'sha256',
            P_TIMESTAMP: f'{int(round(time.time()))}000',
            P_PARTNER_ID: P_SDK_VERSION,
            P_METHOD: request._api_pame,
            P_SIMPLIFY: request._simplify,
            P_FORMAT: request._format
        }

        if self.log_level == P_LOG_LEVEL_DEBUG:
            sys_parameters[P_DEBUG] = 'true'

        if access_token:
            sys_parameters[P_ACCESS_TOKEN] = access_token

        application_parameter = request._api_params

        sign_parameter = sys_parameters.copy()
        sign_parameter.update(application_parameter)

        sign_parameter[P_SIGN] = sign(self._app_secret, request._api_pame, sign_parameter)

        API_DOMAIN = self._server_url

        full_url = f'{API_DOMAIN}?'
        for key in sign_parameter:
            full_url += f'{key}={sign_parameter[key]}&'
        full_url = full_url[0:-1]

        try:
            if request._http_method == 'POST' or len(request._file_params) != 0:
                r = requests.post(API_DOMAIN, data=sign_parameter, files=request._file_params, timeout=self._timeout)
            else:
                r = requests.get(API_DOMAIN, params=sign_parameter, timeout=self._timeout)
            r.raise_for_status() # проверка на HTTP ошибки
        except requests.exceptions.RequestException as err:
            logApiError(self._app_key, P_SDK_VERSION, full_url, 'HTTP_ERROR', str(err))
            raise err

        response = IopResponse()
        try:
            jsonobj = j_loads(r.text)
        except Exception as ex:
            logApiError(self._app_key, P_SDK_VERSION, full_url, 'JSON_ERROR', str(ex))
            raise ex

        if P_CODE in jsonobj:
            response.code = jsonobj[P_CODE]
        if P_TYPE in jsonobj:
            response.type = jsonobj[P_TYPE]
        if P_MESSAGE in jsonobj:
            response.message = jsonobj[P_MESSAGE]
        if P_REQUEST_ID in jsonobj:
            response.request_id = jsonobj[P_REQUEST_ID]

        if response.code is not None and response.code != '0':
            logApiError(self._app_key, P_SDK_VERSION, full_url, response.code, response.message)
        else:
            if self.log_level == P_LOG_LEVEL_DEBUG or self.log_level == P_LOG_LEVEL_INFO:
                logApiError(self._app_key, P_SDK_VERSION, full_url, '', '')

        response.body = jsonobj

        return response