## Анализ кода модуля `affiliated_products_generator.py`

**Качество кода**
9
-   Плюсы
    -   Код хорошо структурирован и разбит на функции, что облегчает чтение и понимание.
    -   Используется асинхронность для неблокирующих операций, таких как загрузка изображений и видео.
    -   Используются `logger` для логирования важной информации и ошибок.
    -   Применяются константы для задания путей и имен файлов, что делает код более гибким и читаемым.
    -   Код старается обрабатывать ошибки и выводит предупреждения, когда не находит аффилиатных ссылок.
-   Минусы
    -   Не все функции и классы имеют docstring в формате reStructuredText (RST).
    -   В коде местами встречаются `print` для отладки.
    -   Некоторые переменные имеют префиксы (`_`), которые могут сбивать с толку.
    -   Использование `SimpleNamespace` может усложнить отладку.
    -   Некоторые части кода закомментированы, их стоит удалить или переработать.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Добавить docstring в формате reStructuredText (RST) для класса `AliAffiliatedProducts`, методов `__init__` и `process_affiliate_products`.
    -   Использовать `:param:` и `:return:` для описания параметров и возвращаемых значений в docstring.
2.  **Логирование**:
    -   Заменить все `print` на `logger.info` или `logger.debug`.
    -   Улучшить форматирование логов для лучшего чтения.
3.  **Переменные**:
    -   Изменить префикс `_` для переменных на более понятный.
    -   Использовать более осмысленные имена переменных.
4.  **Обработка ошибок**:
    -   Использовать `try-except` блоки только там, где это действительно необходимо.
    -   Логировать ошибки через `logger.error` с указанием конкретной ситуации.
5.  **Рефакторинг**:
    -   Разбить метод `process_affiliate_products` на несколько более мелких методов для лучшей читаемости.
    -   Удалить закомментированный код.
6.  **Использование констант**:
    -   Если используются константы для путей, добавить их в начало модуля.
7.  **Безопасность**:
    -   Использовать более безопасные методы для обработки URL.
8.  **Производительность**:
    -   Рассмотреть возможность использования `asyncio.gather` для параллельной загрузки изображений и видео.
9.  **Тестирование**:
    -   Добавить тесты для основных функций, чтобы убедиться в их корректной работе.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для генерации аффилированных товаров AliExpress.
=====================================================

Этот модуль содержит класс :class:`AliAffiliatedProducts`, который используется для сбора полных данных о товарах
с аффилированными ссылками с AliExpress.

Модуль позволяет:
    - Получать аффилированные ссылки на товары.
    - Сохранять изображения и видео товаров.
    - Генерировать HTML для рекламных кампаний.
    - Поддерживает различные языки и валюты.

Пример использования
--------------------

.. code-block:: python

    from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
    import asyncio
    from pathlib import Path

    async def main():
        generator = AliAffiliatedProducts(language='RU', currency='RUB')
        prod_ids = [
             'https://aliexpress.ru/item/1005006184879902.html',
             'https://aliexpress.ru/item/1005005839179329.html'
            ]
        category_root = Path('./output')
        products = await generator.process_affiliate_products(prod_ids, category_root)
        for product in products:
           print(product.product_title)

    if __name__ == "__main__":
        asyncio.run(main())
"""
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

OUTPUT_DIR = Path('./output')
IMAGES_DIR_NAME = 'images'
VIDEOS_DIR_NAME = 'videos'
PRODUCT_TITLES_FILE_NAME = 'product_titles.txt'

class AliAffiliatedProducts(AliApi):
    """
    Класс для сбора полных данных о товарах с аффилированными ссылками с AliExpress.

    :param language: Язык для рекламной кампании (по умолчанию 'EN').
    :type language: str, optional
    :param currency: Валюта для рекламной кампании (по умолчанию 'USD').
    :type currency: str, optional
    """
    language: str = None
    currency: str = None

    def __init__(self,
                 language: str = 'EN',
                 currency: str = 'USD',
                 *args, **kwargs):
        """
        Инициализирует класс AliAffiliatedProducts.

        :param language: Язык для рекламной кампании (по умолчанию 'EN').
        :type language: str, optional
        :param currency: Валюта для рекламной кампании (по умолчанию 'USD').
        :type currency: str, optional
        """
        if not language or not currency:
            logger.critical(f"Отсутствует язык или валюта!")
            return
        super().__init__(language, currency)
        self.language, self.currency = language, currency

    async def process_affiliate_products(self, prod_ids: list[str], category_root: Path | str) -> list[SimpleNamespace]:
        """
        Обрабатывает список ID или URL товаров и возвращает список товаров с аффилированными ссылками и сохраненными изображениями.

        :param prod_ids: Список URL или ID товаров.
        :type prod_ids: list[str]
        :param category_root: Корневой каталог для сохранения данных.
        :type category_root: Path | str
        :return: Список обработанных товаров с аффилированными ссылками и сохраненными изображениями.
        :rtype: list[SimpleNamespace]

        :raises Exception: Если не удается получить аффилированные ссылки.
        """
        promotion_links: list = []
        product_urls: list = []
        normalized_product_urls = ensure_https(prod_ids)
        for product_url in normalized_product_urls:
            affiliate_links = super().get_affiliate_links(product_url)
            if affiliate_links:
                affiliate_link = affiliate_links[0]
                if hasattr(affiliate_link, 'promotion_link'):
                    promotion_links.append(affiliate_link.promotion_link)
                    product_urls.append(product_url)
                    logger.info(f"Найдена аффилированная ссылка: {affiliate_link.promotion_link}")
                else:
                    logger.warning(f"Для {product_url=} не найдена аффилированная ссылка")
                    continue
            else:
                logger.warning(f"Для {product_url=} не найдены аффилированные ссылки")
                continue
        if not promotion_links:
            logger.warning(f'Не найдено аффилированных товаров {prod_ids=}')
            return []
        
        affiliated_products: List[SimpleNamespace] = self.retrieve_product_details(product_urls)
        if not affiliated_products:
            logger.warning(f'Не удалось получить информацию о товарах для {product_urls=}')
            return []


        affiliated_products_list: list[SimpleNamespace] = []
        product_titles: list = []
        for product, promotion_link in zip(affiliated_products, promotion_links):
            product_titles.append(product.product_title)
            product.language = self.language
            product.promotion_link = promotion_link
            image_path = Path(category_root) / IMAGES_DIR_NAME / f"{product.product_id}.png"
            await save_png_from_url(product.product_main_image_url, image_path)
            logger.info(f"Сохранено изображение для {product.product_id=}")
            product.local_saved_image = str(image_path)

            if product.product_video_url:
                parsed_url: Path = urlparse(product.product_video_url)
                suffix: str = Path(parsed_url.path).suffix
                video_path: Path = Path(category_root) / VIDEOS_DIR_NAME / f'{product.product_id}{suffix}'
                await save_video_from_url(product.product_video_url, video_path)
                product.local_saved_video = str(video_path)
                logger.info(f"Сохранено видео для {product.product_id=}")

            logger.info(f"Обработан товар: {product.product_title}")
            j_dumps(product, Path(category_root) / f'{self.language}_{self.currency}' / f'{product.product_id}.json')

            affiliated_products_list.append(product)

        product_titles_path: Path = Path(category_root) / f"{self.language}_{self.currency}" / PRODUCT_TITLES_FILE_NAME
        save_text_file(product_titles, product_titles_path)
        return affiliated_products_list