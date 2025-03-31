# Модуль `affiliated_products_generator`

## Обзор

Модуль `affiliated_products_generator.py` содержит класс `AliAffiliatedProducts`, который предназначен для генерации полных данных о товарах из Aliexpress Affiliate API. Он расширяет класс `AliApi` для обработки URL или идентификаторов продуктов и извлечения деталей об партнерских продуктах, включая сохранение изображений, видео и данных JSON.

## Подробней

Этот модуль является частью проекта `hypotez` и используется для сбора и обработки данных о товарах с AliExpress с целью создания рекламных кампаний. Он автоматизирует процесс получения информации о товарах, загрузки медиафайлов и сохранения данных в структурированном формате. Расположение файла в директории `src/suppliers/aliexpress/_docs/` указывает на его роль в системе поставщиков AliExpress и генерации соответствующей документации.

## Классы

### `AliAffiliatedProducts`

**Описание**: Класс для сбора полных данных о товарах из URL-адресов или идентификаторов продуктов, используя Aliexpress Affiliate API.

**Как работает класс**:
- Класс наследуется от `AliApi` и использует его функциональность для взаимодействия с API Aliexpress.
- При инициализации класса задаются параметры рекламной кампании, такие как имя, категория, язык и валюта.
- Метод `process_affiliate_products` обрабатывает список URL-адресов продуктов, получает партнерские ссылки, скачивает изображения и видео, и сохраняет детали продукта в формате JSON.
- Класс также включает методы для удаления продуктов, у которых нет партнерской ссылки.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `AliAffiliatedProducts`.
- `process_affiliate_products`: Обрабатывает список URL-адресов продуктов для получения партнерских ссылок и деталей продуктов.
- `delete_product`: Удаляет продукт, у которого нет партнерской ссылки.

**Параметры**:
- `campaign_name` (str): Имя рекламной кампании.
- `campaign_category` (Optional[str]): Категория для кампании (по умолчанию `None`).
- `language` (str): Язык для кампании (по умолчанию `'EN'`).
- `currency` (str): Валюта для кампании (по умолчанию `'USD'`).

**Примеры**
```python
# Пример использования класса AliAffiliatedProducts
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

# Создание экземпляра класса
parser = AliAffiliatedProducts(
    campaign_name='test_campaign',
    campaign_category='electronics',
    language='RU',
    currency='RUB'
)

# Список URL-адресов продуктов
product_urls = [
    'https://www.aliexpress.com/item/1234567890.html',
    'https://www.aliexpress.com/item/0987654321.html'
]

# Обработка продуктов
products = parser.process_affiliate_products(product_urls)

# Вывод информации о продуктах
if products:
    for product in products:
        print(f'Product ID: {product.product_id}')
        print(f'Promotion Link: {product.promotion_link}')
        print(f'Local Image Path: {product.local_image_path}')
else:
    print('No affiliate products found.')
```

## Функции

### `process_affiliate_products`

```python
def process_affiliate_products(self, prod_urls: List[str]) -> List[SimpleNamespace]:
    """
    Processes a list of URLs and returns a list of products with affiliate links and saved images.

    :param prod_urls: List of product URLs or IDs.
    :return: List of processed products.
    """
    ...
```

**Описание**: Обрабатывает список URL-адресов продуктов для получения партнерских ссылок, сохранения изображений и деталей продуктов.

**Как работает функция**:
1. Принимает список URL-адресов продуктов или их идентификаторов.
2. Получает партнерские ссылки для каждого продукта, используя метод `get_affiliate_links` из родительского класса `AliApi`.
3. Извлекает детали продукта с использованием метода `retrieve_product_details`.
4. Сохраняет изображения и видео продукта локально, используя функции `save_png_from_url` и `save_video_from_url`.
5. Сохраняет информацию о продукте в формате JSON.
6. Возвращает список объектов `SimpleNamespace`, представляющих обработанные продукты.

**Параметры**:
- `prod_urls` (List[str]): Список URL-адресов продуктов или их идентификаторов.

**Возвращает**:
- `List[SimpleNamespace]`: Список объектов `SimpleNamespace`, представляющих обработанные продукты.

**Примеры**:

```python
# Пример вызова функции process_affiliate_products
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

# Создание экземпляра класса
parser = AliAffiliatedProducts(
    campaign_name='test_campaign',
    campaign_category='electronics',
    language='RU',
    currency='RUB'
)

# Список URL-адресов продуктов
product_urls = [
    'https://www.aliexpress.com/item/1234567890.html',
    'https://www.aliexpress.com/item/0987654321.html'
]

# Обработка продуктов
products = parser.process_affiliate_products(product_urls)

# Вывод информации о продуктах
if products:
    for product in products:
        print(f'Product ID: {product.product_id}')
        print(f'Promotion Link: {product.promotion_link}')
        print(f'Local Image Path: {product.local_image_path}')
else:
    print('No affiliate products found.')
```

### `delete_product`

```python
def delete_product(self, product_id: str, exc_info: bool = False):
    """ Delete a product that does not have an affiliate link"""
    ...
```

**Описание**: Удаляет продукт, у которого нет партнерской ссылки.

**Как работает функция**:
1. Принимает идентификатор продукта.
2. Извлекает идентификатор продукта с использованием функции `extract_prod_ids`.
3. Удаляет запись о продукте из файла `sources.txt` и переименовывает файл продукта, если он существует.
4. Логирует успешное удаление или возникшие ошибки.

**Параметры**:
- `product_id` (str): Идентификатор продукта для удаления.
- `exc_info` (bool): Флаг, указывающий, нужно ли логировать информацию об исключении (по умолчанию `False`).

**Вызывает исключения**:
- `FileNotFoundError`: Если файл продукта не найден.
- `Exception`: Если произошла ошибка при удалении файла продукта.

**Примеры**:

```python
# Пример вызова функции delete_product
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

# Создание экземпляра класса
parser = AliAffiliatedProducts(
    campaign_name='test_campaign',
    campaign_category='electronics',
    language='RU',
    currency='RUB'
)

# Идентификатор продукта для удаления
product_id = '1234567890'

# Удаление продукта
parser.delete_product(product_id)