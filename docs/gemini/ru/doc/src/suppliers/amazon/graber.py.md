# Модуль `graber`

## Обзор

Модуль `graber` предназначен для сбора данных о товарах с сайта `amazon.com`. Он содержит класс `Graber`, который наследуется от класса `Graber` (Grbr) из модуля `src.suppliers.graber`. Класс `Graber` переопределяет методы родительского класса для нестандартной обработки полей на странице товара `amazon.com`.

## Подробней

Этот модуль предоставляет инструменты для автоматизированного извлечения информации о товарах с сайта `amazon.com`. Он использует веб-драйвер для взаимодействия с веб-страницей и извлекает необходимые данные, такие как название, описание, цена и другие характеристики товара. Модуль также включает декоратор `@close_pop_up`, который позволяет закрывать всплывающие окна перед выполнением основной логики функции.

## Классы

### `Graber`

**Описание**: Класс для операций захвата данных с сайта `amazon.com`.

**Методы**:
- `__init__`: Инициализирует класс `Graber`.

#### `__init__`

```python
def __init__(self, driver: Driver, lang_index:int):
    """Инициализация класса сбора полей товара."""
```

**Описание**: Инициализирует класс `Graber`, устанавливает префикс поставщика и вызывает конструктор родительского класса.

**Параметры**:
- `driver` (Driver): Экземпляр веб-драйвера для взаимодействия с веб-страницей.
- `lang_index` (int): Индекс языка.

**Примеры**:

```python
from src.webdriver.driver import Driver
driver = Driver()
graber = Graber(driver, 0)