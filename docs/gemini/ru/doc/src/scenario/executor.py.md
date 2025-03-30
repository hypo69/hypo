# Модуль для выполнения сценариев
## Обзор

Модуль содержит функции для выполнения сценариев, загрузки их из файлов и обработки процесса извлечения информации о продукте и вставки ее в PrestaShop.

## Подробней

Этот модуль является ядром процесса выполнения сценариев в `hypotez`. Он отвечает за загрузку файлов сценариев, их разбор и последовательное выполнение шагов, описанных в каждом сценарии. Модуль тесно интегрирован с другими компонентами системы, такими как модули извлечения данных (`related_modules`), PrestaShop API и база данных для хранения информации о кампаниях продуктов.

## Функции

### `dump_journal`

```python
def dump_journal(s, journal: dict) -> None:
    """
    Args:
        s (object): Supplier instance.
        journal (dict): Dictionary containing the journal data.

    Returns:
        None
    """
```

**Описание**: Сохраняет данные журнала в JSON-файл.

**Параметры**:
- `s` (object): Экземпляр поставщика.
- `journal` (dict): Словарь, содержащий данные журнала.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Как работает функция**:
Функция `dump_journal` принимает экземпляр поставщика `s` и словарь `journal`, содержащий данные для сохранения. Она формирует путь к файлу журнала на основе пути поставщика и имени журнала, а затем использует функцию `j_dumps` для записи данных журнала в JSON-файл.

### `run_scenario_files`

```python
def run_scenario_files(s, scenario_files_list: List[Path] | Path) -> bool:
    """
    Args:
        s (object): Supplier instance.
        scenario_files_list (List[Path] | Path): List of file paths for scenario files, or a single file path.

    Returns:
        bool: True if all scenarios were executed successfully, False otherwise.

    Raises:
        TypeError: If scenario_files_list is not a list or a Path object.
    """
```

**Описание**: Выполняет список файлов сценариев.

**Параметры**:
- `s` (object): Экземпляр поставщика.
- `scenario_files_list` (List[Path] | Path): Список путей к файлам сценариев или один путь к файлу.

**Возвращает**:
- `bool`: `True`, если все сценарии были выполнены успешно, `False` в противном случае.

**Вызывает исключения**:
- `TypeError`: Если `scenario_files_list` не является списком или объектом `Path`.

**Как работает функция**:
Функция `run_scenario_files` принимает экземпляр поставщика `s` и список файлов сценариев `scenario_files_list`. Она перебирает файлы сценариев и вызывает функцию `run_scenario_file` для выполнения каждого файла. Результаты выполнения каждого файла записываются в журнал. Если все сценарии выполнены успешно, функция возвращает `True`, иначе `False`.

### `run_scenario_file`

```python
def run_scenario_file(s, scenario_file: Path) -> bool:
    """
    Args:
        s (object): Supplier instance.
        scenario_file (Path): Path to the scenario file.

    Returns:
        bool: True if the scenario was executed successfully, False otherwise.
    """
```

**Описание**: Загружает и выполняет сценарии из файла.

**Параметры**:
- `s` (object): Экземпляр поставщика.
- `scenario_file` (Path): Путь к файлу сценария.

**Возвращает**:
- `bool`: `True`, если сценарий был выполнен успешно, `False` в противном случае.

**Как работает функция**:
Функция `run_scenario_file` принимает экземпляр поставщика `s` и путь к файлу сценария `scenario_file`. Она загружает сценарии из файла, используя функцию `j_loads`, и затем перебирает сценарии в файле. Для каждого сценария вызывается функция `run_scenario` для выполнения. Результат выполнения каждого сценария логируется. Функция возвращает `True`, если все сценарии в файле выполнены успешно, иначе `False`.

### `run_scenarios`

```python
def run_scenarios(s, scenarios: Optional[List[dict] | dict] = None, _journal=None) -> List | dict | bool:
    """
    Args:
        s (object): Supplier instance.
        scenarios (Optional[List[dict] | dict], optional): Accepts a list of scenarios or a single scenario as a dictionary. Defaults to None.

    Returns:
        List | dict | bool: The result of executing the scenarios, or False in case of an error.

    Todo:
        Check the option when no scenarios are specified from all sides. For example, when s.current_scenario is not specified and scenarios are not specified.
    """
```

**Описание**: Выполняет список сценариев (НЕ ФАЙЛОВ).

**Параметры**:
- `s` (object): Экземпляр поставщика.
- `scenarios` (Optional[List[dict] | dict], optional): Список сценариев или один сценарий в виде словаря. По умолчанию `None`.

**Возвращает**:
- `List | dict | bool`: Результат выполнения сценариев или `False` в случае ошибки.

**Как работает функция**:
Функция `run_scenarios` принимает экземпляр поставщика `s` и список сценариев `scenarios`. Она перебирает сценарии и вызывает функцию `run_scenario` для выполнения каждого сценария. Результаты выполнения каждого сценария записываются в журнал. Функция возвращает список результатов выполнения сценариев.

### `run_scenario`

```python
def run_scenario(supplier, scenario: dict, scenario_name: str, _journal=None) -> List | dict | bool:
    """
    Args:
        supplier (object): Supplier instance.
        scenario (dict): Dictionary containing scenario details.
        scenario_name (str): Name of the scenario.

    Returns:
        List | dict | bool: The result of executing the scenario.

    Todo:
        Check the need for the scenario_name parameter.
    """
```

**Описание**: Выполняет полученный сценарий.

**Параметры**:
- `supplier` (object): Экземпляр поставщика.
- `scenario` (dict): Словарь, содержащий детали сценария.
- `scenario_name` (str): Имя сценария.

**Возвращает**:
- `List | dict | bool`: Результат выполнения сценария.

**Как работает функция**:
Функция `run_scenario` принимает экземпляр поставщика `supplier`, словарь с деталями сценария `scenario` и имя сценария `scenario_name`. Она устанавливает текущий сценарий для поставщика, получает URL из сценария и переходит по нему. Затем она получает список продуктов в категории, перебирает их и для каждого продукта извлекает поля продукта, создает объект `Product` и вставляет полученные данные.

### `insert_grabbed_data_to_prestashop`

```python
async def insert_grabbed_data_to_prestashop(
    f: ProductFields, coupon_code: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None
) -> bool:
    """
    Args:
        f (ProductFields): ProductFields instance containing the product information.
        coupon_code (Optional[str], optional): Optional coupon code. Defaults to None.
        start_date (Optional[str], optional): Optional start date for the promotion. Defaults to None.
        end_date (Optional[str], optional): Optional end date for the promotion. Defaults to None.

    Returns:
        bool: True if the insertion was successful, False otherwise.
    """
```

**Описание**: Вставляет продукт в PrestaShop.

**Параметры**:
- `f` (ProductFields): Экземпляр `ProductFields`, содержащий информацию о продукте.
- `coupon_code` (Optional[str], optional): Код купона (необязательно). По умолчанию `None`.
- `start_date` (Optional[str], optional): Дата начала акции (необязательно). По умолчанию `None`.
- `end_date` (Optional[str], optional): Дата окончания акции (необязательно). По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если вставка прошла успешно, `False` в противном случае.

**Как работает функция**:
Функция `insert_grabbed_data_to_prestashop` принимает экземпляр `ProductFields` `f`, содержащий информацию о продукте, а также необязательные параметры `coupon_code`, `start_date` и `end_date`. Она создает экземпляр `PrestaShop` и вызывает его метод `post_product_data` для вставки данных продукта в PrestaShop. Функция возвращает `True`, если вставка прошла успешно, `False` в противном случае.