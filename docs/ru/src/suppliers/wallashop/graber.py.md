# Модуль `graber.py`

## Обзор

Модуль `graber.py` предназначен для сбора информации о товарах с сайта `wallashop.co.il`. Он содержит класс `Graber`, который наследует функциональность класса `Graber` из модуля `src.suppliers.graber`. Модуль обеспечивает стандартизированный способ извлечения данных о товарах, позволяя переопределять методы обработки полей для нестандартных случаев.

## Подробней

Этот модуль является частью системы сбора данных о товарах из различных онлайн-магазинов. Он специализируется на сборе данных с сайта `wallashop.co.il`. Основная задача модуля - предоставить гибкий и расширяемый способ извлечения информации о товарах, учитывая особенности структуры данных конкретного сайта.

## Классы

### `Graber`

**Описание**: Класс `Graber` предназначен для захвата данных о товарах с сайта `wallashop.co.il`. Он наследует функциональность класса `Graber` из модуля `src.suppliers.graber` и предоставляет возможность переопределения методов для обработки нестандартных полей.

**Наследует**:
- `Graber` (из `src.suppliers.graber`): Обеспечивает базовую функциональность для сбора данных о товарах с веб-страниц.

**Аттрибуты**:
- `supplier_prefix` (str): Префикс поставщика, устанавливается в значение `'wallashop'`.
- `driver` (Driver): Инстанс веб-драйвера для взаимодействия с веб-страницей.
- `lang_index` (int): Индекс языка для локализации.

**Методы**:
- `__init__`: Инициализирует класс `Graber`, устанавливает префикс поставщика и вызывает конструктор родительского класса.
- `close_pop_up`: Декоратор для закрытия всплывающих окон.

### `__init__`

```python
def __init__(self, driver: Driver, lang_index:int):
    """Инициализация класса сбора полей товара."""
    self.supplier_prefix = 'wallashop'
    super().__init__(supplier_prefix=self.supplier_prefix, driver=driver, lang_index=lang_index)

    # Закрыватель поп ап `@close_pop_up`
    Context.locator_for_decorator = None # <- если будет уастановлено значение - то оно выполнится в декораторе `@close_pop_up`
```

**Назначение**: Инициализирует экземпляр класса `Graber`.

**Параметры**:
- `driver` (Driver): Инстанс веб-драйвера для управления браузером.
- `lang_index` (int): Индекс языка, используемый для локализации контента.

**Как работает функция**:
1. Устанавливает атрибут `supplier_prefix` в значение `'wallashop'`, который идентифицирует поставщика.
2. Вызывает конструктор родительского класса `Graber` (из `src.suppliers.graber`) с указанием префикса поставщика, драйвера и индекса языка. Это позволяет инициализировать общие параметры и настройки для сбора данных.
3. Инициализирует `Context.locator_for_decorator` значением `None`. Если установить значение для `Context.locator_for_decorator` то декоратор `@close_pop_up` выполнится

**Примеры**:
```python
from src.webdriver.driver import Driver
from src.webdriver import Firefox
driver = Driver(Firefox)
graber = Graber(driver=driver, lang_index=0)
```

## Функции

### `close_pop_up`

```python
from src.suppliers.graber import close_pop_up
```

**Назначение**: Декоратор, предназначенный для закрытия всплывающих окон на веб-странице перед выполнением основной функции сбора данных.

**Параметры**:
- Отсутствуют, так как это декоратор.

**Как работает функция**:
1. Если `Context.locator_for_decorator` имеет значение, декоратор пытается закрыть всплывающее окно, используя локатор, хранящийся в `Context.locator_for_decorator`.
2. Если `Context.locator_for_decorator` не имеет значения, декоратор не выполняет никаких действий и сразу переходит к выполнению обернутой функции.

**Примеры**:
```python
from src.suppliers.graber import close_pop_up
class Graber(Grbr):
    supplier_prefix: str

    def __init__(self, driver: Driver, lang_index:int):
        """Инициализация класса сбора полей товара."""
        self.supplier_prefix = 'wallashop'
        super().__init__(supplier_prefix=self.supplier_prefix, driver=driver, lang_index=lang_index)

        # Закрыватель поп ап `@close_pop_up`
        Context.locator_for_decorator = None # <- если будет уастановлено значение - то оно выполнится в декораторе `@close_pop_up`