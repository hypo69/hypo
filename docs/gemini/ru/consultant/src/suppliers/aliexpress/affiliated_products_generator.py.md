## Анализ кода модуля `affiliated_products_generator.py`

**Качество кода**
9
 -  Плюсы
    - Код хорошо структурирован и разбит на функции, что делает его читаемым и поддерживаемым.
    - Присутствует базовая обработка ошибок, которая помогает в отладке и предотвращении сбоев.
    - Используются асинхронные операции для неблокирующего ввода-вывода.
    - Код использует `logger` для записи информации, что упрощает отслеживание процессов.
    -  В целом код соответствует PEP8 и использует typing для указания типов переменных.

 -  Минусы
    -  Не все функции и классы документированы в формате reStructuredText (RST).
    -  Использование `print` для отладки не соответствует логгированию, которое должно быть основным способом отслеживания событий.
    -  В коде присутсвуют закомментированные строки, которые нужно удалить или раскомментировать если необходимо.
    -  Некоторые переменные могут быть более описательными, чтобы улучшить читаемость.
    -  Следует избегать прямого использования `return` в `__init__`, лучше сгенерировать исключение.

**Рекомендации по улучшению**

1.  **Документация:**
    - Добавить docstring в формате RST для модуля, класса и методов.
    - Уточнить описание аргументов и возвращаемых значений.

2.  **Логирование:**
    - Заменить `print` на `logger.info` для отладочной печати.
    - Улучшить сообщения об ошибках, добавляя контекст (например, `product_id`).
    - Использовать `logger.exception` для логирования ошибок с трассировкой стека.

3.  **Обработка ошибок:**
    - Пересмотреть использование `return` в `__init__`.
    - Использовать `try-except` блоки более целенаправленно, чтобы избегать перехвата всех исключений.

4.  **Улучшение кода:**
    - Удалить или раскомментировать закоментированный код.
    - Улучшить имена переменных для лучшей читаемости.
    - Добавить проверки на существование директорий перед сохранением файлов.
    - Убрать `if not _promotion_links:` чтобы код дальше исполнялся, даже если аффилиат ссылки не были найдены.

5.  **Оптимизация:**
    - Использовать `asyncio.gather` для параллельной загрузки изображений и видео.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с партнерскими продуктами AliExpress.
=======================================================

Этот модуль предоставляет класс :class:`AliAffiliatedProducts`, который позволяет собирать
полные данные о продуктах с AliExpress, включая партнерские ссылки и сохраненные изображения.

Основной функционал включает:

-   Получение партнерских ссылок на товары.
-   Сбор подробной информации о товарах, такой как название, описание, изображения и видео.
-   Сохранение изображений и видео локально.
-   Генерация HTML-шаблонов для рекламных кампаний.

Пример использования:
---------------------

.. code-block:: python

    from pathlib import Path
    import asyncio
    from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
    
    async def main():
        products_processor = AliAffiliatedProducts(language='RU', currency='RUB')
        prod_ids = ['https://aliexpress.com/item/1005006349572132.html', 'https://aliexpress.com/item/1005006349572133.html']
        category_root = Path('output/test_category')
        products = await products_processor.process_affiliate_products(prod_ids, category_root)
        if products:
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
# from src.logger.logger import logger  # <- дубликат

MODE = 'dev'


class AliAffiliatedProducts(AliApi):
    """
    Класс для сбора полных данных о продуктах с AliExpress, включая партнерские ссылки.

    Этот класс наследует функциональность :class:`AliApi` и расширяет ее возможностями
    по сбору информации о продуктах и их сохранению.

    :param language: Язык для кампании (по умолчанию 'EN').
    :type language: str
    :param currency: Валюта для кампании (по умолчанию 'USD').
    :type currency: str

    :ivar language: Язык для кампании.
    :vartype language: str
    :ivar currency: Валюта для кампании.
    :vartype currency: str
    """

    language: str = None
    currency: str = None

    def __init__(self,
                 language: str = 'EN',
                 currency: str = 'USD',
                 *args, **kwargs):
        """
        Инициализирует класс AliAffiliatedProducts.

        :param language: Язык для кампании (по умолчанию 'EN').
        :type language: str
        :param currency: Валюта для кампании (по умолчанию 'USD').
        :type currency: str
        :raises ValueError: Если язык или валюта не указаны.
        """
        if not language or not currency:
            logger.critical(f"No language or currency provided: {language=}, {currency=}")
            raise ValueError("Language and currency must be provided.")  # <-  выбрасываем исключение
        super().__init__(language, currency)
        self.language, self.currency = language, currency

    async def process_affiliate_products(self, prod_ids: list[str], category_root: Path | str) -> list[SimpleNamespace]:
        """
        Обрабатывает список идентификаторов или URL-адресов продуктов и возвращает список продуктов
        с партнерскими ссылками и сохраненными изображениями.

        :param prod_ids: Список URL-адресов или идентификаторов продуктов.
        :type prod_ids: list[str]
        :param category_root: Путь к корневой директории категории.
        :type category_root: Path | str
        :return: Список обработанных продуктов с партнерскими ссылками и сохраненными изображениями.
        :rtype: list[SimpleNamespace]
        :raises Exception: Если возникает ошибка при обработке продуктов.

         .. note::
            - Получает контент страницы из URL-адресов.
            - Обрабатывает партнерские ссылки и сохранение изображений/видео.
            - Генерирует и сохраняет данные кампании и выходные файлы.
        """

        _promotion_links: list = []
        _prod_urls: list = []
        normilized_prod_urls = ensure_https(prod_ids)  # <- приводим к виду `https://aliexpress.com/item/<product_id>.html`

        for prod_url in normilized_prod_urls:
            _links = super().get_affiliate_links(prod_url)
            if _links:
                _links = _links[0]
            if hasattr(_links, 'promotion_link'):
                _promotion_links.append(_links.promotion_link)
                _prod_urls.append(prod_url)
                logger.info(f"Found affiliate for {_links.promotion_link}")
            else:
                logger.warning(f"No affiliate link found for {prod_url}")  # <- логируем, что для данного товара нет аффилиат ссылки
                continue

        if not _promotion_links:
            logger.warning(f'No affiliate products returned for {prod_ids=}')  # <- сообщаем об этом, но код продолжает работу
            return [] # <- Возвращаем пустой массив, если нет аффилиат ссылок

        _affiliated_products: List[SimpleNamespace] = self.retrieve_product_details(_prod_urls)
        if not _affiliated_products:
           logger.warning(f"No product details retrieved for {_prod_urls=}")  # <- логируем, что не смогли получить данные о товарах
           return [] # <- Возвращаем пустой массив, если нет товаров

        affiliated_products_list: list[SimpleNamespace] = []
        product_titles: list = []
        
        
        async def process_product(product, promotion_link):
            """
            Обрабатывает отдельный продукт, сохраняет изображения и видео.

            :param product: Объект продукта.
            :type product: SimpleNamespace
            :param promotion_link: Партнерская ссылка.
            :type promotion_link: str
            """
            product_titles.append(product.product_title)
            product.language = self.language
            product.promotion_link = promotion_link
            
            category_path = Path(category_root)
            image_path = category_path / 'images' / f"{product.product_id}.png"
            video_path = None
            if not image_path.parent.exists():
                 image_path.parent.mkdir(parents=True, exist_ok=True)

            await save_png_from_url(product.product_main_image_url, image_path)
            logger.info(f"Saved image for {product.product_id=}")
            product.local_saved_image = str(image_path)
            
            if product.product_video_url:
                parsed_url: Path = urlparse(product.product_video_url)
                suffix: str = Path(parsed_url.path).suffix
                
                video_path = category_path / 'videos' / f'{product.product_id}{suffix}'
                if not video_path.parent.exists():
                    video_path.parent.mkdir(parents=True, exist_ok=True)
                await save_video_from_url(product.product_video_url, video_path)
                product.local_saved_video = str(video_path)
                logger.info(f"Saved video for {product.product_id=}")

            logger.info(f"{product.product_title}")
            json_file_path = category_path / f'{self.language}_{self.currency}' / f'{product.product_id}.json'
            if not json_file_path.parent.exists():
               json_file_path.parent.mkdir(parents=True, exist_ok=True)

            j_dumps(product, json_file_path)
            affiliated_products_list.append(product)

        await asyncio.gather(*[process_product(product, promotion_link)
                                for product, promotion_link in zip(_affiliated_products, _promotion_links)])
    
        product_titles_path: Path = Path(category_root) / f"{self.language}_{self.currency}" / 'product_titles.txt'
        if not product_titles_path.parent.exists():
            product_titles_path.parent.mkdir(parents=True, exist_ok=True)

        save_text_file(product_titles, product_titles_path)
        return affiliated_products_list