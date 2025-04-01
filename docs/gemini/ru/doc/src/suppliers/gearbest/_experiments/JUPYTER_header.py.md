# Модуль _experiments

## Обзор

Модуль содержит экспериментальный код, связанный с поставщиком Gearbest. Включает в себя импорты различных модулей и классов, необходимых для работы с веб-драйвером, поставщиками, продуктами, категориями и утилитами.

## Подробнее

Данный код является частью проекта `hypotez` и содержит эксперименты, связанные с поставщиком Gearbest. В нем импортируются необходимые модули и классы для работы с веб-драйвером, поставщиками, продуктами, категориями и утилитами. Также модуль содержит функцию `start_supplier`, предназначенную для запуска поставщика с заданными параметрами.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix: str = 'aliexpress', locale: str = 'en' ):
    """ Старт поставщика """
    ...
```

**Назначение**: Функция для запуска поставщика с заданными параметрами.

**Параметры**:
- `supplier_prefix` (str): Префикс поставщика. По умолчанию 'aliexpress'.
- `locale` (str): Локаль. По умолчанию 'en'.

**Возвращает**:
- `Supplier`: Объект поставщика, созданный с указанными параметрами.

**Как работает функция**:

1.  Определяет параметры в виде словаря, содержащего префикс и локаль поставщика.
2.  Создает и возвращает экземпляр класса `Supplier` с переданными параметрами.

```mermaid
graph LR
    A[Определение параметров] --> B(Создание экземпляра Supplier);
    B --> C(Возврат экземпляра Supplier);
```

**Примеры**:

```python
# Пример запуска поставщика с префиксом 'gearbest' и локалью 'ru'
supplier = start_supplier(supplier_prefix='gearbest', locale='ru')

# Пример запуска поставщика с параметрами по умолчанию
supplier = start_supplier()
```
```python
from pathlib import Path
import json
import re


#from settings import gs
from src.webdriver.driver import Driver
from src.suppliers import Supplier
from src.product import Product, ProductFields
from src.category import Category
from src.utils import StringFormatter, StringNormalizer
from src.utils.printer import  pprint
from src.endpoints.PrestaShop import Product as PrestaProduct
, save_text_file
# ----------------

def start_supplier(supplier_prefix: str = 'aliexpress', locale: str = 'en' ):
    """ Старт поставщика """
    params: dict = \
    {
        'supplier_prefix': supplier_prefix,
        'locale': locale
    }
    
    return Supplier(**params))