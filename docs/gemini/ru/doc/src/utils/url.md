# Модуль `hypotez/src/utils/url.py`

## Обзор

Модуль `url.py` предоставляет функции для работы с URL-строками, включая извлечение параметров запроса и проверку на валидность URL.

## Функции

### `extract_url_params`

**Описание**: Функция извлекает параметры из строки URL.

**Параметры**:
- `url` (str): Строка URL для парсинга.

**Возвращает**:
- `dict | None`: Словарь параметров запроса и их значений или `None`, если URL не содержит параметров.

**Вызывает исключения**:
- Нет


### `is_url`

**Описание**: Проверяет, является ли переданный текст валидным URL с использованием библиотеки `validators`.

**Параметры**:
- `text` (str): Строка для проверки.

**Возвращает**:
- `bool`: `True` если строка является валидным URL, иначе `False`.

**Вызывает исключения**:
- Нет


## Примеры использования (внутри модуля)

```python
# Пример использования extract_url_params
url = "https://example.com/path?param1=value1&param2=value2&param3="
params = extract_url_params(url)
if params:
    print(params)  # Output: {'param1': 'value1', 'param2': 'value2', 'param3': ''}

url_no_params = "https://example.com/path"
params_no_params = extract_url_params(url_no_params)
if params_no_params is None:
  print("URL не содержит параметров")

# Пример использования is_url
valid_url = "https://www.example.com"
invalid_url = "invalid_url"
print(is_url(valid_url))  # Output: True
print(is_url(invalid_url))  # Output: False
```

##  Обработка ввода и вывода (внутри модуля)

Внутри модуля реализована функция `if __name__ == "__main__":`, которая позволяет протестировать модуль непосредственно, запрашивая у пользователя URL и проверяя его валидность. Если URL является валидным, то извлекаются параметры и выводятся на экран.