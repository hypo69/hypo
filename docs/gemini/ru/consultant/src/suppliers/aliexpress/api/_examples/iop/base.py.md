# Анализ кода модуля `base.py`

**Качество кода: 6/10**

- **Плюсы:**
    - Код структурирован в классы `IopRequest`, `IopResponse`, `IopClient`, что облегчает его понимание и использование.
    - Используется логирование для отслеживания ошибок и дебага.
    - Присутствует обработка исключений при выполнении HTTP-запросов.
    - Код совместим с Python 2 и 3.

- **Минусы:**
    - Не используется reStructuredText (RST) для документирования модуля, классов и функций.
    - Используются устаревшие конструкции, такие как `str().join()` вместо `"".join()`.
    - Есть магические строки, которые можно вынести в константы, например, `sha256`, `POST`, `GET`, `0`.
    - Не хватает документации к классам, методам и переменным.
    - Жестко задан формат логирования.
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Используется `Exception` для обработки всех исключений, что может усложнить отладку.
    - Код содержит избыточные комментарии.
    - Смешение логики обработки запроса и логирования.
    - Ошибки логируются даже в дебаг режиме.
    - Не используется f-строки

**Рекомендации по улучшению**
1.  Переписать документацию в формате RST.
2.  Использовать f-строки для форматирования строк.
3.  Использовать `"".join()` вместо `str().join()`.
4.  Вынести магические строки в константы.
5.  Использовать `from src.logger.logger import logger` и `logger.error` вместо стандартного `logging`.
6.  Разделить логику формирования запроса и логику обработки ответа.
7.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.loads` для чтения файлов.
8.  Уточнить обработку исключений, чтобы не перехватывать все исключения подряд.
9.  Удалить избыточные комментарии, а также комментарии, которые не несут смысловой нагрузки.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
 # <- venv win
"""
Модуль для взаимодействия с API AliExpress.
=========================================================================================
    
Этот модуль предоставляет классы для отправки запросов к API AliExpress и обработки ответов.
    
Содержит классы:
    - :class:`IopRequest` - для формирования запросов.
    - :class:`IopResponse` - для представления ответов.
    - :class:`IopClient` - для отправки запросов и обработки ответов.
    
    
Пример использования
--------------------
    
Пример создания и отправки запроса:
    
.. code-block:: python
    
    client = IopClient(server_url='https://api.example.com/rest', app_key='your_app_key', app_secret='your_app_secret')
    request = IopRequest(api_pame='example.method')
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
import socket
import platform
from os.path import expanduser
from typing import Any, Dict
import requests
from src.logger.logger import logger
from src.utils.jjson import j_loads

#  Настройка логирования
dir_path = expanduser("~")
logs_dir = os.path.join(dir_path, "logs")
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

#  Константы
P_SDK_VERSION = "iop-sdk-python-20220609"
P_APPKEY = "app_key"
P_ACCESS_TOKEN = "session"
P_TIMESTAMP = "timestamp"
P_SIGN = "sign"
P_SIGN_METHOD = "sign_method"
P_PARTNER_ID = "partner_id"
P_METHOD = "method"
P_DEBUG = "debug"
P_SIMPLIFY = "simplify"
P_FORMAT = "format"
P_CODE = 'code'
P_TYPE = 'type'
P_MESSAGE = 'message'
P_REQUEST_ID = 'request_id'
P_LOG_LEVEL_DEBUG = "DEBUG"
P_LOG_LEVEL_INFO = "INFO"
P_LOG_LEVEL_ERROR = "ERROR"
SHA256 = "sha256"
HTTP_POST = 'POST'
HTTP_GET = 'GET'
ZERO_CODE = "0"

def sign(secret: str, api: str, parameters: Dict[str, Any]) -> str:
    """
    Формирует подпись запроса.

    :param secret: Секретный ключ приложения.
    :param api: Имя API метода.
    :param parameters: Словарь параметров запроса.
    :return: Подпись запроса в верхнем регистре.
    """
    sorted_dict = sorted(parameters)
    if "/" in api:
        parameters_str = f"{api}{''.join(f'{key}{parameters[key]}' for key in sorted_dict)}"
    else:
        parameters_str = ''.join(f'{key}{parameters[key]}' for key in sorted_dict)

    h = hmac.new(secret.encode(encoding="utf-8"), parameters_str.encode(encoding="utf-8"), digestmod=hashlib.sha256)
    return h.hexdigest().upper()

def mix_str(pstr: Any) -> str:
    """
    Преобразует значение в строку, обрабатывая unicode.

    :param pstr: Значение для преобразования.
    :return: Строковое представление значения.
    """
    if isinstance(pstr, str):
        return pstr
    elif isinstance(pstr, str):
        return pstr.encode('utf-8')
    else:
        return str(pstr)

def log_api_error(appkey: str, sdk_version: str, request_url: str, code: str, message: str):
    """
    Логирует ошибку API запроса.

    :param appkey: Ключ приложения.
    :param sdk_version: Версия SDK.
    :param request_url: URL запроса.
    :param code: Код ошибки.
    :param message: Сообщение об ошибке.
    """
    local_ip = socket.gethostbyname(socket.gethostname())
    platform_type = platform.platform()
    log_message = f"{appkey}^_^{sdk_version}^_^{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}^_^{local_ip}^_^{platform_type}^_^{request_url}^_^{code}^_^{message}"
    logger.error(log_message)

class IopRequest:
    """
    Класс для формирования запроса к API.
    
    :ivar _api_params: Параметры API запроса.
    :vartype _api_params: Dict[str, Any]
    :ivar _file_params: Параметры файлов запроса.
    :vartype _file_params: Dict[str, Any]
    :ivar _api_pame: Имя API метода.
    :vartype _api_pame: str
    :ivar _http_method: HTTP метод запроса.
    :vartype _http_method: str
    :ivar _simplify: Флаг упрощения ответа.
    :vartype _simplify: str
    :ivar _format: Формат ответа.
    :vartype _format: str
    """
    def __init__(self, api_pame: str, http_method: str = HTTP_POST):
        """
        Инициализирует объект запроса.

        :param api_pame: Имя API метода.
        :param http_method: HTTP метод запроса (по умолчанию POST).
        """
        self._api_params: Dict[str, Any] = {}
        self._file_params: Dict[str, Any] = {}
        self._api_pame = api_pame
        self._http_method = http_method
        self._simplify = "false"
        self._format = "json"

    def add_api_param(self, key: str, value: Any):
        """
        Добавляет параметр в API запрос.

        :param key: Ключ параметра.
        :param value: Значение параметра.
        """
        self._api_params[key] = value

    def add_file_param(self, key: str, value: Any):
        """
        Добавляет файл в запрос.

        :param key: Ключ параметра файла.
        :param value: Значение параметра файла.
        """
        self._file_params[key] = value

    def set_simplify(self):
        """
        Устанавливает флаг упрощения ответа.
        """
        self._simplify = "true"

    def set_format(self, value: str):
        """
        Устанавливает формат ответа.

        :param value: Формат ответа.
        """
        self._format = value

class IopResponse:
    """
     Класс для представления ответа от API.
    
    :ivar type: Тип ответа.
    :vartype type: str | None
    :ivar code: Код ответа.
    :vartype code: str | None
    :ivar message: Сообщение ответа.
    :vartype message: str | None
    :ivar request_id: Идентификатор запроса.
    :vartype request_id: str | None
    :ivar body: Тело ответа.
    :vartype body: Any
    """
    def __init__(self):
        """
        Инициализирует объект ответа.
        """
        self.type: str | None = None
        self.code: str | None = None
        self.message: str | None = None
        self.request_id: str | None = None
        self.body: Any = None

    def __str__(self, *args, **kwargs) -> str:
        """
        Возвращает строковое представление объекта ответа.

        :return: Строковое представление ответа.
        """
        sb = f"type={mix_str(self.type)}" \
             f" code={mix_str(self.code)}" \
             f" message={mix_str(self.message)}" \
             f" requestId={mix_str(self.request_id)}"
        return sb

class IopClient:
    """
    Класс для отправки запросов к API.
    
    :ivar log_level: Уровень логирования.
    :vartype log_level: str
    :ivar _server_url: URL сервера API.
    :vartype _server_url: str
    :ivar _app_key: Ключ приложения.
    :vartype _app_key: str
    :ivar _app_secret: Секретный ключ приложения.
    :vartype _app_secret: str
    :ivar _timeout: Таймаут запроса.
    :vartype _timeout: int
    """
    log_level = P_LOG_LEVEL_ERROR

    def __init__(self, server_url: str, app_key: str, app_secret: str, timeout: int = 30):
        """
        Инициализирует объект клиента.

        :param server_url: URL сервера API.
        :param app_key: Ключ приложения.
        :param app_secret: Секретный ключ приложения.
        :param timeout: Таймаут запроса (по умолчанию 30 секунд).
        """
        self._server_url = server_url
        self._app_key = app_key
        self._app_secret = app_secret
        self._timeout = timeout

    def execute(self, request: IopRequest, access_token: str | None = None) -> IopResponse:
        """
        Выполняет запрос к API.

        :param request: Объект запроса IopRequest.
        :param access_token: Токен доступа (опционально).
        :return: Объект ответа IopResponse.
        :raises Exception: Если возникает ошибка при выполнении запроса.
        """
        sys_parameters = {
            P_APPKEY: self._app_key,
            P_SIGN_METHOD: SHA256,
            P_TIMESTAMP: f"{int(round(time.time()))}000",
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

        full_url = f"{self._server_url}?"
        for key, value in sign_parameter.items():
             full_url += f"{key}={str(value)}&"
        full_url = full_url[:-1]

        try:
            if request._http_method == HTTP_POST or request._file_params:
                r = requests.post(self._server_url, params=sign_parameter, files=request._file_params, timeout=self._timeout)
            else:
                r = requests.get(self._server_url, params=sign_parameter, timeout=self._timeout)

            r.raise_for_status()
        except requests.exceptions.RequestException as err:
            log_api_error(self._app_key, P_SDK_VERSION, full_url, "HTTP_ERROR", str(err))
            raise err

        response = IopResponse()
        try:
            jsonobj = j_loads(r.text)

            if P_CODE in jsonobj:
                response.code = jsonobj[P_CODE]
            if P_TYPE in jsonobj:
                response.type = jsonobj[P_TYPE]
            if P_MESSAGE in jsonobj:
                response.message = jsonobj[P_MESSAGE]
            if P_REQUEST_ID in jsonobj:
                response.request_id = jsonobj[P_REQUEST_ID]
            response.body = jsonobj

        except Exception as ex:
              logger.error(f'Ошибка парсинга JSON: {ex}')
              response.code = "PARSE_ERROR"
              response.message = str(ex)
              log_api_error(self._app_key, P_SDK_VERSION, full_url, response.code, response.message)
              return response

        if response.code is not None and response.code != ZERO_CODE:
            log_api_error(self._app_key, P_SDK_VERSION, full_url, response.code, response.message)
        elif self.log_level in (P_LOG_LEVEL_DEBUG, P_LOG_LEVEL_INFO):
             log_api_error(self._app_key, P_SDK_VERSION, full_url, "", "")

        return response
```