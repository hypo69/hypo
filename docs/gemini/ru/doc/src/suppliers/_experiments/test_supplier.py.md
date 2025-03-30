# Модуль тестирования поставщика `test_supplier.py`

## Обзор

Модуль `test_supplier.py` содержит набор тестов для класса `Supplier`, используемого для взаимодействия с поставщиками данных. Он включает в себя тесты для инициализации класса, загрузки настроек и выполнения сценариев. Модуль использует библиотеку `unittest` для организации тестов и `unittest.mock` для имитации внешних зависимостей и проверки взаимодействия компонентов.

## Подробней

Этот модуль предназначен для обеспечения надежности и правильности работы класса `Supplier`. Тесты охватывают различные аспекты функциональности, такие как:

- Инициализация поставщика с различными параметрами и методами (webdriver, api).
- Загрузка настроек поставщика из JSON-файлов.
- Выполнение сценариев, включая успешные и неудачные случаи.
- Обработка авторизации поставщика.

Тесты используют моки (`MagicMock`, `patch`) для изоляции тестируемого кода и проверки его взаимодействия с внешними компонентами, такими как драйвер веб-браузера и файловая система.

## Классы

### `TestSupplier`

**Описание**: Класс, содержащий набор тестов для класса `Supplier`.

**Методы**:

- `setUp`: Подготовка тестовой среды перед каждым тестом.
- `test_init_webdriver`: Тест инициализации класса `Supplier` с методом `webdriver`.
- `test_init_api`: Тест инициализации класса `Supplier` с методом `api`.
- `test_supplier_load_settings_success`: Тест успешной загрузки настроек поставщика.
- `test_supplier_load_settings_failure`: Тест неудачной загрузки настроек поставщика.
- `test_load_settings`: Тест загрузки настроек.
- `test_load_settings_invalid_path`: Тест загрузки настроек с неверным путем.
- `test_load_settings_invalid_locators_path`: Тест загрузки настроек с неверным путем к локаторам.
- `test_load_settings_api`: Тест загрузки настроек для API.
- `test_load_related_functions`: Тест загрузки связанных функций.
- `test_init`: Тест инициализации.
- `test_load_settings_success`: Тест успешной загрузки настроек с использованием `patch`.
- `test_load_settings_failure`: Тест неудачной загрузки настроек с использованием `patch`.
- `test_run_api`: Тест запуска API.
- `test_run_scenario_files_success`: Тест успешного запуска файлов сценария.
- `test_run_scenario_files_failure`: Тест неудачного запуска файлов сценария.
- `test_run_with_login`: Тест запуска с авторизацией.
- `test_run_without_login`: Тест запуска без авторизации.

**Параметры**:

- `self`: Экземпляр класса `TestSupplier`.

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
        # ... (остальные проверки)
```

## Функции

### `test_init_webdriver`

```python
    @patch('mymodule.supplier.gs.j_loads')
    @patch('mymodule.supplier.Driver')
    def test_init_webdriver(self, mock_driver, mock_j_loads):
        """
        Args:
            mock_driver: Mock драйвера.
            mock_j_loads: Mock функции загрузки JSON.
        """
        ...
```

**Описание**: Тестирует инициализацию класса `Supplier` с использованием метода `webdriver`.

**Параметры**:

- `mock_driver`: Mock объекта `Driver`.
- `mock_j_loads`: Mock функции `j_loads` для загрузки JSON-файлов.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если какие-либо из проверок не проходят.

**Примеры**:

```python
    @patch('mymodule.supplier.gs.j_loads')
    @patch('mymodule.supplier.Driver')
    def test_init_webdriver(self, mock_driver, mock_j_loads):
        mock_j_loads.return_value = self.supplier_settings
        mock_driver.return_value = MagicMock()
        supplier = Supplier(self.supplier_prefix, self.lang, self.method)
        self.assertEqual(supplier.supplier_prefix, self.supplier_prefix)
        self.assertEqual(supplier.lang, self.lang)
        # ... (остальные проверки)
```

### `test_init_api`

```python
    @patch('mymodule.supplier.gs.j_loads')
    def test_init_api(self, mock_j_loads):
        """
        Args:
            mock_j_loads: Mock функции загрузки JSON.
        """
        ...
```

**Описание**: Тестирует инициализацию класса `Supplier` с использованием метода `api`.

**Параметры**:

- `mock_j_loads`: Mock функции `j_loads` для загрузки JSON-файлов.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если какие-либо из проверок не проходят.

**Примеры**:

```python
    @patch('mymodule.supplier.gs.j_loads')
    def test_init_api(self, mock_j_loads):
        self.method = 'api'
        mock_j_loads.return_value = self.supplier_settings
        supplier = Supplier(self.supplier_prefix, self.lang, self.method)
        self.assertEqual(supplier.supplier_prefix, self.supplier_prefix)
        self.assertEqual(supplier.lang, self.lang)
        # ... (остальные проверки)
```

### `test_supplier_load_settings_success`

```python
    def test_supplier_load_settings_success():
        """
        Тест успешной загрузки настроек поставщика.
        """
        ...
```

**Описание**: Тестирует успешную загрузку настроек поставщика.

**Параметры**:

- Отсутствуют.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если какие-либо из проверок не проходят.

**Примеры**:

```python
    def test_supplier_load_settings_success():
        supplier = Supplier(supplier_prefix='dummy')
        assert supplier.supplier_id == 'dummy'
        assert supplier.price_rule == 'dummy'
        # ... (остальные проверки)
```

### `test_supplier_load_settings_failure`

```python
    def test_supplier_load_settings_failure():
        """
        Тест неудачной загрузки настроек поставщика.
        """
        ...
```

**Описание**: Тестирует неудачную загрузку настроек поставщика.

**Параметры**:

- Отсутствуют.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если какие-либо из проверок не проходят.

**Примеры**:

```python
    def test_supplier_load_settings_failure():
        supplier = Supplier(supplier_prefix='nonexistent')
        assert supplier.supplier_id == None
        assert supplier.price_rule == None
        # ... (остальные проверки)
```

### `test_load_settings`

```python
    def test_load_settings(supplier):
        """
        Args:
            supplier: Mock объекта Supplier.
        """
        ...
```

**Описание**: Тестирует загрузку настроек.

**Параметры**:

- `supplier`: Mock объекта `Supplier`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если какие-либо из проверок не проходят.

**Примеры**:

```python
    def test_load_settings(supplier):
        assert supplier.supplier_prefix == 'example_supplier'
        assert supplier.lang == 'en'
        assert supplier.scrapping_method == 'web'
        # ... (остальные проверки)
```

### `test_load_settings_invalid_path`

```python
    def test_load_settings_invalid_path(supplier, caplog):
        """
        Args:
            supplier: Mock объекта Supplier.
            caplog: Объект caplog для перехвата логов.
        """
        ...
```

**Описание**: Тестирует загрузку настроек с неверным путем.

**Параметры**:

- `supplier`: Mock объекта `Supplier`.
- `caplog`: Объект `caplog` для перехвата логов.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если какие-либо из проверок не проходят.

**Примеры**:

```python
    def test_load_settings_invalid_path(supplier, caplog):
        supplier._load_settings()
        assert 'Error reading suppliers/example_supplier/example_supplier.json' in caplog.text
```

### `test_load_settings_invalid_locators_path`

```python
    def test_load_settings_invalid_locators_path(supplier, caplog):
        """
        Args:
            supplier: Mock объекта Supplier.
            caplog: Объект caplog для перехвата логов.
        """
        ...
```

**Описание**: Тестирует загрузку настроек с неверным путем к локаторам.

**Параметры**:

- `supplier`: Mock объекта `Supplier`.
- `caplog`: Объект `caplog` для перехвата логов.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если какие-либо из проверок не проходят.

**Примеры**:

```python
    def test_load_settings_invalid_locators_path(supplier, caplog):
        supplier.scrapping_method = 'api'
        supplier._load_settings()
        assert 'Error reading suppliers/example_supplier/locators.json' in caplog.text
```

### `test_load_settings_api`

```python
    def test_load_settings_api(supplier):
        """
        Args:
            supplier: Mock объекта Supplier.
        """
        ...
```

**Описание**: Тестирует загрузку настроек для API.

**Параметры**:

- `supplier`: Mock объекта `Supplier`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если какие-либо из проверок не проходят.

**Примеры**:

```python
    def test_load_settings_api(supplier):
        supplier.scrapping_method = 'api'
        assert supplier.locators is None
        assert supplier.driver is None
```

### `test_load_related_functions`

```python
    def test_load_related_functions(supplier):
        """
        Args:
            supplier: Mock объекта Supplier.
        """
        ...
```

**Описание**: Тестирует загрузку связанных функций.

**Параметры**:

- `supplier`: Mock объекта `Supplier`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если какие-либо из проверок не проходят.

**Примеры**:

```python
    def test_load_related_functions(supplier):
        assert hasattr(supplier, 'related_modules')
        assert hasattr(supplier.related_modules, 'example_function')
```

### `test_init`

```python
    def test_init(supplier):
        """
        Args:
            supplier: Mock объекта Supplier.
        """
        ...
```

**Описание**: Тестирует инициализацию.

**Параметры**:

- `supplier`: Mock объекта `Supplier`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если какие-либо из проверок не проходят.

**Примеры**:

```python
    def test_init(supplier):
        assert supplier.driver is not None
        assert isinstance(supplier.p, list)
        assert isinstance(supplier.c, list)
        assert supplier.current_scenario_filename is None
        assert supplier.current_scenario is None
```

### `test_load_settings_success`

```python
    def test_load_settings_success(self):
        """
        Args:
            self: Экземпляр класса TestSupplier.
        """
        ...
```

**Описание**: Тестирует успешную загрузку настроек с использованием `patch`.

**Параметры**:

- `self`: Экземпляр класса `TestSupplier`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если какие-либо из проверок не проходят.

**Примеры**:

```python
    def test_load_settings_success(self):
        with patch('builtins.open', return_value=MagicMock(spec=open, read=lambda: json.dumps({'supplier_id': 123}))) as mock_open:
            result = self.supplier._load_settings()
            self.assertTrue(result)
            self.assertEqual(self.supplier.supplier_id, 123)
```

### `test_load_settings_failure`

```python
    def test_load_settings_failure(self):
        """
        Args:
            self: Экземпляр класса TestSupplier.
        """
        ...
```

**Описание**: Тестирует неудачную загрузку настроек с использованием `patch`.

**Параметры**:

- `self`: Экземпляр класса `TestSupplier`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если какие-либо из проверок не проходят.

**Примеры**:

```python
    def test_load_settings_failure(self):
        with patch('builtins.open', side_effect=Exception):
            result = self.supplier._load_settings()
            self.assertFalse(result)
```

### `test_run_api`

```python
    def test_run_api(self):
        """
        Args:
            self: Экземпляр класса TestSupplier.
        """
        ...
```

**Описание**: Тестирует запуск API.

**Параметры**:

- `self`: Экземпляр класса `TestSupplier`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если какие-либо из проверок не проходят.

**Примеры**:

```python
    def test_run_api(self):
        with patch('my_module.supplier.importlib.import_module') as mock_import:
            mock_module = MagicMock()
            mock_module.run_api.return_value = True
            mock_import.return_value = mock_module
            result = self.supplier.run()
            self.assertTrue(result)
```

### `test_run_scenario_files_success`

```python
    def test_run_scenario_files_success(self):
        """
        Args:
            self: Экземпляр класса TestSupplier.
        """
        ...
```

**Описание**: Тестирует успешный запуск файлов сценария.

**Параметры**:

- `self`: Экземпляр класса `TestSupplier`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если какие-либо из проверок не проходят.

**Примеры**:

```python
    def test_run_scenario_files_success(self):
        with patch.object(self.supplier, 'login', return_value=True):
            self.supplier._load_settings()
            scenario_file = Path(__file__).parent / 'data/example_supplier/scenario.json'
            result = self.supplier.run_scenario_files(str(scenario_file))
            self.assertTrue(result)
```

### `test_run_scenario_files_failure`

```python
    def test_run_scenario_files_failure(self):
        """
        Args:
            self: Экземпляр класса TestSupplier.
        """
        ...
```

**Описание**: Тестирует неудачный запуск файлов сценария.

**Параметры**:

- `self`: Экземпляр класса `TestSupplier`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если какие-либо из проверок не проходят.

**Примеры**:

```python
    def test_run_scenario_files_failure(self):
        with patch.object(self.supplier, 'login', return_value=True):
            self.supplier._load_settings()
            scenario_file = Path(__file__).parent / 'data/example_supplier/invalid_scenario.json'
            result = self.supplier.run_scenario_files(str(scenario_file))
            self.assertFalse(result)
```

### `test_run_with_login`

```python
    def test_run_with_login(self):
        """
        Args:
            self: Экземпляр класса TestSupplier.
        """
        ...
```

**Описание**: Тестирует запуск с авторизацией.

**Параметры**:

- `self`: Экземпляр класса `TestSupplier`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если какие-либо из проверок не проходят.

**Примеры**:

```python
    def test_run_with_login(self):
        with patch.object(self.supplier, 'login', return_value=True) as mock_login:
            self.supplier._load_settings()
            result = self.supplier.run()
            self.assertTrue(mock_login.called)
            self.assertTrue(result)
```

### `test_run_without_login`

```python
    def test_run_without_login(self):
        """
        Args:
            self: Экземпляр класса TestSupplier.
        """
        ...
```

**Описание**: Тестирует запуск без авторизации.

**Параметры**:

- `self`: Экземпляр класса `TestSupplier`.

**Возвращает**:

- `None`

**Вызывает исключения**:

- `AssertionError`: Если какие-либо из проверок не проходят.

**Примеры**:

```python
    def test_run_without_login(self):
        self.supplier.login['if_login'] = False
        with patch.object(self.supplier, 'run_scenario_files', return_value=True) as mock_run_scenario_files:
            self.supplier._load_settings()
            result = self.supplier.run()
            self.assertFalse(mock_run_scenario_files.called_with())
            self.assertTrue(result)