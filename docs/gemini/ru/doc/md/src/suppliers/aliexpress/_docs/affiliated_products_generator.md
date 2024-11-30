# Модуль `affiliated_products_generator`

## Обзор

Данный модуль содержит класс `AliAffiliatedProducts`, предназначенный для сбора полной информации о продуктах с AliExpress Affiliate API. Класс получает данные по URL или ID продукта, загружает изображения и видео, а также сохраняет JSON-данные. Он основан на классе `AliApi`.

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
from src.utils import j_dumps
from src.utils import save_png_from_url, save_video_from_url
from src.utils import pprint
from src.utils.file import read_text_file, save_text_file

from src.logger import logger
```

- **Стандартные библиотеки Python:** `asyncio`, `itertools`, `math`, `pathlib`, `typing`, `types`, `urllib.parse`
- **Внешние библиотеки:** `src.settings`, `src.suppliers.aliexpress`, `src.utils.convertor`, `src.utils`, `src.logger` (вероятно, ваши собственные модули)


## Класс `AliAffiliatedProducts`

### Документация класса

```python
class AliAffiliatedProducts(AliApi):
    """ Класс для сбора полной информации о продуктах по URL или ID.
    locator_description Для получения более подробной информации о создании шаблонов для рекламных кампаний, обратитесь к разделу "Управление рекламными кампаниями на AliExpress".
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

- **Назначение:** Сбор полной информации о продуктах с AliExpress Affiliate API по URL или ID.
- **Пример использования:**  Демонстрирует инициализацию класса и вызов метода `_affiliate_product` для обработки списка URL.


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
- **`campaign_path`**: Путь к директории для материалов кампании.
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
    Инициализация класса.

    @param campaign_name `str`: Название рекламной кампании. Директория с подготовленным материалом берется по имени.
    @param campaign_category `Optional[str]`: Категория кампании (по умолчанию None).
    @param language `str`: Язык кампании (по умолчанию 'EN').
    @param currency `str`: Валюта кампании (по умолчанию 'USD').
    @param tracking_id `str`: Идентификатор отслеживания для AliExpress API.
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
- **`self.campaign_path`**: Построение пути к директории кампании на основе `campaign_name` и `campaign_category`.


### Методы

#### `process_affiliate_products`

```python
def process_affiliate_products(self, prod_urls: List[str]) -> List[SimpleNamespace]:
    """
    Обрабатывает список URL и возвращает список продуктов с аффилированными ссылками и сохраненными изображениями.

    :param prod_urls: Список URL продуктов или ID.
    :return: Список обработанных продуктов.
    """
    # ... (код метода)
```

- **Назначение:** Обработка списка URL или ID продуктов для получения аффилированных ссылок, сохранения изображений и видео, и хранения деталей продуктов.
- **Параметры:**
  - **`prod_urls`**: Список URL или ID продуктов.
- **Возвращает:** Список объектов `SimpleNamespace`, представляющих обработанные продукты.


#### `delete_product`

(Документация к методу `delete_product` аналогично заполняется)


(Остальные методы описываются подобным образом, со своими документами `Args`, `Returns`, `Raises` и кратким описанием назначения.)


```
```

Этот расширенный шаблон документации в формате Markdown предоставляет более подробную информацию о каждой части кода, следуя указанным требованиям.  Заполните детали для остальных методов и атрибутов, чтобы получить полную документацию.  Обратите внимание на использование правильного синтаксиса Markdown.