# Модуль для тестирования класса Supplier

## Обзор

Этот модуль содержит класс `TestSupplier`, который используется для тестирования функциональности класса `Supplier`. Он включает в себя различные тесты для проверки инициализации, загрузки настроек и выполнения сценариев поставщика.

## Подробней

Модуль `test_supplier.py` предназначен для автоматизированного тестирования класса `Supplier`. Он использует библиотеку `unittest` для организации тестов и `unittest.mock` для создания мок-объектов, чтобы изолировать тестируемый класс от внешних зависимостей. В модуле определены различные тестовые методы, охватывающие разные аспекты работы класса `Supplier`, такие как инициализация с различными параметрами, загрузка настроек из файлов и выполнение сценариев.

## Классы

### `TestSupplier`

**Описание**: Класс `TestSupplier` является подклассом `unittest.TestCase` и содержит набор тестов для проверки класса `Supplier`.

**Как работает класс**:

1.  **setUp**: Метод `setUp` вызывается перед каждым тестовым методом. В нем происходит инициализация тестовых данных, таких как префикс поставщика, язык, метод, настройки поставщика, локаторы и экземпляр класса `Supplier`.
2.  **test\_init\_webdriver**: Тестирует инициализацию класса `Supplier` с методом `webdriver`. Использует `patch` для мокирования функций `j_loads` и `Driver`.
3.  **test\_init\_api**: Тестирует инициализацию класса `Supplier` с методом `api`. Использует `patch` для мокирования функции `j_loads`.
4.  **test\_supplier\_load\_settings\_success**: Проверяет успешную загрузку настроек поставщика.
5.  **test\_supplier\_load\_settings\_failure**: Проверяет ситуацию, когда не удается загрузить настройки поставщика.
6.  **test\_load\_settings**: Проверяет загрузку настроек.
7.  **test\_load\_settings\_invalid\_path**: Проверяет обработку неверного пути к файлу настроек.
8.  **test\_load\_settings\_invalid\_locators\_path**: Проверяет обработку неверного пути к файлу локаторов.
9.  **test\_load\_settings\_api**: Проверяет загрузку настроек при использовании API.
10. **test\_load\_related\_functions**: Проверяет загрузку связанных функций.
11. **test\_init**: Проверяет инициализацию драйвера и списков.
12. **test\_load\_settings\_success**: Проверяет успешную загрузку настроек с использованием мокирования `open`.
13. **test\_load\_settings\_failure**: Проверяет неудачную загрузку настроек с использованием мокирования `open` и вызова исключения.
14. **test\_run\_api**: Проверяет выполнение API.
15. **test\_run\_scenario\_files\_success**: Проверяет успешное выполнение сценария из файла.
16. **test\_run\_scenario\_files\_failure**: Проверяет неудачное выполнение сценария из файла.
17. **test\_run\_with\_login**: Проверяет выполнение с логином.
18. **test\_run\_without\_login**: Проверяет выполнение без логина.

**Методы**:

*   `setUp`: Инициализация тестовых данных перед каждым тестом.
*   `test_init_webdriver`: Тестирование инициализации с `webdriver`.
*   `test_init_api`: Тестирование инициализации с `api`.
*   `test_supplier_load_settings_success`: Тестирование успешной загрузки настроек.
*   `test_supplier_load_settings_failure`: Тестирование неудачной загрузки настроек.
*   `test_load_settings`: Тестирование загрузки настроек.
*   `test_load_settings_invalid_path`: Тестирование неверного пути к файлу настроек.
*   `test_load_settings_invalid_locators_path`: Тестирование неверного пути к файлу локаторов.
*   `test_load_settings_api`: Тестирование загрузки настроек API.
*   `test_load_related_functions`: Тестирование загрузки связанных функций.
*   `test_init`: Тестирование инициализации.
*   `test_load_settings_success`: Тестирование успешной загрузки настроек.
*   `test_load_settings_failure`: Тестирование неудачной загрузки настроек.
*   `test_run_api`: Тестирование выполнения API.
*   `test_run_scenario_files_success`: Тестирование успешного выполнения сценария из файла.
*   `test_run_scenario_files_failure`: Тестирование неудачного выполнения сценария из файла.
*   `test_run_with_login`: Тестирование выполнения с логином.
*   `test_run_without_login`: Тестирование выполнения без логина.

## Функции

### `setUp`

```python
def setUp(self):
    """
    Подготавливает тестовое окружение перед каждым тестом.

    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.

    Returns:
        None

    Как работает функция:
    1. Определяет значения атрибутов класса, такие как `supplier_prefix`, `lang`, `method`, `supplier_settings`, `locators`.
    2. Создает экземпляр класса `Supplier` с именем `'example_supplier'`.
    3. Определяет пути к файлам настроек и локаторов.
    """
```

**Параметры**:

*   `self` (TestSupplier): Экземпляр класса `TestSupplier`.

### `test_init_webdriver`

```python
@patch('mymodule.supplier.gs.j_loads')
@patch('mymodule.supplier.Driver')
def test_init_webdriver(self, mock_driver, mock_j_loads):
    """
    Тестирует инициализацию класса `Supplier` с методом `webdriver`.

    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.
        mock_driver (MagicMock): Мок-объект для класса Driver.
        mock_j_loads (MagicMock): Мок-объект для функции j_loads.

    Returns:
        None

    Как работает функция:
    1. Мокирует функции `j_loads` и `Driver` с помощью декоратора `@patch`.
    2. Устанавливает возвращаемое значение для мокированной функции `j_loads` равным `self.supplier_settings`.
    3. Устанавливает возвращаемое значение для мокированного класса `Driver` равным `MagicMock()`.
    4. Создает экземпляр класса `Supplier` с параметрами `self.supplier_prefix`, `self.lang` и `self.method`.
    5. Проверяет, что атрибуты экземпляра класса `Supplier` установлены правильно.
    6. Проверяет, что функция `j_loads` была вызвана один раз с правильным аргументом.
    7. Проверяет, что класс `Driver` был вызван один раз.
    """
```

**Параметры**:

*   `self` (TestSupplier): Экземпляр класса `TestSupplier`.
*   `mock_driver` (MagicMock): Мок-объект для класса `Driver`.
*   `mock_j_loads` (MagicMock): Мок-объект для функции `j_loads`.

### `test_init_api`

```python
@patch('mymodule.supplier.gs.j_loads')
def test_init_api(self, mock_j_loads):
    """
    Тестирует инициализацию класса `Supplier` с методом `api`.

    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.
        mock_j_loads (MagicMock): Мок-объект для функции j_loads.

    Returns:
        None

    Как работает функция:
    1. Устанавливает метод `self.method` равным `'api'`.
    2. Мокирует функцию `j_loads` с помощью декоратора `@patch`.
    3. Устанавливает возвращаемое значение для мокированной функции `j_loads` равным `self.supplier_settings`.
    4. Создает экземпляр класса `Supplier` с параметрами `self.supplier_prefix`, `self.lang` и `self.method`.
    5. Проверяет, что атрибуты экземпляра класса `Supplier` установлены правильно.
    6. Проверяет, что функция `j_loads` была вызвана один раз с правильным аргументом.
    """
```

**Параметры**:

*   `self` (TestSupplier): Экземпляр класса `TestSupplier`.
*   `mock_j_loads` (MagicMock): Мок-объект для функции `j_loads`.

### `test_supplier_load_settings_success`

```python
def test_supplier_load_settings_success():
    """
    Проверяет успешную загрузку настроек поставщика.

    Args:
        None

    Returns:
        None

    Как работает функция:
    1. Создает экземпляр класса `Supplier` с префиксом `'dummy'`.
    2. Проверяет, что атрибут `supplier_id` экземпляра класса `Supplier` равен `'dummy'`.
    3. Проверяет, что атрибут `price_rule` экземпляра класса `Supplier` равен `'dummy'`.
    4. Проверяет, что атрибут `login_data` экземпляра класса `Supplier` равен словарю с ключами `'if_login'`, `'login_url'`, `'user'` и `'password'`, значения которых равны `None`.
    5. Проверяет, что атрибут `start_url` экземпляра класса `Supplier` равен `'dummy'`.
    6. Проверяет, что атрибут `scrapping_method` экземпляра класса `Supplier` равен `'web'`.
    7. Проверяет, что атрибут `scenarios` экземпляра класса `Supplier` равен пустому списку.
    """
```

### `test_supplier_load_settings_failure`

```python
def test_supplier_load_settings_failure():
    """
    Проверяет ситуацию, когда не удается загрузить настройки поставщика.

    Args:
        None

    Returns:
        None

    Как работает функция:
    1. Создает экземпляр класса `Supplier` с префиксом `'nonexistent'`.
    2. Проверяет, что атрибут `supplier_id` экземпляра класса `Supplier` равен `None`.
    3. Проверяет, что атрибут `price_rule` экземпляра класса `Supplier` равен `None`.
    4. Проверяет, что атрибут `login_data` экземпляра класса `Supplier` равен словарю с ключами `'if_login'`, `'login_url'`, `'user'` и `'password'`, значения которых равны `None`.
    5. Проверяет, что атрибут `start_url` экземпляра класса `Supplier` равен `None`.
    6. Проверяет, что атрибут `scrapping_method` экземпляра класса `Supplier` равен пустой строке.
    """
```

### `test_load_settings`

```python
def test_load_settings(supplier):
    """
    Проверяет загрузку настроек.

    Args:
        supplier: Mock-объект поставщика.

    Returns:
        None

    Как работает функция:
    1. Проверяет, что `supplier.supplier_prefix` равен `'example_supplier'`.
    2. Проверяет, что `supplier.lang` равен `'en'`.
    3. Проверяет, что `supplier.scrapping_method` равен `'web'`.
    4. Проверяет, что `supplier.supplier_id` равен `'1234'`.
    5. Проверяет, что `supplier.price_rule` равен `'example_price_rule'`.
    6. Проверяет, что `supplier.login_data` равен `{'if_login': True, 'login_url': 'https://example.com/login', 'user': None, 'password': None}`.
    7. Проверяет, что `supplier.start_url` равен `'https://example.com/start'`.
    8. Проверяет, что `supplier.scenarios` равен `[{'name': 'scenario1', 'steps': [{'type': 'click', 'locator': 'example_locator'}]}]`.
    9. Проверяет, что `supplier.locators` равен `{'example_locator': '//html/body/div'}`.
    """
```

**Параметры**:

*   `supplier`: Mock-объект поставщика.

### `test_load_settings_invalid_path`

```python
def test_load_settings_invalid_path(supplier, caplog):
    """
    Проверяет обработку неверного пути к файлу настроек.

    Args:
        supplier: Mock-объект поставщика.
        caplog: Объект для перехвата логов.

    Returns:
        None

    Как работает функция:
    1. Вызывает метод `_load_settings` у объекта `supplier`.
    2. Проверяет, что в логах есть сообщение об ошибке чтения файла `suppliers/example_supplier/example_supplier.json`.
    """
```

**Параметры**:

*   `supplier`: Mock-объект поставщика.
*   `caplog`: Объект для перехвата логов.

### `test_load_settings_invalid_locators_path`

```python
def test_load_settings_invalid_locators_path(supplier, caplog):
    """
    Проверяет обработку неверного пути к файлу локаторов.

    Args:
        supplier: Mock-объект поставщика.
        caplog: Объект для перехвата логов.

    Returns:
        None

    Как работает функция:
    1. Устанавливает `supplier.scrapping_method` в `'api'`.
    2. Вызывает метод `_load_settings` у объекта `supplier`.
    3. Проверяет, что в логах есть сообщение об ошибке чтения файла `suppliers/example_supplier/locators.json`.
    """
```

**Параметры**:

*   `supplier`: Mock-объект поставщика.
*   `caplog`: Объект для перехвата логов.

### `test_load_settings_api`

```python
def test_load_settings_api(supplier):
    """
    Проверяет загрузку настроек при использовании API.

    Args:
        supplier: Mock-объект поставщика.

    Returns:
        None

    Как работает функция:
    1. Устанавливает `supplier.scrapping_method` в `'api'`.
    2. Проверяет, что `supplier.locators` равен `None`.
    3. Проверяет, что `supplier.driver` равен `None`.
    """
```

**Параметры**:

*   `supplier`: Mock-объект поставщика.

### `test_load_related_functions`

```python
def test_load_related_functions(supplier):
    """
    Проверяет загрузку связанных функций.

    Args:
        supplier: Mock-объект поставщика.

    Returns:
        None

    Как работает функция:
    1. Проверяет наличие атрибута `related_modules` у объекта `supplier`.
    2. Проверяет наличие атрибута `example_function` у объекта `supplier.related_modules`.
    """
```

**Параметры**:

*   `supplier`: Mock-объект поставщика.

### `test_init`

```python
def test_init(supplier):
    """
    Проверяет инициализацию.

    Args:
        supplier: Mock-объект поставщика.

    Returns:
        None

    Как работает функция:
    1. Проверяет, что `supplier.driver` не равен `None`.
    2. Проверяет, что `supplier.p` является экземпляром списка.
    3. Проверяет, что `supplier.c` является экземпляром списка.
    4. Проверяет, что `supplier.current_scenario_filename` равен `None`.
    5. Проверяет, что `supplier.current_scenario` равен `None`.
    """
```

**Параметры**:

*   `supplier`: Mock-объект поставщика.

### `test_load_settings_success`

```python
def test_load_settings_success(self):
    """
    Проверяет успешную загрузку настроек.

    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.

    Returns:
        None

    Как работает функция:
    1. Мокирует функцию `open` с помощью `patch`, чтобы вернуть `MagicMock` с настроенным `read`, возвращающим JSON-строку с `{'supplier_id': 123}`.
    2. Вызывает метод `_load_settings` у экземпляра класса `Supplier`.
    3. Проверяет, что результат вызова `_load_settings` равен `True`.
    4. Проверяет, что атрибут `supplier_id` экземпляра класса `Supplier` равен `123`.
    """
```

**Параметры**:

*   `self` (TestSupplier): Экземпляр класса `TestSupplier`.

### `test_load_settings_failure`

```python
def test_load_settings_failure(self):
    """
    Проверяет неудачную загрузку настроек.

    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.

    Returns:
        None

    Как работает функция:
    1. Мокирует функцию `open` с помощью `patch`, чтобы вызвать исключение при вызове.
    2. Вызывает метод `_load_settings` у экземпляра класса `Supplier`.
    3. Проверяет, что результат вызова `_load_settings` равен `False`.
    """
```

**Параметры**:

*   `self` (TestSupplier): Экземпляр класса `TestSupplier`.

### `test_run_api`

```python
def test_run_api(self):
    """
    Проверяет выполнение API.

    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.

    Returns:
        None

    Как работает функция:
    1. Мокирует функцию `importlib.import_module` с помощью `patch`.
    2. Создает `MagicMock` для мокированного модуля.
    3. Устанавливает возвращаемое значение `mock_module.run_api` в `True`.
    4. Устанавливает возвращаемое значение `mock_import` в `mock_module`.
    5. Вызывает метод `run` у экземпляра класса `Supplier`.
    6. Проверяет, что результат вызова `run` равен `True`.
    """
```

**Параметры**:

*   `self` (TestSupplier): Экземпляр класса `TestSupplier`.

### `test_run_scenario_files_success`

```python
def test_run_scenario_files_success(self):
    """
    Проверяет успешное выполнение сценария из файла.

    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.

    Returns:
        None

    Как работает функция:
    1. Мокирует метод `login` у экземпляра класса `Supplier`, чтобы возвращал `True`.
    2. Вызывает метод `_load_settings` у экземпляра класса `Supplier`.
    3. Определяет путь к файлу сценария.
    4. Вызывает метод `run_scenario_files` с путем к файлу сценария.
    5. Проверяет, что результат вызова `run_scenario_files` равен `True`.
    """
```

**Параметры**:

*   `self` (TestSupplier): Экземпляр класса `TestSupplier`.

### `test_run_scenario_files_failure`

```python
def test_run_scenario_files_failure(self):
    """
    Проверяет неудачное выполнение сценария из файла.

    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.

    Returns:
        None

    Как работает функция:
    1. Мокирует метод `login` у экземпляра класса `Supplier`, чтобы возвращал `True`.
    2. Вызывает метод `_load_settings` у экземпляра класса `Supplier`.
    3. Определяет путь к файлу неверного сценария.
    4. Вызывает метод `run_scenario_files` с путем к файлу неверного сценария.
    5. Проверяет, что результат вызова `run_scenario_files` равен `False`.
    """
```

**Параметры**:

*   `self` (TestSupplier): Экземпляр класса `TestSupplier`.

### `test_run_with_login`

```python
def test_run_with_login(self):
    """
    Проверяет выполнение с логином.

    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.

    Returns:
        None

    Как работает функция:
    1. Мокирует метод `login` у экземпляра класса `Supplier`, чтобы возвращал `True`.
    2. Вызывает метод `_load_settings` у экземпляра класса `Supplier`.
    3. Вызывает метод `run` у экземпляра класса `Supplier`.
    4. Проверяет, что метод `login` был вызван.
    5. Проверяет, что результат вызова `run` равен `True`.
    """
```

**Параметры**:

*   `self` (TestSupplier): Экземпляр класса `TestSupplier`.

### `test_run_without_login`

```python
def test_run_without_login(self):
    """
    Проверяет выполнение без логина.

    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.

    Returns:
        None

    Как работает функция:
    1. Устанавливает `self.supplier.login['if_login']` в `False`.
    2. Мокирует метод `run_scenario_files` у экземпляра класса `Supplier`, чтобы возвращал `True`.
    3. Вызывает метод `_load_settings` у экземпляра класса `Supplier`.
    4. Вызывает метод `run` у экземпляра класса `Supplier`.
    5. Проверяет, что метод `run_scenario_files` не был вызван.
    6. Проверяет, что результат вызова `run` равен `True`.
    """
```

**Параметры**:

*   `self` (TestSupplier): Экземпляр класса `TestSupplier`.