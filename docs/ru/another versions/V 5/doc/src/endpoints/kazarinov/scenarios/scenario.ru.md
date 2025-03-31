# Сценарий создания мехирона для Сергея Казаринова

## Обзор

Этот скрипт является частью директории `hypotez/src/endpoints/kazarinov/scenarios` и предназначен для автоматизации процесса создания "мехирона" для Сергея Казаринова. Скрипт извлекает, парсит и обрабатывает данные о продуктах от различных поставщиков, подготавливает данные, обрабатывает их через ИИ и интегрирует с Facebook для публикации продуктов.

## Подорбней

Данный скрипт автоматизирует процесс создания "мехирона", который включает в себя извлечение данных о продуктах от разных поставщиков, их обработку с использованием ИИ, сохранение результатов и публикацию в Facebook. Скрипт использует различные компоненты проекта, такие как граберы для парсинга данных с веб-страниц поставщиков, модель Google Generative AI для обработки данных, а также инструменты для создания отчетов и публикации в Facebook.

## Классы

### `MexironBuilder`

**Описание**: Класс предназначен для построения и выполнения сценария "мехирона", включающего парсинг данных о продуктах, их обработку с использованием ИИ и сохранение результатов.

**Как работает класс**:
Класс `MexironBuilder` инициализируется с экземпляром Selenium WebDriver и пользовательским именем для процесса "мехирона". Он загружает конфигурацию из JSON, устанавливает путь для экспорта данных, загружает системные инструкции для модели ИИ и инициализирует модель Google Generative AI. Основной метод `run_scenario` выполняет сценарий: парсит продукты с использованием граберов, конвертирует поля продукта в словарь, сохраняет данные, обрабатывает их через ИИ и генерирует отчеты. Класс также включает методы для получения грабера по URL поставщика, конвертации полей продукта, сохранения данных о продукте, обработки списка продуктов через ИИ и публикации в Facebook.

**Методы**:
- `__init__`
- `run_scenario`
- `get_graber_by_supplier_url`
- `convert_product_fields`
- `save_product_data`
- `process_ai`
- `post_facebook`
- `create_report`

**Атрибуты**:
- `driver`: Экземпляр Selenium WebDriver.
- `export_path`: Путь для экспорта данных.
- `mexiron_name`: Пользовательское имя для процесса мехирона.
- `price`: Цена для обработки.
- `timestamp`: Метка времени для процесса.
- `products_list`: Список обработанных данных о продуктах.
- `model`: Модель Google Generative AI.
- `config`: Конфигурация, загруженная из JSON.

### `__init__(self, driver: Driver, mexiron_name: Optional[str] = None)`

```python
def __init__(self, driver: Driver, mexiron_name: Optional[str] = None):
    """
    Args:
        driver (Driver): Экземпляр Selenium WebDriver.
        mexiron_name (Optional[str], optional): Пользовательское имя для процесса мехирона. Defaults to None.

    """
    ...
```

**Описание**: Инициализирует класс `MexironBuilder` с необходимыми компонентами.

**Как работает функция**:
Функция инициализирует экземпляр класса `MexironBuilder`, принимая в качестве аргументов экземпляр Selenium WebDriver и пользовательское имя для процесса "мехирона". Она устанавливает значения атрибутов класса, таких как `driver`, `export_path`, `mexiron_name`, `price`, `timestamp`, `products_list`, `model` и `config`.

**Параметры**:
- `driver` (Driver): Экземпляр Selenium WebDriver.
- `mexiron_name` (Optional[str], optional): Пользовательское имя для процесса мехирона. По умолчанию `None`.

**Примеры**:

```python
from src.webdriver.driver import Driver
from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder

# Инициализация Driver
driver = Driver(...)

# Инициализация MexironBuilder
mexiron_builder = MexironBuilder(driver, mexiron_name='my_mexiron')
```

### `run_scenario(self, system_instruction: Optional[str] = None, price: Optional[str] = None, mexiron_name: Optional[str] = None, urls: Optional[str | List[str]] = None, bot = None) -> bool`

```python
def run_scenario(self, system_instruction: Optional[str] = None, price: Optional[str] = None, mexiron_name: Optional[str] = None, urls: Optional[str | List[str]] = None, bot = None) -> bool:
    """
    Args:
        system_instruction (Optional[str], optional): Системные инструкции для модели ИИ. Defaults to None.
        price (Optional[str], optional): Цена для обработки. Defaults to None.
        mexiron_name (Optional[str], optional): Пользовательское имя мехирона. Defaults to None.
        urls (Optional[str | List[str]], optional): URLs страниц продуктов. Defaults to None.
        bot (_type_, optional): Defaults to None.

    Returns:
        bool: True, если сценарий выполнен успешно, иначе False.
    """
    ...
```

**Описание**: Выполняет сценарий: парсит продукты, обрабатывает их через ИИ и сохраняет данные.

**Как работает функция**:
Функция `run_scenario` выполняет основной сценарий "мехирона". Она принимает системные инструкции для модели ИИ, цену для обработки, пользовательское имя мехирона и URLs страниц продуктов в качестве параметров. Сценарий включает проверку источника URL (OneTab), поиск грабера для парсинга данных, преобразование данных в нужный формат, сохранение данных, обработку данных через AI для языков `he` и `ru`, генерацию отчетов и отправку PDF через Telegram.

**Параметры**:
- `system_instruction` (Optional[str], optional): Системные инструкции для модели ИИ. По умолчанию `None`.
- `price` (Optional[str], optional): Цена для обработки. По умолчанию `None`.
- `mexiron_name` (Optional[str], optional): Пользовательское имя мехирона. По умолчанию `None`.
- `urls` (Optional[str | List[str]], optional): URLs страниц продуктов. По умолчанию `None`.
- `bot` (_type_, optional): Бот для отправки сообщений. По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если сценарий выполнен успешно, иначе `False`.

**Примеры**:

```python
from src.webdriver.driver import Driver
from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder

# Инициализация Driver
driver = Driver(...)

# Инициализация MexironBuilder
mexiron_builder = MexironBuilder(driver)

# Запуск сценария
urls = ['https://example.com/product1', 'https://example.com/product2']
mexiron_builder.run_scenario(urls=urls)
```

### `get_graber_by_supplier_url(self, url: str)`

```python
def get_graber_by_supplier_url(self, url: str):
    """
    Args:
        url (str): URL страницы поставщика.

    Returns:
        _type_: Экземпляр грабера, если найден, иначе None.
    """
    ...
```

**Описание**: Возвращает соответствующий грабер для данного URL поставщика.

**Как работает функция**:
Функция `get_graber_by_supplier_url` принимает URL страницы поставщика в качестве параметра и возвращает соответствующий грабер для этого URL. Если грабер не найден, функция возвращает `None`.

**Параметры**:
- `url` (str): URL страницы поставщика.

**Возвращает**:
- Экземпляр грабера, если найден, иначе `None`.

**Примеры**:

```python
from src.webdriver.driver import Driver
from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder

# Инициализация Driver
driver = Driver(...)

# Инициализация MexironBuilder
mexiron_builder = MexironBuilder(driver)

# Получение грабера по URL
url = 'https://example.com/product1'
graber = mexiron_builder.get_graber_by_supplier_url(url)
```

### `convert_product_fields(self, f: ProductFields) -> dict`

```python
def convert_product_fields(self, f: ProductFields) -> dict:
    """
    Args:
        f (ProductFields): Объект, содержащий парсированные данные о продукте.

    Returns:
        dict: Форматированный словарь данных о продукте.
    """
    ...
```

**Описание**: Конвертирует поля продукта в словарь.

**Как работает функция**:
Функция `convert_product_fields` принимает объект `ProductFields`, содержащий парсированные данные о продукте, и конвертирует эти данные в форматированный словарь.

**Параметры**:
- `f` (ProductFields): Объект, содержащий парсированные данные о продукте.

**Возвращает**:
- `dict`: Форматированный словарь данных о продукте.

**Примеры**:

```python
from src.webdriver.driver import Driver
from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder
from src.suppliers.example.graber import ProductFields

# Инициализация Driver
driver = Driver(...)

# Инициализация MexironBuilder
mexiron_builder = MexironBuilder(driver)

# Создание объекта ProductFields
product_fields = ProductFields(...)

# Конвертация полей продукта
product_data = mexiron_builder.convert_product_fields(product_fields)
```

### `save_product_data(self, product_data: dict)`

```python
def save_product_data(self, product_data: dict):
    """
    Args:
        product_data (dict): Форматированные данные о продукте.
    """
    ...
```

**Описание**: Сохраняет данные о продукте в файл.

**Как работает функция**:
Функция `save_product_data` принимает форматированные данные о продукте в виде словаря и сохраняет эти данные в файл.

**Параметры**:
- `product_data` (dict): Форматированные данные о продукте.

**Примеры**:

```python
from src.webdriver.driver import Driver
from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder

# Инициализация Driver
driver = Driver(...)

# Инициализация MexironBuilder
mexiron_builder = MexironBuilder(driver)

# Форматированные данные о продукте
product_data = {'name': 'Product 1', 'price': '100'}

# Сохранение данных о продукте
mexiron_builder.save_product_data(product_data)
```

### `process_ai(self, products_list: List[str], lang: str, attempts: int = 3) -> tuple | bool`

```python
def process_ai(self, products_list: List[str], lang: str, attempts: int = 3) -> tuple | bool:
    """
    Args:
        products_list (List[str]): Список словарей данных о продуктах в виде строки.
        lang (str): _type_:
        attempts (int, optional): Количество попыток повторного запроса в случае неудачи. Defaults to 3.

    Returns:
        tuple | bool: Обработанный ответ в форматах ru и he.
    """
    ...
```

**Описание**: Обрабатывает список продуктов через модель ИИ.

**Как работает функция**:
Функция `process_ai` принимает список словарей данных о продуктах в виде строки и обрабатывает эти данные через модель ИИ для указанного языка. Функция выполняет несколько попыток повторного запроса в случае неудачи.

**Параметры**:
- `products_list` (List[str]): Список словарей данных о продуктах в виде строки.
- `lang` (str): Язык для обработки (например, 'ru' или 'he').
- `attempts` (int, optional): Количество попыток повторного запроса в случае неудачи. По умолчанию `3`.

**Возвращает**:
- `tuple | bool`: Обработанный ответ в форматах `ru` и `he`.

**Примеры**:

```python
from src.webdriver.driver import Driver
from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder

# Инициализация Driver
driver = Driver(...)

# Инициализация MexironBuilder
mexiron_builder = MexironBuilder(driver)

# Список данных о продуктах
products_list = ["{'name': 'Product 1', 'price': '100'}"]

# Обработка данных через AI
result = mexiron_builder.process_ai(products_list, lang='ru')
```

### `post_facebook(self, mexiron: SimpleNamespace) -> bool`

```python
def post_facebook(self, mexiron: SimpleNamespace) -> bool:
    """
    Args:
        mexiron (SimpleNamespace): Обработанные данные для публикации.

    Returns:
        bool: True, если публикация успешна, иначе False.
    """
    ...
```

**Описание**: Выполняет сценарий публикации в Facebook.

**Как работает функция**:
Функция `post_facebook` принимает обработанные данные в виде объекта `SimpleNamespace` и выполняет сценарий публикации этих данных в Facebook.

**Параметры**:
- `mexiron` (SimpleNamespace): Обработанные данные для публикации.

**Возвращает**:
- `bool`: `True`, если публикация успешна, иначе `False`.

**Примеры**:

```python
from src.webdriver.driver import Driver
from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder
from types import SimpleNamespace

# Инициализация Driver
driver = Driver(...)

# Инициализация MexironBuilder
mexiron_builder = MexironBuilder(driver)

# Обработанные данные
mexiron_data = SimpleNamespace(name='Product 1', price='100')

# Публикация в Facebook
result = mexiron_builder.post_facebook(mexiron_data)
```

### `create_report(self, data: dict, html_file: Path, pdf_file: Path)`

```python
def create_report(self, data: dict, html_file: Path, pdf_file: Path):
    """
    Args:
        data (dict): Обработанные данные.
        html_file (Path): Путь для сохранения HTML отчета.
        pdf_file (Path): Путь для сохранения PDF отчета.
    """
    ...
```

**Описание**: Генерирует HTML и PDF отчеты из обработанных данных.

**Как работает функция**:
Функция `create_report` принимает обработанные данные, путь для сохранения HTML отчета и путь для сохранения PDF отчета в качестве параметров. Она генерирует HTML и PDF отчеты из обработанных данных и сохраняет их по указанным путям.

**Параметры**:
- `data` (dict): Обработанные данные.
- `html_file` (Path): Путь для сохранения HTML отчета.
- `pdf_file` (Path): Путь для сохранения PDF отчета.

**Примеры**:

```python
from src.webdriver.driver import Driver
from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder
from pathlib import Path

# Инициализация Driver
driver = Driver(...)

# Инициализация MexironBuilder
mexiron_builder = MexironBuilder(driver)

# Обработанные данные
data = {'name': 'Product 1', 'price': '100'}

# Пути для сохранения отчетов
html_file = Path('report.html')
pdf_file = Path('report.pdf')

# Создание отчетов
mexiron_builder.create_report(data, html_file, pdf_file)
```

## Функции

### Описание функций и их параметров
В этом файле нет отдельных функций вне класса `MexironBuilder`. Все методы, описанные выше, являются частью класса.