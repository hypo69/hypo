# Модуль hypotez/src/suppliers/graber.py

## Обзор

Данный модуль содержит базовый класс `Graber` для сбора данных с веб-страниц поставщиков. Он использует веб-драйвер (класс `Driver`) для извлечения целевых полей (например, название, описание, цена). Локаторы полей определяются через JSON-файлы в директории `locators` каждого поставщика.  Для нестандартной обработки полей товара можно переопределять функции в дочерних классах. Модуль включает в себя декоратор `@close_pop_up` для автоматического закрытия всплывающих окон.

## Декораторы

### `@close_pop_up`

**Описание**: Декоратор `@close_pop_up` предназначен для закрытия всплывающих окон перед выполнением основной логики функции. Он использует метод `execute_locator` класса `Driver` для взаимодействия с браузером.

**Аргументы**:
- `value` (Any): Дополнительное значение, которое может использоваться декоратором (по умолчанию `None`).

**Возвращает**:
- `Callable`: Декоратор, оборачивающий функцию.


## Классы

### `Context`

**Описание**: Класс `Context` хранит глобальные настройки, включая драйвер (`driver`), локаторы (`locator`) и префикс поставщика (`supplier_prefix`).

**Атрибуты**:
- `driver` (Driver): Объект драйвера браузера.
- `locator` (SimpleNamespace): Пространство имен для локаторов.
- `supplier_prefix` (str): Префикс поставщика.


### `Graber`

**Описание**: Базовый класс для сбора данных с веб-страницы.

**Методы**:

#### `__init__(self, supplier_prefix: str, driver: Driver)`

**Описание**: Инициализирует экземпляр класса `Graber`.

**Аргументы**:
- `supplier_prefix` (str): Префикс поставщика.
- `driver` (Driver): Экземпляр класса `Driver`.

#### `error(self, field: str)`

**Описание**: Обработчик ошибок для полей.

**Аргументы**:
- `field` (str): Название поля.

#### `set_field_value(self, value: Any, locator_func: Callable[[], Any], field_name: str, default: Any = '')`

**Описание**: Универсальная функция для установки значений полей с обработкой ошибок.

**Аргументы**:
- `value` (Any): Значение для установки.
- `locator_func` (Callable[[], Any]): Функция для получения значения из локатора.
- `field_name` (str): Название поля.
- `default` (Any): Значение по умолчанию (по умолчанию пустая строка).

**Возвращает**:
- `Any`: Установленное значение.


#### `grab_page(self) -> ProductFields`

**Описание**: Асинхронная функция для сбора полей продукта.

**Возвращает**:
- `ProductFields`: Собранные поля продукта.


#### `{методы с именами id_product, name, ...}`

**Описание**: Функции для получения значений конкретных полей данных.  Каждая функция принимает аргумент `value`, который может быть передан в вызывающую функцию для задания значения поля напрямую. В противном случае значение извлекается из локатора.  Они обрабатывают исключения `ExecuteLocatorException`.  Все эти методы имеют @close_pop_up декоратор.


**Аргументы**:
- `value` (Any): Значение поля, которое может быть передано в функцию для установки напрямую. (по умолчанию `None`).

**Возвращает**:
- `Any`: Возвращает `True` при успешном выполнении, или неявное `None` при ошибке.

**Возможные исключения**:
- `ExecuteLocatorException`: Возникает при проблемах с выполнением локатора.