# Модуль hypotez/src/suppliers/aliexpress/campaign/_examples/_example_edit_campaign.py

## Обзор

Модуль содержит примеры кода для редактирования рекламных кампаний на AliExpress. Он предоставляет базовый класс `AliCampaignEditor`, наследующий от `AliPromoCampaign`, для работы с рекламными кампаниями. Модуль использует различные вспомогательные функции и классы для работы с данными кампаний, такими как парсинг, преобразование и обработка.

## Классы

### `AliCampaignEditor`

**Описание**: Класс `AliCampaignEditor` представляет собой редактор рекламных кампаний AliExpress, расширяющий функционал базового класса `AliPromoCampaign`.

**Методы**:

- `__init__(self, campaign_name: str, category_name: str, language: str = 'EN', currency: str = 'USD')`:
    **Описание**: Конструктор класса.
    **Параметры**:
    - `campaign_name` (str): Имя рекламной кампании.
    - `category_name` (str): Название категории.
    - `language` (str, optional): Язык (по умолчанию 'EN').
    - `currency` (str, optional): Валюта (по умолчанию 'USD').
    **Возвращает**:
    -  None

## Функции

(Список функций из импортированных модулей, если они присутствуют, и их документация, если она есть,  следует добавить сюда).


## Вспомогательные модули и функции

(Список импортированных модулей и функций и их краткое описание)

```python
import re
import shutil
from pathlib import Path
from typing import List, Optional, Union
from types import SimpleNamespace
from src import gs
from src.suppliers.aliexpress.scenarios.campaigns import AliPromoCampaign
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids
from src.suppliers.aliexpress.utils.set_full_https import ensure_https
from src.utils import j_loads_ns, j_loads
from src.utils.convertors import list2string, csv2dict
from src.utils import pprint
from src.utils.jjson import j_dumps, j_loads, j_loads_ns
from utils.interface import read_text_file, get_filenames
from src.logger import logger
```

**Описание импортированных модулей**:  Модули и классы, которые используются для работы с данными, файлами, логированием, настройками.


**Примечания:**  Для более полной документации необходимо добавить  документацию к функциям и методам, которые были импортированы и использованы в данном файле.  В текущем коде отсутствует подробная документация, поэтому данное описание является минимальным.