## Анализ кода модуля `affiliated_products_generator`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
  - Использование аннотаций типов.
  - Наличие структуры и базовой документации.
  - Логирование основных этапов работы.
- **Минусы**:
  - Смешанный стиль кавычек (используются как одинарные, так и двойные).
  - Неполная документация, требующая расширения и уточнения.
  - Повторяющийся импорт `logger`.
  - Не везде используется `j_loads` или `j_loads_ns` для работы с JSON.

**Рекомендации по улучшению**:

1. **Форматирование и стиль кода**:
   - Привести весь код к единому стилю кавычек (одинарные).
   - Устранить дублирование импорта `logger`.

2. **Документация**:
   - Дополнить docstring для всех методов и классов, используя формат, указанный в инструкции.
   - Описать все входные параметры и возвращаемые значения.
   - Добавить примеры использования.

3. **Использование `j_loads` и `j_dumps`**:
   - Убедиться, что для чтения JSON файлов используется `j_loads` или `j_loads_ns`, а для записи - `j_dumps`.

4. **Логирование**:
   - Добавить логирование важных этапов выполнения кода, чтобы упростить отладку и мониторинг.
   - Использовать `logger.error` для логирования ошибок с указанием `exc_info=True` для получения полной трассировки.

5. **Обработка исключений**:
   - Добавить обработку исключений, чтобы предотвратить аварийное завершение программы.

6. **Улучшение читаемости**:
   - Разбить длинные строки кода на несколько строк для улучшения читаемости.

**Оптимизированный код**:

```python
## \file /src/suppliers/aliexpress/affiliated_products_generator.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
Модуль для генерации партнерских продуктов AliExpress.
=======================================================

Модуль содержит класс :class:`AliAffiliatedProducts`, который используется для сбора данных о продуктах
с партнерскими ссылками с AliExpress.

Пример использования
----------------------

>>> affiliated_products = AliAffiliatedProducts(language='EN', currency='USD')
>>> product_ids = ['1234567890', '0987654321']
>>> category_root = 'path/to/category'
>>> products = await affiliated_products.process_affiliate_products(product_ids, category_root)
>>> for product in products:
...     print(product.product_title)
"""

import asyncio
from datetime import datetime
import html
from pathlib import Path
from urllib.parse import urlparse
from types import SimpleNamespace
from typing import List, Optional

from src.logger.logger import logger
from src import gs
from src.suppliers.aliexpress import AliApi
from src.suppliers.aliexpress.campaign.html_generators import (
    ProductHTMLGenerator,
    CategoryHTMLGenerator,
    CampaignHTMLGenerator,
)
from src.suppliers.aliexpress.utils.ensure_https import ensure_https
from src.endpoints.prestashop.product_fields import ProductFields as f
from src.utils.image import save_image_from_url_async
from src.utils.video import save_video_from_url
from src.utils.file import (
    read_text_file,
    get_filenames_from_directory,
    get_directory_names,
    save_text_file,
)
from src.utils.jjson import j_loads_ns, j_dumps

class AliAffiliatedProducts(AliApi):
    """
    Класс для сбора данных о продуктах с партнерскими ссылками с AliExpress.
    Для получения дополнительной информации о создании шаблонов для рекламных кампаний см. раздел "Управление рекламными кампаниями Aliexpress".
    """

    language: str = None
    currency: str = None

    def __init__(
        self,
        language: str = 'EN',
        currency: str = 'USD',
        *args,
        **kwargs,
    ) -> None:
        """
        Инициализирует класс AliAffiliatedProducts.

        Args:
            language (str): Язык для кампании (по умолчанию 'EN').
            currency (str): Валюта для кампании (по умолчанию 'USD').

        Example:
            >>> affiliated_products = AliAffiliatedProducts(language='RU', currency='RUB')
        """
        if not language or not currency:
            logger.critical('No language or currency provided!')
            return
        super().__init__(language, currency)
        self.language, self.currency = language, currency

    async def process_affiliate_products(
        self, prod_ids: list[str], category_root: Path | str
    ) -> list[SimpleNamespace] | None:
        """
        Обрабатывает список ID или URL продуктов и возвращает список продуктов с партнерскими ссылками и сохраненными изображениями.

        Args:
            prod_ids (list[str]): Список URL или ID продуктов.
            category_root (Path | str): Корневой путь к категории.

        Returns:
            list[SimpleNamespace] | None: Список обработанных продуктов с партнерскими ссылками и сохраненными изображениями. Возвращает None в случае ошибки.

        Example:
            >>> affiliated_products = AliAffiliatedProducts(language='EN', currency='USD')
            >>> product_ids = ['1234567890', '0987654321']
            >>> category_root = 'path/to/category'
            >>> products = await affiliated_products.process_affiliate_products(product_ids, category_root)
            >>> if products:
            ...     for product in products:
            ...         print(product.product_title)

        Raises:
            Exception: Если возникает ошибка при обработке продуктов.

        Notes:
            - Получает контент страницы из URL.
            - Обрабатывает партнерские ссылки и сохранение изображений/видео.
            - Генерирует и сохраняет данные кампании и выходные файлы.
        """
        _promotion_links: list = []
        _prod_urls: list = []
        normilized_prod_urls = ensure_https(prod_ids)  # <- привожу к виду `https://aliexpress.com/item/<product_id>.html`
        print_flag = ''  # <- флаг переключения печати в одну строку

        for prod_url in normilized_prod_urls:
            _links = super().get_affiliate_links(prod_url)
            if _links:
                _links = _links[0]
            if hasattr(_links, 'promotion_link'):
                _promotion_links.append(_links.promotion_link)
                _prod_urls.append(prod_url)
                logger.info(f'Found affiliate for {_links.promotion_link}')
            else:
                continue

        if not _promotion_links:
            logger.warning(f'No affiliate products returned {prod_ids=}')
            return None

        _affiliated_products: List[SimpleNamespace] = self.retrieve_product_details(
            _prod_urls
        )
        if not _affiliated_products:
            return None

        affiliated_products_list: list[SimpleNamespace] = []
        product_titles: list = []
        for product, promotion_link in zip(_affiliated_products, _promotion_links):
            product_titles.append(product.product_title)
            product.language = self.language
            product.promotion_link = promotion_link
            image_path = Path(category_root) / 'images' / f'{product.product_id}.png'
            try:
                await save_image_from_url(product.product_main_image_url, image_path)
                logger.info(f'Saved image for {product.product_id=}')
            except Exception as e:
                logger.error(f'Error saving image for {product.product_id=}', exc_info=True)

            product.local_image_path = str(image_path)
            if len(product.product_video_url) > 1:
                parsed_url: Path = urlparse(product.product_video_url)
                suffix: str = Path(parsed_url.path).suffix

                video_path: Path = Path(category_root) / 'videos' / f'{product.product_id}{suffix}'
                try:
                    await save_video_from_url(product.product_video_url, video_path)
                    logger.info(f'Saved video for {product.product_id=}')
                except Exception as e:
                    logger.error(f'Error saving video for {product.product_id=}', exc_info=True)
                product.local_video_path = str(video_path)

            logger.info(f'{product.product_title}')
            try:
                j_dumps(product, Path(category_root) / f'{self.language}_{self.currency}' / f'{product.product_id}.json')
            except Exception as e:
                logger.error(f'Error dumping product to JSON for {product.product_id=}', exc_info=True)

            affiliated_products_list.append(product)

        product_titles_path: Path = (
            Path(category_root) / f'{self.language}_{self.currency}' / 'product_titles.txt'
        )
        try:
            await save_text_file(product_titles, product_titles_path)
        except Exception as e:
            logger.error(f'Error saving product titles to file', exc_info=True)

        return affiliated_products_list