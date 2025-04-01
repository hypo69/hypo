# Модуль для работы с cookies
=================================================

Модуль предназначен для загрузки и управления cookies из различных источников, таких как браузеры и файлы, для использования в проекте `hypotez`. Он предоставляет функции для получения, установки и хранения cookies, а также для чтения файлов cookie в форматах HAR и JSON.

## Оглавление

- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Классы](#классы)
    - [CookiesConfig](#cookiesconfig)
- [Функции](#функции)
    - [g4f](#g4f)
    - [get_cookies](#get_cookies)
    - [set_cookies](#set_cookies)
    - [load_cookies_from_browsers](#load_cookies_from_browsers)
    - [set_cookies_dir](#set_cookies_dir)
    - [get_cookies_dir](#get_cookies_dir)
    - [read_cookie_files](#read_cookie_files)

## Обзор

Модуль `cookies` предоставляет функциональность для работы с cookies, включая загрузку из браузеров и файлов, а также управление ими. Он использует библиотеку `browser_cookie3` для загрузки cookies из различных браузеров и предоставляет функции для чтения файлов cookie в форматах HAR и JSON.

## Подробнее

Этот модуль играет важную роль в проекте `hypotez`, обеспечивая возможность автоматической загрузки cookies для различных доменов. Это позволяет автоматизировать процесс аутентификации и обхода различных ограничений, связанных с cookies.

## Классы

### `CookiesConfig`

**Описание**: Класс конфигурации для хранения cookies и пути к директории с cookies.

**Принцип работы**:
Класс `CookiesConfig` содержит статические переменные для хранения словаря cookies (`cookies`) и пути к директории с файлами cookies (`cookies_dir`). Это позволяет хранить и получать cookies, а также путь к директории с cookies, в любом месте кода.

**Аттрибуты**:
- `cookies` (Dict[str, Cookies]): Словарь для хранения cookies по доменам.
- `cookies_dir` (str): Путь к директории с файлами cookies. По умолчанию "./har_and_cookies".

## Функции

### `g4f`

```python
def g4f(domain_name: str) -> list:
    """
    Load cookies from the 'g4f' browser (if exists).

    Args:
        domain_name (str): The domain for which to load cookies.

    Returns:
        list: List of cookies.
    """
    ...
```

**Назначение**: Загружает cookies из браузера "g4f", если он существует.

**Параметры**:
- `domain_name` (str): Домен, для которого необходимо загрузить cookies.

**Возвращает**:
- `list`: Список cookies.

**Как работает функция**:

1. Проверяет, установлена ли библиотека `platformdirs`. Если нет, возвращает пустой список.
2. Определяет путь к директории с данными пользователя для "g4f".
3. Формирует путь к файлу с cookies.
4. Если файл не существует, возвращает пустой список.
5. Если файл существует, загружает cookies с помощью функции `chrome` из библиотеки `browser_cookie3` и возвращает их.

**Примеры**:
```python
cookies = g4f(".google.com")
print(cookies)
```

### `get_cookies`

```python
def get_cookies(domain_name: str, raise_requirements_error: bool = True, single_browser: bool = False, cache_result: bool = True) -> Dict[str, str]:
    """
    Load cookies for a given domain from all supported browsers and cache the results.

    Args:
        domain_name (str): The domain for which to load cookies.
        raise_requirements_error (bool): Если `True`, вызывает исключение `MissingRequirementsError`, если `browser_cookie3` не установлен. По умолчанию `True`.
        single_browser (bool): Если `True`, загружает cookies только из одного браузера. По умолчанию `False`.
        cache_result (bool): Если `True`, кэширует результат загрузки cookies. По умолчанию `True`.

    Returns:
        Dict[str, str]: A dictionary of cookie names and values.
    """
    ...
```

**Назначение**: Загружает cookies для указанного домена из всех поддерживаемых браузеров и кэширует результаты.

**Параметры**:
- `domain_name` (str): Домен, для которого необходимо загрузить cookies.
- `raise_requirements_error` (bool, optional): Если `True`, вызывает исключение `MissingRequirementsError`, если `browser_cookie3` не установлен. По умолчанию `True`.
- `single_browser` (bool, optional): Если `True`, загружает cookies только из одного браузера. По умолчанию `False`.
- `cache_result` (bool, optional): Если `True`, кэширует результат загрузки cookies. По умолчанию `True`.

**Возвращает**:
- `Dict[str, str]`: Словарь, содержащий пары "имя cookie": "значение cookie".

**Как работает функция**:

1. Проверяет, есть ли cookies для данного домена в кэше (`CookiesConfig.cookies`). Если есть и `cache_result` равен `True`, возвращает cookies из кэша.
2. Если cookies в кэше нет или `cache_result` равен `False`, вызывает функцию `load_cookies_from_browsers` для загрузки cookies из браузеров.
3. Если `cache_result` равен `True`, кэширует загруженные cookies в `CookiesConfig.cookies`.
4. Возвращает загруженные cookies.

**Примеры**:
```python
cookies = get_cookies(".google.com")
print(cookies)
```

### `set_cookies`

```python
def set_cookies(domain_name: str, cookies: Cookies = None) -> None:
    """
    Sets the cookies for a given domain in the cache.

    Args:
        domain_name (str): The domain for which to set cookies.
        cookies (Cookies, optional): A dictionary of cookie names and values. If `None`, removes the cookies for the domain from the cache. Defaults to `None`.
    """
    ...
```

**Назначение**: Устанавливает cookies для указанного домена в кэше.

**Параметры**:
- `domain_name` (str): Домен, для которого необходимо установить cookies.
- `cookies` (Cookies, optional): Словарь, содержащий пары "имя cookie": "значение cookie". Если `None`, удаляет cookies для данного домена из кэша. По умолчанию `None`.

**Как работает функция**:

1. Если передан словарь `cookies`, устанавливает его в `CookiesConfig.cookies` для указанного домена.
2. Если `cookies` равен `None`, удаляет cookies для данного домена из `CookiesConfig.cookies`, если они там есть.

**Примеры**:
```python
cookies = {"cookie1": "value1", "cookie2": "value2"}
set_cookies(".google.com", cookies)

set_cookies(".google.com") # Удаляет cookies для домена .google.com из кэша
```

### `load_cookies_from_browsers`

```python
def load_cookies_from_browsers(domain_name: str, raise_requirements_error: bool = True, single_browser: bool = False) -> Cookies:
    """
    Helper function to load cookies from various browsers.

    Args:
        domain_name (str): The domain for which to load cookies.
        raise_requirements_error (bool): If `True`, raises a MissingRequirementsError if browser_cookie3 is not installed.
        single_browser (bool): If `True`, only loads cookies from a single browser.

    Returns:
        Dict[str, str]: A dictionary of cookie names and values.
    """
    ...
```

**Назначение**: Загружает cookies из различных браузеров.

**Параметры**:
- `domain_name` (str): Домен, для которого необходимо загрузить cookies.
- `raise_requirements_error` (bool, optional): Если `True`, вызывает исключение `MissingRequirementsError`, если `browser_cookie3` не установлен. По умолчанию `True`.
- `single_browser` (bool, optional): Если `True`, загружает cookies только из одного браузера. По умолчанию `False`.

**Возвращает**:
- `Dict[str, str]`: Словарь, содержащий пары "имя cookie": "значение cookie".

**Как работает функция**:

1. Проверяет, установлена ли библиотека `browser_cookie3`. Если нет и `raise_requirements_error` равен `True`, вызывает исключение `MissingRequirementsError`.
2. Итерируется по списку браузеров (`browsers`).
3. Для каждого браузера пытается загрузить cookies для указанного домена.
4. Если загрузка прошла успешно, добавляет cookies в общий словарь `cookies`.
5. Если `single_browser` равен `True`, прекращает итерацию после загрузки cookies из первого браузера.
6. В случае ошибки при загрузке cookies из какого-либо браузера, логирует ошибку.
7. Возвращает словарь со всеми загруженными cookies.

**Примеры**:
```python
cookies = load_cookies_from_browsers(".google.com")
print(cookies)
```

### `set_cookies_dir`

```python
def set_cookies_dir(dir: str) -> None:
    """
    Sets the directory where cookies files are stored.

    Args:
        dir (str): The path to the directory.
    """
    ...
```

**Назначение**: Устанавливает директорию, в которой хранятся файлы cookies.

**Параметры**:
- `dir` (str): Путь к директории.

**Как работает функция**:

1. Устанавливает значение `CookiesConfig.cookies_dir` равным переданному пути.

**Примеры**:
```python
set_cookies_dir("./my_cookies")
```

### `get_cookies_dir`

```python
def get_cookies_dir() -> str:
    """
    Gets the directory where cookies files are stored.

    Returns:
        str: The path to the directory.
    """
    ...
```

**Назначение**: Возвращает директорию, в которой хранятся файлы cookies.

**Возвращает**:
- `str`: Путь к директории.

**Как работает функция**:

1. Возвращает значение `CookiesConfig.cookies_dir`.

**Примеры**:
```python
dir = get_cookies_dir()
print(dir)
```

### `read_cookie_files`

```python
def read_cookie_files(dirPath: str = None):
    """
    Reads cookies from .har and .json files in the specified directory.

    Args:
        dirPath (str, optional): The path to the directory containing .har and .json cookie files. Defaults to None, which uses CookiesConfig.cookies_dir.
    """
    ...
```

**Назначение**: Читает cookies из файлов в форматах HAR и JSON, находящихся в указанной директории.

**Параметры**:
- `dirPath` (str, optional): Путь к директории, содержащей файлы cookies в форматах HAR и JSON. По умолчанию `None`, в этом случае используется `CookiesConfig.cookies_dir`.

**Как работает функция**:

1. Если `dirPath` не указан, использует значение `CookiesConfig.cookies_dir`.
2. Проверяет, доступна ли директория для чтения. Если нет, логирует сообщение и завершает работу.
3. Формирует списки файлов с расширениями `.har` и `.json`.
4. Очищает текущий словарь cookies (`CookiesConfig.cookies`).
5. Итерируется по списку HAR-файлов:
   - Пытается загрузить содержимое файла как JSON. В случае ошибки JSONDecodeError переходит к следующему файлу.
   - Извлекает домен из каждого HAR-файла и соответствующие cookies, добавляя их в `CookiesConfig.cookies`.
6. Итерируется по списку JSON-файлов:
   - Пытается загрузить содержимое файла как JSON. В случае ошибки JSONDecodeError переходит к следующему файлу.
   - Проверяет структуру JSON-файла. Если структура не соответствует ожидаемой (список словарей с полем "domain"), переходит к следующему файлу.
   - Извлекает домен и соответствующие cookies из каждого JSON-файла, добавляя их в `CookiesConfig.cookies`.

**Внутренние функции**:

- `get_domain(v: dict) -> str`: Извлекает домен из записи HAR-файла.
    - **Назначение**: Извлекает доменное имя из записи HAR-файла.

    - **Параметры**:
        - `v` (dict): Запись из HAR-файла.

    - **Возвращает**:
        - `str`: Доменное имя, если оно найдено, иначе `None`.

    - **Как работает функция**:
        1. Извлекает значение заголовка "host" или ":authority" из запроса.
        2. Если заголовок не найден, возвращает `None`.
        3. Итерируется по списку допустимых доменов (`DOMAINS`) и проверяет, содержится ли домен в значении заголовка.
        4. Если домен найден, возвращает его.
        5. Если ни один домен не найден, возвращает `None`.
**Примеры**:
```python
read_cookie_files("./cookies")
```
```
ASCII flowchart для `read_cookie_files`:

Начало
  ↓
Получение пути к директории (dirPath)
  ↓
Проверка доступности директории для чтения
  ↓
Поиск HAR-файлов и JSON-файлов
  ↓
Итерация по HAR-файлам
  │
  └──→ Загрузка HAR-файла как JSON
       │
       └──→ Извлечение домена (get_domain) и cookies
            │
            └──→ Добавление cookies в CookiesConfig.cookies
  ↓
Итерация по JSON-файлам
  │
  └──→ Загрузка JSON-файла как JSON
       │
       └──→ Проверка структуры JSON
            │
            └──→ Извлечение домена и cookies
                 │
                 └──→ Добавление cookies в CookiesConfig.cookies
  ↓
Конец
```
```
ASCII flowchart для `get_domain`:

Начало
  ↓
Извлечение заголовка Host или :authority
  ↓
Проверка наличия заголовка
  │
  └── Да →  Итерация по DOMAINS
       │    │
       │    └──→ Проверка вхождения домена в Host
       │         │
       │         └── Да → Возврат домена
       │              │
       │              └── Нет → Продолжение итерации по DOMAINS
       │
       └── Нет → Возврат None
  ↓
Конец