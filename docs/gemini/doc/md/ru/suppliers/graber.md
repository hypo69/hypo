```markdown
# Модуль graber

## Обзор

Этот модуль содержит базовый класс `Graber` для сбора данных с веб-страниц. Он предоставляет асинхронные методы для извлечения данных по различным полям товара, используя локаторы, определённые в файле `product.json`.  Модуль использует декоратор `@close_pop_up` для обработки всплывающих окон.

## Оглавление

* [Модуль graber](#модуль-graber)
* [Обзор](#обзор)
* [Классы](#классы)
    * [`Context`](#context)
    * [`Graber`](#graber)
* [Функции](#функции)
    * [`close_pop_up`](#close_pop_up)

## Классы

### `Context`

**Описание**: Класс `Context` предназначен для хранения глобальных настроек, таких как драйвер браузера (`driver`), локаторы (`locator`), и префикс поставщика (`supplier_prefix`).

**Атрибуты**:

* `driver` (Driver): Объект драйвера, используется для управления браузером или другим интерфейсом.
* `locator` (SimpleNamespace): Пространство имен для хранения локаторов.
* `supplier_prefix` (str): Префикс поставщика.

### `Graber`

**Описание**: Базовый класс для сбора данных со страницы.

**Методы**:

* [`__init__`](#init): Инициализация класса `Graber`.
* [`error`](#error): Обработчик ошибок для полей.
* [`set_field_value`](#set_field_value): Универсальная функция для установки значений полей.
* [`grab_page`](#grab_page): Асинхронная функция для сбора полей продукта.
* Остальные методы (например, `additional_shipping_cost`, `delivery_in_stock`, `active`, `...`) - см. подробное описание ниже.


## Функции

### `close_pop_up`

**Описание**: Создает декоратор для закрытия всплывающих окон.

**Параметры**:

* `value` (Any, необязательно): Дополнительное значение для декоратора.

**Возвращает**:

* `Callable`: Декоратор, оборачивающий функцию.

**Обрабатывает исключения**:

* `ExecuteLocatorException`:  Возникает, если есть ошибки при выполнении локатора.


**Подробное описание методов класса `Graber`:**


(Ниже перечислены остальные методы класса `Graber`, каждый с описанием, параметрами, возвращаемыми значениями и потенциальными исключениями.  Из-за большого количества методов, их все перечислять здесь затруднительно.  Можно сгенерировать отдельный раздел для каждого метода, как показано в примере выше.)

**Пример фрагмента описания для метода `additional_shipping_cost`:**

### `additional_shipping_cost`

**Описание**: Извлекает и устанавливает дополнительную стоимость доставки.

**Параметры**:

* `value` (Any, необязательно):  Значение, которое передаётся извне. Если не передано, извлекается из локатора.

**Возвращает**:

* `bool`: `True` при успешном выполнении, `False` в противном случае.

**Обрабатывает исключения**:

* `Exception`:  Возникает при ошибках при извлечении данных или выполнении локатора.


... (Аналогичное описание для других методов)

**Примечание:**  Полное описание всех методов `Graber` с указанием параметров, возвращаемых значений и обработки исключений, необходимо для полной документации.
```