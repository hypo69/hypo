```
## File hypotez/src/utils/string/url.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils.string 
	:platform: Windows, Unix
	:synopsis: Модуль для работы с URL строками, включая извлечение параметров запроса и проверку на валидность UR
"""
MODE = 'dev'


from urllib.parse import urlparse, parse_qs
import validators

def extract_url_params(url: str) -> dict | None:
    """ Извлекает параметры из строки URL.

    Args:
        url (str): Строка URL для парсинга.

    Returns:
        dict | None: Словарь параметров запроса и их значений или `None`, если URL не содержит параметров.
    """
    parsed_url = urlparse(url)
    params = parse_qs(parsed_url.query)
    
    # Преобразуем значения из списка в строку, если параметр имеет одно значение
    if params:
        params = {k: v if len(v) > 1 else v[0] for k, v in params.items()}
        return params
    return None

def is_url(text: str) -> bool:
    """ Проверяет, является ли переданный текст валидным URL с использованием библиотеки validators.

    Args:
        text (str): Строка для проверки.

    Returns:
        bool: `True` если строка является валидным URL, иначе `False`.
    """
    return validators.url(text)


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

**<algorithm>**

```
[Start]
|
V
Get user input (URL string) --> url
|
V
is_url(url) --> True/False
|
V
[True]
|
V
extract_url_params(url) --> params
|
V
[params is not None]
|
V
Print "Параметры URL:"
Loop through params:
   Print key:value pairs
|
V
[params is None]
|
V
Print "URL не содержит параметров."
|
V
[False]
|
V
Print "Введенная строка не является валидным URL."
|
V
[End]
```

**Examples:**

* **Input:** `https://example.com/page?param1=value1&param2=value2&param3=`
* **Output:**
```
Параметры URL:
param1: value1
param2: value2
param3: 
```

* **Input:** `https://example.com/page`
* **Output:**
```
URL не содержит параметров.
```

* **Input:** `invalid-url`
* **Output:**
```
Введенная строка не является валидным URL.
```

**<explanation>**

* **Imports:**
    * `urllib.parse`: Provides functions for parsing URLs, including `urlparse` for breaking down the URL into components and `parse_qs` for extracting query parameters.  Used for extracting parameters from URLs.
    * `validators`: A library for validating various data types, including URLs. Used for checking if a given string is a valid URL.

* **Classes:**  There are no classes defined in this file.

* **Functions:**
    * `extract_url_params(url: str) -> dict | None`:
        * Takes a URL string as input.
        * Uses `urlparse` to parse the URL into components.
        * Extracts query parameters using `parse_qs`.
        * Handles cases where a parameter has multiple values or a single value. Converts single-value lists to their corresponding values in the dictionary for cleaner output.
        * Returns a dictionary containing the extracted query parameters, or `None` if no parameters were found.  Example usage: `extract_url_params("https://example.com/page?param1=value1&param2=value2")` would return `{param1: 'value1', param2: 'value2'}`
    * `is_url(text: str) -> bool`:
        * Takes a string as input.
        * Uses the `validators.url` function to check if the input string is a valid URL.
        * Returns `True` if it's a valid URL, `False` otherwise. Example usage: `is_url("https://example.com")` returns `True`, `is_url("invalid-url")` returns `False`.

* **Variables:**
    * `MODE`: A string variable, probably for development mode or similar.  Its usage isn't immediately apparent within this function.

* **Potential Errors/Improvements:**
    * **Error Handling:** The code doesn't handle cases where `urlparse` might raise an exception (e.g., malformed URL). Adding a `try...except` block would make the function more robust.
    * **Input Validation:** While the input is checked with `is_url`, the function could benefit from more thorough input validation for the `url` argument to ensure it's not malformed.
    * **Docstrings:** While the docstrings are present, consider adding more detailed explanations of the algorithm and any potential edge cases.


**Relationships with Other Parts of the Project:**

This `url.py` file likely exists in a larger project structure. It's intended as a utility module for other modules in the project that might need URL parsing and validation.  Its relationship would be one of utility—providing services to other code. It would be used by components that need to parse URL parameters or validate URLs.