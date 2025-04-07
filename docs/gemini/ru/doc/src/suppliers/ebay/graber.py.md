# Модуль для сбора данных с сайта eBay
=================================================

Модуль `src.suppliers.ebay.graber` предназначен для сбора информации о товарах с сайта `ebay.com`. Он содержит класс `Graber`, который наследует функциональность от родительского класса `Graber` (Grbr) и переопределяет некоторые методы для специфической обработки данных с eBay.

## Обзор

Модуль предоставляет класс `Graber`, который специализируется на извлечении информации о товарах с сайта eBay. Он использует веб-драйвер для навигации по страницам товаров и извлечения необходимых данных.
Модуль определяет логику для сбора данных, специфичную для структуры страниц eBay.

## Подробней

Этот модуль является частью системы сбора данных о товарах с различных онлайн-платформ. Он расширяет базовый класс `Graber` для адаптации к особенностям структуры HTML и логики работы сайта eBay. Это позволяет эффективно извлекать информацию о товарах, такую как названия, описания, цены и другие характеристики, необходимые для дальнейшей обработки и анализа.

## Классы

### `Graber`

**Описание**: Класс `Graber` предназначен для сбора данных о товарах с сайта eBay. Он наследует функциональность от базового класса `Graber` (Grbr) и адаптирует ее для работы с eBay.

**Наследует**:
- `Grbr` (src.suppliers.graber.Graber): Базовый класс для сбора данных с сайтов-поставщиков.

**Атрибуты**:
- `supplier_prefix` (str): Префикс поставщика, установлен в `'ebay'`.

**Методы**:
- `__init__(driver: Driver, lang_index)`: Инициализирует экземпляр класса `Graber`, устанавливает префикс поставщика и вызывает конструктор родительского класса.
-  `close_pop_up(value: Any = None)`: Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

#### `__init__`

```python
def __init__(self, driver: Driver, lang_index):
    """Инициализация класса сбора полей товара."""
    ...
```

**Назначение**: Инициализирует класс `Graber`, устанавливая префикс поставщика и вызывая конструктор родительского класса.

**Параметры**:
- `driver` (Driver): Экземпляр веб-драйвера для управления браузером.
- `lang_index` (int): Индекс языка, используемый при сборе данных.

**Как работает функция**:

1. Устанавливает атрибут `supplier_prefix` равным `'ebay'`.
2. Вызывает конструктор родительского класса `Grbr` с установленным префиксом поставщика, драйвером и индексом языка.
3. Устанавливает атрибут `Context.locator_for_decorator` в `None`. Это необходимо для работы декоратора `@close_pop_up`, который будет выполняться, только если установлено значение `Context.locator_for_decorator`.

```
Инициализация класса
│
├── Установка supplier_prefix = 'ebay'
│
├── Вызов Grbr.__init__(..., driver, lang_index)
│
└── Установка Context.locator_for_decorator = None
```

**Примеры**:
```python
from src.webdriver.driver import Driver, Chrome
from src.suppliers.ebay.graber import Graber

driver = Driver(Chrome)
graber = Graber(driver, 0)
print(graber.supplier_prefix)  # Вывод: ebay
```
#### `close_pop_up`

```python
def close_pop_up(value: Any = None):
    """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции."""
    ...
```

**Назначение**: Создает декоратор, предназначенный для закрытия всплывающих окон, которые могут появляться на странице перед выполнением основной логики функции сбора данных.

**Параметры**:
- `value` (Any, optional): Дополнительное значение, которое можно передать декоратору. По умолчанию `None`.

**Возвращает**:
- `Callable`: Декоратор, который оборачивает функцию.

**Как работает функция**:

1.  Определяет внутреннюю функцию `decorator`, которая принимает функцию `func` в качестве аргумента.
2.  Внутри `decorator` определяется функция `wrapper`, которая выполняет следующие действия:
    *   Пытается выполнить локатор `Context.locator.close_pop_up` с помощью `Context.driver.execute_locator()`, чтобы закрыть всплывающее окно.
    *   Обрабатывает исключение `ExecuteLocatorException`, которое может возникнуть, если локатор не найден или не может быть выполнен.
    *   Вызывает исходную функцию `func` с переданными аргументами и возвращает результат её выполнения.
3.  Возвращает функцию `decorator`.

```
Создание декоратора close_pop_up
│
├── Определение внутренней функции decorator(func)
│   │
│   ├── Определение внутренней функции wrapper(*args, **kwargs)
│   │   │
│   │   ├── Попытка закрытия всплывающего окна через Context.driver.execute_locator(Context.locator.close_pop_up)
│   │   │   │
│   │   │   └── Обработка исключения ExecuteLocatorException (если возникнет)
│   │   │
│   │   └── Вызов исходной функции func(*args, **kwargs)
│   │
│   └── Возврат wrapper
│
└── Возврат decorator
```

**Примеры**:

```python
from typing import Callable, Any
from functools import wraps
from src.webdriver.driver import Driver, Chrome
from src.suppliers.ebay.graber import Graber
from src.logger.logger import logger

# Модуль для логирования
# logger.info('Some information message')
# ...
# except SomeError as ex:
# logger.error('Some error message', ex, exc_info = True), где ошибка передается вторым аргументом. exc_info определает надо ли выводить служебную информацию.

class Context:
    driver = None
    locator = None
    locator_for_decorator = None


class ExecuteLocatorException(Exception):
    pass


def close_pop_up(value: Any = None) -> Callable:
    """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                # await Context.driver.execute_locator(Context.locator.close_pop_up)  # Await async pop-up close
                print('Выполняется закрытие всплывающего окна')
            except ExecuteLocatorException as ex:
                logger.debug(f'Ошибка выполнения локатора: {ex}')
            result = await func(*args, **kwargs)  # Await the main function
            return result

        return wrapper

    return decorator


async def my_function(arg1: str) -> str:
    """Пример функции, оборачиваемой декоратором."""
    print(f"Выполняется my_function с аргументом: {arg1}")
    return f"Результат: {arg1}"


async def main():
    Context.driver = Driver(Chrome)  # Инициализация драйвера
    Context.locator = type('Locator', (object,), {'close_pop_up': 'locator_value'})()

    decorated_function = close_pop_up()(my_function)  # Оборачиваем функцию декоратором
    result = await decorated_function("test_argument")  # Вызываем обернутую функцию
    print(f"Результат выполнения: {result}")


# Запуск примера
import asyncio

# asyncio.run(main())
```
## Переменные

- `supplier_prefix` (str): Префикс поставщика, используемый для идентификации eBay.
- `Context.locator_for_decorator` (Any): Локатор для выполнения в декораторе `@close_pop_up`. Если установлено значение, декоратор будет выполнен.