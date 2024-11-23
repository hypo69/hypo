```markdown
# Документация модуля Supplier

## Обзор

Модуль `Supplier` предоставляет абстрактный базовый класс для работы с различными поставщиками данных (например, Amazon, Walmart).  Он централизует управление настройками, аутентификацией и выполнением сценариев для взаимодействия с поставщиками.  Класс позволяет легко расширять функциональность для новых поставщиков через наследование.


## Классы

### `Supplier`

**Описание**: Базовый класс для всех поставщиков, обеспечивающий общий функционал управления взаимодействием с источником данных.

**Атрибуты**:

*   `supplier_id` (int): Уникальный идентификатор поставщика.
*   `supplier_prefix` (str): Префикс поставщика (например, 'amazon', 'walmart').
*   `supplier_settings` (dict): Настройки поставщика, загружаемые из JSON файла.
*   `locale` (str, optional): Код локализации (по умолчанию 'en').
*   `price_rule` (str): Правила расчета цен (например, правила НДС).
*   `related_modules` (module): Модули-помощники для работы с конкретным поставщиком.
*   `scenario_files` (list): Список файлов сценариев для выполнения.
*   `current_scenario` (dict): Текущий сценарий, выполняемый системой.
*   `login_data` (dict): Данные для аутентификации.
*   `locators` (dict): Словарь локаторов веб-элементов.
*   `driver` (Driver): Экземпляр WebDriver для взаимодействия с сайтом поставщика.
*   `parsing_method` (str): Метод парсинга данных (например, 'webdriver', 'api', 'xls', 'csv').

**Методы**:

#### `__init__`

**Описание**: Инициализация экземпляра `Supplier`.

```python
def __init__(self, supplier_prefix: str, locale: str = 'en', webdriver: str | Driver | bool = 'default', *attrs, **kwargs):
    """Инициализация экземпляра Supplier.

    Args:
        supplier_prefix (str): Префикс поставщика.
        locale (str, optional): Код локализации. По умолчанию 'en'.
        webdriver (str | Driver | bool, optional): Тип WebDriver. По умолчанию 'default'.

    Raises:
        DefaultSettingsException: Если настройки по умолчанию не настроены корректно.
    """
```

#### `_payload`

**Описание**: Загрузка настроек поставщика и инициализация WebDriver.

```python
def _payload(self, webdriver: str | Driver | bool, *attrs, **kwargs) -> bool:
    """Загружает настройки, локаторы и инициализирует WebDriver.

    Args:
        webdriver (str | Driver | bool): Тип WebDriver.

    Returns:
        bool: Возвращает True, если загрузка выполнена успешно.
    """
```

#### `login`

**Описание**: Обработка аутентификации на сайте поставщика.

```python
def login(self) -> bool:
    """Производит аутентификацию пользователя на сайте поставщика.

    Returns:
        bool: Возвращает True, если вход выполнен успешно.
    """
```

#### `run_scenario_files`

**Описание**: Выполнение одного или нескольких файлов сценариев.

```python
def run_scenario_files(self, scenario_files: str | List[str] = None) -> bool:
    """Запускает предоставленные файлы сценариев.

    Args:
        scenario_files (str | List[str], optional): Список или путь к файлам сценариев.

    Returns:
        bool: Возвращает True, если сценарии выполнены успешно.
    """
```

#### `run_scenarios`

**Описание**: Выполнение указанных сценариев.

```python
def run_scenarios(self, scenarios: dict | list[dict]) -> bool:
    """Запускает указанные сценарии.

    Args:
        scenarios (dict | list[dict]): Сценарии для выполнения.

    Returns:
        bool: Возвращает True, если все сценарии выполнены успешно.
    """
```


##  Использование

Пример использования класса `Supplier`:

```python
from supplier import Supplier
# ... (импорты других необходимых модулей)

supplier = Supplier(supplier_prefix='amazon')
supplier._payload(webdriver='chrome')
supplier.login()
supplier.run_scenario_files(['scenario_file1.json', 'scenario_file2.json'])

```

##  Примечания


- Подробное описание обработки исключений `DefaultSettingsException` и других потенциальных ошибок должно быть дополнено.
- Документация должна быть дополнена описанием структуры файлов сценариев (`.json` или иных).
- Примеры использования сценариев должны быть более конкретными.


```
