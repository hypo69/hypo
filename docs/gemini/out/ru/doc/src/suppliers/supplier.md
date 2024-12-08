# Модуль `hypotez/src/suppliers/supplier.py`

## Обзор

Модуль `hypotez/src/suppliers/supplier.py` содержит базовый класс `Supplier` для работы с поставщиками данных. Класс используется для инициализации, загрузки настроек, выполнения входа и запуска сценариев для конкретного поставщика.

## Оглавление

- [Модуль `hypotez/src/suppliers/supplier.py`](#модуль-hypotezsrcsupplierssupplierpy)
- [Обзор](#обзор)
- [Класс `Supplier`](#класс-supplier)
- [Функции](#функции)
    - [`Supplier.check_supplier_prefix`](#suppliercheck_supplier_prefix)
    - [`Supplier.__init__`](#supplierinit)
    - [`Supplier._payload`](#supplier_payload)
    - [`Supplier.login`](#supplierlogin)
    - [`Supplier.run_scenario_files`](#supplierrun_scenario_files)
    - [`Supplier.run_scenarios`](#supplierrun_scenarios)


## Класс `Supplier`

**Описание**: Базовый класс для работы с поставщиками данных. Обеспечивает загрузку настроек, выполнение входа и запуск сценариев.

**Атрибуты**:

- `supplier_id` (Optional[int]): Идентификатор поставщика.
- `supplier_prefix` (str): Префикс поставщика (имя модуля).
- `locale` (str): Код локали (по умолчанию 'en').
- `price_rule` (Optional[str]): Правило расчета цен.
- `related_modules` (Optional[ModuleType]): Модуль с функциями, специфичными для данного поставщика.
- `scenario_files` (List[str]): Список файлов сценариев для выполнения.
- `current_scenario` (Dict[str, Any]): Текущий исполняемый сценарий.
- `locators` (Dict[str, Any]): Локаторы для элементов страницы.
- `driver` (Optional[Driver]): Веб-драйвер.


## Функции

### `Supplier.check_supplier_prefix`

**Описание**: Проверка префикса поставщика на пустое значение.

**Параметры**:

- `value` (str): Префикс поставщика.

**Возвращает**:

- str: Префикс поставщика.

**Вызывает исключения**:

- `ValueError`: Если `value` пустое.


### `Supplier.__init__`

**Описание**: Инициализация поставщика, загрузка конфигурации.

**Параметры**:

- `**data` (dict): Словарь с данными для инициализации объекта.

**Вызывает исключения**:

- `DefaultSettingsException`: Если загрузка настроек не удалась.


### `Supplier._payload`

**Описание**: Загрузка параметров поставщика с использованием `j_loads_ns`.

**Параметры**:

-  (нет)

**Возвращает**:

- bool: `True`, если загрузка успешна, иначе `False`.

**Вызывает исключения**:

-  Различные исключения при работе с файлами и загрузкой.


### `Supplier.login`

**Описание**: Выполняет вход на сайт поставщика.

**Параметры**:

- (нет)

**Возвращает**:

- bool: `True`, если вход выполнен успешно, иначе `False`.


### `Supplier.run_scenario_files`

**Описание**: Выполнение одного или нескольких файлов сценариев.

**Параметры**:

- `scenario_files` (Optional[str | List[str]]): Список файлов сценариев. Если не указан, берется из `self.scenario_files`.

**Возвращает**:

- bool: `True`, если все сценарии успешно выполнены, иначе `False`.


### `Supplier.run_scenarios`

**Описание**: Выполнение списка или одного сценария.

**Параметры**:

- `scenarios` (dict | List[dict]): Сценарий или список сценариев для выполнения.

**Возвращает**:

- bool: `True`, если сценарий успешно выполнен, иначе `False`.