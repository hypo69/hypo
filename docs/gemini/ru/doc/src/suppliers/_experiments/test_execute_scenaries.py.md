# Модуль `test_execute_scenarios.py`

## Обзор

Модуль содержит тесты для проверки функциональности выполнения сценариев, включая запуск сценариев из файлов, запуск отдельных сценариев и захват страниц продуктов. Он использует библиотеку `unittest` для создания тестовых случаев и `MagicMock` для имитации зависимостей.

## Подробнее

Этот модуль предназначен для тестирования основных функций, связанных с выполнением сценариев парсинга. В частности, проверяется корректность обработки списка файлов со сценариями, запуск сценариев из файла, а также захват данных со страниц продуктов. Модуль использует моки (mock objects) для изоляции тестируемых функций от внешних зависимостей, что позволяет проводить более надежные и предсказуемые тесты.

## Классы

### `TestRunListOfScenarioFiles`

**Описание**: Класс содержит тесты для функции `run_scenarios`, которая отвечает за запуск списка файлов со сценариями.

**Методы**:

- `test_with_scenario_files_...ed`: Тест проверяет запуск сценариев, когда передается список файлов со сценариями.
- `test_with_no_scenario_files_...ed`: Тест проверяет запуск сценариев, когда список файлов со сценариями не передан (используются сценарии по умолчанию).

### `TestRunScenarioFile`

**Описание**: Класс содержит тесты для функции `run_scenario_file`, которая отвечает за запуск сценария из указанного файла.

**Методы**:

- `setUp`: Метод, выполняемый перед каждым тестом. Создает мок объекта `Supplier` с необходимыми атрибутами и настройками.
- `test_run_scenario_file_webdriver`: Тест проверяет запуск сценария из файла с использованием вебдрайвера.
- `test_run_scenario_file_api`: Тест проверяет запуск сценария из файла с использованием API.
- `test_run_scenario_file_no_scenarios`: Тест проверяет ситуацию, когда в файле сценариев отсутствуют сценарии.

### `TestGrabProductPage`

**Описание**: Класс содержит тесты для функции `grab_product_page`, которая отвечает за захват данных со страницы продукта.

**Методы**:

- `setUp`: Метод, выполняемый перед каждым тестом. Создает инстанс класса `Supplier`.
- `test_grab_product_page_succesStringFormatterul`: Тест проверяет успешный захват данных со страницы продукта, когда все необходимые данные присутствуют.
- `test_grab_product_page_failure`: Тест проверяет ситуацию, когда при захвате данных со страницы продукта отсутствуют необходимые данные.

### `TestRunScenario`

**Описание**: Класс содержит тесты для функции `run_scenario`, которая отвечает за запуск отдельного сценария.

**Методы**:

- `setUp`: Метод, выполняемый перед каждым тестом. Создает инстанс класса `Supplier` и настраивает необходимые атрибуты.
- `tearDown`: Метод, выполняемый после каждого теста. 
- `test_run_scenario_no_url`: Тест проверяет ситуацию, когда в сценарии отсутствует URL.
- `test_run_scenario_valid_url`: Тест проверяет запуск сценария с валидным URL.
- `test_run_scenario_export_empty_list`: Тест проверяет ситуацию, когда после выполнения сценария список продуктов пуст (нечего экспортировать).

## Функции

### `run_scenarios`

```python
def run_scenarios(s, scenario_files=None):
    """Запускает сценарии парсинга либо из указанных файлов, либо из настроек по умолчанию.

    Args:
        s (MagicMock): Мок объекта `Supplier`, представляющий поставщика данных.
        scenario_files (list, optional): Список файлов со сценариями. По умолчанию `None`.

    Returns:
        bool: `True`, если все сценарии выполнены успешно, `False` в противном случае.

    Как работает функция:
    1. **Проверяет наличие списка файлов сценариев**:
       - Если `scenario_files` предоставлен, функция использует его для выполнения сценариев.
       - Если `scenario_files` не предоставлен, функция использует список сценариев из настроек `s.settings['scenarios']`.
    2. **Определяет, нужно ли проверять категории на сайте**:
       - Если в настройках `s.settings['check categories on site']` установлено значение `True`, функция вызывает `s.related_modules.build_shop_categories()` для построения категорий магазина.
    3. **Итерирует по файлам сценариев**:
       - Для каждого файла сценария в списке `scenario_files` или `s.settings['scenarios']` функция вызывает `run_scenario_file(s, scenario_file)`.
       - Обновляет `s.current_scenario_filename` и `s.settings['last_runned_scenario']` после каждого выполненного файла сценария.

    Схема работы функции:

    Проверка наличия файлов сценариев --> Определение, нужно ли проверять категории --> Итерация по файлам сценариев --> Обновление информации о текущем сценарии

    Примеры:
    - Запуск с указанием файлов сценариев:
      ```python
      s = MagicMock()
      scenario_files = ["scenario1.json", "scenario2.json"]
      s.settings = {'check categories on site': False, 'scenarios': ["default1.json", "default2.json"]}
      result = run_scenarios(s, scenario_files)
      ```
    - Запуск без указания файлов сценариев (используются сценарии по умолчанию):
      ```python
      s = MagicMock()
      s.settings = {'check categories on site': True, 'scenarios': ["default1.json", "default2.json"]}
      result = run_scenarios(s)
      ```
    """

### `run_scenario_file`

```python
def run_scenario_file(s, scenario_file):
    """Запускает сценарии парсинга из указанного файла.

    Args:
        s (MagicMock): Мок объекта `Supplier`, представляющий поставщика данных.
        scenario_file (str): Имя файла со сценариями.

    Returns:
        bool: `True`, если сценарии выполнены успешно, `False` в противном случае.

    Как работает функция:
    1. **Определяет метод парсинга**:
       - Проверяет значение `s.settings["parcing method [webdriver|api]"]` для определения метода парсинга (webdriver или api).
    2. **Загружает сценарии из файла**:
       - Загружает JSON-файл с помощью `j_loads(s.dir_scenarios + scenario_file)`.
       - Если `j_loads` возвращает `None` или в файле нет сценариев, логирует ошибку и возвращает `False`.
    3. **Выполняет сценарии**:
       - Если метод парсинга - "webdriver", итерирует по сценариям и вызывает `run_scenario(s, scenario)`.
       - Если метод парсинга - "api", вызывает `s.related_modules.run_scenario_file_via_api(s, scenario_file)`.

    Схема работы функции:

    Определение метода парсинга --> Загрузка сценариев из файла --> Выполнение сценариев

    Примеры:
    - Запуск с использованием webdriver:
      ```python
      s = MagicMock()
      s.settings = {"parcing method [webdriver|api]": "webdriver"}
      s.dir_scenarios = "/path/to/scenarios/"
      s.scenarios = {"scenario1": {"url": "https://example.com", "steps": []}}
      with patch("your_module.j_loads") as mock_j_loads:
          mock_j_loads.return_value = {"scenarios": s.scenarios}
          with patch("your_module.run_scenario") as mock_run_scenario:
              run_scenario_file(s, "test_scenario.json")
      ```
    - Запуск с использованием API:
      ```python
      s = MagicMock()
      s.settings = {"parcing method [webdriver|api]": "api"}
      with patch("your_module.related_modules.run_scenario_file_via_api") as mock_run_scenario_file_via_api:
          run_scenario_file(s, "test_scenario.json")
      ```
    """

### `grab_product_page`

```python
def grab_product_page(s):
    """Захватывает данные со страницы продукта.

    Args:
        s (Supplier): Объект `Supplier`, представляющий поставщика данных.

    Returns:
        bool: `True`, если данные успешно захвачены и добавлены в список продуктов, `False` в противном случае.

    Как работает функция:
    1. **Вызывает метод `grab_product_page` у объекта `Supplier`**:
       - Получает словарь с данными продукта, вызвав `s.grab_product_page(_)`.
    2. **Проверяет наличие необходимых данных**:
       - Проверяет наличие ключей 'id', 'price' и 'name' в полученном словаре.
    3. **Добавляет данные в список продуктов**:
       - Если все необходимые данные присутствуют, добавляет словарь в список `s.p`.

    Схема работы функции:

    Вызов метода grab_product_page у объекта Supplier --> Проверка наличия необходимых данных --> Добавление данных в список продуктов

    Примеры:
    - Успешный захват данных:
      ```python
      s = Supplier()
      s.grab_product_page = lambda _: {'id': '123', 'price': 19.99, 'name': 'Product Name'}
      result = grab_product_page(s)
      ```
    - Неудачный захват данных (отсутствуют необходимые данные):
      ```python
      s = Supplier()
      s.grab_product_page = lambda _: {'name': 'Product Name'}
      result = grab_product_page(s)
      ```
    """

### `run_scenario`

```python
def run_scenario(self, scenario: dict) -> bool:
    """Выполняет заданный сценарий парсинга.

    Args:
        scenario (dict): Словарь, содержащий информацию о сценарии.

    Returns:
        bool: `True`, если сценарий выполнен успешно, `False` в противном случае.

    Как работает функция:
    1. **Проверяет наличие URL в сценарии**:
       - Если URL отсутствует (`scenario['url'] is None`), функция возвращает `False`.
    2. **Получает список продуктов в категории**:
       - Вызывает `self.get_list_products_in_category(scenario['url'])` для получения списка URL продуктов в категории.
    3. **Итерирует по списку продуктов**:
       - Для каждого URL продукта вызывает `self.grab_product_page(url)` для захвата данных о продукте.
       - Если `self.grab_product_page(url)` возвращает `True`, добавляет данные продукта в список `self.p`.
    4. **Экспортирует данные**:
       - Если список `self.p` не пуст, вызывает `self.export_files` для экспорта данных в файлы.

    Схема работы функции:

    Проверка наличия URL --> Получение списка продуктов в категории --> Итерация по списку продуктов --> Экспорт данных

    Примеры:
    - Запуск сценария с валидным URL:
      ```python
      supplier = Supplier()
      scenario = {'name': 'scenario2', 'url': 'https://example.com/products'}
      supplier.get_list_products_in_category = MagicMock(return_value=['https://example.com/products/1', 'https://example.com/products/2'])
      supplier.grab_product_page = MagicMock(return_value=True)
      supplier.export_files = MagicMock()
      result = supplier.run_scenario(scenario)
      ```
    - Запуск сценария с пустым списком продуктов:
      ```python
      supplier = Supplier()
      scenario = {'name': 'scenario3', 'url': 'https://example.com/products'}
      supplier.get_list_products_in_category = MagicMock(return_value=['https://example.com/products/1'])
      supplier.grab_product_page = MagicMock(return_value=False)
      supplier.export_files = MagicMock()
      result = supplier.run_scenario(scenario)
      ```
    """

## Запуск тестов

В конце модуля находится блок `if __name__ == '__main__':`, который позволяет запускать тесты, определенные в этом модуле, при его непосредственном выполнении.