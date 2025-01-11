### Анализ кода модуля `html_generators`

**Качество кода**:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код разбит на классы, каждый из которых отвечает за генерацию HTML для определённого уровня (продукты, категории, кампания).
    - Используется f-строки для форматирования HTML, что делает код более читаемым.
    - Присутствует экранирование HTML-спецсимволов.
- **Минусы**:
    - Отсутствует rst-документация для классов и методов.
    - Не используется `from src.logger.logger import logger` для логирования.
    - Присутствуют магические строки типа `https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css`, которые желательно вынести в константы.
    - Не проводится проверка ошибок при записи в файл.
    - Используются двойные кавычки в HTML контенте, что не соответствует гайдлайну.

**Рекомендации по улучшению**:

- Добавить rst-документацию для классов и методов, чтобы сделать код более понятным.
- Добавить импорт `from src.logger.logger import logger` и использовать его для логирования ошибок.
- Вынести магические строки в константы для упрощения поддержки и изменения.
- Добавить обработку ошибок при записи файлов, с использованием `logger.error`.
- Переписать HTML контент с использованием одинарных кавычек.
- Привести импорты в порядок.
- Выровнять названия функций, переменных и импортов.

**Оптимизированный код**:

```python
# -*- coding: utf-8 -*-

"""
.. module:: src.suppliers.aliexpress.campaign.html_generators
    :platform: Windows, Unix
    :synopsis: Генератор HTML контента рекламной кампании
"""

import html
from pathlib import Path
from types import SimpleNamespace

from src.utils.file import save_text_file
from src.logger.logger import logger # Используем logger из src.logger

BOOTSTRAP_CSS_URL = 'https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css'
BOOTSTRAP_JS_URL = 'https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.bundle.min.js'
CUSTOM_CSS_URL = 'styles.css'

class ProductHTMLGenerator:
    """
    Класс для генерации HTML для отдельных продуктов.
    =================================================

    Этот класс предоставляет статический метод для создания HTML-файлов для каждого продукта.
    """
    @staticmethod
    def set_product_html(product: SimpleNamespace, category_path: str | Path) -> None:
        """
        Создает HTML файл для отдельного продукта.

        :param product: Детали продукта для включения в HTML.
        :type product: SimpleNamespace
        :param category_path: Путь для сохранения HTML файла.
        :type category_path: str | Path
        :raises Exception: В случае ошибки при записи в файл.

        Пример:
            >>> product = SimpleNamespace(product_id=123, product_title='Test Product', local_image_path='img.png', target_sale_price=10, target_sale_price_currency='$', target_original_price=20, target_original_price_currency='$', second_level_category_name='Test Category', promotion_link='test.com')
            >>> category_path = 'test_category'
            >>> ProductHTMLGenerator.set_product_html(product, category_path)
        """
        category_name = Path(category_path).name
        html_path = Path(category_path) / 'html' / f'{product.product_id}.html'

        html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(product.product_title)}</title>
    <link rel="stylesheet" href="{BOOTSTRAP_CSS_URL}">
    <link rel="stylesheet" href="{CUSTOM_CSS_URL}"> <!-- Link to custom CSS file -->
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
    
    <script src="{BOOTSTRAP_JS_URL}"></script>
</body>
</html>
'''
        try:
            save_text_file(html_content, html_path)
        except Exception as e:
            logger.error(f'Error creating product HTML file: {e}') # Логируем ошибку

class CategoryHTMLGenerator:
    """
    Класс для генерации HTML для категорий продуктов.
    ==================================================

    Этот класс предоставляет статический метод для создания HTML-файлов для списка продуктов в пределах категории.
    """
    @staticmethod
    def set_category_html(products_list: list[SimpleNamespace] | SimpleNamespace, category_path: str | Path) -> None:
        """
        Создает HTML файл для категории.

        :param products_list: Список продуктов для включения в HTML.
        :type products_list: list[SimpleNamespace] | SimpleNamespace
        :param category_path: Путь для сохранения HTML файла.
        :type category_path: str | Path
        :raises Exception: В случае ошибки при записи в файл.

        Пример:
            >>> products_list = [SimpleNamespace(product_title='Test Product 1', local_image_path='img1.png', target_sale_price=10, target_sale_price_currency='$', target_original_price=20, target_original_price_currency='$', second_level_category_name='Test Category', promotion_link='test1.com'), SimpleNamespace(product_title='Test Product 2', local_image_path='img2.png', target_sale_price=15, target_sale_price_currency='$', target_original_price=25, target_original_price_currency='$', second_level_category_name='Test Category', promotion_link='test2.com')]
            >>> category_path = 'test_category'
            >>> CategoryHTMLGenerator.set_category_html(products_list, category_path)
        """
        products_list = products_list if isinstance(products_list, list) else [products_list]

        category_name = Path(category_path).name
        html_path = Path(category_path) / 'html' / 'index.html'

        html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{html.escape(category_name)} Products</title>
    <link rel="stylesheet" href="{BOOTSTRAP_CSS_URL}">
    <link rel="stylesheet" href="{CUSTOM_CSS_URL}"> <!-- Link to custom CSS file -->
</head>
<body>
    <div class="container">
        <h1 class="my-4">{html.escape(category_name)} Products</h1>
        <div class="row product-grid">
    '''

        for product in products_list:
            image_url = Path(product.local_image_path).as_posix()
            html_content += f'''
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
            '''

        html_content += f'''
        </div>
    </div>
    
    <script src="{BOOTSTRAP_JS_URL}"></script>
</body>
</html>
'''
        try:
            save_text_file(html_content, html_path)
        except Exception as e:
            logger.error(f'Error creating category HTML file: {e}') # Логируем ошибку

class CampaignHTMLGenerator:
    """
    Класс для генерации HTML для кампании.
    =====================================

    Этот класс предоставляет статический метод для создания HTML-файла для кампании,
    отображающего список всех категорий.
    """
    @staticmethod
    def set_campaign_html(categories: list[str], campaign_path: str | Path) -> None:
        """
        Создает HTML файл для кампании, перечисляющий все категории.

        :param categories: Список названий категорий.
        :type categories: list[str]
        :param campaign_path: Путь для сохранения HTML файла.
        :type campaign_path: str | Path
         :raises Exception: В случае ошибки при записи в файл.

        Пример:
            >>> categories = ['category1', 'category2']
            >>> campaign_path = 'test_campaign'
            >>> CampaignHTMLGenerator.set_campaign_html(categories, campaign_path)
        """
        html_path = Path(campaign_path) / 'index.html'

        html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Campaign Overview</title>
    <link rel="stylesheet" href="{BOOTSTRAP_CSS_URL}">
    <link rel="stylesheet" href="{CUSTOM_CSS_URL}"> <!-- Link to custom CSS file -->
</head>
<body>
    <div class="container">
        <h1 class="my-4">Campaign Overview</h1>
        <ul class="list-group">
    '''

        for category in categories:
            html_content += f'''
                <li class="list-group-item">
                    <a href="{category}/index.html">{html.escape(category)}</a>
                </li>
            '''

        html_content += f'''
        </ul>
    </div>
    
    <script src="{BOOTSTRAP_JS_URL}"></script>
</body>
</html>
'''
        try:
            save_text_file(html_content, html_path)
        except Exception as e:
            logger.error(f'Error creating campaign HTML file: {e}') # Логируем ошибку