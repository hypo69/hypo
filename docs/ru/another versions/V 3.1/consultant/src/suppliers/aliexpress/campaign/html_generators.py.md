## Анализ кода модуля `html_generators`

**Качество кода:**

- **Соответствие стандартам**: 6/10
- **Плюсы**:
  - Код достаточно хорошо структурирован и разбит на классы, каждый из которых отвечает за генерацию HTML для определенного уровня (товар, категория, кампания).
  - Использование `html.escape` для предотвращения XSS-атак.
  - Четкое разделение ответственности между классами.
- **Минусы**:
  - Отсутствует подробная документация классов и методов.
  - Не используются f-строки для формирования HTML-контента, что снижает читаемость.
  - Дублирование кода при создании HTML-структуры (например, подключение CSS и JS).
  - Жестко заданные пути к CSS и JS файлам (использование CDN).
  - Не обрабатываются возможные исключения при записи файлов.
  - Не используется логирование.

**Рекомендации по улучшению:**

1.  **Добавить подробную документацию**:

    -   Добавить docstrings для всех классов и методов, описывающие их назначение, параметры и возвращаемые значения.
    -   Оформить документацию в соответствии со стандартом, указанным в инструкции.

2.  **Использовать f-строки**:

    -   Использовать f-строки для более читаемого и эффективного формирования HTML-контента.

3.  **Удалить дублирование кода**:

    -   Вынести общие части HTML-структуры (например, подключение CSS и JS) в отдельные переменные или функции.
    -   Использовать шаблонизатор (например, Jinja2) для генерации HTML-контента, чтобы избежать дублирования кода и упростить его поддержку.

4.  **Обработка ошибок**:

    -   Добавить обработку исключений при записи файлов.
    -   Использовать логирование для записи информации об ошибках и предупреждениях.

5.  **Пути к файлам**:

    -   Сделать пути к CSS и JS файлам относительными, чтобы можно было использовать локальные файлы.
    -   Предоставить возможность настройки путей к файлам через параметры.

6.  **Типизация**:
    -  Во всех методах и функциях должны быть указаны типы.

**Оптимизированный код:**

```python
## \file /src/suppliers/aliexpress/campaign/html_generators.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers.aliexpress.campaign
    :platform: Windows, Unix
    :synopsis: Генератор HTML контента рекламной кампании

"""

import html
from pathlib import Path
from types import SimpleNamespace
from typing import List, Optional
from src.utils.file import save_text_file
from src.logger import logger


class ProductHTMLGenerator:
    """Генератор HTML для отдельных товаров."""

    @staticmethod
    def set_product_html(product: SimpleNamespace, category_path: str | Path) -> None:
        """Создает HTML-файл для отдельного товара.

        Args:
            product (SimpleNamespace): Детали продукта для включения в HTML.
            category_path (str | Path): Путь для сохранения HTML-файла.

        Returns:
            None
        """
        try:
            category_name: str = Path(category_path).name
            html_path: Path = Path(category_path) / 'html' / f'{product.product_id}.html'

            html_content: str = f"""<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>{html.escape(product.product_title)}</title>
    <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css'>
    <link rel='stylesheet' href='styles.css'> <!-- Link to custom CSS file -->
</head>
<body>
    <div class='container'>
        <h1 class='my-4'>{html.escape(product.product_title)}</h1>
        <div class='card'>
            <img src='{Path(product.local_image_path).as_posix()}' alt='{html.escape(product.product_title)}' class='card-img-top'>
            <div class='card-body'>
                <p class='card-text'>Price: <span class='product-price'>{product.target_sale_price} {product.target_sale_price_currency}</span></p>
                <p class='card-text'>Original Price: <span class='product-original-price'>{product.target_original_price} {product.target_original_price_currency}</span></p>
                <p class='card-text'>Category: <span class='product-category'>{html.escape(product.second_level_category_name)}</span></p>
                <a href='{product.promotion_link}' class='btn btn-primary'>Buy Now</a>
            </div>
        </div>
    </div>

    <script src='https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.bundle.min.js'></script>
</body>
</html>
"""
            save_text_file(html_content, html_path)
        except Exception as ex:
            logger.error('Error while setting product HTML', ex, exc_info=True)


class CategoryHTMLGenerator:
    """Генератор HTML для категорий товаров."""

    @staticmethod
    def set_category_html(products_list: list[SimpleNamespace] | SimpleNamespace, category_path: str | Path) -> None:
        """Создает HTML-файл для категории.

        Args:
            products_list (list[SimpleNamespace] | SimpleNamespace): Список товаров для включения в HTML.
            category_path (str | Path): Путь для сохранения HTML-файла.

        Returns:
            None
        """
        try:
            products_list: list[SimpleNamespace] = products_list if isinstance(products_list, list) else [products_list]

            category_name: str = Path(category_path).name
            html_path: Path = Path(category_path) / 'html' / 'index.html'

            html_content: str = f"""<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>{html.escape(category_name)} Products</title>
    <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css'>
    <link rel='stylesheet' href='styles.css'> <!-- Link to custom CSS file -->
</head>
<body>
    <div class='container'>
        <h1 class='my-4'>{html.escape(category_name)} Products</h1>
        <div class='row product-grid'>
    """

            for product in products_list:
                image_url: str = Path(product.local_image_path).as_posix()
                html_content += f"""
                <div class='col-md-4 mb-4'>
                    <div class='card'>
                        <img src='{image_url}' alt='{html.escape(product.product_title)}' class='card-img-top'>
                        <div class='card-body'>
                            <h5 class='card-title'>{html.escape(product.product_title)}</h5>
                            <p class='card-text'>Price: <span class='product-price'>{product.target_sale_price} {product.target_sale_price_currency}</span></p>
                            <p class='card-text'>Original Price: <span class='product-original-price'>{product.target_original_price} {product.target_original_price_currency}</span></p>
                            <p class='card-text'>Category: <span class='product-category'>{html.escape(product.second_level_category_name)}</span></p>
                            <a href='{product.promotion_link}' class='btn btn-primary'>Buy Now</a>
                        </div>
                    </div>
                </div>
            """

            html_content += """
        </div>
    </div>

    <script src='https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.bundle.min.js'></script>
</body>
</html>
"""
            save_text_file(html_content, html_path)
        except Exception as ex:
            logger.error('Error while setting category HTML', ex, exc_info=True)


class CampaignHTMLGenerator:
    """Генератор HTML для кампании."""

    @staticmethod
    def set_campaign_html(categories: list[str], campaign_path: str | Path) -> None:
        """Создает HTML-файл для кампании, перечисляющий все категории.

        Args:
            categories (list[str]): Список названий категорий.
            campaign_path (str | Path): Путь для сохранения HTML-файла.

        Returns:
            None
        """
        try:
            html_path: Path = Path(campaign_path) / 'index.html'

            html_content: str = f"""<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Campaign Overview</title>
    <link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css'>
    <link rel='stylesheet' href='styles.css'> <!-- Link to custom CSS file -->
</head>
<body>
    <div class='container'>
        <h1 class='my-4'>Campaign Overview</h1>
        <ul class='list-group'>
    """

            for category in categories:
                html_content += f"""
                <li class='list-group-item'>
                    <a href='{category}/index.html'>{html.escape(category)}</a>
                </li>
            """

            html_content += """
        </ul>
    </div>

    <script src='https://stackpath.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.bundle.min.js'></script>
</body>
</html>
"""
            save_text_file(html_content, html_path)
        except Exception as ex:
            logger.error('Error while setting campaign HTML', ex, exc_info=True)
```