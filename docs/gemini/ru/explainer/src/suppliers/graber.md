# Анализ кода файла hypotez/src/suppliers/graber.py

## <input code>

```python
from __future__ import annotations
## \file hypotez/src/suppliers/graber.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe
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
MODE = 'dev'

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
    # ... (остальной код декоратора)
```

## <algorithm>

(Блок-схема отсутствует.  Невозможно создать точную блок-схему без контекста `Driver` и предполагаемого использования `j_loads` и `gs.path`).

Однако можно описать основной алгоритм:

1. **Импорт библиотек:** Импортируются необходимые библиотеки, в том числе асинхронные операции (`asyncio`), обработка путей (`pathlib`), типы данных (`typing`), работа с JSON (`jjson`),  нормализация строк, чисел и дат (`normalizer`), логирование (`logger`), работа с изображениями.

2. **Определение `Context`:** Класс `Context` предназначен для хранения глобальных настроек, таких как драйвер (`driver`), локаторы (`locator`), префикс поставщика (`supplier_prefix`).  Эта информация будет доступна всем методам.

3. **Декоратор `close_pop_up`:** Декоратор `close_pop_up` используется для асинхронного закрытия всплывающих окон (`pop-up`) до выполнения функции.  Он использует метод `execute_locator` драйвера для закрытия.  Возможная ошибка при выполнении локатора ловится.

4. **`Graber` класс:** Базовый класс для сбора данных с веб-страницы. При инициализации загрузка локаторов из JSON файла.

5. **Методы класса `Graber`:** Каждая функция (метод) отвечает за извлечение и нормализацию конкретного поля данных с веб-страницы.
	* Они принимают опциональное значение `value` для переопределения данных. 
	* Используют метод `execute_locator` драйвера для извлечения данных по локаторам.
	* Нормализуют данные с помощью функций из модуля `normalize_string`, `normalize_int` и т.д.
	* Записывают результат в соответствующее поле объекта `ProductFields`.
	* Возвращают `True` в случае успеха или `None` (с обработкой исключений).

6. **Функция `grab_page`:** Метод для асинхронного сбора всех полей продукта.  Он динамически вызывает методы для каждого указанного поля.


## <mermaid>

```mermaid
graph LR
    A[Graber] --> B(grab_page);
    B --> C{fetch_all_data};
    C --> D[name];
    C --> E[price];
    ... // Дополнительные поля
    D --> F[ProductFields.name];
    E --> G[ProductFields.price];
    F -- данные --> H[Обработка];
    G -- данные --> H;
    H --> I[Результат];

    subgraph "Webdriver Interaction"
        D --> J[execute_locator];
        E --> J;
        ... // Другие поля
        J --> K[Данные с страницы];
        K --> D;
        K --> E;
        ...
    end
subgraph "Зависимости"
  A -- импорт --> L[ProductFields];
  A -- импорт --> M[driver];
  A -- импорт --> N[j_loads];
  A -- импорт --> O[gs];
  ...
end

```

## <explanation>

**Импорты:**
- `from __future__ import annotations`:  Улучшает работу с типов в Python.
- `import ...`: Стандартные модули Python для работы с датами, системами, потоками, путями, типами данных, локализацией.
- `from src import ...`: Импортируются модули из пакета `src`, которые определяют структуры данных, например `ProductFields`, `Category`. Это указывает на то, что проект имеет структуру с пакетами и модулями.
- `from src.utils.jjson import ...`: Импортируются вспомогательные функции для работы с JSON.
- `from src.utils.image import ...`: Импортируются функции для работы с изображениями (загрузка, сохранение).
- `from src.utils.string.normalizer import ...`: Функции для нормализации строк, чисел и дат.

**Классы:**
- `Context`: Хранит глобальные настройки, как драйвер (webdriver), локаторы, префикс поставщика.
- `Graber`: Базовый класс для сбора данных с веб-страницы. Содержит атрибуты (`supplier_prefix`, `locator`, `driver`, `fields`) и методы для извлечения конкретных полей.

**Функции:**
- `close_pop_up`: Декоратор для асинхронного закрытия всплывающих окон.
- `error`: Обработчик ошибок для полей, записывает сообщение об ошибке в логи.
- `set_field_value`: Универсальная функция для установки значения поля, обрабатывает возможные ошибки и использует `asyncio.to_thread` для асинхронной обработки.
- `grab_page`: Сбор всех данных с помощью вызова методов для каждого поля.
- Все остальные методы, например, `name`, `price` - методы класса `Graber`, ответственные за извлечение конкретных полей продукта. Они принимают необязательный параметр `value` для передачи данных и используют `execute_locator`.

**Переменные:**
- `MODE`: Строковая константа, вероятно, для выбора режима работы (например, 'dev' или 'prod').
- `Context.driver`, `Context.locator`, `Context.supplier_prefix`: Глобальные переменные для хранения данных в классе `Context`.
-  `self.locator`: Объект SimpleNamespace, содержащий локаторы для каждого поля.

**Возможные ошибки и улучшения:**
- **Обработка исключений:** В методах обработки полей очень много повторяющегося кода в обработке исключений. Можно вынести общую функцию или класс для обработки исключений.
- **Улучшение обработки `value`:**  Логирование при отсутствии значения `value` могло бы быть более информированным (с указанием причины, например, не было передано значение, поле не найдено).
- **Проверка локатора:** Добавить проверку на существование локатора, прежде чем его использовать, чтобы избежать неожиданных ошибок.
- **Декоратор для нормализации:** Можно создать декоратор, который будет автоматически нормализовать значение перед записью в поле. Это упростит код и снизит вероятность ошибок.
- **Docstrings:** Добавьте более подробные Docstrings, описывающие параметры и возможные значения.
- **Проверка типов данных:** Методы `normalize_` могут дополнительно проверять корректность типов передаваемых значений, это позволит увеличить надежность обработки данных.
- **Модуль `gs`:** Необходимо определить, откуда берётся этот объект.  Его использование в коде предполагает, что он содержит пути и другие константы.

**Взаимосвязи с другими частями проекта:**
- `Graber` зависит от `Driver` (модуль `src.webdriver.driver`) для выполнения `execute_locator`.
- `ProductFields` и другие классы, используемые в Graber, находятся в `src.product.product_fields`.
-  Существует зависимость от `gs.path`, который, вероятно, предоставляет пути к файлам локаторов.
-  Локаторы хранятся в JSON файлах.
-  Проект использует сторонний инструмент `langdetect` для определения языка текста.
-  Проект использует сторонний инструмент для нормализации данных, например `normalize_string`.
-  Логирование `logger` используется для записи сообщений об ошибках и информации.
- Необходимо контекст для функций `pprint` и `j_loads`, не ясно, откуда они берут значения `gs`.