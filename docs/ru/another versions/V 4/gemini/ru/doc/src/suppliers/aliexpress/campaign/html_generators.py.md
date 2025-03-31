# Модуль `html_generators.py`

## Обзор

Модуль `html_generators.py` предназначен для генерации HTML-контента для рекламных кампаний AliExpress. Он содержит классы для создания HTML-страниц как для отдельных продуктов, так и для категорий продуктов, а также для общей страницы кампании, содержащей список категорий. Модуль использует библиотеку `html` для безопасного экранирования строк и модуль `pathlib` для работы с путями файлов.

## Подробней

Этот модуль предоставляет три основных класса для генерации HTML: `ProductHTMLGenerator`, `CategoryHTMLGenerator` и `CampaignHTMLGenerator`.

- `ProductHTMLGenerator` создает HTML-страницу для отдельного продукта, отображая его изображение, цену, категорию и кнопку "Купить сейчас".
- `CategoryHTMLGenerator` создает HTML-страницу для категории продуктов, отображая список продуктов с их изображениями, ценами, категориями и кнопками "Купить сейчас".
- `CampaignHTMLGenerator` создает HTML-страницу для всей кампании, содержащую список ссылок на страницы категорий.

Эти классы используют статические методы для генерации HTML-контента и сохранения его в файлы.

## Классы

### `ProductHTMLGenerator`

**Описание**: Класс для генерации HTML для отдельных продуктов.

**Методы**:
- `set_product_html`: Создает HTML-файл для отдельного продукта.

#### `set_product_html`

```python
@staticmethod
def set_product_html(product: SimpleNamespace, category_path: str | Path):
    """
    Args:
        product (SimpleNamespace): Детали продукта, включаемые в HTML.
        category_path (str | Path): Путь для сохранения HTML-файла.
    """
```

**Описание**: Создает HTML-файл для отдельного продукта.

**Параметры**:
- `product` (SimpleNamespace): Детали продукта, включаемые в HTML.
- `category_path` (str | Path): Путь для сохранения HTML-файла.

**Примеры**:

```python
from pathlib import Path
from types import SimpleNamespace

product = SimpleNamespace(
    product_id='12345',
    product_title='Example Product',
    local_image_path='images/example.jpg',
    target_sale_price='100',
    target_sale_price_currency='USD',
    target_original_price='120',
    target_original_price_currency='USD',
    second_level_category_name='Example Category',
    promotion_link='https://example.com'
)
category_path = 'output/example_category'
Path(category_path + '/html').mkdir(parents=True, exist_ok=True)

ProductHTMLGenerator.set_product_html(product, category_path)
# Будет создан файл output/example_category/html/12345.html
```

### `CategoryHTMLGenerator`

**Описание**: Класс для генерации HTML для категорий продуктов.

**Методы**:
- `set_category_html`: Создает HTML-файл для категории.

#### `set_category_html`

```python
@staticmethod
def set_category_html(products_list: list[SimpleNamespace] | SimpleNamespace, category_path: str | Path):
    """
    Args:
        products_list (list[SimpleNamespace] | SimpleNamespace): Список продуктов, включаемых в HTML.
        category_path (str | Path): Путь для сохранения HTML-файла.
    """
```

**Описание**: Создает HTML-файл для категории.

**Параметры**:
- `products_list` (list[SimpleNamespace] | SimpleNamespace): Список продуктов, включаемых в HTML.
- `category_path` (str | Path): Путь для сохранения HTML-файла.

**Примеры**:

```python
from pathlib import Path
from types import SimpleNamespace

products_list = [
    SimpleNamespace(
        product_id='12345',
        product_title='Example Product 1',
        local_image_path='images/example1.jpg',
        target_sale_price='100',
        target_sale_price_currency='USD',
        target_original_price='120',
        target_original_price_currency='USD',
        second_level_category_name='Example Category',
        promotion_link='https://example.com/1'
    ),
    SimpleNamespace(
        product_id='67890',
        product_title='Example Product 2',
        local_image_path='images/example2.jpg',
        target_sale_price='200',
        target_sale_price_currency='USD',
        target_original_price='240',
        target_original_price_currency='USD',
        second_level_category_name='Example Category',
        promotion_link='https://example.com/2'
    )
]
category_path = 'output/example_category'
Path(category_path + '/html').mkdir(parents=True, exist_ok=True)

CategoryHTMLGenerator.set_category_html(products_list, category_path)
# Будет создан файл output/example_category/html/index.html
```

### `CampaignHTMLGenerator`

**Описание**: Класс для генерации HTML для кампании.

**Методы**:
- `set_campaign_html`: Создает HTML-файл для кампании, перечисляющий все категории.

#### `set_campaign_html`

```python
@staticmethod
def set_campaign_html(categories: list[str], campaign_path: str | Path):
    """
    Args:
        categories (list[str]): Список названий категорий.
        campaign_path (str | Path): Путь для сохранения HTML-файла.
    """
```

**Описание**: Создает HTML-файл для кампании, перечисляющий все категории.

**Параметры**:
- `categories` (list[str]): Список названий категорий.
- `campaign_path` (str | Path): Путь для сохранения HTML-файла.

**Примеры**:

```python
from pathlib import Path

categories = ['Category1', 'Category2', 'Category3']
campaign_path = 'output/example_campaign'
Path(campaign_path).mkdir(parents=True, exist_ok=True)

CampaignHTMLGenerator.set_campaign_html(categories, campaign_path)
# Будет создан файл output/example_campaign/index.html
```