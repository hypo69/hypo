# <input code>

```python
## \file hypotez/src/suppliers/graber.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""
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
locator = j_loads(gs.path.src.suppliers / f{s} / \'locators\' / \'product.json`)\n\nclass G(Graber):\n\n    @close_pop_up()\n    async def name(self, value: Any = None):\n        self.fields.name = <Ваша реализация>\n        )\n    ```

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
from src.utils.image import save_png_from_url, save_png
from src.utils.string.normalizer import normalize_string, normalize_int, normalize_float, normalize_boolean
from src.logger.exceptions import ExecuteLocatorException
from src.endpoints.prestashop import PrestaShop
from src.utils import pprint
from src.logger import logger

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

**Шаг 1:**  Инициализация класса `Graber`. Принимает префикс поставщика и драйвер. Загружает локаторы из файла `product.json`. Сохраняет ссылки на драйвер и локаторы в экземпляре класса. Создаёт экземпляр `ProductFields`.

**Шаг 2:** Вызов функции `grab_page`.  Функция `fetch_all_data` внутри `grab_page` содержит вызовы различных функций (например, `name`, `price`, `specification`).

**Шаг 3:**  Выполнение функций для каждого поля. Например, `name`:
    *   Проверяет, передано ли значение `value` в вызов.
    *   Если нет, пытается получить значение из локатора с помощью `await self.d.execute_locator(self.l.name)`.
    *   Если значение не найдено или не валидно, записывает значение по умолчанию (пустую строку).
    *   Выполняется нормализация строки `value = normalize_string(value)`
    *   Записывает результат в соответствующее поле `self.fields.name`.

**Шаг 4:** Возвращает заполненный объект `ProductFields`.

**Пример:**

Если вызывается `await grab_page(id_product='123')`, то `id_product` будет передан в функцию `fetch_all_data`.  `fetch_all_data` вызовет `await self.id_product('123')` (внутренняя логика функции). Внутри `id_product`, если  `self.fields.id_supplier` пустое, то оно будет получено через локатор, а в `self.fields.id_product` запишется результат. Если `value` в `id_product` был передано, то оно просто будет сохранено.


# <mermaid>

```mermaid
graph LR
    subgraph Грабер (Graber)
        A[Graber.__init__(supplier_prefix, driver)] --> B{Загрузка локаторов};
        B --> C[Сохранение ссылок на driver и locator];
        C --> D[Создание ProductFields];
        D --> E[Context.driver = self.driver];
        D --> F[Context.supplier_prefix = supplier_prefix];
        E --> G[Вызов grab_page()];

        subgraph Функция grab_page()
            G --> H[fetch_all_data()];
            H --> I[Вызов функций для полей (name, price, etc.)];
            
            subgraph Функция для поля (name)
                I --> J[Проверка value];
                J -- value --> K[value (direct)];
                J -- no value --> L[Поиск через execute_locator];
                L --> M[Обработка ошибки];
                K --> N[Нормализация value];
                N --> O[Запись в self.fields.name];
            end
        end
    end
    
    subgraph Внешние зависимости
        Driver --> A;
        ProductFields --> A;
        j_loads_ns --> A;
        gs.path --> A;
        logger --> A;
        
    end
```

**Объяснение к диаграмме:** Класс `Graber` получает данные из веб-драйвера (`Driver`), используя `execute_locator`, считывая локаторы из файла. Взаимодействует с `ProductFields` для хранения собранных данных. Пакеты `src.utils.jjson`, `gs.path` и другие обеспечивают необходимые вспомогательные функции.


# <explanation>

**Импорты:**

* `import os`, `import sys`, `import asyncio`, `from pathlib import Path`, `from types import SimpleNamespace`, `from typing import Any, Callable`, `from langdetect import detect`, `from functools import wraps`: Стандартные библиотеки Python, необходимые для работы с файлами, асинхронными операциями, типами данных, обнаружения языка и декораторами.
* `import header`: Вероятно, импортирует пользовательские настройки или функции.
* `from src import gs`: Импортирует переменную `gs` из пакета `src`, которая скорее всего содержит пути.
* `from src.product.product_fields import ProductFields`: Импортирует класс `ProductFields`, представляющий структуру данных для полей продукта, из модуля `product_fields`.
* `from src.category import Category`: Импортирует класс `Category`.
* `from src.webdriver import Driver`: Импортирует класс `Driver`, отвечающий за взаимодействие с веб-драйвером (Selenium, Playwright и т.п.), вероятно, из `webdriver` модуля.
* `from src.utils.jjson import j_loads, j_loads_ns, j_dumps`: Импортирует функции для работы с JSON данными.
* `from src.utils.image import save_png_from_url, save_png`: Функции для работы с изображениями.
* `from src.utils.string.normalizer import normalize_string, normalize_int, normalize_float, normalize_boolean`: Функции для нормализации данных (строки, целые, вещественные числа, булевы значения).
* `from src.logger.exceptions import ExecuteLocatorException`: Импортирует пользовательское исключение для обработки ошибок локаторов.
* `from src.endpoints.prestashop import PrestaShop`: Импортирует класс `PrestaShop`, вероятно, относящийся к интеграции с PrestaShop.
* `from src.utils import pprint`: Импортирует функцию для красивого вывода.
* `from src.logger import logger`: Импортирует объект логгера, вероятно, для записи сообщений об ошибках и информации.


**Классы:**

* `Context`: Класс для хранения глобальных настроек, таких как драйвер (`driver`), локаторы (`locator`) и префикс поставщика (`supplier_prefix`).  Используется для централизованного управления ресурсами.
* `Graber`: Базовый класс для сбора данных с веб-страниц для всех поставщиков. Содержит поля `supplier_prefix`, `locator` (загруженный из JSON-файла), `driver`, `fields` (объект `ProductFields`) для хранения данных продукта.


**Функции:**

* `close_pop_up`: Декоратор для закрытия всплывающих окон.  Он оборачивает функцию, вызывая `execute_locator` на драйвере перед выполнением функции.
* `error`: Обработчик ошибок, регистрирует сообщение об ошибке в лог.
* `set_field_value`: Универсальная функция для установки значений полей с обработкой ошибок. Принимает значение, функцию получения значения из локатора, имя поля и значение по умолчанию.
* `grab_page`: Асинхронная функция для сбора всех полей продукта. Содержит вызовы функций для каждого поля.

Функции `id_product`, `name`, `price` и др.: Асинхронные функции для извлечения конкретных полей данных из HTML страницы с помощью веб-драйвера.  Используют локаторы из `locator` для нахождения элементов. Обрабатывают возможные ошибки.


**Переменные:**

* `MODE`: Переменная для хранения режима работы (например, 'dev', 'prod').
* `Context.driver`: Экземпляр класса `Driver`, используется для управления веб-драйвером.
* `Context.locator_for_decorator`: Вспомогательная переменная для декоратора `close_pop_up`, хранит локатор для закрытия всплывающих окон.
* `self.fields`: Объект `ProductFields` для хранения данных о товаре.

**Возможные ошибки и улучшения:**

* **Обработка исключений:**  В каждой функции сбора данных (`name`, `price`, etc.) существуют блоки `try...except`. Но некоторые исключения (например, `ExecuteLocatorException`) не обрабатываются в каждом блоке. Обработка должна быть более полной, чтобы предотвратить сбой программы при возникновении ошибок.
* **Передача данных:** Функция `fetch_all_data` должна получать данные через аргументы.  На данный момент аргументы `**kwargs` не используются должным образом, что может привести к ошибкам или некорректной работе.
* **Логика проверки валидности:**  Проверка валидности результата (`value`) не используется в достаточной степени. Необходимо реализовать более подробные проверки.
* **Документация:** Хотя функции и классы содержат строковые пояснения, некоторые могли бы быть улучшены, добавив более детальные объяснения аргументов, возвращаемых значений, и вариантов использования.
* **Определение `self.d` и `self.l`:**  Использование сокращённых имён `self.d` и `self.l` для `self.driver` и `self.locator` может сделать код менее читаемым в дальнейшем.
* **Обработка пустых значений:**  Использование `or ''` в строках вида `value = value or  await self.d.execute_locator(...) or ''` может быть не оптимальным.


**Взаимосвязи с другими частями проекта:**

Код сильно зависит от `src.webdriver.Driver`, `src.product.product_fields.ProductFields`, `src.logger` для логгирования, и `src.utils.jjson` для работы с JSON-локаторами. Локаторы JSON определяются в соответствующей папке локаторов, в зависимости от `supplier_prefix`, который передаётся в конструктор.  Файл `product.json` содержит структуру локаторов для работы с конкретными полями на веб-странице, что в свою очередь позволяет гибко собирать данные с разных поставщиков.