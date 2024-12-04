# Модуль `hypotez/src/utils/string/url.py`

## Обзор

Модуль `url.py` предоставляет функции для работы со строками URL, включая извлечение параметров запроса и проверку на валидность URL.

## Функции

### `extract_url_params`

**Описание**: Извлекает параметры из строки URL.

**Параметры**:

- `url` (str): Строка URL для парсинга.

**Возвращает**:

- `dict | None`: Словарь параметров запроса и их значений или `None`, если URL не содержит параметров.


**Примеры использования:**

```python
url = "https://example.com/page?param1=value1&param2=value2&param3="
params = extract_url_params(url)
print(params)  # Output: {'param1': 'value1', 'param2': 'value2', 'param3': ''}

url2 = "https://example.com/page"
params2 = extract_url_params(url2)
print(params2)  # Output: None
```


### `is_url`

**Описание**: Проверяет, является ли переданный текст валидным URL с использованием библиотеки `validators`.

**Параметры**:

- `text` (str): Строка для проверки.

**Возвращает**:

- `bool`: `True` если строка является валидным URL, иначе `False`.


**Примеры использования:**

```python
url = "https://www.example.com"
is_valid = is_url(url)
print(is_valid)  # Output: True

invalid_url = "invalid-url"
is_valid2 = is_url(invalid_url)
print(is_valid2)  # Output: False
```

## Пример использования модуля (внутри файла)

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

**Примечания**:

* Код внутри `if __name__ == "__main__":` выполняется только при непосредственном запуске скрипта.  Этот блок демонстрирует взаимодействие функций и их применение.
* Обратите внимание на обработку случаев, когда URL не содержит параметров запроса.
* В примерах `extract_url_params` показано, как функция обрабатывает случаи с одним значением параметра, предотвращая получение списка как значения.


```