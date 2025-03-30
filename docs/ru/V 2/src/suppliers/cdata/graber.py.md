# Модуль `src.suppliers.cdata.graber`

## Обзор

Модуль `src.suppliers.cdata.graber` предназначен для сбора значений полей со страницы товара на сайте `cdata.co.il`. Он наследует функциональность от родительского класса `Graber` и предоставляет возможность переопределять методы обработки полей для нестандартных случаев. Перед отправкой запроса к веб-драйверу можно выполнять предварительные действия с помощью декоратора, который по умолчанию находится в родительском классе.

## Содержание

1.  [Обзор](#обзор)
2.  [Классы](#классы)
    -   [`Graber`](#graber)
3.  [Функции](#функции)
    -   [close_pop_up](#close_pop_up)

## Классы

### `Graber`

**Описание**: Класс для операций захвата данных с сайта `cdata.co.il`.

**Наследует от**: `src.suppliers.graber.Graber`

**Методы**:

-   `__init__`: Инициализирует класс, устанавливает префикс поставщика и настраивает контекст для декоратора.

#### `__init__`

**Описание**: Инициализация класса `Graber` с заданным драйвером.

**Параметры**:

-   `driver` (`Driver`): Экземпляр веб-драйвера для взаимодействия с браузером.

**Возвращает**:
- None

## Функции

### `close_pop_up`

**Описание**: Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции. 
Декоратор может быть использован для предварительных действий перед взаимодействием с веб-страницей.

**Параметры**:

- `value` (`Any`, optional): Дополнительное значение для декоратора. По умолчанию `None`.

**Возвращает**:
- `Callable`: Декоратор, оборачивающий функцию.

**Пример использования**:
```python
    # from typing import Any, Callable
    # from functools import wraps
    # from src.exceptions.exceptions import ExecuteLocatorException
    # from src.logger.logger import logger
    # from src.suppliers.graber import Context
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