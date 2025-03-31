# Модуль для выполнения сценариев
## Обзор

Модуль `executor.py` предназначен для выполнения сценариев, загрузки их из файлов и обработки процесса извлечения информации о продуктах и вставки их в PrestaShop.

## Подробнее

Этот модуль является ключевым компонентом системы, отвечающим за автоматизированное выполнение сценариев, которые определяют порядок действий для извлечения данных о продуктах с веб-сайтов поставщиков и их последующей загрузки в PrestaShop. Он включает в себя функции для загрузки сценариев из файлов, навигации по страницам продуктов, извлечения необходимых данных и вставки их в систему PrestaShop.

## Содержание

- [Классы](#классы)
- [Функции](#функции)
    - [dump_journal](#dump_journal)
    - [run_scenario_files](#run_scenario_files)
    - [run_scenario_file](#run_scenario_file)
    - [run_scenarios](#run_scenarios)
    - [run_scenario](#run_scenario)
    - [insert_grabbed_data_to_prestashop](#insert_grabbed_data_to_prestashop)

## Классы

В данном модуле классы отсутствуют.

## Функции

### `dump_journal`

```python
def dump_journal(s, journal: dict) -> None:
    """!
    Save the journal data to a JSON file.

    Args:
        s (object): Supplier instance.
        journal (dict): Dictionary containing the journal data.

    Returns:
        None
    """
    _journal_file_path = Path(s.supplier_abs_path, '_journal', f"{journal['name']}.json")
    j_dumps(journal, _journal_file_path)
```

**Назначение**: Сохраняет данные журнала в файл JSON.

**Как работает функция**:
Функция `dump_journal` принимает экземпляр поставщика `s` и словарь `journal`, содержащий данные журнала. Она формирует путь к файлу журнала на основе пути поставщика и имени журнала, а затем использует функцию `j_dumps` для сохранения данных журнала в файл JSON.

**Параметры**:
- `s` (object): Экземпляр поставщика.
- `journal` (dict): Словарь, содержащий данные журнала.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Пример**:

```python
# Пример использования функции dump_journal
supplier = Supplier()  # Создаем экземпляр класса Supplier (определение класса не предоставлено)
journal_data = {'name': 'test_journal', 'data': {'key': 'value'}}
dump_journal(supplier, journal_data)
```

### `run_scenario_files`

```python
def run_scenario_files(s, scenario_files_list: List[Path] | Path) -> bool:
    """!
    Executes a list of scenario files.

    Args:
        s (object): Supplier instance.
        scenario_files_list (List[Path] | Path): List of file paths for scenario files, or a single file path.

    Returns:
        bool: True if all scenarios were executed successfully, False otherwise.

    Raises:
        TypeError: If scenario_files_list is not a list or a Path object.
    """
    if isinstance(scenario_files_list, Path):
        scenario_files_list = [scenario_files_list]
    elif not isinstance(scenario_files_list, list):
        raise TypeError('scenario_files_list must be a list or a Path object.')
    scenario_files_list = scenario_files_list if scenario_files_list else s.scenario_files

    _journal['scenario_files'] = {}
    for scenario_file in scenario_files_list:
        _journal['scenario_files'][scenario_file.name] = {}
        try:
            if run_scenario_file(s, scenario_file):
                _journal['scenario_files'][scenario_file.name]['message'] = f'{scenario_file} completed successfully!'
                logger.success(f'Scenario {scenario_file} completed successfully!')
            else:
                _journal['scenario_files'][scenario_file.name]['message'] = f'{scenario_file} FAILED!'
                logger.error(f'Scenario {scenario_file} failed to execute!')
        except Exception as ex:
            logger.critical(f'An error occurred while processing {scenario_file}: {ex}')
            _journal['scenario_files'][scenario_file.name]['message'] = f'Error: {ex}'
    return True
```

**Назначение**: Выполняет список файлов сценариев.

**Как работает функция**:
Функция `run_scenario_files` принимает экземпляр поставщика `s` и список путей к файлам сценариев `scenario_files_list`. Если `scenario_files_list` является одиночным путем, он преобразуется в список. Функция перебирает каждый файл сценария, вызывает функцию `run_scenario_file` для выполнения сценария и записывает результаты в журнал. В случае успеха или неудачи выполнения сценария, а также при возникновении исключений, соответствующие сообщения логируются с использованием модуля `logger`.

**Параметры**:
- `s` (object): Экземпляр поставщика.
- `scenario_files_list` (List[Path] | Path): Список путей к файлам сценариев или одиночный путь к файлу сценария.

**Возвращает**:
- `bool`: `True`, если все сценарии были выполнены успешно, `False` в противном случае.

**Вызывает исключения**:
- `TypeError`: Если `scenario_files_list` не является списком или объектом `Path`.

**Пример**:

```python
# Пример использования функции run_scenario_files
supplier = Supplier()  # Создаем экземпляр класса Supplier (определение класса не предоставлено)
scenario_files = [Path('scenario1.json'), Path('scenario2.json')]
result = run_scenario_files(supplier, scenario_files)
print(f'Scenarios execution result: {result}')
```

### `run_scenario_file`

```python
def run_scenario_file(s, scenario_file: Path) -> bool:
    """!
    Loads and executes scenarios from a file.

    Args:
        s (object): Supplier instance.
        scenario_file (Path): Path to the scenario file.

    Returns:
        bool: True if the scenario was executed successfully, False otherwise.
    """
    try:
        scenarios_dict = j_loads(scenario_file)['scenarios']
        for scenario_name, scenario in scenarios_dict.items():
            s.current_scenario = scenario
            if run_scenario(s, scenario, scenario_name):
                logger.success(f'Scenario {scenario_name} completed successfully!')
            else:
                logger.error(f'Scenario {scenario_name} failed to execute!')
        return True
    except (FileNotFoundError, json.JSONDecodeError) as ex:
        logger.critical(f'Error loading or processing scenario file {scenario_file}: {ex}')
        return False
```

**Назначение**: Загружает и выполняет сценарии из файла.

**Как работает функция**:
Функция `run_scenario_file` принимает экземпляр поставщика `s` и путь к файлу сценария `scenario_file`. Она загружает сценарии из файла с использованием функции `j_loads`, перебирает каждый сценарий и вызывает функцию `run_scenario` для его выполнения. В случае успеха или неудачи выполнения сценария, соответствующие сообщения логируются с использованием модуля `logger`. Если во время загрузки или обработки файла сценария возникают исключения `FileNotFoundError` или `json.JSONDecodeError`, они перехватываются, логируются как критические ошибки, и функция возвращает `False`.

**Параметры**:
- `s` (object): Экземпляр поставщика.
- `scenario_file` (Path): Путь к файлу сценария.

**Возвращает**:
- `bool`: `True`, если сценарий был выполнен успешно, `False` в противном случае.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл сценария не найден.
- `json.JSONDecodeError`: Если файл сценария содержит некорректный JSON.

**Пример**:

```python
# Пример использования функции run_scenario_file
supplier = Supplier()  # Создаем экземпляр класса Supplier (определение класса не предоставлено)
scenario_file = Path('scenario.json')
result = run_scenario_file(supplier, scenario_file)
print(f'Scenario file execution result: {result}')
```

### `run_scenarios`

```python
def run_scenarios(s, scenarios: Optional[List[dict] | dict] = None, _journal=None) -> List | dict | bool:
    """!
    Executes a list of scenarios (NOT FILES).

    Args:
        s (object): Supplier instance.
        scenarios (Optional[List[dict] | dict], optional): Accepts a list of scenarios or a single scenario as a dictionary. Defaults to None.

    Returns:
        List | dict | bool: The result of executing the scenarios, or False in case of an error.

    Todo:
        Check the option when no scenarios are specified from all sides. For example, when s.current_scenario is not specified and scenarios are not specified.
    """
    if not scenarios:
        scenarios = [s.current_scenario]

    scenarios = scenarios if isinstance(scenarios, list) else [scenarios]
    res = []
    for scenario in scenarios:
        res = run_scenario(s, scenario)
        _journal['scenario_files'][-1][scenario] = str(res)
        dump_journal(s, _journal)
    return res
```

**Назначение**: Выполняет список сценариев (НЕ ФАЙЛОВ).

**Как работает функция**:
Функция `run_scenarios` принимает экземпляр поставщика `s` и необязательный список сценариев `scenarios`. Если `scenarios` не указан, используется текущий сценарий поставщика. Функция перебирает каждый сценарий и вызывает функцию `run_scenario` для его выполнения. Результаты выполнения сценариев сохраняются в журнале.

**Параметры**:
- `s` (object): Экземпляр поставщика.
- `scenarios` (Optional[List[dict] | dict], optional): Список сценариев или одиночный сценарий в виде словаря. По умолчанию `None`.

**Возвращает**:
- `List | dict | bool`: Результат выполнения сценариев или `False` в случае ошибки.

**Пример**:

```python
# Пример использования функции run_scenarios
supplier = Supplier()  # Создаем экземпляр класса Supplier (определение класса не предоставлено)
scenarios = [{'url': 'http://example.com/product1'}, {'url': 'http://example.com/product2'}]
results = run_scenarios(supplier, scenarios)
print(f'Scenarios execution results: {results}')
```

### `run_scenario`

```python
def run_scenario(supplier, scenario: dict, scenario_name: str, _journal=None) -> List | dict | bool:
    """!
    Executes the received scenario.

    Args:
        supplier (object): Supplier instance.
        scenario (dict): Dictionary containing scenario details.
        scenario_name (str): Name of the scenario.

    Returns:
        List | dict | bool: The result of executing the scenario.

    Todo:
        Check the need for the scenario_name parameter.
    """
    s = supplier
    logger.info(f'Starting scenario: {scenario_name}')
    s.current_scenario = scenario
    d = s.driver
    d.get_url(scenario['url'])

    # Get list of products in the category
    list_products_in_category: list = s.related_modules.get_list_products_in_category(s)

    # No products in the category (or they haven't loaded yet)
    if not list_products_in_category:
        logger.warning('No product list collected from the category page. Possibly an empty category - ', d.current_url)
        return False

    for url in list_products_in_category:
        if not d.get_url(url):
            logger.error(f'Error navigating to product page at: {url}')
            continue  # <- Error navigating to the page. Skip

        # Grab product page fields
        grabbed_fields = s.related_modules.grab_product_page(s)
        f: ProductFields = asyncio.run(s.related_modules.grab_page(s))
        if not f:
            logger.error('Failed to collect product fields')
            continue

        presta_fields_dict, assist_fields_dict = f.presta_fields_dict, f.assist_fields_dict
        try:
            product: Product = Product(supplier_prefix=s.supplier_prefix, presta_fields_dict=presta_fields_dict)
            insert_grabbed_data(f)
        except Exception as ex:
            logger.error(f'Product {product.fields["name"][1]} could not be saved', ex)
            continue

    return list_products_in_category
```

**Назначение**: Выполняет полученный сценарий.

**Как работает функция**:
Функция `run_scenario` принимает экземпляр поставщика `supplier`, словарь `scenario`, содержащий детали сценария, и имя сценария `scenario_name`. Она устанавливает текущий сценарий поставщика, получает URL из сценария и переходит по нему с использованием драйвера поставщика. Затем функция получает список продуктов в категории с использованием модуля `get_list_products_in_category`. Если список продуктов пуст, функция логирует предупреждение и возвращает `False`. Для каждого URL продукта в списке функция переходит по URL, извлекает поля продукта с использованием модуля `grab_product_page` и `grab_page`. Если не удается извлечь поля продукта, функция логирует ошибку и переходит к следующему URL. Затем функция создает экземпляр класса `Product` и вызывает функцию `insert_grabbed_data` для вставки полученных данных. В случае возникновения исключения при создании продукта или вставке данных, функция логирует ошибку и переходит к следующему URL.

**Параметры**:
- `supplier` (object): Экземпляр поставщика.
- `scenario` (dict): Словарь, содержащий детали сценария.
- `scenario_name` (str): Имя сценария.

**Возвращает**:
- `List | dict | bool`: Результат выполнения сценария.

**Пример**:

```python
# Пример использования функции run_scenario
supplier = Supplier()  # Создаем экземпляр класса Supplier (определение класса не предоставлено)
scenario = {'url': 'http://example.com/category'}
scenario_name = 'test_scenario'
results = run_scenario(supplier, scenario, scenario_name)
print(f'Scenario execution results: {results}')
```

### `insert_grabbed_data_to_prestashop`

```python
async def insert_grabbed_data_to_prestashop(
    f: ProductFields, coupon_code: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None
) -> bool:
    """!
    Inserts the product into PrestaShop.

    Args:
        f (ProductFields): ProductFields instance containing the product information.
        coupon_code (Optional[str], optional): Optional coupon code. Defaults to None.
        start_date (Optional[str], optional): Optional start date for the promotion. Defaults to None.
        end_date (Optional[str], optional): Optional end date for the promotion. Defaults to None.

    Returns:
        bool: True if the insertion was successful, False otherwise.
    """
    try:
        presta = PrestaShop()
        return await presta.post_product_data(
            product_id=f.product_id,
            product_name=f.product_name,
            product_category=f.product_category,
            product_price=f.product_price,
            description=f.description,
            coupon_code=coupon_code,
            start_date=start_date,
            end_date=end_date,
        )

    except Exception as ex:
        logger.error('Failed to insert product data into PrestaShop: ', ex)
        return False
```

**Назначение**: Вставляет продукт в PrestaShop.

**Как работает функция**:
Функция `insert_grabbed_data_to_prestashop` принимает экземпляр `ProductFields` `f`, содержащий информацию о продукте, а также необязательные параметры `coupon_code`, `start_date` и `end_date`. Она создает экземпляр класса `PrestaShop` и вызывает асинхронную функцию `post_product_data` для отправки данных продукта в PrestaShop. В случае возникновения исключения при вставке данных, функция логирует ошибку и возвращает `False`.

**Параметры**:
- `f` (ProductFields): Экземпляр `ProductFields`, содержащий информацию о продукте.
- `coupon_code` (Optional[str], optional): Необязательный код купона. По умолчанию `None`.
- `start_date` (Optional[str], optional): Необязательная дата начала акции. По умолчанию `None`.
- `end_date` (Optional[str], optional): Необязательная дата окончания акции. По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если вставка прошла успешно, `False` в противном случае.

**Пример**:

```python
# Пример использования функции insert_grabbed_data_to_prestashop
product_fields = ProductFields()  # Создаем экземпляр класса ProductFields (определение класса не предоставлено)
product_fields.product_id = '123'
product_fields.product_name = 'Test Product'
product_fields.product_category = 'Test Category'
product_fields.product_price = '10.00'
product_fields.description = 'Test Description'
result = asyncio.run(insert_grabbed_data_to_prestashop(product_fields, coupon_code='TESTCOUPON'))
print(f'Product insertion result: {result}')