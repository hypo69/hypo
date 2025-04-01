# Модуль `test_execute_scenaries.py`

## Обзор

Модуль содержит набор тестов для проверки функциональности выполнения сценариев, включая запуск списка файлов сценариев, запуск одного файла сценария и извлечение данных со страницы продукта.

## Подробней

Этот модуль предназначен для тестирования основных функций, связанных с выполнением сценариев парсинга веб-страниц. Он включает тесты для обработки сценариев, загруженных из файлов, переключения между различными методами парсинга (webdriver и API), а также для проверки успешности и неудачи извлечения данных со страниц продуктов. Модуль использует `unittest` для организации тестов и `MagicMock` для имитации зависимостей и упрощения тестирования отдельных компонентов.

## Классы

### `TestRunListOfScenarioFiles`

**Описание**: Класс содержит тесты для функции `run_scenarios`, которая отвечает за запуск списка файлов сценариев.

**Как работает класс**:

Класс `TestRunListOfScenarioFiles` использует `unittest.TestCase` для определения тестовых методов. Он проверяет поведение функции `run_scenarios` в различных ситуациях, включая случай, когда предоставлен список файлов сценариев, и случай, когда список не предоставлен. Для имитации зависимостей используется `MagicMock`.

**Методы**:

- `test_with_scenario_files_...ed`: Тест проверяет запуск `run_scenarios` со списком файлов сценариев. Он удостоверяется, что функция правильно обрабатывает файлы сценариев и что соответствующие методы не вызываются или вызываются нужное количество раз.
- `test_with_no_scenario_files_...ed`: Тест проверяет запуск `run_scenarios` без списка файлов сценариев. Он удостоверяется, что в этом случае вызываются методы, связанные с построением категорий магазина.

### `TestRunScenarioFile`

**Описание**: Класс содержит тесты для функции `run_scenario_file`, которая отвечает за запуск сценария из файла.

**Как работает класс**:

Класс `TestRunScenarioFile` использует `unittest.TestCase` для определения тестовых методов. Он проверяет поведение функции `run_scenario_file` в различных ситуациях, таких как использование webdriver или API для парсинга, а также случай, когда в файле сценария отсутствуют сценарии. Для имитации зависимостей используются `MagicMock` и `patch`.

**Методы**:

- `setUp`: Подготавливает тестовую среду, создавая экземпляр `MagicMock` для имитации объекта `Supplier` и устанавливая необходимые атрибуты и настройки.
- `test_run_scenario_file_webdriver`: Тест проверяет запуск `run_scenario_file` с использованием webdriver. Он удостоверяется, что функция правильно загружает файл сценария и вызывает функцию `run_scenario` для каждого сценария в файле.
- `test_run_scenario_file_api`: Тест проверяет запуск `run_scenario_file` с использованием API. Он удостоверяется, что функция вызывает функцию `run_scenario_file_via_api` для выполнения сценария через API.
- `test_run_scenario_file_no_scenarios`: Тест проверяет случай, когда файл сценария не содержит сценариев. Он удостоверяется, что функция правильно обрабатывает эту ситуацию и регистрирует ошибку в логе.

### `TestGrabProductPage`

**Описание**: Класс содержит тесты для функции `grab_product_page`, которая отвечает за извлечение данных со страницы продукта.

**Как работает класс**:

Класс `TestGrabProductPage` использует `unittest.TestCase` для определения тестовых методов. Он проверяет поведение функции `grab_product_page` в различных ситуациях, включая успешное извлечение данных и случай, когда данные отсутствуют. Для имитации объекта `Supplier` используется экземпляр класса `Supplier`.

**Методы**:

- `setUp`: Подготавливает тестовую среду, создавая экземпляр класса `Supplier`.
- `test_grab_product_page_succesStringFormatterul`: Тест проверяет успешное извлечение данных со страницы продукта. Он удостоверяется, что функция возвращает `True` и добавляет извлеченные данные в список продуктов `s.p`.
- `test_grab_product_page_failure`: Тест проверяет случай, когда не удается извлечь все необходимые данные со страницы продукта. Он удостоверяется, что функция возвращает `False` и не добавляет данные в список продуктов `s.p`.

### `TestRunScenario`

**Описание**: Класс содержит тесты для функции `run_scenario`, которая отвечает за запуск одного сценария.

**Как работает класс**:

Класс `TestRunScenario` использует `unittest.TestCase` для определения тестовых методов. Он проверяет поведение функции `run_scenario` в различных ситуациях, включая случай, когда URL отсутствует, и случай, когда URL валидный. Для имитации зависимостей используются `MagicMock`.

**Методы**:

- `setUp`: Подготавливает тестовую среду, создавая экземпляр класса `Supplier` и устанавливая необходимые атрибуты и настройки.
- `tearDown`: Выполняет очистку после каждого теста. В данном случае, тело функции не реализовано (`...`).
- `test_run_scenario_no_url`: Тест проверяет запуск сценария без URL. Он удостоверяется, что функция возвращает `False`.
- `test_run_scenario_valid_url`: Тест проверяет запуск сценария с валидным URL. Он удостоверяется, что функция вызывает необходимые методы для извлечения данных и экспорта файлов.
- `test_run_scenario_export_empty_list`: Тест проверяет случай, когда список продуктов пуст после извлечения данных. Он удостоверяется, что функция не вызывает метод экспорта файлов.

## Функции

### `run_scenarios`

```python
def run_scenarios(s, scenario_files) -> bool:
    """
    Запускает сценарии из указанных файлов или из настроек поставщика.

    Args:
        s: Объект поставщика с настройками и связанными модулями.
        scenario_files: Список файлов сценариев для запуска.

    Returns:
        bool: True, если все сценарии выполнены успешно, иначе False.

    Raises:
        Exception: Если возникает ошибка при выполнении сценария.
    """
```

**Как работает функция**:

1. **Определение источника сценариев**: Функция определяет, откуда брать сценарии для выполнения: из переданного списка файлов (`scenario_files`) или из настроек поставщика (`s.settings['scenarios']`).
2. **Обработка списка файлов**: Если предоставлен список файлов (`scenario_files`), функция проходит по каждому файлу и запускает его, обновляя информацию о текущем сценарии и последнем запущенном сценарии в настройках поставщика.
3. **Обработка сценариев из настроек**: Если список файлов не предоставлен, функция предполагает, что сценарии указаны в настройках поставщика (`s.settings['scenarios']`). В этом случае также обновляется информация о текущем сценарии и последнем запущенном сценарии.
4. **Вызов связанных модулей**: Если в настройках указано, что нужно проверять категории на сайте (`s.settings['check categories on site']`), вызывается метод `build_shop_categories` из связанных модулей поставщика.

**Примеры**:

```python
s = MagicMock()
scenario_files = ["scenario1.json", "scenario2.json"]
s.settings = {
    'check categories on site': False,
    'scenarios': ["default1.json", "default2.json"]
}

result = run_scenarios(s, scenario_files)

assert result is True
s.related_modules.build_shop_categories.assert_not_called()
assert s.current_scenario_filename == "scenario2.json"
assert s.settings['last_runned_scenario'] == "scenario2.json"
```

```python
s = MagicMock()
s.settings = {
    'check categories on site': True,
    'scenarios': ["default1.json", "default2.json"]
}

result = run_scenarios(s)

assert result is True
s.related_modules.build_shop_categories.assert_called_once()
assert s.current_scenario_filename == "default2.json"
assert s.settings['last_runned_scenario'] == "default2.json"
```

### `run_scenario_file`

```python
def run_scenario_file(s, scenario_file_name: str) -> bool:
    """
    Запускает сценарии, описанные в указанном файле сценария.

    Args:
        s: Объект поставщика с настройками и связанными модулями.
        scenario_file_name (str): Имя файла сценария для запуска.

    Returns:
        bool: True, если сценарии выполнены успешно, иначе False.

    Raises:
        FileNotFoundError: Если указанный файл сценария не найден.
        Exception: Если возникает ошибка при выполнении сценария.
    """
```

**Как работает функция**:

1. **Определение метода парсинга**: Функция определяет метод парсинга, который будет использоваться для выполнения сценария (webdriver или API), на основе настроек поставщика (`s.settings["parcing method [webdriver|api]"]`).
2. **Загрузка сценариев из файла**: Функция загружает сценарии из указанного файла, используя функцию `j_loads` из модуля `your_module`.
3. **Выполнение сценариев**: Если метод парсинга - webdriver, функция проходит по каждому сценарию в файле и запускает его, вызывая функцию `run_scenario`. Если метод парсинга - API, функция вызывает функцию `run_scenario_file_via_api` из связанных модулей поставщика.
4. **Обработка отсутствия сценариев**: Если в файле сценария не указаны сценарии, функция регистрирует ошибку в логе и возвращает `False`.

**Примеры**:

```python
from unittest.mock import patch

# Mock j_loads function
with patch("your_module.j_loads") as mock_j_loads:
    # Mock scenario data
    mock_j_loads.return_value = {"scenarios": self.s.scenarios}
    
    # Mock run_scenario function
    with patch("your_module.run_scenario") as mock_run_scenario:
        # Execute the function
        run_scenario_file(self.s, "test_scenario.json")
        
        # Assert j_loads was called correctly
        mock_j_loads.assert_called_once_with("/path/to/scenarios/test_scenario.json")
        
        # Assert run_scenario was called with the first scenario
        mock_run_scenario.assert_any_call(self.s, self.s.scenarios["scenario1"])
        
        # Assert run_scenario was not called with the second scenario
        mock_run_scenario.assert_not_called_with(self.s, self.s.scenarios["scenario2"])
```

```python
from unittest.mock import patch

# Set parsing method to "api"
self.s.settings["parcing method [webdriver|api]"] = "api"

# Mock the run_scenario_file_via_api function
with patch("your_module.related_modules.run_scenario_file_via_api") as mock_run_scenario_file_via_api:
    # Execute the function
    run_scenario_file(self.s, "test_scenario.json")
    
    # Assert run_scenario_file_via_api was called correctly
    mock_run_scenario_file_via_api.assert_called_once_with(self.s, "test_scenario.json")
```

### `grab_product_page`

```python
def grab_product_page(s) -> bool:
    """
    Извлекает данные со страницы продукта и сохраняет их в список продуктов поставщика.

    Args:
        s: Объект поставщика с настройками и связанными модулями.

    Returns:
        bool: True, если данные успешно извлечены и сохранены, иначе False.
    """
```

**Как работает функция**:

1. **Извлечение данных**: Функция вызывает метод `grab_product_page` объекта поставщика для извлечения данных со страницы продукта.
2. **Проверка наличия данных**: Функция проверяет, что извлеченные данные содержат все необходимые поля (id, price, name).
3. **Сохранение данных**: Если все необходимые поля присутствуют, функция добавляет извлеченные данные в список продуктов поставщика (`s.p`).
4. **Обработка отсутствия данных**: Если какие-либо необходимые поля отсутствуют, функция не добавляет данные в список продуктов.

**Примеры**:

```python
from unittest.mock import MagicMock

# Mock the Supplier class
s = MagicMock()

# Mock the grab_product_page method to return valid data
s.grab_product_page = lambda _: {'id': '123', 'price': 19.99, 'name': 'Product Name'}

# Call the function
result = grab_product_page(s)

# Assert the result is True
assert result is True

# Assert the product list contains the new product
assert len(s.p) == 1
assert s.p[0]['id'] == '123'
assert s.p[0]['price'] == 19.99
assert s.p[0]['name'] == 'Product Name'
```

```python
from unittest.mock import MagicMock

# Mock the Supplier class
s = MagicMock()

# Mock the grab_product_page method to return incomplete data
s.grab_product_page = lambda _: {'name': 'Product Name'}

# Call the function
result = grab_product_page(s)

# Assert the result is False
assert result is False

# Assert the product list is empty
assert len(s.p) == 0
```

### `run_scenario`

```python
def run_scenario(self, scenario: dict) -> bool:
    """
    Выполняет сценарий парсинга для указанного URL.

    Args:
        scenario (dict): Словарь с информацией о сценарии, включая название и URL.

    Returns:
        bool: True, если сценарий выполнен успешно, иначе False.
    """
```

**Как работает функция**:

1. **Проверка URL**: Функция проверяет, что в сценарии указан URL. Если URL отсутствует, функция возвращает `False`.
2. **Получение списка продуктов**: Функция вызывает метод `get_list_products_in_category` объекта `supplier` для получения списка URL продуктов в категории.
3. **Извлечение данных о продуктах**: Функция проходит по списку URL продуктов и вызывает метод `grab_product_page` для каждого URL, чтобы извлечь данные о продукте.
4. **Экспорт данных**: Если данные о продуктах были успешно извлечены, функция вызывает метод `export_files` для экспорта данных в файл.
5. **Обработка пустых списков**: Если после извлечения данных список продуктов пуст, функция не вызывает метод экспорта файлов.

**Примеры**:

```python
from unittest.mock import MagicMock

# Mock the Supplier class
self.supplier = MagicMock()

# Set up the scenario with no URL
scenario = {'name': 'scenario1', 'url': None}

# Mock the scenarios attribute
self.supplier.scenarios = {'scenario1': scenario}

# Mock the get_list_products_in_category method
self.supplier.get_list_products_in_category = MagicMock(return_value=[])

# Assert the function returns False
self.assertFalse(self.supplier.run_scenario(scenario))
```

```python
from unittest.mock import MagicMock

# Mock the Supplier class
self.supplier = MagicMock()

# Set up the scenario with a valid URL
scenario = {'name': 'scenario2', 'url': 'https://example.com/products'}

# Mock the scenarios attribute
self.supplier.scenarios = {'scenario2': scenario}

# Mock the get_list_products_in_category method to return a list of product URLs
self.supplier.get_list_products_in_category = MagicMock(return_value=['https://example.com/products/1', 'https://example.com/products/2'])

# Mock the grab_product_page method to return True
self.supplier.grab_product_page = MagicMock(return_value=True)

# Mock the export_files method
self.supplier.export_files = MagicMock()

# Assert the function returns True
self.assertTrue(self.supplier.run_scenario(scenario))

# Assert the product list contains 2 products
self.assertEqual(len(self.supplier.p), 2)

# Assert the export_files method was called with the correct arguments
self.supplier.export_files.assert_called_once_with(self.supplier, self.supplier.p, 'test_export-1', ['csv'])
```

```python
from unittest.mock import MagicMock

# Mock the Supplier class
self.supplier = MagicMock()

# Set up the scenario with a valid URL
scenario = {'name': 'scenario3', 'url': 'https://example.com/products'}

# Mock the scenarios attribute
self.supplier.scenarios = {'scenario3': scenario}

# Mock the get_list_products_in_category method to return a list of product URLs
self.supplier.get_list_products_in_category = MagicMock(return_value=['https://example.com/products/1'])

# Mock the grab_product_page method to return False
self.supplier.grab_product_page = MagicMock(return_value=False)

# Mock the export_files method
self.supplier.export_files = MagicMock()

# Assert the function returns False
self.assertFalse(self.supplier.run_scenario(scenario))

# Assert the product list is empty
self.assertEqual(len(self.supplier.p), 0)

# Assert the export_files method was not called
self.supplier.export_files.assert_not_called()
```