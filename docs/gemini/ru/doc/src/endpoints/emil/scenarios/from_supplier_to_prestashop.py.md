# Модуль: from_supplier_to_prestashop

## Обзор

Модуль `from_supplier_to_prestashop` предназначен для автоматизации процесса извлечения, обработки и публикации данных о товарах от различных поставщиков в интернет-магазин на платформе Prestashop. Он включает в себя функциональность для парсинга данных с сайтов поставщиков, использования AI для обработки информации о товарах, сохранения данных в формате, совместимом с Prestashop, и публикации товаров в магазине.

## Подробней

Этот модуль является частью проекта `hypotez` и служит для упрощения и автоматизации процесса обновления каталога товаров в Prestashop. Он позволяет извлекать информацию о товарах непосредственно с сайтов поставщиков или из JSON файлов, обрабатывать эту информацию с использованием AI (например, для генерации описаний товаров) и публиковать товары в Prestashop. Модуль также включает функциональность для работы с изображениями товаров, создания отчетов и интеграции с рекламными платформами, такими как Facebook.

## Классы

### `SupplierToPrestashopProvider`

**Описание**: Класс `SupplierToPrestashopProvider` предоставляет методы для извлечения, обработки и сохранения данных о продуктах поставщиков. Он использует Selenium WebDriver для парсинга сайтов, AI модель Gemini для обработки текста и API Prestashop для публикации товаров.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `SupplierToPrestashopProvider`.
- `initialise_ai_model`: Инициализирует AI модель Gemini с системными инструкциями.
- `run_scenario`: Запускает основной сценарий обработки товаров: парсинг, обработка AI и сохранение данных.
- `save_product_data`: Сохраняет данные отдельного товара в файл JSON.
- `process_ai`: Обрабатывает список товаров с использованием AI модели.
- `read_data_from_json`: Загружает данные из JSON файлов.
- `save_in_prestashop`: Сохраняет товары в Prestashop.
- `post_facebook`: Исполняет сценарий рекламного модуля `facebook`.
- `create_report`: Создает отчет о мехироне в форматах `html` и `pdf`.

**Параметры**:
- `lang` (str): Язык, на котором будет происходить обработка данных.
- `gemini_api` (str): API ключ для доступа к модели Gemini.
- `presta_api` (str): API ключ для доступа к Prestashop.
- `presta_url` (str): URL адрес Prestashop.
- `driver` (Optional[Driver], optional): Экземпляр Selenium WebDriver. По умолчанию `None`.

**Примеры**:

```python
# Пример инициализации класса SupplierToPrestashopProvider
from src.webdriver.driver import Driver
from src.webdriver.firefox import Firefox
from src.endpoints.emil.scenarios.from_supplier_to_prestashop import SupplierToPrestashopProvider

driver = Driver(Firefox)
supplier_to_presta = SupplierToPrestashopProvider(
    lang='ru',
    gemini_api='YOUR_GEMINI_API_KEY',
    presta_api='YOUR_PRESTA_API_KEY',
    presta_url='YOUR_PRESTA_URL',
    driver=driver
)
```

## Функции

### `initialise_ai_model`

```python
def initialise_ai_model(self):
    """Инициализация модели Gemini"""
```

**Описание**: Инициализирует и возвращает модель Google Gemini с заданными системными инструкциями.

**Параметры**:
- Нет явных параметров, использует атрибуты экземпляра класса.

**Возвращает**:
- `GoogleGenerativeAI`: Инициализированная модель Google Gemini.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при загрузке инструкций.

**Примеры**:

```python
# Пример вызова метода initialise_ai_model
model = supplier_to_presta.initialise_ai_model()
```

### `run_scenario`

```python
async def run_scenario(
    self, 
    urls: list[str],\
    price: Optional[str] = \'\', 
    mexiron_name: Optional[str] = \'\', 
) -> bool:
    """
    Executes the scenario: parses products, processes them via AI, and stores data.
    Args:
        urls (list[str]): Product page URLs.
        price (Optional[str]): Price to process.
        mexiron_name (Optional[str]): Custom Mexiron name.
    Returns:
        bool: True if the scenario executes successfully, False otherwise.
    """
```

**Описание**: Запускает сценарий обработки товаров: парсит товары с заданных URL, обрабатывает их с помощью AI и сохраняет полученные данные.

**Параметры**:
- `urls` (list[str]): Список URL-адресов страниц товаров.
- `price` (Optional[str], optional): Цена товара. По умолчанию ''.
- `mexiron_name` (Optional[str], optional): Пользовательское имя мехирона. По умолчанию ''.

**Возвращает**:
- `bool`: `True`, если сценарий выполнен успешно, `False` в противном случае.

**Примеры**:

```python
# Пример вызова метода run_scenario
urls = ['https://example.com/product1', 'https://example.com/product2']
result = await supplier_to_presta.run_scenario(urls=urls, price='100', mexiron_name='Мехирон 1')
```

### `save_product_data`

```python
async def save_product_data(self, product_data: dict):
    """
    Saves individual product data to a file.
    Args:
        product_data (dict): Formatted product data.
    """
```

**Описание**: Сохраняет данные отдельного товара в файл JSON.

**Параметры**:
- `product_data` (dict): Словарь с данными о товаре.

**Возвращает**:
- `bool`: `True`, если данные успешно сохранены, `None` в противном случае.

**Примеры**:

```python
# Пример вызова метода save_product_data
product_data = {'product_id': '123', 'name': 'Товар 1', 'description': 'Описание товара 1'}
result = await supplier_to_presta.save_product_data(product_data=product_data)
```

### `process_ai`

```python
async def process_ai(self, products_list: List[str], lang:str,  attempts: int = 3) -> tuple | bool:
    """
    Processes the product list through the AI model.
    Args:
        products_list (str): List of product data dictionaries as a string.
        attempts (int, optional): Number of attempts to retry in case of failure. Defaults to 3.
    Returns:
        tuple: Processed response in `ru` and `he` formats.
        bool: False if unable to get a valid response after retries.
    """
```

**Описание**: Обрабатывает список товаров с использованием AI модели для получения дополнительной информации или модификации существующих данных.

**Параметры**:
- `products_list` (List[str]): Список данных о товарах в виде строки.
- `lang` (str): Язык, на котором будет производиться обработка.
- `attempts` (int, optional): Количество попыток повторной обработки в случае неудачи. По умолчанию 3.

**Возвращает**:
- `dict`: Обработанный ответ от AI модели.
- `bool`: `False`, если не удалось получить валидный ответ после всех попыток.

**Примеры**:

```python
# Пример вызова метода process_ai
products_list = [{'product_id': '123', 'name': 'Товар 1', 'description': 'Описание товара 1'}]
result = await supplier_to_presta.process_ai(products_list=products_list, lang='ru')
```

### `read_data_from_json`

```python
async def read_data_from_json(self):
    """Загружаю JSON файлы и фотки, которые я сделал через телеграм"""
```

**Описание**: Загружает данные из JSON файлов, полученных через телеграм.

**Параметры**:
- Нет явных параметров, использует атрибуты экземпляра класса.

**Возвращает**:
- None

**Примеры**:

```python
# Пример вызова метода read_data_from_json
await supplier_to_presta.read_data_from_json()
```

### `save_in_prestashop`

```python
async def save_in_prestashop(self, products_list:ProductFields | list[ProductFields]) -> bool:
    """Функция, которая сохраняет товары в Prestashop emil-design.com """
```

**Описание**: Сохраняет товары в Prestashop.

**Параметры**:
- `products_list` (ProductFields | list[ProductFields]): Список товаров для сохранения.

**Возвращает**:
- `bool`: `True`, если товары успешно сохранены, `False` в противном случае.

**Примеры**:

```python
# Пример вызова метода save_in_prestashop
from src.endpoints.prestashop.product_fields import ProductFields
products_list = [ProductFields(...), ProductFields(...)]  # Замените ... на реальные данные
result = await supplier_to_presta.save_in_prestashop(products_list=products_list)
```

### `post_facebook`

```python
async def post_facebook(self, mexiron:SimpleNamespace) -> bool:
    """Функция исполняет сценарий рекламного модуля `facvebook`."""
```

**Описание**: Публикует информацию о товаре в Facebook.

**Параметры**:
- `mexiron` (SimpleNamespace): Объект с данными о товаре.

**Возвращает**:
- `bool`: `True`, если публикация прошла успешно, `False` в противном случае.

**Примеры**:

```python
# Пример вызова метода post_facebook
from types import SimpleNamespace
mexiron = SimpleNamespace(title='Мехирон 1', description='Описание мехирона 1', price='100', products=['image1.jpg', 'image2.jpg'])
result = await supplier_to_presta.post_facebook(mexiron=mexiron)
```

### `create_report`

```python
async def create_report(self, data: dict, lang:str, html_file: Path, pdf_file: Path) -> bool:
    """Функция отправляет задание на создание мехирона в формате `html` и `pdf`.
    Если мехорон в pdf создался (`generator.create_report()` вернул True) - 
    отправить его боту
    """
```

**Описание**: Создает отчет о мехироне в форматах `html` и `pdf` и отправляет PDF-файл боту.

**Параметры**:
- `data` (dict): Данные для отчета.
- `lang` (str): Язык отчета.
- `html_file` (Path): Путь для сохранения HTML-файла.
- `pdf_file` (Path): Путь для сохранения PDF-файла.

**Возвращает**:
- `bool`: `True`, если отчет успешно создан и отправлен, `False` в противном случае.

**Примеры**:

```python
# Пример вызова метода create_report
from pathlib import Path
data = {'title': 'Мехирон 1', 'description': 'Описание мехирона 1', 'price': '100'}
html_file = Path('report.html')
pdf_file = Path('report.pdf')
result = await supplier_to_presta.create_report(data=data, lang='ru', html_file=html_file, pdf_file=pdf_file)
```

### `main`

```python
async def main(suppier_to_presta):
    """На данный момент функция читает JSON со списком фотографий , которые были получены от Эмиля"""
```

**Описание**: Основная функция, которая считывает JSON-файл со списком фотографий, полученных от Эмиля, и сохраняет товары в Prestashop.

**Параметры**:
- `suppier_to_presta` (SupplierToPrestashopProvider): Экземпляр класса `SupplierToPrestashopProvider`.

**Возвращает**:
- None

**Примеры**:

```python
# Пример вызова функции main
import asyncio
from src.endpoints.emil.scenarios.from_supplier_to_prestashop import SupplierToPrestashopProvider

async def main():
    lang = 'he'
    suppier_to_presta = SupplierToPrestashopProvider(lang=lang, gemini_api='YOUR_GEMINI_API_KEY', presta_api='YOUR_PRESTA_API_KEY', presta_url='YOUR_PRESTA_URL')
    # products_ns = j_loads_ns(gs.path.external_storage / ENDPOINT / 'out_250108230345305_he.json')
    # products_list: list = [f for f in products_ns]
    # await suppier_to_presta.save_in_prestashop(products_list)

if __name__ == '__main__':
    asyncio.run(main())