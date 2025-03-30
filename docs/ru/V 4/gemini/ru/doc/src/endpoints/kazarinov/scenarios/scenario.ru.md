# Сценарий создания мехирона для Сергея Казаринова

## Обзор

Этот скрипт является частью директории `hypotez/src/endpoints/kazarinov/scenarios` и предназначен для автоматизации процесса создания "мехирона" для Сергея Казаринова. Скрипт извлекает, парсит и обрабатывает данные о продуктах от различных поставщиков, подготавливает данные, обрабатывает их через ИИ и интегрирует с Facebook для публикации продуктов.

## Подорбней

Этот модуль автоматизирует процесс сбора, обработки и публикации данных о продуктах. Он использует различные граберы для извлечения информации с сайтов поставщиков, преобразует эти данные в структурированный формат, обрабатывает их с помощью моделей искусственного интеллекта и публикует результаты в Facebook. Основная цель - упростить и ускорить процесс создания рекламных объявлений и отчетов, связанных с продуктами.

## Классы

### `MexironBuilder`

**Описание**: Класс для построения и выполнения сценария создания мехирона.

**Методы**:
- `__init__`: Инициализирует класс `MexironBuilder`.
- `run_scenario`: Выполняет основной сценарий: парсит продукты, обрабатывает их через ИИ и сохраняет данные.
- `get_graber_by_supplier_url`: Возвращает соответствующий грабер для данного URL поставщика.
- `convert_product_fields`: Конвертирует поля продукта в словарь.
- `save_product_data`: Сохраняет данные о продукте в файл.
- `process_ai`: Обрабатывает список продуктов через модель ИИ.
- `post_facebook`: Выполняет сценарий публикации в Facebook.
- `create_report`: Генерирует HTML и PDF отчеты из обработанных данных.

**Параметры**:
- `driver`: Экземпляр Selenium WebDriver.
- `export_path`: Путь для экспорта данных.
- `mexiron_name`: Пользовательское имя для процесса мехирона.
- `price`: Цена для обработки.
- `timestamp`: Метка времени для процесса.
- `products_list`: Список обработанных данных о продуктах.
- `model`: Модель Google Generative AI.
- `config`: Конфигурация, загруженная из JSON.

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

## Функции

### `__init__`

```python
def __init__(self, driver: Driver, mexiron_name: Optional[str] = None):
    """
    Args:
        driver (Driver): Экземпляр Selenium WebDriver.
        mexiron_name (Optional[str], optional): Пользовательское имя для процесса мехирона. По умолчанию None.
    """
    ...
```

**Описание**: Инициализирует класс `MexironBuilder` с необходимыми компонентами.

**Параметры**:
- `driver` (Driver): Экземпляр Selenium WebDriver.
- `mexiron_name` (Optional[str], optional): Пользовательское имя для процесса мехирона. По умолчанию `None`.

### `run_scenario`

```python
def run_scenario(self, system_instruction: Optional[str] = None, price: Optional[str] = None, mexiron_name: Optional[str] = None, urls: Optional[str | List[str]] = None, bot = None) -> bool:
    """
    Args:
        system_instruction (Optional[str], optional): Системные инструкции для модели ИИ. По умолчанию None.
        price (Optional[str], optional): Цена для обработки. По умолчанию None.
        mexiron_name (Optional[str], optional): Пользовательское имя мехирона. По умолчанию None.
        urls (Optional[str | List[str]], optional): URLs страниц продуктов. По умолчанию None.
        bot: Объект бота (не указан тип). По умолчанию None.

    Returns:
        bool: True, если сценарий выполнен успешно, иначе False.
    """
    ...
```

**Описание**: Выполняет сценарий: парсит продукты, обрабатывает их через ИИ и сохраняет данные.

**Параметры**:
- `system_instruction` (Optional[str], optional): Системные инструкции для модели ИИ. По умолчанию `None`.
- `price` (Optional[str], optional): Цена для обработки. По умолчанию `None`.
- `mexiron_name` (Optional[str], optional): Пользовательское имя мехирона. По умолчанию `None`.
- `urls` (Optional[str | List[str]], optional): URLs страниц продуктов. По умолчанию `None`.
- `bot`: Объект бота (не указан тип). По умолчанию `None`.

**Возвращает**:
- `bool`: `True`, если сценарий выполнен успешно, иначе `False`.

**Примеры**:
```python
urls = ['https://example.com/product1', 'https://example.com/product2']
mexiron_builder.run_scenario(urls=urls)
```

### `get_graber_by_supplier_url`

```python
def get_graber_by_supplier_url(self, url: str):
    """
    Args:
        url (str): URL страницы поставщика.

    Returns:
        Экземпляр грабера, если найден, иначе None.
    """
    ...
```

**Описание**: Возвращает соответствующий грабер для данного URL поставщика.

**Параметры**:
- `url` (str): URL страницы поставщика.

**Возвращает**:
- Экземпляр грабера, если найден, иначе `None`.

### `convert_product_fields`

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

**Параметры**:
- `f` (ProductFields): Объект, содержащий парсированные данные о продукте.

**Возвращает**:
- `dict`: Форматированный словарь данных о продукте.

### `save_product_data`

```python
def save_product_data(self, product_data: dict):
    """
    Args:
        product_data (dict): Форматированные данные о продукте.
    """
    ...
```

**Описание**: Сохраняет данные о продукте в файл.

**Параметры**:
- `product_data` (dict): Форматированные данные о продукте.

### `process_ai`

```python
def process_ai(self, products_list: List[str], lang: str, attempts: int = 3) -> tuple | bool:
    """
    Args:
        products_list (List[str]): Список словарей данных о продуктах в виде строки.
        lang (str): Язык для обработки.
        attempts (int, optional): Количество попыток повторного запроса в случае неудачи. По умолчанию 3.

    Returns:
        tuple | bool: Обработанный ответ в форматах ru и he.
    """
    ...
```

**Описание**: Обрабатывает список продуктов через модель ИИ.

**Параметры**:
- `products_list` (List[str]): Список словарей данных о продуктах в виде строки.
- `lang` (str): Язык для обработки.
- `attempts` (int, optional): Количество попыток повторного запроса в случае неудачи. По умолчанию `3`.

**Возвращает**:
- `tuple | bool`: Обработанный ответ в форматах `ru` и `he`.

### `post_facebook`

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

**Параметры**:
- `mexiron` (SimpleNamespace): Обработанные данные для публикации.

**Возвращает**:
- `bool`: `True`, если публикация успешна, иначе `False`.

### `create_report`

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

**Параметры**:
- `data` (dict): Обработанные данные.
- `html_file` (Path): Путь для сохранения HTML отчета.
- `pdf_file` (Path): Путь для сохранения PDF отчета.