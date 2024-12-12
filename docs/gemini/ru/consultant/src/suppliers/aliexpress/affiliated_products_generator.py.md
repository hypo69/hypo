# Анализ кода модуля `affiliated_products_generator.py`

**Качество кода**
1.  **Соответствие требованиям по оформлению кода**: 7/10
    -   **Плюсы**:
        -   Код структурирован, используется асинхронность.
        -   Используется `logger` для логирования.
        -   Присутствуют docstring для методов и классов.
    -   **Минусы**:
        -   Не все комментарии соответствуют формату reStructuredText (RST).
        -   Не везде используется `logger.error` для обработки ошибок.
        -   Присутствует избыточное логирование.
        -   Не все функции и методы имеют подробные docstring.
        -   Использование `pprint` заменено на `logger.info`, но в коде остались закомментированные варианты.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Переписать все комментарии и docstring в формате RST.
    -   Добавить более подробные описания параметров и возвращаемых значений в docstring.
    -   Удалить закомментированный код.
2.  **Логирование**:
    -   Заменить общие `try-except` на обработку ошибок с помощью `logger.error`.
    -   Уменьшить избыточное логирование, оставив только важные сообщения.
3.  **Обработка данных**:
    -   Использовать `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load` (если используется)
4. **Импорты**:
    - Добавить недостающие импорты, если необходимо.
5.  **Рефакторинг**:
    -   Упростить логику обработки ошибок.
    -   Переименовать переменные для лучшей читаемости.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для генерации аффилированных продуктов AliExpress.
=========================================================================================

Этот модуль содержит класс :class:`AliAffiliatedProducts`, который используется для
сбора полных данных о продуктах по URL-адресам или идентификаторам продуктов.

Подробную информацию о создании шаблонов для рекламных кампаний см. в разделе
`Управление рекламными кампаниями AliExpress`.

Пример использования
--------------------

Пример использования класса `AliAffiliatedProducts`:

.. code-block:: python

    affiliated_products = AliAffiliatedProducts(language='RU', currency='RUB')
    product_ids = ['https://aliexpress.com/item/1005006190803860.html', '1005006190803860']
    category_path = Path('output') / 'category_name'
    products = await affiliated_products.process_affiliate_products(product_ids, category_path)
    for product in products:
        print(product.product_title)

"""
MODE = 'dev'

import asyncio
from datetime import datetime
import html
from pathlib import Path
from urllib.parse import urlparse
from types import SimpleNamespace
from typing import List

from src.logger.logger import logger
from src import gs
from src.suppliers.aliexpress import AliApi
from src.suppliers.aliexpress.campaign.html_generators import ProductHTMLGenerator, CategoryHTMLGenerator, CampaignHTMLGenerator
from src.suppliers.aliexpress.utils.ensure_https import ensure_https
from src.product.product_fields import ProductFields as f
from src.utils.image import save_png_from_url
from src.utils.video import save_video_from_url
from src.utils.file import get_directory_names, get_filenames, read_text_file, save_text_file
from src.utils.jjson import j_loads_ns, j_dumps
from src.utils.printer import pprint


class AliAffiliatedProducts(AliApi):
    """
    Класс для сбора данных о продуктах с аффилированными ссылками.

    :param language: Язык для рекламной кампании (по умолчанию 'EN').
    :type language: str | dict
    :param currency: Валюта для рекламной кампании (по умолчанию 'USD').
    :type currency: str
    """
    language: str = None
    currency: str = None

    def __init__(self,
                 language: str | dict = 'EN',
                 currency: str = 'USD',
                 *args, **kwargs):
        """
        Инициализирует класс AliAffiliatedProducts.

        :param language: Язык для рекламной кампании (по умолчанию 'EN').
        :type language: str | dict
        :param currency: Валюта для рекламной кампании (по умолчанию 'USD').
        :type currency: str
        """
        if not language or not currency:
            logger.critical('Не указан язык или валюта!')
            return
        super().__init__(language, currency)
        self.language, self.currency = language, currency

    async def process_affiliate_products(self, prod_ids: list[str], category_root: Path | str) -> list[SimpleNamespace]:
        """
        Обрабатывает список идентификаторов или URL-адресов продуктов, возвращая список продуктов с партнерскими ссылками и сохраненными изображениями.

        :param prod_ids: Список URL-адресов или идентификаторов продуктов.
        :type prod_ids: list[str]
        :param category_root: Путь к корневой директории категории.
        :type category_root: Path | str
        :return: Список обработанных продуктов с партнерскими ссылками и сохраненными изображениями.
        :rtype: list[SimpleNamespace]

        :raises Exception: Если не удалось найти категорию в кампании.

        :Example:
            >>> campaign = SimpleNamespace(category={})
            >>> category_name = "electronics"
            >>> prod_ids = ["http://example.com/product1", "http://example.com/product2"]
            >>> products = await campaign.process_affiliate_products(category_name, prod_ids)
            >>> for product in products:
            ...     print(product.product_title)
            "Product 1 Title"
            "Product 2 Title"

        :Notes:
            - Извлекает содержимое страниц из URL-адресов.
            - Обрабатывает партнерские ссылки и сохранение изображений/видео.
            - Генерирует и сохраняет данные кампании и выходные файлы.

        :Flowchart:
            
            .. code-block:: text
            
                ┌───────────────────────────────────────────────┐
                │ Start                                         │
                └───────────────────────────────────────────────┘
                                    │
                                    ▼
                ┌─────────────────────────────────────────────────────────┐
                │ Try to get category from campaign using `category_name` │
                └─────────────────────────────────────────────────────────┘
                                    │
                                    ┴───────────────────────────────────────────┐
                                    │                                           │
                                    ▼                                           ▼
                ┌──────────────────────────────────────────────────────┐
                │ Campaign Category found: Initialize paths,           │
                │ set promotional URLs, and process products           │
                └──────────────────────────────────────────────────────┘
                                    │
                                    ▼
                ┌───────────────────────────────────────────────┐
                │ No category found: Create default category    │
                │ and initialize paths, set promotional URLs,   │
                │ and process products                          │
                └───────────────────────────────────────────────┘
                                    │
                                    ▼
                ┌───────────────────────────────────────────────┐
                │ Initialize paths and prepare data structures  │
                └───────────────────────────────────────────────┘
                                    │
                                    ▼
                ┌───────────────────────────────────────────────┐
                │ Process products URLs to get affiliate links  │
                └───────────────────────────────────────────────┘
                                    │
                        ┌───────────┴───────────────────────────┐
                        │                                       │
                        ▼                                       ▼
                ┌─────────────────────────────────────────────┐
                │ No affiliate links found: Log warning       │
                └─────────────────────────────────────────────┘
                                    │
                                    ▼
                ┌───────────────────────────────────────────────┐
                │ Retrieve product details for affiliate URLs   │
                └───────────────────────────────────────────────┘
                                    │
                                    ▼
                ┌───────────────────────────────────────────────┐
                │ Process each product and save images/videos   │
                └───────────────────────────────────────────────┘
                                    │
                                    ▼
                ┌───────────────────────────────────────────────┐
                │ Prepare and save final output data            │
                └───────────────────────────────────────────────┘
                                    │
                                    ▼
                ┌───────────────────────────────────────────────┐
                │ Return list of affiliated products            │    
                └───────────────────────────────────────────────┘
                                    │
                                    ▼
                ┌───────────────────────────────────────────────┐
                │ End                                           │
                └───────────────────────────────────────────────┘
        """
        _promotion_links: list = []
        _prod_urls: list = []
        # Преобразует URL-адреса продуктов в формат `https://aliexpress.com/item/<product_id>.html`
        normilized_prod_urls = ensure_https(prod_ids)

        for prod_url in normilized_prod_urls:
            # Получение партнерских ссылок для каждого URL-адреса
            _links = super().get_affiliate_links(prod_url)
            if _links:
                _links = _links[0]
            if hasattr(_links, 'promotion_link'):
                # Добавление партнерской ссылки и URL-адреса продукта в списки
                _promotion_links.append(_links.promotion_link)
                _prod_urls.append(prod_url)
                logger.info(f"Найдена партнерская ссылка для {_links.promotion_link}")
            else:
                continue

        if not _promotion_links:
            # Логирование предупреждения, если не найдено партнерских ссылок
            logger.warning(
                f'Не найдены партнерские продукты {prod_ids=}\n')
            return

        # Получение подробной информации о продуктах по партнерским ссылкам
        _affiliated_products: List[SimpleNamespace] = self.retrieve_product_details(
            _prod_urls)
        if not _affiliated_products:
            return

        affiliated_products_list: list[SimpleNamespace] = []
        product_titles: list = []
        for product, promotion_link in zip(_affiliated_products, _promotion_links):
            # Добавление заголовка продукта в список
            product_titles.append(product.product_title)
            # Установка языка и партнерской ссылки для продукта
            product.language = self.language
            product.promotion_link = promotion_link
            # Формирование пути для сохранения изображения
            image_path = Path(category_root) / 'images' / \
                f"{product.product_id}.png"
            # Сохранение изображения продукта
            await save_png_from_url(product.product_main_image_url, image_path)
            logger.info(f"Сохранено изображение для {product.product_id=}")

            # Сохранение пути к изображению
            product.local_saved_image = str(image_path)
            if len(product.product_video_url) > 1:
                # Получение расширения файла видео
                parsed_url: Path = urlparse(product.product_video_url)
                suffix: str = Path(parsed_url.path).suffix

                # Формирование пути для сохранения видео
                video_path: Path = Path(category_root) / 'videos' / \
                    f'{product.product_id}{suffix}'
                # Сохранение видео продукта
                await save_video_from_url(product.product_video_url, video_path)
                # Сохранение пути к видео
                product.local_saved_video = str(video_path)
                logger.info(f"Сохранено видео для {product.product_id=}")
            # Логирование заголовка продукта
            logger.info(f"{product.product_title}")
            # Сохранение данных о продукте в JSON файл
            j_dumps(product, Path(category_root) /
                    f'{self.language}_{self.currency}' / f'{product.product_id}.json')
            # Добавление продукта в список
            affiliated_products_list.append(product)

        # Формирование пути для сохранения списка заголовков продуктов
        product_titles_path: Path = category_root / \
            f"{self.language}_{self.currency}" / 'product_titles.txt'
        # Сохранение списка заголовков продуктов в файл
        save_text_file(product_titles, product_titles_path)
        # Возврат списка обработанных продуктов
        return affiliated_products_list

```