# Модуль `ensure_https`

## Обзор

Модуль `ensure_https` предназначен для работы с URL, относящимися к площадке AliExpress. Его основная задача - гарантировать, что предоставленные URL-адреса содержат префикс `https://`. Если входные данные представляют собой ID товара, модуль формирует полноценный URL с использованием этого ID и префикса `https://`.

## Подробнее

Модуль содержит функцию `ensure_https`, которая принимает на вход строку или список строк (URL или ID товаров) и возвращает строку или список строк, где все URL гарантированно начинаются с `https://`. В случае, если передан ID товара, функция формирует полный URL для AliExpress с использованием этого ID.

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
        _prod_id = extract_prod_ids(prod_id)
        if _prod_id:
            return f"https://www.aliexpress.com/item/{_prod_id}.html"
        else:
            logger.error(f"Invalid product ID or URL: {prod_id=}", exc_info=False)
            return prod_id

    if isinstance(prod_ids, list):
        return [ensure_https_single(prod_id) for prod_id in prod_ids]
    else:
        return ensure_https_single(prod_ids)
```

**Назначение**: Гарантирует, что предоставленные URL-адреса содержат префикс `https://`. Если входные данные являются ID товара, формирует полный URL с префиксом `https://`.

**Параметры**:
- `prod_ids` (str | list[str]): URL или список URL-адресов для проверки и изменения, если это необходимо.

**Возвращает**:
- `str | list[str]`: URL или список URL-адресов с префиксом `https://`.

**Вызывает исключения**:
- `ValueError`: Если `prod_ids` является экземпляром `WindowsPath`.

**Как работает функция**:

1. Функция `ensure_https` принимает на вход параметр `prod_ids`, который может быть строкой или списком строк.
2. Проверяется, является ли `prod_ids` списком.
3. Если `prod_ids` является списком, функция применяет функцию `ensure_https_single` к каждому элементу списка и возвращает новый список с обработанными URL.
4. Если `prod_ids` не является списком, функция вызывает `ensure_https_single` для обработки единственной строки и возвращает результат.

#### Внутренние функции:

##### `ensure_https_single`

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
            _prod_id = extract_prod_ids(prod_id)
            if _prod_id:
                return f"https://www.aliexpress.com/item/{_prod_id}.html"
            else:
                logger.error(f"Invalid product ID or URL: {prod_id=}", exc_info=False)
                return prod_id
```

**Назначение**: Гарантирует, что предоставленная строка URL или ID товара имеет префикс `https://`.

**Параметры**:
- `prod_id` (str): URL или ID товара.

**Возвращает**:
- `str`: URL с префиксом `https://`.

**Вызывает исключения**:
- `ValueError`: Если `prod_id` является экземпляром `WindowsPath`.

**Как работает функция**:

1. Функция `ensure_https_single` принимает на вход параметр `prod_id`, который является строкой, представляющей URL или ID товара.
2. Извлекает ID продукта с помощью функции `extract_prod_ids(prod_id)`.
3. Если `_prod_id` существует (т.е. был успешно извлечен ID продукта), функция возвращает полный URL, используя ID продукта и префикс `https://www.aliexpress.com/item/{_prod_id}.html`.
4. Если `_prod_id` не существует (т.е. не удалось извлечь ID продукта), функция регистрирует ошибку с помощью `logger.error` и возвращает исходный `prod_id` без изменений.

**Примеры**:

```
A (Получение prod_ids)
|
B (Является ли prod_ids списком?)
|
├── Нет: C (Вызов ensure_https_single(prod_ids))
|   |
|   └── D (Завершение)
|
└── Да: E (Применение ensure_https_single к каждому элементу списка)
    |
    └── F (Завершение)
```

**Примеры**:

```python
# Пример 1: Передача ID товара
result = ensure_https("1234567890")
print(result)  # Вывод: https://www.aliexpress.com/item/1234567890.html

# Пример 2: Передача URL с http
result = ensure_https("http://www.aliexpress.com/item/1234567890.html")
print(result)  # Вывод: https://www.aliexpress.com/item/1234567890.html

# Пример 3: Передача URL с https
result = ensure_https("https://www.aliexpress.com/item/1234567890.html")
print(result)  # Вывод: https://www.aliexpress.com/item/1234567890.html

# Пример 4: Передача списка ID товаров и URL
result = ensure_https(["1234567890", "https://www.aliexpress.com/item/0987654321.html"])
print(result)  # Вывод: ['https://www.aliexpress.com/item/1234567890.html', 'https://www.aliexpress.com/item/0987654321.html']
```