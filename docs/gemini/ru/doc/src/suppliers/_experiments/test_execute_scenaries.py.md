# Модуль `test_execute_scenarios`

## Обзор

Модуль `test_execute_scenarios.py` содержит набор тестов для проверки функциональности выполнения сценариев парсинга, включая запуск сценариев из файлов, запуск отдельных сценариев и захват данных со страниц продуктов. Он использует библиотеку `unittest` и моки (`MagicMock`) для изоляции тестируемых компонентов и упрощения проверки их поведения.

## Подробней

Этот модуль важен для обеспечения надежности и правильности работы системы парсинга, позволяя проверять различные аспекты выполнения сценариев, такие как обработка файлов сценариев, взаимодействие с API или веб-драйвером, а также экспорт полученных данных. Тесты охватывают как успешные сценарии, так и случаи возникновения ошибок или отсутствия данных.

## Классы

### `TestRunListOfScenarioFiles`

**Описание**: Класс, содержащий тесты для функции `run_scenarios`, которая отвечает за запуск списка файлов сценариев.

**Методы**:
- `test_with_scenario_files_...ed`: Тест проверяет запуск сценариев при наличии файлов сценариев в настройках.
- `test_with_no_scenario_files_...ed`: Тест проверяет запуск сценариев при отсутствии файлов сценариев в настройках, используя значения по умолчанию.

### `TestRunScenarioFile`

**Описание**: Класс, содержащий тесты для функции `run_scenario_file`, которая отвечает за запуск сценария из файла.

**Методы**:
- `setUp`: Подготавливает мок Supplier с необходимыми атрибутами перед каждым тестом.
- `test_run_scenario_file_webdriver`: Тест проверяет запуск сценария через веб-драйвер.
- `test_run_scenario_file_api`: Тест проверяет запуск сценария через API.
- `test_run_scenario_file_no_scenarios`: Тест проверяет обработку ситуации, когда в файле сценариев нет сценариев.

### `TestGrabProductPage`

**Описание**: Класс, содержащий тесты для функции `grab_product_page`, которая отвечает за захват данных со страницы продукта.

**Методы**:
- `setUp`: Подготавливает объект Supplier перед каждым тестом.
- `test_grab_product_page_succesStringFormatterul`: Тест проверяет успешный захват данных со страницы продукта при наличии всех необходимых данных.
- `test_grab_product_page_failure`: Тест проверяет ситуацию, когда при захвате данных со страницы продукта отсутствуют необходимые данные.

### `TestRunScenario`

**Описание**: Класс, содержащий тесты для функции `run_scenario`, которая отвечает за запуск отдельного сценария.

**Методы**:
- `setUp`: Подготавливает объект Supplier с необходимыми атрибутами перед каждым тестом.
- `tearDown`: Выполняет очистку после каждого теста. В текущей реализации содержит `...`.
- `test_run_scenario_no_url`: Тест проверяет ситуацию, когда в сценарии отсутствует URL.
- `test_run_scenario_valid_url`: Тест проверяет запуск сценария с валидным URL.
- `test_run_scenario_export_empty_list`: Тест проверяет ситуацию, когда список продуктов для экспорта пуст.

## Функции

### `run_scenarios`

```python
def run_scenarios(s, scenario_files = None):
    """
    Args:
        s (Supplier): Mock-объект Supplier.
        scenario_files (Optional[list[str]], optional): Список файлов сценариев. По умолчанию `None`.

    Returns:
        bool: Возвращает `True`, если сценарии выполнены успешно.

    Raises:
        AssertionError: Если `s.settings` или `s.settings['scenarios']` не определены.

    Example:
        >>> s = MagicMock()
        >>> s.settings = {'check categories on site': False, 'scenarios': ['default1.json', 'default2.json']}
        >>> scenario_files = ["scenario1.json", "scenario2.json"]
        >>> result = run_scenarios(s, scenario_files)
        >>> assert result == True
    """
```

**Описание**: Функция выполняет сценарии парсинга на основе списка файлов сценариев или настроек по умолчанию.

**Параметры**:
- `s`: Mock-объект Supplier, содержащий настройки и методы для выполнения сценариев.
- `scenario_files`: Список файлов сценариев для выполнения. Если не указан, используются сценарии из настроек Supplier.

**Возвращает**:
- `bool`: `True`, если все сценарии выполнены успешно, иначе `False`.

**Примеры**:

- Запуск с указанными файлами сценариев:

```python
s = MagicMock()
s.settings = {'check categories on site': False, 'scenarios': ['default1.json', 'default2.json']}
scenario_files = ["scenario1.json", "scenario2.json"]
result = run_scenarios(s, scenario_files)
```

- Запуск без указания файлов сценариев (используются значения по умолчанию из настроек):

```python
s = MagicMock()
s.settings = {'check categories on site': True, 'scenarios': ['default1.json', 'default2.json']}
result = run_scenarios(s)
```

### `run_scenario_file`

```python
def run_scenario_file(s, scenario_file):
    """
    Args:
        s (Supplier): Mock-объект Supplier.
        scenario_file (str): Имя файла сценария.

    Returns:
        bool: Возвращает `True`, если сценарий выполнен успешно.

    Raises:
        FileNotFoundError: Если файл сценария не найден.

    Example:
        >>> s = MagicMock()
        >>> s.current_scenario_filename = "test_scenario.json"
        >>> s.settings = {"parcing method [webdriver|api]": "webdriver"}
        >>> s.dir_export_imagesECTORY_FOR_STORE = "/path/to/images"
        >>> s.scenarios = {"scenario1": {"url": "https://example.com", "steps": []}}
        >>> result = run_scenario_file(s, "test_scenario.json")
        >>> assert result == True
    """
```

**Описание**: Функция выполняет сценарий парсинга, определенный в файле сценария.

**Параметры**:
- `s`: Mock-объект Supplier, содержащий настройки и методы для выполнения сценариев.
- `scenario_file`: Имя файла сценария для выполнения.

**Возвращает**:
- `bool`: `True`, если сценарий выполнен успешно, иначе `False`.

**Примеры**:

- Запуск сценария через веб-драйвер:

```python
s = MagicMock()
s.current_scenario_filename = "test_scenario.json"
s.settings = {"parcing method [webdriver|api]": "webdriver"}
s.dir_export_imagesECTORY_FOR_STORE = "/path/to/images"
s.scenarios = {"scenario1": {"url": "https://example.com", "steps": []}}
result = run_scenario_file(s, "test_scenario.json")
```

- Запуск сценария через API:

```python
s = MagicMock()
s.current_scenario_filename = "test_scenario.json"
s.settings = {"parcing method [webdriver|api]": "api"}
s.dir_export_imagesECTORY_FOR_STORE = "/path/to/images"
s.scenarios = {"scenario1": {"url": "https://example.com", "steps": []}}
result = run_scenario_file(s, "test_scenario.json")
```

### `run_scenario`

```python
def run_scenario(self, scenario):
    """
    Args:
        scenario (dict): Словарь с данными сценария.

    Returns:
        bool: Возвращает `True`, если сценарий выполнен успешно.

    Raises:
        Exception: Описание ситуации, в которой возникает исключение.

    Example:
        >>> supplier = Supplier()
        >>> supplier.settings['parcing method [webdriver|api]'] = 'webdriver'
        >>> supplier.current_scenario_filename = 'test_scenario.json'
        >>> supplier.export_file_name = 'test_export'
        >>> supplier.dir_export_imagesECTORY_FOR_STORE = '/test/path'
        >>> supplier.p = []
        >>> scenario = {'name': 'scenario2', 'url': 'https://example.com/products'}
        >>> supplier.scenarios = {'scenario2': scenario}
        >>> supplier.get_list_products_in_category = MagicMock(return_value=['https://example.com/products/1', 'https://example.com/products/2'])
        >>> supplier.grab_product_page = MagicMock(return_value=True)
        >>> supplier.export_files = MagicMock()
        >>> result = supplier.run_scenario(scenario)
        >>> assert result == True
    """
```

**Описание**: Функция выполняет отдельный сценарий парсинга.

**Параметры**:
- `scenario`: Словарь, содержащий данные сценария, такие как URL и шаги.

**Возвращает**:
- `bool`: `True`, если сценарий выполнен успешно, иначе `False`.

**Примеры**:

- Запуск сценария с валидным URL:

```python
supplier = Supplier()
supplier.settings['parcing method [webdriver|api]'] = 'webdriver'
supplier.current_scenario_filename = 'test_scenario.json'
supplier.export_file_name = 'test_export'
supplier.dir_export_imagesECTORY_FOR_STORE = '/test/path'
supplier.p = []
scenario = {'name': 'scenario2', 'url': 'https://example.com/products'}
supplier.scenarios = {'scenario2': scenario}
supplier.get_list_products_in_category = MagicMock(return_value=['https://example.com/products/1', 'https://example.com/products/2'])
supplier.grab_product_page = MagicMock(return_value=True)
supplier.export_files = MagicMock()
result = supplier.run_scenario(scenario)
```

- Запуск сценария без URL:

```python
supplier = Supplier()
supplier.settings['parcing method [webdriver|api]'] = 'webdriver'
supplier.current_scenario_filename = 'test_scenario.json'
supplier.export_file_name = 'test_export'
supplier.dir_export_imagesECTORY_FOR_STORE = '/test/path'
supplier.p = []
scenario = {'name': 'scenario1', 'url': None}
supplier.scenarios = {'scenario1': scenario}
supplier.get_list_products_in_category = MagicMock(return_value=[])
result = supplier.run_scenario(scenario)
```

### `grab_product_page`

```python
def grab_product_page(self):
    """
    Args:
        self (Supplier): Экземпляр класса Supplier.

    Returns:
        bool: Возвращает `True`, если данные о продукте успешно получены и добавлены в список.

    Raises:
        AttributeError: Если в данных о продукте отсутствуют необходимые поля (`id`, `price`, `name`).

    Example:
        >>> supplier = Supplier()
        >>> supplier.grab_product_page = lambda _: {'id': '123', 'price': 19.99, 'name': 'Product Name'}
        >>> result = grab_product_page(supplier)
        >>> assert result == True
    """
```

**Описание**: Функция пытается получить информацию о продукте и добавить ее в список продуктов Supplier.

**Параметры**:
- `self`: Экземпляр класса Supplier.

**Возвращает**:
- `bool`: `True`, если данные о продукте успешно получены и добавлены в список, иначе `False`.

**Примеры**:

- Успешный захват данных о продукте:

```python
supplier = Supplier()
supplier.grab_product_page = lambda _: {'id': '123', 'price': 19.99, 'name': 'Product Name'}
result = grab_product_page(supplier)
```

- Неудачный захват данных о продукте (отсутствуют необходимые поля):

```python
supplier = Supplier()
supplier.grab_product_page = lambda _: {'name': 'Product Name'}
result = grab_product_page(supplier)