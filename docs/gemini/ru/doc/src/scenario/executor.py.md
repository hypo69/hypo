# Модуль для выполнения сценариев
## Обзор
Модуль `executor.py` предназначен для выполнения сценариев, загрузки их из файлов, а также обработки процесса извлечения информации о продуктах и вставки ее в PrestaShop. Он содержит функции для запуска сценариев, загрузки их из файлов и обработки процесса извлечения информации о продукте и вставки ее в PrestaShop.

## Подробнее
Модуль предоставляет функциональность для автоматизации процесса сбора данных о товарах с веб-сайтов поставщиков и их добавления в интернет-магазин PrestaShop. Он включает в себя функции для чтения сценариев из файлов, навигации по страницам товаров, извлечения данных и вставки их в PrestaShop. Этот модуль является центральным компонентом системы, отвечающим за координацию действий по сбору и публикации данных о товарах.
## Функции

### `dump_journal`

```python
def dump_journal(s, journal: dict) -> None:
    """
    Сохраняет данные журнала в файл JSON.

    Args:
        s (object): Объект поставщика (Supplier instance).
        journal (dict): Словарь, содержащий данные журнала.

    Returns:
        None
    """
```

**Назначение**: Функция `dump_journal` предназначена для сохранения данных журнала выполнения сценариев в файл в формате JSON.

**Параметры**:
- `s` (object): Объект поставщика, содержащий информацию о поставщике и путях к файлам.
- `journal` (dict): Словарь, содержащий данные журнала, такие как информация о выполненных сценариях, времени выполнения и статусе.

**Как работает функция**:
1. Формируется путь к файлу журнала, который включает в себя абсолютный путь к каталогу поставщика, подкаталог `_journal` и имя файла, сгенерированное на основе текущей временной метки.
2. Данные из словаря `journal` записываются в файл JSON по указанному пути с помощью функции `j_dumps`.

**Примеры**:
```python
from pathlib import Path
class Supplier:
    def __init__(self):
        self.supplier_abs_path = Path('./')  # Укажите путь к директории поставщика
supplier = Supplier()
journal_data = {'scenario_files': {'scenario1.json': {'status': 'completed'}}, 'name': '2024-10-26_15-00-00'}
dump_journal(supplier, journal_data)
```

### `run_scenario_files`

```python
def run_scenario_files(s, scenario_files_list: List[Path] | Path) -> bool:
    """
    Выполняет список файлов сценариев.

    Args:
        s (object): Объект поставщика (Supplier instance).
        scenario_files_list (List[Path] | Path): Список путей к файлам сценариев или один путь к файлу.

    Returns:
        bool: True, если все сценарии выполнены успешно, иначе False.

    Raises:
        TypeError: Если scenario_files_list не является списком или объектом Path.
    """
```

**Назначение**: Функция `run_scenario_files` предназначена для выполнения сценариев, загруженных из одного или нескольких файлов. Она принимает список файлов сценариев и последовательно выполняет каждый из них.

**Параметры**:
- `s` (object): Объект поставщика, содержащий общую конфигурацию и методы, необходимые для выполнения сценариев.
- `scenario_files_list` (List[Path] | Path): Список объектов `Path`, указывающих на файлы сценариев, или один объект `Path`, указывающий на файл сценария.

**Как работает функция**:

1.  **Проверка типа аргумента**: Функция проверяет, является ли `scenario_files_list` экземпляром `Path` или списком. Если это экземпляр `Path`, он преобразуется в список, содержащий только этот путь. Если это не список и не `Path`, вызывается исключение `TypeError`.
2.  **Инициализация журнала**: Инициализируется раздел `'scenario_files'` в глобальном журнале `_journal` для отслеживания выполнения сценариев.
3.  **Цикл по файлам сценариев**: Функция проходит по каждому файлу сценария в списке `scenario_files_list`.
4.  **Выполнение сценария**: Для каждого файла сценария вызывается функция `run_scenario_file`, которая выполняет сценарии, содержащиеся в файле.
5.  **Обработка результатов**: В зависимости от результата выполнения сценария, в журнал добавляется сообщение об успехе или неудаче. Также логируется соответствующее сообщение с использованием `logger.success` или `logger.error`.
6.  **Обработка исключений**: Если во время выполнения сценария возникает исключение, оно перехватывается, логируется как критическая ошибка, и в журнал добавляется сообщение об ошибке.

**Примеры**:

```python
from pathlib import Path
class Supplier:
    def __init__(self):
        self.supplier_abs_path = Path('./')  # Укажите путь к директории поставщика
supplier = Supplier()

# Пример вызова с одним файлом сценария
scenario_file = Path('scenario1.json')
run_scenario_files(supplier, scenario_file)

# Пример вызова со списком файлов сценариев
scenario_files = [Path('scenario1.json'), Path('scenario2.json')]
run_scenario_files(supplier, scenario_files)

# Пример вызова без указания списка файлов (используется s.scenario_files)
supplier.scenario_files = [Path('scenario1.json')]
run_scenario_files(supplier, [])
```

### `run_scenario_file`

```python
def run_scenario_file(s, scenario_file: Path) -> bool:
    """
    Загружает и выполняет сценарии из файла.

    Args:
        s (object): Объект поставщика (Supplier instance).
        scenario_file (Path): Путь к файлу сценария.

    Returns:
        bool: True, если сценарий выполнен успешно, иначе False.
    """
```

**Назначение**: Функция `run_scenario_file` загружает сценарии из указанного файла и выполняет их.

**Параметры**:
- `s` (object): Объект поставщика, содержащий необходимую информацию и методы для выполнения сценариев.
- `scenario_file` (Path): Объект `Path`, представляющий путь к файлу сценария.

**Как работает функция**:
1.  **Чтение файла сценария**: Сначала функция пытается загрузить содержимое файла сценария, используя функцию `j_loads`, и извлекает список сценариев из ключа `'scenarios'`.
2.  **Перебор сценариев**: Затем функция перебирает все сценарии в списке.
3.  **Выполнение сценария**: Для каждого сценария вызывается функция `run_scenario` для его выполнения.
4.  **Логирование результатов**: В зависимости от результата выполнения сценария, в лог записывается сообщение об успехе или неудаче.
5.  **Обработка ошибок**: Если во время загрузки или выполнения сценария возникает ошибка (например, файл не найден или содержит неверный JSON), функция перехватывает исключение, логирует критическую ошибку и возвращает `False`.

**Примеры**:

```python
from pathlib import Path
class Supplier:
    def __init__(self):
        self.supplier_abs_path = Path('./')  # Укажите путь к директории поставщика
supplier = Supplier()

# Пример вызова с существующим файлом сценария
scenario_file = Path('scenario1.json')
run_scenario_file(supplier, scenario_file)

# Пример вызова с несуществующим файлом сценария
scenario_file = Path('non_existent_scenario.json')
run_scenario_file(supplier, scenario_file)
```

### `run_scenarios`

```python
def run_scenarios(s, scenarios: Optional[List[dict] | dict] = None, _journal=None) -> List | dict | bool:
    """
    Выполняет список сценариев (НЕ ФАЙЛЫ).

    Args:
        s (object): Объект поставщика (Supplier instance).
        scenarios (Optional[List[dict] | dict], optional): Список сценариев или один сценарий в виде словаря. По умолчанию None.

    Returns:
        List | dict | bool: Результат выполнения сценариев или False в случае ошибки.

    Todo:
        Check the option when no scenarios are specified from all sides. For example, when s.current_scenario is not specified and scenarios are not specified.
    """
```

**Назначение**: Функция `run_scenarios` выполняет список сценариев, представленных в виде словарей.

**Параметры**:
- `s` (object): Объект поставщика, предоставляющий контекст и ресурсы для выполнения сценариев.
- `scenarios` (Optional[List[dict] | dict], optional): Список словарей, представляющих сценарии, или один словарь, представляющий сценарий. Если не указан, используется `s.current_scenario`. По умолчанию `None`.
- `_journal`: Переменная не используется внутри функции

**Как работает функция**:
1.  **Определение сценариев для выполнения**: Если аргумент `scenarios` не указан, функция использует сценарий, сохраненный в `s.current_scenario`.
2.  **Преобразование в список**: Если `scenarios` является словарем, он преобразуется в список, содержащий только этот словарь.
3.  **Выполнение сценариев**: Функция проходит по каждому сценарию в списке и вызывает функцию `run_scenario` для его выполнения. Результаты выполнения сохраняются в списке `res`.
4.  **Запись в журнал**: После выполнения каждого сценария результат записывается в журнал `_journal`, а также вызывается функция `dump_journal` для сохранения журнала на диск.

**Примеры**:

```python
from pathlib import Path
class Supplier:
    def __init__(self):
        self.supplier_abs_path = Path('./')  # Укажите путь к директории поставщика
supplier = Supplier()

# Пример вызова с одним сценарием
scenario = {'name': 'scenario1', 'url': 'http://example.com'}
result = run_scenarios(supplier, scenario)

# Пример вызова со списком сценариев
scenarios = [{'name': 'scenario1', 'url': 'http://example.com'}, {'name': 'scenario2', 'url': 'http://example.com'}]
result = run_scenarios(supplier, scenarios)

# Пример вызова без указания сценариев (используется s.current_scenario)
supplier.current_scenario = {'name': 'scenario1', 'url': 'http://example.com'}
result = run_scenarios(supplier)
```

### `run_scenario`

```python
def run_scenario(supplier, scenario: dict, scenario_name: str, _journal=None) -> List | dict | bool:
    """
    Выполняет полученный сценарий.

    Args:
        supplier (object): Объект поставщика (Supplier instance).
        scenario (dict): Словарь, содержащий детали сценария.
        scenario_name (str): Имя сценария.

    Returns:
        List | dict | bool: Результат выполнения сценария.

    Todo:
        Check the need for the scenario_name parameter.
    """
```

**Назначение**: Функция `run_scenario` выполняет один сценарий, который задан в виде словаря.

**Параметры**:
- `supplier` (object): Объект поставщика, предоставляющий контекст и ресурсы для выполнения сценария.
- `scenario` (dict): Словарь, содержащий детали сценария, такие как URL для открытия и локаторы для взаимодействия с веб-страницей.
- `scenario_name` (str): Имя сценария, используемое для логирования и отслеживания.
- `_journal`: Переменная не используется внутри функции

**Как работает функция**:

1.  **Инициализация**:
    *   Устанавливает объект поставщика `supplier` в локальную переменную `s`.
    *   Записывает в лог информацию о начале выполнения сценария.
    *   Сохраняет текущий сценарий в `s.current_scenario`.
    *   Получает объект драйвера из `s.driver`.
2.  **Навигация к URL**:
    *   Открывает URL, указанный в сценарии, с помощью `d.get_url(scenario['url'])`.
3.  **Получение списка товаров**:
    *   Вызывает функцию `s.related_modules.get_list_products_in_category(s)` для получения списка товаров в категории.
4.  **Обработка отсутствия товаров**:
    *   Если список товаров пуст, функция логирует предупреждение и возвращает `False`.
5.  **Перебор товаров**:
    *   Для каждого URL товара в списке:
        *   Открывает страницу товара с помощью `d.get_url(url)`. Если происходит ошибка навигации, логируется ошибка, и происходит переход к следующему URL.
        *   Вызывает функцию `s.related_modules.grab_product_page(s)` для извлечения полей продукта.
        *   Асинхронно вызывает функцию `s.related_modules.grab_page(s)` для извлечения дополнительных полей продукта. Если не удается извлечь поля, логируется ошибка, и происходит переход к следующему URL.
        *   Извлекает словари `presta_fields_dict` и `assist_fields_dict` из объекта `f: ProductFields`.
        *   Создает объект `Product` с использованием префикса поставщика и словаря полей PrestaShop.
        *   Вызывает функцию `insert_grabbed_data(f)` для вставки извлеченных данных.
        *   Обрабатывает исключения, которые могут возникнуть при сохранении продукта.
6.  **Завершение**:
    *   После перебора всех товаров функция возвращает список URL товаров.

**Примеры**:

```python
from pathlib import Path
class Supplier:
    def __init__(self):
        self.supplier_abs_path = Path('./')  # Укажите путь к директории поставщика
supplier = Supplier()

# Пример вызова с простым сценарием
scenario = {'name': 'scenario1', 'url': 'http://example.com'}
result = run_scenario(supplier, scenario, scenario['name'])

# Пример вызова с более сложным сценарием
scenario = {
    'name': 'scenario2',
    'url': 'http://example.com/category',
    'product_list_locator': {'by': 'css', 'selector': '.product-item a'},
    'product_fields': {
        'name': {'by': 'css', 'selector': '.product-title'},
        'price': {'by': 'css', 'selector': '.product-price'}
    }
}
result = run_scenario(supplier, scenario, scenario['name'])
```

### `insert_grabbed_data_to_prestashop`

```python
async def insert_grabbed_data_to_prestashop(
    f: ProductFields, coupon_code: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None
) -> bool:
    """
    Вставляет продукт в PrestaShop.

    Args:
        f (ProductFields): Экземпляр ProductFields, содержащий информацию о продукте.
        coupon_code (Optional[str], optional): Опциональный код купона. По умолчанию None.
        start_date (Optional[str], optional): Опциональная дата начала акции. По умолчанию None.
        end_date (Optional[str], optional): Опциональная дата окончания акции. По умолчанию None.

    Returns:
        bool: True, если вставка прошла успешно, иначе False.
    """
```

**Назначение**: Функция `insert_grabbed_data_to_prestashop` асинхронно вставляет данные о товаре в PrestaShop.

**Параметры**:
- `f` (ProductFields): Экземпляр `ProductFields`, содержащий информацию о продукте, такую как ID, имя, категория, цена и описание.
- `coupon_code` (Optional[str], optional): Опциональный код купона для товара. По умолчанию `None`.
- `start_date` (Optional[str], optional): Опциональная дата начала действия купона. По умолчанию `None`.
- `end_date` (Optional[str], optional): Опциональная дата окончания действия купона. По умолчанию `None`.

**Как работает функция**:
1.  **Создание экземпляра PrestaShop**: Создается экземпляр класса `PrestaShop`, который предоставляет методы для взаимодействия с API PrestaShop.
2.  **Вставка данных о продукте**: Вызывается асинхронный метод `presta.post_product_data` для отправки данных о продукте в PrestaShop. Передаются параметры продукта, такие как ID, имя, категория, цена, описание, а также код купона и даты его действия (если они указаны).
3.  **Обработка исключений**: Если во время вставки данных возникает исключение, оно перехватывается, логируется сообщение об ошибке, и функция возвращает `False`.

**Примеры**:

```python
from pathlib import Path
class ProductFields:
    def __init__(self):
        self.product_id = 123
        self.product_name = "Test Product"
        self.product_category = "Test Category"
        self.product_price = 99.99
        self.description = "Test Description"
supplier = Supplier()
# Пример вызова без указания параметров купона
f = ProductFields()
result = await insert_grabbed_data_to_prestashop(f)

# Пример вызова с указанием параметров купона
f = ProductFields()
coupon_code = "SUMMER20"
start_date = "2024-06-01"
end_date = "2024-08-31"
result = await insert_grabbed_data_to_prestashop(f, coupon_code, start_date, end_date)