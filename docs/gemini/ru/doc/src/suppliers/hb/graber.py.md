# Модуль для сбора данных о товарах с сайта hb.co.il

## Обзор

Модуль `graber.py` предназначен для извлечения информации о товарах с сайта `hb.co.il`. Он наследует функциональность от базового класса `Graber` и переопределяет методы для обработки специфических полей и элементов на страницах товаров этого поставщика. Модуль использует веб-драйвер для взаимодействия с сайтом и сбора данных.

## Подробней

Основная задача модуля - автоматизировать процесс сбора данных о товарах, представленных на сайте `hb.co.il`. Он специализируется на обработке структуры и элементов этого конкретного сайта, что позволяет эффективно извлекать нужную информацию.

## Классы

### `Graber`

**Описание**: Класс `Graber` предназначен для операций захвата данных с сайта `hb.co.il`.

**Принцип работы**:
Класс наследует от `Graber` (который, как предполагается, является общим классом для граберов) и специализируется на логике сбора данных с сайта `hb.co.il`. Он инициализирует префикс поставщика и использует декоратор для выполнения предварительных действий перед запросом к веб-драйверу, таких как закрытие всплывающих окон.

- Устанавливает префикс поставщика `hb` для идентификации.
- Инициализирует класс `Graber` из `src.suppliers.graber`.
- Устанавливает глобальные настройки через `Context`.
- Позволяет выполнять предварительные действия через декоратор, если установлено значение `Context.locator_for_decorator`.

**Атрибуты**:

- `supplier_prefix` (str): Префикс поставщика, устанавливается как `'hb'`.

**Методы**:

- `__init__(self, driver: Driver, lang_index)`: Инициализация класса сбора полей товара.

   **Параметры**:
   - `driver` (Driver): Экземпляр веб-драйвера для взаимодействия с сайтом.
   - `lang_index` (int): Индекс языка, используемого на сайте.

   **Как работает функция**:
   1. Устанавливает префикс поставщика (`supplier_prefix`) в значение `'hb'`.
   2. Вызывает конструктор родительского класса `Graber` (`Grbr`) с указанием префикса поставщика, драйвера и индекса языка.
   3. Устанавливает атрибут `Context.locator_for_decorator` в `None`. Если установить значение, декоратор `@close_pop_up` выполнит его.

   ```ascii
   Инициализация
   │
   ├─── Установка префикса поставщика: supplier_prefix = 'hb'
   │
   ├─── Инициализация родительского класса Graber
   │
   └─── Установка locator_for_decorator: Context.locator_for_decorator = None
   ```

   **Примеры**:

   ```python
   from src.webdriver.driver import Driver
   from src.webdriver.firefox import Firefox

   driver = Driver(Firefox)
   graber = Graber(driver=driver, lang_index=0)
   print(graber.supplier_prefix)  # Вывод: hb
   ```

## Функции

### `close_pop_up`
```python
def close_pop_up(value: Any = None): # -> Callable:
    """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

    Args:
        value (Any): Дополнительное значение для декоратора.

    Returns:
        Callable: Декоратор, оборачивающий функцию.
    """
    def decorator(func): # -> Callable:
        """Декоратор."""
        def wrapper(*args, **kwargs):
            """Обертка для декоратора."""
            try:
                # await Context.driver.execute_locator(Context.locator.close_pop_up)  # Await async pop-up close  
                ...
            except ExecuteLocatorException as ex:
                logger.debug(f'Ошибка выполнения локатора: {ex}')
            return func(*args, **kwargs)  # Await the main function
        return wrapper
    return decorator
```
    **Назначение**: Функция `close_pop_up` создает декоратор, который пытается закрыть всплывающее окно перед выполнением основной функции.

    **Параметры**:
    - `value` (Any, optional): Дополнительное значение, которое можно передать декоратору. По умолчанию `None`.

    **Возвращает**:
    - `Callable`: Декоратор, который оборачивает функцию.

    **Вызывает исключения**:
    - `ExecuteLocatorException`: Возникает, если не удается выполнить локатор для закрытия всплывающего окна.

    **Внутренние функции**:

    ### `decorator`

    ```python
    def decorator(func): # -> Callable:
        """Декоратор."""
        def wrapper(*args, **kwargs):
            """Обертка для декоратора."""
            try:
                # await Context.driver.execute_locator(Context.locator.close_pop_up)  # Await async pop-up close  
                ...
            except ExecuteLocatorException as ex:
                logger.debug(f'Ошибка выполнения локатора: {ex}')
            return func(*args, **kwargs)  # Await the main function
        return wrapper
    return decorator
    ```
        **Назначение**: Функция `decorator` является фабрикой декораторов. Она принимает функцию `func` и возвращает новую функцию (`wrapper`), которая оборачивает исходную функцию.

        **Параметры**:
        - `func` (Callable): Функция, которую нужно обернуть.

        **Возвращает**:
        - `Callable`: Функция `wrapper`, которая оборачивает исходную функцию.

        **Внутренние функции**:

        ### `wrapper`

        ```python
        def wrapper(*args, **kwargs):
            """Обертка для декоратора."""
            try:
                # await Context.driver.execute_locator(Context.locator.close_pop_up)  # Await async pop-up close  
                ...
            except ExecuteLocatorException as ex:
                logger.debug(f'Ошибка выполнения локатора: {ex}')
            return func(*args, **kwargs)  # Await the main function
        return wrapper
        ```
            **Назначение**: Функция `wrapper` является оберткой для исходной функции. Она выполняет попытку закрытия всплывающего окна перед вызовом исходной функции и обрабатывает возможные исключения.

            **Параметры**:
            - `*args`: Позиционные аргументы, переданные в исходную функцию.
            - `**kwargs`: Именованные аргументы, переданные в исходную функцию.

            **Возвращает**:
            - Результат вызова исходной функции.

            **Вызывает исключения**:
            - `ExecuteLocatorException`: Возникает, если не удается выполнить локатор для закрытия всплывающего окна.

            **Как работает функция**:

            1. Пытается выполнить локатор для закрытия всплывающего окна, используя `Context.driver.execute_locator(Context.locator.close_pop_up)`.
            2. Если возникает исключение `ExecuteLocatorException`, логирует ошибку.
            3. Вызывает исходную функцию `func` с переданными аргументами и возвращает результат.

            ```ascii
            Начало wrapper
            │
            ├─── Попытка закрытия всплывающего окна
            │   │
            │   └─── ExecuteLocatorException: Логирование ошибки
            │
            └─── Вызов исходной функции func
                 │
                 └─── Возврат результата
            ```

    **Как работает функция**:

    1. Определяет функцию `decorator`, которая принимает функцию `func` в качестве аргумента.
    2. Внутри `decorator` определяется функция `wrapper`, которая выполняет действия до и после вызова `func`.
    3. Функция `wrapper` пытается закрыть всплывающее окно с помощью `Context.driver.execute_locator`.
    4. Если закрытие всплывающего окна вызывает исключение, оно перехватывается и логируется.
    5. Функция `wrapper` вызывает исходную функцию `func` и возвращает результат её выполнения.
    6. Функция `decorator` возвращает функцию `wrapper`.
    7. Функция `close_pop_up` возвращает функцию `decorator`.

    ```ascii
    close_pop_up
    │
    ├─── Определение decorator(func)
    │   │
    │   └─── Определение wrapper(*args, **kwargs)
    │       │
    │       ├─── Попытка закрытия всплывающего окна
    │       │   │
    │       │   └─── ExecuteLocatorException: Логирование ошибки
    │       │
    │       └─── Вызов func(*args, **kwargs)
    │            │
    │            └─── Возврат результата
    │
    └─── Возврат decorator
    ```

    **Примеры**:

    ```python
    from src.logger.logger import logger
    from typing import Callable, Any

    class Context:
        class locator:
            close_pop_up = {"selector": "//button[@class='close']", "by": "xpath"}
        driver = None

    class ExecuteLocatorException(Exception):
        pass

    def close_pop_up(value: Any = None) -> Callable:
        """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции."""
        def decorator(func: Callable) -> Callable:
            """Декоратор."""
            def wrapper(*args: Any, **kwargs: Any) -> Any:
                """Обертка для декоратора."""
                try:
                    logger.info('Закрываем всплывающее окно')
                    # Context.driver.execute_locator(Context.locator.close_pop_up)  # Await async pop-up close
                    ...
                except ExecuteLocatorException as ex:
                    logger.debug(f'Ошибка выполнения локатора: {ex}')
                return func(*args, **kwargs)  # Await the main function
            return wrapper
        return decorator

    @close_pop_up()
    def my_function():
        """Функция, к которой применяется декоратор."""
        logger.info("Выполнение основной функции")
        return "Hello, world!"

    result = my_function()
    print(result)