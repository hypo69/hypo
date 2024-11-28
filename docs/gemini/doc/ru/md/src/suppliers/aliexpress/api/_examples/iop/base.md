# Модуль `hypotez/src/suppliers/aliexpress/api/_examples/iop/base.py`

## Обзор

Этот модуль предоставляет базовые классы и функции для работы с API AliExpress (IOP). Он содержит методы для создания запросов, обработки ответов и ведения логов ошибок.

## Классы

### `IopRequest`

**Описание**: Класс для создания и настройки запросов к API.

**Методы**:

- `add_api_param(key, value)`: Добавляет параметр к запросу.
  ```python
  def add_api_param(self, key, value):
      self._api_params[key] = value
  ```
- `add_file_param(key, value)`: Добавляет параметр файла к запросу.
  ```python
  def add_file_param(self, key, value):
      self._file_params[key] = value
  ```
- `set_simplify()`: Устанавливает параметр `simplify` для упрощения ответа.
  ```python
  def set_simplify(self):
      self._simplify = "true"
  ```
- `set_format(value)`: Устанавливает формат ответа (например, "json").
  ```python
  def set_format(self, value):
      self._format = value;
  ```

### `IopResponse`

**Описание**: Класс для обработки ответов от API.

**Методы**:

- `__init__(self)`: Инициализирует ответ с пустым телом.
  ```python
  def __init__(self):
      self.type = None
      self.code = None
      self.message = None
      self.request_id = None
      self.body = None
  ```
- `__str__(self, *args, **kwargs)`: Возвращает строковое представление ответа.
  ```python
  def __str__(self, *args, **kwargs):
      sb = "type=" + mixStr(self.type) + \
          " code=" + mixStr(self.code) + \
          " message=" + mixStr(self.message) + \
          " requestId=" + mixStr(self.request_id)
      return sb
  ```


### `IopClient`

**Описание**: Класс для взаимодействия с API AliExpress.

**Методы**:

- `__init__(self, server_url, app_key, app_secret, timeout=30)`: Инициализирует клиента с указанными параметрами.
  ```python
  def __init__(self, server_url, app_key, app_secret, timeout=30):
      self._server_url = server_url
      self._app_key = app_key
      self._app_secret = app_secret
      self._timeout = timeout
  ```
- `execute(self, request, access_token=None)`: Выполняет запрос к API.
  ```python
  def execute(self, request, access_token=None):
      # ... (Код выполнения запроса)
      return response
  ```

## Функции

### `sign(secret, api, parameters)`

**Описание**: Функция для вычисления подписи запроса.

**Параметры**:
- `secret` (str): Секретный ключ приложения.
- `api` (str):  Название API метода.
- `parameters` (dict): Параметры запроса.

**Возвращает**:
- str: Вычисленная подпись.

**Вызывает исключения**:
-  Возможны исключения, связанные с неправильным форматом входных данных, которые не описаны в коде.


### `mixStr(pstr)`

**Описание**: Функция для преобразования различных типов данных в строку UTF-8.

**Параметры**:
- `pstr`: Данные, которые нужно преобразовать.

**Возвращает**:
- str: Строковое представление данных.

### `logApiError(appkey, sdkVersion, requestUrl, code, message)`

**Описание**: Функция для записи сообщений об ошибках в лог.

**Параметры**:
- `appkey` (str): Ключ приложения.
- `sdkVersion` (str): Версия SDK.
- `requestUrl` (str): URL запроса.
- `code` (str): Код ошибки.
- `message` (str): Сообщение об ошибке.

**Возвращает**:
-  Не возвращает значения.


## Константы

Описание констант, используемых в модуле.


```