# Модуль для работы с cookies
================================

Модуль содержит функции и классы для загрузки, управления и хранения cookies из различных источников, включая браузеры и файлы.

## Обзор

Этот модуль предназначен для работы с cookies, используемыми для аутентификации и сохранения состояния сессии при взаимодействии с веб-сайтами. Он предоставляет функции для загрузки cookies из различных браузеров, чтения из файлов и управления ими. Модуль также включает конфигурацию для хранения и управления каталогом cookies.

## Подробней

Модуль `cookies.py` в проекте `hypotez` предназначен для автоматизации процессов, связанных с cookies, что позволяет эффективно управлять сессиями и данными пользователей при взаимодействии с веб-сайтами. Он обеспечивает гибкий и удобный способ загрузки, хранения и использования cookies, что особенно важно при тестировании и автоматизации веб-приложений.

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
    ...
```

**Назначение**: Функция `g4f` предназначена для загрузки cookies из специального браузера `'g4f'`, если он установлен и настроен. Этот браузер может использоваться для специфических целей, требующих отдельной конфигурации cookies.

**Параметры**:
- `domain_name` (str): Домен, для которого необходимо загрузить cookies.

**Возвращает**:
- `list`: Список cookies, полученных из браузера `'g4f'`. Если браузер не найден или cookies отсутствуют, возвращается пустой список.

**Как работает функция**:
1. Проверяет, установлена ли библиотека `platformdirs`. Если нет, возвращает пустой список.
2. Определяет путь к каталогу с данными пользователя для браузера `'g4f'`.
3. Формирует путь к файлу с cookies (`Cookies`).
4. Если файл не существует, возвращает пустой список.
5. Использует функцию `chrome` из `browser_cookie3` для загрузки cookies из указанного файла для заданного домена.

**Примеры**:

```python
cookies = g4f('.google.com')
if cookies:
    print(f'Найдено {len(cookies)} cookies для домена .google.com')
else:
    print('Cookies для домена .google.com не найдены')
```

### `get_cookies`

```python
def get_cookies(domain_name: str, raise_requirements_error: bool = True, single_browser: bool = False, cache_result: bool = True) -> Dict[str, str]:
    """
    Загружает cookies для заданного домена из всех поддерживаемых браузеров и кэширует результаты.

    Args:
        domain_name (str): Домен, для которого загружаются cookies.
        raise_requirements_error (bool): Если `True`, вызывает исключение `MissingRequirementsError`, если не установлен пакет `browser_cookie3`.
        single_browser (bool): Если `True`, загружает cookies только из первого найденного браузера.
        cache_result (bool): Если `True`, кэширует результаты для последующих вызовов.

    Returns:
        Dict[str, str]: Словарь с именами и значениями cookie.
    """
    ...
```

**Назначение**: Функция `get_cookies` предназначена для получения cookies для указанного домена из всех поддерживаемых браузеров. Она также поддерживает кэширование результатов для повышения производительности.

**Параметры**:
- `domain_name` (str): Домен, для которого необходимо получить cookies.
- `raise_requirements_error` (bool): Флаг, указывающий, следует ли вызывать исключение, если не установлены необходимые зависимости. По умолчанию `True`.
- `single_browser` (bool): Флаг, указывающий, следует ли загружать cookies только из первого найденного браузера. По умолчанию `False`.
- `cache_result` (bool): Флаг, указывающий, следует ли кэшировать результаты для последующих вызовов. По умолчанию `True`.

**Возвращает**:
- `Dict[str, str]`: Словарь, содержащий имена и значения cookies.

**Как работает функция**:
1. Проверяет, есть ли cookies для данного домена в кэше (`CookiesConfig.cookies`). Если есть и `cache_result` равен `True`, возвращает кэшированные cookies.
2. Вызывает функцию `load_cookies_from_browsers` для загрузки cookies из браузеров.
3. Если `cache_result` равен `True`, сохраняет полученные cookies в кэш.
4. Возвращает полученные cookies.

**Примеры**:

```python
cookies = get_cookies('.google.com')
if cookies:
    print(f'Найдено {len(cookies)} cookies для домена .google.com')
else:
    print('Cookies для домена .google.com не найдены')
```

### `set_cookies`

```python
def set_cookies(domain_name: str, cookies: Cookies = None) -> None:
    """
    Устанавливает cookies для заданного домена.

    Args:
        domain_name (str): Домен, для которого устанавливаются cookies.
        cookies (Cookies, optional): Словарь с cookies для установки. Если `None`, удаляет cookies для указанного домена.
    """
    ...
```

**Назначение**: Функция `set_cookies` позволяет установить или удалить cookies для определенного домена в кэше `CookiesConfig.cookies`.

**Параметры**:
- `domain_name` (str): Домен, для которого устанавливаются или удаляются cookies.
- `cookies` (Cookies, optional): Cookies, которые необходимо установить для данного домена. Если значение равно `None`, cookies для данного домена будут удалены.

**Как работает функция**:
1. Если передан словарь `cookies`, он сохраняется в `CookiesConfig.cookies` для указанного домена.
2. Если `cookies` равен `None`, функция пытается удалить запись о cookies для указанного домена из `CookiesConfig.cookies`.

**Примеры**:

```python
# Установка cookies для домена .example.com
cookies = {'sessionid': '123', 'csrftoken': 'abc'}
set_cookies('.example.com', cookies)

# Удаление cookies для домена .example.com
set_cookies('.example.com', None)
```

### `load_cookies_from_browsers`

```python
def load_cookies_from_browsers(domain_name: str, raise_requirements_error: bool = True, single_browser: bool = False) -> Cookies:
    """
    Вспомогательная функция для загрузки cookies из различных браузеров.

    Args:
        domain_name (str): Домен, для которого загружаются cookies.
        raise_requirements_error (bool): Если `True`, вызывает исключение `MissingRequirementsError`, если не установлен пакет `browser_cookie3`.
        single_browser (bool): Если `True`, загружает cookies только из первого найденного браузера.

    Returns:
        Dict[str, str]: Словарь с именами и значениями cookie.
    """
    ...
```

**Назначение**: Функция `load_cookies_from_browsers` предназначена для загрузки cookies из различных установленных браузеров. Она итерируется по списку поддерживаемых браузеров и пытается получить cookies для указанного домена.

**Параметры**:
- `domain_name` (str): Домен, для которого загружаются cookies.
- `raise_requirements_error` (bool): Если `True`, вызывает исключение `MissingRequirementsError`, если не установлен пакет `browser_cookie3`. По умолчанию `True`.
- `single_browser` (bool): Если `True`, загружает cookies только из первого браузера, который успешно вернул cookies. По умолчанию `False`.

**Возвращает**:
- `Dict[str, str]`: Словарь, содержащий имена и значения cookies, собранные из всех доступных браузеров.

**Как работает функция**:
1. Проверяет, установлен ли пакет `browser_cookie3`. Если нет и `raise_requirements_error` равен `True`, вызывает исключение `MissingRequirementsError`.
2. Инициализирует пустой словарь `cookies` для хранения полученных cookies.
3. Итерируется по списку функций для загрузки cookies из разных браузеров (`browsers`).
4. Для каждого браузера пытается получить cookies, обрабатывая возможные исключения (`BrowserCookieError` и `Exception`).
5. Если cookies успешно получены, добавляет их в общий словарь `cookies`, проверяя, не истек ли срок их действия.
6. Если `single_browser` равен `True` и cookies были успешно получены, прекращает итерацию по остальным браузерам.
7. Возвращает словарь с собранными cookies.

**Примеры**:

```python
cookies = load_cookies_from_browsers('.google.com')
if cookies:
    print(f'Найдено {len(cookies)} cookies для домена .google.com')
else:
    print('Cookies для домена .google.com не найдены')
```

### `set_cookies_dir`

```python
def set_cookies_dir(dir: str) -> None:
    """
    Устанавливает каталог для хранения файлов cookie.

    Args:
        dir (str): Путь к каталогу для хранения файлов cookie.
    """
    ...
```

**Назначение**: Функция `set_cookies_dir` устанавливает каталог, используемый для хранения файлов cookie. Это позволяет изменить местоположение, где хранятся файлы cookie, настраивая таким образом параметры хранения cookie.

**Параметры**:
- `dir` (str): Строка, представляющая путь к каталогу, который будет использоваться для хранения файлов cookie.

**Как работает функция**:
1. Присваивает значение параметра `dir` атрибуту `CookiesConfig.cookies_dir`, изменяя таким образом местоположение каталога для хранения файлов cookie.

**Примеры**:

```python
# Установка нового каталога для хранения файлов cookie
set_cookies_dir('./custom_cookies')
```

### `get_cookies_dir`

```python
def get_cookies_dir() -> str:
    """
    Возвращает каталог, используемый для хранения файлов cookie.

    Returns:
        str: Путь к каталогу для хранения файлов cookie.
    """
    ...
```

**Назначение**: Функция `get_cookies_dir` возвращает путь к каталогу, который в данный момент используется для хранения файлов cookie. Это позволяет получить информацию о текущем местоположении файлов cookie.

**Возвращает**:
- `str`: Строка, представляющая путь к каталогу, используемому для хранения файлов cookie.

**Как работает функция**:
1. Возвращает значение атрибута `CookiesConfig.cookies_dir`, который содержит путь к каталогу для хранения файлов cookie.

**Примеры**:

```python
# Получение текущего каталога для хранения файлов cookie
cookies_dir = get_cookies_dir()
print(f'Текущий каталог для хранения файлов cookie: {cookies_dir}')
```

### `read_cookie_files`

```python
def read_cookie_files(dirPath: str = None):
    """
    Читает файлы cookie из указанного каталога.

    Args:
        dirPath (str, optional): Путь к каталогу с файлами cookie. Если `None`, используется `CookiesConfig.cookies_dir`.
    """
    ...
```

**Назначение**: Функция `read_cookie_files` предназначена для чтения файлов cookie из указанного каталога. Она сканирует каталог в поисках файлов с расширениями `.har` и `.json`, содержащих информацию о cookie, и загружает эту информацию в `CookiesConfig.cookies`.

**Параметры**:
- `dirPath` (str, optional): Путь к каталогу, в котором расположены файлы cookie. Если не указан, используется значение по умолчанию из `CookiesConfig.cookies_dir`.

**Как работает функция**:
1. Определяет путь к каталогу для чтения файлов cookie. Если `dirPath` не указан, используется значение из `CookiesConfig.cookies_dir`.
2. Проверяет наличие прав на чтение каталога. Если прав нет, выводит сообщение в лог и завершает работу.
3. Сканирует каталог в поисках файлов с расширениями `.har` и `.json`.
4. Для каждого найденного `.har` файла пытается загрузить его содержимое как JSON и извлечь информацию о cookie.
5. Для каждого найденного `.json` файла пытается загрузить его содержимое как JSON и извлечь информацию о cookie.
6. Обновляет `CookiesConfig.cookies` информацией о cookie, полученной из файлов.

**Внутренние функции**:

- `get_domain(v: dict) -> str`
    ```python
        def get_domain(v: dict) -> str:
            """
            Извлекает домен из записи HAR файла.
    
            Args:
                v (dict): Запись HAR файла.
    
            Returns:
                str: Доменное имя, если найдено, иначе `None`.
            """
            ...
    ```
    **Назначение**: Извлекает доменное имя из записи HAR (HTTP Archive) файла.

    **Параметры**:
    - `v` (dict): Словарь, представляющий запись HAR файла.

    **Возвращает**:
    - `str`: Доменное имя, если оно найдено в заголовках запроса, иначе `None`.

    **Как работает функция**:
    1. Извлекает значения заголовков 'host' или ':authority' из записи HAR файла.
    2. Если заголовки не найдены, возвращает `None`.
    3. Извлекает первое значение из списка заголовков.
    4. Проверяет, содержит ли значение доменное имя из списка `DOMAINS`.
    5. Если доменное имя найдено, возвращает его, иначе возвращает `None`.

**Примеры**:

```python
# Чтение файлов cookie из каталога по умолчанию
read_cookie_files()

# Чтение файлов cookie из указанного каталога
read_cookie_files('./custom_cookies')
```

## Классы

### `CookiesConfig`

```python
class CookiesConfig():
    """
    Конфигурация для хранения и управления cookies.

    Attributes:
        cookies (Dict[str, Cookies]): Словарь, содержащий cookies для различных доменов.
        cookies_dir (str): Путь к каталогу для хранения файлов cookie.
    """
    ...
```

**Описание**: Класс `CookiesConfig` предназначен для хранения и управления глобальными настройками, связанными с cookies.

**Аттрибуты**:
- `cookies` (Dict[str, Cookies]): Словарь, где ключом является доменное имя (str), а значением - словарь с cookies для этого домена.
- `cookies_dir` (str): Путь к каталогу, где хранятся файлы с cookies. По умолчанию `"./har_and_cookies"`.

### Принцип работы:
Класс `CookiesConfig` служит контейнером для хранения глобальных настроек, связанных с cookies, таких как словарь с cookies для различных доменов и путь к каталогу для хранения файлов cookie. Он используется для централизованного управления cookies в приложении.

## Переменные

### `DOMAINS`

```python
DOMAINS = [
    ".bing.com",
    ".meta.ai",
    ".google.com",
    "www.whiterabbitneo.com",
    "huggingface.co",
    "chat.reka.ai",
    "chatgpt.com",
    ".cerebras.ai",
    "github.com",
    "huggingface.co",
    ".huggingface.co"
]
```

**Описание**: Список доменных имен, используемых для определения домена из HAR-файлов.

## Обработка условий

```python
if has_browser_cookie3 and os.environ.get('DBUS_SESSION_BUS_ADDRESS') == "/dev/null":
    _LinuxPasswordManager.get_password = lambda a, b: b"secret"
```

**Назначение**: Этот условный блок предназначен для обхода проблемы с `browser_cookie3` в окружениях, где отсутствует доступ к DBus (например, в Docker-контейнерах).

**Как работает**:
1. Проверяет, установлен ли пакет `browser_cookie3` и установлено ли значение переменной окружения `DBUS_SESSION_BUS_ADDRESS` в `/dev/null`.
2. Если оба условия выполняются, переопределяет метод `get_password` класса `_LinuxPasswordManager` таким образом, чтобы он всегда возвращал `"secret"`. Это позволяет избежать запросов к DBus для получения паролей, что необходимо в окружениях без доступа к DBus.

## Оглавление

1.  [Обзор](#обзор)
2.  [Подробней](#подробней)
3.  [Функции](#функции)
    *   [g4f](#g4f)
    *   [get_cookies](#get_cookies)
    *   [set_cookies](#set_cookies)
    *   [load_cookies_from_browsers](#load_cookies_from_browsers)
    *   [set_cookies_dir](#set_cookies_dir)
    *   [get_cookies_dir](#get_cookies_dir)
    *   [read_cookie_files](#read_cookie_files)
4.  [Классы](#классы)
    *   [CookiesConfig](#cookiesconfig)
5.  [Переменные](#переменные)
    *   [DOMAINS](#domains)
6.  [Обработка условий](#обработка-условий)