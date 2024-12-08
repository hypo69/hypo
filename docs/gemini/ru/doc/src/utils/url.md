# Модуль `hypotez/src/utils/string/url.py`

## Обзор

Этот модуль предоставляет функции для работы со строками URL, включая извлечение параметров запроса и проверку валидности URL-адресов.

## Функции

### `extract_url_params`

**Описание**: Извлекает параметры из строки URL.

**Параметры**:
- `url` (str): Строка URL для парсинга.

**Возвращает**:
- `dict | None`: Словарь параметров запроса и их значений или `None`, если URL не содержит параметров.

**Примеры использования**:

```python
url = "https://example.com/page?param1=value1&param2=value2&param3="
params = extract_url_params(url)
print(params)  # Output: {'param1': 'value1', 'param2': 'value2', 'param3': ''}
```

```python
url = "https://example.com/page"
params = extract_url_params(url)
print(params) # Output: None
```

### `is_url`

**Описание**: Проверяет, является ли переданный текст валидным URL с использованием библиотеки `validators`.

**Параметры**:
- `text` (str): Строка для проверки.

**Возвращает**:
- `bool`: `True` если строка является валидным URL, иначе `False`.

**Примеры использования**:

```python
url1 = "https://www.example.com"
url2 = "invalid_url"
print(is_url(url1))  # Output: True
print(is_url(url2))  # Output: False
```

## Пример использования модуля

```python
# Получаем строку URL от пользователя
url = input("Введите URL: ")

# Проверяем валидность URL
if is_url(url):
    params = extract_url_params(url)

    # Выводим параметры
    if params:
        print("Параметры URL:")
        for key, value in params.items():
            print(f"{key}: {value}")
    else:
        print("URL не содержит параметров.")
else:
    print("Введенная строка не является валидным URL.")
```

```python
# Пример вывода при вводе "https://www.example.com/page?param1=value1&param2=value2"
# Параметры URL:
# param1: value1
# param2: value2
```

```python
# Пример вывода при вводе "invalid_url"
# Введенная строка не является валидным URL.
```

## Описание модуля

Модуль `src.utils.string.url` предоставляет вспомогательные функции для работы с URL-адресами, в том числе для извлечения параметров запроса и проверки валидности URL. Функции `extract_url_params` и `is_url` предназначены для упрощения работы с URL-адресами в Python-приложениях.
```