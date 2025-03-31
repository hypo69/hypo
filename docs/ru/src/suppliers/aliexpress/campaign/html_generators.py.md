# Модуль `html_generators.py`

## Обзор

Модуль `html_generators.py` предназначен для генерации HTML-страниц для рекламной кампании AliExpress. Он содержит классы, которые позволяют создавать HTML-страницы как для отдельных продуктов, так и для категорий продуктов и общей страницы кампании.

## Подробней

Этот модуль предоставляет функциональность для автоматического создания HTML-страниц на основе данных о продуктах и категориях, полученных из AliExpress. Он использует классы `ProductHTMLGenerator`, `CategoryHTMLGenerator` и `CampaignHTMLGenerator` для создания соответствующих HTML-файлов, которые могут быть использованы для отображения информации о продуктах и категориях в удобном для пользователя формате. Модуль использует `save_text_file` из `src.utils.file` для сохранения сгенерированного HTML контента в файлы.

## Классы

### `ProductHTMLGenerator`

**Описание**: Класс для генерации HTML-страниц для отдельных продуктов.

**Как работает класс**:
Класс `ProductHTMLGenerator` содержит статический метод `set_product_html`, который создает HTML-файл для отдельного продукта. Он принимает объект `product` (типа `SimpleNamespace`, содержащий информацию о продукте) и путь к категории (`category_path`). Метод генерирует HTML-код, включающий название продукта, изображение, цену, категорию и ссылку для покупки. Сгенерированный HTML-код сохраняется в файл с именем `product_id.html` в подкаталоге `html` внутри каталога категории.

**Методы**:
- `set_product_html`: Создает HTML-файл для отдельного продукта.

### `CategoryHTMLGenerator`

**Описание**: Класс для генерации HTML-страниц для категорий продуктов.

**Как работает класс**:
Класс `CategoryHTMLGenerator` содержит статический метод `set_category_html`, который создает HTML-файл для категории продуктов. Он принимает список объектов `product` (типа `SimpleNamespace`, содержащий информацию о продукте) и путь к категории (`category_path`). Метод генерирует HTML-код, включающий список продуктов с их названиями, изображениями, ценами, категориями и ссылками для покупки. Сгенерированный HTML-код сохраняется в файл `index.html` в подкаталоге `html` внутри каталога категории.

**Методы**:
- `set_category_html`: Создает HTML-файл для категории продуктов.

### `CampaignHTMLGenerator`

**Описание**: Класс для генерации HTML-страницы для общей страницы кампании.

**Как работает класс**:
Класс `CampaignHTMLGenerator` содержит статический метод `set_campaign_html`, который создает HTML-файл для общей страницы кампании. Он принимает список категорий (`categories`) и путь к кампании (`campaign_path`). Метод генерирует HTML-код, включающий список ссылок на HTML-страницы категорий. Сгенерированный HTML-код сохраняется в файл `index.html` в каталоге кампании.

**Методы**:
- `set_campaign_html`: Создает HTML-файл для общей страницы кампании.

## Функции

### `ProductHTMLGenerator.set_product_html`

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

**Как работает функция**:
Метод `set_product_html` генерирует HTML-страницу для заданного продукта. Он извлекает детали продукта, такие как название, изображение, цена и категория, из объекта `product`. Затем он формирует HTML-код, который включает эти детали, и сохраняет его в файл с именем `product_id.html` в подкаталоге `html` внутри каталога категории. HTML включает стили Bootstrap и пользовательский CSS.

**Параметры**:
- `product` (SimpleNamespace): Объект, содержащий информацию о продукте (название, изображение, цена, категория, ссылка для покупки).
- `category_path` (str | Path): Путь к каталогу категории, в котором будет сохранен HTML-файл.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Вызывает исключения**:
- Отсутствуют явные исключения.

**Примеры**:
```python
from types import SimpleNamespace
from pathlib import Path

# Пример использования
product = SimpleNamespace(
    product_id='12345',
    product_title='Example Product',
    local_image_path='images/example.jpg',
    target_sale_price='10.00',
    target_sale_price_currency='USD',
    target_original_price='15.00',
    target_original_price_currency='USD',
    second_level_category_name='Example Category',
    promotion_link='https://example.com/product/12345'
)
category_path = 'campaign/category1'

ProductHTMLGenerator.set_product_html(product, category_path)
# Будет создан файл campaign/category1/html/12345.html с HTML-кодом продукта
```

### `CategoryHTMLGenerator.set_category_html`

```python
@staticmethod
def set_category_html(products_list: list[SimpleNamespace] | SimpleNamespace, category_path: str | Path):
    """ Creates an HTML file for the category.
    
    @param products_list: List of products to include in the HTML.
    @param category_path: Path to save the HTML file.
    """
    ...
```

**Описание**: Создает HTML-файл для категории продуктов.

**Как работает функция**:
Метод `set_category_html` генерирует HTML-страницу для заданной категории продуктов. Он принимает список объектов `product` (или один объект `product`), содержащих информацию о продуктах, и путь к каталогу категории. Метод формирует HTML-код, который включает список продуктов с их деталями, и сохраняет его в файл `index.html` в подкаталоге `html` внутри каталога категории. HTML включает стили Bootstrap и пользовательский CSS.

**Параметры**:
- `products_list` (list[SimpleNamespace] | SimpleNamespace): Список объектов, содержащих информацию о продуктах (название, изображение, цена, категория, ссылка для покупки).
- `category_path` (str | Path): Путь к каталогу категории, в котором будет сохранен HTML-файл.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Вызывает исключения**:
- Отсутствуют явные исключения.

**Примеры**:
```python
from types import SimpleNamespace
from pathlib import Path

# Пример использования
products = [
    SimpleNamespace(
        product_id='12345',
        product_title='Example Product 1',
        local_image_path='images/example1.jpg',
        target_sale_price='10.00',
        target_sale_price_currency='USD',
        target_original_price='15.00',
        target_original_price_currency='USD',
        second_level_category_name='Example Category',
        promotion_link='https://example.com/product/12345'
    ),
    SimpleNamespace(
        product_id='67890',
        product_title='Example Product 2',
        local_image_path='images/example2.jpg',
        target_sale_price='20.00',
        target_sale_price_currency='USD',
        target_original_price='25.00',
        target_original_price_currency='USD',
        second_level_category_name='Example Category',
        promotion_link='https://example.com/product/67890'
    )
]
category_path = 'campaign/category1'

CategoryHTMLGenerator.set_category_html(products, category_path)
# Будет создан файл campaign/category1/html/index.html с HTML-кодом категории продуктов
```

### `CampaignHTMLGenerator.set_campaign_html`

```python
@staticmethod
def set_campaign_html(categories: list[str], campaign_path: str | Path):
    """ Creates an HTML file for the campaign, listing all categories.
    
    @param categories: List of category names.
    @param campaign_path: Path to save the HTML file.
    """
    ...
```

**Описание**: Создает HTML-файл для общей страницы кампании, перечисляющий все категории.

**Как работает функция**:
Метод `set_campaign_html` генерирует HTML-страницу для общей страницы кампании. Он принимает список категорий (`categories`) и путь к каталогу кампании. Метод формирует HTML-код, который включает список ссылок на HTML-страницы категорий, и сохраняет его в файл `index.html` в каталоге кампании. HTML включает стили Bootstrap и пользовательский CSS.

**Параметры**:
- `categories` (list[str]): Список названий категорий.
- `campaign_path` (str | Path): Путь к каталогу кампании, в котором будет сохранен HTML-файл.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Вызывает исключения**:
- Отсутствуют явные исключения.

**Примеры**:
```python
from pathlib import Path

# Пример использования
categories = ['category1', 'category2', 'category3']
campaign_path = 'campaign'

CampaignHTMLGenerator.set_campaign_html(categories, campaign_path)
# Будет создан файл campaign/index.html с HTML-кодом общей страницы кампании