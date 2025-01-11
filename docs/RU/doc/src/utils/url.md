# Модуль `hypotez/src/utils/url.py`

## Обзор

Этот модуль предоставляет функции для работы со строками URL, включая извлечение параметров запроса и проверку валидности URL.

## Функции

### `extract_url_params`

**Описание**: Извлекает параметры из строки URL.

**Параметры**:

- `url` (str): Строка URL для парсинга.

**Возвращает**:

- `dict | None`: Словарь параметров запроса и их значений или `None`, если URL не содержит параметров.

**Пример использования**:

```python
url = "https://example.com?param1=value1&param2=value2&param3="
params = extract_url_params(url)
print(params)  # Output: {'param1': 'value1', 'param2': 'value2', 'param3': ''}
```


### `is_url`

**Описание**: Проверяет, является ли переданный текст валидным URL с использованием библиотеки `validators`.

**Параметры**:

- `text` (str): Строка для проверки.

**Возвращает**:

- `bool`: `True` если строка является валидным URL, иначе `False`.


**Пример использования**:

```python
url = "https://www.example.com"
is_valid = is_url(url)
print(is_valid)  # Output: True

invalid_url = "invalid_url"
is_valid = is_url(invalid_url)
print(is_valid)  # Output: False
```

## Пример использования (внутри модуля)

```python
if __name__ == "__main__":
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
```