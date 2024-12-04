# <input code>

```python
## \file hypotez/src/suppliers/graber.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.suppliers 
	:platform: Windows, Unix
	:synopsis:  Базовый класс сбора данных со старницы HTML поставщиков.
    Целевые поля страницы (`название`,`описание`,`спецификация`,`артикул`,`цена`,...) собирает вебдрйвер (class: [`Driver`](../webdriver))
    Местополжение поля определяется его локатором. Локаторы хранятся в словарях JSON в директории `locators` каждого поставщика.
    ([подробно о локаторах](locators.ru.md))


## Для нестендартной обработки полей товара просто переопределите функцию в своем классе.
Пример:
```python
s = `suppler_prefix`
from src.suppliers imoprt Graber
locator = j_loads(gs.path.src.suppliers / f{s} / 'locators' / 'product.json`)

class G(Graber):

    @close_pop_up()
    async def name(self, value: Any = None):
        self.fields.name = <Ваша реализация>
        )
```

"""
MODE = 'dev'


import os
import sys
import asyncio
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Callable
from langdetect import detect
from functools import wraps

import header
from src import gs

from src.product.product_fields import ProductFields
from src.category import Category
from src.webdriver import Driver
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import save_png_from_url
from src.utils import pprint
from src.logger import logger
from src.logger.exceptions import ExecuteLocatorException
from src.endpoints.prestashop import PrestaShop

# Глобальные настройки через объект `Context`
class Context:
    """
    Класс для хранения глобальных настроек.

    :ivar driver: Объект драйвера, используется для управления браузером или другим интерфейсом.
    :vartype driver: Driver
    :ivar locator: Пространство имен для хранения локаторов.
    :vartype locator: SimpleNamespace
    :ivar supplier_prefix: Префикс поставщика.
    :vartype supplier_prefix: str
    """

    # Атрибуты класса
    driver: Driver = None
    locator_for_decorator: SimpleNamespace = None  # <- Если будет установлен - выполнится декоратор `@close_pop_up`. Устанавливается при инициализации поставщика, например: `Context.locator = self.locator.close_pop_up`
    supplier_prefix: str = None


# Определение декоратора для закрытия всплывающих окон
# В каждом отдельном поставщике (`Supplier`) декоратор может использоваться в индивидуальных целях
# Общее название декоратора `@close_pop_up` можно изменить 
# Если декоратор не используется в поставщике - поставь 

def close_pop_up(value: Any = None) -> Callable:
    """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

    Args:
        value (Any): Дополнительное значение для декоратора.

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


class Graber:
    """Базовый класс сбора данных со страницы для всех поставщиков."""

    def __init__(self, supplier_prefix: str, driver: Driver):
        """Инициализация класса Graber.

        Args:
            supplier_prefix (str): Префикс поставщика.
            locator (Locator): Экземпляр класса Locator.
            driver (Driver): Экземпляр класса Driver.
        """
        self.supplier_prefix = supplier_prefix
        self.locator: SimpleNamespace = j_loads_ns(gs.path.src / 'suppliers' / supplier_prefix / 'locators' / 'product.json')
        self.l = self.locator
        self.driver: Driver = driver
        self.d = self.driver
        self.fields: ProductFields = ProductFields()
        Context.driver = self.driver
        Context.supplier_prefix = supplier_prefix

    # ... (остальной код)
```

# <algorithm>

Этот код реализует базовый класс `Graber` для сбора данных с веб-страниц.  Алгоритм работы можно представить следующей блок-схемой:

1. **Инициализация (`__init__`)**:
   - Принимает префикс поставщика (`supplier_prefix`) и драйвер (`driver`) как входные данные.
   - Загружает локаторы из файла `product.json` (в папке `locators` поставщика) с использованием `j_loads_ns` из `src.utils.jjson`.
   - Инициализирует атрибуты `self.locator`, `self.driver`, `self.fields`.
   - Устанавливает глобальные настройки `Context.driver` и `Context.supplier_prefix`.

   *Пример*: `self.supplier_prefix = 'amazon'`
   *Пример данных, перемещаемых между функциями*: `supplier_prefix` и `driver` объект передаются в конструктор и глобальная переменная `Context.supplier_prefix` устанавливается равной значению переменной `supplier_prefix`.

2. **Обработка ошибок (`error`)**:
   - Логирует сообщения об ошибках во время сбора данных.

3. **Универсальное заполнение полей (`set_field_value`)**:
   - Принимает значение, функцию получения значения из локатора, имя поля и значение по умолчанию.
   - Использует `asyncio.to_thread` для безопасного выполнения функции получения из локатора.
   - Возвращает полученное значение или значение по умолчанию, если локатор не найден.


4. **Сбор данных с страницы (`grab_page`)**:
   - Вызывает ряд функций для сбора конкретных данных.
   - Возвращает объект `ProductFields` с собранными данными.

   *Пример*: Загрузка данных полей "name", "price", "specification", ..., используя `await self.name()`, `await self.price()`, `await self.specification()`.
   *Пример перемещения данных*: Данные, полученные из функций сбора данных, записываются в атрибут `self.fields` класса `Graber`, который затем возвращается в `grab_page`.


5. **Функции сбора отдельных полей (например, `name`, `price`)**:
   - Используют декоратор `@close_pop_up` для автоматического закрытия всплывающих окон.
   - Получают значение из локатора с использованием `await self.d.execute_locator(self.l.name)`.
   - Проверяют валидность значения и, при необходимости, обрабатывают его.
   - Записывают значение в соответствующее поле объекта `ProductFields`.

   *Пример*: Функция `name` использует локатор `self.l.name` для получения имени продукта.
   *Пример перемещения данных*: Полученные данные помещаются в `self.fields.name`, что приводит к изменению состояния объекта `ProductFields`.


**Пошаговая блок-схема (частично):**


```mermaid
graph TD
    A[Graber.__init__(supplier_prefix, driver)] --> B{Загрузка локаторов};
    B -- Да -> C[Инициализация self.locator, self.driver, self.fields];
    B -- Нет -> D[Обработка ошибки];
    C --> E[Context.driver = driver];
    C --> F[Context.supplier_prefix = supplier_prefix];
    F --> G[grab_page()];
    G --> H[fetch_all_data()];
    H --> I[name(), price(), ...];
    I --> J[Запись данных в self.fields];
    J --> K[Возврат self.fields];
```



# <mermaid>

```mermaid
graph LR
    subgraph Graber Class
        A[Graber] --> B(init);
        B --> C[Загрузка локаторов];
        C --> D{Инициализация self.locator};
        D --> E{Инициализация Context};
        E --> F(grab_page);
        F --> G[fetch_all_data()];
        subgraph data_collection
            G --> H[name()];
            H --> I[execute_locator(name)];
            I --> J[Запись в ProductFields];

        end
    end
    subgraph Dependencies
        C --> K[j_loads_ns];
        K --> L[gs.path];
        L -- путь к json -> M[product.json];

        D --> N[ProductFields];
        N --> O[ProductFields.name];
        G --> P[Driver];
        P --> Q[execute_locator()];
    end
```


# <explanation>

* **Импорты**: 
   - `os`, `sys`, `asyncio`, `pathlib`, `types`, `typing`, `langdetect`, `functools`: Стандартные библиотеки Python.
   - `header`: Вероятно, содержит дополнительные настройки или функции, специфичные для проекта.
   - `gs`:  Этот импорт (`from src import gs`) указывает на зависимость от модуля `gs` в папке `src`, который, скорее всего, предоставляет глобальные настройки или пути к ресурсам.
   - `ProductFields`, `Category`, `Driver`, `j_loads`, `j_loads_ns`, `j_dumps`, `save_png_from_url`, `pprint`, `logger`, `ExecuteLocatorException`, `PrestaShop`:  Все эти импорты относятся к внутренним модулям проекта, находящимся в директориях `src.product.product_fields`, `src.category`, `src.webdriver`, `src.utils.jjson`, `src.utils.image`, `src.utils`, `src.logger`, `src.logger.exceptions`, `src.endpoints.prestashop` соответственно.  Они определяют структуры данных, функциональность управления веб-драйвером, работу с JSON, обработку изображений, логирование и возможно, взаимодействие с определенным API.

* **Классы**:
   - `Context`: Хранит глобальные конфигурационные настройки, например, экземпляр `Driver` (веб-драйвер) и префикс поставщика. Это позволяет обращаться к этим данным из разных частей кода.
   - `Graber`: Базовый класс для сбора данных с веб-страниц. Обладает атрибутами (`self.supplier_prefix`, `self.locator`, `self.driver`, `self.fields`) и методами для управления драйвером (`self.d.execute_locator`), сбора данных из локаторов и их записи в `ProductFields`.

* **Функции**:
   - `close_pop_up`: Декоратор для закрытия всплывающих окон. Важно, что он проверяет значение `Context.locator_for_decorator` и, если оно установлено, выполняет `execute_locator`.
   - Сбор данных (например, `name`, `price`, `specification`) : Функции для получения конкретных полей данных с веб-страницы. Они используют `await self.d.execute_locator(self.l.fieldname)` для поиска данных по локаторам.

* **Переменные**: `MODE`, `value`, `field`, `locator_func`, `field_name`, `default`, `locator_result`, `kwargs`: Типы этих переменных указаны в аннотациях типов (`typing`). Используются для передачи данных, локаторов, обработки ошибок и хранения значений полей.

* **Возможные ошибки и улучшения**:
   - **Поддержка различных локаторов:** Код жестко привязан к `product.json`. В реальном проекте может потребоваться поддержка различных стратегий поиска (CSS, XPath, ID и т.д.).
   - **Более подробная обработка ошибок:** В блоках `try...except`  отсутствует  детальная обработка специфических исключений.  Нужно  было бы предоставить более релевантные сообщения об ошибках.
   - **Проверка типов:** Необходимо убедиться, что полученные значения соответствуют ожидаемому типу.
   - **Переиспользование кода:** Многие методы `Graber`  выглядят очень похожими, можно рассмотреть возможность объединения или абстракции повторяющегося кода.
   - **Документация:** Комментарии могут быть более точными и понятными.
   - **Валидация данных:**  Добавить проверки полученных данных на валидность (формат, диапазон значений).

**Цепочка взаимосвязей**:

`Graber` использует `Driver` из `src.webdriver` для взаимодействия с веб-драйвером и `ProductFields` из `src.product.product_fields` для хранения собранных данных.  Классы  из  `src.utils` и `src.logger` обеспечивают функциональность для работы с данными и ведения журнала. `gs` (likely Global Settings) предоставляет глобальную информацию, а `product.json` содержит локаторы. Все эти компоненты работают вместе для сбора данных о товарах с веб-сайтов поставщиков.