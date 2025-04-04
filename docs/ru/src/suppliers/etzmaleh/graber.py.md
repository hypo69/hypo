# Модуль для сбора данных с сайта etzmaleh.co.il

## Обзор

Модуль `graber.py` предназначен для сбора данных о товарах с сайта `etzmaleh.co.il`. Он содержит класс `Graber`, который наследуется от класса `Graber` (Grbr) из модуля `src.suppliers.graber`. Класс `Graber` переопределяет некоторые методы родительского класса для обработки специфичных полей и элементов на страницах товаров `etzmaleh.co.il`.

## Подробней

Этот модуль является частью системы сбора данных о товарах от различных поставщиков. Он использует веб-драйвер для навигации по сайту и извлечения необходимой информации. Модуль также включает в себя механизм для обработки всплывающих окон и других интерактивных элементов, которые могут мешать сбору данных.

## Классы

### `Graber`

**Описание**: Класс `Graber` предназначен для захвата данных с сайта `etzmaleh.co.il`.

**Наследует**:
- `Graber` (Grbr) из модуля `src.suppliers.graber`

**Атрибуты**:
- `supplier_prefix` (str): Префикс поставщика, используемый для идентификации поставщика в системе.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Graber`.

#### `__init__`

```python
def __init__(self, driver: Driver, lang_index):
    """Инициализация класса сбора полей товара.

    Args:
        driver (Driver): Экземпляр веб-драйвера для управления браузером.
        lang_index: Индекс языка, используемый для локализации.

    Returns:
        None

    """
```

**Назначение**: Инициализирует класс `Graber`, устанавливает префикс поставщика и вызывает конструктор родительского класса.

**Параметры**:
- `driver` (Driver): Экземпляр веб-драйвера, используемый для взаимодействия с сайтом.
- `lang_index`: Индекс языка для локализации.

**Как работает функция**:
1. Устанавливает атрибут `supplier_prefix` равным `'etzmaleh'`.
2. Вызывает конструктор родительского класса `Graber` (Grbr) с передачей `supplier_prefix`, `driver` и `lang_index`.
3. Устанавливает `Context.locator_for_decorator` в `None`.

```
A: Установка supplier_prefix = 'etzmaleh'
|
B: Вызов Graber.__init__()
|
C: Установка Context.locator_for_decorator = None
```

**Примеры**:
```python
from src.webdriver.driver import Driver
from src.webdriver import Firefox
driver = Driver(Firefox)
graber = Graber(driver, 0)