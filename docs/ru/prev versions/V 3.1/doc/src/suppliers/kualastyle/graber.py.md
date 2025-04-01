# Модуль `graber`

## Обзор

Модуль `graber` предназначен для сбора значений полей на странице товара веб-сайта `kualastyle.co.il`. Он содержит класс `Graber`, который наследуется от класса `Graber` (Grbr) и переопределяет его методы для специфической обработки полей товаров на сайте `kualastyle.co.il`. Модуль использует декораторы для выполнения предварительных действий перед отправкой запроса к веб-драйверу.

## Подорбней

Этот модуль является частью системы для извлечения и обработки данных с веб-сайтов поставщиков. Он специализируется на сайте `kualastyle.co.il`, адаптируя общие механизмы сбора данных (`Graber` из `src.suppliers.graber`) к особенностям структуры и представления данных на этом конкретном сайте.

## Классы

### `Graber`

**Описание**: Класс `Graber` предназначен для извлечения информации о товарах с сайта `kualastyle.co.il`. Он наследуется от класса `Graber` (Grbr) и переопределяет его методы для адаптации к специфической структуре данных сайта.

**Методы**: 
- `__init__`: Инициализирует экземпляр класса `Graber`, устанавливает префикс поставщика и вызывает конструктор родительского класса.

**Параметры**: 
- `driver` (Driver): Экземпляр веб-драйвера для взаимодействия с веб-страницами.
- `lang_index` (int): Индекс языка, используемого на сайте.

**Примеры**
```python
from src.webdriver.driver import Driver
from src.suppliers.kualastyle.graber import Graber

# Пример создания экземпляра класса Graber
driver = Driver()
graber = Graber(driver, 0) 
```

## Функции

### `close_pop_up`

```python
def close_pop_up(value: Any = None) -> Callable:
    """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

    Args:
        value (Any): Дополнительное значение для декоратора.

    Returns:
        Callable: Декоратор, оборачивающий функцию.
    """
```

**Описание**: Функция `close_pop_up` является декоратором, предназначенным для закрытия всплывающих окон на веб-странице перед выполнением основной логики декорируемой функции. Это полезно для обработки ситуаций, когда всплывающие окна могут мешать сбору данных.

**Параметры**:
- `value` (Any, optional): Дополнительное значение, которое может быть передано декоратору. По умолчанию `None`.

**Возвращает**:
- `Callable`: Декоратор, который можно использовать для оборачивания функций.

**Вызывает исключения**:
- `ExecuteLocatorException`: Возникает, если при выполнении локатора происходит ошибка.

**Примеры**:
```python
from src.suppliers.kualastyle.graber import close_pop_up

@close_pop_up()
async def my_function():
    # Основная логика функции
    pass
```
```python
def __init__(self, driver: Driver, lang_index:int):
    """Инициализация класса сбора полей товара."""
```

**Описание**: Инициализирует экземпляр класса `Graber`, устанавливает префикс поставщика и вызывает конструктор родительского класса.

**Параметры**:
- `driver` (Driver): Экземпляр веб-драйвера для взаимодействия с веб-страницами.
- `lang_index` (int): Индекс языка, используемого на сайте.

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
from src.webdriver.driver import Driver
from src.suppliers.kualastyle.graber import Graber

# Пример создания экземпляра класса Graber
driver = Driver()
graber = Graber(driver, 0)
```
```python
 Context.locator_for_decorator = None # <- если будет уастановлено значение - то оно выполнится в декораторе `@close_pop_up`
```
**Описание**: устанавливает значение `Context.locator_for_decorator` в `None`, тем самым отключает выполнение декоратора `@close_pop_up`. Если присвоить  `Context.locator_for_decorator`  значение, то декоратор `@close_pop_up` выполнится.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
from src.webdriver.driver import Driver
from src.suppliers.kualastyle.graber import Graber

# Пример создания экземпляра класса Graber и установки Context.locator_for_decorator
driver = Driver()
graber = Graber(driver, 0)

Context.locator_for_decorator = None # отключаем декоратор
Context.locator_for_decorator = 'locator' # включаем декоратор
```
```python
        self.supplier_prefix = 'kualastyle'
        super().__init__(supplier_prefix=self.supplier_prefix, driver=driver, lang_index=lang_index)
```
**Описание**: устанавливает префикс поставщика `kualastyle` и вызывает конструктор родительского класса.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
from src.webdriver.driver import Driver
from src.suppliers.kualastyle.graber import Graber

# Пример создания экземпляра класса Graber и инициализации родительского класса
driver = Driver()
graber = Graber(driver, 0)
```
```python
    supplier_prefix: str
```
**Описание**: `supplier_prefix` содержит название поставщика, в данном случае `kualastyle`.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
from src.webdriver.driver import Driver
from src.suppliers.kualastyle.graber import Graber

# Пример создания экземпляра класса Graber и доступа к supplier_prefix
driver = Driver()
graber = Graber(driver, 0)
print(graber.supplier_prefix)
```
```python
class Graber(Grbr):
    """Класс для операций захвата Morlevi."""
```
**Описание**:  `Graber` является наследником класса `Grbr`, что позволяет использовать основные методы сбора данных, определенные в родительском классе. При этом `Graber` может переопределять или добавлять методы для адаптации к особенностям конкретного сайта.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
from src.webdriver.driver import Driver
from src.suppliers.kualastyle.graber import Graber

# Пример создания экземпляра класса Graber
driver = Driver()
graber = Graber(driver, 0)
```
```python
from src.logger.logger import logger
```
**Описание**:  импортирует модуль логгера для записи информации о работе программы, включая ошибки, предупреждения и отладочные сообщения.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
from src.logger.logger import logger

# Пример использования логгера для записи информации
logger.info('Starting the process of grabbing data...')
```
```python
from src.webdriver.driver import Driver
```
**Описание**:  импортирует класс `Driver` из модуля `src.webdriver.driver`, который представляет собой абстракцию для управления веб-драйвером (например, Chrome Driver или Firefox Driver).
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
from src.webdriver.driver import Driver

# Пример создания экземпляра класса Driver
driver = Driver()
```
```python
from src.suppliers.graber import Graber as Grbr, Context, close_pop_up
```
**Описание**:  импортирует класс `Graber` (под псевдонимом `Grbr`), класс `Context` и функцию `close_pop_up` из модуля `src.suppliers.graber`.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
from src.suppliers.graber import Graber as Grbr, Context, close_pop_up

# Пример использования импортированных классов и функции
class MyGraber(Grbr):
    pass

Context.locator_for_decorator = None
close_pop_up()
```
```python
from typing import Any
import header
```
**Описание**:  импортирует `Any` из модуля `typing` и модуль `header`.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
from typing import Any
import header

# Пример использования импортированных элементов
def my_function(value: Any):
    print(header.Header())
```
```python
#\n#\n#           DECORATOR TEMPLATE. \n#\n# def close_pop_up(value: Any = None) -> Callable:\n#     """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.\n\n#     Args:\n#         value (Any): Дополнительное значение для декоратора.\n\n#     Returns:\n#         Callable: Декоратор, оборачивающий функцию.\n#     """\n#     def decorator(func: Callable) -> Callable:\n#         @wraps(func)\n#         async def wrapper(*args, **kwargs):\n#             try:\n#                 # await Context.driver.execute_locator(Context.locator.close_pop_up)  # Await async pop-up close  \n#                 ... \n#             except ExecuteLocatorException as e:\n#                 logger.debug(f'Ошибка выполнения локатора: {e}')\n#             return await func(*args, **kwargs)  # Await the main function\n#         return wrapper\n#     return decorator\n#     return decorator
```
**Описание**:  Шаблон декоратора `close_pop_up` предназначен для закрытия всплывающих окон на веб-странице перед выполнением основной логики декорируемой функции.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
#Пример использования декоратора
#@close_pop_up()
#async def my_function():
#    # Основная логика функции
#    pass
```
```python
"""\n.. module:: src.suppliers.kualastyle \n\t:platform: Windows, Unix\n\t:synopsis: Класс собирает значение полей на странице  товара `kualastyle.co.il`. \n    Для каждого поля страницы товара сделана функция обработки поля в родительском классе.\n    Если нужна нестандертная обработка, функция перегружается в этом классе.\n    ------------------\n    Перед отправкой запроса к вебдрайверу можно совершить предварительные действия через декоратор. \n    Декоратор по умолчанию находится в родительском классе. Для того, чтобы декоратор сработал надо передать значение \n    в `Context.locator`, Если надо реализовать свой декоратор - раскоментируйте строки с декоратором и переопределите его поведение\n\n\n"""
```
**Описание**:  Этот блок документации описывает назначение модуля `src.suppliers.kualastyle`, который собирает значения полей на странице товара `kualastyle.co.il`.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
#Пример использования модуля
#from src.suppliers.kualastyle import graber
```
```python
#! .pyenv/bin/python3
```
**Описание**:  Указывает путь к интерпретатору Python3, используемому для запуска скрипта. В данном случае, используется интерпретатор, установленный через `pyenv`.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
#Пример использования пути к интерпретатору
#!/usr/bin/env python3
```
```python
# -*- coding: utf-8 -*-
```
**Описание**:  Указывает кодировку исходного файла как UTF-8. Это необходимо для правильной обработки символов, не входящих в стандартную кодировку ASCII, таких как символы кириллицы.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
#Пример указания кодировки
#coding: utf-8
```
```python
## \\file /src/suppliers/kualastyle/graber.py
```
**Описание**:  Указывает путь к файлу `graber.py` в проекте `hypotez`.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
## \\file /src/suppliers/kualastyle/graber.py
```
```python
from src.logger.logger import logger
```
**Описание**: импортирует модуль логгера для записи информации о работе программы, включая ошибки, предупреждения и отладочные сообщения.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
from src.logger.logger import logger

# Пример использования логгера для записи информации
logger.info('Starting the process of grabbing data...')
```
```python
from src.webdriver.driver import Driver
```
**Описание**: импортирует класс `Driver` из модуля `src.webdriver.driver`, который представляет собой абстракцию для управления веб-драйвером (например, Chrome Driver или Firefox Driver).
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
from src.webdriver.driver import Driver

# Пример создания экземпляра класса Driver
driver = Driver()
```
```python
from src.suppliers.graber import Graber as Grbr, Context, close_pop_up
```
**Описание**: импортирует класс `Graber` (под псевдонимом `Grbr`), класс `Context` и функцию `close_pop_up` из модуля `src.suppliers.graber`.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
from src.suppliers.graber import Graber as Grbr, Context, close_pop_up

# Пример использования импортированных классов и функции
class MyGraber(Grbr):
    pass

Context.locator_for_decorator = None
close_pop_up()
```
```python
from typing import Any
import header
```
**Описание**: импортирует `Any` из модуля `typing` и модуль `header`.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
from typing import Any
import header

# Пример использования импортированных элементов
def my_function(value: Any):
    print(header.Header())
```
```python
#\n#\n#           DECORATOR TEMPLATE. \n#\n# def close_pop_up(value: Any = None) -> Callable:\n#     """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.\n\n#     Args:\n#         value (Any): Дополнительное значение для декоратора.\n\n#     Returns:\n#         Callable: Декоратор, оборачивающий функцию.\n#     """\n#     def decorator(func: Callable) -> Callable:\n#         @wraps(func)\n#         async def wrapper(*args, **kwargs):\n#             try:\n#                 # await Context.driver.execute_locator(Context.locator.close_pop_up)  # Await async pop-up close  \n#                 ... \n#             except ExecuteLocatorException as e:\n#                 logger.debug(f'Ошибка выполнения локатора: {e}')\n#             return await func(*args, **kwargs)  # Await the main function\n#         return wrapper\n#     return decorator\n#     return decorator
```
**Описание**: Шаблон декоратора `close_pop_up` предназначен для закрытия всплывающих окон на веб-странице перед выполнением основной логики декорируемой функции.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
#Пример использования декоратора
#@close_pop_up()
#async def my_function():
#    # Основная логика функции
#    pass
```
```python
"""\n.. module:: src.suppliers.kualastyle \n\t:platform: Windows, Unix\n\t:synopsis: Класс собирает значение полей на странице  товара `kualastyle.co.il`. \n    Для каждого поля страницы товара сделана функция обработки поля в родительском классе.\n    Если нужна нестандертная обработка, функция перегружается в этом классе.\n    ------------------\n    Перед отправкой запроса к вебдрайверу можно совершить предварительные действия через декоратор. \n    Декоратор по умолчанию находится в родительском классе. Для того, чтобы декоратор сработал надо передать значение \n    в `Context.locator`, Если надо реализовать свой декоратор - раскоментируйте строки с декоратором и переопределите его поведение\n\n\n"""
```
**Описание**: Этот блок документации описывает назначение модуля `src.suppliers.kualastyle`, который собирает значения полей на странице товара `kualastyle.co.il`.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
#Пример использования модуля
#from src.suppliers.kualastyle import graber
```
```python
#! .pyenv/bin/python3
```
**Описание**: Указывает путь к интерпретатору Python3, используемому для запуска скрипта. В данном случае, используется интерпретатор, установленный через `pyenv`.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
#Пример использования пути к интерпретатору
#!/usr/bin/env python3
```
```python
# -*- coding: utf-8 -*-
```
**Описание**: Указывает кодировку исходного файла как UTF-8. Это необходимо для правильной обработки символов, не входящих в стандартную кодировку ASCII, таких как символы кириллицы.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
#Пример указания кодировки
#coding: utf-8
```
```python
## \\file /src/suppliers/kualastyle/graber.py
```
**Описание**: Указывает путь к файлу `graber.py` в проекте `hypotez`.
**Параметры**:
- нет

**Возвращает**:
- None

**Вызывает исключения**:
- Не вызывает исключений

**Примеры**:
```python
## \\file /src/suppliers/kualastyle/graber.py