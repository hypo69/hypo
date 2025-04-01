# Модуль `quotation_builder.py`

## Обзор

Модуль `quotation_builder.py` предназначен для обработки данных о продуктах от различных поставщиков, их разбора и подготовки к публикации. Он включает в себя функциональность для извлечения данных, их обработки с использованием моделей искусственного интеллекта и интеграции с Facebook для публикации рекламных объявлений.

## Подробней

Основная задача модуля — автоматизировать процесс создания рекламных материалов на основе данных, полученных от поставщиков. Он использует веб-драйверы для извлечения информации с сайтов, AI-модели для генерации контента и API Facebook для публикации. Модуль предназначен для работы в конвейере обработки данных и требует настройки конфигурационных файлов и учетных данных.

## Классы

### `QuotationBuilder`

**Описание**: Класс `QuotationBuilder` обрабатывает извлечение, разбор и сохранение данных о продуктах от поставщиков.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `QuotationBuilder`.
- `convert_product_fields`: Преобразует поля продукта в формат, подходящий для AI-модели.
- `process_ai`: Обрабатывает список продуктов с использованием AI-модели.
- `process_ai_async`: Асинхронно обрабатывает список продуктов с использованием AI-модели.
- `save_product_data`: Сохраняет данные продукта в файл.
- `post_facebook_async`: Исполняет сценарий рекламного модуля `facebook`.

**Параметры**:
- `base_path` (Path): Базовый путь к файлам модуля.
- `config` (SimpleNamespace): Конфигурация модуля, загружаемая из JSON.
- `html_path` (str | Path): Путь к HTML-файлу.
- `pdf_path` (str | Path): Путь к PDF-файлу.
- `docx_path` (str | Path): Путь к DOCX-файлу.
- `driver` (Driver): Экземпляр веб-драйвера.
- `export_path` (Path): Путь для экспорта данных.
- `mexiron_name` (str): Имя процесса обработки данных.
- `price` (float): Цена продукта.
- `timestamp` (str): Временная метка.
- `products_list` (List): Список обработанных данных о продуктах.
- `model` (GoogleGenerativeAI): Экземпляр AI-модели.
- `translations` (SimpleNamespace): Переводы, загружаемые из JSON.
- `required_fields` (tuple): Кортеж необходимых полей товара.

**Примеры**
```python
# Пример инициализации класса QuotationBuilder
quotation_builder = QuotationBuilder(mexiron_name='test_mexiron', driver='firefox')
```

## Функции

### `__init__`

```python
def __init__(self, mexiron_name:Optional[str] = gs.now, driver:Optional[Firefox | Playwrid | str] = None,  **kwards):
    """
    Args:
        driver (Driver): Selenium WebDriver instance.
        mexiron_name (Optional[str]): Custom name for the Mexiron process.
        webdriver_name (Optional[str]): Name of the WebDriver to use. Defaults to 'firefox'. call to Firefox or Playwrid
        window_mode (Optional[str]): Оконный режим вебдрайвера. Может быть 'maximized', 'headless', 'minimized', 'fullscreen', 'normal', 'hidden', 'kiosk'

    """
```

**Описание**: Инициализирует класс `QuotationBuilder` с требуемыми компонентами, такими как веб-драйвер и модель Gemini.

**Параметры**:
- `mexiron_name` (Optional[str]): Имя процесса Mexiron. По умолчанию `gs.now`.
- `driver` (Optional[Firefox | Playwrid | str]): Экземпляр веб-драйвера или его название. По умолчанию `None`.
- `**kwards`: Дополнительные аргументы для веб-драйвера.

**Примеры**:
```python
quotation = QuotationBuilder(mexiron_name='test', driver='firefox')
```

### `convert_product_fields`

```python
def convert_product_fields(self, f: ProductFields) -> dict:
    """
    Args:
        f (ProductFields): Object containing parsed product data.

    Returns:
        dict: Formatted product data dictionary.

    """
```

**Описание**: Преобразует поля продукта из объекта `ProductFields` в словарь для использования в AI-модели.

**Параметры**:
- `f` (ProductFields): Объект, содержащий распарсенные данные продукта.

**Возвращает**:
- `dict`: Словарь с отформатированными данными продукта.

**Примеры**:
```python
product_fields = ProductFields()
product_data = quotation.convert_product_fields(product_fields)
```

### `process_ai`

```python
def process_ai(self, products_list: List[str], lang:str,  attempts: int = 3) -> tuple | bool:
    """
    Args:
        products_list (str): List of product data dictionaries as a string.
        attempts (int, optional): Number of attempts to retry in case of failure. Defaults to 3.

    Returns:
        tuple: Processed response in `ru` and `he` formats.
        bool: False if unable to get a valid response after retries.

    """
```

**Описание**: Обрабатывает список продуктов с использованием AI-модели для генерации контента на указанном языке.

**Параметры**:
- `products_list` (List[str]): Список данных о продуктах в виде строки.
- `lang` (str): Язык, на котором требуется сгенерировать контент.
- `attempts` (int, optional): Количество попыток повторной обработки в случае неудачи. По умолчанию 3.

**Возвращает**:
- `dict`: Обработанный ответ от AI-модели.
- `bool`: `False`, если не удалось получить валидный ответ после нескольких попыток.

**Примеры**:
```python
products = ['{"product_name": "Example Product"}']
response = quotation.process_ai(products, 'ru')
```

### `process_ai_async`

```python
async def process_ai_async(self, products_list: List[str], lang:str,  attempts: int = 3) -> tuple | bool:
    """
    Args:
        products_list (str): List of product data dictionaries as a string.
        attempts (int, optional): Number of attempts to retry in case of failure. Defaults to 3.

    Returns:
        tuple: Processed response in `ru` and `he` formats.
        bool: False if unable to get a valid response after retries.

    """
```

**Описание**: Асинхронно обрабатывает список продуктов с использованием AI-модели для генерации контента на указанном языке.

**Параметры**:
- `products_list` (List[str]): Список данных о продуктах в виде строки.
- `lang` (str): Язык, на котором требуется сгенерировать контент.
- `attempts` (int, optional): Количество попыток повторной обработки в случае неудачи. По умолчанию 3.

**Возвращает**:
- `dict`: Обработанный ответ от AI-модели.
- `bool`: `False`, если не удалось получить валидный ответ после нескольких попыток.

**Примеры**:
```python
products = ['{"product_name": "Example Product"}']
response = await quotation.process_ai_async(products, 'ru')
```

### `save_product_data`

```python
async def save_product_data(self, product_data: dict) -> bool:
    """
    Args:
        product_data (dict): Formatted product data.
    """
```

**Описание**: Сохраняет данные продукта в файл в формате JSON.

**Параметры**:
- `product_data` (dict): Словарь с данными продукта.

**Примеры**:
```python
product_data = {"product_id": "123", "product_name": "Example Product"}
await quotation.save_product_data(product_data)
```

### `post_facebook_async`

```python
async def post_facebook_async(self, mexiron:SimpleNamespace) -> bool:
    """Функция исполняет сценарий рекламного модуля `facvebook`."""
```

**Описание**: Выполняет сценарий публикации рекламного объявления в Facebook.

**Параметры**:
- `mexiron` (SimpleNamespace): Объект с данными для публикации в Facebook.

**Примеры**:
```python
mexiron_data = SimpleNamespace(title='Title', description='Description', price=100, products=['image1.jpg'])
await quotation.post_facebook_async(mexiron_data)
```

### `main`

```python
def main():
    """"""
    ...
```

**Описание**: Основная функция для запуска процесса создания отчетов.

**Примеры**:
```python
main()