# Анализ кода из файла hypotez/src/suppliers/graber.py

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
    """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции."""
    # ... (определение декоратора)
```

## <algorithm>

**Блок-схема (фрагмент, из-за большого размера кода):**

1. **Импорт модулей:**
    - Импортируются необходимые библиотеки: `datetime`, `os`, `sys`, `asyncio`, `pathlib`, `typing`, `langdetect`, `functools`, `header`, `gs`, `ProductFields`, `Category`, `jjson`, `image`, `normalizer`, `ExecuteLocatorException`, `printer`, `logger`.
    - Импортируются дополнительные модули, скорее всего, для управления веб-драйвером, JSON-данными, обработкой изображений и логированием.
    - Импортируются модули из пакета `src`.

2. **Определение константы `MODE`:**
    - Устанавливается значение константы.

3. **Определение класса `Context`:**
    - Хранит глобальные настройки (например, драйвер, локатор, префикс поставщика).
    - `Context.driver` - глобальный экземпляр веб-драйвера.
    - `Context.locator_for_decorator` - глобальный локатор для декоратора `@close_pop_up`.

4. **Определение декоратора `close_pop_up`:**
    - Функция-декоратор для асинхронного закрытия всплывающих окон (`execute_locator`).
    - Декоратор `@wraps` сохраняет метаданные оригинальной функции.

5. **Определение класса `Graber`:**
    - `__init__(self, supplier_prefix: str, driver: 'Driver')` - инициализация с передачей префикса и веб-драйвера. Загружает локаторы из `product.json`.
    - `grab_page(*args, **kwards)` - получает данные для полей, указанных в `args` и `kwards`.

6. **Методы `set_field_value`, `error`:**
    - `error(field: str)` - обработчик ошибок при работе с полями.
    - `set_field_value(self, value, locator_func, field_name, default)` - универсальная функция для установки значений поля, с обработкой возможных ошибок.

7. **Методы для сбора данных (name, price, etc.):**
    - Методы с `@close_pop_up()` для каждого поля продукта.
    - Получают значение из локатора, используя `await self.driver.execute_locator()`.
    - Нормализуют полученные значения с помощью функций `normalize_*`.
    - Записывают значение в соответствующее поле `self.fields`.
    - Возвращают результат `True` или `None`.

8. **Пример использования:**
    - Продемонстрирован пример того, как создать класс, унаследованный от `Graber`, переопределить метод `name`, и использовать декоратор `@close_pop_up`.

**Пример данных:**

- `self.locator` - содержит локаторы для каждого поля в файле `product.json`.
- `self.fields` - объект `ProductFields`, куда записываются собранные значения.
- `Context.driver` - ссылка на экземпляр веб-драйвера.


## <mermaid>

```mermaid
graph LR
    subgraph "Graber Class"
        Graber --> init
        init --> locator_load
        locator_load --> fields_init
        fields_init --> grab_page
        grab_page --> fetch_data
        fetch_data --> [loop over fields]
        [loop over fields] --> set_field_value
        set_field_value --> result_field
        result_field --> fields_update
        fields_update --> return_fields
    end
    subgraph "Data Flow"
        Driver --> execute_locator
        execute_locator --locator data--> Graber
        Graber --field values--> ProductFields
    end
    subgraph "Dependencies"
        Graber --> ProductFields
        Graber --> Driver
        Graber --> src.utils.jjson
        Graber --> src.utils.image
        Graber --> src.utils.string.normalizer
        Graber --> src.logger
        Graber --> header
        Graber --> src.gs
        Graber --> Category
    end
```


## <explanation>

**Импорты:**

- `from __future__ import annotations`: используется для улучшенной совместимости с type hints.
- `import ...`: Импортирует стандартные библиотеки Python для работы со временем, системами, вводом/выводом и т.д., а также библиотеку `langdetect` для определения языка текста.  `header` и `gs` -  вероятно, внутренние модули проекта.
- `from src import ...`: Импортирует классы и функции из других файлов и папок проекта.  `ProductFields`, `Category`, `jjson`, `image`, `normalizer`, `ExecuteLocatorException`, `printer`, и `logger` находятся в `src`-пакете, что подразумевает организацию проекта по модулям/пакетам.

**Классы:**

- `Context`: Класс для хранения глобальных настроек, таких как веб-драйвер (`driver`), локаторы (`locator`) и префикс поставщика (`supplier_prefix`).   Он используется для обеспечения доступа к данным из разных частей приложения.
- `Graber`: Базовый класс для сбора данных с веб-страниц разных поставщиков.  Его методы (`name`, `price`, ...) осуществляют запрос данных к веб-драйверу.  Ключевой момент - методы  используют декоратор `@close_pop_up` для закрытия потенциальных всплывающих окон перед обращением к локатору.


**Функции:**

- `close_pop_up()`: Декоратор, который асинхронно закрывает всплывающие окна перед выполнением метода.  Он  помогает обрабатывать диалоговые окна, которые могут появиться на странице.
- `set_field_value()`: Функция для установки значения поля.  Обрабатывает потенциальные исключения и возвращает значение по умолчанию, если локатор не найден.
- `grab_page()`: Асинхронная функция, которая собирает данные для определённых полей. Она вызывает методы для каждого поля, переданного в `args`, что позволяет динамически получать данные.


**Переменные:**

- ``:  Предполагает, что это константа для определения режима работы программы (например, разработка/производство).


**Возможные ошибки и улучшения:**

- **Обнаруженный баг:** В `local_image_path` метод `id_product` вызывается  неправильно.  `await self.id_product()` - это  *неправильный* способ передачи данных из методов.  Необходимо пересмотреть механизм передачи значений между методами, возможно, через аргументы или глобальные переменные.  Более надёжный способ передачи данных из `grab_product_page()` в `local_image_path()` - через аргументы или через атрибуты класса `Graber` (при условии, что `id_product` может быть рассчитан или получен *до* вызова `local_image_path`).
- **Обработка ошибок:**  В большинстве методов присутствуют блоки `try...except`. Это хорошо, но в некоторых местах не хватает более ясной информации об ошибке или более подробной логики обработки (например, `...`).


**Взаимосвязи с другими частями проекта:**

- `Graber` напрямую зависит от класса `Driver` (`src.webdriver.driver`).  Методы `Graber`  вызывают `execute_locator` для получения данных с помощью веб-драйвера.
- `Graber` использует нормализаторы из `src.utils.string.normalizer`, для обработки данных, чтобы убрать избыточность и улучшить качество данных.
- `ProductFields` – это, вероятно, структура данных, содержащая поля для товара, и `Graber` записывает в него полученные значения.
- `gs` – это, вероятно, вспомогательный модуль с глобальными переменными (`gs.path`, `gs.now`), используемый для хранения путей и текущего времени соответственно.
- `logger` (и `ExecuteLocatorException`) используется для логирования действий и обработки ошибок во время выполнения.


Этот код реализует структурированный и гибкий подход к сбору данных о товарах с веб-страниц поставщиков.  Однако, для увеличения устойчивости и корректности работы требуется решить проблему передачи данных между методами и добавить более подробные и эффективные обработчики ошибок.