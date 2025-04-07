# Модуль для проверки локатора закрытия поп-ап окна

## Обзор

Модуль `close_pop_up.py` предназначен для проверки работоспособности локатора закрытия всплывающего окна на сайте поставщика Morlevi. Он использует веб-драйвер для открытия страницы продукта и взаимодействует с ней для закрытия поп-ап окна. Модуль является экспериментальным и служит для отладки и проверки локаторов.

## Подробнее

Этот модуль используется для автоматизированной проверки элементов интерфейса, таких как кнопки закрытия всплывающих окон, на веб-страницах. Он позволяет убедиться, что локаторы, используемые для поиска этих элементов, работают корректно.

## Классы

### `Graber`

**Описание**: Класс `Graber` предназначен для сбора информации о продуктах с сайта Morlevi.

**Наследует**:
- `MorleviGraber`: Класс наследуется от `MorleviGraber`, который, вероятно, содержит общую логику для сбора данных с сайта Morlevi.

**Атрибуты**:
- Отсутствуют в предоставленном коде.

**Методы**:
- Определены в родительском классе `MorleviGraber`.

## Функции

В данном коде функции отсутствуют.

## Как работает код:

1. **Инициализация драйвера**:
   - Создается экземпляр драйвера `Firefox` с использованием класса `Driver` из модуля `src.webdriver.driver`.
   - `driver = Driver(Firefox)`

2. **Инициализация грабера**:
   - Создается экземпляр класса `MorleviGraber`, которому передается драйвер.
   - `graber = MorleviGraber(driver)`

3. **Открытие URL**:
   - Используется метод `get_url` драйвера для открытия страницы продукта на сайте Morlevi.
   - `driver.get_url('https://www.morlevi.co.il/product/19041')`

4. **Получение ID продукта**:
   - ID продукта извлекается с использованием атрибута `id_product` экземпляра `graber`.
   - `product_id = graber.id_product`

5. **Многоточие**:
   - Оставшаяся часть кода не предоставлена.

## Примеры

Пример инициализации и открытия страницы:

```python
from src.webdriver.driver import Driver
from src.webdriver.firefox import Firefox
from src.suppliers.morlevi.graber import Graber as MorleviGraber

driver = Driver(Firefox)
graber = MorleviGraber(driver)
driver.get_url('https://www.morlevi.co.il/product/19041')
product_id = graber.id_product
```

## ASCII flowchart:

```
Driver(Firefox) --> graber = MorleviGraber(driver) --> driver.get_url('https://www.morlevi.co.il/product/19041') --> product_id = graber.id_product