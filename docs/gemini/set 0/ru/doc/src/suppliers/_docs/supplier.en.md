# Модуль `suppliers` - Класс `Supplier`

## Обзор

Данный модуль содержит класс `Supplier`, предназначенный для управления поставщиками данных. Он предоставляет базовый функционал для взаимодействия с различными источниками данных (Amazon, AliExpress, Walmart и т.д.), включая инициализацию поставщика, обработку сценариев сбора данных и выполнение логина.

## Оглавление

- [Модуль `suppliers` - Класс `Supplier`](#модуль-suppliers-класс-supplier)
- [Обзор](#обзор)
- [Описание класса `Supplier`](#описание-класса-supplier)
- [Атрибуты класса](#атрибуты-класса)
- [Методы класса](#методы-класса)
- [Как работает класс `Supplier`](#как-работает-класс-supplier)
- [Пример использования](#пример-использования)
- [Заключение](#заключение)


## Описание класса `Supplier`

Класс `Supplier` служит базовым классом для управления поставщиками данных. Он предоставляет структуру для взаимодействия с различными источниками данных, такими как Amazon, AliExpress, Walmart и другие. Данный класс отвечает за инициализацию настроек, специфичных для поставщика, управление сценариями сбора данных и методы для входа и выполнения сценариев.

## Атрибуты класса

#### `supplier_id`
Уникальный идентификатор поставщика.

#### `supplier_prefix`
Префикс поставщика, например, `aliexpress` или `amazon`.

#### `supplier_settings`
Настройки для поставщика, загруженные из файла конфигурации.

#### `locale`
Код локализации (например, `en` для английского, `ru` для русского).

#### `price_rule`
Правило для расчета цен (например, добавление НДС или применение скидок).

#### `related_modules`
Модуль, содержащий функции, специфичные для поставщика.

#### `scenario_files`
Список файлов сценариев, которые необходимо выполнить.

#### `current_scenario`
Текущий выполняемый сценарий.

#### `login_data`
Данные для входа на сайт поставщика (если требуется).

#### `locators`
Локаторы для веб-элементов на сайте поставщика.

#### `driver`
Веб-драйвер для взаимодействия с сайтом поставщика.

#### `parsing_method`
Метод для парсинга данных (например, `webdriver`, `api`, `xls`, `csv`).


## Методы класса

### `__init__`

**Описание**: Конструктор, инициализирующий атрибуты на основе префикса поставщика и других параметров.

**Параметры**:
- `supplier_prefix` (str): Префикс поставщика.
- `locale` (str, optional): Код локализации. По умолчанию `'en'`.
- `webdriver` (str | Driver | bool, optional): Веб-драйвер. По умолчанию `'default'`.

### `_payload`

**Описание**: Загружает конфигурации, локаторы, специфичные для поставщика, и инициализирует веб-драйвер.

**Параметры**:
- `webdriver` (str | Driver | bool): Веб-драйвер.

**Возвращает**:
- bool: `True` если загрузка успешна, `False` иначе.


### `login`

**Описание**: Обрабатывает процесс входа на сайт поставщика, если требуется аутентификация.

**Возвращает**:
- bool: `True` если вход успешен, `False` иначе.

### `run_scenario_files`

**Описание**: Выполняет один или несколько файлов сценариев.

**Параметры**:
- `scenario_files` (str | List[str], optional): Файлы сценариев. По умолчанию `None`.

**Возвращает**:
- bool: `True` если все сценарии успешно выполнены, `False` иначе.


### `run_scenarios`

**Описание**: Выполняет один или несколько сценариев.

**Параметры**:
- `scenarios` (dict | list[dict]): Список или словарь сценариев.

**Возвращает**:
- bool: `True` если все сценарии успешно выполнены, `False` иначе.


## Как работает класс `Supplier`

1. **Инициализация**: При создании объекта класса `Supplier`, метод `__init__` инициализирует префикс поставщика, локаль и веб-драйвер.

2. **Загрузка конфигурации**: Метод `_payload` загружает файлы конфигурации для поставщика, включая настройки, локаторы и инициализирует веб-драйвер.

3. **Вход**: Метод `login` обрабатывает процесс аутентификации на сайте поставщика.

4. **Выполнение сценариев**: Методы `run_scenario_files` и `run_scenarios` выполняют сценарии, полученные из файлов или списка сценариев.

## Пример использования

```python
# Создание объекта Supplier для 'aliexpress'
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')

# Выполнение входа
supplier.login()

# Выполнение сценариев из файла
supplier.run_scenario_files(['example_scenario.json'])

# Или выполнение конкретных сценариев
supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
```

## Заключение

Класс `Supplier` предоставляет структурированный способ взаимодействия с поставщиками данных, управляя конфигурацией, выполнением входа и исполнением сценариев сбора данных. Он служит основой для расширения для конкретных поставщиков данных, путем наследования от этого базового класса и добавления или переопределения функциональности по мере необходимости.