# Модуль `_example_ali_promo_campaign.py`

## Обзор

Данный модуль содержит примеры создания рекламной кампании на AliExpress с использованием класса `AliPromoCampaign`. Он демонстрирует, как инициализировать и использовать данный класс для настройки кампаний.

## Содержание

- [Обзор](#обзор)
- [Импорт модулей](#импорт-модулей)
- [Переменные](#переменные)
- [Примеры использования](#примеры-использования)

## Импорт модулей

В данном разделе перечислены все импортированные модули, необходимые для работы кода.

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

В данном разделе определены основные переменные, используемые в примерах.

```python
campaigns_directory = Path(gs.path.google_drive, 'aliexpress', 'campaigns')
campaign_names = get_directory_names(campaigns_directory)

campaign_name = '280624_cleararanse'
category_name = 'gaming_comuter_accessories'
language = 'EN'
currency = 'USD'
```

## Примеры использования

В этом разделе представлены примеры использования класса `AliPromoCampaign` для создания рекламной кампании.

### Пример 1: Инициализация с именованными аргументами
Создание экземпляра `AliPromoCampaign` с использованием именованных аргументов.
```python
a:SimpleNamespace = AliPromoCampaign(campaign_name = campaign_name, 
                     category_name = category_name, 
                     language = language, 
                     currency = currency) 

campaign = a.campaign
category = a.category
products = a.category.products
```

### Пример 2: Инициализация с аргументом типа `dict`
Создание экземпляра `AliPromoCampaign` с передачей словаря, содержащего языковые и валютные настройки.
```python
a = AliPromoCampaign(campaign_name, category_name, {'EN':'USD'})
```

### Пример 3: Инициализация со строковыми аргументами
Создание экземпляра `AliPromoCampaign` с передачей строковых аргументов для языка и валюты.
```python
a = AliPromoCampaign(campaign_name, category_name, 'EN','USD')
```