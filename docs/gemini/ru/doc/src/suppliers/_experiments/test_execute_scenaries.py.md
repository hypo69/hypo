# Модуль тестирования сценариев выполнения (`test_execute_scenaries.py`)

## Обзор

Модуль `test_execute_scenaries.py` содержит набор тестов для проверки корректности выполнения сценариев, связанных с парсингом и обработкой данных о товарах. Он использует библиотеку `unittest` для организации тестов и `MagicMock` для создания заглушек, имитирующих поведение различных компонентов системы.

## Подробней

Модуль предназначен для тестирования основных функций выполнения сценариев: `run_scenarios`, `run_scenario_file`, `run_scenario`, и `grab_product_page`. Каждый тестовый класс имитирует определенные условия и проверяет, что функции ведут себя ожидаемым образом. Это включает в себя проверку вызовов функций, обработку данных и логирование ошибок.

## Классы

### `TestRunListOfScenarioFiles`

**Описание**: Класс содержит тесты для функции `run_scenarios`, которая отвечает за выполнение списка файлов сценариев.

**Методы**:

- `test_with_scenario_files_...ed()`: Тест проверяет случай, когда передается список файлов сценариев.
- `test_with_no_scenario_files_...ed()`: Тест проверяет случай, когда список файлов сценариев не передается, и функция должна использовать сценарии по умолчанию.

### `TestRunScenarioFile`

**Описание**: Класс содержит тесты для функции `run_scenario_file`, которая отвечает за выполнение сценария из файла.

**Методы**:

- `setUp()`: Подготавливает мок Supplier с необходимыми атрибутами.
- `test_run_scenario_file_webdriver()`: Тест проверяет выполнение сценария с использованием `webdriver`.
- `test_run_scenario_file_api()`: Тест проверяет выполнение сценария с использованием API.
- `test_run_scenario_file_no_scenarios()`: Тест проверяет случай, когда файл сценария не содержит сценариев.

### `TestGrabProductPage`

**Описание**: Класс содержит тесты для функции `grab_product_page`, которая отвечает за получение данных со страницы товара.

**Методы**:

- `setUp()`: Подготавливает мок Supplier.
- `test_grab_product_page_succesStringFormatterul()`: Тест проверяет успешное получение данных со страницы товара.
- `test_grab_product_page_failure()`: Тест проверяет случай, когда не все необходимые данные присутствуют на странице товара.

### `TestRunScenario`

**Описание**: Класс содержит тесты для функции `run_scenario`, которая отвечает за выполнение отдельного сценария.

**Методы**:

- `setUp()`: Подготавливает мок Supplier с необходимыми атрибутами.
- `tearDown()`: Метод очистки после выполнения каждого теста. В текущей версии не реализован (`...`).
- `test_run_scenario_no_url()`: Тест проверяет случай, когда в сценарии не указан URL.
- `test_run_scenario_valid_url()`: Тест проверяет выполнение сценария с валидным URL.
- `test_run_scenario_export_empty_list()`: Тест проверяет случай, когда после сбора данных список товаров пуст.

## Функции

### `run_scenarios`

**Назначение**: Выполняет список файлов сценариев или сценарии по умолчанию, если список не предоставлен.

**Параметры**:

- `s`: Мок Supplier, содержащий настройки и связанные модули.
- `scenario_files` (Optional[List[str]]): Список файлов сценариев для выполнения. По умолчанию `None`.

**Возвращает**:
- `bool`: Возвращает `True`, если выполнение успешно, иначе `False`.

**Как работает функция**:

1.  Проверяет, передан ли список файлов сценариев.
2.  Если список передан, выполняет сценарии из каждого файла.
3.  Если список не передан, использует сценарии по умолчанию из настроек.
4.  Вызывает `build_shop_categories`, если в настройках указана необходимость проверки категорий.
5.  Обновляет `current_scenario_filename` и `last_runned_scenario` в настройках.

**Примеры**:

```python
# Пример вызова функции с файлами сценариев
s = MagicMock()
scenario_files = ["scenario1.json", "scenario2.json"]
s.settings = {
    'check categories on site': False,
    'scenarios': ["default1.json", "default2.json"]
}
result = run_scenarios(s, scenario_files)
```

```python
# Пример вызова функции без файлов сценариев
s = MagicMock()
s.settings = {
    'check categories on site': True,
    'scenarios': ["default1.json", "default2.json"]
}
result = run_scenarios(s)
```

### `run_scenario_file`

**Назначение**: Выполняет сценарии, описанные в файле сценариев.

**Параметры**:

- `s`: Мок Supplier, содержащий настройки и сценарии.
- `scenario_file`: Имя файла сценариев для выполнения.

**Возвращает**:
- `bool`: Возвращает `True`, если выполнение успешно, иначе `False`.

**Как работает функция**:

1.  Определяет метод парсинга (webdriver или API) из настроек.
2.  Если метод парсинга - webdriver, загружает сценарии из файла и выполняет каждый сценарий.
3.  Если метод парсинга - API, вызывает функцию `run_scenario_file_via_api`.
4.  Логирует ошибку и возвращает `False`, если файл сценариев не содержит сценариев.

**Примеры**:

```python
# Пример вызова функции для webdriver
s = MagicMock()
s.current_scenario_filename = "test_scenario.json"
s.settings = {
    "parcing method [webdriver|api]": "webdriver"
}
s.dir_export_imagesECTORY_FOR_STORE = "/path/to/images"
s.scenarios = {
    "scenario1": {
        "url": "https://example.com",
        "steps": []
    },
    "scenario2": {
        "url": None,
        "steps": []
    }
}
run_scenario_file(s, "test_scenario.json")
```

```python
# Пример вызова функции для API
s = MagicMock()
s.current_scenario_filename = "test_scenario.json"
s.settings = {
    "parcing method [webdriver|api]": "api"
}
s.dir_export_imagesECTORY_FOR_STORE = "/path/to/images"
s.scenarios = {
    "scenario1": {
        "url": "https://example.com",
        "steps": []
    },
    "scenario2": {
        "url": None,
        "steps": []
    }
}
run_scenario_file(s, "test_scenario.json")
```

### `run_scenario`

**Назначение**: Выполняет отдельный сценарий.

**Параметры**:

- `supplier`: Мок Supplier, содержащий настройки и сценарии.
- `scenario`: Словарь, описывающий сценарий для выполнения.

**Возвращает**:
- `bool`: Возвращает `True`, если выполнение успешно, иначе `False`.

**Как работает функция**:

1.  Проверяет наличие URL в сценарии. Если URL отсутствует, возвращает `False`.
2.  Получает список товаров в категории с использованием `get_list_products_in_category`.
3.  Для каждого товара вызывает `grab_product_page` для получения данных.
4.  Экспортирует данные в файлы с использованием `export_files`.

**Примеры**:

```python
# Пример вызова функции с валидным URL
supplier = MagicMock()
supplier.settings = {'parcing method [webdriver|api]': 'webdriver'}
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

```python
# Пример вызова функции без URL
supplier = MagicMock()
scenario = {'name': 'scenario1', 'url': None}
supplier.scenarios = {'scenario1': scenario}
supplier.get_list_products_in_category = MagicMock(return_value=[])
result = supplier.run_scenario(scenario)
```

### `grab_product_page`

**Назначение**: Получает данные со страницы товара.

**Параметры**:

- `s`: Мок Supplier, содержащий метод `grab_product_page`.

**Возвращает**:
- `bool`: Возвращает `True`, если получение данных успешно, иначе `False`.

**Как работает функция**:

1.  Вызывает метод `grab_product_page` у Supplier для получения данных о товаре.
2.  Проверяет наличие необходимых данных (`id`, `price`, `name`).
3.  Добавляет полученные данные в список товаров (`s.p`).

**Примеры**:

```python
# Пример успешного получения данных
s = MagicMock()
s.grab_product_page = lambda _: {'id': '123', 'price': 19.99, 'name': 'Product Name'}
s.p = []
result = grab_product_page(s)
```

```python
# Пример неуспешного получения данных
s = MagicMock()
s.grab_product_page = lambda _: {'name': 'Product Name'}
s.p = []
result = grab_product_page(s)
```