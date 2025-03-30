# Документация модуля graber.py

## Обзор

Модуль `graber.py` предназначен для сбора данных о товарах с веб-сайта `morlevi.co.il`. Он расширяет функциональность базового класса `Graber`, предоставляя специализированные методы для обработки полей товаров Morlevi.

## Подробнее

Этот модуль является частью системы сбора данных о товарах с различных поставщиков. Он использует веб-драйвер для взаимодействия с веб-страницей и извлекает необходимую информацию о товаре. Для каждого поля товара предусмотрена функция обработки, которая может быть переопределена для нестандартной обработки.

## Классы

### `Graber`

**Описание**: Класс для операций захвата данных с сайта Morlevi.

**Методы**:
- `__init__`: Инициализация класса.

**Параметры**:
- `supplier_prefix` (str): Префикс поставщика (в данном случае 'morlevi').
- `driver` (Driver): Экземпляр веб-драйвера.
- `lang_index` (int): Индекс языка.

**Примеры**:

```python
from src.webdriver.driver import Driver

# Пример создания экземпляра класса Graber
driver = Driver()  # Инициализация веб-драйвера
graber = Graber(driver=driver, lang_index=0)
```

## Функции

### `__init__`

```python
    def __init__(self, driver: Driver, lang_index:int):
        """Инициализация класса сбора полей товара."""
        super().__init__(supplier_prefix=self.supplier_prefix, driver=driver, lang_index=lang_index)
        Context.locator_for_decorator = self.locator.close_pop_up
```

**Описание**: Инициализирует класс `Graber` для сбора полей товара.

**Параметры**:
- `driver` (Driver): Экземпляр веб-драйвера, используемый для взаимодействия с веб-страницей.
- `lang_index` (int): Индекс языка, используемый при сборе данных.

**Возвращает**:
- `None`

**Примеры**:

```python
from src.webdriver.driver import Driver
from src.suppliers.morlevi.graber import Graber

# Пример создания и инициализации экземпляра класса Graber
driver = Driver()  # Инициализация веб-драйвера
graber = Graber(driver=driver, lang_index=0)
```