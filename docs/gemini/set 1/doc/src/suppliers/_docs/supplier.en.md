# Класс `Supplier`

## Обзор

Класс `Supplier` служит базовым классом для управления поставщиками данных в приложении. Он предоставляет структуру для взаимодействия с различными источниками данных, такими как Amazon, AliExpress, Walmart и другими. Этот класс обрабатывает инициализацию настроек, специфичных для поставщика, управляет сценариями сбора данных и предоставляет методы для входа в систему и выполнения сценариев.

## Оглавление

* [Класс `Supplier`](#класс-supplier)
    * [Обзор](#обзор)
    * [Компоненты класса `Supplier`](#компоненты-класса-supplier)
        * [Атрибуты класса](#атрибуты-класса)
        * [Методы](#методы)
    * [Как это работает](#как-это-работает)
    * [Визуальное представление](#визуальное-представление)
    * [Пример использования](#пример-использования)
    * [Резюме](#резюме)


## Компоненты класса `Supplier`

### Атрибуты класса

* `supplier_id`: Уникальный идентификатор поставщика.
* `supplier_prefix`: Префикс для поставщика, например, `aliexpress` или `amazon`.
* `supplier_settings`: Настройки для поставщика, загруженные из файла конфигурации.
* `locale`: Код локализации (например, `en` для английского, `ru` для русского).
* `price_rule`: Правило для расчета цен (например, добавление НДС или применение скидок).
* `related_modules`: Модуль, содержащий функции, специфичные для поставщика.
* `scenario_files`: Список файлов сценариев, которые должны быть выполнены.
* `current_scenario`: Текущий выполняемый сценарий.
* `login_data`: Данные для входа в систему на веб-сайте поставщика (при необходимости).
* `locators`: Локаторы веб-элементов на сайте поставщика.
* `driver`: Веб-драйвер для взаимодействия с сайтом поставщика.
* `parsing_method`: Метод для разбора данных (например, `webdriver`, `api`, `xls`, `csv`).

### Методы

* `__init__` : Конструктор, который инициализирует атрибуты на основе префикса поставщика и других параметров.
    ```python
    def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | 'Driver' | bool = 'default', *attrs, **kwargs):
        """
        Инициализирует префикс поставщика, локаль и веб-драйвер.

        Args:
            supplier_prefix (str): Префикс поставщика.
            locale (str, optional): Код локализации. По умолчанию 'en'.
            webdriver (str | 'Driver' | bool, optional): Веб-драйвер. По умолчанию 'default'.
        """
        # Инициализирует атрибуты поставщика
    ```
* `_payload` : Загружает конфигурации, локаторы, специфичные для поставщика, и инициализирует веб-драйвер.
    ```python
    def _payload(self, webdriver: str | 'Driver' | bool, *attrs, **kwargs) -> bool:
        """
        Загружает файлы конфигурации и инициализирует веб-драйвер.

        Args:
            webdriver (str | 'Driver' | bool): Веб-драйвер.

        Returns:
            bool: True, если загрузка прошла успешно, иначе False.

        Raises:
            FileNotFoundError: Если файл конфигурации не найден.
            Exception: При других ошибках.
        """
        # Загружает файлы конфигурации и настраивает веб-драйвер
    ```
* `login` : Обрабатывает процесс входа в систему на сайте поставщика, если требуется аутентификация.
    ```python
    def login(self) -> bool:
        """
        Выполняет вход в систему на сайте поставщика.

        Returns:
            bool: True, если вход выполнен успешно, иначе False.

        Raises:
            Exception: При ошибках входа в систему.
        """
        # Выполняет вход в систему
    ```
* `run_scenario_files` : Выполняет один или несколько файлов сценариев.
    ```python
    def run_scenario_files(self, scenario_files: str | list[str] = None) -> bool:
        """
        Выполняет сценарии из указанных файлов.

        Args:
            scenario_files (str | list[str], optional): Список файлов сценариев. По умолчанию None.

        Returns:
            bool: True, если все сценарии выполнены успешно, иначе False.

        Raises:
            Exception: При ошибках выполнения сценариев.
        """
        # Выполняет сценарии
    ```
* `run_scenarios` : Выполняет один или несколько сценариев.
    ```python
    def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
        """
        Выполняет указанные сценарии.

        Args:
            scenarios (dict | list[dict]): Сценарии для выполнения.

        Returns:
            bool: True, если все сценарии выполнены успешно, иначе False.

        Raises:
            Exception: При ошибках выполнения сценариев.
        """
        # Выполняет сценарии
    ```


## Как это работает

1. **Инициализация**: При создании объекта класса `Supplier` метод `__init__` инициализирует префикс поставщика, локаль и веб-драйвер.
2. **Загрузка конфигурации**: Метод `_payload` загружает файлы конфигурации для поставщика, включая настройки и локаторы, и инициализирует веб-драйвер.
3. **Вход**: Метод `login` обрабатывает процесс аутентификации на веб-сайте поставщика.
4. **Выполнение сценариев**: Метод `run_scenario_files` выполняет сценарии из списка файлов. Метод `run_scenarios` выполняет сценарии на основе определённых условий или задач.

## Визуальное представление

Класс `Supplier` действует как чертёж для управления сбором данных от разных поставщиков. Он определяет общие методы и атрибуты, которые могут быть использованы или расширены конкретными реализациями для разных поставщиков. Класс централизует управление поставщиками, включая конфигурацию, вход в систему и выполнение сценариев.

## Пример использования

```python
# Создание объекта Supplier для 'aliexpress'
supplier = Supplier(supplier_prefix='aliexpress', locale='en', webdriver='chrome')

# Выполнение входа в систему
supplier.login()

# Выполнение сценариев из файлов
supplier.run_scenario_files(['example_scenario.json'])

# Или выполнение определенных сценариев
supplier.run_scenarios([{'action': 'scrape', 'target': 'product_list'}])
```

## Резюме

В заключение, класс `Supplier` предоставляет структурированный способ взаимодействия с поставщиками данных путём управления конфигурациями, выполнения входа в систему и выполнения сценариев сбора данных. Он служит основополагающим компонентом, который может быть расширен для конкретных поставщиков путём наследования от этого базового класса и добавления или переопределения функциональности по мере необходимости.