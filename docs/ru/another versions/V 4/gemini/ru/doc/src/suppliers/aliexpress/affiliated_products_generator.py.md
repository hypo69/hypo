# Модуль `affiliated_products_generator.py`

## Обзор

Модуль `affiliated_products_generator.py` предназначен для работы с партнерскими продуктами AliExpress. Он предоставляет функциональность для сбора данных о продуктах по предоставленным URL или идентификаторам продуктов, получения партнерских ссылок, сохранения изображений и видео, а также генерации данных для рекламных кампаний.

## Подробней

Этот модуль является частью системы для управления рекламными кампаниями AliExpress. Он автоматизирует процесс получения информации о продуктах, создания партнерских ссылок и подготовки медиа-контента для использования в рекламных материалах. Модуль использует API AliExpress для получения данных о продуктах и включает инструменты для сохранения изображений и видео, а также для форматирования данных в удобном для дальнейшей обработки виде.

## Классы

### `AliAffiliatedProducts`

**Описание**:
Класс `AliAffiliatedProducts` предназначен для сбора полных данных о продуктах из URL-адресов или идентификаторов продуктов. Он наследуется от класса `AliApi` и расширяет его функциональность, добавляя возможность обработки партнерских ссылок и сохранения медиа-контента.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliAffiliatedProducts`.
- `process_affiliate_products`: Обрабатывает список идентификаторов продуктов или URL-адресов и возвращает список продуктов с партнерскими ссылками и сохраненными изображениями.

**Параметры**:
- `language` (str): Язык для рекламной кампании (по умолчанию 'EN').
- `currency` (str): Валюта для рекламной кампании (по умолчанию 'USD').

**Примеры**:

```python
# Пример инициализации класса AliAffiliatedProducts
affiliated_products = AliAffiliatedProducts(language='RU', currency='RUB')

# Пример использования метода process_affiliate_products
# prod_ids = ["http://example.com/product1", "http://example.com/product2"]
# category_root = "path/to/category"
# products = await affiliated_products.process_affiliate_products(prod_ids, category_root)
# for product in products:
#     print(product.product_title)
```

## Функции

### `process_affiliate_products`

```python
async def process_affiliate_products(self, prod_ids: list[str], category_root: Path | str) -> list[SimpleNamespace]:
    """
    Processes a list of product IDs or URLs and returns a list of products with affiliate links and saved images.

    Args:
        prod_ids (list[str]): List of product URLs or IDs.
        category_root (Path | str): The root directory for the category to process.

    Returns:
        list[SimpleNamespace]: A list of processed products with affiliate links and saved images.

    Raises:
        Exception: If the category name is not found in the campaign.

    Example:
        >>> from pathlib import Path
        >>> import asyncio
        >>> from types import SimpleNamespace
        >>> from unittest.mock import AsyncMock
        >>>
        >>> # Mocking dependencies for the example
        >>> class MockAliAffiliatedProducts:
        ...     def __init__(self, language: str = 'EN', currency: str = 'USD'):
        ...         self.language = language
        ...         self.currency = currency
        ...     async def process_affiliate_products(self, prod_ids: list[str], category_root: Path | str) -> list[SimpleNamespace]:
        ...         # Dummy implementation for demonstration
        ...         products = []
        ...         for i, prod_id in enumerate(prod_ids):
        ...             product = SimpleNamespace(
        ...                 product_id=str(i),
        ...                 product_title=f"Product {i} Title",
        ...                 product_main_image_url=f"http://example.com/image{i}.jpg",
        ...                 product_video_url="",
        ...                 language=self.language,
        ...                 promotion_link=f"http://example.com/affiliate_link{i}"
        ...             )
        ...             products.append(product)
        ...         return products
        >>>
        >>> # Example Usage
        >>> async def main():
        ...     mock_instance = MockAliAffiliatedProducts(language='RU', currency='RUB')
        ...     prod_ids = ["http://example.com/product1", "http://example.com/product2"]
        ...     category_root = Path("/tmp/category")
        ...     products = await mock_instance.process_affiliate_products(prod_ids, category_root)
        ...     for product in products:
        ...         print(f"Title: {product.product_title}, Affiliate Link: {product.promotion_link}")
        ...
        >>> asyncio.run(main())
        Title: Product 0 Title, Affiliate Link: http://example.com/affiliate_link0
        Title: Product 1 Title, Affiliate Link: http://example.com/affiliate_link1
    """
```

**Описание**:
Обрабатывает список идентификаторов продуктов или URL-адресов, получает партнерские ссылки, сохраняет изображения и видео, и возвращает список объектов `SimpleNamespace` с информацией о продуктах.

**Параметры**:
- `prod_ids` (list[str]): Список URL-адресов или идентификаторов продуктов.
- `category_root` (Path | str): Корневой каталог для сохранения изображений и видео.

**Возвращает**:
- `list[SimpleNamespace]`: Список обработанных продуктов с партнерскими ссылками и сохраненными изображениями.

**Вызывает исключения**:
- `Exception`: Если имя категории не найдено в кампании.

**Примеры**:

```python
# Пример использования функции process_affiliate_products
# prod_ids = ["http://example.com/product1", "http://example.com/product2"]
# category_root = "path/to/category"
# products = await affiliated_products.process_affiliate_products(prod_ids, category_root)
# for product in products:
#     print(product.product_title)
```