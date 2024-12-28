# Модуль `graber.py`

## Обзор

Модуль `graber.py` предназначен для сбора данных о товарах с сайта `gearbest.com`. Он предоставляет класс `Graber`, который наследуется от родительского класса `Graber` и переопределяет некоторые его методы для специфической обработки полей товаров на сайте Gearbest.

## Содержание

1. [Импорты](#импорты)
2. [Константы](#константы)
3. [Декоратор](#декоратор)
4. [Класс `Graber`](#класс-graber)
    - [Метод `__init__`](#__init__)

## Импорты

```python
from typing import Any
import header
from src.suppliers.graber import Graber as Grbr, Context, close_pop_up
from src.webdriver.driver import Driver
from src.logger.logger import logger
```

Импортируются необходимые модули и классы для работы с веб-драйвером, контекстом, логированием и общими классами для сбора данных.

## Константы

```python

```
Константа `MODE` устанавливает режим работы (в данном случае, `dev`).

## Декоратор

### `close_pop_up`
```python
# def close_pop_up(value: Any = None) -> Callable:
#     """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

#     Args:
#         value (Any): Дополнительное значение для декоратора.

#     Returns:
#         Callable: Декоратор, оборачивающий функцию.
#     """
#     def decorator(func: Callable) -> Callable:
#         @wraps(func)
#         async def wrapper(*args, **kwargs):
#             try:
#                 # await Context.driver.execute_locator(Context.locator.close_pop_up)  # Await async pop-up close  
#                 ... 
#             except ExecuteLocatorException as e:
#                 logger.debug(f'Ошибка выполнения локатора: {e}')
#             return await func(*args, **kwargs)  # Await the main function
#         return wrapper
#     return decorator
```

**Описание**:

Декоратор предназначен для закрытия всплывающих окон перед выполнением основной логики функции. Он оборачивает функцию и выполняет действия по закрытию всплывающего окна, если это необходимо. Декоратор по умолчанию отключен. Чтобы использовать его, раскомментируйте код и переопределите логику внутри блока `try`.

**Параметры**:
-   `value` (Any, optional): Дополнительное значение для декоратора.

**Возвращает**:
- `Callable`: Декоратор, оборачивающий функцию.

## Класс `Graber`

### Описание

```python
class Graber(Grbr):
    """Класс для операций захвата Morlevi."""
    supplier_prefix: str
```
Класс `Graber` предназначен для сбора данных о товарах с сайта Gearbest. Он наследует функциональность от класса `Graber` (импортированного как `Grbr`) и добавляет специфическую логику для работы с Gearbest.

### Метод `__init__`

```python
    def __init__(self, driver: Driver):
        """Инициализация класса сбора полей товара."""
        self.supplier_prefix = 'etzmaleh'
        super().__init__(supplier_prefix=self.supplier_prefix, driver=driver)
        # Устанавливаем глобальные настройки через Context
        
        Context.locator_for_decorator = None # <- если будет уастановлено значение - то оно выполнится в декораторе `@close_pop_up`
```

**Описание**:
Инициализирует экземпляр класса `Graber`. Устанавливает префикс поставщика, вызывает конструктор родительского класса и настраивает контекст для работы с декоратором.

**Параметры**:
- `driver` (Driver): Экземпляр класса `Driver` для управления веб-драйвером.