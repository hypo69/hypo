# Модуль `graber.py`

## Обзор

Модуль `graber.py` предназначен для сбора данных о товарах с сайта `wallashop.co.il`. Он содержит класс `Graber`, который наследует функциональность от родительского класса `Graber` (`Grbr`). Класс `Graber` переопределяет методы родительского класса для нестандартной обработки полей, специфичных для сайта `wallashop.co.il`.

## Подробней

Этот модуль является частью системы сбора данных о товарах от различных поставщиков (`suppliers`) в проекте `hypotez`. Он использует веб-драйвер для взаимодействия с сайтом `wallashop.co.il` и извлечения необходимой информации.

Основная задача класса `Graber` — определить и реализовать логику извлечения данных, специфичную для `wallashop.co.il`, используя общую структуру, заданную в родительском классе `Graber` (`Grbr`).

## Классы

### `Graber`

**Описание**: Класс `Graber` предназначен для операций сбора данных с сайта `wallashop.co.il`.

**Наследует**:
- `Graber` (`Grbr`) из модуля `src.suppliers.graber`: Определяет общую структуру и функциональность для сбора данных с сайтов поставщиков.

**Атрибуты**:
- `supplier_prefix` (str): Префикс поставщика, установлен в `'wallashop'`.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Graber`.

### `__init__`

```python
def __init__(self, driver: Driver, lang_index:int):
    """Инициализация класса сбора полей товара."""
    self.supplier_prefix = 'wallashop'
    super().__init__(supplier_prefix=self.supplier_prefix, driver=driver, lang_index=lang_index)

    # Закрыватель поп ап `@close_pop_up`
    Context.locator_for_decorator = None # <- если будет уастановлено значение - то оно выполнится в декораторе `@close_pop_up`
```

**Назначение**: Инициализация экземпляра класса `Graber`.

**Параметры**:
- `driver` (Driver): Экземпляр класса `Driver` из модуля `src.webdriver.driver`, используемый для управления веб-драйвером.
- `lang_index` (int): Индекс языка, используемый для локализации.

**Как работает функция**:

1.  Устанавливает атрибут `supplier_prefix` равным `'wallashop'`.
2.  Вызывает конструктор родительского класса `Graber` (`Grbr`) с параметрами `supplier_prefix`, `driver` и `lang_index`.
3.  Устанавливает атрибут `Context.locator_for_decorator` в `None`. Это необходимо для работы декоратора `@close_pop_up`.

```
Инициализация экземпляра класса Graber
│
├── Установка значения атрибута supplier_prefix = 'wallashop'
│
├── Вызов конструктора родительского класса Graber (Grbr)
│
└── Установка значения атрибута Context.locator_for_decorator = None
```

**Примеры**:

```python
from src.webdriver.driver import Driver
from src.webdriver import Firefox

driver = Driver(Firefox)
graber = Graber(driver=driver, lang_index=0)