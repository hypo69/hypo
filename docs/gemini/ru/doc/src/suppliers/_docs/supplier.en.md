# Класс `Supplier`

## Обзор

Класс `Supplier` служит базовым классом для управления поставщиками данных в приложении. Он предоставляет структуру для взаимодействия с различными источниками данных, такими как Amazon, AliExpress, Walmart и другие. Этот класс обрабатывает инициализацию настроек, специфичных для поставщика, управляет сценариями сбора данных и предоставляет методы для входа в систему и выполнения сценариев.

## Оглавление

* [Классы](#классы)
* [Функции](#функции)
* [Методы класса `Supplier`](#методы-класса-supplier)
* [Как это работает](#как-это-работает)
* [Пример использования](#пример-использования)
* [Резюме](#резюме)


## Классы

Не существует других классов, кроме класса `Supplier` в предоставленном коде.


## Функции

Нет функций в предоставленном коде.


## Методы класса `Supplier`

### `__init__`

**Описание**: Конструктор, инициализирующий атрибуты на основе префикса поставщика и других параметров.

**Параметры**:
* `supplier_prefix` (str): Префикс поставщика, например, `aliexpress` или `amazon`.
* `locale` (str, опционально): Код локализации (например, `en` для английского языка, `ru` для русского). По умолчанию `'en'`.
* `webdriver` (str | Driver | bool, опционально): Наименование драйвера или сам объект драйвера. По умолчанию `'default'`.
* `*attrs`: Дополнительные позиционные аргументы.
* `**kwargs`: Дополнительные именованные аргументы.

**Возвращает**:
-  Ничего.


### `_payload`

**Описание**: Загружает конфигурации, специфичные для поставщика, локэйторы и инициализирует веб-драйвер.

**Параметры**:
* `webdriver` (str | Driver | bool): Наименование драйвера или сам объект драйвера.


**Возвращает**:
- `bool`: `True` в случае успешной загрузки и инициализации, `False` в противном случае.


### `login`

**Описание**: Обрабатывает процесс входа в систему для сайта поставщика, если требуется аутентификация.

**Параметры**:
- Нет.

**Возвращает**:
- `bool`: `True` если вход в систему успешен, `False` в противном случае.


### `run_scenario_files`

**Описание**: Выполняет один или несколько сценариев из файлов.

**Параметры**:
* `scenario_files` (str | List[str], опционально): Список имен файлов сценариев или имя файла сценария. По умолчанию `None`.


**Возвращает**:
- `bool`: `True` если все сценарии успешно выполнены, `False` в противном случае.


### `run_scenarios`

**Описание**: Выполняет один или несколько сценариев на основе заданных параметров.

**Параметры**:
* `scenarios`: (dict | list[dict]): Словарь или список словарей, описывающих сценарии.

**Возвращает**:
- `bool`: `True` если все сценарии успешно выполнены, `False` в противном случае.


## Как это работает

1. **Инициализация**: При создании объекта класса `Supplier` метод `__init__` инициализирует префикс поставщика, локаль и веб-драйвер.


2. **Загрузка конфигурации**: Метод `_payload` загружает конфигурационные файлы для поставщика, включая настройки, локэйторы и инициализирует веб-драйвер.


3. **Вход в систему**: Метод `login` обрабатывает процесс аутентификации на веб-сайте поставщика.


4. **Выполнение сценариев**:
   - Метод `run_scenario_files` выполняет сценарии из списка файлов.
   - Метод `run_scenarios` выполняет сценарии на основе определенных условий или задач.


## Пример использования

```python
# Создание объекта Supplier для 'aliexpress'
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')

# Выполнить вход в систему
supplier.login()

# Выполнение сценариев из файла
supplier.run_scenario_files(['example_scenario.json'])

# Или выполнение конкретных сценариев
supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
```


## Резюме

Класс `Supplier` предоставляет структурированный способ взаимодействия с поставщиками данных, управляя конфигурациями, выполняя вход в систему и выполняя сценарии сбора данных. Он служит основополагающим компонентом, который можно расширить для конкретных поставщиков, унаследовав от этого базового класса и добавляя или переопределяя функциональность по мере необходимости.