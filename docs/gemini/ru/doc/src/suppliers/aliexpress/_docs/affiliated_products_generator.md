# ИНСТРУКЦИЯ ПО ИСПОЛЬЗОВАНИЮ MODULЯ `affiliated_products_generator.py`

## Обзор

Модуль `affiliated_products_generator.py` из пакета `aliexpress` отвечает за получение полных данных о продуктах с сайта AliExpress, используя API для партнёрских ссылок. Он расширяет возможности класса `AliApi`, позволяя обрабатывать URL или ID продуктов и извлекать информацию о партнёрских продуктах, включая сохранение изображений, видео и JSON-данных.

## Импорты и Зависимости

Этот модуль использует следующие импорты:

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

from src.logger import logger
```

В импорты входят стандартные библиотеки Python, внешние библиотеки и вспомогательные модули из проекта `src`.

## Класс `AliAffiliatedProducts`

### Описание

```python
class AliAffiliatedProducts(AliApi):
    """ Класс для сбора полных данных о продуктах по URL или ID.
    locator_description Для более подробной информации о создании шаблонов для рекламных кампаний, см. раздел "Управление рекламными кампаниями на AliExpress".
    @code
    # Пример использования:
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

Класс `AliAffiliatedProducts` предназначен для сбора полных данных о продуктах AliExpress по URL или ID, используя API партнёрских ссылок.

### Атрибуты

```python
campaign_name: str
campaign_category: Optional[str]
campaign_path: Path
language: str
currency: str
```

* `campaign_name`: Название рекламной кампании.
* `campaign_category`: Категория кампании (по умолчанию `None`).
* `campaign_path`: Путь к директории, где хранятся материалы кампании.
* `language`: Язык кампании (по умолчанию `'EN'`).
* `currency`: Валюта кампании (по умолчанию `'USD'`).


### Инициализация

```python
def __init__(self,
             campaign_name: str,
             campaign_category: Optional[str] = None,
             language: str = 'EN',
             currency: str = 'USD',
             *args, **kwargs):
    """
    Инициализирует класс с данными о кампании.

    @param campaign_name `str`: Название рекламной кампании. Директория с подготовленным материалом определяется по имени.
    @param campaign_category `Optional[str]`: Категория кампании (по умолчанию None).
    @param language `str`: Язык кампании (по умолчанию 'EN').
    @param currency `str`: Валюта кампании (по умолчанию 'USD').
    @param tracking_id `str`: Идентификатор отслеживания для API AliExpress.
    """
    super().__init__(language, currency)

    self.campaign_name = campaign_name
    self.campaign_category = campaign_category
    self.language = language
    self.currency = currency
    self.locale = f"{self.language}_{self.currency}"
    self.campaign_path = gs.path.google_drive / 'aliexpress' / 'campaigns' / self.campaign_name / 'categories' / self.campaign_category
```

### Методы

#### `process_affiliate_products`

```python
def process_affiliate_products(self, prod_urls: List[str]) -> List[SimpleNamespace]:
    """
    Обрабатывает список URL и возвращает список продуктов с партнёрскими ссылками и сохранёнными изображениями.

    :param prod_urls: Список URL продуктов или их ID.
    :return: Список обработанных продуктов.
    """
    # ... (код метода)
```

Метод `process_affiliate_products` обрабатывает список URL продуктов, получает партнёрские ссылки, сохраняет изображения и видео, и записывает подробности продуктов в локальный файл JSON.

#### `delete_product`

```python
def delete_product(self, product_id: str, exc_info: bool = False):
    """ Удаляет продукт, для которого не найдена партнёрская ссылка."""
    # ... (код метода)
```

Метод `delete_product` удаляет информацию о продукте, если для него не удалось найти партнёрскую ссылку.

## Подробное описание методов (кратко)

Каждый метод описан в документации кода в формате Python, включая описание параметров, возвращаемых значений и возможных исключений.

## Пример использования


```
#Пример использования
prod_urls = ['https://www.aliexpress.com/item/123.html', 'https://www.aliexpress.com/item/456.html']
parser = AliAffiliatedProducts('my_campaign', 'electronics', 'RU', 'RUB')
products = parser.process_affiliate_products(prod_urls)

if products:
  for product in products:
    print(product.product_id, product.promotion_link)
```

Этот пример демонстрирует, как использовать класс `AliAffiliatedProducts` для обработки списка URL продуктов.


```
```