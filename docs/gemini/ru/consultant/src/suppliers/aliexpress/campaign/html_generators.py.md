# Анализ кода модуля `html_generators.py`

**Качество кода**
10
- Плюсы
    - Код хорошо структурирован и разбит на классы для генерации HTML, что соответствует принципам объектно-ориентированного программирования.
    - Используются статические методы, что уместно для генераторов HTML, так как они не зависят от состояния экземпляра класса.
    - Код читабельный, с понятными именами переменных и функций.
    - Применяется экранирование HTML-спецсимволов, что важно для предотвращения XSS-атак.
    - Используются f-строки для форматирования, что повышает читаемость и эффективность.
- Минусы
    - Отсутствуют docstring для модулей, классов и методов.
    - Не используется логирование, что затрудняет отладку и анализ ошибок.
    -  Не добавлен импорт `from src.logger.logger import logger`.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля, классов и методов в формате RST.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок и отладки.
3.  Удалить лишние shebang.
4.  Добавить проверку на существование директории перед созданием файлов.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для генерации HTML контента рекламной кампании.
======================================================

Этот модуль предоставляет классы для генерации HTML-страниц
для отдельных товаров, категорий товаров и всей рекламной кампании.

Классы:
    - ProductHTMLGenerator: Генерирует HTML для отдельных товаров.
    - CategoryHTMLGenerator: Генерирует HTML для категорий товаров.
    - CampaignHTMLGenerator: Генерирует HTML для всей кампании.

"""

import html
from pathlib import Path
from types import SimpleNamespace
# Добавлен импорт logger
from src.logger.logger import logger
# Добавлен импорт save_text_file
from src.utils.file import save_text_file

# Константа для режима работы
MODE = 'dev'

class ProductHTMLGenerator:
    """
    Класс для генерации HTML для отдельных товаров.
    """
    @staticmethod
    def set_product_html(product: SimpleNamespace, category_path: str | Path):
        """
        Создает HTML-файл для отдельного товара.

        :param product: Детали товара для включения в HTML.
        :type product: SimpleNamespace
        :param category_path: Путь для сохранения HTML-файла.
        :type category_path: str | Path
        """
        # получаем имя категории из пути
        category_name = Path(category_path).name
        # формируем путь к html файлу
        html_path = Path(category_path) / 'html' / f"{product.product_id}.html"

        # формируем html контент
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
            <img src="{Path(product.local_saved_image).as_posix()}" alt="{html.escape(product.product_title)}" class="card-img-top">
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
        # Код сохраняет HTML-контент в файл
        save_text_file(html_content, html_path)

class CategoryHTMLGenerator:
    """
    Класс для генерации HTML для категорий товаров.
    """
    @staticmethod
    def set_category_html(products_list: list[SimpleNamespace] | SimpleNamespace, category_path: str | Path):
        """
        Создает HTML-файл для категории товаров.

        :param products_list: Список товаров для включения в HTML.
        :type products_list: list[SimpleNamespace] | SimpleNamespace
        :param category_path: Путь для сохранения HTML-файла.
        :type category_path: str | Path
        """
        # Проверяем тип products_list и приводим к списку
        products_list = products_list if isinstance(products_list, list) else [products_list]
        # получаем имя категории из пути
        category_name = Path(category_path).name
        # формируем путь к html файлу
        html_path = Path(category_path) / 'html' / 'index.html'

        # формируем html контент
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
        # Цикл по всем продуктам в списке
        for product in products_list:
            # получаем путь к изображению продукта
            image_url = Path(product.local_saved_image).as_posix()
            # добавляем html разметку продукта в общий html контент
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
        # добавляем завершающие теги html
        html_content += """ 
        </div>
    </div>
    
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""
        # Код сохраняет HTML-контент в файл
        save_text_file(html_content, html_path)

class CampaignHTMLGenerator:
    """
    Класс для генерации HTML для всей кампании.
    """
    @staticmethod
    def set_campaign_html(categories: list[str], campaign_path: str | Path):
        """
        Создает HTML-файл для всей рекламной кампании, перечисляя все категории.

        :param categories: Список имен категорий.
        :type categories: list[str]
        :param campaign_path: Путь для сохранения HTML-файла.
        :type campaign_path: str | Path
        """
        # формируем путь к html файлу
        html_path = Path(campaign_path) / 'index.html'
        # формируем html контент
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
        # Цикл по всем категориям
        for category in categories:
            # добавляем html разметку категории в общий html контент
            html_content += f"""
                <li class="list-group-item">
                    <a href="{category}/index.html">{html.escape(category)}</a>
                </li>
            """
        # добавляем завершающие теги html
        html_content += """ 
        </ul>
    </div>
    
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""
        # Код сохраняет HTML-контент в файл
        save_text_file(html_content, html_path)