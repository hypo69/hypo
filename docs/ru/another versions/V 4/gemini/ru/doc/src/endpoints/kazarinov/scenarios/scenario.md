# Документация модуля `scenario`

## Обзор

Данный модуль предназначен для автоматизации процесса создания "мехирона" (mechiron) для Сергея Казаринова. Он извлекает, анализирует и обрабатывает данные о продуктах от различных поставщиков, подготавливает данные, обрабатывает их с помощью ИИ и интегрируется с Facebook для публикации продуктов.

## Подробней

Модуль автоматизирует процесс получения данных о товарах от различных поставщиков, их обработки с использованием AI, сохранения и подготовки отчетов, а также публикации в Facebook. Он предназначен для упрощения и ускорения процесса создания и публикации информации о продуктах.

## Содержание

1.  [Классы](#классы)
    *   [`MexironBuilder`](#mexironbuilder)
2.  [Функции](#функции)
    *   [`get_graber_by_supplier_url`](#get_graber_by_supplier_url)
    *   [`convert_product_fields`](#convert_product_fields)
    *   [`save_product_data`](#save_product_data)
    *   [`process_ai`](#process_ai)
    *   [`post_facebook`](#post_facebook)
    *   [`create_report`](#create_report)

## Классы

### `MexironBuilder`

**Описание**: Класс `MexironBuilder` предназначен для построения и выполнения сценариев обработки данных о продуктах, их анализа с использованием AI, сохранения и подготовки отчетов, а также публикации в Facebook.

**Методы**:

*   [`__init__`](#__init__): Инициализирует класс `MexironBuilder` с необходимыми компонентами.
*   [`run_scenario`](#run_scenario): Выполняет основной сценарий: извлекает данные о продуктах, обрабатывает их с помощью AI и сохраняет данные.
*   [`get_graber_by_supplier_url`](#get_graber_by_supplier_url): Возвращает соответствующий грабер для заданного URL поставщика.
*   [`convert_product_fields`](#convert_product_fields): Преобразует поля продукта в словарь.
*   [`save_product_data`](#save_product_data): Сохраняет данные о продукте в файл.
*   [`process_ai`](#process_ai): Обрабатывает список продуктов через AI-модель.
*   [`post_facebook`](#post_facebook): Выполняет сценарий публикации в Facebook.
*   [`create_report`](#create_report): Генерирует отчеты в формате HTML и PDF из обработанных данных.

**Параметры**:

*   `driver`: Экземпляр Selenium WebDriver.
*   `export_path`: Путь для экспорта данных.
*   `mexiron_name`: Пользовательское имя для процесса "мехирон".
*   `price`: Цена для обработки.
*   `timestamp`: Временная метка процесса.
*   `products_list`: Список обработанных данных о продуктах.
*   `model`: Google Generative AI модель.
*   `config`: Конфигурация, загруженная из JSON.

**Примеры**

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

### `get_graber_by_supplier_url`

```python
def get_graber_by_supplier_url(self, url: str):
    """
    Args:
        url (str): Supplier page URL.

    Returns:
        Graber instance if found, otherwise `None`.

    Raises:
         Ошибка выполнение

    Example:
        Примеры вызовов

    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Возвращает соответствующий грабер для заданного URL поставщика.

**Параметры**:

*   `url` (str): URL страницы поставщика.

**Возвращает**:

*   Graber: Экземпляр грабера, если найден.
*   `None`: Если грабер не найден.

**Примеры**:

```python
mexiron_builder = MexironBuilder(driver)
graber = mexiron_builder.get_graber_by_supplier_url('https://example.com')
if graber:
    print("Graber найден")
else:
    print("Graber не найден")
```

### `convert_product_fields`

```python
def convert_product_fields(self, f: ProductFields) -> dict:
    """
    Args:
        f (ProductFields): Object containing parsed product data.

    Returns:
        dict: Formatted dictionary of product data.

    Raises:
         Ошибка выполнение

    Example:
        Примеры вызовов

    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Преобразует поля продукта в словарь.

**Параметры**:

*   `f` (ProductFields): Объект, содержащий разобранные данные о продукте.

**Возвращает**:

*   `dict`: Отформатированный словарь данных о продукте.

**Примеры**:

```python
product_fields = ProductFields(...)
product_data = mexiron_builder.convert_product_fields(product_fields)
print(product_data)
```

### `save_product_data`

```python
def save_product_data(self, product_data: dict):
    """
    Args:
        product_data (dict): Formatted product data.

    Returns:
        dict: Formatted dictionary of product data.

    Raises:
         Ошибка выполнение

    Example:
        Примеры вызовов

    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Сохраняет данные о продукте в файл.

**Параметры**:

*   `product_data` (dict): Отформатированные данные о продукте.

**Примеры**:

```python
product_data = {'name': 'Example Product', 'price': 100}
mexiron_builder.save_product_data(product_data)
```

### `process_ai`

```python
def process_ai(self, products_list: List[str], lang: str, attempts: int = 3) -> tuple | bool:
    """
    Args:
        products_list (List[str]): List of product data dictionaries as strings.
        attempts (int): Number of retry attempts in case of failure.

    Returns:
        tuple | bool: Processed response in `ru` and `he` formats.

    Raises:
         Ошибка выполнение

    Example:
        Примеры вызовов

    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Обрабатывает список продуктов с использованием AI-модели.

**Параметры**:

*   `products_list` (List[str]): Список словарей данных о продуктах в виде строк.
*   `lang` (str): Язык обработки (`ru` или `he`).
*   `attempts` (int): Количество попыток повтора в случае неудачи.

**Возвращает**:

*   `tuple`: Обработанные ответы в форматах `ru` и `he`.
*   `bool`: `False` в случае неудачи.

**Примеры**:

```python
products_list = ["{'name': 'Product 1', 'price': 100}"]
result = mexiron_builder.process_ai(products_list, 'ru')
if result:
    print("AI обработка выполнена успешно")
else:
    print("AI обработка завершилась с ошибкой")
```

### `post_facebook`

```python
def post_facebook(self, mexiron: SimpleNamespace) -> bool:
    """
    Args:
        mexiron (SimpleNamespace): Processed data for publication.

    Returns:
        bool: `True` if publication is successful, otherwise `False`.

    Raises:
         Ошибка выполнение

    Example:
        Примеры вызовов

    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Выполняет сценарий публикации в Facebook.

**Параметры**:

*   `mexiron` (SimpleNamespace): Обработанные данные для публикации.

**Возвращает**:

*   `bool`: `True`, если публикация успешна, иначе `False`.

**Примеры**:

```python
mexiron_data = SimpleNamespace(...)
success = mexiron_builder.post_facebook(mexiron_data)
if success:
    print("Публикация в Facebook выполнена успешно")
else:
    print("Публикация в Facebook завершилась с ошибкой")
```

### `create_report`

```python
def create_report(self, data: dict, html_file: Path, pdf_file: Path):
    """
    Args:
        data (dict): Processed data.
        html_file (Path): Path to save the HTML report.
        pdf_file (Path): Path to save the PDF report.

    Returns:
        dict: Formatted dictionary of product data.

    Raises:
         Ошибка выполнение

    Example:
        Примеры вызовов

    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Генерирует HTML и PDF отчеты из обработанных данных.

**Параметры**:

*   `data` (dict): Обработанные данные.
*   `html_file` (Path): Путь для сохранения HTML отчета.
*   `pdf_file` (Path): Путь для сохранения PDF отчета.

**Примеры**:

```python
data = {'name': 'Example Product', 'price': 100}
html_path = Path('report.html')
pdf_path = Path('report.pdf')
mexiron_builder.create_report(data, html_path, pdf_path)