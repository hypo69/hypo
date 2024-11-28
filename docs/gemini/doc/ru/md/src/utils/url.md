# Модуль `hypotez/src/utils/url.py`

## Обзор

Модуль `hypotez/src/utils/url.py` предоставляет функции для работы со строками URL, включая извлечение параметров запроса и проверку на валидность.

## Функции

### `extract_url_params`

**Описание**: Функция извлекает параметры из строки URL.

**Параметры**:
- `url` (str): Строка URL для парсинга.

**Возвращает**:
- `dict | None`: Словарь параметров запроса и их значений или `None`, если URL не содержит параметров.


### `is_url`

**Описание**: Функция проверяет, является ли переданный текст валидным URL с использованием библиотеки `validators`.

**Параметры**:
- `text` (str): Строка для проверки.

**Возвращает**:
- `bool`: `True`, если строка является валидным URL, иначе `False`.


## Примеры использования

```python
# Пример использования extract_url_params
url = "https://example.com/page?param1=value1&param2=value2&param3="
params = extract_url_params(url)
if params:
    print(params)  # Output: {'param1': 'value1', 'param2': 'value2', 'param3': ''}

url_no_params = "https://example.com/page"
params = extract_url_params(url_no_params)
if params is None:
    print("URL не содержит параметров.")


# Пример использования is_url
valid_url = "https://www.example.com"
invalid_url = "invalid_url"

print(f"'{valid_url}' is a valid URL: {is_url(valid_url)}")  # Output: True
print(f"'{invalid_url}' is a valid URL: {is_url(invalid_url)}")  # Output: False
```

##  Обработка исключений


Этот модуль не содержит блоков обработки исключений.

**Примечание**:  Этот модуль использует библиотеку `validators`, которую необходимо установить, если она отсутствует.  
```bash
pip install validators
```