# Модуль `affiliated_products_generator`

## Обзор

Модуль `affiliated_products_generator.py` содержит класс `AliAffiliatedProducts`. Этот класс предназначен для генерации полных данных о продуктах из Aliexpress Affiliate API. Он основан на классе `AliApi` для обработки URL-адресов или идентификаторов продуктов и получения подробной информации о партнерских продуктах, включая сохранение изображений, видео и данных в формате JSON.

## Содержание

- [Импорты и зависимости](#импорты-и-зависимости)
- [Класс `AliAffiliatedProducts`](#класс-aliaffiliatedproducts)
    - [Описание класса](#описание-класса)
    - [Атрибуты](#атрибуты)
    - [Инициализация](#инициализация)
    - [Методы](#методы)
        - [`process_affiliate_products`](#process_affiliate_products)
        - [`delete_product`](#delete_product)

## Импорты и зависимости

```python
import asyncio
from itertools import count
from math import log
from pathlib import Path
from typing import List, Union, Optional
from types import SimpleNamespace
from urllib.parse import urlparse, parse_qs

from src import gs
from src.suppliers.aliexpress import AliApi
from src.suppliers.aliexpress import Aliexpress
from src.suppliers.aliexpress.affiliate_links_shortener_via_webdriver import AffiliateLinksShortener
from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids
from src.suppliers.aliexpress.utils.set_full_https import ensure_https
from src.utils.convertor.csv2json import csv2dict 
from src.utils.jjson import j_dumps
from src.utils import save_png_from_url, save_video_from_url
from src.utils.printer import pprint 
from src.utils.file import read_text_file, save_text_file

from src.logger.logger import logger
```

- **Стандартные библиотеки:** `asyncio`, `itertools`, `math`, `pathlib`, `typing`, `types`, `urllib.parse`
- **Внешние библиотеки:** `src.settings`, `src.suppliers.aliexpress`, `src.utils.convertor`, `src.utils`, `src.logger`

## Класс `AliAffiliatedProducts`

### Описание класса

```python
class AliAffiliatedProducts(AliApi):
    """ Class to collect full product data from URLs or product IDs
    locator_description For more details on how to create templates for ad campaigns, see the section `Managing Aliexpress Ad Campaigns`
    @code
    # Example usage:
    prod_urls = ['123','456',...]
    prod_urls = ['https://www.aliexpress.com/item/123.html','456',...]

    parser = AliAffiliatedProducts(
                                campaign_name,
                                campaign_category,
                                language,
                                currency)

    products = parser._affiliate_product(prod_urls)
    @endcode
    """
```

**Назначение:** Сбор полных данных о продуктах из URL-адресов или идентификаторов продуктов с использованием Aliexpress Affiliate API.

**Пример использования:** Показывает, как инициализировать класс и вызвать метод `_affiliate_product` для обработки URL-адресов продуктов.

### Атрибуты

```python
campaign_name: str
campaign_category: Optional[str]
campaign_path: Path
language: str
currency: str
```

- **`campaign_name`**: Имя рекламной кампании.
- **`campaign_category`**: Категория для кампании (по умолчанию `None`).
- **`campaign_path`**: Путь к каталогу, где хранятся материалы кампании.
- **`language`**: Язык для кампании (по умолчанию `'EN'`).
- **`currency`**: Валюта для кампании (по умолчанию `'USD'`).

### Инициализация

```python
def __init__(self,
             campaign_name: str,
             campaign_category: Optional[str] = None,
             language: str = 'EN',
             currency: str = 'USD',
             *args, **kwargs):
    """
    @param campaign_name `str`: Name of the advertising campaign. The directory with the prepared material is taken by name.
    @param campaign_category `Optional[str]`: Category for the campaign (default None).
    @param language `str`: Language for the campaign (default 'EN').
    @param currency `str`: Currency for the campaign (default 'USD').
    @param tracking_id `str`: Tracking ID for Aliexpress API.
    """
    super().__init__(language, currency)

    self.campaign_name = campaign_name
    self.campaign_category = campaign_category
    self.language = language
    self.currency = currency
    self.locale = f"{self.language}_{self.currency}"
    self.campaign_path = gs.path.google_drive / 'aliexpress' / 'campaigns' / self.campaign_name / 'categories' / self.campaign_category
```

- **`super().__init__(language, currency)`**: Вызывает конструктор родительского класса `AliApi`.
- **`self.campaign_path`**: Создает путь к каталогу кампании на основе `campaign_name` и `campaign_category`.

### Методы

#### `process_affiliate_products`

```python
def process_affiliate_products(self, prod_urls: List[str]) -> List[SimpleNamespace]:
    """
    Processes a list of URLs and returns a list of products with affiliate links and saved images.

    :param prod_urls: List of product URLs or IDs.
    :return: List of processed products.
    """
    ...
    _promotion_links: list = []
    _prod_urls: list = []
    promotional_prod_urls = ensure_https(prod_urls)
    print_flag = 'new_line'
    for prod_url in promotional_prod_urls:
        _link = super().get_affiliate_links(prod_url)
        if _link:
            _link = _link[0]    
        if hasattr(_link, 'promotion_link'):
            _promotion_links.append(_link.promotion_link)
            _prod_urls.append(prod_url)
            
            pprint(f'found affiliate for: {_link.promotion_link}', end=print_flag)
            print_flag = 'inline'
        else:
            logger.info_red(f'Not found affiliate for {prod_url}')
    
    if not _promotion_links:
        logger.error('No affiliate products returned')
        return
    logger.info_red('Start receiving product details...')
    _affiliate_products: SimpleNamespace = self.retrieve_product_details(_prod_urls)
    if not _affiliate_products:
        return 
    
    print_flag = 'new_line'
    for product, promotion_link in zip(_affiliate_products, _promotion_links):
        ...

        if not promotion_link:
            parsed_url = urlparse(product.promotion_link)
            query_params = parse_qs(parsed_url.query)
            aff_short_key = query_params.get('aff_short_key', [None])[0]
            if aff_short_key:
                product.promotion_link = fr'https://s.click.aliexpress.com/e/{aff_short_key}'
            else:
                """ This product is not an affiliate"""
                self.delete_product(product.product_id)
                ...
        else:
            product.promotion_link = promotion_link
        
        image_path = self.campaign_path / 'images' / f"{product.product_id}.png"
        save_png_from_url(product.product_main_image_url, image_path, exc_info=False)
        product.local_saved_image = str(image_path)
        if len(product.product_video_url) > 1:
            parsed_url = urlparse(product.product_video_url)
            suffix = Path(parsed_url.path).suffix
            
            video_path = self.campaign_path / 'videos' / f'{product.product_id}.{suffix}'
            save_video_from_url(product.product_video_url, video_path, exc_info=False)
            product.local_saved_video = str(video_path)

        pprint(f'caught product - {product.product_id}', end=print_flag)
        print_flag = 'inline'
        
        if not j_dumps(product, self.campaign_path / self.locale / f"{product.product_id}.json", exc_info=False):
            logger.warning(f"""Failed to write dictionary: \\n {pprint(product)} \\n path: {self.campaign_path / self.locale / product.product_id}.json""", exc_info=False)
            ...
            continue
            
    pprint(f'caught {len(_affiliate_products)}', end='new_line')
    return _affiliate_products
```

**Описание**: Обрабатывает список URL-адресов или идентификаторов продуктов для получения партнерских ссылок, сохранения изображений и видео, а также хранения деталей продукта.

**Параметры**:
- `prod_urls` (List[str]): Список URL-адресов или идентификаторов продуктов.

**Возвращает**:
- `List[SimpleNamespace]`: Список объектов `SimpleNamespace`, представляющих обработанные продукты.

#### `delete_product`

```python
def delete_product(self, product_id: str, exc_info: bool = False):
    """ Delete a product that does not have an affiliate link"""
    ...
    _product_id = extract_prod_ids(product_id)
    
    product_path = self.campaign_path / 'sources.txt'
    prepared_product_path = self.campaign_path / '_sources.txt'
    products_list = read_text_file(product_path)
    if products_list:
        products_list = convert_list_to_homogeneous_list(products_list)
        for record in products_list:
            if _product_id:
                record_id = extract_prod_ids(record)
                if record_id == str(product_id):
                    products_list.remove(record)
                    save_text_file(list2string(products_list, '\n'), prepared_product_path)
                    break
            else:
                if record == str(product_id):
                    products_list.remove(record)
                    save_text_file(list2string(products_list, '\n'), product_path)
            
    else:
        product_path = self.campaign_path / 'sources' / f'{product_id}.html'    
        try:
            product_path.rename(self.campaign_path / 'sources' / f'{product_id}_.html')
            # product_path.unlink()
            logger.success(f"Product file {product_path} renamed successfully.")
        except FileNotFoundError as ex:
            logger.error(f"Product file {product_path} not found.", exc_info=exc_info)
        except Exception as ex:
            logger.critical(f"An error occurred while deleting the product file {product_path}.", ex)                
    ...
```

**Описание**: Удаляет продукт, у которого нет партнерской ссылки.

**Параметры**:
- `product_id` (str): Идентификатор продукта.
- `exc_info` (bool, optional): Флаг для отображения дополнительной информации об исключении. По умолчанию `False`.