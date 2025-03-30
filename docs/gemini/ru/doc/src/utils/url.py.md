# Модуль `url`

## Обзор

Модуль `url` предоставляет инструменты для работы с URL-адресами, включая извлечение параметров запроса, проверку валидности URL и сокращение длинных ссылок с использованием сервиса TinyURL.

## Подробней

Этот модуль предназначен для упрощения работы с URL-адресами в Python. Он включает функции для проверки валидности URL-адресов, извлечения параметров запроса и сокращения длинных URL-адресов. Модуль использует сторонние библиотеки, такие как `validators` для проверки URL и `requests` для взаимодействия с сервисом TinyURL.

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
```

**Описание**: Извлекает параметры запроса из предоставленной строки URL.

**Параметры**:
- `url` (str): URL-адрес, из которого требуется извлечь параметры.

**Возвращает**:
- `dict | None`: Словарь, содержащий параметры запроса в формате ключ-значение, или `None`, если URL не содержит параметров.

**Примеры**:
```python
url = "https://example.com?param1=value1&param2=value2"
params = extract_url_params(url)
print(params)  # Вывод: {'param1': 'value1', 'param2': 'value2'}

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
```

**Описание**: Проверяет, является ли предоставленная строка валидным URL-адресом.

**Параметры**:
- `text` (str): Строка, которую необходимо проверить на соответствие формату URL.

**Возвращает**:
- `bool`: `True`, если строка является валидным URL-адресом, и `False` в противном случае.

**Примеры**:
```python
print(is_url("https://example.com"))  # Вывод: True
print(is_url("not a url"))  # Вывод: False
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
```

**Описание**: Сокращает длинный URL-адрес с использованием сервиса TinyURL.

**Параметры**:
- `long_url` (str): URL-адрес, который требуется сократить.

**Возвращает**:
- `str | None`: Сокращенный URL-адрес или `None`, если произошла ошибка при сокращении.

**Примеры**:
```python
long_url = "https://www.example.com/very/long/url/to/shorten"
short_url = url_shortener(long_url)
if short_url:
    print(f"Сокращенный URL: {short_url}")
else:
    print("Не удалось сократить URL.")