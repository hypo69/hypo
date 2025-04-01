# Модуль для работы с cookies в g4f
## Обзор

Модуль `cookies.py` предназначен для управления файлами cookie, используемыми в проекте `g4f`. Он предоставляет функциональность для загрузки файлов cookie из различных браузеров, установки, получения и чтения файлов cookie из каталогов.

## Подробнее

Этот модуль играет важную роль в управлении аутентификацией и сохранении состояния сессий при взаимодействии с различными веб-сервисами. Он использует библиотеку `browser_cookie3` для извлечения файлов cookie из установленных браузеров и предоставляет инструменты для работы с cookie, сохраненными в формате HAR (HTTP Archive) и JSON.

## Содержание

1.  [Импорты](#Импорты)
2.  [Исключения](#Исключения)
3.  [Функции](#Функции)
    *   [g4f](#g4f)
    *   [get_cookies](#get_cookies)
    *   [set_cookies](#set_cookies)
    *   [load_cookies_from_browsers](#load_cookies_from_browsers)
    *   [set_cookies_dir](#set_cookies_dir)
    *   [get_cookies_dir](#get_cookies_dir)
    *   [read_cookie_files](#read_cookie_files)
        *   [get_domain](#get_domain)
3.  [Классы](#Классы)
    *   [CookiesConfig](#CookiesConfig)

## Импорты

В данном модуле используются следующие импорты:

-   `os`: для работы с операционной системой, например, для проверки существования файлов и доступа к ним.
-   `time`: для работы со временем, например, для проверки срока действия cookie.
-   `json`: для работы с JSON-форматом, используемым для хранения cookie в файлах.
-   `platformdirs.user_config_dir`: (опционально) для определения каталога конфигурации пользователя.
-   `browser_cookie3`: (опционально) для загрузки cookie из различных браузеров.
-   `.typing.Dict, Cookies`: для аннотации типов.
-   `.errors.MissingRequirementsError`: для обработки ошибок, связанных с отсутствием необходимых зависимостей.
-   `. import debug`: для отладочного логирования.

## Исключения

В модуле используется исключение `MissingRequirementsError`, которое вызывается, если не установлена библиотека `browser_cookie3`.

## Классы

### `CookiesConfig`

```python
class CookiesConfig():
    cookies: Dict[str, Cookies] = {}
    cookies_dir: str = "./har_and_cookies"
```

**Описание**:
Класс `CookiesConfig` предназначен для хранения глобальных настроек, связанных с cookie.

**Принцип работы**:
Класс содержит два атрибута:

*   `cookies`: Словарь, где ключи - доменные имена, а значения - словари cookie для этих доменов.
*   `cookies_dir`: Путь к каталогу, где хранятся файлы cookie.

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

**Назначение**:
Загружает файлы cookie из браузера `g4f` (если он существует).

**Параметры**:
-   `domain_name` (str): Домен, для которого необходимо загрузить cookie.

**Возвращает**:
-   `list`: Список cookie.

**Как работает функция**:

1.  Проверяет, установлена ли библиотека `platformdirs`. Если нет, возвращает пустой список.
2.  Определяет каталог конфигурации пользователя для `g4f`.
3.  Формирует путь к файлу cookie.
4.  Если файл cookie не существует, возвращает пустой список.
5.  В противном случае загружает cookie из файла с помощью функции `chrome` из `browser_cookie3` и возвращает их.

**Примеры**:

```python
cookies = g4f('.google.com')
print(cookies) #  Вывод:  [<cookie .google.com ...>, ...]
```

### `get_cookies`

```python
def get_cookies(domain_name: str, raise_requirements_error: bool = True, single_browser: bool = False, cache_result: bool = True) -> Dict[str, str]:
    """
    Load cookies for a given domain from all supported browsers and cache the results.

    Args:
        domain_name (str): The domain for which to load cookies.
        raise_requirements_error (bool): определяет, нужно ли вызывать исключение, если не установлены необходимые библиотеки.
        single_browser (bool):  определяет, нужно ли загружать cookie только из одного браузера.
        cache_result (bool): определяет, нужно ли кэшировать результат.

    Returns:
        Dict[str, str]: A dictionary of cookie names and values.
    """
    ...
```

**Назначение**:
Загружает cookie для указанного домена из всех поддерживаемых браузеров и кэширует результаты.

**Параметры**:

*   `domain_name` (str): Домен, для которого необходимо загрузить cookie.
*   `raise_requirements_error` (bool, optional): Определяет, нужно ли вызывать исключение `MissingRequirementsError`, если не установлена библиотека `browser_cookie3`. По умолчанию `True`.
*   `single_browser` (bool, optional): Если `True`, загружает cookie только из первого браузера, в котором они найдены. По умолчанию `False`.
*   `cache_result` (bool, optional): Если `True`, кэширует результаты загрузки cookie в `CookiesConfig.cookies`. По умолчанию `True`.

**Возвращает**:

*   `Dict[str, str]`: Словарь, где ключи - имена cookie, а значения - их значения.

**Как работает функция**:

1.  Проверяет, есть ли cookie для данного домена в кэше (`CookiesConfig.cookies`). Если есть и `cache_result` равен `True`, возвращает cookie из кэша.
2.  Если cookie нет в кэше, вызывает функцию `load_cookies_from_browsers` для загрузки cookie из браузеров.
3.  Если `cache_result` равен `True`, сохраняет загруженные cookie в кэше (`CookiesConfig.cookies`).
4.  Возвращает загруженные cookie.

**Примеры**:

```python
cookies = get_cookies('.google.com')
print(cookies) #  Вывод:  {'cookie_name': 'cookie_value', ...}
```

### `set_cookies`

```python
def set_cookies(domain_name: str, cookies: Cookies = None) -> None:
    """
    Sets the cookies for a given domain name.

    Args:
        domain_name (str): The domain name for which to set cookies.
        cookies (Cookies, optional): The cookies to set for the domain. Defaults to None.

    Returns:
        None
    """
    ...
```

**Назначение**:
Устанавливает cookie для указанного домена.

**Параметры**:

*   `domain_name` (str): Домен, для которого необходимо установить cookie.
*   `cookies` (Cookies, optional): Словарь cookie, которые необходимо установить для домена. Если `None`, удаляет cookie для данного домена из кэша (`CookiesConfig.cookies`). По умолчанию `None`.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Если передан словарь `cookies`, сохраняет его в кэше (`CookiesConfig.cookies`) для указанного домена.
2.  Если `cookies` равен `None`, удаляет cookie для данного домена из кэша (`CookiesConfig.cookies`), если они там есть.

**Примеры**:

```python
set_cookies('.google.com', {'cookie_name': 'cookie_value'})
```

### `load_cookies_from_browsers`

```python
def load_cookies_from_browsers(domain_name: str, raise_requirements_error: bool = True, single_browser: bool = False) -> Cookies:
    """
    Helper function to load cookies from various browsers.

    Args:
        domain_name (str): The domain for which to load cookies.
        raise_requirements_error (bool): определяет, нужно ли вызывать исключение, если не установлены необходимые библиотеки.
        single_browser (bool):  определяет, нужно ли загружать cookie только из одного браузера.

    Returns:
        Dict[str, str]: A dictionary of cookie names and values.
    """
    ...
```

**Назначение**:
Загружает cookie из различных браузеров.

**Параметры**:

*   `domain_name` (str): Домен, для которого необходимо загрузить cookie.
*   `raise_requirements_error` (bool, optional): Определяет, нужно ли вызывать исключение `MissingRequirementsError`, если не установлена библиотека `browser_cookie3`. По умолчанию `True`.
*   `single_browser` (bool, optional): Если `True`, загружает cookie только из первого браузера, в котором они найдены. По умолчанию `False`.

**Возвращает**:

*   `Dict[str, str]`: Словарь, где ключи - имена cookie, а значения - их значения.

**Как работает функция**:

1.  Проверяет, установлена ли библиотека `browser_cookie3`. Если нет и `raise_requirements_error` равен `True`, вызывает исключение `MissingRequirementsError`.
2.  Перебирает список браузеров (`browsers`).
3.  Для каждого браузера пытается загрузить cookie с помощью соответствующей функции.
4.  Если cookie успешно загружены, добавляет их в общий словарь `cookies`, пропуская cookie с истекшим сроком действия.
5.  Если `single_browser` равен `True`, прекращает загрузку cookie после первого успешного браузера.
6.  Обрабатывает исключения `BrowserCookieError` и другие исключения, возникающие при загрузке cookie из браузера.

**Примеры**:

```python
cookies = load_cookies_from_browsers('.google.com')
print(cookies) #  Вывод:  {'cookie_name': 'cookie_value', ...}
```

### `set_cookies_dir`

```python
def set_cookies_dir(dir: str) -> None:
    """
    Sets the directory where cookies are stored.

    Args:
        dir (str): The directory where cookies are stored.

    Returns:
        None
    """
    ...
```

**Назначение**:
Устанавливает каталог, в котором хранятся файлы cookie.

**Параметры**:

*   `dir` (str): Путь к каталогу, в котором хранятся файлы cookie.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Устанавливает значение атрибута `cookies_dir` класса `CookiesConfig` равным переданному значению `dir`.

**Примеры**:

```python
set_cookies_dir('./my_cookies')
```

### `get_cookies_dir`

```python
def get_cookies_dir() -> str:
    """
    Gets the directory where cookies are stored.

    Returns:
        str: The directory where cookies are stored.
    """
    ...
```

**Назначение**:
Возвращает каталог, в котором хранятся файлы cookie.

**Параметры**:

*   Нет

**Возвращает**:

*   `str`: Путь к каталогу, в котором хранятся файлы cookie.

**Как работает функция**:

1.  Возвращает значение атрибута `cookies_dir` класса `CookiesConfig`.

**Примеры**:

```python
cookies_dir = get_cookies_dir()
print(cookies_dir) #  Вывод:  ./har_and_cookies
```

### `read_cookie_files`

```python
def read_cookie_files(dirPath: str = None):
    """
    Reads cookie files from the specified directory.

    Args:
        dirPath (str, optional): The path to the directory containing cookie files. Defaults to None.

    Returns:
        None
    """
    ...
```

**Назначение**:
Считывает файлы cookie из указанного каталога.

**Параметры**:

*   `dirPath` (str, optional): Путь к каталогу, содержащему файлы cookie. Если `None`, используется значение `CookiesConfig.cookies_dir`. По умолчанию `None`.

**Возвращает**:

*   `None`

**Как работает функция**:

1.  Определяет путь к каталогу с файлами cookie. Если `dirPath` не указан, используется значение `CookiesConfig.cookies_dir`.
2.  Проверяет, доступен ли каталог для чтения. Если нет, выводит сообщение в лог и завершает работу.
3.  Находит все файлы с расширениями `.har` и `.json` в указанном каталоге и его подкаталогах.
4.  Перебирает найденные HAR-файлы.
5.  Для каждого HAR-файла пытается загрузить JSON-содержимое. Если загрузка не удалась, переходит к следующему файлу.
6.  Извлекает домен из каждого элемента `entries` в HAR-файле с помощью функции `get_domain`.
7.  Извлекает cookie из каждого элемента `entries` и сохраняет их в `CookiesConfig.cookies`.
8.  Перебирает найденные JSON-файлы.
9.  Для каждого JSON-файла пытается загрузить JSON-содержимое. Если загрузка не удалась или файл не является списком словарей с доменами, переходит к следующему файлу.
10. Извлекает cookie из каждого элемента и сохраняет их в `CookiesConfig.cookies`.

**Внутренние функции**:

#### `get_domain`

```python
def get_domain(v: dict) -> str:
    """
    Extracts the domain from a HAR entry.

    Args:
        v (dict): A HAR entry.

    Returns:
        str: The domain name, or None if not found.
    """
    ...
```

**Назначение**:
Извлекает домен из записи HAR.

**Параметры**:

*   `v` (dict): Запись HAR.

**Возвращает**:

*   `str`: Имя домена или `None`, если домен не найден.

**Как работает функция**:

1.  Извлекает заголовок `host` или `:authority` из записи HAR.
2.  Если заголовок не найден, возвращает `None`.
3.  Проверяет, содержится ли домен в списке `DOMAINS`.
4.  Если домен найден, возвращает его.

**Примеры**:

```python
read_cookie_files('./my_cookies')