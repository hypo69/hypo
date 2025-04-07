# Модуль `utils`

## Обзор

Модуль `utils` предоставляет утилиты для получения cookies из различных браузеров. Он включает класс `Utils` с методом `get_cookies`, который позволяет извлекать cookies для определенного домена из поддерживаемых браузеров.

## Подробней

Этот модуль предназначен для автоматического сбора cookies из установленных браузеров. Он полезен в случаях, когда необходимо аутентифицироваться на веб-сайтах без ручного ввода данных. Модуль использует библиотеку `browser_cookie3` для доступа к cookies браузеров.

## Классы

### `Utils`

**Описание**: Класс `Utils` предоставляет статические методы для работы с cookies браузеров.

**Принцип работы**: Класс содержит список поддерживаемых браузеров и метод для извлечения cookies из этих браузеров.

**Атрибуты**:

- `browsers` (List[browser_cookie3]): Список поддерживаемых браузеров, таких как Chrome, Safari, Firefox, Edge, Opera, Brave, Opera GX и Vivaldi.

**Методы**:

- `get_cookies`: Метод для получения cookies для указанного домена из различных браузеров.

## Функции

### `get_cookies`

```python
def get_cookies(domain: str, setName: str = None, setBrowser: str = False) -> dict:
    """ Функция для получения cookies для указанного домена из различных браузеров.

    Args:
        domain (str): Домен, для которого нужно получить cookies.
        setName (str, optional): Имя конкретной cookie, которую нужно получить. По умолчанию `None`.
        setBrowser (str, optional): Имя конкретного браузера, из которого нужно получить cookies. По умолчанию `False`.

    Returns:
        dict: Словарь с cookies, где ключи - имена cookies, а значения - их значения.

    Raises:
        ValueError: Если `setName` указан, но cookie с таким именем не найдена ни в одном браузере.

    Example:
        >>> cookies = Utils.get_cookies('example.com')
        >>> print(cookies)
        {'cookie1': 'value1', 'cookie2': 'value2', ...}

        >>> specific_cookie = Utils.get_cookies('example.com', setName='cookie1')
        >>> print(specific_cookie)
        {'cookie1': 'value1'}

        >>> browser_cookie = Utils.get_cookies('example.com', setBrowser='chrome')
        >>> print(browser_cookie)
        {'cookie1': 'value1', 'cookie2': 'value2', ...}
    """
```

**Назначение**: Получение cookies для указанного домена из различных браузеров.

**Параметры**:

- `domain` (str): Домен, для которого нужно получить cookies.
- `setName` (str, optional): Имя конкретной cookie, которую нужно получить. По умолчанию `None`.
- `setBrowser` (str, optional): Имя конкретного браузера, из которого нужно получить cookies. По умолчанию `False`.

**Возвращает**:

- `dict`: Словарь с cookies, где ключи - имена cookies, а значения - их значения.

**Вызывает исключения**:

- `ValueError`: Если `setName` указан, но cookie с таким именем не найдена ни в одном браузере.

**Как работает функция**:

1. Инициализация пустого словаря `cookies` для хранения извлеченных cookies.
2. Проверка, указан ли конкретный браузер для поиска cookies (`setBrowser`).
3. Если `setBrowser` указан, выполняется перебор браузеров из списка `Utils.browsers` в поисках соответствующего браузера.
4. Если `setBrowser` не указан, выполняется перебор всех браузеров из списка `Utils.browsers`.
5. Для каждого браузера выполняется попытка извлечения cookies для указанного домена.
6. Cookies извлекаются с использованием метода `browser(domain_name=domain)` из библиотеки `browser_cookie3`.
7. Каждая cookie добавляется в словарь `cookies`, если её имени ещё нет в словаре.
8. Обрабатываются исключения, которые могут возникнуть при доступе к cookies браузера.
9. Если указано имя конкретной cookie (`setName`), функция пытается вернуть только эту cookie из словаря.
10. Если `setName` указан, но cookie с таким именем не найдена, вызывается исключение `ValueError`.
11. Если `setName` не указан, функция возвращает словарь со всеми найденными cookies.

```
    A: Инициализация словаря cookies
    │
    ├── B: Проверка setBrowser
    │   ├── C1: Перебор браузеров (setBrowser)
    │   │   ├── D1: Извлечение cookies из браузера
    │   │   │   ├── E1: Добавление cookie в словарь
    │   │   │   └── E2: Обработка исключений
    │   │   └── C2: Перебор браузеров (все)
    │   │       ├── D2: Извлечение cookies из браузера
    │   │       │   ├── E3: Добавление cookie в словарь
    │   │       │   └── E4: Обработка исключений
    │   │       └── F: Проверка setName
    │   │           ├── G1: Возврат конкретной cookie
    │   │           └── G2: Возврат всех cookies
    │   │
    │   └── H: Обработка ошибок и возврат результата
    │
    └── I: Возврат словаря cookies
```

**Примеры**:

```python
# Получение всех cookies для домена example.com
cookies = Utils.get_cookies('example.com')
print(cookies)

# Получение конкретной cookie с именем 'cookie1' для домена example.com
specific_cookie = Utils.get_cookies('example.com', setName='cookie1')
print(specific_cookie)

# Получение cookies для домена example.com из браузера Chrome
browser_cookie = Utils.get_cookies('example.com', setBrowser='chrome')
print(browser_cookie)