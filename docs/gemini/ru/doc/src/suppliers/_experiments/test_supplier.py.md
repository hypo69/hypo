# Модуль тестирования поставщика

## Обзор

Этот модуль содержит набор тестов для класса `Supplier`, который отвечает за взаимодействие с поставщиками данных. Тесты проверяют корректность инициализации, загрузки настроек и выполнения сценариев работы с поставщиками.

## Подробней

Модуль `test_supplier.py` содержит класс `TestSupplier`, который наследуется от `unittest.TestCase`. Этот класс содержит различные методы для тестирования функциональности класса `Supplier`. В частности, проверяется корректность загрузки настроек из файлов, инициализации объекта `Supplier` с разными параметрами (например, с использованием `webdriver` или `api`), а также выполнение сценариев. Модуль использует `patch` из библиотеки `unittest.mock` для подмены внешних зависимостей и упрощения тестирования.

## Классы

### `TestSupplier`

**Описание**: Класс `TestSupplier` предназначен для тестирования класса `Supplier`.

**Наследует**:
- `unittest.TestCase`: Базовый класс для создания тестовых случаев.

**Атрибуты**:
- `supplier_prefix` (str): Префикс имени поставщика для тестов.
- `lang` (str): Язык поставщика для тестов.
- `method` (str): Метод сбора данных поставщиком (например, `web` или `api`).
- `supplier_settings` (dict): Настройки поставщика для тестов.
- `locators` (dict): Локаторы элементов для тестов.
- `supplier` (Supplier): Объект поставщика для тестов.
- `settings_file` (Path): Путь к файлу настроек поставщика.
- `locators_file` (Path): Путь к файлу локаторов.

**Методы**:
- `setUp()`: Подготовка тестовой среды перед каждым тестом.
- `test_init_webdriver()`: Тестирование инициализации поставщика с использованием `webdriver`.
- `test_init_api()`: Тестирование инициализации поставщика с использованием `api`.
- `test_supplier_load_settings_success()`: Тестирование успешной загрузки настроек поставщика.
- `test_supplier_load_settings_failure()`: Тестирование неудачной загрузки настроек поставщика.
- `test_load_settings()`: Тестирование загрузки настроек.
- `test_load_settings_invalid_path()`: Тестирование загрузки настроек при неверном пути к файлу.
- `test_load_settings_invalid_locators_path()`: Тестирование загрузки настроек при неверном пути к файлу локаторов.
- `test_load_settings_api()`: Тестирование загрузки настроек для `api`.
- `test_load_related_functions()`: Тестирование загрузки связанных функций.
- `test_init()`: Тестирование инициализации.
- `test_load_settings_success()`: Тестирование успешной загрузки настроек.
- `test_load_settings_failure()`: Тестирование неудачной загрузки настроек.
- `test_run_api()`: Тестирование запуска `api`.
- `test_run_scenario_files_success()`: Тестирование успешного выполнения файлов сценариев.
- `test_run_scenario_files_failure()`: Тестирование неудачного выполнения файлов сценариев.
- `test_run_with_login()`: Тестирование запуска с авторизацией.
- `test_run_without_login()`: Тестирование запуска без авторизации.

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
    """
    ...
```

**Назначение**:
Метод `setUp` устанавливает начальные значения атрибутов класса `TestSupplier`, такие как префикс поставщика, язык, метод сбора данных, настройки поставщика, локаторы, объект поставщика, а также пути к файлам настроек и локаторов. Это позволяет использовать эти значения в каждом тестовом методе.

**Как работает функция**:

1.  **Инициализация атрибутов**: Метод устанавливает значения атрибутов класса `TestSupplier`, такие как `supplier_prefix`, `lang`, `method`, `supplier_settings`, `locators`, `supplier`, `settings_file` и `locators_file`. Эти атрибуты используются в других тестовых методах для проверки различных аспектов работы класса `Supplier`.
2.  **Определение путей к файлам**: Метод определяет пути к файлам настроек и локаторов, используя `Path` из библиотеки `pathlib`. Это позволяет загружать настройки и локаторы из файлов для тестирования.
3.  **Создание экземпляра класса `Supplier`**: Создается экземпляр класса `Supplier` с префиксом `'example_supplier'`. Этот экземпляр используется для тестирования методов класса `Supplier`.

```
Инициализация атрибутов --> Определение путей к файлам --> Создание экземпляра класса `Supplier`
```

**Примеры**:

```python
test_class = TestSupplier()
test_class.setUp()
print(test_class.supplier_prefix)  # Вывод: test_supplier
print(test_class.lang)  # Вывод: en
```

### `test_init_webdriver`

```python
@patch('mymodule.supplier.gs.j_loads')
@patch('mymodule.supplier.Driver')
def test_init_webdriver(self, mock_driver, mock_j_loads):
    """
    Тестирует инициализацию поставщика с использованием `webdriver`.
    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.
        mock_driver (MagicMock): Заглушка для класса Driver.
        mock_j_loads (MagicMock): Заглушка для функции j_loads.
    Returns:
        None
    """
    ...
```

**Назначение**:
Метод `test_init_webdriver` тестирует инициализацию класса `Supplier` с методом сбора данных `webdriver`. Он проверяет, что при инициализации с методом `webdriver` правильно загружаются настройки поставщика, создается экземпляр драйвера, и устанавливаются соответствующие атрибуты объекта `Supplier`.

**Как работает функция**:

1.  **Подмена зависимостей**: Используются декораторы `@patch` для подмены функций `j_loads` и класса `Driver` из модуля `mymodule.supplier`. Это позволяет изолировать тестируемый код и избежать реального взаимодействия с внешними ресурсами.
2.  **Установка возвращаемых значений заглушек**: Устанавливаются возвращаемые значения для заглушек `mock_j_loads` и `mock_driver`. `mock_j_loads` возвращает `self.supplier_settings`, а `mock_driver` возвращает `MagicMock()`.
3.  **Инициализация объекта `Supplier`**: Создается экземпляр класса `Supplier` с параметрами `self.supplier_prefix`, `self.lang` и `self.method`.
4.  **Проверка атрибутов объекта `Supplier`**: Проверяются атрибуты созданного объекта `Supplier`, такие как `supplier_prefix`, `lang`, `scrapping_method`, `supplier_id`, `price_rule`, `login_data`, `start_url` и `scenarios`, чтобы убедиться, что они соответствуют ожидаемым значениям.
5.  **Проверка вызовов заглушек**: Проверяется, что заглушки `mock_j_loads` и `mock_driver` были вызваны с правильными аргументами.

```
Подмена зависимостей --> Установка возвращаемых значений заглушек --> Инициализация объекта `Supplier` --> Проверка атрибутов объекта `Supplier` --> Проверка вызовов заглушек
```

**Примеры**:

```python
test_class = TestSupplier()
test_class.setUp()
with patch('mymodule.supplier.gs.j_loads') as mock_j_loads, \
        patch('mymodule.supplier.Driver') as mock_driver:
    mock_j_loads.return_value = test_class.supplier_settings
    mock_driver.return_value = MagicMock()
    test_class.test_init_webdriver(mock_driver, mock_j_loads)
```

### `test_init_api`

```python
@patch('mymodule.supplier.gs.j_loads')
def test_init_api(self, mock_j_loads):
    """
    Тестирует инициализацию поставщика с использованием `api`.
    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.
        mock_j_loads (MagicMock): Заглушка для функции j_loads.
    Returns:
        None
    """
    ...
```

**Назначение**:
Метод `test_init_api` тестирует инициализацию класса `Supplier` с методом сбора данных `api`. Он проверяет, что при инициализации с методом `api` правильно загружаются настройки поставщика и устанавливаются соответствующие атрибуты объекта `Supplier`.

**Как работает функция**:

1.  **Подмена зависимости**: Используется декоратор `@patch` для подмены функции `j_loads` из модуля `mymodule.supplier`.
2.  **Установка возвращаемого значения заглушки**: Устанавливается возвращаемое значение для заглушки `mock_j_loads`. `mock_j_loads` возвращает `self.supplier_settings`.
3.  **Изменение метода сбора данных**: Устанавливается значение атрибута `self.method` равным `'api'`.
4.  **Инициализация объекта `Supplier`**: Создается экземпляр класса `Supplier` с параметрами `self.supplier_prefix`, `self.lang` и `self.method`.
5.  **Проверка атрибутов объекта `Supplier`**: Проверяются атрибуты созданного объекта `Supplier`, такие как `supplier_prefix`, `lang`, `scrapping_method`, `supplier_id`, `price_rule`, `login_data`, `start_url` и `scenarios`, чтобы убедиться, что они соответствуют ожидаемым значениям.
6.  **Проверка вызова заглушки**: Проверяется, что заглушка `mock_j_loads` была вызвана с правильными аргументами.

```
Подмена зависимости --> Установка возвращаемого значения заглушки --> Изменение метода сбора данных --> Инициализация объекта `Supplier` --> Проверка атрибутов объекта `Supplier` --> Проверка вызова заглушки
```

**Примеры**:

```python
test_class = TestSupplier()
test_class.setUp()
with patch('mymodule.supplier.gs.j_loads') as mock_j_loads:
    mock_j_loads.return_value = test_class.supplier_settings
    test_class.method = 'api'
    test_class.test_init_api(mock_j_loads)
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
    """
    ...
```

**Назначение**:
Метод `test_supplier_load_settings_success` тестирует успешную загрузку настроек поставщика при инициализации класса `Supplier` с префиксом `'dummy'`. Он проверяет, что атрибуты объекта `Supplier` устанавливаются в значения по умолчанию, когда настройки успешно загружены.

**Как работает функция**:

1.  **Инициализация объекта `Supplier`**: Создается экземпляр класса `Supplier` с параметром `supplier_prefix='dummy'`.
2.  **Проверка атрибутов объекта `Supplier`**: Проверяются атрибуты созданного объекта `Supplier`, такие как `supplier_id`, `price_rule`, `login_data`, `start_url`, `scrapping_method` и `scenarios`, чтобы убедиться, что они соответствуют значениям по умолчанию.

```
Инициализация объекта `Supplier` --> Проверка атрибутов объекта `Supplier`
```

**Примеры**:

```python
test_supplier_load_settings_success()
```

### `test_supplier_load_settings_failure`

```python
def test_supplier_load_settings_failure():
    """
    Тестирует неудачную загрузку настроек поставщика.
    Args:
        None
    Returns:
        None
    """
    ...
```

**Назначение**:
Метод `test_supplier_load_settings_failure` тестирует неудачную загрузку настроек поставщика при инициализации класса `Supplier` с префиксом `'nonexistent'`. Он проверяет, что атрибуты объекта `Supplier` устанавливаются в `None` или пустые строки, когда настройки не удалось загрузить.

**Как работает функция**:

1.  **Инициализация объекта `Supplier`**: Создается экземпляр класса `Supplier` с параметром `supplier_prefix='nonexistent'`.
2.  **Проверка атрибутов объекта `Supplier`**: Проверяются атрибуты созданного объекта `Supplier`, такие как `supplier_id`, `price_rule`, `login_data`, `start_url` и `scrapping_method`, чтобы убедиться, что они соответствуют значениям по умолчанию (None или пустые строки).

```
Инициализация объекта `Supplier` --> Проверка атрибутов объекта `Supplier`
```

**Примеры**:

```python
test_supplier_load_settings_failure()
```

### `test_load_settings`

```python
def test_load_settings(supplier, caplog):
    """
    Тестирует загрузку настроек.
    Args:
        supplier:
        caplog:
    Returns:
        None
    """
    ...
```

**Назначение**:
Метод `test_load_settings` тестирует загрузку настроек. Проверяет значения атрибутов объекта `supplier` после загрузки настроек.

**Как работает функция**:

1.  **Проверка атрибутов объекта `supplier`**: Проверяются атрибуты созданного объекта `supplier`, такие как `supplier_prefix`, `lang`, `scrapping_method`, `supplier_id`, `price_rule`, `login_data`, `start_url`, `scenarios` и `locators`, чтобы убедиться, что они соответствуют значениям.

```
Проверка атрибутов объекта `supplier`
```

### `test_load_settings_invalid_path`

```python
def test_load_settings_invalid_path(supplier, caplog):
    """
    Тестирует загрузку настроек при неверном пути к файлу.
    Args:
        supplier:
        caplog:
    Returns:
        None
    """
    ...
```

**Назначение**:
Метод `test_load_settings_invalid_path` тестирует загрузку настроек при указании неверного пути к файлу настроек. Проверяется, что в лог записывается сообщение об ошибке.

**Как работает функция**:

1.  **Вызов метода `_load_settings`**: Вызывается метод `_load_settings` объекта `supplier`.
2.  **Проверка наличия сообщения об ошибке в логе**: Проверяется, что в логе `caplog.text` присутствует сообщение об ошибке, указывающее на то, что не удалось прочитать файл настроек.

```
Вызов метода `_load_settings` --> Проверка наличия сообщения об ошибке в логе
```

### `test_load_settings_invalid_locators_path`

```python
def test_load_settings_invalid_locators_path(supplier, caplog):
    """
    Тестирует загрузку настроек при неверном пути к файлу локаторов.
    Args:
        supplier:
        caplog:
    Returns:
        None
    """
    ...
```

**Назначение**:
Метод `test_load_settings_invalid_locators_path` тестирует загрузку настроек при указании неверного пути к файлу локаторов. Проверяется, что в лог записывается сообщение об ошибке.

**Как работает функция**:

1.  **Установка метода сбора данных**: Устанавливается значение атрибута `supplier.scrapping_method` равным `'api'`.
2.  **Вызов метода `_load_settings`**: Вызывается метод `_load_settings` объекта `supplier`.
3.  **Проверка наличия сообщения об ошибке в логе**: Проверяется, что в логе `caplog.text` присутствует сообщение об ошибке, указывающее на то, что не удалось прочитать файл локаторов.

```
Установка метода сбора данных --> Вызов метода `_load_settings` --> Проверка наличия сообщения об ошибке в логе
```

### `test_load_settings_api`

```python
def test_load_settings_api(supplier):
    """
    Тестирует загрузку настроек для `api`.
    Args:
        supplier:
    Returns:
        None
    """
    ...
```

**Назначение**:
Метод `test_load_settings_api` тестирует загрузку настроек для метода сбора данных `api`. Проверяется, что атрибуты `locators` и `driver` объекта `supplier` равны `None`.

**Как работает функция**:

1.  **Установка метода сбора данных**: Устанавливается значение атрибута `supplier.scrapping_method` равным `'api'`.
2.  **Проверка атрибутов `locators` и `driver`**: Проверяется, что атрибуты `supplier.locators` и `supplier.driver` равны `None`.

```
Установка метода сбора данных --> Проверка атрибутов `locators` и `driver`
```

### `test_load_related_functions`

```python
def test_load_related_functions(supplier):
    """
    Тестирует загрузку связанных функций.
    Args:
        supplier:
    Returns:
        None
    """
    ...
```

**Назначение**:
Метод `test_load_related_functions` тестирует загрузку связанных функций. Проверяется, что у объекта `supplier` есть атрибут `related_modules` и что у этого атрибута есть атрибут `example_function`.

**Как работает функция**:

1.  **Проверка наличия атрибута `related_modules`**: Проверяется, что у объекта `supplier` есть атрибут `related_modules` с помощью функции `hasattr`.
2.  **Проверка наличия атрибута `example_function`**: Проверяется, что у атрибута `supplier.related_modules` есть атрибут `example_function` с помощью функции `hasattr`.

```
Проверка наличия атрибута `related_modules` --> Проверка наличия атрибута `example_function`
```

### `test_init`

```python
def test_init(supplier):
    """
    Тестирует инициализацию.
    Args:
        supplier:
    Returns:
        None
    """
    ...
```

**Назначение**:
Метод `test_init` тестирует инициализацию объекта `supplier`. Проверяет, что атрибут `driver` не равен `None`, а также что атрибуты `p` и `c` являются списками, и что атрибуты `current_scenario_filename` и `current_scenario` равны `None`.

**Как работает функция**:

1.  **Проверка атрибута `driver`**: Проверяется, что атрибут `supplier.driver` не равен `None`.
2.  **Проверка атрибутов `p` и `c`**: Проверяется, что атрибуты `supplier.p` и `supplier.c` являются экземплярами класса `list`.
3.  **Проверка атрибутов `current_scenario_filename` и `current_scenario`**: Проверяется, что атрибуты `supplier.current_scenario_filename` и `supplier.current_scenario` равны `None`.

```
Проверка атрибута `driver` --> Проверка атрибутов `p` и `c` --> Проверка атрибутов `current_scenario_filename` и `current_scenario`
```

### `test_load_settings_success`

```python
def test_load_settings_success(self):
    """
    Тестирует успешную загрузку настроек.
    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.
    Returns:
        None
    """
    ...
```

**Назначение**:
Метод `test_load_settings_success` тестирует успешную загрузку настроек поставщика из файла JSON. Он проверяет, что настройки успешно загружаются и применяются к атрибутам объекта `Supplier`.

**Как работает функция**:

1.  **Подмена функции `open`**: Используется `patch` для подмены встроенной функции `open`. Вместо реального открытия файла возвращается `MagicMock`, который имитирует файл с содержимым JSON.
2.  **Определение возвращаемого значения `MagicMock`**: Определяется поведение `MagicMock` так, чтобы метод `read` возвращал строку с JSON-представлением настроек поставщика (`{'supplier_id': 123}`).
3.  **Вызов метода `_load_settings`**: Вызывается метод `_load_settings` объекта `self.supplier`.
4.  **Проверка возвращаемого значения**: Проверяется, что метод `_load_settings` возвращает `True`, что означает успешную загрузку настроек.
5.  **Проверка атрибутов объекта `Supplier`**: Проверяется, что атрибут `self.supplier.supplier_id` был обновлен значением из JSON (123).
6.  **Проверка вызова `mock_open`**: Проверяется, что функция `mock_open` была вызвана.

```
Подмена функции `open` --> Определение возвращаемого значения `MagicMock` --> Вызов метода `_load_settings` --> Проверка возвращаемого значения --> Проверка атрибутов объекта `Supplier` --> Проверка вызова `mock_open`
```

**Примеры**:

```python
test_class = TestSupplier()
test_class.setUp()
with patch('builtins.open', return_value=MagicMock(spec=open, read=lambda: json.dumps({'supplier_id': 123}))) as mock_open:
    test_class.test_load_settings_success()
```

### `test_load_settings_failure`

```python
def test_load_settings_failure(self):
    """
    Тестирует неудачную загрузку настроек.
    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.
    Returns:
        None
    """
    ...
```

**Назначение**:
Метод `test_load_settings_failure` тестирует случай, когда не удается загрузить настройки поставщика из файла (например, если файл не существует или содержит некорректный JSON). Он проверяет, что метод `_load_settings` возвращает `False` в случае ошибки.

**Как работает функция**:

1.  **Подмена функции `open`**: Используется `patch` для подмены встроенной функции `open`. Вместо реального открытия файла, при вызове `open` генерируется исключение.
2.  **Вызов метода `_load_settings`**: Вызывается метод `_load_settings` объекта `self.supplier`.
3.  **Проверка возвращаемого значения**: Проверяется, что метод `_load_settings` возвращает `False`, что означает неудачную загрузку настроек.

```
Подмена функции `open` --> Вызов метода `_load_settings` --> Проверка возвращаемого значения
```

**Примеры**:

```python
test_class = TestSupplier()
test_class.setUp()
with patch('builtins.open', side_effect=Exception):
    test_class.test_load_settings_failure()
```

### `test_run_api`

```python
def test_run_api(self):
    """
    Тестирует запуск `api`.
    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.
    Returns:
        None
    """
    ...
```

**Назначение**:
Метод `test_run_api` тестирует запуск поставщика с методом сбора данных `api`. Он проверяет, что при вызове метода `run` импортируется правильный модуль и вызывается функция `run_api` этого модуля.

**Как работает функция**:

1.  **Подмена функции `importlib.import_module`**: Используется `patch` для подмены функции `importlib.import_module`. Вместо реального импорта модуля возвращается `MagicMock`, который имитирует модуль с функцией `run_api`.
2.  **Определение поведения `MagicMock`**: Определяется поведение `MagicMock` так, чтобы атрибут `run_api` возвращал `True`.
3.  **Вызов метода `run`**: Вызывается метод `run` объекта `self.supplier`.
4.  **Проверка возвращаемого значения**: Проверяется, что метод `run` возвращает `True`, что означает успешный запуск `api`.

```
Подмена функции `importlib.import_module` --> Определение поведения `MagicMock` --> Вызов метода `run` --> Проверка возвращаемого значения
```

**Примеры**:

```python
test_class = TestSupplier()
test_class.setUp()
with patch('my_module.supplier.importlib.import_module') as mock_import:
    mock_module = MagicMock()
    mock_module.run_api.return_value = True
    mock_import.return_value = mock_module
    test_class.test_run_api()
```

### `test_run_scenario_files_success`

```python
def test_run_scenario_files_success(self):
    """
    Тестирует успешное выполнение файлов сценариев.
    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.
    Returns:
        None
    """
    ...
```

**Назначение**:
Метод `test_run_scenario_files_success` тестирует успешное выполнение файлов сценариев. Он проверяет, что при вызове метода `run_scenario_files` с правильным путем к файлу сценария возвращается `True`.

**Как работает функция**:

1.  **Подмена метода `login`**: Используется `patch.object` для подмены метода `login` объекта `self.supplier`. Вместо реальной авторизации метод `login` всегда возвращает `True`.
2.  **Вызов метода `_load_settings`**: Вызывается метод `_load_settings` объекта `self.supplier` для загрузки настроек.
3.  **Определение пути к файлу сценария**: Определяется путь к файлу сценария, который будет использоваться для тестирования.
4.  **Вызов метода `run_scenario_files`**: Вызывается метод `run_scenario_files` объекта `self.supplier` с путем к файлу сценария.
5.  **Проверка возвращаемого значения**: Проверяется, что метод `run_scenario_files` возвращает `True`, что означает успешное выполнение сценария.

```
Подмена метода `login` --> Вызов метода `_load_settings` --> Определение пути к файлу сценария --> Вызов метода `run_scenario_files` --> Проверка возвращаемого значения
```

**Примеры**:

```python
test_class = TestSupplier()
test_class.setUp()
with patch.object(test_class.supplier, 'login', return_value=True):
    test_class.supplier._load_settings()
    scenario_file = Path(__file__).parent / 'data/example_supplier/scenario.json'
    test_class.test_run_scenario_files_success()
```

### `test_run_scenario_files_failure`

```python
def test_run_scenario_files_failure(self):
    """
    Тестирует неудачное выполнение файлов сценариев.
    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.
    Returns:
        None
    """
    ...
```

**Назначение**:
Метод `test_run_scenario_files_failure` тестирует неудачное выполнение файлов сценариев. Он проверяет, что при вызове метода `run_scenario_files` с неправильным путем к файлу сценария возвращается `False`.

**Как работает функция**:

1.  **Подмена метода `login`**: Используется `patch.object` для подмены метода `login` объекта `self.supplier`. Вместо реальной авторизации метод `login` всегда возвращает `True`.
2.  **Вызов метода `_load_settings`**: Вызывается метод `_load_settings` объекта `self.supplier` для загрузки настроек.
3.  **Определение пути к файлу сценария**: Определяется путь к файлу сценария, который будет использоваться для тестирования (невалидный сценарий).
4.  **Вызов метода `run_scenario_files`**: Вызывается метод `run_scenario_files` объекта `self.supplier` с путем к файлу сценария.
5.  **Проверка возвращаемого значения**: Проверяется, что метод `run_scenario_files` возвращает `False`, что означает неудачное выполнение сценария.

```
Подмена метода `login` --> Вызов метода `_load_settings` --> Определение пути к файлу сценария --> Вызов метода `run_scenario_files` --> Проверка возвращаемого значения
```

**Примеры**:

```python
test_class = TestSupplier()
test_class.setUp()
with patch.object(test_class.supplier, 'login', return_value=True):
    test_class.supplier._load_settings()
    scenario_file = Path(__file__).parent / 'data/example_supplier/invalid_scenario.json'
    test_class.test_run_scenario_files_failure()
```

### `test_run_with_login`

```python
def test_run_with_login(self):
    """
    Тестирует запуск с авторизацией.
    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.
    Returns:
        None
    """
    ...
```

**Назначение**:
Метод `test_run_with_login` тестирует запуск поставщика с авторизацией. Он проверяет, что при вызове метода `run` вызывается метод `login`, и возвращается `True`.

**Как работает функция**:

1.  **Подмена метода `login`**: Используется `patch.object` для подмены метода `login` объекта `self.supplier`. Вместо реальной авторизации метод `login` всегда возвращает `True`.
2.  **Вызов метода `_load_settings`**: Вызывается метод `_load_settings` объекта `self.supplier` для загрузки настроек.
3.  **Вызов метода `run`**: Вызывается метод `run` объекта `self.supplier`.
4.  **Проверка вызова метода `login`**: Проверяется, что метод `login` был вызван.
5.  **Проверка возвращаемого значения**: Проверяется, что метод `run` возвращает `True`, что означает успешный запуск.

```
Подмена метода `login` --> Вызов метода `_load_settings` --> Вызов метода `run` --> Проверка вызова метода `login` --> Проверка возвращаемого значения
```

**Примеры**:

```python
test_class = TestSupplier()
test_class.setUp()
with patch.object(test_class.supplier, 'login', return_value=True) as mock_login:
    test_class.supplier._load_settings()
    test_class.test_run_with_login()
```

### `test_run_without_login`

```python
def test_run_without_login(self):
    """
    Тестирует запуск без авторизации.
    Args:
        self (TestSupplier): Экземпляр класса TestSupplier.
    Returns:
        None
    """
    ...
```

**Назначение**:
Метод `test_run_without_login` тестирует запуск поставщика без авторизации. Он проверяет, что при вызове метода `run`, когда `if_login` установлен в `False`, метод `run_scenario_files` не вызывается, и возвращается `True`.

**Как работает функция**:

1.  **Установка `if_login` в `False`**: Устанавливается значение атрибута `self.supplier.login['if_login']` равным `False`, чтобы имитировать запуск без авторизации.
2.  **Подмена метода `run_scenario_files`**: Используется `patch.object` для подмены метода `run_scenario_files` объекта `self.supplier`. Метод `run_scenario_files` всегда возвращает `True`.
3.  **Вызов метода `_load_settings`**: Вызывается метод `_load_settings` объекта `self.supplier` для загрузки настроек.
4.  **Вызов метода `run`**: Вызывается метод `run` объекта `self.supplier`.
5.  **Проверка, что `run_scenario_files` не был вызван**: Проверяется, что метод `run_scenario_files` не был вызван.
6.  **Проверка возвращаемого значения**: Проверяется, что метод `run` возвращает `True`, что означает успешный запуск.

```
Установка `if_login` в `False` --> Подмена метода `run_scenario_files` --> Вызов метода `_load_settings` --> Вызов метода `run` --> Проверка, что `run_scenario_files` не был вызван --> Проверка возвращаемого значения
```

**Примеры**:

```python
test_class = TestSupplier()
test_class.setUp()
test_class.supplier.login['if_login'] = False
with patch.object(test_class.supplier, 'run_scenario_files', return_value=True) as mock_run_scenario_files:
    test_class.supplier._load_settings()
    test_class.test_run_without_login()