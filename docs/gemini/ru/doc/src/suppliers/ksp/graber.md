# Модуль hypotez/src/suppliers/ksp/graber.py

## Обзор

Модуль `graber.py` содержит класс `Graber`, предназначенный для сбора данных с сайта `ksp.co.il`. Класс наследуется от базового класса `Grbr` из модуля `src.suppliers.graber`.  Он предоставляет методы для обработки полей данных на странице товара, а также может переопределять стандартные методы обработки для нестандартных случаев.  В классе реализована возможность предварительного выполнения действий (например, закрытие всплывающих окон) через декоратор.  Модуль использует библиотеки `jjson`, `logger`, и `gs` для обработки данных и логгирования.

## Классы

### `Graber`

**Описание**:  Класс для сбора данных с сайта `ksp.co.il`.

**Атрибуты**:

- `supplier_prefix`: Строка, представляющая префикс поставщика (`ksp`).


**Методы**:

- `__init__`: Инициализирует объект `Graber`.
    ```python
    def __init__(self, driver: 'Driver'):
        """Инициализация класса сбора полей товара.

        Args:
            driver ('Driver'): Объект веб-драйвера.
        """
        self.supplier_prefix = 'ksp'
        super().__init__(supplier_prefix=self.supplier_prefix, driver=driver)

        if '/mob/' in self.driver.current_url:
            self.locator = j_loads_ns(gs.path.src / 'suppliers' / 'ksp' / 'locators' / 'product_mobile_site.json')
            logger.info("Установлены локаторы для мобильной версии сайта KSP")
            ...
        Context.locator_for_decorator = None
    ```

## Функции


### `close_pop_up` (Закомментирована в файле)

**Описание**: Декоратор для закрытия всплывающих окон.

**Параметры**:

- `value (Any, optional)`: Дополнительное значение для декоратора (по умолчанию `None`).

**Возвращает**:
- `Callable`: Декоратор для функции.

**Вызывает исключения**:

- `ExecuteLocatorException`: Если возникает ошибка при выполнении локатора.

```python
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
            except ExecuteLocatorException as e:
                logger.debug(f'Ошибка выполнения локатора: {e}')
            return await func(*args, **kwargs)  # Await the main function
        return wrapper
    return decorator
```


**Примечание**: Код декоратора `close_pop_up` закомментирован в исходном файле.  В документации он представлен для полноты, но в рабочем коде его использование не требуется.


## Глобальные переменные и объекты

### `MODE`

**Описание**: Глобальная переменная, хранящая режим работы (например, 'dev').

### `Context` (Закомментирован в файле)

**Описание**:  Класс `Context` (закомментирован в файле) используется для хранения глобальных настроек.  В комментариях к коду есть примеры, как это можно реализовать.


## Использование

В данном модуле определен класс `Graber`, который можно использовать для сбора данных с сайта.  Он наследуется от `Grbr` и предоставляет переопределяемые методы для обработки полей, а также механизм предварительной обработки через декоратор `close_pop_up`.  Этот модуль интегрируется с другими частями проекта через импорты библиотек (`header`, `gs`, `src.suppliers.graber`, `src.utils.jjson`, `src.logger.logger`).