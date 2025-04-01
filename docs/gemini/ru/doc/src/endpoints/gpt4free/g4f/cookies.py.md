# Модуль для работы с cookies
=======================================

Модуль предоставляет функциональность для загрузки и управления cookies из различных источников, таких как браузеры и файлы. Он включает в себя функции для получения, установки и чтения cookies, а также для настройки директории, в которой хранятся файлы cookies.

## Оглавление
- [Обзор](#обзор)
- [Подробнее](#подробнее)
- [Функции](#функции)
  - [g4f](#g4f)
  - [get_cookies](#get_cookies)
  - [set_cookies](#set_cookies)
  - [load_cookies_from_browsers](#load_cookies_from_browsers)
  - [set_cookies_dir](#set_cookies_dir)
  - [get_cookies_dir](#get_cookies_dir)
  - [read_cookie_files](#read_cookie_files)

## Обзор

Модуль предназначен для автоматизации работы с cookies в контексте проекта `hypotez`. Он позволяет загружать cookies из браузеров, если установлена библиотека `browser_cookie3`, а также считывать их из HAR (HTTP Archive) и JSON файлов. Модуль также предоставляет возможность кэширования cookies для повышения производительности.

## Подробнее

Модуль `cookies.py` предоставляет инструменты для управления cookies, используемыми в различных доменах. Он обеспечивает возможность загрузки cookies из браузеров с использованием библиотеки `browser_cookie3`, а также из файлов формата HAR и JSON. Модуль также включает функции для установки и получения директории, в которой хранятся файлы cookies. Это позволяет гибко управлять cookies и использовать их в различных сценариях, таких как автоматизированное тестирование и сбор данных.

## Функции

### `g4f`
```python
def g4f(domain_name: str) -> list:
    """
    Загружает cookies из браузера \'g4f\' (если он существует).

    Args:
        domain_name (str): Домен, для которого загружаются cookies.

    Returns:
        list: Список cookies.
    """
```

**Как работает функция**:
1. Проверяет, установлена ли библиотека `platformdirs`.
2. Если библиотека `platformdirs` не установлена, возвращает пустой список.
3. Определяет директорию пользовательских конфигураций для "g4f".
4. Формирует путь к файлу cookies.
5. Если файл cookies не существует, возвращает пустой список.
6. Использует функцию `chrome` из библиотеки `browser_cookie3` для загрузки cookies из файла.

**Примеры**:
```python
cookies = g4f(".google.com")
print(cookies)
```

### `get_cookies`
```python
def get_cookies(domain_name: str, raise_requirements_error: bool = True, single_browser: bool = False, cache_result: bool = True) -> Dict[str, str]:
    """
    Загружает cookies для заданного домена из всех поддерживаемых браузеров и кэширует результаты.

    Args:
        domain_name (str): Домен, для которого загружаются cookies.
        raise_requirements_error (bool, optional): Если `True`, вызывает исключение `MissingRequirementsError`, если не установлена библиотека `browser_cookie3`. По умолчанию `True`.
        single_browser (bool, optional): Если `True`, загружает cookies только из первого найденного браузера. По умолчанию `False`.
        cache_result (bool, optional): Если `True`, кэширует результаты загрузки cookies. По умолчанию `True`.

    Returns:
        Dict[str, str]: Словарь с именами и значениями cookie.
    """
```

**Как работает функция**:
1. Проверяет, включено ли кэширование результатов и есть ли cookies для данного домена в кэше.
2. Если cookies найдены в кэше, возвращает их.
3. Вызывает функцию `load_cookies_from_browsers` для загрузки cookies из браузеров.
4. Если включено кэширование результатов, сохраняет загруженные cookies в кэше.
5. Возвращает словарь с cookies.

**Примеры**:
```python
cookies = get_cookies(".google.com")
print(cookies)
```

### `set_cookies`
```python
def set_cookies(domain_name: str, cookies: Cookies = None) -> None:
    """
    Устанавливает cookies для заданного домена.

    Args:
        domain_name (str): Домен, для которого устанавливаются cookies.
        cookies (Cookies, optional): Словарь с cookies для установки. Если `None`, cookies для данного домена удаляются из кэша. По умолчанию `None`.
    """
```

**Как работает функция**:
1. Если передан словарь с cookies, сохраняет его в кэше для заданного домена.
2. Если `cookies` равен `None`, удаляет cookies для данного домена из кэша, если они там есть.

**Примеры**:
```python
cookies = {"cookie1": "value1", "cookie2": "value2"}
set_cookies(".google.com", cookies)
```

### `load_cookies_from_browsers`
```python
def load_cookies_from_browsers(domain_name: str, raise_requirements_error: bool = True, single_browser: bool = False) -> Cookies:
    """
    Вспомогательная функция для загрузки cookies из различных браузеров.

    Args:
        domain_name (str): Домен, для которого загружаются cookies.
        raise_requirements_error (bool, optional): Если `True`, вызывает исключение `MissingRequirementsError`, если не установлена библиотека `browser_cookie3`. По умолчанию `True`.
        single_browser (bool, optional): Если `True`, загружает cookies только из первого найденного браузера. По умолчанию `False`.

    Returns:
        Dict[str, str]: Словарь с именами и значениями cookie.
    """
```

**Как работает функция**:
1. Проверяет, установлена ли библиотека `browser_cookie3`.
2. Если библиотека `browser_cookie3` не установлена и `raise_requirements_error` равен `True`, вызывает исключение `MissingRequirementsError`.
3. Итерируется по списку браузеров `browsers`.
4. Для каждого браузера пытается загрузить cookies для заданного домена.
5. Если cookies успешно загружены, добавляет их в общий словарь cookies.
6. Если `single_browser` равен `True`, прекращает загрузку cookies после первого успешного браузера.
7. Обрабатывает исключения `BrowserCookieError` и другие исключения, логируя ошибки.
8. Возвращает словарь с cookies.

**Примеры**:
```python
cookies = load_cookies_from_browsers(".google.com")
print(cookies)
```

### `set_cookies_dir`
```python
def set_cookies_dir(dir: str) -> None:
    """
    Устанавливает директорию для хранения файлов cookies.

    Args:
        dir (str): Путь к директории.
    """
```

**Как работает функция**:
1. Устанавливает значение атрибута `cookies_dir` класса `CookiesConfig` равным переданному пути.

**Примеры**:
```python
set_cookies_dir("./cookies")
```

### `get_cookies_dir`
```python
def get_cookies_dir() -> str:
    """
    Возвращает директорию, в которой хранятся файлы cookies.

    Returns:
        str: Путь к директории.
    """
```

**Как работает функция**:
1. Возвращает значение атрибута `cookies_dir` класса `CookiesConfig`.

**Примеры**:
```python
cookies_dir = get_cookies_dir()
print(cookies_dir)
```

### `read_cookie_files`
```python
def read_cookie_files(dirPath: str = None):
    """
    Считывает файлы cookie из указанной директории.

    Args:
        dirPath (str, optional): Путь к директории с файлами cookie. Если `None`, используется директория по умолчанию из `CookiesConfig.cookies_dir`.
    """
```

**Внутренние функции**:

#### `get_domain`
```python
def get_domain(v: dict) -> str:
    """
    Извлекает домен из записи HAR файла.

    Args:
        v (dict): Запись из HAR файла.

    Returns:
        str: Доменное имя, если найдено, иначе `None`.
    """
```

**Как работает функция `get_domain`**:
1. Извлекает заголовок "host" или ":authority" из записи HAR файла.
2. Если заголовок не найден, возвращает `None`.
3. Ищет совпадение домена с доменами из списка `DOMAINS`.
4. Если совпадение найдено, возвращает домен.

**Как работает функция `read_cookie_files`**:
1. Определяет путь к директории с файлами cookies. Если `dirPath` не указан, использует значение из `CookiesConfig.cookies_dir`.
2. Проверяет, доступна ли директория для чтения. Если нет, логирует сообщение и возвращается.
3. Находит все HAR и JSON файлы в указанной директории и её поддиректориях.
4. Очищает текущий кэш cookies `CookiesConfig.cookies`.
5. Для каждого HAR файла:
    - Открывает и пытается загрузить HAR файл.
    - Если файл не является корректным HAR файлом, переходит к следующему файлу.
    - Извлекает cookies из каждой записи HAR файла и добавляет их в кэш `CookiesConfig.cookies`.
6. Для каждого JSON файла:
    - Открывает и пытается загрузить JSON файл.
    - Если файл не является корректным JSON файлом или не содержит списка словарей с доменом, переходит к следующему файлу.
    - Извлекает cookies из JSON файла и добавляет их в кэш `CookiesConfig.cookies`.

**Примеры**:
```python
read_cookie_files("./cookies")
```
```python
read_cookie_files()  # использует директорию по умолчанию из CookiesConfig.cookies_dir