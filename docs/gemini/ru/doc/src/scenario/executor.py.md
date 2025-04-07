# Модуль для выполнения сценариев
## Обзор

Этот модуль содержит функции для выполнения сценариев, загрузки их из файлов и обработки процесса извлечения информации о продукте и вставки ее в PrestaShop.

## Подробней
Модуль `executor.py` предназначен для автоматизации процесса сбора информации о товарах с веб-сайтов поставщиков и добавления этих товаров в PrestaShop. Он содержит функции для чтения сценариев из файлов, навигации по сайтам поставщиков, извлечения данных о товарах и вставки этих данных в PrestaShop.
Взаимодействие с PrestaShop выполняется с использованием асинхронных запросов. Все операции логируются для отслеживания процесса выполнения сценариев и выявления ошибок.

## Классы

В данном модуле классы не определены.

## Функции

### `dump_journal`

```python
def dump_journal(s, journal: dict) -> None:
    """
    Сохраняет данные журнала в файл JSON.

    Args:
        s (object): Инстанс поставщика.
        journal (dict): Словарь, содержащий данные журнала.

    Returns:
        None
    """
```

**Назначение**: Сохраняет информацию о ходе выполнения сценария в файл JSON. Это позволяет отслеживать, какие сценарии были выполнены, какие данные были собраны, и какие ошибки произошли.

**Параметры**:
- `s` (object): Объект поставщика, содержащий информацию о поставщике и конфигурацию.
- `journal` (dict): Словарь с данными журнала, которые необходимо сохранить.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Как работает функция**:
1. Формирует путь к файлу журнала, используя абсолютный путь поставщика и имя журнала.
2. Использует функцию `j_dumps` для записи содержимого словаря `journal` в файл JSON по указанному пути.

```ascii
Получение_пути_к_файлу_журнала --> Сохранение_данных_журнала_в_JSON
```

**Примеры**:

Предположим, что у нас есть объект поставщика `s` и словарь `journal`:

```python
class Supplier:
    def __init__(self, supplier_abs_path):
        self.supplier_abs_path = supplier_abs_path

s = Supplier('/path/to/supplier')
journal = {'name': 'test_scenario', 'status': 'completed'}

dump_journal(s, journal)
```

В результате выполнения этого кода будет создан файл `/path/to/supplier/_journal/test_scenario.json`, содержащий JSON-представление словаря `journal`.

### `run_scenario_files`

```python
def run_scenario_files(s, scenario_files_list: List[Path] | Path) -> bool:
    """
    Выполняет список файлов сценариев.

    Args:
        s (object): Инстанс поставщика.
        scenario_files_list (List[Path] | Path): Список путей к файлам сценариев или один путь к файлу.

    Returns:
        bool: True, если все сценарии были выполнены успешно, False в противном случае.

    Raises:
        TypeError: Если scenario_files_list не является списком или объектом Path.
    """
```

**Назначение**: Выполняет сценарии, загружая их из указанных файлов.

**Параметры**:
- `s` (object): Инстанс поставщика.
- `scenario_files_list` (List[Path] | Path): Список объектов `Path`, указывающих на файлы сценариев, или один объект `Path`, указывающий на файл сценария.

**Возвращает**:
- `bool`: `True`, если все сценарии были выполнены успешно, `False` в противном случае.

**Вызывает исключения**:
- `TypeError`: Если `scenario_files_list` не является списком или объектом `Path`.

**Как работает функция**:
1. Проверяет, является ли `scenario_files_list` экземпляром `Path`. Если это так, преобразует его в список, содержащий только этот путь.
2. Проверяет, является ли `scenario_files_list` списком. Если нет, вызывает исключение `TypeError`.
3. Если `scenario_files_list` пуст, использует `s.scenario_files` (список файлов сценариев, связанных с поставщиком).
4. Инициализирует запись для 'scenario_files' в глобальном журнале `_journal`.
5. Перебирает список файлов сценариев.
6. Для каждого файла сценария вызывает функцию `run_scenario_file`, чтобы выполнить сценарий.
7. Обновляет журнал (`_journal`) сообщением об успехе или неудаче выполнения сценария.
8. Если во время обработки файла сценария возникает исключение, записывает критическую ошибку в журнал и логирует ее.
9. Возвращает `True`.

```ascii
Проверка_типа_scenario_files_list --> Преобразование_в_список (если Path) --> Инициализация_журнала --> Для_каждого_файла_сценария: Выполнение_сценария (run_scenario_file) --> Обновление_журнала --> Возврат_True
```

**Примеры**:

```python
from pathlib import Path

class Supplier:
    def __init__(self, scenario_files):
        self.scenario_files = scenario_files

    def run_scenario_file(self, scenario_file: Path) -> bool:
      # Мок-функция для тестирования
      print(f"Выполняется сценарий {scenario_file}")
      return True

# Пример с одним файлом сценария
s = Supplier([])
scenario_file = Path('scenario1.json')
result = run_scenario_files(s, scenario_file)
print(result)

# Пример со списком файлов сценариев
s = Supplier([])
scenario_files = [Path('scenario1.json'), Path('scenario2.json')]
result = run_scenario_files(s, scenario_files)
print(result)
```

### `run_scenario_file`

```python
def run_scenario_file(s, scenario_file: Path) -> bool:
    """
    Загружает и выполняет сценарии из файла.

    Args:
        s (object): Инстанс поставщика.
        scenario_file (Path): Путь к файлу сценария.

    Returns:
        bool: True, если сценарий был выполнен успешно, False в противном случае.
    """
```

**Назначение**: Загружает сценарии из файла и последовательно их выполняет.

**Параметры**:
- `s` (object): Инстанс поставщика.
- `scenario_file` (Path): Путь к файлу сценария.

**Возвращает**:
- `bool`: `True`, если все сценарии в файле были выполнены успешно, `False` в случае ошибки.

**Как работает функция**:
1. Пытается загрузить содержимое файла сценария, используя функцию `j_loads`, и извлекает словарь сценариев из ключа `scenarios`.
2. Перебирает сценарии в словаре.
3. Для каждого сценария устанавливает текущий сценарий поставщика (`s.current_scenario`) и вызывает функцию `run_scenario` для выполнения сценария.
4. Логирует сообщение об успехе или неудаче выполнения сценария.
5. Если во время загрузки или обработки файла возникает исключение (`FileNotFoundError`, `json.JSONDecodeError`), логирует критическую ошибку и возвращает `False`.
6. Возвращает `True`.

```ascii
Загрузка_сценариев_из_файла (j_loads) --> Для_каждого_сценария: Установка_текущего_сценария_поставщика --> Выполнение_сценария (run_scenario) --> Логирование_результата --> Возврат_True
```

**Примеры**:

```python
from pathlib import Path
import json

class Supplier:
    def __init__(self):
        self.current_scenario = None
    
    def run_scenario(self, scenario: dict, scenario_name: str):
        # Мок-функция для тестирования
        print(f"Выполняется сценарий {scenario_name}: {scenario}")
        return True

# Создаем мок-файл сценария
scenario_data = {
    "scenarios": {
        "scenario1": {"url": "http://example.com/product1"},
        "scenario2": {"url": "http://example.com/product2"}
    }
}
with open("test_scenario.json", "w") as f:
    json.dump(scenario_data, f)

# Пример использования
s = Supplier()
scenario_file = Path("test_scenario.json")
result = run_scenario_file(s, scenario_file)
print(result)
```

### `run_scenarios`

```python
def run_scenarios(s, scenarios: Optional[List[dict] | dict] = None, _journal=None) -> List | dict | bool:
    """
    Выполняет список сценариев (НЕ ФАЙЛЫ).

    Args:
        s (object): Инстанс поставщика.
        scenarios (Optional[List[dict] | dict], optional): Список сценариев или один сценарий в виде словаря. По умолчанию None.

    Returns:
        List | dict | bool: Результат выполнения сценариев или False в случае ошибки.

    Todo:
        Check the option when no scenarios are specified from all sides. For example, when s.current_scenario is not specified and scenarios are not specified.
    """
```

**Назначение**: Выполняет предоставленные сценарии, которые передаются как список или как один сценарий.

**Параметры**:
- `s` (object): Инстанс поставщика.
- `scenarios` (Optional[List[dict] | dict], optional): Список словарей, представляющих сценарии, или один словарь, представляющий сценарий. По умолчанию `None`.
- `_journal`: Журнал выполнения.

**Возвращает**:
- `List | dict | bool`: Результат выполнения сценариев. Если передается список сценариев, возвращает список результатов. Если передается один сценарий, возвращает результат выполнения этого сценария. В случае ошибки возвращает `False`.

**Как работает функция**:
1. Если `scenarios` не указаны, использует текущий сценарий поставщика (`s.current_scenario`).
2. Преобразует `scenarios` в список, если это один сценарий.
3. Перебирает сценарии в списке.
4. Для каждого сценария вызывает функцию `run_scenario` для выполнения сценария.
5. Обновляет журнал (`_journal`) результатом выполнения сценария.
6. Сохраняет журнал с помощью функции `dump_journal`.
7. Возвращает список результатов выполнения сценариев.

```ascii
Проверка_наличия_сценариев --> Использование_текущего_сценария (если None) --> Преобразование_в_список (если один сценарий) --> Для_каждого_сценария: Выполнение_сценария (run_scenario) --> Обновление_журнала --> Сохранение_журнала --> Возврат_результатов
```

**Примеры**:

```python
class Supplier:
    def __init__(self):
        self.current_scenario = None
    
    def run_scenario(self, scenario: dict):
        # Мок-функция для тестирования
        print(f"Выполняется сценарий: {scenario}")
        return True

# Пример с одним сценарием
s = Supplier()
s.current_scenario = {"url": "http://example.com/product1"}
result = run_scenarios(s)
print(result)

# Пример со списком сценариев
s = Supplier()
scenarios = [
    {"url": "http://example.com/product1"},
    {"url": "http://example.com/product2"}
]
result = run_scenarios(s, scenarios)
print(result)
```

### `run_scenario`

```python
def run_scenario(supplier, scenario: dict, scenario_name: str, _journal=None) -> List | dict | bool:
    """
    Выполняет полученный сценарий.

    Args:
        supplier (object): Инстанс поставщика.
        scenario (dict): Словарь, содержащий детали сценария.
        scenario_name (str): Имя сценария.

    Returns:
        List | dict | bool: Результат выполнения сценария.

    Todo:
        Check the need for the scenario_name parameter.
    """
```

**Назначение**: Выполняет один сценарий, определенный в виде словаря.

**Параметры**:
- `supplier` (object): Инстанс поставщика.
- `scenario` (dict): Словарь, содержащий детали сценария, такие как URL для посещения и локаторы элементов для извлечения данных.
- `scenario_name` (str): Имя сценария для логирования и отслеживания.
- `_journal`: Журнал выполнения.

**Возвращает**:
- `List | dict | bool`: Список товаров в категории.

**Как работает функция**:
1. Устанавливает инстанс поставщика (`s`) и имя сценария.
2. Инициализирует драйвер (`d`) из инстанса поставщика.
3. Открывает URL, указанный в сценарии (`scenario['url']`), с помощью драйвера.
4. Получает список товаров в категории, используя `s.related_modules.get_list_products_in_category(s)`.
5. Проверяет, что список товаров не пуст. Если список пуст, логирует предупреждение и возвращает `False`.
6. Перебирает URL товаров в списке.
7. Для каждого URL открывает страницу товара с помощью драйвера. Если происходит ошибка навигации, логирует ошибку и переходит к следующему URL.
8. Извлекает поля страницы товара, используя `s.related_modules.grab_product_page(s)`.
9. Извлекает поля страницы товара, используя `s.related_modules.grab_page(s)`.
10. Разделяет полученные поля на `presta_fields_dict` и `assist_fields_dict`.
11. Создает инстанс класса `Product` с использованием префикса поставщика и полей PrestaShop.
12. Вызывает функцию `insert_grabbed_data` для вставки извлеченных данных.
13. Если во время создания или сохранения товара возникает исключение, логирует ошибку и переходит к следующему товару.
14. Возвращает список товаров в категории.

```ascii
Начало_сценария --> Получение_списка_товаров_в_категории --> Для_каждого_товара: Открытие_страницы_товара --> Извлечение_полей_страницы --> Создание_инстанса_Product --> Вставка_данных --> Возврат_списка_товаров
```

**Примеры**:

```python
class Driver:
    def get_url(self, url: str) -> bool:
        print(f"Открываю URL: {url}")
        return True

class RelatedModules:
    def get_list_products_in_category(self, s) -> list:
        return ["http://example.com/product1", "http://example.com/product2"]
    
    def grab_product_page(self, s) -> dict:
        return {"name": "Product Name"}

class Supplier:
    def __init__(self):
        self.driver = Driver()
        self.related_modules = RelatedModules()
        self.supplier_prefix = "SUPPLIER"

def insert_grabbed_data(f: dict) -> None:
    print(f"Вставляю данные: {f}")

# Пример использования
supplier = Supplier()
scenario = {"url": "http://example.com/category"}
scenario_name = "Test Scenario"
result = run_scenario(supplier, scenario, scenario_name)
print(result)
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

**Назначение**: Асинхронно вставляет данные о продукте в PrestaShop.

**Параметры**:
- `f` (ProductFields): Инстанс `ProductFields`, содержащий информацию о продукте для вставки.
- `coupon_code` (Optional[str], optional): Код купона для продукта. По умолчанию `None`.
- `start_date` (Optional[str], optional): Дата начала действия купона. По умолчанию `None`.
- `end_date` (Optional[str], optional): Дата окончания действия купона. По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если данные успешно вставлены в PrestaShop, `False` в противном случае.

**Как работает функция**:
1. Создает инстанс класса `PrestaShop`.
2. Вызывает асинхронный метод `presta.post_product_data` для отправки данных о продукте в PrestaShop.
3. Передает данные о продукте, такие как ID продукта, имя, категория, цена и описание, а также код купона и даты начала и окончания его действия.
4. Если во время вставки данных возникает исключение, логирует ошибку и возвращает `False`.
5. Возвращает результат вызова `presta.post_product_data`.

```ascii
Создание_инстанса_PrestaShop --> Отправка_данных_в_PrestaShop (presta.post_product_data) --> Обработка_исключений --> Возврат_результата
```

**Примеры**:

```python
class PrestaShop:
    async def post_product_data(self, product_id: str, product_name: str, product_category: str, product_price: float, description: str, coupon_code: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None) -> bool:
        # Мок-функция для тестирования
        print(f"Вставляю данные в PrestaShop: {product_id}, {product_name}, {product_category}, {product_price}, {description}, {coupon_code}, {start_date}, {end_date}")
        return True

class ProductFields:
    def __init__(self):
        self.product_id = "123"
        self.product_name = "Test Product"
        self.product_category = "Test Category"
        self.product_price = 99.99
        self.description = "Test Description"

# Пример использования
async def main():
    f = ProductFields()
    result = await insert_grabbed_data_to_prestashop(f, coupon_code="TESTCOUPON", start_date="2024-01-01", end_date="2024-01-31")
    print(result)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())