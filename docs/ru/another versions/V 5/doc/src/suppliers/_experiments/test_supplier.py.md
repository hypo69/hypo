# Модуль: `test_supplier`

## Обзор

Модуль `test_supplier.py` содержит набор тестов для класса `Supplier`. Тесты охватывают инициализацию класса, загрузку настроек и выполнение сценариев.

## Подробней

Этот файл содержит модульные тесты для класса `Supplier`, который, по-видимому, является частью системы для работы с поставщиками. Тесты проверяют различные аспекты функциональности класса, такие как правильная инициализация с разными параметрами, загрузка настроек из файлов и выполнение сценариев. В частности, тестируются сценарии успешной и неуспешной загрузки настроек, а также корректная работа методов `run` и `run_scenario_files`.  Файл использует `unittest` для организации тестов и `unittest.mock` для изоляции тестируемого класса от внешних зависимостей, таких как файловая система и другие модули.

## Классы

### `TestSupplier`

**Описание**: Класс `TestSupplier` представляет собой набор тестов для класса `Supplier`.

**Как работает класс**:
Класс содержит несколько методов, каждый из которых является отдельным тестом. В методе `setUp` происходит инициализация общих для всех тестов данных, таких как префикс поставщика, язык, метод сбора данных, настройки поставщика и локаторы. Каждый тестовый метод проверяет определенную часть функциональности класса `Supplier`, используя патчи (`patch`) для имитации поведения внешних зависимостей и утверждения (`assert`) для проверки ожидаемых результатов.

**Методы**:

- `setUp`: Инициализация данных для тестов.
- `test_init_webdriver`: Тест инициализации класса `Supplier` с методом сбора данных `webdriver`.
- `test_init_api`: Тест инициализации класса `Supplier` с методом сбора данных `api`.
- `test_supplier_load_settings_success`: Тест успешной загрузки настроек поставщика.
- `test_supplier_load_settings_failure`: Тест неуспешной загрузки настроек поставщика.
- `test_load_settings`: Тест загрузки настроек.
- `test_load_settings_invalid_path`: Тест загрузки настроек с неверным путем.
- `test_load_settings_invalid_locators_path`: Тест загрузки настроек с неверным путем к локаторам.
- `test_load_settings_api`: Тест загрузки настроек для API.
- `test_load_related_functions`: Тест загрузки связанных функций.
- `test_init`: Тест инициализации.
- `test_load_settings_success`: Тест успешной загрузки настроек.
- `test_load_settings_failure`: Тест неуспешной загрузки настроек.
- `test_run_api`: Тест запуска API.
- `test_run_scenario_files_success`: Тест успешного выполнения сценария из файла.
- `test_run_scenario_files_failure`: Тест неуспешного выполнения сценария из файла.
- `test_run_with_login`: Тест запуска с авторизацией.
- `test_run_without_login`: Тест запуска без авторизации.

#### `setUp`

```python
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

**Описание**: Метод инициализирует переменные, используемые в тестовых методах.

**Как работает метод**:

- `self.supplier_prefix`: Префикс поставщика, используемый для формирования имени файла настроек.
- `self.lang`: Язык, используемый в настройках поставщика.
- `self.method`: Метод сбора данных (web или api).
- `self.supplier_settings`: Словарь с настройками поставщика, такими как идентификатор, правило ценообразования, параметры авторизации и сценарии.
- `self.locators`: Словарь с локаторами элементов на веб-странице.
- `self.supplier`: Экземпляр класса `Supplier`, используемый для тестирования.
- `self.settings_file`: Путь к файлу настроек поставщика.
- `self.locators_file`: Путь к файлу с локаторами элементов.

#### `test_init_webdriver`

```python
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
    mock_j_loads.assert_called_once_with(Path('suppliers', self.supplier_prefix, f'''{self.supplier_prefix}.json'''))
    mock_driver.assert_called_once()
```

**Описание**: Тестирует инициализацию класса `Supplier` с методом сбора данных `webdriver`.

**Как работает метод**:

- Использует `patch` для имитации функций `j_loads` и `Driver`.
- Устанавливает возвращаемые значения для имитированных функций.
- Создает экземпляр класса `Supplier`.
- Проверяет, что атрибуты экземпляра класса `Supplier` установлены правильно.
- Проверяет, что функции `j_loads` и `Driver` были вызваны с правильными аргументами.

**Параметры**:

- `mock_driver`: Имитированный класс `Driver`.
- `mock_j_loads`: Имитированная функция `j_loads`.

#### `test_init_api`

```python
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
    mock_j_loads.assert_called_once_with(Path('suppliers', self.supplier_prefix, f'''{self.supplier_prefix}.json'''))
```

**Описание**: Тестирует инициализацию класса `Supplier` с методом сбора данных `api`.

**Как работает метод**:

- Устанавливает метод сбора данных в `api`.
- Использует `patch` для имитации функции `j_loads`.
- Устанавливает возвращаемое значение для имитированной функции.
- Создает экземпляр класса `Supplier`.
- Проверяет, что атрибуты экземпляра класса `Supplier` установлены правильно.
- Проверяет, что функция `j_loads` была вызвана с правильными аргументами.

**Параметры**:

- `mock_j_loads`: Имитированная функция `j_loads`.

#### `test_supplier_load_settings_success`

```python
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

**Описание**: Тестирует успешную загрузку настроек поставщика.

**Как работает метод**:

- Создает экземпляр класса `Supplier` с префиксом `dummy`.
- Проверяет, что атрибуты экземпляра класса `Supplier` установлены значениями по умолчанию.

#### `test_supplier_load_settings_failure`

```python
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

**Описание**: Тестирует неуспешную загрузку настроек поставщика.

**Как работает метод**:

- Создает экземпляр класса `Supplier` с префиксом `nonexistent`.
- Проверяет, что атрибуты экземпляра класса `Supplier` установлены в `None` или пустую строку.

#### `test_load_settings`

```python
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

**Описание**: Тестирует загрузку настроек.

**Как работает метод**:

- Проверяет, что атрибуты экземпляра класса `Supplier` установлены правильными значениями.

**Параметры**:

- `supplier`: Экземпляр класса `Supplier`.

#### `test_load_settings_invalid_path`

```python
def test_load_settings_invalid_path(supplier, caplog):
    supplier._load_settings()
    assert 'Error reading suppliers/example_supplier/example_supplier.json' in caplog.text
```

**Описание**: Тестирует загрузку настроек с неверным путем.

**Как работает метод**:

- Вызывает метод `_load_settings` экземпляра класса `Supplier`.
- Проверяет, что в логе ошибок есть сообщение об ошибке чтения файла настроек.

**Параметры**:

- `supplier`: Экземпляр класса `Supplier`.
- `caplog`: Объект для захвата логов.

#### `test_load_settings_invalid_locators_path`

```python
def test_load_settings_invalid_locators_path(supplier, caplog):
    supplier.scrapping_method = 'api'
    supplier._load_settings()
    assert 'Error reading suppliers/example_supplier/locators.json' in caplog.text
```

**Описание**: Тестирует загрузку настроек с неверным путем к локаторам.

**Как работает метод**:

- Устанавливает метод сбора данных в `api`.
- Вызывает метод `_load_settings` экземпляра класса `Supplier`.
- Проверяет, что в логе ошибок есть сообщение об ошибке чтения файла локаторов.

**Параметры**:

- `supplier`: Экземпляр класса `Supplier`.
- `caplog`: Объект для захвата логов.

#### `test_load_settings_api`

```python
def test_load_settings_api(supplier):
    supplier.scrapping_method = 'api'
    assert supplier.locators is None
    assert supplier.driver is None
```

**Описание**: Тестирует загрузку настроек для API.

**Как работает метод**:

- Устанавливает метод сбора данных в `api`.
- Проверяет, что атрибуты `locators` и `driver` экземпляра класса `Supplier` установлены в `None`.

**Параметры**:

- `supplier`: Экземпляр класса `Supplier`.

#### `test_load_related_functions`

```python
def test_load_related_functions(supplier):
    assert hasattr(supplier, 'related_modules')
    assert hasattr(supplier.related_modules, 'example_function')
```

**Описание**: Тестирует загрузку связанных функций.

**Как работает метод**:

- Проверяет, что у экземпляра класса `Supplier` есть атрибут `related_modules`.
- Проверяет, что у атрибута `related_modules` есть атрибут `example_function`.

**Параметры**:

- `supplier`: Экземпляр класса `Supplier`.

#### `test_init`

```python
def test_init(supplier):
    assert supplier.driver is not None
    assert isinstance(supplier.p, list)
    assert isinstance(supplier.c, list)
    assert supplier.current_scenario_filename is None
    assert supplier.current_scenario is None
```

**Описание**: Тестирует инициализацию.

**Как работает метод**:

- Проверяет, что у экземпляра класса `Supplier` атрибут `driver` не равен `None`.
- Проверяет, что атрибуты `p` и `c` экземпляра класса `Supplier` являются списками.
- Проверяет, что атрибуты `current_scenario_filename` и `current_scenario` экземпляра класса `Supplier` установлены в `None`.

**Параметры**:

- `supplier`: Экземпляр класса `Supplier`.

#### `test_load_settings_success`

```python
def test_load_settings_success(self):
    with patch('builtins.open', return_value=MagicMock(spec=open, read=lambda: json.dumps({'supplier_id': 123}))) as mock_open:
        result = self.supplier._load_settings()
        self.assertTrue(result)
        self.assertEqual(self.supplier.supplier_id, 123)
```

**Описание**: Тест успешной загрузки настроек.

**Как работает метод**:

- Использует `patch` для имитации функции `open`.
- Устанавливает возвращаемое значение для имитированной функции.
- Вызывает метод `_load_settings` экземпляра класса `Supplier`.
- Проверяет, что метод вернул `True`.
- Проверяет, что атрибут `supplier_id` экземпляра класса `Supplier` установлен правильно.

**Параметры**:

- `mock_open`: Имитированная функция `open`.

#### `test_load_settings_failure`

```python
def test_load_settings_failure(self):
    with patch('builtins.open', side_effect=Exception):
        result = self.supplier._load_settings()
        self.assertFalse(result)
```

**Описание**: Тест неуспешной загрузки настроек.

**Как работает метод**:

- Использует `patch` для имитации функции `open`.
- Устанавливает, что имитированная функция должна вызывать исключение.
- Вызывает метод `_load_settings` экземпляра класса `Supplier`.
- Проверяет, что метод вернул `False`.

#### `test_run_api`

```python
def test_run_api(self):
    with patch('my_module.supplier.importlib.import_module') as mock_import:
        mock_module = MagicMock()
        mock_module.run_api.return_value = True
        mock_import.return_value = mock_module
        result = self.supplier.run()
        self.assertTrue(result)
```

**Описание**: Тест запуска API.

**Как работает метод**:

- Использует `patch` для имитации функции `importlib.import_module`.
- Устанавливает возвращаемое значение для имитированной функции.
- Вызывает метод `run` экземпляра класса `Supplier`.
- Проверяет, что метод вернул `True`.

**Параметры**:

- `mock_import`: Имитированная функция `importlib.import_module`.

#### `test_run_scenario_files_success`

```python
def test_run_scenario_files_success(self):
    with patch.object(self.supplier, 'login', return_value=True):
        self.supplier._load_settings()
        scenario_file = Path(__file__).parent / 'data/example_supplier/scenario.json'
        result = self.supplier.run_scenario_files(str(scenario_file))
        self.assertTrue(result)
```

**Описание**: Тест успешного выполнения сценария из файла.

**Как работает метод**:

- Использует `patch.object` для имитации метода `login` экземпляра класса `Supplier`.
- Устанавливает возвращаемое значение для имитированного метода.
- Вызывает метод `_load_settings` экземпляра класса `Supplier`.
- Вызывает метод `run_scenario_files` экземпляра класса `Supplier`.
- Проверяет, что метод вернул `True`.

#### `test_run_scenario_files_failure`

```python
def test_run_scenario_files_failure(self):
    with patch.object(self.supplier, 'login', return_value=True):
        self.supplier._load_settings()
        scenario_file = Path(__file__).parent / 'data/example_supplier/invalid_scenario.json'
        result = self.supplier.run_scenario_files(str(scenario_file))
        self.assertFalse(result)
```

**Описание**: Тест неуспешного выполнения сценария из файла.

**Как работает метод**:

- Использует `patch.object` для имитации метода `login` экземпляра класса `Supplier`.
- Устанавливает возвращаемое значение для имитированного метода.
- Вызывает метод `_load_settings` экземпляра класса `Supplier`.
- Вызывает метод `run_scenario_files` экземпляра класса `Supplier`.
- Проверяет, что метод вернул `False`.

#### `test_run_with_login`

```python
def test_run_with_login(self):
    with patch.object(self.supplier, 'login', return_value=True) as mock_login:
        self.supplier._load_settings()
        result = self.supplier.run()
        self.assertTrue(mock_login.called)
        self.assertTrue(result)
```

**Описание**: Тест запуска с авторизацией.

**Как работает метод**:

- Использует `patch.object` для имитации метода `login` экземпляра класса `Supplier`.
- Устанавливает возвращаемое значение для имитированного метода.
- Вызывает метод `_load_settings` экземпляра класса `Supplier`.
- Вызывает метод `run` экземпляра класса `Supplier`.
- Проверяет, что метод `login` был вызван.
- Проверяет, что метод `run` вернул `True`.

**Параметры**:

- `mock_login`: Имитированный метод `login`.

#### `test_run_without_login`

```python
def test_run_without_login(self):
    self.supplier.login['if_login'] = False
    with patch.object(self.supplier, 'run_scenario_files', return_value=True) as mock_run_scenario_files:
        self.supplier._load_settings()
        result = self.supplier.run()
        self.assertFalse(mock_run_scenario_files.called_with())
        self.assertTrue(result)
```

**Описание**: Тест запуска без авторизации.

**Как работает метод**:

- Устанавливает значение `if_login` в `False`.
- Использует `patch.object` для имитации метода `run_scenario_files` экземпляра класса `Supplier`.
- Устанавливает возвращаемое значение для имитированного метода.
- Вызывает метод `_load_settings` экземпляра класса `Supplier`.
- Вызывает метод `run` экземпляра класса `Supplier`.
- Проверяет, что метод `run_scenario_files` не был вызван.
- Проверяет, что метод `run` вернул `True`.

**Параметры**:

- `mock_run_scenario_files`: Имитированный метод `run_scenario_files`.