# Модуль `hypotez/src/utils/string/url.py`

## Обзор

Модуль `src.utils.string.url` предоставляет функции для работы со строками URL, включая извлечение параметров запроса и проверку на валидность URL-адресов.

## Функции

### `extract_url_params`

**Описание**: Извлекает параметры из строки URL.

**Параметры**:
- `url` (str): Строка URL для парсинга.

**Возвращает**:
- `dict | None`: Словарь параметров запроса и их значений или `None`, если URL не содержит параметров.

**Пример использования**:
```python
url = "https://example.com/path?param1=value1&param2=value2&param3="
params = extract_url_params(url)
print(params)  # Output: {'param1': 'value1', 'param2': 'value2', 'param3': ''}
```


### `is_url`

**Описание**: Проверяет, является ли переданный текст валидным URL с использованием библиотеки `validators`.

**Параметры**:
- `text` (str): Строка для проверки.

**Возвращает**:
- `bool`: `True`, если строка является валидным URL, иначе `False`.

**Пример использования**:
```python
url = "https://example.com"
valid_url = is_url(url)
print(valid_url)  # Output: True

invalid_url = "invalid_url"
invalid_valid_url = is_url(invalid_url)
print(invalid_valid_url)  # Output: False
```

##  Пример использования (встроенный в модуль):

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

**Примечание**:  Код примера демонстрирует как использовать функции из модуля и обрабатывать возможные ошибки.