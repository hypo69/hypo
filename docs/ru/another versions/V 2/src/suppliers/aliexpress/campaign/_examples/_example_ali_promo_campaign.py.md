# src.suppliers.aliexpress.campaign._examples._example_ali_promo_campaign.py

## Обзор

Примеры создания рекламной кампании.

## Содержание

- [Импорты](#Импорты)
- [Переменные](#Переменные)
- [Примеры использования класса `AliPromoCampaign`](#Примеры-использования-класса-AliPromoCampaign)

## Импорты

В данном разделе перечислены все используемые импорты.

```python
import header
from pathlib import Path
from types import SimpleNamespace
from src import gs
from src.suppliers.aliexpress import AliPromoCampaign
from src.suppliers.aliexpress import AliAffiliatedProducts
from src.utils import get_filenames, get_directory_names, read_text_file, csv2dict
from src.utils.jjson import j_loads_ns
from src.utils.printer import pprint
from src.logger.logger import logger
```

## Переменные

В данном разделе перечислены все используемые переменные.

```python
campaigns_directory = Path(gs.path.google_drive, 'aliexpress', 'campaigns')
campaign_names = get_directory_names(campaigns_directory)

campaign_name = '280624_cleararanse'
category_name = 'gaming_comuter_accessories'
language = 'EN'
currency = 'USD'
```
## Примеры использования класса `AliPromoCampaign`

В этом разделе представлены примеры использования класса `AliPromoCampaign` с различными вариантами инициализации.

### Пример 1

Создание экземпляра `AliPromoCampaign` с явным указанием параметров `campaign_name`, `category_name`, `language` и `currency`.

```python
a:SimpleNamespace = AliPromoCampaign(campaign_name = campaign_name, 
                     category_name = category_name, 
                     language = language, 
                     currency = currency) 
```

В результате создается объект `a`, содержащий атрибуты `campaign`, `category`, и `products`, полученные из `AliPromoCampaign`.

```python
campaign = a.campaign
category = a.category
products = a.category.products
```

### Пример 2

Создание экземпляра `AliPromoCampaign` с передачей словаря, где ключ - это `language`, а значение - `currency`.

```python
a = AliPromoCampaign(campaign_name,category_name,{'EN':'USD'})
```

### Пример 3

Создание экземпляра `AliPromoCampaign` с передачей параметров `language` и `currency` как отдельных строковых аргументов.

```python
a = AliPromoCampaign(campaign_name,category_name, 'EN','USD')
```