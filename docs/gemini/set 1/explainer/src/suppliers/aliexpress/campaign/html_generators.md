# <input code>

```python
## \file hypotez/src/suppliers/aliexpress/campaign/html_generators.py
# -*- coding: utf-8 -*-\

#! venv/bin/python/python3.12

"""
.. module:: src.suppliers.aliexpress.campaign 
	:platform: Windows, Unix
	:synopsis: Генератор HTML контента рекламной кампании

"""


import header   
from pathlib import Path
from types import SimpleNamespace
from src.utils.file import save_text_file
import html

class ProductHTMLGenerator:
    """ Class for generating HTML for individual products."""

    @staticmethod
    def set_product_html(product: SimpleNamespace, category_path: str | Path):
        """ Creates an HTML file for an individual product.

        @param product: The product details to include in the HTML.
        @param category_path: The path to save the HTML file.
        """
        category_name = Path(category_path).name
        html_path = Path(category_path) / 'html' / f"{product.product_id}.html"

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(product.product_title)}</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="styles.css"> <!-- Link to custom CSS file -->
</head>
<body>
    <div class="container">
        <h1 class="my-4">{html.escape(product.product_title)}</h1>
        <div class="card">
            <img src="{Path(product.local_image_path).as_posix()}" alt="{html.escape(product.product_title)}" class="card-img-top">
            <div class="card-body">
                <p class="card-text">Price: <span class="product-price">{product.target_sale_price} {product.target_sale_price_currency}</span></p>
                <p class="card-text">Original Price: <span class="product-original-price">{product.target_original_price} {product.target_original_price_currency}</span></p>
                <p class="card-text">Category: <span class="product-category">{html.escape(product.second_level_category_name)}</span></p>
                <a href="{product.promotion_link}" class="btn btn-primary">Buy Now</a>
            </div>
        </div>
    </div>

    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""
        save_text_file(html_content, html_path)


class CategoryHTMLGenerator:
    """ Class for generating HTML for product categories."""

    @staticmethod
    def set_category_html(products_list: list[SimpleNamespace] | SimpleNamespace, category_path: str | Path):
        """ Creates an HTML file for the category.

        @param products_list: List of products to include in the HTML.
        @param category_path: Path to save the HTML file.
        """
        products_list = products_list if isinstance(products_list, list) else [products_list]

        category_name = Path(category_path).name
        html_path = Path(category_path) / 'html' / 'index.html'

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(category_name)} Products</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="styles.css"> <!-- Link to custom CSS file -->
</head>
<body>
    <div class="container">
        <h1 class="my-4">{html.escape(category_name)} Products</h1>
        <div class="row product-grid">
    """

        for product in products_list:
            image_url = Path(product.local_image_path).as_posix()
            html_content += f"""
                <div class="col-md-4 mb-4">
                    <div class="card">
                        <img src="{image_url}" alt="{html.escape(product.product_title)}" class="card-img-top">
                        <div class="card-body">
                            <h5 class="card-title">{html.escape(product.product_title)}</h5>
                            <p class="card-text">Price: <span class="product-price">{product.target_sale_price} {product.target_sale_price_currency}</span></p>
                            <p class="card-text">Original Price: <span class="product-original-price">{product.target_original_price} {product.target_original_price_currency}</span></p>
                            <p class="card-text">Category: <span class="product-category">{html.escape(product.second_level_category_name)}</span></p>
                            <a href="{product.promotion_link}" class="btn btn-primary">Buy Now</a>
                        </div>
                    </div>
                </div>
            """

        html_content += """ 
        </div>
    </div>

    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""
        save_text_file(html_content, html_path)


class CampaignHTMLGenerator:
    """ Class for generating HTML for a campaign."""

    @staticmethod
    def set_campaign_html(categories: list[str], campaign_path: str | Path):
        """ Creates an HTML file for the campaign, listing all categories.

        @param categories: List of category names.
        @param campaign_path: Path to save the HTML file.
        """
        html_path = Path(campaign_path) / 'index.html'

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Campaign Overview</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="styles.css"> <!-- Link to custom CSS file -->
</head>
<body>
    <div class="container">
        <h1 class="my-4">Campaign Overview</h1>
        <ul class="list-group">
    """

        for category in categories:
            html_content += f"""
                <li class="list-group-item">
                    <a href="{category}/index.html">{html.escape(category)}</a>
                </li>
            """

        html_content += """ 
        </ul>
    </div>

    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""
        save_text_file(html_content, html_path)
```

# <algorithm>

```mermaid
graph TD
    A[Input: categories, campaign_path] --> B{CampaignHTMLGenerator.set_campaign_html};
    B --> C[Create html_content with links to category];
    C --> D{save_text_file(html_content, html_path)};
    
    E[Input: products_list, category_path] --> F{CategoryHTMLGenerator.set_category_html};
    F --> G[Create html_content with product list];
    G --> H{save_text_file(html_content, html_path)};
    
    I[Input: product, category_path] --> J{ProductHTMLGenerator.set_product_html};
    J --> K[Create html_content for single product];
    K --> L{save_text_file(html_content, html_path)};
```

**Пример:**  Пусть `categories = ['Electronics', 'Clothing']`, `campaign_path = 'campaigns/winter_sale'`. Функция `CampaignHTMLGenerator.set_campaign_html` создаст HTML-файл `campaigns/winter_sale/index.html` со ссылками на `Electronics/index.html` и `Clothing/index.html`.

**Пример (Category):**  Пусть `products_list = [product1, product2, product3]`, `category_path = 'campaigns/winter_sale/Electronics'`. Функция `CategoryHTMLGenerator.set_category_html` создаст `campaigns/winter_sale/Electronics/html/index.html` с  HTML-разметкой, содержащей информацию о каждом продукте из `products_list`.

# <mermaid>

```mermaid
graph LR
    subgraph Импорты
        A[header] --> B(src.suppliers.aliexpress.campaign);
        C[pathlib] --> B;
        D[types] --> B;
        E[src.utils.file] --> B;
        F[html] --> B;
    end

    subgraph Классы
        B1[ProductHTMLGenerator] --> B2(set_product_html);
        B3[CategoryHTMLGenerator] --> B4(set_category_html);
        B5[CampaignHTMLGenerator] --> B6(set_campaign_html);
    end
    
    subgraph Функции
        B2 --> C1[save_text_file];
        B4 --> C1;
        B6 --> C1;
    end

    subgraph Взаимосвязи
        B(src.suppliers.aliexpress.campaign) -- генерация HTML -- B1;
        B(src.suppliers.aliexpress.campaign) -- генерация HTML -- B3;
        B(src.suppliers.aliexpress.campaign) -- генерация HTML -- B5;
        C1 -- запись в файл -- B1;
        C1 -- запись в файл -- B3;
        C1 -- запись в файл -- B5;
        B5 --> B3;
        B5 --> B1;
    end
```

# <explanation>

**Импорты:**

* `header`:  Непонятно, что это, без контекста проекта.  Нужно посмотреть, что импортируется из `header`. Возможно, это вспомогательные функции или константы.
* `pathlib`: Предоставляет классы для работы с путями к файлам (Path).
* `types`: Предоставляет базовые типы данных, в частности `SimpleNamespace`.
* `src.utils.file`: Вероятно, содержит функции для работы с файлами, вероятно, для сохранения текста.
* `html`: Предоставляет функции для работы с HTML-экранированием.

**Классы:**

* `ProductHTMLGenerator`: Создаёт HTML-страницы для отдельных продуктов.
    * `set_product_html`: Создаёт HTML-код для одного продукта и сохраняет его в файл.  Принимает `product` (объект типа `SimpleNamespace`) и `category_path`.  Обратите внимание на использование `html.escape()`. Это важно для безопасности, чтобы предотвратить XSS-атаки.
* `CategoryHTMLGenerator`: Создаёт HTML-страницы для категорий продуктов.
    * `set_category_html`: Создаёт HTML-код для всей категории продуктов и сохраняет его в файл.  Принимает список продуктов (`products_list`) и `category_path`.  Важный момент - обработка списка и единственного элемента `products_list`.
* `CampaignHTMLGenerator`:  Создаёт HTML-страницы для рекламной кампании.
    * `set_campaign_html`: Создаёт HTML-код для обзора всей кампании (список категорий) и сохраняет его в файл. Принимает список категорий (`categories`) и `campaign_path`.

**Функции:**

* `save_text_file`: Вероятно, сохраняет текст в файл.  Из кода понятно, что она принимает путь к файлу и содержимое для сохранения.  Её реализация находится в `src.utils.file`.

**Переменные:**

* `MODE`: Контекстная переменная, определяющая режим работы (в данном случае `dev`).
* `html_path`: Путь к сохраняемому HTML-файлу.
* `html_content`: Содержимое генерируемого HTML-файла, строка.

**Возможные ошибки или области для улучшений:**

* **Обработка исключений:**  При работе с файлами рекомендуется использовать обработку исключений (например, `try...except FileNotFoundError`).
* **Логирование:** Добавление логирования могло бы улучшить отладку и мониторинг процесса.
* **Переиспользование компонентов:**  Есть избыточное использование Bootstrap в каждом файле.  Можно вынести стили в отдельный файл (styles.css) и импортировать его.
* **Использование шаблонизатора:** Рассмотреть возможность использования шаблонизатора (например, Jinja2), чтобы сделать генерацию HTML более гибкой и читаемой.
* **Поддержка других шаблонов:**  Можно добавить возможность работы с другими шаблонами (например, вместо bootstrap), или параметров стилей.

**Цепочка взаимосвязей:**

Код генерации HTML для кампании ( `CampaignHTMLGenerator`)  вызывает код генерации HTML для категорий (`CategoryHTMLGenerator`), а код генерации HTML для категорий вызывает код генерации HTML для отдельных продуктов (`ProductHTMLGenerator`).


**Подробное объяснение диаграммы:**

Диаграмма иллюстрирует, как различные компоненты кода взаимодействуют друг с другом.


```