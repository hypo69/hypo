# Модуль `ensure_https`

## Обзор

Модуль `ensure_https` предназначен для проверки и добавления префикса `https://` к предоставленным URL или идентификаторам продуктов. Если на вход передается идентификатор продукта, модуль конструирует полный URL с использованием этого идентификатора и добавляет префикс `https://`.

## Подробней

Этот модуль используется для стандартизации URL, используемых в проекте `hypotez`, особенно при работе с данными, полученными от AliExpress. Он гарантирует, что все URL имеют безопасный протокол HTTPS, что важно для безопасности и надежности приложения. Функция `ensure_https` принимает строку или список строк и возвращает строку или список строк с добавленным или сохраненным префиксом `https://`.

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

**Описание**: Функция `ensure_https` проверяет, содержит ли предоставленная строка URL-адрес или идентификатор продукта префикс `https://`. Если входные данные являются идентификатором продукта, функция создает полный URL-адрес с префиксом `https://`.

**Как работает функция**:
1. Функция `ensure_https` принимает на вход либо строку `prod_ids`, представляющую собой URL или идентификатор продукта, либо список строк, содержащих URL-ы или идентификаторы продуктов.
2. Если `prod_ids` является списком, функция применяет функцию `ensure_https_single` к каждому элементу списка и возвращает новый список с обработанными URL.
3. Если `prod_ids` является строкой, функция вызывает `ensure_https_single` для обработки этой строки и возвращает результат.

**Параметры**:
- `prod_ids` (str | list[str]): URL-адрес или список URL-адресов для проверки и изменения при необходимости.

**Возвращает**:
- `str | list[str]`: URL-адрес или список URL-адресов с префиксом `https://`.

**Вызывает исключения**:
- `ValueError`: Если `prod_ids` является экземпляром `WindowsPath`.

**Примеры**:

```python
ensure_https("example_product_id")
# Результат: 'https://www.aliexpress.com/item/example_product_id.html'

ensure_https(["example_product_id1", "https://www.aliexpress.com/item/example_product_id2.html"])
# Результат: ['https://www.aliexpress.com/item/example_product_id1.html', 'https://www.aliexpress.com/item/example_product_id2.html']

ensure_https("https://www.example.com/item/example_product_id")
# Результат: 'https://www.example.com/item/example_product_id'
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
    ...
```

**Описание**: Функция `ensure_https_single` проверяет, содержит ли предоставленная строка URL-адрес или идентификатор продукта префикс `https://`. Если входные данные являются идентификатором продукта, функция создает полный URL-адрес с префиксом `https://`.

**Как работает функция**:
1. Функция `ensure_https_single` принимает на вход строку `prod_id`, представляющую собой URL или идентификатор продукта.
2. Использует функцию `extract_prod_ids` для извлечения идентификатора продукта из входной строки.
3. Если `extract_prod_ids` возвращает значение (т.е. был обнаружен идентификатор продукта), функция формирует URL-адрес на основе этого идентификатора с префиксом `https://` и возвращает его.
4. Если `extract_prod_ids` возвращает `None` (т.е. не удалось извлечь идентификатор продукта), функция логирует ошибку с помощью `logger.error` и возвращает исходную строку `prod_id`.

**Параметры**:
- `prod_id` (str): URL-адрес или идентификатор продукта.

**Возвращает**:
- `str`: URL-адрес с префиксом `https://`.

**Вызывает исключения**:
- `ValueError`: Если `prod_id` является экземпляром `WindowsPath`.

**Примеры**:

```python
ensure_https_single("example_product_id")
# Результат: 'https://www.aliexpress.com/item/example_product_id.html'

ensure_https_single("https://www.example.com/item/example_product_id")
# Результат: 'https://www.example.com/item/example_product_id'