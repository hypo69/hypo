# Модуль `affiliated_products_generator`

## Обзор

Модуль `affiliated_products_generator.py` содержит класс `AliAffiliatedProducts`, который отвечает за генерацию полных данных о продуктах из Aliexpress Affiliate API. Он расширяет класс `AliApi` для обработки URL-адресов или идентификаторов продуктов и получения подробной информации о партнерских продуктах, включая сохранение изображений, видео и данных JSON.

## Подробнее

Этот модуль является частью проекта `hypotez` и предназначен для автоматизации процесса получения информации о продуктах с платформы Aliexpress через Affiliate API. Он позволяет собирать полные данные о продуктах, включая изображения и видео, и сохранять их локально для дальнейшего использования в рекламных кампаниях или других целях.

## Классы

### `AliAffiliatedProducts`

**Описание**: Класс для сбора полных данных о продуктах из URL-адресов или идентификаторов продуктов.

**Методы**:
- `process_affiliate_products`: Обрабатывает список URL-адресов и возвращает список продуктов с партнерскими ссылками и сохраненными изображениями.
- `delete_product`: Удаляет продукт, у которого нет партнерской ссылки.

**Параметры**:
- `campaign_name` (str): Название рекламной кампании.
- `campaign_category` (Optional[str], optional): Категория кампании (по умолчанию `None`).
- `language` (str): Язык для кампании (по умолчанию `'EN'`).
- `currency` (str): Валюта для кампании (по умолчанию `'USD'`).

**Примеры**
```python
# Пример использования:
# prod_urls = ['123','456',...]
# prod_urls = ['https://www.aliexpress.com/item/123.html','456',...]

# parser = AliAffiliatedProducts(
#                             campaign_name,
#                             campaign_category,
#                             language,
#                             currency)

# products = parser._affiliate_product(prod_urls)
```

## Функции

### `process_affiliate_products`

```python
def process_affiliate_products(self, prod_urls: List[str]) -> List[SimpleNamespace]:
    """
    Args:
        prod_urls (List[str]): Список URL-адресов или идентификаторов продуктов.

    Returns:
        List[SimpleNamespace]: Список обработанных продуктов.
    """
```

**Описание**: Обрабатывает список URL-адресов и возвращает список продуктов с партнерскими ссылками и сохраненными изображениями.

**Параметры**:
- `prod_urls` (List[str]): Список URL-адресов или идентификаторов продуктов.

**Возвращает**:
- `List[SimpleNamespace]`: Список обработанных продуктов.

**Примеры**:
```python
# Пример вызова функции process_affiliate_products
# products = parser.process_affiliate_products(prod_urls)
```

### `delete_product`

```python
def delete_product(self, product_id: str, exc_info: bool = False):
    """ Delete a product that does not have an affiliate link"""
```

**Описание**: Удаляет продукт, у которого нет партнерской ссылки.

**Параметры**:
- `product_id` (str): Идентификатор продукта для удаления.
- `exc_info` (bool, optional): Флаг, указывающий, следует ли выводить информацию об исключении. По умолчанию `False`.