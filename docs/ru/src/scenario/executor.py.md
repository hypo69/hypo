# Модуль для выполнения сценариев
## Обзор

Модуль `executor.py` предназначен для выполнения сценариев, загрузки их из файлов и обработки процесса извлечения информации о продуктах и вставки их в PrestaShop.

## Подробнее

Этот модуль содержит функции для выполнения сценариев, загрузки их из файлов и обработки процесса извлечения информации о продуктах и вставки ее в PrestaShop. Он включает в себя функции для запуска сценариев из файлов, управления сеансами браузера и взаимодействия с PrestaShop API. Модуль использует глобальный журнал для отслеживания выполнения сценариев и включает обработку ошибок для обеспечения надежности процесса.

## Классы

В данном модуле классы отсутствуют

## Функции

### `dump_journal`

```python
def dump_journal(s, journal: dict) -> None:
    """
    Сохраняет данные журнала в файл JSON.

    Args:
        s (object): Экземпляр поставщика.
        journal (dict): Словарь, содержащий данные журнала.

    Returns:
        None
    """
```

**Назначение**: Функция сохраняет данные журнала (информацию о выполнении сценариев) в файл JSON.

**Параметры**:
- `s` (object): Экземпляр класса поставщика, содержащий информацию о поставщике.
- `journal` (dict): Словарь, содержащий данные журнала, которые нужно сохранить.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Как работает функция**:
1.  Определяется путь к файлу журнала, используя атрибут `supplier_abs_path` экземпляра поставщика `s` и текущую дату и время.
2.  Вызывается функция `j_dumps` для записи содержимого словаря `journal` в файл JSON по указанному пути.

```ascii
Получение пути к файлу журнала  -->  Запись данных журнала в файл JSON
```

**Примеры**:

Предположим, у нас есть экземпляр поставщика `s` и словарь `journal` с данными:

```python
class Supplier:
    def __init__(self, supplier_abs_path):
        self.supplier_abs_path = supplier_abs_path

s = Supplier('/path/to/supplier')
journal = {'name': 'test_scenario', 'status': 'completed'}
dump_journal(s, journal)
```

В результате будет создан файл `/path/to/supplier/_journal/test_scenario.json`, содержащий данные из словаря `journal`.

### `run_scenario_files`

```python
def run_scenario_files(s, scenario_files_list: List[Path] | Path) -> bool:
    """
    Выполняет список файлов сценариев.

    Args:
        s (object): Экземпляр поставщика.
        scenario_files_list (List[Path] | Path): Список путей к файлам сценариев или одиночный путь к файлу.

    Returns:
        bool: True, если все сценарии были выполнены успешно, False в противном случае.

    Raises:
        TypeError: Если scenario_files_list не является списком или объектом Path.
    """
```

**Назначение**: Функция выполняет сценарии, загружая их из указанных файлов.

**Параметры**:
- `s` (object): Экземпляр класса поставщика, содержащий общую конфигурацию и состояние.
- `scenario_files_list` (List[Path] | Path): Список объектов `Path`, указывающих на файлы сценариев, или один объект `Path`.

**Возвращает**:
- `bool`: `True`, если все сценарии из всех файлов были выполнены успешно, `False` в противном случае.

**Вызывает исключения**:
- `TypeError`: Если `scenario_files_list` не является экземпляром `Path` или списком.

**Как работает функция**:

1.  Проверяет тип `scenario_files_list`. Если это `Path`, преобразует его в список. Если это не список и не `Path`, вызывает исключение `TypeError`.
2.  Инициализирует запись в глобальном журнале `_journal` для отслеживания выполнения сценариев.
3.  Перебирает каждый файл сценария в `scenario_files_list`.
4.  Для каждого файла вызывает функцию `run_scenario_file` для выполнения сценариев, содержащихся в файле.
5.  Обновляет журнал `_journal` информацией об успехе или неудаче выполнения каждого сценария.
6.  Логирует результаты выполнения сценариев, используя `logger`.
7.  Возвращает `True`, если все сценарии выполнены успешно, в противном случае возвращает `False`.

```ascii
Проверка типа scenario_files_list --> Инициализация журнала  -->  Перебор файлов сценариев
--> Вызов run_scenario_file для каждого файла  -->  Обновление журнала  -->  Логирование результатов
```

**Примеры**:

```python
class Supplier:
    def __init__(self, scenario_files):
        self.scenario_files = scenario_files

# Пример с одним файлом сценария
s = Supplier([Path('scenario1.json')])
result = run_scenario_files(s, s.scenario_files)

# Пример со списком файлов сценариев
s = Supplier([Path('scenario1.json'), Path('scenario2.json')])
result = run_scenario_files(s, s.scenario_files)
```

### `run_scenario_file`

```python
def run_scenario_file(s, scenario_file: Path) -> bool:
    """
    Загружает и выполняет сценарии из файла.

    Args:
        s (object): Экземпляр поставщика.
        scenario_file (Path): Путь к файлу сценария.

    Returns:
        bool: True, если сценарий был выполнен успешно, False в противном случае.
    """
```

**Назначение**: Функция загружает сценарии из указанного файла и выполняет их.

**Параметры**:
- `s` (object): Экземпляр класса поставщика, содержащий общую конфигурацию и состояние.
- `scenario_file` (Path): Объект `Path`, указывающий на файл сценария.

**Возвращает**:
- `bool`: `True`, если все сценарии в файле были выполнены успешно, `False` в противном случае.

**Как работает функция**:

1.  Пытается загрузить сценарии из файла, используя функцию `j_loads`, и извлекает словарь сценариев из ключа `scenarios`.
2.  Перебирает сценарии в словаре.
3.  Для каждого сценария присваивает его атрибуту `current_scenario` экземпляра поставщика `s`.
4.  Вызывает функцию `run_scenario` для выполнения сценария.
5.  Логирует результаты выполнения сценария, используя `logger`.
6.  В случае возникновения исключений `FileNotFoundError` или `json.JSONDecodeError` логирует ошибку и возвращает `False`.
7.  Возвращает `True`, если все сценарии выполнены успешно, в противном случае возвращает `False`.

```ascii
Загрузка сценариев из файла  -->  Перебор сценариев  -->  Присвоение current_scenario
--> Вызов run_scenario для каждого сценария  -->  Логирование результатов
```

**Примеры**:

```python
class Supplier:
    def __init__(self):
        self.current_scenario = None

s = Supplier()
scenario_file = Path('scenario.json')
result = run_scenario_file(s, scenario_file)
```

### `run_scenarios`

```python
def run_scenarios(s, scenarios: Optional[List[dict] | dict] = None, _journal=None) -> List | dict | bool:
    """
    Выполняет список сценариев (НЕ ФАЙЛЫ).

    Args:
        s (object): Экземпляр поставщика.
        scenarios (Optional[List[dict] | dict], optional): Принимает список сценариев или одиночный сценарий в виде словаря. По умолчанию None.

    Returns:
        List | dict | bool: Результат выполнения сценариев или False в случае ошибки.

    Todo:
        Проверить вариант, когда сценарии не указаны со всех сторон. Например, когда s.current_scenario не указан и сценарии не указаны.
    """
```

**Назначение**: Функция выполняет переданные сценарии, которые представлены в виде списка словарей или одного словаря.

**Параметры**:
- `s` (object): Экземпляр класса поставщика, содержащий общую конфигурацию и состояние.
- `scenarios` (Optional[List[dict] | dict], optional): Список словарей, представляющих сценарии, или один словарь. Если не указан, используется `s.current_scenario`. По умолчанию `None`.
- `_journal`: Переменная, похоже, не используется

**Возвращает**:
- `List | dict | bool`: Результат выполнения сценариев. Возвращает список результатов, если передается список сценариев, результат одного сценария, если передан один сценарий, или `False` в случае ошибки.

**Как работает функция**:

1.  Если `scenarios` не указаны, используется `s.current_scenario`.
2.  Преобразует `scenarios` в список, если передан один сценарий в виде словаря.
3.  Перебирает сценарии в списке.
4.  Для каждого сценария вызывает функцию `run_scenario` для выполнения сценария.
5.  Обновляет журнал `_journal` результатом выполнения сценария.
6.  Сохраняет журнал с помощью функции `dump_journal`.
7.  Возвращает список результатов выполнения сценариев.

```ascii
Проверка scenarios --> Преобразование в список --> Перебор сценариев  -->  Вызов run_scenario для каждого сценария
--> Обновление журнала --> Сохранение журнала
```

**Примеры**:

```python
class Supplier:
    def __init__(self):
        self.current_scenario = {'name': 'default_scenario'}

s = Supplier()

# Пример с одним сценарием
scenario = {'name': 'scenario1'}
result = run_scenarios(s, scenario)

# Пример со списком сценариев
scenarios = [{'name': 'scenario1'}, {'name': 'scenario2'}]
result = run_scenarios(s, scenarios)

# Пример без указания scenarios (используется s.current_scenario)
result = run_scenarios(s)
```

### `run_scenario`

```python
def run_scenario(supplier, scenario: dict, scenario_name: str, _journal=None) -> List | dict | bool:
    """
    Выполняет полученный сценарий.

    Args:
        supplier (object): Экземпляр поставщика.
        scenario (dict): Словарь, содержащий детали сценария.
        scenario_name (str): Имя сценария.

    Returns:
        List | dict | bool: Результат выполнения сценария.

    Todo:
        Check the need for the scenario_name parameter.
    """
```

**Назначение**: Функция выполняет сценарий, извлекая информацию о продуктах со страницы и подготавливая данные для вставки в PrestaShop.

**Параметры**:

-   `supplier` (object): Экземпляр класса поставщика, содержащий общую конфигурацию, состояние и инструменты, необходимые для выполнения сценария.
-   `scenario` (dict): Словарь, содержащий детали сценария, такие как URL страницы, локаторы элементов и другие параметры.
-   `scenario_name` (str): Имя сценария для логирования и отслеживания.
-   `_journal`: Переменная, похоже, не используется

**Возвращает**:

-   `List | dict | bool`: Список URL продуктов в категории, если успешно, или `False` в случае неудачи.

**Как работает функция**:

1.  Инициализирует выполнение сценария, логируя начало сценария с именем `scenario_name`.
2.  Устанавливает `current_scenario` поставщика равным текущему сценарию.
3.  Получает экземпляр драйвера из поставщика.
4.  Открывает URL, указанный в сценарии, с помощью драйвера.
5.  Извлекает список продуктов в категории, используя метод `get_list_products_in_category` связанного модуля поставщика.
6.  Если список продуктов пуст, логирует предупреждение и возвращает `False`.
7.  Перебирает URL каждого продукта в списке.
8.  Для каждого URL открывает страницу продукта с помощью драйвера. Если происходит ошибка навигации, логирует ошибку и переходит к следующему URL.
9.  Извлекает поля страницы продукта, используя метод `grab_product_page` связанного модуля поставщика.
10. Асинхронно извлекает поля страницы, используя метод `grab_page` связанного модуля поставщика.
11. Если не удалось извлечь поля, логирует ошибку и переходит к следующему URL.
12. Разделяет извлеченные поля на `presta_fields_dict` и `assist_fields_dict`.
13. Создает экземпляр класса `Product` с использованием `presta_fields_dict`.
14. Вызывает функцию `insert_grabbed_data` для вставки извлеченных данных.
15. Если происходит ошибка при сохранении продукта, логирует ошибку и переходит к следующему URL.
16. Возвращает список URL продуктов в категории.

```ascii
Начало сценария --> Получение драйвера --> Открытие URL --> Извлечение списка продуктов
|
V
Если список пуст: логирование и возврат False
|
V
Перебор URL продуктов --> Открытие страницы продукта --> Извлечение полей страницы
|
V
Если не удалось извлечь поля: логирование и переход к следующему URL
|
V
Разделение полей --> Создание экземпляра Product --> Вставка данных
|
V
Если произошла ошибка: логирование и переход к следующему URL
|
V
Возврат списка URL продуктов
```

**Примеры**:

```python
class Supplier:
    def __init__(self, driver, related_modules, supplier_prefix):
        self.driver = driver
        self.related_modules = related_modules
        self.supplier_prefix = supplier_prefix
        self.current_scenario = {}

    def get_url(self, url):
        print(f"Navigating to {url}")
        return True

class Driver:
    def get_url(self, url):
        print(f"Driver navigating to {url}")
        return True

class RelatedModules:
    def get_list_products_in_category(self, s):
        return ["http://example.com/product1", "http://example.com/product2"]

    def grab_product_page(self, s):
        return {"name": "Product Name", "price": 100}
    
    async def grab_page(self, s):
        class ProductFields:
            def __init__(self):
                self.presta_fields_dict = {"name": "Product Name", "price": 100}
                self.assist_fields_dict = {"description": "Product Description"}
        return ProductFields()

class Product:
    def __init__(self, supplier_prefix, presta_fields_dict):
        self.fields = presta_fields_dict

def insert_grabbed_data(f):
    print(f"Inserting data: {f.presta_fields_dict}")


# Создаем экземпляры классов
driver = Driver()
related_modules = RelatedModules()
supplier = Supplier(driver, related_modules, "SUPPLIER")
scenario = {"url": "http://example.com/category"}

# Запускаем сценарий
result = run_scenario(supplier, scenario, "Test Scenario")
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
        coupon_code (Optional[str], optional): Необязательный код купона. По умолчанию None.
        start_date (Optional[str], optional): Необязательная дата начала акции. По умолчанию None.
        end_date (Optional[str], optional): Необязательная дата окончания акции. По умолчанию None.

    Returns:
        bool: True, если вставка прошла успешно, False в противном случае.
    """
```

**Назначение**: Функция отправляет данные о продукте в PrestaShop для создания или обновления информации о товаре.

**Параметры**:
- `f` (ProductFields): Экземпляр класса `ProductFields`, содержащий информацию о продукте.
- `coupon_code` (Optional[str], optional): Код купона для продукта. По умолчанию `None`.
- `start_date` (Optional[str], optional): Дата начала действия купона. По умолчанию `None`.
- `end_date` (Optional[str], optional): Дата окончания действия купона. По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если данные успешно отправлены в PrestaShop, `False` в противном случае.

**Как работает функция**:

1.  Создает экземпляр класса `PrestaShop`.
2.  Вызывает асинхронный метод `post_product_data` для отправки данных о продукте в PrestaShop.
3.  Обрабатывает возможные исключения, логирует ошибку и возвращает `False`, если произошла ошибка.

```ascii
Создание экземпляра PrestaShop  -->  Вызов post_product_data  -->  Обработка исключений
```

**Примеры**:

```python
class ProductFields:
    def __init__(self):
        self.product_id = 123
        self.product_name = "Test Product"
        self.product_category = "Test Category"
        self.product_price = 99.99
        self.description = "Test Description"

class PrestaShop:
    async def post_product_data(self, product_id, product_name, product_category, product_price, description, coupon_code, start_date, end_date):
        print("Sending data to PrestaShop...")
        return True

f = ProductFields()
async def main():
    result = await insert_grabbed_data_to_prestashop(f, coupon_code="COUPON123", start_date="2024-01-01", end_date="2024-01-31")
    print(result)

asyncio.run(main())