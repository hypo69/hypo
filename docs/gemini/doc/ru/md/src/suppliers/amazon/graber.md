# Модуль hypotez/src/suppliers/amazon/graber.py

## Обзор

Модуль `graber.py` предоставляет класс `Graber`, предназначенный для сбора данных о товарах с сайта amazon.com. Класс наследуется от базового класса `Grbr` и реализует функции для извлечения различных полей товара.  Предусмотрены декораторы для обработки всплывающих окон перед выполнением основного функционала.  Класс `Graber` включает функции для извлечения множества полей, таких как наименование, описание, цена, изображения и т.д.

## Оглавление

* [Модуль `graber.py`](#модуль-graberpy)
* [Класс `Graber`](#класс-graber)
    * [`grab_page`](#grab_page)
    * [Другие методы](#другие-методы)

## Класс `Graber`

**Описание**: Класс `Graber` отвечает за сбор данных о товарах с amazon.com. Он расширяет функциональность родительского класса `Grbr`, предоставляя специализированные методы для извлечения данных с этой платформы.


**Атрибуты**:

* `supplier_prefix`: Строка, определяющая префикс поставщика.


**Методы**:

### `__init__`

**Описание**: Конструктор класса `Graber`.

**Параметры**:

* `driver` (`Driver`): Экземпляр класса `Driver` для работы с веб-драйвером.

**Возвращает**:
    - Не имеет возвращаемого значения.


### `grab_page`

**Описание**: Асинхронная функция для сбора полей товара.

**Параметры**:

* `driver` (`Driver`): Экземпляр класса `Driver` для работы с веб-драйвером.

**Возвращает**:
    - `ProductFields`: Объект, содержащий собранные поля товара.

**Вызывает исключения**:
    - Возможные исключения, связанные с выполнением асинхронных операций или сбоем сбора данных.

### Другие методы

Класс `Graber` содержит ряд методов, реализующих логику сбора отдельных полей товара, такие как: `id_product`, `additional_shipping_cost`, `delivery_in_stock`, и т.д. (Полный список методов приведен в исходном коде). Каждый метод отвечает за извлечение конкретного поля и имеет соответствующую документацию, включая описание параметров, возвращаемых значений и потенциальных исключений.  Важно обратить внимание, что большинство этих методов вызываются асинхронно.