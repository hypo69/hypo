# Модуль hypotez/src/suppliers/morlevi/graber.py

## Обзор

Модуль `hypotez/src/suppliers/morlevi/graber.py` содержит класс `Graber`, предназначенный для сбора данных со страницы товара на сайте `morlevi.co.il`. Класс наследуется от базового класса `Grbr` из `src.suppliers.graber` и предоставляет методы для обработки конкретных полей товара.  Он поддерживает предварительные действия перед запросом к веб-драйверу через декоратор `close_pop_up`.

## Классы

### `Graber`

**Описание**:  Класс `Graber` отвечает за сбор данных с сайта `morlevi.co.il`.  Он содержит методы для обработки различных полей товара, в том числе для загрузки и сохранения изображений.  Переопределяет методы из базового класса для специфических потребностей сайта.

**Атрибуты**:

- `supplier_prefix`: Префикс для идентификации поставщика.

**Методы**:

#### `__init__(self, driver: Driver)`

**Описание**: Инициализирует класс `Graber`.

**Параметры**:

- `driver (Driver)`: Объект веб-драйвера.

#### `local_saved_image(self, value: Any = None)`

**Описание**: Загружает и сохраняет изображение товара локально.

**Параметры**:

- `value (Any, optional):` Дополнительное значение, которое может быть передано в словаре kwargs при вызове функции `grab_product_page`. Если `value` передан, он подставляется в поле `ProductFields.local_saved_image`. По умолчанию `None`.

**Возвращает**:

- `bool`: `True`, если изображение успешно сохранено, `False` в противном случае.


**Обрабатывает исключения**:

- `Exception`:  Любые ошибки при работе с веб-драйвером или сохранении изображения.  Подробная информация об ошибке выводится в лог.


## Функции

(Здесь будут функции, если они присутствуют в файле.  В данном случае нет функций, кроме методов класса `Graber`.)


## Модули

- `header`
- `gs`
- `src.suppliers.graber`
- `src.webdriver.driver`
- `src.utils.image`
- `src.logger`


## Константы

- `MODE`: Значение переменной `MODE` (по умолчанию 'dev').