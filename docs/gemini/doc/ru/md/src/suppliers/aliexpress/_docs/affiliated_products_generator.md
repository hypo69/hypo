# Модуль `affiliated_products_generator`

## Обзор

Этот модуль содержит класс `AliAffiliatedProducts`, предназначенный для сбора полной информации о продуктах с AliExpress Affiliate API.  Класс обрабатывает URL-адреса или ID продуктов, извлекает данные о продуктах, включая изображения, видео и JSON-данные, и сохраняет их локально.

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
from src.utils import j_dumps, save_png_from_url, save_video_from_url, pprint
from src.utils.file import read_text_file, save_text_file

from src.logger import logger
```

- **Стандартные библиотеки:** `asyncio`, `itertools`, `math`, `pathlib`, `typing`, `types`, `urllib.parse`
- **Внешние библиотеки:** `src.settings`, `src.suppliers.aliexpress`, `src.utils.convertor`, `src.utils`, `src.logger` (и другие модули из проекта)

## Класс `AliAffiliatedProducts`

### Документация класса

```python
class AliAffiliatedProducts(AliApi):
    """ Класс для сбора полной информации о продуктах по URL-адресам или ID.
    locator_description Более подробную информацию о создании шаблонов для рекламных кампаний см. в разделе «Управление рекламными кампаниями AliExpress».
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

- **Назначение:** Сбор полной информации о продуктах по URL-адресам или ID с помощью AliExpress Affiliate API.
- **Пример использования:** Показ инициализации класса и вызова метода `_affiliate_product` для обработки URL-адресов продуктов.


### Атрибуты

```python
campaign_name: str
campaign_category: Optional[str]
campaign_path: Path
language: str
currency: str
```

- **`campaign_name`**: Название рекламной кампании.
- **`campaign_category`**: Категория кампании (по умолчанию `None`).
- **`campaign_path`**: Путь к каталогу с материалами кампании.
- **`language`**: Язык кампании (по умолчанию `'EN'`).
- **`currency`**: Валюта кампании (по умолчанию `'USD'`).


### Инициализация

```python
def __init__(self,
             campaign_name: str,
             campaign_category: Optional[str] = None,
             language: str = 'EN',
             currency: str = 'USD',
             *args, **kwargs):
    """
    @param campaign_name `str`: Название рекламной кампании. Каталог с подготовленным материалом берется по имени.
    @param campaign_category `Optional[str]`: Категория кампании (по умолчанию None).
    @param language `str`: Язык кампании (по умолчанию 'EN').
    @param currency `str`: Валюта кампании (по умолчанию 'USD').
    @param tracking_id `str`: ID отслеживания для AliExpress API.
    """
    super().__init__(language, currency)

    self.campaign_name = campaign_name
    self.campaign_category = campaign_category
    self.language = language
    self.currency = currency
    self.locale = f"{self.language}_{self.currency}"
    self.campaign_path = gs.path.google_drive / 'aliexpress' / 'campaigns' / self.campaign_name / 'categories' / self.campaign_category
```

- **`super().__init__(language, currency)`**: Вызов конструктора родительского класса `AliApi`.
- **`self.campaign_path`**: Конструирование пути к каталогу кампании на основе `campaign_name` и `campaign_category`.

### Методы

#### `process_affiliate_products`

```python
def process_affiliate_products(self, prod_urls: List[str]) -> List[SimpleNamespace]:
    """
    Обрабатывает список URL-адресов и возвращает список продуктов с аффилированными ссылками и сохранёнными изображениями.

    :param prod_urls: Список URL-адресов или ID продуктов.
    :return: Список обработанных продуктов.
    """
    # ... (тело метода)
```

- **Назначение:** Обработка списка URL-адресов или ID продуктов для получения аффилированных ссылок, сохранения изображений и видео, и сохранения деталей продуктов.
- **Параметры:**
  - **`prod_urls`**: Список URL-адресов или ID продуктов.
- **Возвращает:** Список объектов `SimpleNamespace`, представляющих обработанные продукты.

#### `delete_product`

```python
def delete_product(self, product_id: str, exc_info: bool = False):
    """ Удаляет продукт, для которого не найдена аффилированная ссылка. """
    # ... (тело метода)
```

- **Назначение:** Удаление продукта, для которого не найдена аффилированная ссылка.

(Подробное описание методов `process_affiliate_products` и `delete_product` требует анализа их реализации.  В данном ответе представлено краткое описание, но для полной документации необходимо детальное описание логики, алгоритмов и обработки исключений, а также примеров использования.)


##  Заключение

Данная документация предоставляет базовый обзор модуля `affiliated_products_generator`.  Для более глубокого понимания необходимо изучить код и реализацию методов, а также документацию связанных модулей.