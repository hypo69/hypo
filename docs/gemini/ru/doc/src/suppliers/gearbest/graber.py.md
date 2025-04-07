# Модуль для сбора данных с сайта Gearbest
## Обзор

Модуль `graber.py` предназначен для сбора данных о товарах с сайта `gearbest.com`. Он содержит класс `Graber`, который наследуется от базового класса `Graber` (`Grbr`) и переопределяет некоторые его методы для специфической обработки данных с сайта Gearbest. Модуль использует веб-драйвер для взаимодействия с сайтом и библиотеку `logger` для логирования.

## Подорбней
Этот модуль является частью системы сбора данных о товарах с различных интернет-магазинов, используемой в проекте `hypotez`. Он предназначен для автоматизированного извлечения информации о товарах с сайта `gearbest.com` и дальнейшей обработки этих данных.
Основная задача класса `Graber` - предоставить специализированные методы для извлечения данных с учетом структуры и особенностей сайта `gearbest.com`.
Модуль использует декораторы для предварительной обработки запросов к веб-драйверу, например, для закрытия всплывающих окон.

## Классы

### `Graber`

**Описание**: Класс `Graber` предназначен для сбора информации о товарах с сайта `gearbest.com`. Он наследуется от класса `Graber` (`Grbr`) из модуля `src.suppliers.graber` и переопределяет некоторые его методы для адаптации к структуре сайта Gearbest.

**Принцип работы**:
Класс инициализируется с использованием веб-драйвера и индекса языка. Он устанавливает префикс поставщика (`supplier_prefix`) как `'etzmaleh'` и вызывает конструктор родительского класса. Также класс позволяет устанавливать глобальные настройки через `Context`, включая локатор для декоратора `@close_pop_up`.

**Наследует**:

- `Graber` (`Grbr`) из модуля `src.suppliers.graber`.

**Аттрибуты**:

-   `supplier_prefix` (str): Префикс поставщика, используемый в классе.

**Методы**:

-   `__init__`: Инициализация класса `Graber`.

### `__init__`

```python
def __init__(self, driver: Driver, lang_index):
    """Инициализация класса сбора полей товара."""
```

**Назначение**: Инициализирует экземпляр класса `Graber`, устанавливая префикс поставщика и вызывая конструктор родительского класса.

**Параметры**:

-   `driver` (Driver): Экземпляр веб-драйвера для управления браузером.
-   `lang_index` (int): Индекс языка для выбора локализации сайта.

**Возвращает**:

-   None

**Как работает функция**:

1. Устанавливает атрибут `supplier_prefix` равным `'etzmaleh'`.
2. Вызывает конструктор родительского класса (`Grbr`) с параметрами `supplier_prefix`, `driver` и `lang_index`.
3. Устанавливает атрибут `Context.locator_for_decorator` равным `None`.

```
A: Установка supplier_prefix = 'etzmaleh'
|
B: Вызов конструктора родительского класса Grbr
|
C: Установка Context.locator_for_decorator = None
```

**Примеры**:

```python
from src.webdriver.driver import Driver, Firefox

# Пример создания экземпляра класса Graber
driver = Driver(Firefox)
graber = Graber(driver, lang_index=0)
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

**Назначение**: Функция `close_pop_up` создает декоратор, который закрывает всплывающие окна перед выполнением основной логики функции.

**Параметры**:

-   `value` (Any, optional): Дополнительное значение для декоратора. По умолчанию `None`.

**Возвращает**:

-   `Callable`: Декоратор, который оборачивает функцию.

**Внутренние функции**:

### `decorator`

```python
def decorator(func: Callable) -> Callable:
    """Декоратор, оборачивающий функцию."""
```

**Назначение**: Функция `decorator` является декоратором, который оборачивает функцию для выполнения дополнительной логики.

**Параметры**:

-   `func` (Callable): Функция, которую нужно обернуть.

**Возвращает**:

-   `Callable`: Обернутая функция.

### `wrapper`

```python
async def wrapper(*args, **kwargs):
    """Обертка для выполнения закрытия всплывающих окон и основной функции."""
```

**Назначение**: Функция `wrapper` является оберткой для выполнения логики закрытия всплывающих окон и основной функции.

**Параметры**:

-   `*args`: Позиционные аргументы, передаваемые в функцию.
-   `**kwargs`: Именованные аргументы, передаваемые в функцию.

**Возвращает**:

-   `Any`: Результат выполнения основной функции.

**Как работает функция**:

1.  Пытается закрыть всплывающее окно, используя `Context.driver.execute_locator(Context.locator.close_pop_up)`.
2.  Ловит исключение `ExecuteLocatorException` и логирует его как отладочное сообщение.
3.  Выполняет основную функцию `func` с переданными аргументами.
4.  Возвращает результат выполнения основной функции.

```
A: Попытка закрытия всплывающего окна с помощью Context.driver.execute_locator
|
B: Если возникла ошибка ExecuteLocatorException, логирование ошибки
|
C: Выполнение основной функции func
|
D: Возврат результата выполнения основной функции
```

**Примеры**:

```python
from typing import Callable, Any

# Пример использования декоратора close_pop_up
@close_pop_up()
async def my_function():
    """Моя функция."""
    return "Hello, world!"
```
```python
from typing import Callable, Any
from src.webdriver.driver import Driver
from src.webdriver.exceptions import ExecuteLocatorException
from src.logger.logger import logger
from functools import wraps


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
            try:
                # await Context.driver.execute_locator(Context.locator.close_pop_up)  # Await async pop-up close
                print("Закрытие всплывающего окна")
                ...
            except ExecuteLocatorException as ex:
                logger.debug(f'Ошибка выполнения локатора: {ex}')
            result = await func(*args, **kwargs)  # Await the main function
            return result
        return wrapper
    return decorator


async def some_function():
    """Некая функция"""
    print("Некая функция")

@close_pop_up()
async def main():
    """
    Пример использования декоратора close_pop_up
    """
    driver = Driver(driver_type='Chrome')
    try:
        # await driver.get("https://www.example.com")  # Замените на реальный URL
        await some_function()
    finally:
        driver.quit()

# Запуск примера
# asyncio.run(main()) #TODO