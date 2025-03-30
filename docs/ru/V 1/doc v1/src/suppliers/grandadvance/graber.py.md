# Модуль `graber.py`

## Обзор

Модуль `graber.py` предназначен для сбора информации о товарах с сайта `grandadvanse.co.il`. Он содержит класс `Graber`, который наследуется от базового класса `Graber` (`Grbr`) и переопределяет методы для обработки специфичных полей товаров на этом сайте. Модуль использует конфигурационные файлы и локаторы для определения элементов страницы и выполняет нестандартную обработку полей, если это необходимо.

## Подорбней

Модуль предназначен для извлечения данных о товарах с сайта `grandadvanse.co.il`. Он использует веб-драйвер для взаимодействия со страницей и извлекает необходимые данные, такие как название, описание, цена и другие характеристики товара. Для каждого поля товара создается функция обработки, которая может быть переопределена в классе `Graber` для нестандартной обработки.

Перед отправкой запроса к веб-драйверу можно выполнить предварительные действия с помощью декоратора. Декоратор по умолчанию находится в родительском классе. Чтобы декоратор сработал, необходимо передать значение в `Context.locator`. Если требуется реализовать свой декоратор, нужно раскомментировать соответствующие строки и переопределить его поведение.

## Классы

### `Graber`

**Описание**: Класс `Graber` наследуется от класса `Graber` (`Grbr`) и предназначен для сбора информации о товарах с сайта `grandadvanse.co.il`. Он содержит методы для обработки полей товаров и использует конфигурационные файлы и локаторы для определения элементов страницы.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `Graber`.

**Параметры**:
- `driver` (Driver): Экземпляр веб-драйвера для взаимодействия со страницей.
- `lang_index` (int): Индекс языка.

**Примеры**
```python
from src.webdriver.driver import Driver
from src.suppliers.grandadvance.graber import Graber

# Пример создания экземпляра класса Graber
driver = Driver()
graber = Graber(driver, 0)
```

## Функции

### `__init__`

```python
def __init__(self, driver: Driver, lang_index:int):
    """Класс населедутет Graber. 
    все поля 
    товара устана
   вливвв модуле `src.supplier."""
    config:SimpleNamespace = j_loads_ns(gs.path.src / 'suppliers' / ENDPOINT / f'{ENDPOINT}.json')
    locator: SimpleNamespace = j_loads_ns(gs.path.src / 'suppliers' / ENDPOINT / 'locators' / 'product.json')
    super().__init__(supplier_prefix=ENDPOINT, driver=driver, lang_index=lang_index)
    Context.locator_for_decorator = locator.click_to_specifications # <- if locator not definded decorator 
```

**Описание**: Инициализирует экземпляр класса `Graber`, загружает конфигурационные файлы и устанавливает локаторы для взаимодействия с элементами страницы.

**Параметры**:
- `driver` (Driver): Экземпляр веб-драйвера для взаимодействия со страницей.
- `lang_index` (int): Индекс языка.

**Возвращает**:
- `None`

**Примеры**:
```python
from src.webdriver.driver import Driver
from src.suppliers.grandadvance.graber import Graber

driver = Driver()
graber = Graber(driver, 0)
```