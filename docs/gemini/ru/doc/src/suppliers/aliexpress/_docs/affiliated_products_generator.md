# ИНСТРУКЦИЯ ПО ИСПОЛЬЗОВАНИЮ `affiliated_products_generator.py`

## Обзор

Файл `affiliated_products_generator.py` содержит класс `AliAffiliatedProducts`, предназначенный для извлечения полной информации о продуктах с сайта AliExpress, используя API аффилированных программ.  Класс позволяет обрабатывать URL или ID продуктов, извлекать данные о продуктах, а также сохранять изображения и видео.  Он опирается на класс `AliApi` для взаимодействия с API.


## Импорты и Зависимости

Этот раздел содержит список импортируемых библиотек и модулей:

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

- **Стандартные библиотеки:** `asyncio`, `itertools`, `math`, `pathlib`, `typing`, `types`, `urllib.parse`
- **Внешние библиотеки:** Модули из пакета `src`, включая классы для работы с AliExpress API, обработкой файлов, логгированием и другими вспомогательными функциями.

## Класс `AliAffiliatedProducts`

#### Документация класса

```python
class AliAffiliatedProducts(AliApi):
    """ Класс для сбора полной информации о продуктах по URL или ID продукта.
    locator_description Подробнее о создании шаблонов рекламных кампаний смотрите в разделе `Управление рекламными кампаниями на AliExpress`.
    @code
    # Пример использования:
    prod_urls = ['123', '456', ...]
    prod_urls = ['https://www.aliexpress.com/item/123.html', '456', ...]

    parser = AliAffiliatedProducts(
                                campaign_name,
                                campaign_category,
                                language,
                                currency)

    products = parser._affiliate_product(prod_urls)
    @endcode
    """
```

- **Назначение:** Сбор полной информации о продуктах по URL или ID продукта с помощью API аффилированных программ AliExpress.
- **Пример использования:** Показывает, как инициализировать класс и вызвать метод `_affiliate_product` для обработки URL продуктов.

#### Атрибуты

```python
campaign_name: str
campaign_category: Optional[str]
campaign_path: Path
language: str
currency: str
```

- **`campaign_name`**: Название рекламной кампании.
- **`campaign_category`**: Категория кампании (по умолчанию `None`).
- **`campaign_path`**: Путь к каталогу, где хранятся материалы кампании.
- **`language`**: Язык кампании (по умолчанию `'EN'`).
- **`currency`**: Валюта кампании (по умолчанию `'USD'`).


#### Инициализация

```python
def __init__(self,
             campaign_name: str,
             campaign_category: Optional[str] = None,
             language: str = 'EN',
             currency: str = 'USD',
             *args, **kwargs):
    """
    Инициализация класса с параметрами кампании.

    @param campaign_name `str`: Название рекламной кампании. Директория с подготовленным материалом берется по имени.
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

- **`super().__init__(language, currency)`**: Вызов конструктора родительского класса `AliApi`.
- **`self.campaign_path`**: Построение пути к каталогу кампании на основе `campaign_name` и `campaign_category`.

#### Методы

Подробное описание методов приведено ниже.


##### `process_affiliate_products`

```python
def process_affiliate_products(self, prod_urls: List[str]) -> List[SimpleNamespace]:
    """
    Обрабатывает список URL и возвращает список продуктов с аффилированными ссылками и сохраненными изображениями.

    :param prod_urls: Список URL или ID продуктов.
    :return: Список обработанных продуктов.
    """
    ...
```

- **Назначение:** Обработка списка URL или ID продуктов для извлечения аффилированных ссылок, сохранения изображений и видео, и сохранения деталей продуктов.
- **Параметры:**
  - **`prod_urls`**: Список URL или ID продуктов.
- **Возвращает:** Список объектов `SimpleNamespace`, представляющих обработанные продукты.

##### `delete_product`

(Описание метода `delete_product` следует аналогично структуре документации для `process_affiliate_products`)


## Пример использования

Пример использования класса `AliAffiliatedProducts` и метода `process_affiliate_products` для работы с набором URL продуктов.


```python
# пример инициализации
parser = AliAffiliatedProducts('campaign_name', 'category')

# пример обработки списка URL продуктов
prod_urls = ['url1', 'url2', 'url3']
result = parser.process_affiliate_products(prod_urls)
```


Этот документ предоставляет краткое введение в функционал `affiliated_products_generator.py`.  Для более глубокого понимания рекомендуется ознакомиться с кодом и документацией связанных модулей.