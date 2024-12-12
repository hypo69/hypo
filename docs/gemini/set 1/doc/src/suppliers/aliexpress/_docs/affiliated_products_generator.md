# ИНСТРУКЦИЯ ПО ИСПОЛЬЗОВАНИЮ `affiliated_products_generator.py`

## Обзор

Файл `affiliated_products_generator.py` содержит класс `AliAffiliatedProducts`, предназначенный для сбора полной информации о продуктах с AliExpress Affiliate API. Он расширяет функциональность класса `AliApi`, обрабатывая URL-адреса или идентификаторы продуктов и извлекая данные об аффилированных продуктах, включая сохранение изображений, видео и JSON-данных.

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

Список используемых библиотек и модулей:

- Стандартные библиотеки Python (`asyncio`, `itertools`, `math`, `pathlib`, `typing`, `types`, `urllib.parse`)
- Модули проекта (`src`, `src.suppliers.aliexpress`, `src.utils.convertor`, `src.utils`, `src.logger`)

## Класс `AliAffiliatedProducts`

### Документация класса

```python
class AliAffiliatedProducts(AliApi):
    """ Класс для сбора полной информации о продуктах из URL-адресов или идентификаторов продуктов
    locator_description Для получения более подробной информации о создании шаблонов для рекламных кампаний, см. раздел `Управление рекламными кампаниями на AliExpress`
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

### Цель

Сбор полной информации о продуктах с использованием AliExpress Affiliate API по URL-адресам или идентификаторам продуктов.

### Пример использования

Демонстрирует инициализацию класса и вызов метода `_affiliate_product` для обработки URL-адресов продуктов.

### Атрибуты

```python
campaign_name: str
campaign_category: Optional[str]
campaign_path: Path
language: str
currency: str
```

- `campaign_name`: Название рекламной кампании.
- `campaign_category`: Категория кампании (по умолчанию `None`).
- `campaign_path`: Путь к директории, где хранятся материалы кампании.
- `language`: Язык кампании (по умолчанию `'EN'`).
- `currency`: Валюта кампании (по умолчанию `'USD'`).


### Инициализация

```python
def __init__(self,
             campaign_name: str,
             campaign_category: Optional[str] = None,
             language: str = 'EN',
             currency: str = 'USD',
             *args, **kwargs):
    """
    @param campaign_name `str`: Название рекламной кампании. Директория с подготовленным материалом берется по имени.
    @param campaign_category `Optional[str]`: Категория для кампании (по умолчанию None).
    @param language `str`: Язык для кампании (по умолчанию 'EN').
    @param currency `str`: Валюта для кампании (по умолчанию 'USD').
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

### Методы

(Документация для методов `process_affiliate_products` и `delete_product` приведена ниже)


```
# Документация для остальных методов (если они есть)
```


## Метод `process_affiliate_products`

### Описание

Обрабатывает список URL-адресов и возвращает список продуктов с аффилированными ссылками и сохраненными изображениями.

### Параметры

- `prod_urls`: Список URL-адресов или идентификаторов продуктов.

### Возвращает

Список обработанных продуктов в формате `SimpleNamespace`.

### Исключения

(Если метод `process_affiliate_products` вызывает исключения, укажите их здесь)


## Метод `delete_product`

### Описание

Удаляет продукт, для которого не найдена аффилированная ссылка.

### Параметры

- `product_id`: Идентификатор продукта.

### Исключения

- `FileNotFoundError`: Если файл продукта не найден.
- `Exception`: Другие ошибки.


**ПРИМЕЧАНИЕ**:  Для полной документации необходимо добавить описание всех других методов и функций, содержащихся в файле `affiliated_products_generator.py`, а также детально описать используемые алгоритмы и логику.