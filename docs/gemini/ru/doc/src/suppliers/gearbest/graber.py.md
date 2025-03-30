# Модуль src.suppliers.gearbest.graber

## Обзор

Модуль `src.suppliers.gearbest.graber` предназначен для сбора данных о товарах с сайта `gearbest.com`. Он содержит класс `Graber`, который наследуется от родительского класса `Graber` (Grbr) и переопределяет некоторые его методы для обработки специфических полей товаров на сайте `gearbest.com`. Модуль использует декораторы для выполнения предварительных действий перед отправкой запроса к веб-драйверу.

## Подробнее

Этот модуль является частью системы для сбора и обработки данных о товарах из различных онлайн-магазинов. Он специализируется на сборе информации с сайта `gearbest.com`. Класс `Graber` содержит методы для обработки различных полей на странице товара. Если стандартные методы обработки, предоставляемые родительским классом, не подходят, они переопределяются в этом классе.

## Классы

### `Graber`

**Описание**: Класс `Graber` предназначен для сбора данных о товарах с сайта `gearbest.com`. Он наследуется от класса `Graber` (Grbr) и переопределяет некоторые его методы для обработки специфических полей товаров на сайте `gearbest.com`.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Graber`.

**Параметры**:
- `driver` (Driver): Экземпляр веб-драйвера для взаимодействия с сайтом.
- `lang_index` (int): Индекс языка.

**Примеры**
```python
from src.webdriver.driver import Driver
from src.suppliers.gearbest.graber import Graber

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

**Описание**: Функция `close_pop_up` создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

**Параметры**:
- `value` (Any, optional): Дополнительное значение для декоратора. По умолчанию `None`.

**Возвращает**:
- `Callable`: Декоратор, оборачивающий функцию.

**Примеры**:
```python
from typing import Callable, Any
from functools import wraps

def close_pop_up(value: Any = None) -> Callable:
    """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                # await Context.driver.execute_locator(Context.locator.close_pop_up)  # Await async pop-up close  
                ... 
            except ExecuteLocatorException as ex:
                logger.debug(f'Ошибка выполнения локатора: {ex}')
            return await func(*args, **kwargs)  # Await the main function
        return wrapper
    return decorator