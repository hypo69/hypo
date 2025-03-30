# Модуль `executor`

## Обзор

Модуль `executor` предназначен для выполнения сценариев, загрузки их из файлов и обработки процесса извлечения информации о продукте и вставки ее в PrestaShop.

## Подробней

Модуль содержит функции для выполнения сценариев, загрузки их из файлов и обработки процесса извлечения информации о продукте и вставки ее в PrestaShop. Основные функции модуля включают загрузку и выполнение сценариев из файлов, запуск отдельных сценариев и вставку полученных данных в PrestaShop. Модуль использует другие модули, такие как `gs`, `jjson`, `PrestaProductAsync`, `ProductCampaignsManager` и `logger`.

## Функции

### `dump_journal`

```python
def dump_journal(s, journal: dict) -> None:
    """
    Сохраняет данные журнала в JSON-файл.

    Args:
        s (object): Экземпляр поставщика.
        journal (dict): Словарь, содержащий данные журнала.

    Returns:
        None
    """
```

**Описание**: Сохраняет данные журнала в JSON-файл. Файл сохраняется в директории `_journal` поставщика.

**Параметры**:
- `s` (object): Экземпляр поставщика.
- `journal` (dict): Словарь, содержащий данные журнала.

**Возвращает**:
- `None`

### `run_scenario_files`

```python
def run_scenario_files(s, scenario_files_list: List[Path] | Path) -> bool:
    """
    Выполняет список файлов сценариев.

    Args:
        s (object): Экземпляр поставщика.
        scenario_files_list (List[Path] | Path): Список путей к файлам сценариев или путь к одному файлу.

    Returns:
        bool: `True`, если все сценарии были успешно выполнены, `False` в противном случае.

    Raises:
        TypeError: Если `scenario_files_list` не является списком или объектом `Path`.
    """
```

**Описание**: Выполняет сценарии, загружая их из указанных файлов. Если передается один файл, он преобразуется в список.

**Параметры**:
- `s` (object): Экземпляр поставщика.
- `scenario_files_list` (List[Path] | Path): Список путей к файлам сценариев или путь к одному файлу.

**Возвращает**:
- `bool`: `True`, если все сценарии были успешно выполнены, `False` в противном случае.

**Вызывает исключения**:
- `TypeError`: Если `scenario_files_list` не является списком или объектом `Path`.

### `run_scenario_file`

```python
def run_scenario_file(s, scenario_file: Path) -> bool:
    """
    Загружает и выполняет сценарии из файла.

    Args:
        s (object): Экземпляр поставщика.
        scenario_file (Path): Путь к файлу сценария.

    Returns:
        bool: `True`, если сценарий был успешно выполнен, `False` в противном случае.
    """
```

**Описание**: Загружает сценарии из указанного файла и выполняет их.

**Параметры**:
- `s` (object): Экземпляр поставщика.
- `scenario_file` (Path): Путь к файлу сценария.

**Возвращает**:
- `bool`: `True`, если сценарий был успешно выполнен, `False` в противном случае.

### `run_scenarios`

```python
def run_scenarios(s, scenarios: Optional[List[dict] | dict] = None, _journal=None) -> List | dict | bool:
    """
    Выполняет список сценариев (НЕ ФАЙЛОВ).

    Args:
        s (object): Экземпляр поставщика.
        scenarios (Optional[List[dict] | dict], optional): Список сценариев или один сценарий в виде словаря. По умолчанию `None`.

    Returns:
        List | dict | bool: Результат выполнения сценариев или `False` в случае ошибки.

    Todo:
        Check the option when no scenarios are specified from all sides. For example, when s.current_scenario is not specified and scenarios are not specified.
    """
```

**Описание**: Выполняет сценарии, переданные в виде списка или словаря. Если сценарии не указаны, использует текущий сценарий поставщика.

**Параметры**:
- `s` (object): Экземпляр поставщика.
- `scenarios` (Optional[List[dict] | dict], optional): Список сценариев или один сценарий в виде словаря. По умолчанию `None`.

**Возвращает**:
- `List | dict | bool`: Результат выполнения сценариев или `False` в случае ошибки.

### `run_scenario`

```python
def run_scenario(supplier, scenario: dict, scenario_name: str, _journal=None) -> List | dict | bool:
    """
    Выполняет полученный сценарий.

    Args:
        supplier (object): Экземпляр поставщика.
        scenario (dict): Словарь, содержащий детали сценария.
        scenario_name (str): Имя сценария.

    Returns:
        List | dict | bool: Результат выполнения сценария.

    Todo:
        Check the need for the scenario_name parameter.
    """
```

**Описание**: Выполняет переданный сценарий.

**Параметры**:
- `supplier` (object): Экземпляр поставщика.
- `scenario` (dict): Словарь, содержащий детали сценария.
- `scenario_name` (str): Имя сценария.

**Возвращает**:
- `List | dict | bool`: Результат выполнения сценария.

### `insert_grabbed_data_to_prestashop`

```python
async def insert_grabbed_data_to_prestashop(
    f: ProductFields, coupon_code: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None
) -> bool:
    """
    Вставляет продукт в PrestaShop.

    Args:
        f (ProductFields): Экземпляр `ProductFields`, содержащий информацию о продукте.
        coupon_code (Optional[str], optional): Код купона (необязательно). По умолчанию `None`.
        start_date (Optional[str], optional): Дата начала акции (необязательно). По умолчанию `None`.
        end_date (Optional[str], optional): Дата окончания акции (необязательно). По умолчанию `None`.

    Returns:
        bool: `True`, если вставка прошла успешно, `False` в противном случае.
    """
```

**Описание**: Вставляет информацию о продукте в PrestaShop.

**Параметры**:
- `f` (ProductFields): Экземпляр `ProductFields`, содержащий информацию о продукте.
- `coupon_code` (Optional[str], optional): Код купона (необязательно). По умолчанию `None`.
- `start_date` (Optional[str], optional): Дата начала акции (необязательно). По умолчанию `None`.
- `end_date` (Optional[str], optional): Дата окончания акции (необязательно). По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если вставка прошла успешно, `False` в противном случае.