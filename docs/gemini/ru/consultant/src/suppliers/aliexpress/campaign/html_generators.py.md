# Анализ кода модуля `html_generators`

**Качество кода**
7
- Плюсы
    - Код хорошо структурирован и разбит на классы, каждый из которых отвечает за генерацию HTML для определенного уровня (продукт, категория, кампания).
    - Используются f-строки для формирования HTML, что делает код более читаемым и удобным в сопровождении.
    - Присутствует экранирование HTML-спецсимволов, что помогает избежать проблем с отображением и XSS-атак.
    - Код использует `pathlib` для работы с путями, что является хорошей практикой.
- Минусы
    - Отсутствует описание модуля в начале файла.
    - Нет документации в формате RST для классов и методов.
    - В коде используется `save_text_file` без обработки возможных исключений.
    - В HTML коде используется абсолютный путь до `styles.css`, что может вызвать проблемы.
    - Отсутствует импорт `logger` из `src.logger.logger`.

**Рекомендации по улучшению**

1.  Добавить описание модуля в начале файла.
2.  Добавить документацию в формате RST для классов и методов.
3.  Импортировать `logger` из `src.logger.logger`.
4.  Обработать исключения при сохранении файлов через `try-except` и логировать ошибки через `logger.error`.
5.  Заменить абсолютный путь до `styles.css` на относительный.
6.  Для большей гибкости можно рассмотреть вынесение HTML шаблонов в отдельные файлы.
7.  Убедиться, что все необходимые импорты присутствуют, а неиспользуемые удалены.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для генерации HTML контента рекламной кампании.
=========================================================================================

Этот модуль содержит классы для генерации HTML-страниц для отдельных продуктов, категорий продуктов и
целых рекламных кампаний. Используется для создания статических HTML-страниц на основе данных о товарах.

Пример использования
--------------------

Пример использования классов `ProductHTMLGenerator`, `CategoryHTMLGenerator`, `CampaignHTMLGenerator`:

.. code-block:: python

    from pathlib import Path
    from types import SimpleNamespace
    
    product_data = SimpleNamespace(
        product_id='12345',
        product_title='Sample Product',
        local_image_path='images/product.jpg',
        target_sale_price=100.00,
        target_sale_price_currency='$',
        target_original_price=120.00,
        target_original_price_currency='$',
        second_level_category_name='Electronics',
        promotion_link='http://example.com/product'
    )
    
    category_path = Path('./test_category')
    
    ProductHTMLGenerator.set_product_html(product_data, category_path)
    CategoryHTMLGenerator.set_category_html([product_data], category_path)
    CampaignHTMLGenerator.set_campaign_html(['test_category'], './test_campaign')
"""

import html
from pathlib import Path
from types import SimpleNamespace
# from src.utils.file import save_text_file  # Исправлено в соответствии с инструкцией
from src.logger.logger import logger
from src.utils.file import save_text_file # Исправлен импорт

class ProductHTMLGenerator:
    """
    Класс для генерации HTML для отдельных продуктов.
    
    Используется для создания HTML-страниц с описанием и ссылкой на покупку одного товара.
    """
    @staticmethod
    def set_product_html(product: SimpleNamespace, category_path: str | Path) -> None:
        """
        Создает HTML-файл для отдельного продукта.

        Args:
            product (SimpleNamespace): Детали продукта для включения в HTML.
            category_path (str | Path): Путь для сохранения HTML-файла.
        """
        #  Определение имени категории
        category_name = Path(category_path).name
        #  Формирование пути к HTML файлу
        html_path = Path(category_path) / 'html' / f'{product.product_id}.html'
        
        #  Формирование HTML контента
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
        #  Сохранение HTML контента в файл
        try:
            save_text_file(html_path, html_content)
        except Exception as e:
            logger.error(f'Ошибка при сохранении HTML файла продукта: {html_path}', exc_info=True)
            # raise  # Можно раскомментировать для проброса исключения дальше, если это необходимо

class CategoryHTMLGenerator:
    """
    Класс для генерации HTML для категорий продуктов.

    Создает HTML-страницу, содержащую список товаров в данной категории.
    """

    @staticmethod
    def set_category_html(products_list: list[SimpleNamespace] | SimpleNamespace, category_path: str | Path) -> None:
        """
        Создает HTML-файл для категории продуктов.

        Args:
            products_list (list[SimpleNamespace] | SimpleNamespace): Список продуктов для включения в HTML.
            category_path (str | Path): Путь для сохранения HTML-файла.
        """
        #  Преобразование в список, если передан один продукт
        products_list = products_list if isinstance(products_list, list) else [products_list]
        #  Определение имени категории
        category_name = Path(category_path).name
        #  Формирование пути к HTML файлу
        html_path = Path(category_path) / 'html' / 'index.html'
        #  Формирование HTML контента
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
        
        #  Добавление HTML для каждого продукта
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
        #  Сохранение HTML контента в файл
        try:
            save_text_file(html_path, html_content)
        except Exception as e:
            logger.error(f'Ошибка при сохранении HTML файла категории: {html_path}', exc_info=True)
            # raise  # Можно раскомментировать для проброса исключения дальше, если это необходимо


class CampaignHTMLGenerator:
    """
    Класс для генерации HTML для рекламной кампании.

    Создает HTML-страницу, содержащую список категорий товаров, участвующих в кампании.
    """

    @staticmethod
    def set_campaign_html(categories: list[str], campaign_path: str | Path) -> None:
        """
        Создает HTML-файл для рекламной кампании, перечисляя все категории.

        Args:
            categories (list[str]): Список имен категорий.
            campaign_path (str | Path): Путь для сохранения HTML-файла.
        """
        #  Формирование пути к HTML файлу
        html_path = Path(campaign_path) / 'index.html'
        #  Формирование HTML контента
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
        #  Добавление HTML для каждой категории
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
        #  Сохранение HTML контента в файл
        try:
            save_text_file(html_path, html_content)
        except Exception as e:
            logger.error(f'Ошибка при сохранении HTML файла кампании: {html_path}', exc_info=True)
            # raise  # Можно раскомментировать для проброса исключения дальше, если это необходимо