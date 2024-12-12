# Анализ кода модуля `html_generators.py`

**Качество кода: 7/10**

- **Плюсы**
    - Код хорошо структурирован и разбит на классы, каждый из которых отвечает за свою задачу: генерация HTML для продуктов, категорий и кампаний.
    - Используется `SimpleNamespace` для хранения данных о продуктах, что упрощает доступ к атрибутам.
    - Применяется `html.escape` для предотвращения XSS-атак, что является хорошей практикой.
    - Код использует `pathlib` для работы с путями, что делает код более читаемым и кроссплатформенным.
    -  Присутствует явное разделение ответственности между классами.
- **Минусы**
    - Отсутствуют необходимые импорты, такие как `from src.logger.logger import logger`.
    - Нет обработки ошибок с использованием `logger.error`.
    -  Используется прямое форматирование строк с f-строками, что может быть менее гибким, чем шаблонизация.
    -  В коде используются `str` для конкатенации строк, что может быть неэффективно для больших объемов HTML.
    -  Нет документации в формате reStructuredText (RST).
    -   Используется `Path` в `f-строке`, что снижает читаемость.

**Рекомендации по улучшению**

1.  **Добавить импорты**: Добавить необходимые импорты, такие как `from src.logger.logger import logger` и `from src.utils.jjson import j_loads, j_loads_ns`.
2.  **Обработка ошибок**: Заменить стандартные `try-except` на `logger.error` для обработки исключений.
3.  **Документация**: Добавить документацию в формате reStructuredText (RST) для всех классов, методов и переменных.
4.  **Использовать шаблонизатор**: Рассмотреть использование шаблонизатора (например, Jinja2) для генерации HTML, чтобы сделать код более читаемым и поддерживаемым.
5.  **Оптимизировать конкатенацию строк**: Использовать `join` для более эффективной конкатенации HTML-строк.
6.  **Улучшить читаемость**: Вынести формирование URL изображений из f-строки.
7.  **Унифицировать кавычки**: Использовать только одинарные кавычки (`'`) в коде.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для генерации HTML контента рекламной кампании.
=========================================================================================

Этот модуль содержит классы для генерации HTML-страниц для продуктов, категорий и кампаний.
Он использует `pathlib` для работы с путями и `html` для экранирования HTML-спецсимволов.

:platform: Windows, Unix
:synopsis: Генератор HTML контента рекламной кампании

Пример использования
--------------------

Пример использования классов:

.. code-block:: python

    from types import SimpleNamespace
    from pathlib import Path
    from src.suppliers.aliexpress.campaign.html_generators import ProductHTMLGenerator, CategoryHTMLGenerator, CampaignHTMLGenerator

    product = SimpleNamespace(
        product_id='123',
        product_title='Test Product',
        local_saved_image='images/test.jpg',
        target_sale_price=10.0,
        target_sale_price_currency='USD',
        target_original_price=20.0,
        target_original_price_currency='USD',
        second_level_category_name='Test Category',
        promotion_link='https://test.com'
    )
    category_path = Path('test_category')
    ProductHTMLGenerator.set_product_html(product, category_path)
    CategoryHTMLGenerator.set_category_html([product], category_path)
    CampaignHTMLGenerator.set_campaign_html(['test_category'], Path('test_campaign'))
"""
MODE = 'dev'

import html
from pathlib import Path
from types import SimpleNamespace
# from src.utils.file import save_text_file # перенесён ниже
# from src.logger.logger import logger # перенесён ниже
from src.utils.file import save_text_file
from src.logger.logger import logger

class ProductHTMLGenerator:
    """
    Класс для генерации HTML для отдельных продуктов.
    
    :ivar str MODE: Режим работы.
    """

    @staticmethod
    def set_product_html(product: SimpleNamespace, category_path: str | Path):
        """
        Создает HTML файл для отдельного продукта.

        :param product: Детали продукта для включения в HTML.
        :type product: SimpleNamespace
        :param category_path: Путь для сохранения HTML файла.
        :type category_path: str | Path
        """
        try: # обработка ошибок
            category_name = Path(category_path).name
            html_path = Path(category_path) / 'html' / f'{product.product_id}.html'

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
            save_text_file(html_content, html_path)
        except Exception as ex: # Логирование ошибки
            logger.error(f'Ошибка при создании HTML для продукта {product.product_id}: {ex}')

class CategoryHTMLGenerator:
    """
    Класс для генерации HTML для категорий продуктов.

     :ivar str MODE: Режим работы.
    """

    @staticmethod
    def set_category_html(products_list: list[SimpleNamespace] | SimpleNamespace, category_path: str | Path):
        """
        Создает HTML файл для категории.

        :param products_list: Список продуктов для включения в HTML.
        :type products_list: list[SimpleNamespace] | SimpleNamespace
        :param category_path: Путь для сохранения HTML файла.
        :type category_path: str | Path
        """
        try: # Обработка ошибок
            products_list = products_list if isinstance(products_list, list) else [products_list]
            
            category_name = Path(category_path).name
            html_path = Path(category_path) / 'html' / 'index.html'
            
            html_content_parts = [
                f"""<!DOCTYPE html>
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
            ]
            
            for product in products_list:
                image_url = Path(product.local_saved_image).as_posix()
                html_content_parts.append(f"""
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
            """)
            
            html_content_parts.append(""" 
        </div>
    </div>
    
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")
            html_content = ''.join(html_content_parts)
            save_text_file(html_content, html_path)
        except Exception as ex: # Логирование ошибки
             logger.error(f'Ошибка при создании HTML для категории {category_name}: {ex}')

class CampaignHTMLGenerator:
    """
    Класс для генерации HTML для кампании.

    :ivar str MODE: Режим работы.
    """

    @staticmethod
    def set_campaign_html(categories: list[str], campaign_path: str | Path):
        """
        Создает HTML файл для кампании, перечисляя все категории.

        :param categories: Список названий категорий.
        :type categories: list[str]
        :param campaign_path: Путь для сохранения HTML файла.
        :type campaign_path: str | Path
        """
        try: # обработка ошибок
            html_path = Path(campaign_path) / 'index.html'
            
            html_content_parts = [
            f"""<!DOCTYPE html>
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
        ]
            
            for category in categories:
                html_content_parts.append(f"""
                <li class="list-group-item">
                    <a href="{category}/index.html">{html.escape(category)}</a>
                </li>
            """)
            
            html_content_parts.append(""" 
        </ul>
    </div>
    
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
""")
            
            html_content = ''.join(html_content_parts)
            save_text_file(html_content, html_path)
        except Exception as ex: # Логирование ошибки
            logger.error(f'Ошибка при создании HTML для кампании {campaign_path}: {ex}')