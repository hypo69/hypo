# Модуль для сбора данных о товарах с AliExpress

## Обзор

Модуль предназначен для сбора данных о товарах с веб-сайта AliExpress. Он содержит класс `Graber`, который наследуется от базового класса `src.suppliers.graber.Graber` и предоставляет методы для обработки различных полей товара на странице.

## Подробнее

Этот модуль является частью системы для сбора данных о товарах из различных интернет-магазинов. Класс `Graber` специализируется на сборе информации с AliExpress, адаптируя общие механизмы сбора данных под особенности структуры страниц этого сайта. Модуль использует веб-драйвер для взаимодействия с сайтом и извлечения необходимых данных.

## Классы

### `Graber`

**Описание**: Класс для сбора данных о товарах с AliExpress.

**Наследует**:
- `src.suppliers.graber.Graber`: Базовый класс для сбора данных с сайтов поставщиков.

**Атрибуты**:
- `supplier_prefix` (str): Префикс поставщика, установлен в значение `'aliexpress'`.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Graber`.

#### `__init__`

```python
def __init__(self, driver: Driver, lang_index:int):
    """
    Инициализация класса сбора полей товара.

    :param driver: Экземпляр веб-драйвера для взаимодействия с браузером.
    :type driver: Driver
    """
    self.supplier_prefix = 'aliexpress'
    # вызов конструктора родительского класса
    super().__init__(supplier_prefix=self.supplier_prefix, driver=driver, lang_index=lang_index)

    # устанавливает значение локатора для декоратора в `None`
    # если будет установленно значение - то оно выполнится в декораторе `@close_pop_up`
    Context.locator_for_decorator = None
```

**Назначение**: Инициализация экземпляра класса `Graber`.

**Параметры**:
- `driver` (Driver): Экземпляр веб-драйвера, используемый для взаимодействия с браузером.
- `lang_index` (int): Индекс языка.

**Как работает функция**:
1. Устанавливает атрибут `supplier_prefix` равным `'aliexpress'`, что определяет префикс поставщика для данного грабера.
2. Вызывает конструктор родительского класса `Graber` (`src.suppliers.graber.Graber`) с указанием префикса поставщика и экземпляра веб-драйвера.
3. Устанавливает атрибут `Context.locator_for_decorator` в `None`. Этот атрибут используется декоратором `@close_pop_up` для выполнения действий по закрытию всплывающих окон перед сбором данных.

```
Инициализация Graber
│
├── Установка supplier_prefix = 'aliexpress'
│
├── Вызов конструктора родительского класса Graber
│
└── Установка Context.locator_for_decorator = None
```

**Примеры**:

```python
from src.webdriver.driver import Driver, Chrome
# Пример создания экземпляра класса Graber
driver = Driver(Chrome)
graber = Graber(driver=driver, lang_index=1)
print(graber.supplier_prefix)
# aliexpress