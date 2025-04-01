# Модуль для работы с куки (cookies)
## Обзор

Модуль `cookies.py` предназначен для управления и загрузки куки (cookies) из различных источников, таких как браузеры и файлы (`.har` и `.json`). Он предоставляет функциональность для автоматического получения куки из поддерживаемых браузеров, а также для чтения куки из файлов, что позволяет использовать их в различных запросах.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для автоматизации процессов, связанных с веб-скрапингом и тестированием, где требуется работа с куки для имитации поведения пользователя. Он позволяет загружать куки из различных браузеров, таких как Chrome, Firefox, Opera и других, а также из файлов в форматах HAR и JSON.

## Классы

### `CookiesConfig`

**Описание**:
Класс `CookiesConfig` предназначен для хранения конфигурации куки, включая сами куки и директорию, в которой они хранятся.

**Принцип работы**:
Класс содержит статические переменные для хранения куки и директории с куками. Это позволяет использовать куки, полученные из разных источников, в одном месте.

**Методы**:
- Нет методов, только статические переменные.

**Переменные класса**:
- `cookies (Dict[str, Cookies])`: Словарь, содержащий куки для каждого домена.
- `cookies_dir (str)`: Путь к директории, в которой хранятся файлы с куками. По умолчанию `"./har_and_cookies"`.

## Функции

### `g4f(domain_name: str) -> list`

```python
def g4f(domain_name: str) -> list:
    """
    Load cookies from the \'g4f\' browser (if exists).

    Args:
        domain_name (str): The domain for which to load cookies.

    Returns:
        list: List of cookies.
    """
    ...
```

**Назначение**:
Функция загружает куки из браузера `'g4f'`, если он существует.

**Параметры**:
- `domain_name (str)`: Домен, для которого необходимо загрузить куки.

**Возвращает**:
- `list`: Список куки. Возвращает пустой список, если `platformdirs` не установлен или файл с куками не существует.

**Как работает функция**:
1. Проверяет, установлен ли пакет `platformdirs`. Если нет, возвращает пустой список.
2. Определяет директорию пользовательских конфигураций для `'g4f'` с помощью `user_config_dir("g4f")`.
3. Формирует путь к файлу с куками: `os.path.join(user_data_dir, "Default", "Cookies")`.
4. Проверяет, существует ли файл с куками. Если нет, возвращает пустой список.
5. Если файл существует, вызывает функцию `chrome` из `browser_cookie3` для загрузки куки из файла и возвращает результат.

**Примеры**:
```python
domain = "example.com"
cookies = g4f(domain)
if cookies:
    print(f"Cookies for {domain}: {cookies}")
else:
    print(f"No cookies found for {domain} in g4f browser.")
```

### `get_cookies(domain_name: str, raise_requirements_error: bool = True, single_browser: bool = False, cache_result: bool = True) -> Dict[str, str]`

```python
def get_cookies(domain_name: str, raise_requirements_error: bool = True, single_browser: bool = False, cache_result: bool = True) -> Dict[str, str]:
    """
    Load cookies for a given domain from all supported browsers and cache the results.

    Args:
        domain_name (str): The domain for which to load cookies.

    Returns:
        Dict[str, str]: A dictionary of cookie names and values.
    """
    ...
```

**Назначение**:
Функция загружает куки для заданного домена из всех поддерживаемых браузеров и кэширует результаты.

**Параметры**:
- `domain_name (str)`: Домен, для которого необходимо загрузить куки.
- `raise_requirements_error (bool, optional)`: Если `True`, вызывает исключение `MissingRequirementsError`, если не установлен пакет `browser_cookie3`. По умолчанию `True`.
- `single_browser (bool, optional)`: Если `True`, загружает куки только из одного браузера. По умолчанию `False`.
- `cache_result (bool, optional)`: Если `True`, кэширует результаты загрузки куки. По умолчанию `True`.

**Возвращает**:
- `Dict[str, str]`: Словарь, содержащий имена и значения куки.

**Как работает функция**:
1. Проверяет, нужно ли использовать кэшированные куки. Если да, и куки для данного домена уже есть в кэше (`CookiesConfig.cookies`), возвращает кэшированные куки.
2. Вызывает функцию `load_cookies_from_browsers` для загрузки куки из браузеров.
3. Если `cache_result` равен `True`, сохраняет загруженные куки в кэш (`CookiesConfig.cookies`).
4. Возвращает загруженные куки.

**Примеры**:
```python
domain = "example.com"
cookies = get_cookies(domain)
if cookies:
    print(f"Cookies for {domain}: {cookies}")
else:
    print(f"No cookies found for {domain}.")
```

### `set_cookies(domain_name: str, cookies: Cookies = None) -> None`

```python
def set_cookies(domain_name: str, cookies: Cookies = None) -> None:
    """
    Sets cookies for a given domain.

    Args:
        domain_name (str): The domain for which to set cookies.
        cookies (Cookies, optional): Cookies to set for the domain. If None, cookies for the domain are removed. Defaults to None.

    Returns:
        None
    """
    ...
```

**Назначение**:
Функция устанавливает куки для заданного домена.

**Параметры**:
- `domain_name (str)`: Домен, для которого необходимо установить куки.
- `cookies (Cookies, optional)`: Куки, которые необходимо установить для домена. Если `None`, куки для домена будут удалены. По умолчанию `None`.

**Возвращает**:
- `None`

**Как работает функция**:
1. Если переданы куки (`cookies` не `None`), сохраняет их в кэш (`CookiesConfig.cookies`).
2. Если `cookies` равен `None`, и куки для данного домена есть в кэше, удаляет их из кэша.

**Примеры**:
```python
domain = "example.com"
new_cookies = {"cookie1": "value1", "cookie2": "value2"}
set_cookies(domain, new_cookies)
print(f"Cookies for {domain} set successfully.")

set_cookies(domain)
print(f"Cookies for {domain} removed successfully.")
```

### `load_cookies_from_browsers(domain_name: str, raise_requirements_error: bool = True, single_browser: bool = False) -> Cookies`

```python
def load_cookies_from_browsers(domain_name: str, raise_requirements_error: bool = True, single_browser: bool = False) -> Cookies:
    """
    Helper function to load cookies from various browsers.

    Args:
        domain_name (str): The domain for which to load cookies.

    Returns:
        Dict[str, str]: A dictionary of cookie names and values.
    """
    ...
```

**Назначение**:
Вспомогательная функция для загрузки куки из различных браузеров.

**Параметры**:
- `domain_name (str)`: Домен, для которого необходимо загрузить куки.
- `raise_requirements_error (bool, optional)`: Если `True`, вызывает исключение `MissingRequirementsError`, если не установлен пакет `browser_cookie3`. По умолчанию `True`.
- `single_browser (bool, optional)`: Если `True`, загружает куки только из одного браузера. По умолчанию `False`.

**Возвращает**:
- `Dict[str, str]`: Словарь, содержащий имена и значения куки.

**Как работает функция**:
1. Проверяет, установлен ли пакет `browser_cookie3`. Если нет, и `raise_requirements_error` равен `True`, вызывает исключение `MissingRequirementsError`. В противном случае возвращает пустой словарь.
2. Инициализирует пустой словарь `cookies` для хранения куки.
3. Перебирает список браузеров (`browsers`).
4. Для каждого браузера пытается загрузить куки с помощью соответствующей функции (`cookie_fn`).
5. Если загрузка прошла успешно, добавляет куки в словарь `cookies`, исключая куки с истекшим сроком действия.
6. Если `single_browser` равен `True`, останавливает перебор браузеров после первого успешного получения куки.
7. Обрабатывает исключения `BrowserCookieError` и другие исключения, логируя ошибки.
8. Возвращает словарь `cookies`.

**Примеры**:
```python
domain = "example.com"
cookies = load_cookies_from_browsers(domain)
if cookies:
    print(f"Cookies for {domain}: {cookies}")
else:
    print(f"No cookies found for {domain} in any browser.")
```

### `set_cookies_dir(dir: str) -> None`

```python
def set_cookies_dir(dir: str) -> None:
    """
    Set the directory for cookie files.

    Args:
        dir (str): The directory to set for cookie files.
    """
    ...
```

**Назначение**:
Функция устанавливает директорию для файлов с куками.

**Параметры**:
- `dir (str)`: Директория, которую необходимо установить для файлов с куками.

**Возвращает**:
- `None`

**Как работает функция**:
1. Устанавливает значение статической переменной `CookiesConfig.cookies_dir` равным переданной директории.

**Примеры**:
```python
new_dir = "/path/to/cookies"
set_cookies_dir(new_dir)
print(f"Cookies directory set to: {new_dir}")
```

### `get_cookies_dir() -> str`

```python
def get_cookies_dir() -> str:
    """
    Get the directory for cookie files.

    Returns:
        str: The directory for cookie files.
    """
    ...
```

**Назначение**:
Функция возвращает директорию, в которой хранятся файлы с куками.

**Параметры**:
- Нет параметров.

**Возвращает**:
- `str`: Директория, в которой хранятся файлы с куками.

**Как работает функция**:
1. Возвращает значение статической переменной `CookiesConfig.cookies_dir`.

**Примеры**:
```python
cookies_dir = get_cookies_dir()
print(f"Cookies directory: {cookies_dir}")
```

### `read_cookie_files(dirPath: str = None)`

```python
def read_cookie_files(dirPath: str = None):
    """
    Reads cookie files (HAR and JSON) from a directory and stores them in CookiesConfig.cookies.

    Args:
        dirPath (str, optional): The directory to read cookie files from. Defaults to CookiesConfig.cookies_dir if None.
    """
    ...
```

**Назначение**:
Функция считывает файлы с куками (в форматах HAR и JSON) из директории и сохраняет их в `CookiesConfig.cookies`.

**Параметры**:
- `dirPath (str, optional)`: Директория, из которой необходимо считать файлы с куками. Если `None`, используется значение `CookiesConfig.cookies_dir`.

**Как работает функция**:
1. Определяет директорию для чтения файлов с куками. Если `dirPath` не передан, использует значение `CookiesConfig.cookies_dir`.
2. Проверяет, доступна ли директория для чтения. Если нет, логирует сообщение и выходит из функции.
3. Инициализирует пустые списки `harFiles` и `cookieFiles` для хранения путей к файлам в форматах HAR и JSON соответственно.
4. Обходит директорию `dirPath` и добавляет пути к файлам с расширениями ".har" и ".json" в соответствующие списки.
5. Очищает словарь `CookiesConfig.cookies`.
6. Перебирает список файлов в формате HAR (`harFiles`):
   - Открывает каждый файл, пытается загрузить его содержимое как JSON. Если происходит ошибка JSONDecodeError, переходит к следующему файлу.
   - Извлекает домен из каждого HAR-файла.
   - Извлекает куки из каждого HAR-файла и добавляет их в `CookiesConfig.cookies`.
7. Перебирает список файлов в формате JSON (`cookieFiles`):
   - Открывает каждый файл, пытается загрузить его содержимое как JSON. Если происходит ошибка JSONDecodeError или файл не является списком словарей с ключом "domain", переходит к следующему файлу.
   - Извлекает куки из каждого JSON-файла и добавляет их в `CookiesConfig.cookies`.
8. Логирует информацию о количестве добавленных куки для каждого домена.

**Внутренние функции**:
### `get_domain(v: dict) -> str`
```python
        def get_domain(v: dict) -> str:
            """
            Extracts the domain from a HAR file entry.

            Args:
                v (dict): A HAR file entry.

            Returns:
                str: The domain name, or None if not found.
            """
            ...
```
**Назначение**:
Функция извлекает домен из записи HAR-файла.

**Параметры**:
- `v (dict)`: Запись HAR-файла.

**Возвращает**:
- `str`: Доменное имя или `None`, если домен не найден.

**Как работает функция**:
1. Извлекает значения заголовков "host" или ":authority" из записи HAR-файла.
2. Если заголовки не найдены, возвращает `None`.
3. Извлекает первое значение заголовка и проверяет, содержится ли в нем один из доменов из списка `DOMAINS`.
4. Если домен найден, возвращает его. В противном случае возвращает `None`.

**Примеры**:
```python
read_cookie_files("/path/to/cookie/files")
print(f"Cookies loaded from files. Available domains: {CookiesConfig.cookies.keys()}")
```
```python
# Пример структуры файла cookieFile (JSON):
# [
#     {"domain": ".example.com", "name": "cookie1", "value": "value1"},
#     {"domain": ".example.com", "name": "cookie2", "value": "value2"}
# ]
```
```python
# Пример структуры файла harFile (HAR):
# {
#     "log": {
#         "entries": [
#             {
#                 "request": {
#                     "headers": [
#                         {"name": "Host", "value": "www.example.com"},
#                         {"name": ":authority", "value": "www.example.com"}
#                     ],
#                     "cookies": [
#                         {"name": "cookie1", "value": "value1"},
#                         {"name": "cookie2", "value": "value2"}
#                     ]
#                 }
#             }
#         ]
#     }
# }