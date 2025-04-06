# Модуль для работы с куки (cookies)
========================================

Модуль предназначен для загрузки куки из различных браузеров и файлов, а также для управления каталогом, в котором хранятся куки.

## Обзор

Модуль `cookies.py` предоставляет функциональность для автоматического извлечения куки из установленных браузеров, таких как Chrome, Firefox, Opera и других. Он также позволяет считывать куки из HAR (HTTP Archive) и JSON файлов. Модуль предназначен для использования в проектах, требующих автоматизированного взаимодействия с веб-сайтами, где необходимо сохранять состояние сессии или выполнять другие действия, требующие наличия куки.

## Подробнее

Этот модуль облегчает процесс получения куки, автоматически определяя поддерживаемые браузеры и извлекая соответствующие данные. Он также включает в себя механизмы для обработки ошибок и логирования, что упрощает отладку и поддержку.

## Классы

### `CookiesConfig`

**Описание**: Класс конфигурации для хранения куки и директории для хранения файлов куки.

**Принцип работы**:
Класс `CookiesConfig` используется для хранения глобальной конфигурации, связанной с куками. Он содержит словарь `cookies`, где ключом является доменное имя, а значением - словарь с именами и значениями куки. Также класс хранит путь к директории, где хранятся файлы куки.

**Аттрибуты**:
- `cookies` (Dict[str, Cookies]): Словарь для хранения куки. Ключ - доменное имя, значение - словарь с именами и значениями куки.
- `cookies_dir` (str): Путь к директории, где хранятся файлы куки. По умолчанию "./har_and_cookies".

## Функции

### `g4f(domain_name: str) -> list`

```python
def g4f(domain_name: str) -> list:
    """
    Load cookies from the 'g4f' browser (if exists).

    Args:
        domain_name (str): The domain for which to load cookies.

    Returns:
        list: List of cookies.
    """
```

**Назначение**: Загружает куки из браузера 'g4f', если он существует.

**Параметры**:
- `domain_name` (str): Домен, для которого необходимо загрузить куки.

**Возвращает**:
- `list`: Список куки.

**Как работает функция**:

1. **Проверка наличия `platformdirs`**: Функция сначала проверяет, установлен ли пакет `platformdirs`. Если нет, возвращается пустой список.
2. **Определение директории пользователя**: Если `platformdirs` установлен, определяется директория пользователя для хранения конфигурации 'g4f'.
3. **Формирование пути к файлу куки**: Формируется путь к файлу куки внутри директории пользователя.
4. **Проверка существования файла куки**: Проверяется, существует ли файл куки. Если нет, возвращается пустой список.
5. **Загрузка куки**: Если файл куки существует, куки загружаются с использованием функции `chrome` из библиотеки `browser_cookie3`.
6. **Возврат списка куки**: Возвращается список куки.

**Примеры**:

```python
cookies = g4f('.google.com')
print(cookies)  # doctest: +SKIP
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
```

**Назначение**: Загружает куки для указанного домена из всех поддерживаемых браузеров и кэширует результаты.

**Параметры**:
- `domain_name` (str): Домен, для которого необходимо загрузить куки.
- `raise_requirements_error` (bool, optional): Если `True`, вызывает исключение `MissingRequirementsError`, если не установлены необходимые пакеты. По умолчанию `True`.
- `single_browser` (bool, optional): Если `True`, загружает куки только из одного браузера. По умолчанию `False`.
- `cache_result` (bool, optional): Если `True`, кэширует результаты загрузки куки. По умолчанию `True`.

**Возвращает**:
- `Dict[str, str]`: Словарь с именами и значениями куки.

**Как работает функция**:

1. **Проверка кэша**: Функция сначала проверяет, есть ли куки для указанного домена в кэше (`CookiesConfig.cookies`). Если есть и `cache_result` равен `True`, возвращаются куки из кэша.
2. **Загрузка куки из браузеров**: Если куки нет в кэше или `cache_result` равен `False`, вызывается функция `load_cookies_from_browsers` для загрузки куки из установленных браузеров.
3. **Кэширование результата**: Если `cache_result` равен `True`, загруженные куки сохраняются в кэше (`CookiesConfig.cookies`).
4. **Возврат куки**: Возвращается словарь с именами и значениями куки.

**Примеры**:

```python
cookies = get_cookies('.google.com')
print(cookies)  # doctest: +SKIP
```

### `set_cookies(domain_name: str, cookies: Cookies = None) -> None`

```python
def set_cookies(domain_name: str, cookies: Cookies = None) -> None:
    """
    Sets cookies for a specified domain.

    Args:
        domain_name (str): The domain for which to set cookies.
        cookies (Cookies, optional): The cookies to set. Defaults to None.
    """
```

**Назначение**: Устанавливает куки для указанного домена.

**Параметры**:
- `domain_name` (str): Домен, для которого необходимо установить куки.
- `cookies` (Cookies, optional): Куки для установки. По умолчанию `None`.

**Как работает функция**:

1. **Установка куки**: Если передан словарь `cookies`, он сохраняется в кэше (`CookiesConfig.cookies`) для указанного домена.
2. **Удаление куки**: Если `cookies` равен `None`, и куки для указанного домена есть в кэше, они удаляются из кэша.

**Примеры**:

```python
set_cookies('.google.com', {'cookie_name': 'cookie_value'})
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
```

**Назначение**: Загружает куки из различных браузеров.

**Параметры**:
- `domain_name` (str): Домен, для которого необходимо загрузить куки.
- `raise_requirements_error` (bool, optional): Если `True`, вызывает исключение `MissingRequirementsError`, если не установлен пакет `browser_cookie3`. По умолчанию `True`.
- `single_browser` (bool, optional): Если `True`, загружает куки только из одного браузера. По умолчанию `False`.

**Возвращает**:
- `Dict[str, str]`: Словарь с именами и значениями куки.

**Как работает функция**:

1. **Проверка наличия `browser_cookie3`**: Функция сначала проверяет, установлен ли пакет `browser_cookie3`. Если нет и `raise_requirements_error` равен `True`, вызывается исключение `MissingRequirementsError`.
2. **Итерация по браузерам**: Функция итерируется по списку браузеров (`browsers`).
3. **Загрузка куки из каждого браузера**: Для каждого браузера вызывается соответствующая функция загрузки куки.
4. **Обработка ошибок**: Если при загрузке куки возникает ошибка, она логируется с использованием `debug.error`.
5. **Сохранение куки**: Загруженные куки сохраняются в словарь `cookies`.
6. **Учет параметра `single_browser`**: Если `single_browser` равен `True`, загрузка куки прекращается после первого успешного извлечения куки.
7. **Возврат куки**: Возвращается словарь с именами и значениями куки.

**Примеры**:

```python
cookies = load_cookies_from_browsers('.google.com')
print(cookies)  # doctest: +SKIP
```

### `set_cookies_dir(dir: str) -> None`

```python
def set_cookies_dir(dir: str) -> None:
    """
    Sets the directory where cookies are stored.

    Args:
        dir (str): The directory path.
    """
```

**Назначение**: Устанавливает директорию, где хранятся файлы куки.

**Параметры**:
- `dir` (str): Путь к директории.

**Как работает функция**:

1. **Установка директории**: Функция устанавливает значение атрибута `cookies_dir` класса `CookiesConfig` равным переданному пути.

**Примеры**:

```python
set_cookies_dir('./custom_cookies')
```

### `get_cookies_dir() -> str`

```python
def get_cookies_dir() -> str:
    """
    Gets the directory where cookies are stored.

    Returns:
        str: The directory path.
    """
```

**Назначение**: Возвращает директорию, где хранятся файлы куки.

**Возвращает**:
- `str`: Путь к директории.

**Как работает функция**:

1. **Получение директории**: Функция возвращает значение атрибута `cookies_dir` класса `CookiesConfig`.

**Примеры**:

```python
cookies_dir = get_cookies_dir()
print(cookies_dir)
```

### `read_cookie_files(dirPath: str = None)`

```python
def read_cookie_files(dirPath: str = None):
    """
    Reads cookie files from a specified directory and loads them into the CookiesConfig.cookies dictionary.

    Args:
        dirPath (str, optional): The path to the directory containing cookie files. 
                                 Defaults to CookiesConfig.cookies_dir if None.
    """
```

**Назначение**: Считывает файлы куки из указанной директории и загружает их в словарь `CookiesConfig.cookies`.

**Параметры**:
- `dirPath` (str, optional): Путь к директории, содержащей файлы куки. Если `None`, используется `CookiesConfig.cookies_dir`.

**Как работает функция**:

1. **Определение директории**: Если `dirPath` не указан, используется значение `CookiesConfig.cookies_dir`.
2. **Проверка доступа к директории**: Проверяется, есть ли доступ на чтение к указанной директории. Если нет, функция завершается.
3. **Определение домена**: Определяется внутренняя функция `get_domain`, которая извлекает домен из HAR-файла.
4. **Поиск файлов**: Функция ищет HAR-файлы (`.har`) и файлы куки (`.json`) в указанной директории.
5. **Чтение HAR-файлов**: Для каждого HAR-файла выполняется попытка чтения и извлечения куки. Если файл не является HAR-файлом, обработка продолжается со следующим файлом. Извлекаются куки из HAR-файла и сохраняются в `CookiesConfig.cookies`.
6. **Чтение файлов куки**: Для каждого файла куки выполняется попытка чтения и извлечения куки. Если файл не является файлом куки, обработка продолжается со следующим файлом. Извлекаются куки из файла и сохраняются в `CookiesConfig.cookies`.

**Внутренние функции**:
- `get_domain(v: dict) -> str`:
    ```python
        def get_domain(v: dict) -> str:
            """
            Extracts the domain from a HAR file entry.

            Args:
                v (dict): The HAR file entry.

            Returns:
                str: The extracted domain, or None if not found.
            """
    ```

    **Назначение**: Извлекает домен из записи HAR-файла.

    **Параметры**:
    - `v` (dict): Запись HAR-файла.

    **Возвращает**:
    - `str`: Извлеченный домен или `None`, если домен не найден.

    **Как работает функция**:

    1.  **Извлечение заголовка Host**: Извлекает заголовок `Host` или `:authority` из запроса HAR-файла.
    2.  **Проверка домена**: Проверяет, содержит ли заголовок Host один из доменов из списка `DOMAINS`.
    3.  **Возврат домена**: Если домен найден, он возвращается. В противном случае возвращается `None`.

**Примеры**:

```python
read_cookie_files('./cookies')
```

```ascii
    +---------------------+
    |  dirPath is None   |
    +---------------------+
             |
             Y
    +---------------------+
    | dirPath =           |
    | CookiesConfig.cookies_dir|
    +---------------------+
             |
    +---------------------+
    | os.access(dirPath,  |
    |  os.R_OK)           |
    +---------------------+
             |
             N
    +---------------------+
    |       return        |
    +---------------------+
             |
             Y
    +---------------------+
    |    harFiles = []    |
    | cookieFiles = []    |
    +---------------------+
             |
    +---------------------+
    | os.walk(dirPath)    |
    +---------------------+
             |
    +---------------------+
    | Проход по файлам    |
    +---------------------+
             |
    +---------------------+
    |  file.endswith      |
    | (".har" или ".json")|
    +---------------------+
             |
    +---------------------+
    |Добавление файлов    |
    | в harFiles/         |
    | cookieFiles         |
    +---------------------+
             |
    +---------------------+
    | CookiesConfig.cookies|
    |  = {}               |
    +---------------------+
             |
    +---------------------+
    |  Чтение HAR файлов   |
    +---------------------+
             |
    +---------------------+
    |   Чтение COOKIE      |
    |    файлов           |
    +---------------------+