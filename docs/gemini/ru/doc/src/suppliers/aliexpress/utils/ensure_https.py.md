# Модуль для обеспечения HTTPS

## Обзор

Модуль `ensure_https.py` предназначен для проверки и добавления префикса `https://` к строкам URL. Если входные данные являются идентификатором продукта, он строит полный URL с префиксом `https://`.

## Подробнее

Этот модуль гарантирует, что все URL, используемые в проекте, используют безопасный протокол HTTPS. Он принимает строку URL или список URL, проверяет, начинается ли URL с `https://`, и добавляет его, если это не так. Если предоставлен идентификатор продукта, он создает полный URL AliExpress с этим идентификатором.

## Функции

### `ensure_https`

```python
def ensure_https(prod_ids: str | list[str]) -> str | list[str]:
    """ Ensures that the provided URL string(s) contain the https:// prefix.
    If the input is a product ID, it constructs a full URL with https:// prefix.

    Args:
        prod_ids (str | list[str]): A URL string or a list of URL strings to check and modify if necessary.

    Returns:
        str | list[str]: The URL string or list of URL strings with the https:// prefix.

    Raises:
        ValueError: If `prod_ids` is an instance of `WindowsPath`.

    Examples:
        >>> ensure_https("example_product_id")
        'https://www.aliexpress.com/item/example_product_id.html'

        >>> ensure_https(["example_product_id1", "https://www.aliexpress.com/item/example_product_id2.html"])
        ['https://www.aliexpress.com/item/example_product_id1.html', 'https://www.aliexpress.com/item/example_product_id2.html']

        >>> ensure_https("https://www.example.com/item/example_product_id")
        'https://www.example.com/item/example_product_id'
    """
    ...
```

**Назначение**: Обеспечивает наличие префикса `https://` в предоставленной строке URL или списке URL. Если входные данные являются идентификатором продукта, функция создает полный URL-адрес с префиксом `https://`.

**Параметры**:

- `prod_ids` (str | list[str]): Строка URL или список строк URL для проверки и изменения при необходимости.

**Возвращает**:

- `str | list[str]`: Строка URL или список строк URL с префиксом `https://`.

**Вызывает исключения**:

- `ValueError`: Если `prod_ids` является экземпляром `WindowsPath`.

**Как работает функция**:

1. Функция `ensure_https` принимает на вход `prod_ids`, который может быть строкой или списком строк.
2. Если `prod_ids` является списком, функция применяет функцию `ensure_https_single` к каждому элементу списка и возвращает новый список с обработанными URL.
3. Если `prod_ids` является строкой, функция вызывает `ensure_https_single` для обработки этой строки и возвращает результат.

**Внутренние функции**:

### `ensure_https_single`

```python
 def ensure_https_single(prod_id: str) -> str:
        """ Ensures a single URL or product ID string has the https:// prefix.

        Args:
            prod_id (str): The URL or product ID string.

        Returns:
            str: The URL string with the https:// prefix.

        Raises:
            ValueError: If `prod_id` is an instance of `WindowsPath`.

        Examples:
            >>> ensure_https_single("example_product_id")
            'https://www.aliexpress.com/item/example_product_id.html'

            >>> ensure_https_single("https://www.example.com/item/example_product_id")
            'https://www.example.com/item/example_product_id'
        """
        ...
```

**Назначение**: Обеспечивает наличие префикса `https://` в одной строке URL или идентификаторе продукта.

**Параметры**:

- `prod_id` (str): Строка URL или идентификатор продукта.

**Возвращает**:

- `str`: Строка URL с префиксом `https://`.

**Вызывает исключения**:

- `ValueError`: Если `prod_id` является экземпляром `WindowsPath`.

**Как работает функция**:

1. Функция `ensure_https_single` принимает на вход `prod_id` - строку, представляющую URL или ID продукта.
2. Извлекает ID продукта из `prod_id` с помощью функции `extract_prod_ids`.
3. Если `_prod_id` не пустой, возвращает URL-адрес, отформатированный как `https://www.aliexpress.com/item/{_prod_id}.html`.
4. Если `_prod_id` пустой (то есть, `extract_prod_ids` вернул `None`), записывает сообщение об ошибке в лог с помощью `logger.error` и возвращает исходный `prod_id` без изменений.

**Примеры**:

```python
>>> ensure_https("example_product_id")
'https://www.aliexpress.com/item/example_product_id.html'

>>> ensure_https(["example_product_id1", "https://www.aliexpress.com/item/example_product_id2.html"])
['https://www.aliexpress.com/item/example_product_id1.html', 'https://www.aliexpress.com/item/example_product_id2.html']

>>> ensure_https("https://www.example.com/item/example_product_id")
'https://www.example.com/item/example_product_id'
```

**ASCII Flowchart функции `ensure_https`**:

```
     A [Входные данные: prod_ids (str | list[str])]
     |
     B [Проверка типа prod_ids: список?]
     |
     No --> C [Вызов ensure_https_single(prod_ids)]
     |
     Yes --> D [Применение ensure_https_single к каждому элементу списка]
     |
     E [Возврат обработанного списка URL]
     |
     F [Выход]
```

Где:

- `A`: Начало функции с входными данными `prod_ids`.
- `B`: Проверка, является ли `prod_ids` списком.
- `C`: Если `prod_ids` не является списком, вызывается `ensure_https_single` с `prod_ids` в качестве аргумента.
- `D`: Если `prod_ids` является списком, `ensure_https_single` применяется к каждому элементу списка.
- `E`: Возвращается обработанный список URL.
- `F`: Конец функции.

**ASCII Flowchart функции `ensure_https_single`**:

```
A [Входные данные: prod_id (str)]
     |
     B [Извлечение ID продукта: _prod_id = extract_prod_ids(prod_id)]
     |
     C [Проверка: _prod_id не пустой?]
     |
     Yes --> D [Формирование URL: https://www.aliexpress.com/item/{_prod_id}.html]
     |
     No --> E [Логирование ошибки: logger.error(...)]
     |
     F [Возврат prod_id (без изменений)]
     |
     G [Выход]
```

Где:

- `A`: Начало функции с входными данными `prod_id`.
- `B`: Извлечение ID продукта с использованием `extract_prod_ids(prod_id)`.
- `C`: Проверка, не является ли `_prod_id` пустым.
- `D`: Если `_prod_id` не пустой, формируется URL-адрес с использованием ID продукта.
- `E`: Если `_prod_id` пустой, логируется сообщение об ошибке.
- `F`: Возвращается исходный `prod_id` без изменений.
- `G`: Конец функции.