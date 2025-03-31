# Модуль extract_product_id

## Обзор

Модуль `extract_product_id` предназначен для извлечения идентификаторов товаров (product IDs) из URL-адресов, полученных с сайта AliExpress. Он также может проверять, является ли предоставленная строка уже идентификатором товара.

## Подорбней

Этот модуль предоставляет функцию `extract_prod_ids`, которая принимает на вход URL-адрес или список URL-адресов и извлекает из них идентификаторы товаров. Он использует регулярные выражения для поиска и извлечения этих идентификаторов. Если передан список URL-адресов, функция возвращает список извлеченных идентификаторов. Если передан один URL-адрес, функция возвращает один идентификатор. Если ни один идентификатор не найден, функция возвращает `None`.
Этот модуль важен для задач, связанных с парсингом данных с AliExpress, где требуется извлекать и обрабатывать идентификаторы товаров. Расположение файла `/src/suppliers/aliexpress/utils/extract_product_id.py` указывает на то, что данный модуль является частью системы обработки данных от поставщиков, в частности, от AliExpress.

## Функции

### `extract_prod_ids`

```python
def extract_prod_ids(urls: str | list[str]) -> str | list[str] | None:
    """ Extracts item IDs from a list of URLs or directly returns IDs if given.

    Args:
        urls (str | list[str]): A URL, a list of URLs, or product IDs.

    Returns:
        str | list[str] | None: A list of extracted item IDs, a single ID, or `None` if no valid ID is found.

    Examples:
        >>> extract_prod_ids("https://www.aliexpress.com/item/123456.html")
        '123456'

        >>> extract_prod_ids(["https://www.aliexpress.com/item/123456.html", "7891011.html"])
        ['123456', '7891011']

        >>> extract_prod_ids(["https://www.example.com/item/123456.html", "https://www.example.com/item/abcdef.html"])
        ['123456']

        >>> extract_prod_ids("7891011")
        '7891011'

        >>> extract_prod_ids("https://www.example.com/item/abcdef.html")
        None
    """
    # Regular expression to find product identifiers
    pattern = re.compile(r"(?:item/|/)?(\\d+)\\.html")

    def extract_id(url: str) -> str | None:
        """ Extracts a product ID from a given URL or validates a product ID.

        Args:
            url (str): The URL or product ID.

        Returns:
            str | None: The extracted product ID or the input itself if it's a valid ID, or `None` if no valid ID is found.

        Examples:
            >>> extract_id("https://www.aliexpress.com/item/123456.html")
            '123456'

            >>> extract_id("7891011")
            '7891011'

            >>> extract_id("https://www.example.com/item/abcdef.html")
            None
        """
        # Check if the input is a valid product ID
        if url.isdigit():
            return url

        # Otherwise, try to extract the ID from the URL
        match = pattern.search(url)
        if match:
            return match.group(1)
        return

    if isinstance(urls, list):
        extracted_ids = [extract_id(url) for url in urls if extract_id(url) is not None]
        return extracted_ids if extracted_ids else None
    else:
        return extract_id(urls)
```

**Описание**: Извлекает идентификаторы товаров из списка URL-адресов или возвращает идентификаторы, если они уже предоставлены.

**Параметры**:
- `urls` (str | list[str]): URL-адрес, список URL-адресов или идентификаторы продуктов.

**Возвращает**:
- `str | list[str] | None`: Список извлеченных идентификаторов товаров, один идентификатор или `None`, если не найдено ни одного допустимого идентификатора.

**Примеры**:
```python
>>> extract_prod_ids("https://www.aliexpress.com/item/123456.html")
'123456'

>>> extract_prod_ids(["https://www.aliexpress.com/item/123456.html", "7891011.html"])
['123456', '7891011']

>>> extract_prod_ids(["https://www.example.com/item/123456.html", "https://www.example.com/item/abcdef.html"])
['123456']

>>> extract_prod_ids("7891011")
'7891011'

>>> extract_prod_ids("https://www.example.com/item/abcdef.html")
None