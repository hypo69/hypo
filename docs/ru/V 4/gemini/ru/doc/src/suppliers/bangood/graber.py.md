# Модуль `src.suppliers.bangood.graber`

## Обзор

Модуль `src.suppliers.bangood.graber` предназначен для сбора данных о товарах с сайта `bangood.com`. Он содержит класс `Graber`, который наследуется от родительского класса `Graber` (Grbr) и переопределяет некоторые его методы для обработки специфичных полей товаров на сайте `bangood.com`. Модуль использует декораторы для выполнения предварительных действий перед отправкой запроса к веб-драйверу, таких как закрытие всплывающих окон.

## Подробней

Этот модуль является частью системы сбора данных о товарах с различных онлайн-платформ. Он специализируется на парсинге данных с сайта `bangood.com`. Основная задача модуля - извлечение информации о товарах, такой как название, цена, описание и другие характеристики, и приведение этой информации к унифицированному формату для дальнейшей обработки и анализа. Класс `Graber` содержит логику для взаимодействия с веб-драйвером, навигации по страницам товаров и извлечения необходимых данных.

## Классы

### `Graber`

**Описание**:
Класс `Graber` предназначен для сбора данных о товарах с сайта `bangood.com`. Он наследуется от класса `Graber` (Grbr) и переопределяет его методы для обработки специфичных полей товаров на сайте `bangood.com`.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Graber`.

**Параметры**:
- `driver` (Driver): Экземпляр веб-драйвера для взаимодействия с сайтом `bangood.com`.
- `lang_index` (int): Индекс языка, используемого на сайте.

**Примеры**:
```python
from src.webdriver.driver import Driver
from src.suppliers.bangood.graber import Graber

# Пример создания экземпляра класса Graber
driver = Driver()
graber = Graber(driver, lang_index=0)
```

## Функции

### `close_pop_up`

```python
# def close_pop_up(value: Any = None) -> Callable:
#     """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

#     Args:
#         value (Any): Дополнительное значение для декоратора.

#     Returns:
#         Callable: Декоратор, оборачивающий функцию.
#     """
```

**Описание**:
Декоратор `close_pop_up` предназначен для закрытия всплывающих окон на сайте `bangood.com` перед выполнением основной логики функции сбора данных о товаре. Он позволяет избежать проблем, связанных с перекрытием элементов страницы всплывающими окнами.

**Параметры**:
- `value` (Any, optional): Дополнительное значение, которое может быть передано декоратору. По умолчанию `None`.

**Возвращает**:
- `Callable`: Декоратор, который оборачивает функцию.

**Вызывает исключения**:
- `ExecuteLocatorException`: Если возникает ошибка при выполнении локатора для закрытия всплывающего окна.

**Примеры**:
```python
from typing import Any, Callable, wraps
from src.logger.logger import logger
# from src.webdriver.driver import ExecuteLocatorException
from src.suppliers.graber import Context

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
                ...
            except Exception as ex:
                logger.debug(f'Ошибка выполнения локатора: {ex}')
            return await func(*args, **kwargs)  # Await the main function
        return wrapper
    return decorator

@close_pop_up()
async def get_product_data():
    """Функция сбора данных о товаре."""
    ...