# Модуль: Скрипт создания "мехирона" Sergey Kazarinov's

## Обзор

Этот скрипт автоматизирует процесс создания "мехирона" для Sergey Kazarinov. Он извлекает, анализирует и обрабатывает данные о продуктах от различных поставщиков, подготавливает данные, обрабатывает их с помощью ИИ и интегрируется с Facebook для публикации продуктов. Скрипт расположен в директории `hypotez/src/endpoints/kazarinov/scenarios`.

## Подробнее

Основная задача скрипта - автоматизировать процесс сбора и обработки данных о товарах от различных поставщиков для последующей публикации в Facebook. Он включает в себя несколько этапов: извлечение данных, обработка данных с использованием AI, сохранение обработанных данных, генерация отчетов и публикация в Facebook. Скрипт предназначен для упрощения и ускорения процесса создания "мехирона", минимизируя ручной труд.

## Оглавление

- [Классы](#Классы)
    - [`MexironBuilder`](#MexironBuilder)
        - [`__init__`](#__init__)
        - [`run_scenario`](#run_scenario)
        - [`get_graber_by_supplier_url`](#get_graber_by_supplier_url)
        - [`convert_product_fields`](#convert_product_fields)
        - [`save_product_data`](#save_product_data)
        - [`process_ai`](#process_ai)
        - [`post_facebook`](#post_facebook)
        - [`create_report`](#create_report)
- [Использование](#Использование)
- [Зависимости](#Зависимости)
- [Обработка ошибок](#Обработка-ошибок)
- [Лицензия](#Лицензия)

## Классы

### `MexironBuilder`

**Описание**: Класс `MexironBuilder` предназначен для автоматизации процесса создания "мехирона", включая извлечение данных о продуктах, обработку с использованием AI, сохранение данных и публикацию в Facebook.

**Как работает класс**:
Класс инициализируется с помощью экземпляра `Driver` (Selenium WebDriver) и опционального имени "мехирона". Он содержит методы для загрузки конфигураций, запуска сценария обработки данных, получения грабера для URL поставщика, преобразования полей продукта, сохранения данных продукта, обработки данных с использованием AI, публикации в Facebook и создания отчетов. Класс является центральным элементом скрипта, координирующим различные этапы обработки данных.

**Атрибуты**:
- `driver`: Selenium WebDriver instance.
- `export_path`: Path for data export.
- `mexiron_name`: Custom name for the mechiron process.
- `price`: Price for processing.
- `timestamp`: Timestamp for the process.
- `products_list`: List of processed product data.
- `model`: Google Generative AI model.
- `config`: Configuration loaded from JSON.

#### `__init__`

**Описание**: Инициализирует класс `MexironBuilder` с необходимыми компонентами.

```python
def __init__(self, driver: Driver, mexiron_name: Optional[str] = None):
    """ This if example function
    Args:
        driver (Driver): Selenium WebDriver instance.
        mexiron_name (Optional[str], optional): Custom name for the mechiron process. Defaults to None.
    """
```

**Параметры**:
- `driver` (Driver): Экземпляр Selenium WebDriver.
- `mexiron_name` (Optional[str], optional): Пользовательское имя для процесса "мехирона". По умолчанию `None`.

**Примеры**:

```python
from src.webdriver.driver import Driver
from src.endpoints.kazarinov.scenarios.scenario_pricelist import MexironBuilder

# Инициализация Driver
driver = Driver(...)

# Инициализация MexironBuilder
mexiron_builder = MexironBuilder(driver, mexiron_name="TestMexiron")
```

#### `run_scenario`

**Описание**: Выполняет сценарий: анализирует продукты, обрабатывает их с помощью AI и сохраняет данные.

```python
def run_scenario(self, system_instruction: Optional[str] = None, price: Optional[str] = None, mexiron_name: Optional[str] = None, urls: Optional[str | List[str]] = None, bot = None) -> bool:
    """ This if example function
    Args:
        system_instruction (Optional[str], optional): System instructions for the AI model. Defaults to None.
        price (Optional[str], optional): Price for processing. Defaults to None.
        mexiron_name (Optional[str], optional): Custom mechiron name. Defaults to None.
        urls (Optional[str  |  List[str]], optional): URLs of product pages. Defaults to None.
    Returns:
        bool: True, если сценарий выполнен успешно, иначе False.
    """
```

**Как работает функция**:
Функция `run_scenario` выполняет основной сценарий обработки данных. Она начинается с проверки, предоставлены ли URL для анализа. Если URL предоставлены, функция определяет, является ли URL из OneTab, и извлекает данные соответственно. Затем функция ищет грабер для каждого URL, извлекает данные со страницы, преобразует поля продукта, сохраняет данные продукта, обрабатывает данные с помощью AI (на языках `he` и `ru`), сохраняет JSON для каждого языка, генерирует отчеты и отправляет PDF через Telegram. В случае возникновения ошибок на любом этапе, функция логирует ошибку и возвращает `True`.

**Параметры**:
- `system_instruction` (Optional[str], optional): Системные инструкции для модели AI. По умолчанию `None`.
- `price` (Optional[str], optional): Цена для обработки. По умолчанию `None`.
- `mexiron_name` (Optional[str], optional): Пользовательское имя для "мехирона". По умолчанию `None`.
- `urls` (Optional[str | List[str]], optional): URL-адреса страниц продуктов. По умолчанию `None`.
- `bot`:  <инструкция для модели gemini:параметр bot. Требуется дать определение и указать тип данных.>

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

#### `get_graber_by_supplier_url`

**Описание**: Возвращает соответствующий грабер для данного URL-адреса поставщика.

```python
def get_graber_by_supplier_url(self, url: str):
    """ This if example function
    Args:
        url (str): Supplier page URL.
    Returns:
        Graber instance if found, otherwise None.
    """
```

**Как работает функция**:
Функция принимает URL-адрес поставщика и пытается определить, какой грабер следует использовать для извлечения данных с этой страницы. Если соответствующий грабер найден, функция возвращает его экземпляр; в противном случае возвращается `None`.

**Параметры**:
- `url` (str): URL-адрес страницы поставщика.

**Возвращает**:
- Graber instance: Экземпляр грабера, если найден, иначе `None`.

#### `convert_product_fields`

**Описание**: Преобразует поля продукта в словарь.

```python
def convert_product_fields(self, f: ProductFields) -> dict:
    """ This if example function
    Args:
        f (ProductFields): Object containing parsed product data.
    Returns:
        dict: Formatted dictionary of product data.
    """
```

**Как работает функция**:
Функция принимает объект `ProductFields`, содержащий разобранные данные продукта, и преобразует его в отформатированный словарь. Это необходимо для стандартизации данных перед их сохранением или обработкой.

**Параметры**:
- `f` (ProductFields): Объект, содержащий разобранные данные продукта.

**Возвращает**:
- `dict`: Отформатированный словарь данных продукта.

#### `save_product_data`

**Описание**: Сохраняет данные продукта в файл.

```python
def save_product_data(self, product_data: dict):
    """ This if example function
    Args:
        product_data (dict): Formatted product data.
    """
```

**Как работает функция**:
Функция принимает словарь с отформатированными данными продукта и сохраняет его в файл. Это позволяет сохранить извлеченные и преобразованные данные для последующего использования.

**Параметры**:
- `product_data` (dict): Отформатированные данные продукта.

#### `process_ai`

**Описание**: Обрабатывает список продуктов через модель AI.

```python
def process_ai(self, products_list: List[str], lang: str, attempts: int = 3) -> tuple | bool:
    """ This if example function
    Args:
        products_list (List[str]): List of product data dictionaries as strings.
        attempts (int, optional): Number of retry attempts in case of failure. Defaults to 3.
    Returns:
        tuple | bool: Processed response in ru and he formats.
    """
```

**Как работает функция**:
Функция принимает список данных продуктов в виде строк, язык и количество попыток обработки. Она отправляет данные в модель AI для обработки и возвращает обработанный ответ в форматах `ru` и `he`. Если обработка не удалась после нескольких попыток, возвращается `False`.

**Параметры**:
- `products_list` (List[str]): Список словарей данных продуктов в виде строк.
- `lang` (str): Язык обработки (`ru` или `he`).
- `attempts` (int, optional): Количество попыток повтора в случае неудачи. По умолчанию `3`.

**Возвращает**:
- `tuple | bool`: Обработанный ответ в форматах `ru` и `he` или `False` в случае неудачи.

#### `post_facebook`

**Описание**: Выполняет сценарий публикации в Facebook.

```python
def post_facebook(self, mexiron: SimpleNamespace) -> bool:
    """ This if example function
    Args:
        mexiron (SimpleNamespace): Processed data for publication.
    Returns:
        bool: True if publication is successful, otherwise False.
    """
```

**Как работает функция**:
Функция принимает обработанные данные для публикации в Facebook и выполняет сценарий публикации. Она возвращает `True`, если публикация прошла успешно, и `False` в противном случае.

**Параметры**:
- `mexiron` (SimpleNamespace): Обработанные данные для публикации.

**Возвращает**:
- `bool`: `True`, если публикация выполнена успешно, иначе `False`.

#### `create_report`

**Описание**: Генерирует HTML и PDF отчеты из обработанных данных.

```python
def create_report(self, data: dict, html_file: Path, pdf_file: Path):
    """ This if example function
    Args:
        data (dict): Processed data.
        html_file (Path): Path to save the HTML report.
        pdf_file (Path): Path to save the PDF report.
    """
```

**Как работает функция**:
Функция принимает обработанные данные и пути для сохранения HTML и PDF отчетов. Она генерирует отчеты в указанных форматах на основе предоставленных данных.

**Параметры**:
- `data` (dict): Обработанные данные.
- `html_file` (Path): Путь для сохранения HTML отчета.
- `pdf_file` (Path): Путь для сохранения PDF отчета.

## Использование

Чтобы использовать этот скрипт, выполните следующие шаги:

1. **Инициализация Driver**: Создайте экземпляр класса `Driver`.
2. **Инициализация MexironBuilder**: Создайте экземпляр класса `MexironBuilder` с драйвером.
3. **Запуск сценария**: Вызовите метод `run_scenario` с необходимыми параметрами.

## Зависимости

- `selenium`: Для автоматизации веб-интерфейса.
- `asyncio`: Для асинхронных операций.
- `pathlib`: Для обработки путей к файлам.
- `types`: Для создания простых пространств имен.
- `typing`: Для аннотаций типов.
- `src.ai.gemini`: Для обработки данных с использованием AI.
- `src.suppliers.*.graber`: Для извлечения данных от различных поставщиков.
- `src.endpoints.advertisement.facebook.scenarios`: Для публикации в Facebook.

## Обработка ошибок

Скрипт включает надежную обработку ошибок для обеспечения непрерывного выполнения, даже если некоторые элементы не найдены или есть проблемы с веб-страницей. Это особенно полезно для обработки динамических или нестабильных веб-страниц.

## Лицензия

Этот скрипт лицензирован в соответствии с лицензией MIT. См. файл `LICENSE` для получения подробной информации.