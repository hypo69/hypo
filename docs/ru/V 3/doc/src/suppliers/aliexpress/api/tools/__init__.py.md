# Модуль `src.suppliers.aliexpress.api.tools`

## Обзор

Модуль `src.suppliers.aliexpress.api.tools` содержит набор инструментов, используемых для взаимодействия с API AliExpress. В текущей версии он предоставляет функцию `get_product_id` для извлечения ID продукта из URL.

## Подробней

Этот модуль служит для упрощения работы с API AliExpress, предоставляя удобные функции для выполнения типичных задач, таких как извлечение идентификатора продукта. В частности, функция `get_product_id` позволяет получить ID товара из URL, что может быть полезно при автоматизации сбора данных о товарах.

## Функции

### `get_product_id`

```python
def get_product_id(url: str) -> str | None:
    """
    Извлекает ID продукта из URL AliExpress.

    Args:
        url (str): URL товара на AliExpress.

    Returns:
        str | None: ID продукта или None, если ID не найден.

    Raises:
        None

    Example:
        >>> get_product_id('https://www.aliexpress.com/item/1234567890.html')
        '1234567890'
        >>> get_product_id('https://aliexpress.ru/item/1234567890.html')
        '1234567890'
        >>> get_product_id('https://m.aliexpress.com/item/1234567890.html')
        '1234567890'
        >>> get_product_id('https://www.aliexpress.com/item/1005004997441909.html?spm=a2g2w.productlist.search.1.2aef4aa6dLmvwL')
        '1005004997441909'
    """
    ...
```

**Описание**: Извлекает ID продукта из предоставленного URL-адреса AliExpress.

**Параметры**:
- `url` (str): URL товара на AliExpress.

**Возвращает**:
- `str | None`: ID продукта в виде строки или `None`, если ID не найден.

**Вызывает исключения**:
- Отсутствуют.

**Примеры**:
```python
>>> get_product_id('https://www.aliexpress.com/item/1234567890.html')
'1234567890'
>>> get_product_id('https://aliexpress.ru/item/1234567890.html')
'1234567890'
>>> get_product_id('https://m.aliexpress.com/item/1234567890.html')
'1234567890'
>>> get_product_id('https://www.aliexpress.com/item/1005004997441909.html?spm=a2g2w.productlist.search.1.2aef4aa6dLmvwL')
'1005004997441909'