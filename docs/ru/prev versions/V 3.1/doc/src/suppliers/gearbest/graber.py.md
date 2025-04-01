# Модуль `graber.py`

## Обзор

Модуль `graber.py` предназначен для сбора данных о товарах с сайта `gearbest.com`. Он содержит класс `Graber`, который наследует функциональность от родительского класса `Graber` (обозначенного как `Grbr`) из модуля `src.suppliers.graber`. Основная задача класса `Graber` — извлечение и обработка полей товаров на страницах `gearbest.com`.

## Подробней

Этот модуль является частью системы сбора данных о товарах из различных источников для проекта `hypotez`. Он специализируется на парсинге страниц товаров `gearbest.com`. Для нестандартной обработки полей товаров, функции обработки, унаследованные от родительского класса, могут быть перегружены.

Перед отправкой запросов к веб-драйверу, модуль позволяет выполнять предварительные действия с использованием декоратора. Декоратор по умолчанию находится в родительском классе. Для активации декоратора необходимо передать значение в `Context.locator`. Если требуется специфическое поведение, можно переопределить декоратор.

## Классы

### `Graber`

**Описание**: Класс `Graber` предназначен для извлечения информации о товарах с сайта `gearbest.com`. Он наследуется от класса `Graber` (обозначенного как `Grbr`) из модуля `src.suppliers.graber` и переопределяет некоторые его методы для адаптации к структуре данных `gearbest.com`.

**Методы**:

- `__init__`: Инициализирует экземпляр класса `Graber`, устанавливая префикс поставщика и вызывая конструктор родительского класса.

**Параметры**:

- `driver` (Driver): Экземпляр веб-драйвера, используемый для взаимодействия с веб-страницей.
- `lang_index` (int): Индекс языка, используемый для локализации контента.

**Примеры**:

```python
from src.webdriver.driver import Driver
from src.suppliers.gearbest.graber import Graber

# Пример инициализации класса Graber
driver = Driver()
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
    ...
```

**Описание**: Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

**Параметры**:

- `value` (Any, optional): Дополнительное значение для декоратора. По умолчанию `None`.

**Возвращает**:

- `Callable`: Декоратор, оборачивающий функцию.

**Примеры**:

```python
from typing import Any, Callable
from functools import wraps
from src.logger.logger import logger
from src.webdriver.driver import Driver
from src.suppliers.gearbest.graber import Graber, Context
from src.exceptions.exceptions import ExecuteLocatorException

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
                print('Имитация закрытия всплывающего окна')
            except ExecuteLocatorException as ex:
                logger.debug(f'Ошибка выполнения локатора: {ex}')
            return await func(*args, **kwargs)  # Await the main function
        return wrapper
    return decorator

# Пример использования декоратора
@close_pop_up()
async def some_function():
    print("Функция выполнена после закрытия всплывающего окна")

# Пример вызова функции
# import asyncio
# asyncio.run(some_function())