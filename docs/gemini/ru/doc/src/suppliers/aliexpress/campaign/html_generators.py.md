# Модуль для генерации HTML контента рекламной кампании

## Обзор

Модуль `html_generators.py` предназначен для создания HTML-страниц, отображающих информацию о товарах, категориях и рекламных кампаниях. Он содержит три класса: `ProductHTMLGenerator`, `CategoryHTMLGenerator` и `CampaignHTMLGenerator`, каждый из которых отвечает за генерацию HTML-контента определенного типа. Модуль использует библиотеку `html` для безопасного экранирования текста, а также модуль `pathlib` для работы с путями к файлам.

## Подробнее

Этот модуль является важной частью проекта `hypotez`, так как он позволяет автоматически создавать HTML-страницы для рекламных кампаний на AliExpress. Сгенерированные страницы отображают информацию о товарах, категориях и кампаниях, что упрощает навигацию и просмотр.

## Классы

### `ProductHTMLGenerator`

**Описание**: Класс для генерации HTML-страницы отдельного товара.

**Принцип работы**:
Класс `ProductHTMLGenerator` содержит один статический метод `set_product_html`, который генерирует HTML-код для страницы товара на основе предоставленных данных о товаре. HTML-код включает в себя заголовок страницы, изображение товара, цену, категорию и ссылку для покупки. Сгенерированный HTML-код сохраняется в файл с именем `product_id.html` в подкаталоге `html` каталога категории.

**Методы**:
- `set_product_html(product: SimpleNamespace, category_path: str | Path)`: Создает HTML-файл для отдельного товара.

**Параметры**:
- `product` (SimpleNamespace): Объект, содержащий информацию о товаре (название, изображение, цена, категория, ссылка на продвижение).
- `category_path` (str | Path): Путь к каталогу категории, в котором будет сохранен HTML-файл.

### `CategoryHTMLGenerator`

**Описание**: Класс для генерации HTML-страницы категории товаров.

**Принцип работы**:
Класс `CategoryHTMLGenerator` содержит один статический метод `set_category_html`, который генерирует HTML-код для страницы категории товаров. HTML-код включает в себя заголовок страницы, список товаров с изображениями, ценами, категориями и ссылками для покупки. Сгенерированный HTML-код сохраняется в файл `index.html` в подкаталоге `html` каталога категории.

**Методы**:
- `set_category_html(products_list: list[SimpleNamespace] | SimpleNamespace, category_path: str | Path)`: Создает HTML-файл для категории товаров.

**Параметры**:
- `products_list` (list[SimpleNamespace] | SimpleNamespace): Список объектов, содержащих информацию о товарах в категории.
- `category_path` (str | Path): Путь к каталогу категории, в котором будет сохранен HTML-файл.

### `CampaignHTMLGenerator`

**Описание**: Класс для генерации HTML-страницы кампании.

**Принцип работы**:
Класс `CampaignHTMLGenerator` содержит один статический метод `set_campaign_html`, который генерирует HTML-код для страницы кампании. HTML-код включает в себя заголовок страницы и список категорий, представленных в кампании, со ссылками на страницы категорий. Сгенерированный HTML-код сохраняется в файл `index.html` в каталоге кампании.

**Методы**:
- `set_campaign_html(categories: list[str], campaign_path: str | Path)`: Создает HTML-файл для кампании.

**Параметры**:
- `categories` (list[str]): Список названий категорий, представленных в кампании.
- `campaign_path` (str | Path): Путь к каталогу кампании, в котором будет сохранен HTML-файл.

## Функции

### `ProductHTMLGenerator.set_product_html`

```python
@staticmethod
def set_product_html(product: SimpleNamespace, category_path: str | Path):
    """ Создает HTML-файл для отдельного товара.

    Args:
        product (SimpleNamespace): Объект, содержащий информацию о товаре (название, изображение, цена, категория, ссылка на продвижение).
        category_path (str | Path): Путь к каталогу категории, в котором будет сохранен HTML-файл.
    """
    ...
```

**Назначение**: Создание HTML-файла для отдельного товара.

**Параметры**:
- `product` (SimpleNamespace): Объект `SimpleNamespace`, содержащий информацию о товаре, такую как название (`product.product_title`), путь к локальному изображению (`product.local_image_path`), целевая цена продажи (`product.target_sale_price`), валюта (`product.target_sale_price_currency`), оригинальная цена (`product.target_original_price`), валюта оригинальной цены (`product.target_original_price_currency`), название категории второго уровня (`product.second_level_category_name`) и ссылка на продвижение (`product.promotion_link`).
- `category_path` (str | Path): Путь к каталогу категории, где будет создан HTML-файл. Может быть представлен в виде строки или объекта `Path`.

**Возвращает**: Ничего. Функция сохраняет HTML-файл в указанном каталоге.

**Вызывает исключения**: Отсутствуют.

**Как работает функция**:

1.  **Извлечение имени категории**: Извлекает имя категории из пути `category_path` с использованием `Path(category_path).name`.
2.  **Определение пути к HTML-файлу**: Формирует путь к HTML-файлу, который будет создан, используя `Path(category_path) / 'html' / f"{product.product_id}.html"`. HTML-файл будет сохранен в подкаталоге `html` каталога категории и назван по `product_id` товара.
3.  **Формирование HTML-контента**: Формирует HTML-контент с использованием f-строк. HTML-контент включает в себя структуру HTML-документа, метаданные, подключение стилей Bootstrap и пользовательского CSS, а также информацию о продукте, такую как название, изображение, цена, категория и ссылка для покупки.
4.  **Сохранение HTML-контента в файл**: Сохраняет сгенерированный HTML-контент в файл по указанному пути с использованием функции `save_text_file(html_content, html_path)`.

**ASCII flowchart**:

```
    Получение имени категории из category_path
    │
    └── Создание пути к HTML-файлу (category_path / 'html' / product_id.html)
    │
    └── Формирование HTML-контента (шаблон с данными продукта)
    │
    └── Сохранение HTML-контента в файл (save_text_file)
```

**Примеры**:

```python
from types import SimpleNamespace
from pathlib import Path

# Пример данных о продукте
product_data = SimpleNamespace(
    product_id="12345",
    product_title="Example Product",
    local_image_path="images/example.jpg",
    target_sale_price="19.99",
    target_sale_price_currency="USD",
    target_original_price="29.99",
    target_original_price_currency="USD",
    second_level_category_name="Electronics",
    promotion_link="https://example.com/product/12345"
)

# Пример пути к категории
category_path = "campaign/category1"

# Вызов функции для создания HTML-файла продукта
ProductHTMLGenerator.set_product_html(product_data, category_path)
```

### `CategoryHTMLGenerator.set_category_html`

```python
@staticmethod
def set_category_html(products_list: list[SimpleNamespace] | SimpleNamespace, category_path: str | Path):
    """ Создает HTML-файл для категории товаров.

    Args:
        products_list (list[SimpleNamespace] | SimpleNamespace): Список объектов, содержащих информацию о товарах в категории.
        category_path (str | Path): Путь к каталогу категории, в котором будет сохранен HTML-файл.
    """
    ...
```

**Назначение**: Создание HTML-файла для страницы категории товаров.

**Параметры**:
- `products_list` (list[SimpleNamespace] | SimpleNamespace): Список объектов `SimpleNamespace`, содержащих информацию о товарах в категории. Каждый объект должен иметь атрибуты, такие как `product_title`, `local_image_path`, `target_sale_price`, `target_sale_price_currency`, `target_original_price`, `target_original_price_currency`, `second_level_category_name` и `promotion_link`. Если передан один объект `SimpleNamespace`, он будет преобразован в список.
- `category_path` (str | Path): Путь к каталогу категории, где будет создан HTML-файл. Может быть представлен в виде строки или объекта `Path`.

**Возвращает**: Ничего. Функция сохраняет HTML-файл в указанном каталоге.

**Вызывает исключения**: Отсутствуют.

**Как работает функция**:

1.  **Преобразование в список**: Преобразует `products_list` в список, если был передан один объект `SimpleNamespace`.
2.  **Извлечение имени категории**: Извлекает имя категории из пути `category_path` с использованием `Path(category_path).name`.
3.  **Определение пути к HTML-файлу**: Формирует путь к HTML-файлу, который будет создан, используя `Path(category_path) / 'html' / 'index.html'`. HTML-файл будет сохранен в подкаталоге `html` каталога категории и назван `index.html`.
4.  **Формирование HTML-контента**: Формирует HTML-контент с использованием f-строк. HTML-контент включает в себя структуру HTML-документа, метаданные, подключение стилей Bootstrap и пользовательского CSS, а также информацию о каждом продукте в списке, такую как название, изображение, цена, категория и ссылка для покупки.
5.  **Сохранение HTML-контента в файл**: Сохраняет сгенерированный HTML-контент в файл по указанному пути с использованием функции `save_text_file(html_content, html_path)`.

**ASCII flowchart**:

```
    Преобразование products_list в список (если необходимо)
    │
    └── Получение имени категории из category_path
    │
    └── Создание пути к HTML-файлу (category_path / 'html' / 'index.html')
    │
    └── Формирование HTML-контента (шаблон с данными продуктов)
    │
    └── Сохранение HTML-контента в файл (save_text_file)
```

**Примеры**:

```python
from types import SimpleNamespace
from pathlib import Path

# Пример данных о продуктах
product1_data = SimpleNamespace(
    product_title="Product 1",
    local_image_path="images/product1.jpg",
    target_sale_price="19.99",
    target_sale_price_currency="USD",
    target_original_price="29.99",
    target_original_price_currency="USD",
    second_level_category_name="Electronics",
    promotion_link="https://example.com/product/1"
)

product2_data = SimpleNamespace(
    product_title="Product 2",
    local_image_path="images/product2.jpg",
    target_sale_price="29.99",
    target_sale_price_currency="USD",
    target_original_price="39.99",
    target_original_price_currency="USD",
    second_level_category_name="Electronics",
    promotion_link="https://example.com/product/2"
)

products_list = [product1_data, product2_data]

# Пример пути к категории
category_path = "campaign/category1"

# Вызов функции для создания HTML-файла категории
CategoryHTMLGenerator.set_category_html(products_list, category_path)
```

### `CampaignHTMLGenerator.set_campaign_html`

```python
@staticmethod
def set_campaign_html(categories: list[str], campaign_path: str | Path):
    """ Создает HTML-файл для кампании, перечисляющий все категории.

    Args:
        categories (list[str]): Список названий категорий.
        campaign_path (str | Path): Путь для сохранения HTML-файла.
    """
    ...
```

**Назначение**: Создание HTML-файла для страницы кампании, содержащего список категорий.

**Параметры**:
- `categories` (list[str]): Список строк, представляющих названия категорий, которые будут отображены на странице кампании.
- `campaign_path` (str | Path): Путь к каталогу кампании, где будет сохранен HTML-файл. Может быть представлен в виде строки или объекта `Path`.

**Возвращает**: Ничего. Функция сохраняет HTML-файл в указанном каталоге.

**Вызывает исключения**: Отсутствуют.

**Как работает функция**:

1.  **Определение пути к HTML-файлу**: Формирует путь к HTML-файлу, который будет создан, используя `Path(campaign_path) / 'index.html'`. HTML-файл будет сохранен в каталоге кампании и назван `index.html`.
2.  **Формирование HTML-контента**: Формирует HTML-контент с использованием f-строк. HTML-контент включает в себя структуру HTML-документа, метаданные, подключение стилей Bootstrap и пользовательского CSS, а также список категорий, представленных в виде ссылок на страницы категорий.
3.  **Сохранение HTML-контента в файл**: Сохраняет сгенерированный HTML-контент в файл по указанному пути с использованием функции `save_text_file(html_content, html_path)`.

**ASCII flowchart**:

```
    Создание пути к HTML-файлу (campaign_path / 'index.html')
    │
    └── Формирование HTML-контента (шаблон со списком категорий)
    │
    └── Сохранение HTML-контента в файл (save_text_file)
```

**Примеры**:

```python
from pathlib import Path

# Пример списка категорий
categories_list = ["category1", "category2", "category3"]

# Пример пути к кампании
campaign_path = "campaign"

# Вызов функции для создания HTML-файла кампании
CampaignHTMLGenerator.set_campaign_html(categories_list, campaign_path)