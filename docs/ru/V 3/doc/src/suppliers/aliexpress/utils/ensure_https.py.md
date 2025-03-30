# Модуль `ensure_https`

## Обзор

Модуль `ensure_https` предназначен для обеспечения наличия префикса `https://` в предоставленных URL-адресах. Если входные данные являются идентификатором продукта, он строит полный URL с префиксом `https://`.

## Подробней

Этот модуль предоставляет функциональность для принудительного использования HTTPS-соединения при работе с URL-ами, особенно с идентификаторами товаров AliExpress. Он проверяет, начинается ли URL с `https://`, и если нет, добавляет этот префикс. В случае, если предоставлен только идентификатор товара, модуль формирует полный URL, используя домен AliExpress. Это гарантирует, что все запросы будут выполняться через безопасное соединение.

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
Обеспечивает наличие префикса `https://` в предоставленной строке URL или списке URL. Если входные данные являются идентификатором продукта, он строит полный URL с префиксом `https://`.

**Параметры**:
- `prod_ids` (str | list[str]): Строка URL или список строк URL для проверки и изменения, если это необходимо.

**Возвращает**:
- `str | list[str]`: Строка URL или список строк URL с префиксом `https://`.

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
Обеспечивает, чтобы одиночная строка URL или идентификатор продукта имели префикс `https://`.

**Параметры**:
- `prod_id` (str): Строка URL или идентификатор продукта.

**Возвращает**:
- `str`: Строка URL с префиксом `https://`.

**Вызывает исключения**:
- `ValueError`: Если `prod_id` является экземпляром `WindowsPath`.

**Примеры**:

```python
ensure_https_single("example_product_id")
# 'https://www.aliexpress.com/item/example_product_id.html'

ensure_https_single("https://www.example.com/item/example_product_id")
# 'https://www.example.com/item/example_product_id'