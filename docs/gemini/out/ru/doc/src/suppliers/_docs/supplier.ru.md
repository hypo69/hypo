# Класс `Supplier`

## Обзор

Данный класс представляет собой базовый класс для работы с поставщиками данных. Он предоставляет общие методы и атрибуты для взаимодействия с различными поставщиками (например, Amazon, AliExpress, Walmart), обеспечивая структурированный и переиспользуемый подход к работе с данными.

## Оглавление

- [Классы](#классы)
- [Функции](#функции)
- [Атрибуты](#атрибуты)
- [Методы](#методы)
- [Пример использования](#пример-использования)
- [Визуальное представление](#визуальное-представление)


## Атрибуты

### `supplier_id`

**Описание**: Уникальный идентификатор поставщика.

**Тип**: `str`


### `supplier_prefix`

**Описание**: Префикс для поставщика, например, `aliexpress` или `amazon`.

**Тип**: `str`


### `supplier_settings`

**Описание**: Настройки для поставщика, загруженные из файла конфигурации.

**Тип**: `dict`


### `locale`

**Описание**: Код локализации (например, `en` для английского, `ru` для русского).

**Тип**: `str`


### `price_rule`

**Описание**: Правило для расчета цены (например, добавление НДС или скидки).

**Тип**: `Callable`


### `related_modules`

**Описание**: Модуль, содержащий специфические для поставщика функции.

**Тип**: `module`


### `scenario_files`

**Описание**: Список файлов сценариев, которые должны быть выполнены.

**Тип**: `List[str]`


### `current_scenario`

**Описание**: Текущий сценарий выполнения.

**Тип**: `str`


### `login_data`

**Описание**: Данные для входа на сайт поставщика (если требуется).

**Тип**: `dict`


### `locators`

**Описание**: Локаторы для веб-элементов на страницах сайта поставщика.

**Тип**: `dict`


### `driver`

**Описание**: Веб-драйвер для взаимодействия с сайтом поставщика.

**Тип**: `WebDriver`


### `parsing_method`

**Описание**: Метод парсинга данных (например, `webdriver`, `api`, `xls`, `csv`).

**Тип**: `str`


## Методы

### `__init__`

**Описание**: Конструктор класса, инициализирующий атрибуты на основе префикса поставщика и других параметров.

**Параметры**:
- `supplier_prefix` (str): Префикс поставщика.
- `locale` (str, optional): Код локализации. По умолчанию 'en'.
- `webdriver` (str | WebDriver | bool, optional): Веб-драйвер. По умолчанию 'default'.
- `*attrs`: Дополнительные атрибуты.
- `**kwargs`: Дополнительные ключевые аргументы.


### `_payload`

**Описание**: Загружает настройки поставщика, конфигурационные файлы и инициализирует веб-драйвер.

**Параметры**:
- `webdriver` (str | WebDriver | bool): Веб-драйвер.


**Возвращает**:
- `bool`: True, если загрузка успешна, иначе False.


### `login`

**Описание**: Метод для выполнения входа на сайт поставщика (если требуется).

**Возвращает**:
- `bool`: True, если вход успешен, иначе False.


### `run_scenario_files`

**Описание**: Запускает выполнение файлов сценариев.

**Параметры**:
- `scenario_files` (str | List[str], optional): Файлы сценариев. По умолчанию `None`.


**Возвращает**:
- `bool`: True, если сценарии выполнены, иначе False.


### `run_scenarios`

**Описание**: Запускает один или несколько сценариев.

**Параметры**:
- `scenarios` (dict | list[dict]): Сценарии для выполнения.


**Возвращает**:
- `bool`: True, если сценарии выполнены, иначе False.


## Пример использования

```python
# Создаем объект для поставщика 'aliexpress'
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')

# Выполняем вход на сайт поставщика
supplier.login()

# Запускаем сценарии из файлов
supplier.run_scenario_files(['example_scenario.json'])

# Или запускаем сценарии по определенным условиям
supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
```


## Визуальное представление

Класс `Supplier` можно представить как абстрактный класс, определяющий общую структуру для работы с различными поставщиками. Конкретные реализации (например, `AliExpressSupplier`, `AmazonSupplier`) будут наследоваться от этого класса и добавлять специфичную логику для каждого поставщика.