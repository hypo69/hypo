# Модуль `suppliers`

## Обзор

Данный модуль предоставляет базовый класс `Supplier` для работы с различными поставщиками данных (например, интернет-магазины). Он унифицирует взаимодействие с ними, используя стандартизированные операции, включая инициализацию, конфигурацию, авторизацию и выполнение заданных сценариев. Поддерживает различные методы получения данных, включая `webdriver` и `api`.

## Классы

### `Supplier`

**Описание**: Базовый класс для всех поставщиков данных. Предназначен для абстрагирования взаимодействия с разными источниками данных, такими как веб-сайты, документы или базы данных.

**Атрибуты**:

- `supplier_id` (int): Уникальный идентификатор поставщика.
- `supplier_prefix` (str): Префикс поставщика (например, `'amazon'`, `'aliexpress'`).
- `supplier_settings` (dict): Настройки поставщика, загруженные из JSON файла.
- `locale` (str): Код локализации (по умолчанию: `'en'`).
- `price_rule` (str): Правила расчета цен (например, правила НДС).
- `related_modules` (module): Вспомогательные модули для специфических операций с поставщиком.
- `scenario_files` (list): Список файлов сценариев для выполнения.
- `current_scenario` (dict): Сценарий, который выполняется в данный момент.
- `login_data` (dict): Данные для аутентификации.
- `locators` (dict): Словарь локаторов веб-элементов.
- `driver` (Driver): Экземпляр WebDriver для взаимодействия с веб-сайтом поставщика.
- `parsing_method` (str): Метод парсинга данных (например, `'webdriver'`, `'api'`, `'xls'`, `'csv'`).

**Методы**:

- `__init__`:
    ```python
    def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs):
        """Инициализирует экземпляр класса Supplier.

        Args:
            supplier_prefix (str): Префикс поставщика.
            locale (str, optional): Код локализации. По умолчанию 'en'.
            webdriver (str | Driver | bool, optional): Тип WebDriver. По умолчанию 'default'.

        Raises:
            DefaultSettingsException: Если настройки по умолчанию не настроены должным образом.
        """
    ```
- `_payload`:
    ```python
    def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
        """Загружает настройки, локаторы и инициализирует WebDriver.

        Args:
            webdriver (str | Driver | bool): Тип WebDriver.

        Returns:
            bool: Возвращает `True`, если загрузка прошла успешно.
        """
    ```
- `login`:
    ```python
    def login(self) -> bool:
        """Производит авторизацию на сайте поставщика.

        Returns:
            bool: Возвращает `True`, если авторизация прошла успешно.
        """
    ```
- `run_scenario_files`:
    ```python
    def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
        """Выполняет предоставленные файлы сценариев.

        Args:
            scenario_files (str | List[str], optional): Список или путь к файлам сценариев.

        Returns:
            bool: Возвращает `True`, если сценарии были успешно выполнены.
        """
    ```
- `run_scenarios`:
    ```python
    def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
        """Выполняет заданные сценарии.

        Args:
            scenarios (dict | list[dict]): Сценарии для выполнения.

        Returns:
            bool: Возвращает `True`, если все сценарии были успешно выполнены.
        """
    ```

## Список реализованных поставщиков

Список реализованных поставщиков и используемых ими сценариев:

[aliexpress](aliexpress) - `webdriver`, `api`
[amazon](amazon) - `webdriver`
... (и так далее, как в исходном коде)

## Схема взаимодействия

(Вставка mermaid диаграммы)


## Как работает модуль

(Описание процесса работы в 4 пунктах, как в исходном коде)