# Модуль `html_generators`

## Обзор

Модуль `html_generators` предназначен для генерации HTML-контента для рекламной кампании AliExpress. Он содержит классы для создания HTML-страниц как для отдельных продуктов, так и для категорий продуктов и общей страницы кампании.

## Подробней

Этот модуль предоставляет функциональность для автоматического создания HTML-файлов, необходимых для представления продуктов и категорий продуктов в рамках рекламной кампании. Он использует данные о продуктах (такие как название, цена, изображение и категория) для генерации HTML-кода, который затем сохраняется в файлы. Это позволяет автоматизировать процесс создания веб-страниц для рекламной кампании, что особенно полезно при большом количестве продуктов и категорий.

## Классы

### `ProductHTMLGenerator`

**Описание**: Класс для генерации HTML для отдельных продуктов.

**Методы**:
- `set_product_html`: Создает HTML-файл для отдельного продукта.

#### `set_product_html`

```python
@staticmethod
def set_product_html(product: SimpleNamespace, category_path: str | Path):
    """ Creates an HTML file for an individual product.
    
    @param product: The product details to include in the HTML.
    @param category_path: The path to save the HTML file.
    """
    ...
```

**Описание**: Создает HTML-файл для отдельного продукта.

**Параметры**:
- `product` (SimpleNamespace): Детали продукта для включения в HTML.
- `category_path` (str | Path): Путь для сохранения HTML-файла.

**Пример**:

```python
from types import SimpleNamespace
from pathlib import Path

# Пример данных продукта
product_data = SimpleNamespace(
    product_id='12345',
    product_title='Example Product',
    local_image_path='images/example.jpg',
    target_sale_price='10.00',
    target_sale_price_currency='USD',
    target_original_price='15.00',
    target_original_price_currency='USD',
    second_level_category_name='Example Category',
    promotion_link='https://example.com'
)

# Пример пути категории
category_path = 'path/to/category'

# Создание HTML-файла продукта
ProductHTMLGenerator.set_product_html(product_data, category_path)
```

### `CategoryHTMLGenerator`

**Описание**: Класс для генерации HTML для категорий продуктов.

**Методы**:
- `set_category_html`: Создает HTML-файл для категории.

#### `set_category_html`

```python
@staticmethod
def set_category_html(products_list: list[SimpleNamespace] | SimpleNamespace, category_path: str | Path):
    """ Creates an HTML file for the category.
    
    @param products_list: List of products to include in the HTML.
    @param category_path: Path to save the HTML file.
    """
    ...
```

**Описание**: Создает HTML-файл для категории.

**Параметры**:
- `products_list` (list[SimpleNamespace] | SimpleNamespace): Список продуктов для включения в HTML.
- `category_path` (str | Path): Путь для сохранения HTML-файла.

**Пример**:

```python
from types import SimpleNamespace
from pathlib import Path

# Пример данных продукта
product_data1 = SimpleNamespace(
    product_id='12345',
    product_title='Example Product 1',
    local_image_path='images/example1.jpg',
    target_sale_price='10.00',
    target_sale_price_currency='USD',
    target_original_price='15.00',
    target_original_price_currency='USD',
    second_level_category_name='Example Category',
    promotion_link='https://example.com/1'
)

product_data2 = SimpleNamespace(
    product_id='67890',
    product_title='Example Product 2',
    local_image_path='images/example2.jpg',
    target_sale_price='20.00',
    target_sale_price_currency='USD',
    target_original_price='25.00',
    target_original_price_currency='USD',
    second_level_category_name='Example Category',
    promotion_link='https://example.com/2'
)

# Пример списка продуктов
products_list = [product_data1, product_data2]

# Пример пути категории
category_path = 'path/to/category'

# Создание HTML-файла категории
CategoryHTMLGenerator.set_category_html(products_list, category_path)
```

### `CampaignHTMLGenerator`

**Описание**: Класс для генерации HTML для кампании.

**Методы**:
- `set_campaign_html`: Создает HTML-файл для кампании, перечисляя все категории.

#### `set_campaign_html`

```python
@staticmethod
def set_campaign_html(categories: list[str], campaign_path: str | Path):
    """ Creates an HTML file for the campaign, listing all categories.
    
    @param categories: List of category names.
    @param campaign_path: Path to save the HTML file.
    """
    ...
```

**Описание**: Создает HTML-файл для кампании, перечисляя все категории.

**Параметры**:
- `categories` (list[str]): Список названий категорий.
- `campaign_path` (str | Path): Путь для сохранения HTML-файла.

**Пример**:

```python
from pathlib import Path

# Пример списка категорий
categories = ['Category1', 'Category2', 'Category3']

# Пример пути кампании
campaign_path = 'path/to/campaign'

# Создание HTML-файла кампании
CampaignHTMLGenerator.set_campaign_html(categories, campaign_path)
```