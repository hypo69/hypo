# Модуль: Генераторы HTML контента рекламной кампании

## Обзор

Модуль `html_generators.py` предназначен для генерации HTML-контента, необходимого для отображения рекламных кампаний, категорий продуктов и отдельных продуктов. Он содержит классы, которые создают HTML-файлы для каждой из этих сущностей, используя предоставленные данные о продуктах и категориях.

## Подробней

Этот модуль играет важную роль в создании интерактивных веб-страниц для рекламных кампаний. Он использует данные о продуктах, такие как название, цена, изображение и категория, чтобы сгенерировать HTML-код. Этот код затем сохраняется в виде HTML-файлов, которые могут быть развернуты на веб-сервере для отображения рекламной кампании.

## Классы

### `ProductHTMLGenerator`

**Описание**: Класс для генерации HTML-кода для отдельного продукта.

**Принцип работы**:
Класс `ProductHTMLGenerator` предоставляет статический метод `set_product_html`, который принимает информацию о продукте и путь к категории, а затем создает HTML-файл с подробной информацией об этом продукте. В HTML включается название продукта, изображение, цена, категория и ссылка для покупки.

**Методы**:
- `set_product_html(product: SimpleNamespace, category_path: str | Path)`: Создает HTML-файл для отдельного продукта.

**Параметры**:
- `product` (SimpleNamespace): Объект, содержащий детали продукта (название, описание, цена, изображение, URL и т. д.).
- `category_path` (str | Path): Путь к каталогу, в котором следует сохранить HTML-файл продукта.

**Примеры**:
Пример использования класса для создания HTML-страницы продукта:

```python
from pathlib import Path
from types import SimpleNamespace

# Создание объекта SimpleNamespace с данными о продукте
product_data = SimpleNamespace(
    product_id="12345",
    product_title="Супер Товар",
    local_image_path="images/super_tovar.jpg",
    target_sale_price="1999",
    target_sale_price_currency="руб.",
    target_original_price="2499",
    target_original_price_currency="руб.",
    second_level_category_name="Электроника",
    promotion_link="https://example.com/super_tovar"
)

# Определение пути к категории
category_path = "campaign/category1"

# Создание HTML-страницы продукта
ProductHTMLGenerator.set_product_html(product_data, category_path)
```

### `CategoryHTMLGenerator`

**Описание**: Класс для генерации HTML-кода для страницы категории продуктов.

**Принцип работы**:
Класс `CategoryHTMLGenerator` предоставляет статический метод `set_category_html`, который генерирует HTML-страницу, содержащую список продуктов в заданной категории. Он принимает список объектов, представляющих продукты, и путь к категории, где будет сохранен HTML-файл.

**Методы**:
- `set_category_html(products_list: list[SimpleNamespace] | SimpleNamespace, category_path: str | Path)`: Создает HTML-файл для категории продуктов.

**Параметры**:
- `products_list` (list[SimpleNamespace] | SimpleNamespace): Список объектов, содержащих информацию о продуктах в категории.
- `category_path` (str | Path): Путь к каталогу, в котором следует сохранить HTML-файл категории.

**Примеры**:
Пример использования класса для создания HTML-страницы категории продуктов:

```python
from pathlib import Path
from types import SimpleNamespace

# Создание списка объектов SimpleNamespace с данными о продуктах
products_data = [
    SimpleNamespace(
        product_title="Товар 1",
        local_image_path="images/tovar1.jpg",
        target_sale_price="999",
        target_sale_price_currency="руб.",
        target_original_price="1299",
        target_original_price_currency="руб.",
        second_level_category_name="Электроника",
        promotion_link="https://example.com/tovar1"
    ),
    SimpleNamespace(
        product_title="Товар 2",
        local_image_path="images/tovar2.jpg",
        target_sale_price="1499",
        target_sale_price_currency="руб.",
        target_original_price="1799",
        target_original_price_currency="руб.",
        second_level_category_name="Электроника",
        promotion_link="https://example.com/tovar2"
    )
]

# Определение пути к категории
category_path = "campaign/category1"

# Создание HTML-страницы категории продуктов
CategoryHTMLGenerator.set_category_html(products_data, category_path)
```

### `CampaignHTMLGenerator`

**Описание**: Класс для генерации HTML-кода для главной страницы кампании, содержащей список категорий.

**Принцип работы**:
Класс `CampaignHTMLGenerator` предоставляет статический метод `set_campaign_html`, который создает HTML-файл для главной страницы кампании, перечисляя все категории, доступные в кампании. Он принимает список названий категорий и путь к каталогу кампании, где будет сохранен HTML-файл.

**Методы**:
- `set_campaign_html(categories: list[str], campaign_path: str | Path)`: Создает HTML-файл для главной страницы кампании.

**Параметры**:
- `categories` (list[str]): Список названий категорий для включения в HTML-страницу кампании.
- `campaign_path` (str | Path): Путь к каталогу, в котором следует сохранить HTML-файл кампании.

**Примеры**:
Пример использования класса для создания HTML-страницы кампании:

```python
from pathlib import Path

# Создание списка категорий
categories = ["category1", "category2", "category3"]

# Определение пути к кампании
campaign_path = "campaign"

# Создание HTML-страницы кампании
CampaignHTMLGenerator.set_campaign_html(categories, campaign_path)
```

## Функции

В данном модуле нет отдельных функций, только статические методы внутри классов.