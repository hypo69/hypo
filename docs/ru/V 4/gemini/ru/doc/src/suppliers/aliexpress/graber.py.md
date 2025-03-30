# Модуль `graber` для AliExpress

## Обзор

Модуль `graber` предназначен для сбора данных о товарах с AliExpress. Он содержит класс `Graber`, который наследуется от базового класса `src.suppliers.graber.Graber` и предоставляет методы для обработки полей товара на веб-странице AliExpress.

## Подробнее

Этот модуль является частью системы для сбора и обработки данных о товарах от различных поставщиков. Он специализируется на сборе информации с AliExpress. Класс `Graber` предоставляет возможность переопределять методы обработки полей товара, если требуется нестандартная логика. Также поддерживается выполнение предварительных действий перед отправкой запроса к веб-драйверу с использованием декораторов.

## Классы

### `Graber`

**Описание**: Класс для сбора данных о товарах с AliExpress.

**Наследует от**: `src.suppliers.graber.Graber`

**Параметры**:
- `supplier_prefix` (str): Префикс поставщика (aliexpress).

**Методы**:

- `__init__(self, driver: Driver, lang_index: int)`: Инициализация класса `Graber`.

  **Описание**: Инициализирует экземпляр класса `Graber`, устанавливает префикс поставщика и вызывает конструктор родительского класса.

  **Параметры**:
    - `driver` (Driver): Экземпляр веб-драйвера для взаимодействия с браузером.
    - `lang_index` (int): Индекс языка.

  **Пример**:
    ```python
    from src.webdriver.driver import Driver
    driver_instance = Driver()
    graber = Graber(driver=driver_instance, lang_index=0)
    ```

## Функции
### `close_pop_up`
   ```python
    # def close_pop_up(value: Any = None) -> Callable:
    #     """
    #     Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.
        
    #     :param value: Дополнительное значение для декоратора.\n
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

**Описание**: Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.
   **Параметры**:
    - `value` (Any): Дополнительное значение для декоратора.
   **Возвращает**:
    - `Callable`: Декоратор, оборачивающий функцию.
   **Вызывает исключения**:
    - `ExecuteLocatorException`:  Возникает, если не удается выполнить локатор.
   **Примеры**:
   ```python
    from src.webdriver.driver import Driver
    from functools import wraps
    
    def test_func(driver):
        @wraps(driver)
        async def wrapper(*args, **kwargs):
            return await driver(*args, **kwargs)  
        return wrapper
   ```