# Анализ кода файла hypotez/src/suppliers/graber.py

## <input code>

```python
from __future__ import annotations
## \file hypotez/src/suppliers/graber.py
# -*- coding: utf-8 -*-\n
#! venv/bin/python/python3.12

"""

```rst
.. module: src.suppliers 
	:platform: Windows, Unix
	:synopsis:  Базовый класс сбора данных со старницы HTML поставщиков.
    Целевые поля страницы (`название`,`описание`,`спецификация`,`артикул`,`цена`,...) собирает вебдрйвер (class: [`Driver`](../webdriver))
    Местополжение поля определяется его локатором. Локаторы хранятся в словарях JSON в директории `locators` каждого поставщика.
    ([подробно о локаторах](locators.ru.md))
```    

## Для нестендартной обработки полей товара просто переопределите функцию в своем классе.
Пример:
```python
s = `suppler_prefix`
from src.suppliers imoprt Graber
locator = j_loads(gs.path.src.suppliers / f{s} / \'locators\' / \'product.json`)\n

class G(Graber):

    @close_pop_up()
    async def name(self, value:Optional[Any] = None):
        self.fields.name = <Ваша реализация>
        )
```

"""


import datetime
import os
import sys
import asyncio
from pathlib import Path
from typing import Optional, Any
from types import SimpleNamespace
from typing import Callable
from langdetect import detect
from functools import wraps

import header
from src import gs

from src.product.product_fields import ProductFields
from src.category import Category
# from src.webdriver.driver import Driver  # не требуется импортировать здесь
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import save_png_from_url, save_png
from src.utils.string.normalizer import normalize_string, normalize_int, normalize_float, normalize_boolean, normalize_sql_date
from src.logger.exceptions import ExecuteLocatorException
#from src.endpoints.prestashop import PrestaShop
from src.utils.printer import pprint
from src.logger import logger

# Глобальные настройки через объект `Context`
class Context:
    """
    Класс для хранения глобальных настроек.

    :ivar driver: Объект драйвера, используется для управления браузером или другим интерфейсом.
    :vartype driver: 'Driver'
    :ivar locator: Пространство имен для хранения локаторов.
    :vartype locator: SimpleNamespace
    :ivar supplier_prefix: Префикс поставщика.
    :vartype supplier_prefix: str
    """

    # Атрибуты класса
    driver: 'Driver' = None
    locator_for_decorator: SimpleNamespace = None  # <- Если будет установлен - выполнится декоратор `@close_pop_up`. Устанавливается при инициализации поставщика, например: `Context.locator = self.locator.close_pop_up`
    supplier_prefix: str = None


# Определение декоратора для закрытия всплывающих окон
# В каждом отдельном поставщике (`Supplier`) декоратор может использоваться в индивидуальных целях
# Общее название декоратора `@close_pop_up` можно изменить 
# Если декоратор не используется в поставщике - поставь 

def close_pop_up(value: 'Driver' = None) -> Callable:
    """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

    Args:
        value ('Driver'): Дополнительное значение для декоратора.

    Returns:
        Callable: Декоратор, оборачивающий функцию.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if Context.locator_for_decorator:
                try:
                    await Context.driver.execute_locator(Context.locator_for_decorator)  # Await async pop-up close  
                    ... 
                except ExecuteLocatorException as ex:
                    logger.debug(f'Ошибка выполнения локатора:', ex)
            return await func(*args, **kwargs)  # Await the main function
        return wrapper
    return decorator

# ... (остальной код)
```

## <algorithm>

(Блок-схема – сложно представить в текстовом формате. mermaid – см. ниже)

Алгоритм работы класса `Graber` заключается в асинхронном сборе данных с веб-страницы, используя веб-драйвер (`Driver`).  Локаторы полей на странице хранятся в файлах JSON.  Основной цикл сбора проходит по списку полей (`args`) и вызывает соответствующие методы. Каждое поле обрабатывается отдельным методом, который использует `execute_locator` для получения значения из веб-драйвера. Данные нормализуются перед записью в объект `ProductFields`. Декоратор `@close_pop_up` опционально выполняет закрытие всплывающих окон до получения данных.

**Пример**:  При вызове `grab_page` с параметрами `args=['name', 'price']`, алгоритм выполняет следующие шаги:
1. Вызывает `fetch_all_data` с переданными `args`.
2. `fetch_all_data` циклически вызывает методы `name` и `price`.
3. Методы `name` и `price` используют `await self.driver.execute_locator` для получения значения из локатора.
4. Результаты обработки сохраняются в `self.fields`.
5. Возвращает `self.fields`.


## <mermaid>

```mermaid
graph LR
    subgraph "Graber Class"
        A[grab_page(args, kwargs)] --> B{fetch_all_data};
        B --> C[for filed_name in args];
        C --> D{getattr(self, filed_name)};
        D -- exists --> E[await function(kwards.get(filed_name))];
        D -- not exists --> F[skip];
        E --> G[execute_locator(locator)];
        G --> H[normalize_string/int/float];
        H --> I[set_field_value(self, value, filed_name)];
        I --> J[return self.fields];
    end
    subgraph "Close Pop-up Decorator"
        B -- Context.locator_for_decorator --> K[await Context.driver.execute_locator(Context.locator_for_decorator)];
        K --> E; 
    end
    subgraph "Data Flow"
        A --> Driver;
        Driver --> G;
        G -- result --> H;
        H --> ProductFields;
    end
    subgraph "External Dependencies"
        Driver --> ../webdriver;
        ProductFields --> src/product/product_fields;
        j_loads/j_loads_ns --> src/utils/jjson;
        normalize_string --> src/utils/string/normalizer;
        save_png_from_url --> src/utils/image;
        logger --> src/logger;
        gs --> src/gs;
        Category --> src/category;
    end
```


## <explanation>

**Импорты:**
- `from __future__ import annotations`:  Позволяет использовать аннотации типов для методов и атрибутов в коде (совместимость с более новыми версиями Python).
- `import datetime`, `import os`, `import sys`, `import asyncio`: Стандартные библиотечные импорты для работы с датами, операционной системой, асинхронностью и т.д.
- `from pathlib import Path`: Для работы с путями к файлам, обеспечивая платформонезависимость.
- `from typing import Optional, Any, Callable, List`:  Из пакета `typing`, который используется для объявления типов данных,  предоставляя такие типы как Optional, Any, Callable.
- `from types import SimpleNamespace`: Для создания пространств имен, используемых для хранения данных (например, локаторов).
- `from langdetect import detect`: Библиотека для автоматической детекции языка текста.
- `from functools import wraps`:  для декораторов.
- `import header`: Импорт модуля `header`, который, скорее всего, содержит константы или другие настройки, но без дополнительной информации определить его роль невозможно.
- `from src import gs`:  Импортирует переменную или класс `gs`, скорее всего, связанную с глобальными настройками проекта, `gs` неявно импортируется и содержит глобальные настройки из пакета `src`.
- `from src.product.product_fields import ProductFields`: Импортирует класс `ProductFields` из модуля `src.product.product_fields`, который, вероятно, представляет структуру для хранения полей продукта.
- `from src.category import Category`: Импортирует класс `Category` из модуля `src.category`, который, вероятно, представляет структуру для хранения данных о категориях продуктов.
- `from src.utils.jjson import j_loads, j_loads_ns, j_dumps`:  Из пакета `src.utils.jjson` импортируются функции для работы с JSON-данными, в том числе для загрузки локаторов из файлов JSON.
- `from src.utils.image import save_png_from_url, save_png`: Импортирует функции для работы с изображениями, вероятно, для загрузки и сохранения изображений продукта.
- `from src.utils.string.normalizer import ...`: Импортирует функции для нормализации строк, чисел и дат.
- `from src.logger.exceptions import ExecuteLocatorException`: Импортирует класс `ExecuteLocatorException`, который, вероятно, используется для обработки исключений, связанных с выполнением локаторов.
- `from src.utils.printer import pprint`: Импортирует функцию для красивого вывода данных.
- `from src.logger import logger`: Импорт объекта логгера.

**Классы:**
- `Context`: Хранит глобальные настройки (например, веб-драйвер, локаторы, префикс поставщика).
- `Graber`: Базовый класс для сбора данных с веб-страниц.  Использует веб-драйвер (`Driver`) для получения данных, используя локаторы из файла `product.json`, нормализует полученные значения и записывает их в `ProductFields`.
- `ProductFields`: Вероятно, представляет структуру данных для хранения собранных полей продукта.

**Функции:**
- `close_pop_up`: Декоратор, который выполняет закрытие всплывающих окон перед выполнением декорированной функции.
- `error`: Обработчик ошибок для полей продукта.
- `set_field_value`: Универсальная функция для установки значений полей с обработкой ошибок.
- `grab_page`: Асинхронная функция для сбора всех полей продукта. Использует методы для каждого поля и передаёт их значение в соответствующие функции.
- `fetch_all_data`: Динамически вызывает методы для получения данных для каждого поля.
- методы `name`, `price`, ..., `visibility`, `weight`: Асинхронные методы для получения конкретных полей продукта с помощью `await self.driver.execute_locator(self.locator.поле)`. 

**Переменные:**
- `MODE`: Глобальная переменная, вероятно, для выбора режима работы (например, "dev" или "prod").
- `Context.driver`, `Context.locator_for_decorator`, `Context.supplier_prefix`: Атрибуты класса `Context` для хранения глобальных настроек.
- `self.supplier_prefix`, `self.locator`, `self.driver`, `self.fields`: Атрибуты класса `Graber` для хранения префикса поставщика, локаторов, веб-драйвера и полей продукта соответственно.


**Возможные ошибки и улучшения:**
- **Ошибка в коде примера**: `s = `suppler_prefix`\nfrom src.suppliers imoprt Graber\nlocator = j_loads(gs.path.src.suppliers / f{s} / \'locators\' / \'product.json`)\n` -  в примере не закрыт `'` перед product.json
- **Упрощение обработки ошибок:**  Обработка исключений выглядит избыточной.  Возможно, стоит использовать более компактную структуру обработки ошибок.
- **Документация:**  Документация могла бы быть более полной и структурированной.
- **Типизация:** Используются аннотации типов, но некоторые типы данных (например, `locator_func`) могли бы быть более точно определены.
- **Управление локаторами**: Важно удостовериться, что локаторы (`self.locator`) в каждом классе `Supplier` корректны и соответствую структуре файла `product.json`.
- **Проверка логгирования**: Ошибки логгируются, но не все важные моменты, например, успешное получение значений или невалидные данные. Логирование должно быть более подробным и информативным.
- **Объект `gs`:** Необходимо уточнить, что представляет из себя объект `gs` (globals settings). Без понимания `gs` сложно понять контекст.
- **Возвращаемые значения:** Некоторые методы (например, `fetch_all_data`) возвращают значения, которые не используются.  Уточнить смысл отсутствия возвращаемого значения для этих методов и, если это необходимо, привести к более единообразной практике.
- **Переменная `d`:** В методе `locale` используется переменная `d`, которая не определена в данном отрывке кода. Это потенциальная ошибка.


**Взаимосвязь с другими частями проекта:**
-  Код взаимодействует с классом `Driver` (из `src.webdriver.driver`) для получения данных с веб-страниц.
- Использует классы и функции из `src` (напр., `ProductFields`, `normalize_string`, `logger`).
- Зависимость от `gs.path.src.suppliers / f{s} / 'locators' / 'product.json`' указывает на существование директории `locators` с локаторами.