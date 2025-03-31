# Модуль `ensure_https`

## Обзор

Модуль `ensure_https` предназначен для проверки и добавления префикса `https://` к URL или идентификаторам продуктов AliExpress. Он обеспечивает, чтобы все URL имели безопасный протокол HTTPS, и автоматически формирует полные URL для идентификаторов продуктов.

## Подробней

Модуль содержит функцию `ensure_https`, которая принимает на вход строку или список строк, представляющих собой URL или идентификаторы продуктов. Если входные данные являются идентификатором продукта, функция формирует полный URL с префиксом `https://`. Если URL уже содержит `https://`, функция оставляет его без изменений. Это необходимо для обеспечения безопасного соединения при работе с AliExpress.

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
```

**Описание**:
Обеспечивает наличие префикса `https://` в предоставленных URL или строках идентификаторов продуктов. Если входные данные являются идентификатором продукта, функция создает полный URL с префиксом `https://`.

**Параметры**:
- `prod_ids` (str | list[str]): URL-адрес или список URL-адресов для проверки и изменения при необходимости.

**Возвращает**:
- `str | list[str]`: URL-адрес или список URL-адресов с префиксом `https://`.

**Вызывает исключения**:
- `ValueError`: Если `prod_ids` является экземпляром `WindowsPath`.

**Примеры**:

```python
ensure_https("example_product_id")
# 'https://www.aliexpress.com/item/example_product_id.html'

ensure_https(["example_product_id1", "https://www.aliexpress.com/item/example_product_id2.html"])
# ['https://www.aliexpress.com/item/example_product_id1.html', 'https://www.aliexpress.com/item/example_product_id2.html']

ensure_https("https://www.example.com/item/example_product_id")
# 'https://www.example.com/item/example_product_id'
```

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
```

**Описание**:
Обеспечивает наличие префикса `https://` в отдельном URL-адресе или строке идентификатора продукта.

**Параметры**:
- `prod_id` (str): URL-адрес или строка идентификатора продукта.

**Возвращает**:
- `str`: URL-адрес с префиксом `https://`.

**Вызывает исключения**:
- `ValueError`: Если `prod_id` является экземпляром `WindowsPath`.

**Примеры**:

```python
ensure_https_single("example_product_id")
# 'https://www.aliexpress.com/item/example_product_id.html'

ensure_https_single("https://www.example.com/item/example_product_id")
# 'https://www.example.com/item/example_product_id'