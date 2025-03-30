# Модуль: src.suppliers.aliexpress.graber

## Обзор

Модуль предназначен для сбора данных о товарах с веб-сайта AliExpress. Он содержит класс `Graber`, который наследуется от базового класса `src.suppliers.graber.Graber` и предоставляет методы для обработки различных полей товара на странице AliExpress.

## Подробнее

Этот модуль является частью системы для сбора и обработки данных о товарах из различных источников. Класс `Graber` специализируется на сборе данных именно с AliExpress. Он использует веб-драйвер для взаимодействия с сайтом и извлечения необходимой информации. Модуль также включает в себя функциональность для обработки всплывающих окон и других элементов интерфейса, которые могут мешать сбору данных.

## Классы

### `Graber`

**Описание**:
Класс для сбора данных о товарах с AliExpress.

**Методы**:
- `__init__`: Инициализирует класс `Graber`, вызывая конструктор родительского класса `Graber` и устанавливая префикс поставщика.

**Параметры**:
- `supplier_prefix` (str): Префикс поставщика (aliexpress).

**Примеры**
```python
from src.webdriver.driver import Driver
from src.suppliers.aliexpress.graber import Graber

# Пример создания экземпляра класса Graber
driver = Driver()
graber = Graber(driver=driver, lang_index=1)

# Теперь можно использовать методы класса Graber для сбора данных о товарах с AliExpress
```

## Функции

### `close_pop_up`

```python
def close_pop_up(value: Any = None) -> Callable:
    """
    Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.
    
    :param value: Дополнительное значение для декоратора.
    :type value: Any
    :return: Декоратор, оборачивающий функцию.
    :rtype: Callable
    
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                # проверяет наличие локатора для закрытия всплывающего окна
                if Context.locator_for_decorator and Context.locator_for_decorator.close_pop_up:
                     # исполняет локатор закрытия всплывающего окна
                    await Context.driver.execute_locator(Context.locator_for_decorator.close_pop_up) 
                ...
            except ExecuteLocatorException as ex:
                # логирует ошибку выполнения локатора
                logger.debug(f'Ошибка выполнения локатора: ', ex)
            # ожидает выполнения основной функции
            return await func(*args, **kwargs)  
        return wrapper
    return decorator
```

**Описание**:
Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

**Параметры**:
- `value` (Any, optional): Дополнительное значение для декоратора. По умолчанию `None`.

**Возвращает**:
- `Callable`: Декоратор, оборачивающий функцию.

**Вызывает исключения**:
- `ExecuteLocatorException`: Возникает, если не удается выполнить локатор для закрытия всплывающего окна.

**Примеры**:
```python
from src.suppliers.aliexpress.graber import close_pop_up

# Пример использования декоратора для закрытия всплывающих окон
@close_pop_up()
async def my_function():
    # Основная логика функции
    pass