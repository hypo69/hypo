# Модуль `test_execute_scenarios`

## Обзор

Модуль `test_execute_scenarios` содержит набор тестов для проверки функциональности выполнения сценариев, включая запуск списка файлов сценариев, запуск отдельного файла сценария и извлечение данных со страницы продукта. Он использует библиотеку `unittest` и `MagicMock` для имитации объектов и проверки взаимодействия между различными компонентами.

## Подробней

Этот модуль важен для обеспечения правильной работы системы выполнения сценариев, которая является ключевой частью процесса сбора данных о продуктах. Тесты охватывают различные случаи использования, такие как запуск сценариев из файлов, обработка сценариев с использованием `webdriver` или `api`, а также обработка ситуаций, когда сценарии отсутствуют или не содержат необходимых данных. Расположение файла в структуре проекта указывает на то, что это модуль тестирования, предназначенный для проверки корректности работы модулей, связанных с выполнением сценариев.

## Классы

### `TestRunListOfScenarioFiles`

**Описание**: Класс `TestRunListOfScenarioFiles` содержит тесты для функции `run_scenarios`, которая отвечает за запуск списка файлов сценариев.

**Как работает класс**:
Класс использует `unittest.TestCase` для определения тестовых методов. `MagicMock` используется для имитации объекта `Supplier` и его атрибутов. Тесты проверяют, что функция `run_scenarios` правильно обрабатывает сценарии, запускает необходимые модули и устанавливает правильные значения атрибутов объекта `Supplier`.

**Методы**:
- `test_with_scenario_files_...ed`: Тест проверяет запуск сценариев из списка файлов.
- `test_with_no_scenario_files_...ed`: Тест проверяет запуск сценариев, когда список файлов не предоставлен.

#### `test_with_scenario_files_...ed`

```python
def test_with_scenario_files_...ed(self):
    ...
```

**Описание**: Тест проверяет запуск сценариев из предоставленного списка файлов.

**Как работает функция**:
1. Создается имитация объекта `Supplier` с помощью `MagicMock`.
2. Определяется список файлов сценариев `scenario_files`.
3. Устанавливаются значения атрибутов `settings` объекта `Supplier`.
4. Вызывается функция `run_scenarios` с имитированным объектом `Supplier` и списком файлов сценариев.
5. Проверяется, что функция вернула `True`.
6. Проверяется, что метод `build_shop_categories` не был вызван.
7. Проверяется, что атрибуты `current_scenario_filename` и `settings['last_runned_scenario']` были установлены в правильные значения.

**Параметры**:
- `self` (TestRunListOfScenarioFiles): Экземпляр класса `TestRunListOfScenarioFiles`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если какое-либо из утверждений не выполняется.

**Примеры**:
```python
import unittest
from unittest.mock import MagicMock
from execute_scenarios import run_scenarios

class TestRunListOfScenarioFiles(unittest.TestCase):
    def test_with_scenario_files_...ed(self):
        s = MagicMock()
        scenario_files = ["scenario1.json", "scenario2.json"]
        s.settings = {
            'check categories on site': False,
            'scenarios': ["default1.json", "default2.json"]
        }
        
        result = run_scenarios(s, scenario_files)
        
        self.assertTrue(result)
        s.related_modules.build_shop_categories.assert_not_called()
        self.assertEqual(s.current_scenario_filename, "scenario2.json")
        self.assertEqual(s.settings['last_runned_scenario'], "scenario2.json")
```

#### `test_with_no_scenario_files_...ed`

```python
def test_with_no_scenario_files_...ed(self):
    ...
```

**Описание**: Тест проверяет запуск сценариев, когда список файлов сценариев не предоставлен.

**Как работает функция**:
1. Создается имитация объекта `Supplier` с помощью `MagicMock`.
2. Устанавливаются значения атрибутов `settings` объекта `Supplier`.
3. Вызывается функция `run_scenarios` с имитированным объектом `Supplier`.
4. Проверяется, что функция вернула `True`.
5. Проверяется, что метод `build_shop_categories` был вызван один раз.
6. Проверяется, что атрибуты `current_scenario_filename` и `settings['last_runned_scenario']` были установлены в правильные значения.

**Параметры**:
- `self` (TestRunListOfScenarioFiles): Экземпляр класса `TestRunListOfScenarioFiles`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если какое-либо из утверждений не выполняется.

**Примеры**:
```python
import unittest
from unittest.mock import MagicMock
from execute_scenarios import run_scenarios

class TestRunListOfScenarioFiles(unittest.TestCase):
    def test_with_no_scenario_files_...ed(self):
        s = MagicMock()
        s.settings = {
            'check categories on site': True,
            'scenarios': ["default1.json", "default2.json"]
        }
        
        result = run_scenarios(s)
        
        self.assertTrue(result)
        s.related_modules.build_shop_categories.assert_called_once()
        self.assertEqual(s.current_scenario_filename, "default2.json")
        self.assertEqual(s.settings['last_runned_scenario'], "default2.json")
```

### `TestRunScenarioFile`

**Описание**: Класс `TestRunScenarioFile` содержит тесты для функции `run_scenario_file`, которая отвечает за запуск отдельного файла сценария.

**Как работает класс**:
Класс использует `unittest.TestCase` для определения тестовых методов. `MagicMock` используется для имитации объекта `Supplier` и его атрибутов. `patch` используется для замены функций `j_loads` и `run_scenario` имитированными объектами. Тесты проверяют, что функция `run_scenario_file` правильно загружает сценарии из файла, вызывает необходимые функции и обрабатывает различные ситуации, такие как отсутствие сценариев.

**Методы**:
- `setUp`: Метод для настройки тестовой среды перед каждым тестом.
- `test_run_scenario_file_webdriver`: Тест проверяет запуск сценария с использованием `webdriver`.
- `test_run_scenario_file_api`: Тест проверяет запуск сценария с использованием `api`.
- `test_run_scenario_file_no_scenarios`: Тест проверяет обработку ситуации, когда файл сценария не содержит сценариев.

#### `setUp`

```python
def setUp(self):
    ...
```

**Описание**: Метод для настройки тестовой среды перед каждым тестом.

**Как работает функция**:
1. Создается имитация объекта `Supplier` с помощью `MagicMock`.
2. Устанавливаются значения атрибутов `current_scenario_filename`, `settings`, `dir_export_imagesECTORY_FOR_STORE` и `scenarios` объекта `Supplier`.

**Параметры**:
- `self` (TestRunScenarioFile): Экземпляр класса `TestRunScenarioFile`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `None`

**Примеры**:
```python
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from execute_scenarios import run_scenario_file

class TestRunScenarioFile(unittest.TestCase):
    def setUp(self):
        self.s = MagicMock()
        self.s.current_scenario_filename = "test_scenario.json"
        self.s.settings = {
            "parcing method [webdriver|api]": "webdriver"
        }
        self.s.dir_export_imagesECTORY_FOR_STORE = "/path/to/images"
        self.s.scenarios = {
            "scenario1": {
                "url": "https://example.com",
                "steps": []
            },
            "scenario2": {
                "url": None,
                "steps": []
            }
        }
```

#### `test_run_scenario_file_webdriver`

```python
def test_run_scenario_file_webdriver(self):
    ...
```

**Описание**: Тест проверяет запуск сценария с использованием `webdriver`.

**Как работает функция**:
1. Используется `patch` для замены функций `j_loads` и `run_scenario` имитированными объектами.
2. Устанавливается возвращаемое значение функции `j_loads` равным словарю с имитированными сценариями.
3. Вызывается функция `run_scenario_file` с имитированным объектом `Supplier` и именем файла сценария.
4. Проверяется, что функция `j_loads` была вызвана один раз с правильным аргументом.
5. Проверяется, что функция `run_scenario` была вызвана с правильными аргументами.
6. Проверяется, что функция `run_scenario` не была вызвана с неверными аргументами.

**Параметры**:
- `self` (TestRunScenarioFile): Экземпляр класса `TestRunScenarioFile`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если какое-либо из утверждений не выполняется.

**Примеры**:
```python
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from execute_scenarios import run_scenario_file

class TestRunScenarioFile(unittest.TestCase):
    def test_run_scenario_file_webdriver(self):
        with patch("your_module.j_loads") as mock_j_loads:
            mock_j_loads.return_value = {"scenarios": self.s.scenarios}
            with patch("your_module.run_scenario") as mock_run_scenario:
                run_scenario_file(self.s, "test_scenario.json")
                mock_j_loads.assert_called_once_with("/path/to/scenarios/test_scenario.json")
                mock_run_scenario.assert_any_call(self.s, self.s.scenarios["scenario1"])
                mock_run_scenario.assert_not_called_with(self.s, self.s.scenarios["scenario2"])
```

#### `test_run_scenario_file_api`

```python
def test_run_scenario_file_api(self):
    ...
```

**Описание**: Тест проверяет запуск сценария с использованием `api`.

**Как работает функция**:
1. Устанавливается значение атрибута `settings["parcing method [webdriver|api]"]` объекта `Supplier` равным `"api"`.
2. Используется `patch` для замены функции `related_modules.run_scenario_file_via_api` имитированным объектом.
3. Вызывается функция `run_scenario_file` с имитированным объектом `Supplier` и именем файла сценария.
4. Проверяется, что функция `run_scenario_file_via_api` была вызвана один раз с правильными аргументами.

**Параметры**:
- `self` (TestRunScenarioFile): Экземпляр класса `TestRunScenarioFile`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если какое-либо из утверждений не выполняется.

**Примеры**:
```python
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from execute_scenarios import run_scenario_file

class TestRunScenarioFile(unittest.TestCase):
    def test_run_scenario_file_api(self):
        self.s.settings["parcing method [webdriver|api]"] = "api"
        with patch("your_module.related_modules.run_scenario_file_via_api") as mock_run_scenario_file_via_api:
            run_scenario_file(self.s, "test_scenario.json")
            mock_run_scenario_file_via_api.assert_called_once_with(self.s, "test_scenario.json")
```

#### `test_run_scenario_file_no_scenarios`

```python
def test_run_scenario_file_no_scenarios(self):
    ...
```

**Описание**: Тест проверяет обработку ситуации, когда файл сценария не содержит сценариев.

**Как работает функция**:
1. Используется `patch` для замены функций `j_loads` и `logger.error` имитированными объектами.
2. Устанавливается возвращаемое значение функции `j_loads` равным словарю с `None` в качестве значения ключа `"scenarios"`.
3. Вызывается функция `run_scenario_file` с имитированным объектом `Supplier` и именем файла сценария.
4. Проверяется, что функция вернула `False`.
5. Проверяется, что функция `logger.error` была вызвана один раз с правильным сообщением об ошибке.

**Параметры**:
- `self` (TestRunScenarioFile): Экземпляр класса `TestRunScenarioFile`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если какое-либо из утверждений не выполняется.

**Примеры**:
```python
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from execute_scenarios import run_scenario_file

class TestRunScenarioFile(unittest.TestCase):
    def test_run_scenario_file_no_scenarios(self):
        with patch("your_module.j_loads") as mock_j_loads:
            mock_j_loads.return_value = {"scenarios": None}
            with patch("your_module.logger.error") as mocklogger_console_error:
                self.assertFalse(run_scenario_file(self.s, "test_scenario.json"))
                mocklogger_console_error.assert_called_once_with("Возможно файл test_scenario.json не содержит сценариев")
```

### `TestGrabProductPage`

**Описание**: Класс `TestGrabProductPage` содержит тесты для функции `grab_product_page`, которая отвечает за извлечение данных со страницы продукта.

**Как работает класс**:
Класс использует `unittest.TestCase` для определения тестовых методов. Объект `Supplier` создается в методе `setUp`. Тесты проверяют, что функция `grab_product_page` правильно обрабатывает данные, добавляет продукты в список и обрабатывает ситуации, когда необходимые данные отсутствуют.

**Методы**:
- `setUp`: Метод для настройки тестовой среды перед каждым тестом.
- `test_grab_product_page_succesStringFormatterul`: Тест проверяет успешное извлечение данных со страницы продукта.
- `test_grab_product_page_failure`: Тест проверяет обработку ситуации, когда необходимые данные отсутствуют.

#### `setUp`

```python
def setUp(self):
    ...
```

**Описание**: Метод для настройки тестовой среды перед каждым тестом.

**Как работает функция**:
1. Создается экземпляр класса `Supplier`.

**Параметры**:
- `self` (TestGrabProductPage): Экземпляр класса `TestGrabProductPage`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `None`

**Примеры**:
```python
import unittest
from unittest import Supplier # Предполагается, что класс Supplier существует
from unittest.mock import MagicMock
from execute_scenarios import grab_product_page

class TestGrabProductPage(unittest.TestCase):
    def setUp(self):
        self.s = Supplier()
```

#### `test_grab_product_page_succesStringFormatterul`

```python
def test_grab_product_page_succesStringFormatterul(self):
    ...
```

**Описание**: Тест проверяет успешное извлечение данных со страницы продукта.

**Как работает функция**:
1. Устанавливается имитированная функция `grab_product_page` объекта `Supplier`, которая возвращает словарь с данными продукта.
2. Вызывается функция `grab_product_page` с имитированным объектом `Supplier`.
3. Проверяется, что функция вернула `True`.
4. Проверяется, что длина списка продуктов `self.s.p` равна 1.
5. Проверяется, что данные продукта в списке `self.s.p` соответствуют ожидаемым значениям.

**Параметры**:
- `self` (TestGrabProductPage): Экземпляр класса `TestGrabProductPage`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если какое-либо из утверждений не выполняется.

**Примеры**:
```python
import unittest
from unittest import Supplier # Предполагается, что класс Supplier существует
from unittest.mock import MagicMock
from execute_scenarios import grab_product_page

class TestGrabProductPage(unittest.TestCase):
    def test_grab_product_page_succesStringFormatterul(self):
        self.s.grab_product_page = lambda _: {'id': '123', 'price': 19.99, 'name': 'Product Name'}
        result = grab_product_page(self.s)
        self.assertTrue(result)
        self.assertEqual(len(self.s.p), 1)
        self.assertEqual(self.s.p[0]['id'], '123')
        self.assertEqual(self.s.p[0]['price'], 19.99)
        self.assertEqual(self.s.p[0]['name'], 'Product Name')
```

#### `test_grab_product_page_failure`

```python
def test_grab_product_page_failure(self):
    ...
```

**Описание**: Тест проверяет обработку ситуации, когда необходимые данные отсутствуют.

**Как работает функция**:
1. Устанавливается имитированная функция `grab_product_page` объекта `Supplier`, которая возвращает словарь с неполными данными продукта.
2. Вызывается функция `grab_product_page` с имитированным объектом `Supplier`.
3. Проверяется, что функция вернула `False`.
4. Проверяется, что длина списка продуктов `self.s.p` равна 0.

**Параметры**:
- `self` (TestGrabProductPage): Экземпляр класса `TestGrabProductPage`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если какое-либо из утверждений не выполняется.

**Примеры**:
```python
import unittest
from unittest import Supplier # Предполагается, что класс Supplier существует
from unittest.mock import MagicMock
from execute_scenarios import grab_product_page

class TestGrabProductPage(unittest.TestCase):
    def test_grab_product_page_failure(self):
        self.s.grab_product_page = lambda _: {'name': 'Product Name'}
        result = grab_product_page(self.s)
        self.assertFalse(result)
        self.assertEqual(len(self.s.p), 0)
```

### `TestRunScenario`

**Описание**: Класс `TestRunScenario` содержит тесты для метода `run_scenario` класса `Supplier`, который отвечает за выполнение отдельного сценария.

**Как работает класс**:
Класс использует `unittest.TestCase` для определения тестовых методов. Создается экземпляр класса `Supplier` и настраиваются его атрибуты в методе `setUp`. Используется `MagicMock` для имитации методов класса `Supplier`. Тесты проверяют, что метод `run_scenario` правильно обрабатывает различные сценарии, такие как отсутствие URL, наличие валидного URL и экспорт пустых списков.

**Методы**:
- `setUp`: Метод для настройки тестовой среды перед каждым тестом.
- `tearDown`: Метод для очистки тестовой среды после каждого теста.
- `test_run_scenario_no_url`: Тест проверяет сценарий, когда URL отсутствует.
- `test_run_scenario_valid_url`: Тест проверяет сценарий с валидным URL.
- `test_run_scenario_export_empty_list`: Тест проверяет сценарий, когда список продуктов для экспорта пуст.

#### `setUp`

```python
def setUp(self):
    ...
```

**Описание**: Метод для настройки тестовой среды перед каждым тестом.

**Как работает функция**:
1. Создается экземпляр класса `Supplier`.
2. Устанавливаются значения атрибутов `settings`, `current_scenario_filename`, `export_file_name`, `dir_export_imagesECTORY_FOR_STORE` и `p` объекта `Supplier`.

**Параметры**:
- `self` (TestRunScenario): Экземпляр класса `TestRunScenario`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `None`

**Примеры**:
```python
import unittest
from unittest import Supplier
from unittest.mock import MagicMock
from execute_scenarios import run_scenario

class TestRunScenario(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier()
        self.supplier.settings['parcing method [webdriver|api]'] = 'webdriver'
        self.supplier.current_scenario_filename = 'test_scenario.json'
        self.supplier.export_file_name = 'test_export'
        self.supplier.dir_export_imagesECTORY_FOR_STORE = '/test/path'
        self.supplier.p = []
```

#### `tearDown`

```python
def tearDown(self):
    ...
```

**Описание**: Метод для очистки тестовой среды после каждого теста.

**Как работает функция**:
- Функция ничего не выполняет (`...`).

**Параметры**:
- `self` (TestRunScenario): Экземпляр класса `TestRunScenario`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `None`

**Примеры**:
```python
import unittest
from unittest import Supplier
from unittest.mock import MagicMock
from execute_scenarios import run_scenario

class TestRunScenario(unittest.TestCase):
    def tearDown(self):
        pass  # or replace ... with pass
```

#### `test_run_scenario_no_url`

```python
def test_run_scenario_no_url(self):
    ...
```

**Описание**: Тест проверяет сценарий, когда URL отсутствует.

**Как работает функция**:
1. Создается словарь `scenario` с `None` в качестве значения ключа `url`.
2. Устанавливается словарь `scenarios` объекта `Supplier` с созданным сценарием.
3. Имитируется метод `get_list_products_in_category` объекта `Supplier`, который возвращает пустой список.
4. Проверяется, что метод `run_scenario` объекта `Supplier` возвращает `False`.

**Параметры**:
- `self` (TestRunScenario): Экземпляр класса `TestRunScenario`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если какое-либо из утверждений не выполняется.

**Примеры**:
```python
import unittest
from unittest import Supplier
from unittest.mock import MagicMock
from execute_scenarios import run_scenario

class TestRunScenario(unittest.TestCase):
    def test_run_scenario_no_url(self):
        scenario = {'name': 'scenario1', 'url': None}
        self.supplier.scenarios = {'scenario1': scenario}
        self.supplier.get_list_products_in_category = MagicMock(return_value=[])
        self.assertFalse(self.supplier.run_scenario(scenario))
```

#### `test_run_scenario_valid_url`

```python
def test_run_scenario_valid_url(self):
    ...
```

**Описание**: Тест проверяет сценарий с валидным URL.

**Как работает функция**:
1. Создается словарь `scenario` с валидным URL.
2. Устанавливается словарь `scenarios` объекта `Supplier` с созданным сценарием.
3. Имитируется метод `get_list_products_in_category` объекта `Supplier`, который возвращает список URL продуктов.
4. Имитируется метод `grab_product_page` объекта `Supplier`, который возвращает `True`.
5. Имитируется метод `export_files` объекта `Supplier`.
6. Проверяется, что метод `run_scenario` объекта `Supplier` возвращает `True`.
7. Проверяется, что длина списка продуктов `self.supplier.p` равна 2.
8. Проверяется, что метод `export_files` был вызван один раз с правильными аргументами.

**Параметры**:
- `self` (TestRunScenario): Экземпляр класса `TestRunScenario`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если какое-либо из утверждений не выполняется.

**Примеры**:
```python
import unittest
from unittest import Supplier
from unittest.mock import MagicMock
from execute_scenarios import run_scenario

class TestRunScenario(unittest.TestCase):
    def test_run_scenario_valid_url(self):
        scenario = {'name': 'scenario2', 'url': 'https://example.com/products'}
        self.supplier.scenarios = {'scenario2': scenario}
        self.supplier.get_list_products_in_category = MagicMock(return_value=['https://example.com/products/1', 'https://example.com/products/2'])
        self.supplier.grab_product_page = MagicMock(return_value=True)
        self.supplier.export_files = MagicMock()
        self.assertTrue(self.supplier.run_scenario(scenario))
        self.assertEqual(len(self.supplier.p), 2)
        self.supplier.export_files.assert_called_once_with(self.supplier, self.supplier.p, 'test_export-1', ['csv'])
```

#### `test_run_scenario_export_empty_list`

```python
def test_run_scenario_export_empty_list(self):
    ...
```

**Описание**: Тест проверяет сценарий, когда список продуктов для экспорта пуст.

**Как работает функция**:
1. Создается словарь `scenario` с валидным URL.
2. Устанавливается словарь `scenarios` объекта `Supplier` с созданным сценарием.
3. Имитируется метод `get_list_products_in_category` объекта `Supplier`, который возвращает список URL продуктов.
4. Имитируется метод `grab_product_page` объекта `Supplier`, который возвращает `False`.
5. Имитируется метод `export_files` объекта `Supplier`.
6. Проверяется, что метод `run_scenario` объекта `Supplier` возвращает `False`.
7. Проверяется, что длина списка продуктов `self.supplier.p` равна 0.
8. Проверяется, что метод `export_files` не был вызван.

**Параметры**:
- `self` (TestRunScenario): Экземпляр класса `TestRunScenario`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `AssertionError`: Если какое-либо из утверждений не выполняется.

**Примеры**:
```python
import unittest
from unittest import Supplier
from unittest.mock import MagicMock
from execute_scenarios import run_scenario

class TestRunScenario(unittest.TestCase):
    def test_run_scenario_export_empty_list(self):
        scenario = {'name': 'scenario3', 'url': 'https://example.com/products'}
        self.supplier.scenarios = {'scenario3': scenario}
        self.supplier.get_list_products_in_category = MagicMock(return_value=['https://example.com/products/1'])
        self.supplier.grab_product_page = MagicMock(return_value=False)
        self.supplier.export_files = MagicMock()
        self.assertFalse(self.supplier.run_scenario(scenario))
        self.assertEqual(len(self.supplier.p), 0)
        self.supplier.export_files.assert_not_called()
```

## Функции

### `run_scenarios`

```python
def run_scenarios(s, scenario_files: Optional[list[str]] = None) -> bool:
    ...
```

**Описание**: Функция запускает сценарии из списка файлов или из настроек поставщика.

**Как работает функция**:
Функция сначала проверяет, предоставлен ли список файлов сценариев `scenario_files`. Если да, то она перебирает файлы в списке и запускает каждый файл сценария с помощью функции `run_scenario_file`. Если список файлов не предоставлен, функция использует список файлов сценариев, указанных в настройках поставщика (`s.settings['scenarios']`). Если включена проверка категорий на сайте (`s.settings['check categories on site']`), функция также вызывает метод `build_shop_categories` поставщика.

**Параметры**:
- `s` (Supplier): Объект поставщика с настройками и методами для запуска сценариев.
- `scenario_files` (Optional[list[str]], optional): Список файлов сценариев для запуска. По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если все сценарии были успешно запущены, `False` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при запуске сценария.

**Примеры**:
```python
from unittest.mock import MagicMock
from execute_scenarios import run_scenarios, run_scenario_file

# Пример запуска сценариев из списка файлов
s = MagicMock()
s.settings = {'check categories on site': False, 'scenarios': ["default1.json", "default2.json"]}
scenario_files = ["scenario1.json", "scenario2.json"]
result = run_scenarios(s, scenario_files)

# Пример запуска сценариев из настроек поставщика
s = MagicMock()
s.settings = {'check categories on site': True, 'scenarios': ["default1.json", "default2.json"]}
s.related_modules.build_shop_categories = MagicMock()
run_scenario_file = MagicMock() #  определена как MagicMock
result = run_scenarios(s)
```

### `run_scenario_file`

```python
def run_scenario_file(s, scenario_file_name: str) -> bool:
    ...
```

**Описание**: Функция запускает сценарии из указанного файла сценария.

**Как работает функция**:
Функция загружает сценарии из файла, используя функцию `j_loads`. Если метод парсинга установлен как `"api"`, функция вызывает `run_scenario_file_via_api` из `s.related_modules`. В противном случае функция перебирает сценарии в файле и запускает каждый сценарий с помощью функции `run_scenario`.

**Параметры**:
- `s` (Supplier): Объект поставщика с настройками и методами для запуска сценариев.
- `scenario_file_name` (str): Имя файла сценария для запуска.

**Возвращает**:
- `bool`: `True`, если все сценарии были успешно запущены, `False` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при загрузке или запуске сценария.

**Примеры**:
```python
from unittest.mock import MagicMock
from execute_scenarios import run_scenario_file

# Пример запуска сценария с использованием webdriver
s = MagicMock()
s.settings = {"parcing method [webdriver|api]": "webdriver"}
s.dir_export_imagesECTORY_FOR_STORE = "/path/to/images"
s.scenarios = {"scenario1": {"url": "https://example.com", "steps": []}}
s.run_scenario = MagicMock(return_value=True)
run_scenario_file(s, "test_scenario.json")

# Пример запуска сценария с использованием api
s = MagicMock()
s.settings = {"parcing method [webdriver|api]": "api"}
s.related_modules.run_scenario_file_via_api = MagicMock(return_value=True)
run_scenario_file(s, "test_scenario.json")
```

### `run_scenario`

```python
def run_scenario(self, scenario: dict) -> bool:
    ...
```

**Описание**: Метод класса `Supplier`, который выполняет один сценарий.

**Как работает функция**:
Функция проверяет, установлен ли URL в сценарии. Если URL отсутствует, функция возвращает `False`. В противном случае функция получает список продуктов в категории, используя метод `get_list_products_in_category`. Затем функция перебирает URL продуктов и извлекает данные о продукте, используя метод `grab_product_page`. Если данные успешно извлечены, продукт добавляется в список `self.p`. После извлечения данных о всех продуктах функция экспортирует список продуктов, используя метод `export_files`.

**Параметры**:
- `self` (Supplier): Объект поставщика.
- `scenario` (dict): Словарь, содержащий информацию о сценарии, включая URL.

**Возвращает**:
- `bool`: `True`, если сценарий был успешно выполнен, `False` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при выполнении сценария.

**Примеры**:
```python
from unittest.mock import MagicMock
from execute_scenarios import run_scenario

# Пример запуска сценария с валидным URL
supplier = MagicMock()
supplier.settings = {'parcing method [webdriver|api]': 'webdriver'}
supplier.current_scenario_filename = 'test_scenario.json'
supplier.export_file_name = 'test_export'
supplier.dir_export_imagesECTORY_FOR_STORE = '/test/path'
supplier.p = []
supplier.get_list_products_in_category = MagicMock(return_value=['https://example.com/products/1', 'https://example.com/products/2'])
supplier.grab_product_page = MagicMock(return_value=True)
supplier.export_files = MagicMock()
scenario = {'name': 'scenario2', 'url': 'https://example.com/products'}
supplier.run_scenario(scenario)
```

### `grab_product_page`

```python
def grab_product_page(self) -> bool:
    ...
```

**Описание**: Метод класса `Supplier`, который извлекает данные со страницы продукта.

**Как работает функция**:
Функция вызывает метод `grab_product_page` объекта `Supplier` для извлечения данных о продукте. Если данные содержат `id`, `price` и `name`, продукт добавляется в список `self.p`.

**Па