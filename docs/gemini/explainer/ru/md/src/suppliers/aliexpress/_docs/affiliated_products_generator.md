# affiliated_products_generator.py

## Обзор файла `affiliated_products_generator.py`

Файл `affiliated_products_generator.py` из модуля `src.suppliers.aliexpress` содержит класс `AliAffiliatedProducts`. Этот класс отвечает за генерацию полных данных о продуктах с AliExpress Affiliate API. Он основан на классе `AliApi`, обрабатывает URL-адреса или ID продуктов и извлекает информацию о связанных продуктах, включая сохранение изображений, видео и JSON-данных.

### Импорты и зависимости

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

Список импортированных библиотек, включая стандартные библиотеки Python и пользовательские модули из пакета `src`.  Обратите внимание на импорты для работы с файлами, обработкой URL, асинхронностью, логгированием и другими вспомогательными функциями.


### Класс `AliAffiliatedProducts`

#### Документация класса

```python
class AliAffiliatedProducts(AliApi):
    """ Класс для сбора полных данных о продуктах по URL или ID
    locator_description Для получения более подробной информации о создании шаблонов для рекламных кампаний, см. раздел `Управление рекламными кампаниями на Aliexpress`
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

Описание класса, указывающее его назначение и пример использования.


#### Атрибуты

```python
campaign_name: str
campaign_category: Optional[str]
campaign_path: Path
language: str
currency: str
```

Описание атрибутов класса, представляющих данные о рекламной кампании (название, категория, язык, валюта) и путь к папке кампании.


#### Инициализация

```python
def __init__(self,
             campaign_name: str,
             campaign_category: Optional[str] = None,
             language: str = 'EN',
             currency: str = 'USD',
             *args, **kwargs):
    """
    @param campaign_name `str`: Название рекламной кампании. Директория с подготовленным материалом берется по имени.
    @param campaign_category `Optional[str]`: Категория кампании (по умолчанию None).
    @param language `str`: Язык кампании (по умолчанию 'EN').
    @param currency `str`: Валюта кампании (по умолчанию 'USD').
    @param tracking_id `str`: ID отслеживания для API AliExpress.
    """
    super().__init__(language, currency)

    self.campaign_name = campaign_name
    self.campaign_category = campaign_category
    self.language = language
    self.currency = currency
    self.locale = f"{self.language}_{self.currency}"
    self.campaign_path = gs.path.google_drive / 'aliexpress' / 'campaigns' / self.campaign_name / 'categories' / self.campaign_category
```

Инициализация класса. Обращает внимание на построение пути к папке кампании на основе переданных параметров.


#### Методы

##### `process_affiliate_products`

```python
def process_affiliate_products(self, prod_urls: List[str]) -> List[SimpleNamespace]:
    """
    Обрабатывает список URL-адресов и возвращает список продуктов с партнерскими ссылками и сохраненными изображениями.
    
    :param prod_urls: Список URL-адресов или ID продуктов.
    :return: Список обработанных продуктов.
    """
    ...
```

Метод обрабатывает список URL-адресов продуктов, извлекает партнерские ссылки, сохраняет изображения и видео, и сохраняет подробности продукта в JSON-файлы.  Внутри метода реализованы логика обработки ошибок и сохранения данных.

##### `delete_product`

```python
def delete_product(self, product_id: str, exc_info: bool = False):
    """ Удаляет продукт, у которого нет партнерской ссылки"""
    ...
```

Метод удаляет информацию о продукте, у которого не найдена партнерская ссылка. Реализует механизм удаления записи о продукте из файла источников.


**Краткое резюме:**

Код реализует класс для работы с API AliExpress Affiliate, позволяющий собрать информацию о продуктах, включая партнерские ссылки, изображения и видео.  Класс обрабатывает список URL-адресов продуктов, сохраняет данные локально и обрабатывает различные ситуации, такие как отсутствие партнерской ссылки или ошибки ввода-вывода.  Для работы с данным классом необходимы внешние зависимости, которые не включены в представленный фрагмент кода.