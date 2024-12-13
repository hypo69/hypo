# Модуль `aliexpress.graber`

## Обзор

Модуль `aliexpress.graber` предназначен для сбора данных о товарах с веб-сайта AliExpress. Он содержит класс `Graber`, который наследуется от базового класса `src.suppliers.graber.Graber` и предоставляет методы для обработки различных полей товара на странице.

## Содержание

- [Обзор](#обзор)
- [Классы](#классы)
    - [`Graber`](#graber)
- [Декоратор](#декоратор)

## Классы

### `Graber`

**Описание**: Класс для сбора данных о товарах с AliExpress.

Наследует функциональность от `src.suppliers.graber.Graber` и предоставляет методы для обработки полей товара.

**Переменные класса**:
- `supplier_prefix` (str): Префикс поставщика (aliexpress).

**Методы**:

#### `__init__`

**Описание**: Инициализация класса сбора полей товара.

**Параметры**:
- `driver` (Driver): Экземпляр веб-драйвера для взаимодействия с браузером.

## Декоратор
```python
# def close_pop_up(value: Any = None) -> Callable:
#     """
#     Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.
    
#     :param value: Дополнительное значение для декоратора.
#     :type value: Any
#     :return: Декоратор, оборачивающий функцию.
#     :rtype: Callable
    
#     """
#     def decorator(func: Callable) -> Callable:
#         @wraps(func)
#         async def wrapper(*args, **kwargs):
#             try:
#                 # проверяет наличие локатора для закрытия всплывающего окна
#                 if Context.locator_for_decorator and Context.locator_for_decorator.close_pop_up:
#                      # исполняет локатор закрытия всплывающего окна
#                     await Context.driver.execute_locator(Context.locator_for_decorator.close_pop_up) 
#                 ...
#             except ExecuteLocatorException as ex:
#                 # логирует ошибку выполнения локатора
#                 logger.debug(f'Ошибка выполнения локатора: ', ex)
#             # ожидает выполнения основной функции
#             return await func(*args, **kwargs)  
#         return wrapper
#     return decorator
```
**Описание**:
Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

**Параметры**:
    - `value` (Any, optional): Дополнительное значение для декоратора. По умолчанию `None`.

**Возвращает**:
    - `Callable`: Декоратор, оборачивающий функцию.