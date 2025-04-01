# Модуль для работы с URL строками
## Обзор

Модуль `src.utils.string.url` предоставляет функциональность для работы с URL строками, включая извлечение параметров запроса, проверку на валидность URL и сокращение ссылок. Он включает функции для парсинга URL, проверки их валидности и сокращения длинных URL с использованием сервиса TinyURL.

## Подробней

Этот модуль предназначен для облегчения работы с URL в проекте `hypotez`. Он позволяет извлекать параметры из URL для дальнейшей обработки, проверять, является ли строка валидным URL, и сокращать длинные URL для удобства использования и обмена.

## Функции

### `extract_url_params`

```python
def extract_url_params(url: str) -> dict | None:
    """ Извлекает параметры из строки URL.

    Args:
        url (str): Строка URL для парсинга.

    Returns:
        dict | None: Словарь параметров запроса и их значений или `None`, если URL не содержит параметров.
    """
    ...
```

**Назначение**: Извлекает параметры запроса из URL строки.

**Параметры**:
- `url` (str): URL строка, из которой нужно извлечь параметры.

**Возвращает**:
- `dict | None`: Словарь, содержащий параметры запроса и их значения. Если URL не содержит параметров, возвращает `None`.

**Как работает функция**:
1. URL строка парсится с использованием `urlparse` для разделения URL на компоненты.
2. Извлекается строка запроса (query) из URL.
3. Строка запроса парсится с использованием `parse_qs` для получения словаря параметров.
4. Если параметры присутствуют, значения параметров преобразуются из списка в строку, если параметр имеет только одно значение.
5. Возвращается словарь параметров.

```
URL -> Парсинг URL (urlparse)
|
Извлечение строки запроса
|
Парсинг строки запроса (parse_qs)
|
Преобразование значений параметров (из списка в строку, если len(v)==1)
|
Возврат словаря параметров
```

**Примеры**:
```python
url_with_params = "https://example.com?param1=value1&param2=value2"
params = extract_url_params(url_with_params)
print(params)  # Вывод: {'param1': 'value1', 'param2': 'value2'}

url_with_single_param = "https://example.com?param1=value1"
params = extract_url_params(url_with_single_param)
print(params)  # Вывод: {'param1': 'value1'}

url_without_params = "https://example.com"
params = extract_url_params(url_without_params)
print(params)  # Вывод: None
```

### `is_url`

```python
def is_url(text: str) -> bool:
    """ Проверяет, является ли переданный текст валидным URL с использованием библиотеки validators.

    Args:
        text (str): Строка для проверки.

    Returns:
        bool: `True` если строка является валидным URL, иначе `False`.
    """
    ...
```

**Назначение**: Проверяет, является ли переданная строка валидным URL.

**Параметры**:
- `text` (str): Строка, которую необходимо проверить.

**Возвращает**:
- `bool`: `True`, если строка является валидным URL, иначе `False`.

**Как работает функция**:
1. Функция использует библиотеку `validators` для проверки, является ли переданная строка валидным URL.
2. Возвращает результат проверки.

```
Строка для проверки -> Проверка URL (validators.url)
|
Возврат результата (True или False)
```

**Примеры**:
```python
valid_url = "https://example.com"
is_valid = is_url(valid_url)
print(is_valid)  # Вывод: True

invalid_url = "not a url"
is_valid = is_url(invalid_url)
print(is_valid)  # Вывод: False
```

### `url_shortener`

```python
def url_shortener(long_url: str) -> str | None:
    """ Сокращает длинный URL с использованием сервиса TinyURL.

    Args:
        long_url (str): Длинный URL для сокращения.

    Returns:
        str | None: Сокращённый URL или `None`, если произошла ошибка.
    """
    ...
```

**Назначение**: Сокращает длинный URL с использованием сервиса TinyURL.

**Параметры**:
- `long_url` (str): Длинный URL, который нужно сократить.

**Возвращает**:
- `str | None`: Сокращенный URL или `None`, если произошла ошибка.

**Как работает функция**:
1. Формируется URL для запроса к API TinyURL.
2. Отправляется GET запрос к API TinyURL.
3. Если запрос успешен (status_code == 200), возвращается сокращенный URL из ответа.
4. В случае ошибки возвращается `None`.

```
Длинный URL -> Формирование URL для запроса к API TinyURL
|
Отправка GET запроса к API TinyURL
|
Успешный ответ?
| Да:
Извлечение сокращенного URL из ответа
|
Возврат сокращенного URL
| Нет:
Возврат None
```

**Примеры**:
```python
long_url = "https://example.com/very/long/url/to/some/resource"
short_url = url_shortener(long_url)
print(short_url)  # Вывод: http://tinyurl.com/xxxxxx (или None, если произошла ошибка)

another_long_url = "https://example.com/another/long/url"
short_url = url_shortener(another_long_url)
print(short_url)  # Вывод: http://tinyurl.com/yyyyyy (или None, если произошла ошибка)
```