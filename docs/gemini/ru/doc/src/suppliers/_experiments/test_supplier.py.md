# Модуль для тестирования поставщиков

## Обзор

Модуль содержит класс `TestSupplier`, который используется для тестирования класса `Supplier`. Класс `Supplier` предназначен для работы с данными о поставщиках, такими как ID поставщика, правила ценообразования, параметры для входа в систему, URL для начала работы и сценарии.

## Подробней

Этот модуль содержит набор тестов для проверки корректной работы класса `Supplier`. Тесты охватывают различные аспекты инициализации класса, загрузки настроек и выполнения сценариев. Модуль использует `unittest` для организации тестов и `unittest.mock` для имитации внешних зависимостей, таких как чтение файлов и взаимодействие с веб-драйвером.

## Классы

### `TestSupplier`

**Описание**: Класс `TestSupplier` предназначен для тестирования функциональности класса `Supplier`.

**Наследует**:
- `unittest.TestCase`: Базовый класс для создания тестовых случаев в `unittest`.

**Атрибуты**:
- `supplier_prefix` (str): Префикс имени поставщика.
- `lang` (str): Язык поставщика.
- `method` (str): Метод парсинга ('web' или 'api').
- `supplier_settings` (dict): Настройки поставщика, включая ID, правила ценообразования, параметры для входа в систему, URL для начала работы и сценарии.
- `locators` (dict): Локаторы элементов веб-страницы.
- `supplier` (Supplier): Экземпляр класса `Supplier`, используемый для тестов.
- `settings_file` (Path): Путь к файлу настроек поставщика.
- `locators_file` (Path): Путь к файлу локаторов.

**Методы**:
- `setUp()`: Метод, выполняющийся перед каждым тестом. Инициализирует атрибуты класса для каждого тестового случая.
- `test_init_webdriver()`: Тестирует инициализацию класса `Supplier` с методом парсинга 'web'.
- `test_init_api()`: Тестирует инициализацию класса `Supplier` с методом парсинга 'api'.
- `test_supplier_load_settings_success()`: Тестирует успешную загрузку настроек поставщика.
- `test_supplier_load_settings_failure()`: Тестирует ситуацию, когда загрузка настроек поставщика завершается неудачей.
- `test_load_settings()`: Тестирует загрузку настроек.
- `test_load_settings_invalid_path()`: Тестирует загрузку настроек при неверном пути к файлу.
- `test_load_settings_invalid_locators_path()`: Тестирует загрузку настроек при неверном пути к файлу локаторов.
- `test_load_settings_api()`: Тестирует загрузку настроек для API.
- `test_load_related_functions()`: Тестирует загрузку связанных функций.
- `test_init()`: Тестирует инициализацию.
- `test_load_settings_success()`: Тестирует успешную загрузку настроек.
- `test_load_settings_failure()`: Тестирует неудачную загрузку настроек.
- `test_run_api()`: Тестирует запуск API.
- `test_run_scenario_files_success()`: Тестирует успешное выполнение файлов сценариев.
- `test_run_scenario_files_failure()`: Тестирует неудачное выполнение файлов сценариев.
- `test_run_with_login()`: Тестирует запуск с входом в систему.
- `test_run_without_login()`: Тестирует запуск без входа в систему.

## Функции

### `setUp`

```python
def setUp(self):
    """
    Подготавливает тестовую среду перед каждым тестом.

    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.

    Returns:
        None

    Raises:
        None

    Example:
        >>> test_supplier = TestSupplier()
        >>> test_supplier.setUp()
        >>> print(test_supplier.supplier_prefix)
        test_supplier
    """
    ...
```

**Назначение**:
Метод `setUp` инициализирует атрибуты класса `TestSupplier` перед каждым тестом. Это позволяет создать согласованную и предсказуемую среду для каждого тестового случая.

**Как работает функция**:
1. Устанавливает `supplier_prefix` в `'test_supplier'`.
2. Устанавливает `lang` в `'en'`.
3. Устанавливает `method` в `'web'`.
4. Определяет словарь `supplier_settings`, содержащий настройки поставщика, такие как `supplier_id`, `price_rule`, `if_login`, `login_url`, `start_url` и `scenarios`.
5. Определяет словарь `locators`, содержащий XPath-локаторы для различных элементов веб-страницы.
6. Создает экземпляр класса `Supplier` с именем `'example_supplier'`.
7. Определяет путь к файлу настроек поставщика (`settings_file`).
8. Определяет путь к файлу локаторов (`locators_file`).

**Примеры**:

```python
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
from mymodule.supplier import Supplier

class TestSupplier(unittest.TestCase):
    def setUp(self):
        self.supplier_prefix = 'test_supplier'
        self.lang = 'en'
        self.method = 'web'
        self.supplier_settings = {
            'supplier_id': '123',
            'price_rule': '*1.2',
            'if_login': True,
            'login_url': 'http://example.com/login',
            'start_url': 'http://example.com/start',
            'parcing method [webdriver|api]': 'webdriver',
            'scenarios': [
                {'name': 'scenario1', 'file': 'scenario1.json'},
                {'name': 'scenario2', 'file': 'scenario2.json'},
            ]
        }
        self.locators = {
            'search_box': {'xpath': '//*[@id="search-box"]'},
            'search_button': {'xpath': '//*[@id="search-button"]'},
            'product_name': {'xpath': '//*[@id="product-name"]'},
            'product_price': {'xpath': '//*[@id="product-price"]'},
        }
        self.supplier = Supplier('example_supplier')
        self.settings_file = Path(__file__).parent / 'data/example_supplier/example_supplier.json'
        self.locators_file = Path(__file__).parent / 'data/example_supplier/locators.json'
```

### `test_init_webdriver`

```python
@patch('mymodule.supplier.gs.j_loads')
@patch('mymodule.supplier.Driver')
def test_init_webdriver(self, mock_driver, mock_j_loads):
    """
    Тестирует инициализацию класса `Supplier` с методом парсинга 'web'.

    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.
        mock_driver (MagicMock): Заглушка для класса Driver.
        mock_j_loads (MagicMock): Заглушка для функции j_loads.

    Returns:
        None

    Raises:
        AssertionError: Если утверждения не выполняются.

    Example:
        >>> test_supplier = TestSupplier()
        >>> test_supplier.setUp()
        >>> test_supplier.test_init_webdriver(MagicMock(), MagicMock())
    """
    ...
```

**Назначение**:
Метод `test_init_webdriver` тестирует инициализацию класса `Supplier` с методом парсинга `'web'`. Он проверяет, что атрибуты экземпляра класса `Supplier` правильно инициализированы на основе предоставленных настроек.

**Как работает функция**:

1. Используются декораторы `@patch` для замены `mymodule.supplier.gs.j_loads` и `mymodule.supplier.Driver` заглушками (`MagicMock`). Это позволяет изолировать тестируемый код и контролировать его поведение.
2. Устанавливается возвращаемое значение для `mock_j_loads` равным `self.supplier_settings`.
3. Устанавливается возвращаемое значение для `mock_driver` равным `MagicMock()`.
4. Создается экземпляр класса `Supplier` с параметрами `self.supplier_prefix`, `self.lang` и `self.method`.
5. Проверяются атрибуты созданного экземпляра класса `Supplier` на соответствие ожидаемым значениям из `self.supplier_settings`.
6. Проверяется, что функция `mock_j_loads` была вызвана с ожидаемым аргументом (`Path('suppliers', self.supplier_prefix, f'{self.supplier_prefix}.json')`).
7. Проверяется, что функция `mock_driver` была вызвана один раз.

**Примеры**:

```python
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
from mymodule.supplier import Supplier

class TestSupplier(unittest.TestCase):
    def setUp(self):
        self.supplier_prefix = 'test_supplier'
        self.lang = 'en'
        self.method = 'web'
        self.supplier_settings = {
            'supplier_id': '123',
            'price_rule': '*1.2',
            'if_login': True,
            'login_url': 'http://example.com/login',
            'start_url': 'http://example.com/start',
            'parcing method [webdriver|api]': 'webdriver',
            'scenarios': [
                {'name': 'scenario1', 'file': 'scenario1.json'},
                {'name': 'scenario2', 'file': 'scenario2.json'},
            ]
        }
        self.locators = {
            'search_box': {'xpath': '//*[@id="search-box"]'},
            'search_button': {'xpath': '//*[@id="search-button"]'},
            'product_name': {'xpath': '//*[@id="product-name"]'},
            'product_price': {'xpath': '//*[@id="product-price"]'},
        }
        self.supplier = Supplier('example_supplier')
        self.settings_file = Path(__file__).parent / 'data/example_supplier/example_supplier.json'
        self.locators_file = Path(__file__).parent / 'data/example_supplier/locators.json'

    @patch('mymodule.supplier.gs.j_loads')
    @patch('mymodule.supplier.Driver')
    def test_init_webdriver(self, mock_driver, mock_j_loads):
        mock_j_loads.return_value = self.supplier_settings
        mock_driver.return_value = MagicMock()
        supplier = Supplier(self.supplier_prefix, self.lang, self.method)
        self.assertEqual(supplier.supplier_prefix, self.supplier_prefix)
        self.assertEqual(supplier.lang, self.lang)
        self.assertEqual(supplier.scrapping_method, self.method)
        self.assertEqual(supplier.supplier_id, self.supplier_settings['supplier_id'])
        self.assertEqual(supplier.price_rule, self.supplier_settings['price_rule'])
        self.assertEqual(supplier.login_data['if_login'], self.supplier_settings['if_login'])
        self.assertEqual(supplier.login_data['login_url'], self.supplier_settings['login_url'])
        self.assertEqual(supplier.start_url, self.supplier_settings['start_url'])
        self.assertEqual(supplier.scenarios, self.supplier_settings['scenarios'])
        mock_j_loads.assert_called_once_with(Path('suppliers', self.supplier_prefix, f'{self.supplier_prefix}.json'))
        mock_driver.assert_called_once()
```

### `test_init_api`

```python
@patch('mymodule.supplier.gs.j_loads')
def test_init_api(self, mock_j_loads):
    """
    Тестирует инициализацию класса `Supplier` с методом парсинга 'api'.

    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.
        mock_j_loads (MagicMock): Заглушка для функции j_loads.

    Returns:
        None

    Raises:
        AssertionError: Если утверждения не выполняются.

    Example:
        >>> test_supplier = TestSupplier()
        >>> test_supplier.setUp()
        >>> test_supplier.test_init_api(MagicMock())
    """
    ...
```

**Назначение**:
Метод `test_init_api` тестирует инициализацию класса `Supplier` с методом парсинга `'api'`. Он проверяет, что атрибуты экземпляра класса `Supplier` правильно инициализированы на основе предоставленных настроек, когда используется API.

**Как работает функция**:

1. Используется декоратор `@patch` для замены `mymodule.supplier.gs.j_loads` заглушкой (`MagicMock`).
2. Устанавливается значение `self.method` в `'api'`.
3. Устанавливается возвращаемое значение для `mock_j_loads` равным `self.supplier_settings`.
4. Создается экземпляр класса `Supplier` с параметрами `self.supplier_prefix`, `self.lang` и `self.method`.
5. Проверяются атрибуты созданного экземпляра класса `Supplier` на соответствие ожидаемым значениям из `self.supplier_settings`.
6. Проверяется, что функция `mock_j_loads` была вызвана с ожидаемым аргументом (`Path('suppliers', self.supplier_prefix, f'{self.supplier_prefix}.json')`).

**Примеры**:

```python
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
from mymodule.supplier import Supplier

class TestSupplier(unittest.TestCase):
    def setUp(self):
        self.supplier_prefix = 'test_supplier'
        self.lang = 'en'
        self.method = 'web'
        self.supplier_settings = {
            'supplier_id': '123',
            'price_rule': '*1.2',
            'if_login': True,
            'login_url': 'http://example.com/login',
            'start_url': 'http://example.com/start',
            'parcing method [webdriver|api]': 'webdriver',
            'scenarios': [
                {'name': 'scenario1', 'file': 'scenario1.json'},
                {'name': 'scenario2', 'file': 'scenario2.json'},
            ]
        }
        self.locators = {
            'search_box': {'xpath': '//*[@id="search-box"]'},
            'search_button': {'xpath': '//*[@id="search-button"]'},
            'product_name': {'xpath': '//*[@id="product-name"]'},
            'product_price': {'xpath': '//*[@id="product-price"]'},
        }
        self.supplier = Supplier('example_supplier')
        self.settings_file = Path(__file__).parent / 'data/example_supplier/example_supplier.json'
        self.locators_file = Path(__file__).parent / 'data/example_supplier/locators.json'

    @patch('mymodule.supplier.gs.j_loads')
    def test_init_api(self, mock_j_loads):
        self.method = 'api'
        mock_j_loads.return_value = self.supplier_settings
        supplier = Supplier(self.supplier_prefix, self.lang, self.method)
        self.assertEqual(supplier.supplier_prefix, self.supplier_prefix)
        self.assertEqual(supplier.lang, self.lang)
        self.assertEqual(supplier.scrapping_method, self.method)
        self.assertEqual(supplier.supplier_id, self.supplier_settings['supplier_id'])
        self.assertEqual(supplier.price_rule, self.supplier_settings['price_rule'])
        self.assertEqual(supplier.login_data['if_login'], self.supplier_settings['if_login'])
        self.assertEqual(supplier.login_data['login_url'], self.supplier_settings['login_url'])
        self.assertEqual(supplier.start_url, self.supplier_settings['start_url'])
        self.assertEqual(supplier.scenarios, self.supplier_settings['scenarios'])
        mock_j_loads.assert_called_once_with(Path('suppliers', self.supplier_prefix, f'{self.supplier_prefix}.json'))
```

### `test_supplier_load_settings_success`

```python
def test_supplier_load_settings_success():
    """
    Тестирует успешную загрузку настроек поставщика.

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: Если утверждения не выполняются.

    Example:
        >>> TestSupplier.test_supplier_load_settings_success()
    """
    ...
```

**Назначение**:
Метод `test_supplier_load_settings_success` тестирует успешную загрузку настроек поставщика. Он проверяет, что атрибуты экземпляра класса `Supplier` правильно инициализированы значениями по умолчанию, когда настройки успешно загружены.

**Как работает функция**:

1. Создается экземпляр класса `Supplier` с `supplier_prefix='dummy'`.
2. Проверяется, что `supplier.supplier_id` равно `'dummy'`.
3. Проверяется, что `supplier.price_rule` равно `'dummy'`.
4. Проверяется, что `supplier.login_data` равно `{'if_login': None, 'login_url': None, 'user': None, 'password': None}`.
5. Проверяется, что `supplier.start_url` равно `'dummy'`.
6. Проверяется, что `supplier.scrapping_method` равно `'web'`.
7. Проверяется, что `supplier.scenarios` равно `[]`.

**Примеры**:

```python
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
from mymodule.supplier import Supplier

class TestSupplier(unittest.TestCase):
    def test_supplier_load_settings_success():
        supplier = Supplier(supplier_prefix='dummy')
        assert supplier.supplier_id == 'dummy'
        assert supplier.price_rule == 'dummy'
        assert supplier.login_data == {
            'if_login': None,
            'login_url': None,
            'user': None,
            'password': None,
        }
        assert supplier.start_url == 'dummy'
        assert supplier.scrapping_method == 'web'
        assert supplier.scenarios == []
```

### `test_supplier_load_settings_failure`

```python
def test_supplier_load_settings_failure():
    """
    Тестирует ситуацию, когда загрузка настроек поставщика завершается неудачей.

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: Если утверждения не выполняются.

    Example:
        >>> TestSupplier.test_supplier_load_settings_failure()
    """
    ...
```

**Назначение**:
Метод `test_supplier_load_settings_failure` тестирует ситуацию, когда загрузка настроек поставщика завершается неудачей. Он проверяет, что атрибуты экземпляра класса `Supplier` правильно инициализированы значением `None` или пустой строкой, когда настройки не могут быть загружены.

**Как работает функция**:

1. Создается экземпляр класса `Supplier` с `supplier_prefix='nonexistent'`.
2. Проверяется, что `supplier.supplier_id` равно `None`.
3. Проверяется, что `supplier.price_rule` равно `None`.
4. Проверяется, что `supplier.login_data` равно `{'if_login': None, 'login_url': None, 'user': None, 'password': None}`.
5. Проверяется, что `supplier.start_url` равно `None`.
6. Проверяется, что `supplier.scrapping_method` равно `''`.

**Примеры**:

```python
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
from mymodule.supplier import Supplier

class TestSupplier(unittest.TestCase):
    def test_supplier_load_settings_failure():
        supplier = Supplier(supplier_prefix='nonexistent')
        assert supplier.supplier_id == None
        assert supplier.price_rule == None
        assert supplier.login_data == {
            'if_login': None,
            'login_url': None,
            'user': None,
            'password': None,
        }
        assert supplier.start_url == None
        assert supplier.scrapping_method == ''
```

### `test_load_settings`

```python
def test_load_settings(supplier):
    """
    Тестирует загрузку настроек.

    Args:
        supplier (Supplier): Экземпляр класса Supplier.

    Returns:
        None

    Raises:
        AssertionError: Если утверждения не выполняются.

    Example:
        >>> supplier = Supplier('example_supplier')
        >>> TestSupplier.test_load_settings(supplier)
    """
    ...
```

**Назначение**:
Метод `test_load_settings` тестирует загрузку настроек поставщика. Он проверяет, что атрибуты экземпляра класса `Supplier` правильно инициализированы на основе настроек из файла.

**Как работает функция**:

1. Проверяется, что `supplier.supplier_prefix` равно `'example_supplier'`.
2. Проверяется, что `supplier.lang` равно `'en'`.
3. Проверяется, что `supplier.scrapping_method` равно `'web'`.
4. Проверяется, что `supplier.supplier_id` равно `'1234'`.
5. Проверяется, что `supplier.price_rule` равно `'example_price_rule'`.
6. Проверяется, что `supplier.login_data` равно `{'if_login': True, 'login_url': 'https://example.com/login', 'user': None, 'password': None}`.
7. Проверяется, что `supplier.start_url` равно `'https://example.com/start'`.
8. Проверяется, что `supplier.scenarios` равно `[{'name': 'scenario1', 'steps': [{'type': 'click', 'locator': 'example_locator'}]}]`.
9. Проверяется, что `supplier.locators` равно `{'example_locator': '//html/body/div'}`.

**Примеры**:

```python
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
from mymodule.supplier import Supplier

class TestSupplier(unittest.TestCase):
    def test_load_settings(supplier):
        assert supplier.supplier_prefix == 'example_supplier'
        assert supplier.lang == 'en'
        assert supplier.scrapping_method == 'web'
        assert supplier.supplier_id == '1234'
        assert supplier.price_rule == 'example_price_rule'
        assert supplier.login_data == {'if_login': True, 'login_url': 'https://example.com/login', 'user': None, 'password': None}
        assert supplier.start_url == 'https://example.com/start'
        assert supplier.scenarios == [{'name': 'scenario1', 'steps': [{'type': 'click', 'locator': 'example_locator'}]}]
        assert supplier.locators == {'example_locator': '//html/body/div'}
```

### `test_load_settings_invalid_path`

```python
def test_load_settings_invalid_path(supplier, caplog):
    """
    Тестирует загрузку настроек при неверном пути к файлу.

    Args:
        supplier (Supplier): Экземпляр класса Supplier.
        caplog (logging.CapLog): Объект для захвата логов.

    Returns:
        None

    Raises:
        AssertionError: Если утверждения не выполняются.

    Example:
        >>> supplier = Supplier('example_supplier')
        >>> TestSupplier.test_load_settings_invalid_path(supplier, caplog)
    """
    ...
```

**Назначение**:
Метод `test_load_settings_invalid_path` тестирует загрузку настроек поставщика при неверном пути к файлу настроек. Он проверяет, что сообщение об ошибке логируется при неудачной попытке чтения файла настроек.

**Как работает функция**:

1. Вызывается метод `_load_settings` экземпляра класса `Supplier`.
2. Проверяется, что сообщение `'Error reading suppliers/example_supplier/example_supplier.json'` содержится в тексте логов (`caplog.text`).

**Примеры**:

```python
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
from mymodule.supplier import Supplier

class TestSupplier(unittest.TestCase):
    def test_load_settings_invalid_path(supplier, caplog):
        supplier._load_settings()
        assert 'Error reading suppliers/example_supplier/example_supplier.json' in caplog.text
```

### `test_load_settings_invalid_locators_path`

```python
def test_load_settings_invalid_locators_path(supplier, caplog):
    """
    Тестирует загрузку настроек при неверном пути к файлу локаторов.

    Args:
        supplier (Supplier): Экземпляр класса Supplier.
        caplog (logging.CapLog): Объект для захвата логов.

    Returns:
        None

    Raises:
        AssertionError: Если утверждения не выполняются.

    Example:
        >>> supplier = Supplier('example_supplier')
        >>> supplier.scrapping_method = 'api'
        >>> TestSupplier.test_load_settings_invalid_locators_path(supplier, caplog)
    """
    ...
```

**Назначение**:
Метод `test_load_settings_invalid_locators_path` тестирует загрузку настроек поставщика при неверном пути к файлу локаторов. Он проверяет, что сообщение об ошибке логируется при неудачной попытке чтения файла локаторов.

**Как работает функция**:

1. Устанавливается `supplier.scrapping_method` в `'api'`.
2. Вызывается метод `_load_settings` экземпляра класса `Supplier`.
3. Проверяется, что сообщение `'Error reading suppliers/example_supplier/locators.json'` содержится в тексте логов (`caplog.text`).

**Примеры**:

```python
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
from mymodule.supplier import Supplier

class TestSupplier(unittest.TestCase):
    def test_load_settings_invalid_locators_path(supplier, caplog):
        supplier.scrapping_method = 'api'
        supplier._load_settings()
        assert 'Error reading suppliers/example_supplier/locators.json' in caplog.text
```

### `test_load_settings_api`

```python
def test_load_settings_api(supplier):
    """
    Тестирует загрузку настроек для API.

    Args:
        supplier (Supplier): Экземпляр класса Supplier.

    Returns:
        None

    Raises:
        AssertionError: Если утверждения не выполняются.

    Example:
        >>> supplier = Supplier('example_supplier')
        >>> TestSupplier.test_load_settings_api(supplier)
    """
    ...
```

**Назначение**:
Метод `test_load_settings_api` тестирует загрузку настроек поставщика для метода парсинга `'api'`. Он проверяет, что атрибуты `locators` и `driver` экземпляра класса `Supplier` установлены в `None`.

**Как работает функция**:

1. Устанавливается `supplier.scrapping_method` в `'api'`.
2. Проверяется, что `supplier.locators` равно `None`.
3. Проверяется, что `supplier.driver` равно `None`.

**Примеры**:

```python
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
from mymodule.supplier import Supplier

class TestSupplier(unittest.TestCase):
    def test_load_settings_api(supplier):
        supplier.scrapping_method = 'api'
        assert supplier.locators is None
        assert supplier.driver is None
```

### `test_load_related_functions`

```python
def test_load_related_functions(supplier):
    """
    Тестирует загрузку связанных функций.

    Args:
        supplier (Supplier): Экземпляр класса Supplier.

    Returns:
        None

    Raises:
        AssertionError: Если утверждения не выполняются.

    Example:
        >>> supplier = Supplier('example_supplier')
        >>> TestSupplier.test_load_related_functions(supplier)
    """
    ...
```

**Назначение**:
Метод `test_load_related_functions` тестирует загрузку связанных функций для поставщика. Он проверяет, что атрибут `related_modules` существует и содержит функцию `example_function`.

**Как работает функция**:

1. Проверяется, что у экземпляра класса `Supplier` есть атрибут `related_modules`.
2. Проверяется, что у атрибута `related_modules` есть атрибут `example_function`.

**Примеры**:

```python
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
from mymodule.supplier import Supplier

class TestSupplier(unittest.TestCase):
    def test_load_related_functions(supplier):
        assert hasattr(supplier, 'related_modules')
        assert hasattr(supplier.related_modules, 'example_function')
```

### `test_init`

```python
def test_init(supplier):
    """
    Тестирует инициализацию.

    Args:
        supplier (Supplier): Экземпляр класса Supplier.

    Returns:
        None

    Raises:
        AssertionError: Если утверждения не выполняются.

    Example:
        >>> supplier = Supplier('example_supplier')
        >>> TestSupplier.test_init(supplier)
    """
    ...
```

**Назначение**:
Метод `test_init` тестирует инициализацию экземпляра класса `Supplier`. Он проверяет, что атрибуты `driver`, `p`, `c`, `current_scenario_filename` и `current_scenario` инициализированы правильно.

**Как работает функция**:

1. Проверяется, что `supplier.driver` не равен `None`.
2. Проверяется, что `supplier.p` является экземпляром списка (`list`).
3. Проверяется, что `supplier.c` является экземпляром списка (`list`).
4. Проверяется, что `supplier.current_scenario_filename` равен `None`.
5. Проверяется, что `supplier.current_scenario` равен `None`.

**Примеры**:

```python
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
from mymodule.supplier import Supplier

class TestSupplier(unittest.TestCase):
    def test_init(supplier):
        assert supplier.driver is not None
        assert isinstance(supplier.p, list)
        assert isinstance(supplier.c, list)
        assert supplier.current_scenario_filename is None
        assert supplier.current_scenario is None
```

### `test_load_settings_success` (self)

```python
def test_load_settings_success(self):
    """
    Тестирует успешную загрузку настроек.

    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.

    Returns:
        None

    Raises:
        AssertionError: Если утверждения не выполняются.

    Example:
        >>> test_supplier = TestSupplier()
        >>> test_supplier.setUp()
        >>> test_supplier.test_load_settings_success()
    """
    ...
```

**Назначение**:
Метод `test_load_settings_success(self)` тестирует успешную загрузку настроек поставщика. Он проверяет, что атрибут `supplier_id` экземпляра класса `Supplier` правильно устанавливается после успешной загрузки настроек.

**Как работает функция**:

1. Используется `patch` для замены встроенной функции `open` заглушкой.
2. Заглушка `open` возвращает `MagicMock` с методом `read`, который возвращает JSON-строку `{'supplier_id': 123}`.
3. Вызывается метод `_load_settings` экземпляра класса `Supplier`.
4. Проверяется, что метод вернул `True`, указывая на успешную загрузку.
5. Проверяется, что атрибут `self.supplier.supplier_id` равен 123.

**Примеры**:

```python
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
from mymodule.supplier import Supplier
import json

class TestSupplier(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier('example_supplier')

    def test_load_settings_success(self):
        with patch('builtins.open', return_value=MagicMock(spec=open, read=lambda: json.dumps({'supplier_id': 123}))) as mock_open:
            result = self.supplier._load_settings()
            self.assertTrue(result)
            self.assertEqual(self.supplier.supplier_id, 123)
```

### `test_load_settings_failure` (self)

```python
def test_load_settings_failure(self):
    """
    Тестирует неудачную загрузку настроек.

    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.

    Returns:
        None

    Raises:
        AssertionError: Если утверждения не выполняются.

    Example:
        >>> test_supplier = TestSupplier()
        >>> test_supplier.setUp()
        >>> test_supplier.test_load_settings_failure()
    """
    ...
```

**Назначение**:
Метод `test_load_settings_failure(self)` тестирует ситуацию, когда загрузка настроек поставщика завершается неудачей. Он проверяет, что метод `_load_settings` возвращает `False`, если во время загрузки настроек происходит исключение.

**Как работает функция**:

1. Используется `patch` для замены встроенной функции `open` заглушкой, которая вызывает исключение.
2. Вызывается метод `_load_settings` экземпляра класса `Supplier`.
3. Проверяется, что метод вернул `False`, указывая на неудачную загрузку.

**Примеры**:

```python
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
from mymodule.supplier import Supplier
import json

class TestSupplier(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier('example_supplier')

    def test_load_settings_failure(self):
        with patch('builtins.open