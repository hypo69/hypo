# Анализ кода модуля `base.py`

**Качество кода: 6/10**

-   **Плюсы:**
    -   Присутствует базовая структура для работы с API AliExpress.
    -   Реализованы функции для подписи запросов и выполнения HTTP-запросов.
    -   Используется логирование ошибок.
-   **Минусы:**
    -   Используется устаревшее форматирование логов.
    -   Отсутствует документация в формате reStructuredText (RST).
    -   Используются глобальные переменные.
    -   Многословное и неэффективное форматирование строк.
    -   Отсутствуют проверки типов и валидация данных.
    -   Не используются `j_loads` и `j_loads_ns` из `src.utils.jjson`.
    -   Множество магических строк.

**Рекомендации по улучшению:**

1.  **Документация:**
    -   Добавить docstring в формате RST для всех модулей, классов, функций и методов.
2.  **Логирование:**
    -   Использовать `from src.logger.logger import logger` для логирования.
    -   Улучшить формат логов, использовать f-строки.
    -   Избегать множественного вызова `logApiError` для одного события.
3.  **Обработка данных:**
    -   Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки JSON.
4.  **Структура:**
    -   Удалить неиспользуемый код и переменные.
    -   Разделить код на более мелкие функции для улучшения читаемости.
    -   Использовать константы для магических строк.
5.  **Безопасность:**
    -   Избегать хранения секретов в коде (вынести в переменные окружения или config).
6.  **Общее:**
    -   Сделать код более читаемым и понятным.
    -   Проверять типы входных данных.
    -   Добавить обработку исключений.

**Оптимизированный код:**

```python
"""
Модуль для работы с API AliExpress.
=========================================================================================

Этот модуль содержит классы и функции для отправки запросов к API AliExpress,
включая подпись запросов, формирование параметров и обработку ответов.

Пример использования
--------------------

Пример создания и выполнения запроса:

.. code-block:: python

    client = IopClient(server_url='https://api.example.com', app_key='your_app_key', app_secret='your_app_secret')
    request = IopRequest(api_pame='example.method')
    request.add_api_param('param1', 'value1')
    response = client.execute(request)
    print(response.body)
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
import hashlib
import hmac
import time
import socket
import platform
import requests
import os
from os.path import expanduser
from src.utils.jjson import j_loads
from src.logger.logger import logger

# Получаем домашнюю директорию пользователя
HOME_DIR = expanduser("~")
LOG_DIR = os.path.join(HOME_DIR, "logs")

# Проверяем, существует ли директория для логов, и создаем ее при необходимости
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Настраиваем базовый логгер
LOG_FILE = os.path.join(LOG_DIR, f"iopsdk.log.{time.strftime('%Y-%m-%d', time.localtime())}")

# Константы для API
SDK_VERSION = "iop-sdk-python-20220609"
APP_KEY = "app_key"
ACCESS_TOKEN = "session"
TIMESTAMP = "timestamp"
SIGN = "sign"
SIGN_METHOD = "sign_method"
PARTNER_ID = "partner_id"
METHOD = "method"
DEBUG = "debug"
SIMPLIFY = "simplify"
FORMAT = "format"
CODE = 'code'
TYPE = 'type'
MESSAGE = 'message'
REQUEST_ID = 'request_id'
LOG_LEVEL_DEBUG = "DEBUG"
LOG_LEVEL_INFO = "INFO"
LOG_LEVEL_ERROR = "ERROR"

def generate_sign(secret: str, api: str, parameters: dict) -> str:
    """Генерирует подпись для запроса API.

    :param secret: Секретный ключ приложения.
    :param api: Название API метода.
    :param parameters: Словарь параметров запроса.
    :return: Строка сгенерированной подписи.
    """
    sorted_keys = sorted(parameters.keys())
    if "/" in api:
        params_str = f"{api}{''.join(f'{key}{parameters[key]}' for key in sorted_keys)}"
    else:
        params_str = ''.join(f'{key}{parameters[key]}' for key in sorted_keys)

    hashed = hmac.new(secret.encode("utf-8"), params_str.encode("utf-8"), hashlib.sha256)
    return hashed.hexdigest().upper()

def convert_to_str(value: any) -> str:
    """Преобразует значение в строку.

    :param value: Значение любого типа.
    :return: Строковое представление значения.
    """
    if isinstance(value, str):
        return value
    if isinstance(value, bytes):
        return value.decode('utf-8') # Используем decode для корректной обработки
    return str(value)

def log_api_error(app_key: str, sdk_version: str, request_url: str, code: str, message: str):
    """Логирует ошибку API запроса.

    :param app_key: Ключ приложения.
    :param sdk_version: Версия SDK.
    :param request_url: URL запроса.
    :param code: Код ошибки.
    :param message: Сообщение об ошибке.
    """
    local_ip = socket.gethostbyname(socket.gethostname())
    platform_type = platform.platform()
    log_message = (
        f"{app_key}^_^"
        f"{sdk_version}^_^"
        f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}^_^"
        f"{local_ip}^_^"
        f"{platform_type}^_^"
        f"{request_url}^_^"
        f"{code}^_^"
        f"{message}"
    )
    logger.error(log_message)

class IopRequest:
    """Класс для представления запроса к API."""
    def __init__(self, api_pame: str, http_method: str = 'POST'):
        """Инициализирует объект запроса.

        :param api_pame: Название API метода.
        :param http_method: HTTP метод запроса (GET или POST).
        """
        self._api_params = {}
        self._file_params = {}
        self._api_pame = api_pame
        self._http_method = http_method
        self._simplify = "false"
        self._format = "json"

    def add_api_param(self, key: str, value: any):
        """Добавляет параметр к запросу.

        :param key: Ключ параметра.
        :param value: Значение параметра.
        """
        self._api_params[key] = value

    def add_file_param(self, key: str, value: any):
        """Добавляет файловый параметр к запросу.

        :param key: Ключ параметра.
        :param value: Значение параметра.
        """
        self._file_params[key] = value

    def set_simplify(self):
        """Устанавливает параметр simplify в true."""
        self._simplify = "true"

    def set_format(self, value: str):
        """Устанавливает формат ответа.

        :param value: Формат ответа.
        """
        self._format = value

class IopResponse:
    """Класс для представления ответа от API."""
    def __init__(self):
        """Инициализирует объект ответа."""
        self.type = None
        self.code = None
        self.message = None
        self.request_id = None
        self.body = None

    def __str__(self, *args, **kwargs):
         """Возвращает строковое представление объекта ответа."""
         return (
            f"type={convert_to_str(self.type)} "
            f"code={convert_to_str(self.code)} "
            f"message={convert_to_str(self.message)} "
            f"requestId={convert_to_str(self.request_id)}"
        )


class IopClient:
    """Класс для отправки запросов к API."""
    log_level = LOG_LEVEL_ERROR
    def __init__(self, server_url: str, app_key: str, app_secret: str, timeout: int = 30):
        """Инициализирует объект клиента API.

        :param server_url: URL сервера API.
        :param app_key: Ключ приложения.
        :param app_secret: Секретный ключ приложения.
        :param timeout: Тайм-аут запроса в секундах.
        """
        self._server_url = server_url
        self._app_key = app_key
        self._app_secret = app_secret
        self._timeout = timeout

    def execute(self, request: IopRequest, access_token: str = None) -> IopResponse:
        """Выполняет запрос к API.

        :param request: Объект запроса :class:`IopRequest`.
        :param access_token: Токен доступа (если требуется).
        :return: Объект ответа :class:`IopResponse`.
        """
        sys_params = {
            APP_KEY: self._app_key,
            SIGN_METHOD: "sha256",
            TIMESTAMP: str(int(round(time.time())))+'000',
            PARTNER_ID: SDK_VERSION,
            METHOD: request._api_pame,
            SIMPLIFY: request._simplify,
            FORMAT: request._format,
        }

        if self.log_level == LOG_LEVEL_DEBUG:
            sys_params[DEBUG] = 'true'

        if access_token:
            sys_params[ACCESS_TOKEN] = access_token

        all_params = sys_params.copy()
        all_params.update(request._api_params)
        all_params[SIGN] = generate_sign(self._app_secret, request._api_pame, all_params)

        full_url = self._server_url + "?"
        full_url += "&".join(f"{key}={all_params[key]}" for key in all_params)

        try:
            if request._http_method == 'POST' or request._file_params:
                r = requests.post(self._server_url, params=all_params, files=request._file_params, timeout=self._timeout)
            else:
                r = requests.get(self._server_url, params=all_params, timeout=self._timeout)
            r.raise_for_status()  # Вызывает исключение для HTTP ошибок

        except requests.exceptions.RequestException as err:
            log_api_error(self._app_key, SDK_VERSION, full_url, "HTTP_ERROR", str(err))
            raise

        response = IopResponse()
        try:
            json_obj = r.json()
        except json.JSONDecodeError as err:
             log_api_error(self._app_key, SDK_VERSION, full_url, "JSON_ERROR", str(err))
             response.code = "JSON_ERROR"
             response.message = str(err)
             return response

        if CODE in json_obj:
            response.code = json_obj[CODE]
        if TYPE in json_obj:
            response.type = json_obj[TYPE]
        if MESSAGE in json_obj:
            response.message = json_obj[MESSAGE]
        if REQUEST_ID in json_obj:
            response.request_id = json_obj[REQUEST_ID]


        if response.code != "0" and response.code is not None:
            log_api_error(self._app_key, SDK_VERSION, full_url, response.code, response.message)
        elif self.log_level in (LOG_LEVEL_DEBUG, LOG_LEVEL_INFO):
            log_api_error(self._app_key, SDK_VERSION, full_url, "", "")

        response.body = json_obj
        return response
```