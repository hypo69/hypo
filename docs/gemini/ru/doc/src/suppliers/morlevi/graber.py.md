# Модуль `graber`

## Обзор

Модуль `graber` представляет собой класс `Graber`, предназначенный для сбора информации о товарах с сайта `morlevi.co.il`. Он наследуется от базового класса `Graber` (Grbr) и переопределяет некоторые методы для обработки специфических полей на странице товара. Модуль использует веб-драйвер для взаимодействия с сайтом и извлечения необходимых данных.

## Подорбней

Этот модуль является частью системы сбора данных о товарах с различных сайтов. Он специализируется на сайте `morlevi.co.il` и предоставляет функциональность для извлечения информации о товарах, такой как наименование, описание, цена и изображения.
Класс `Graber` переопределяет методы родительского класса для адаптации к структуре и особенностям сайта `morlevi.co.il`. Это позволяет обрабатывать поля, требующие нестандартного подхода.

## Классы

### `Graber`

**Описание**: Класс для операций захвата данных с сайта Morlevi. Наследуется от класса `Graber` (Grbr).

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Graber`.

**Параметры**:
- `driver` (Driver): Экземпляр веб-драйвера для взаимодействия с сайтом.
- `lang_index` (int): Индекс языка, используемого на сайте.

**Примеры**

```python
from src.webdriver.driver import Driver
from src.suppliers.morlevi.graber import Graber

# Пример создания экземпляра класса Graber
driver = Driver()
lang_index = 0
graber = Graber(driver, lang_index)
```

## Функции

### `__init__`

```python
    def __init__(self, driver: Driver, lang_index:int):
        """Инициализация класса сбора полей товара."""
        super().__init__(supplier_prefix=self.supplier_prefix, driver=driver, lang_index=lang_index)
        Context.locator_for_decorator = self.locator.close_pop_up
```

**Описание**: Инициализирует класс `Graber`, вызывая конструктор родительского класса и устанавливая локатор для декоратора.

**Параметры**:
- `driver` (Driver): Экземпляр веб-драйвера для взаимодействия с сайтом.
- `lang_index` (int): Индекс языка, используемого на сайте.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: В случае ошибок при инициализации родительского класса.

**Примеры**:

```python
from src.webdriver.driver import Driver
from src.suppliers.morlevi.graber import Graber

# Пример создания экземпляра класса Graber
driver = Driver()
lang_index = 0
graber = Graber(driver, lang_index)