# Анализ кода модуля `affiliated_products_generator.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован, используются классы для организации функциональности.
    - Присутствует логирование с использованием `logger`.
    - Код использует асинхронные операции, что повышает производительность.
    -  Используются `Path` для работы с файловой системой.
    -  Присутствуют docstring для классов и методов.
    -  Код использует `j_loads_ns` и `j_dumps` для работы с JSON.
-  Минусы
    -  Не все функции имеют подробные docstring с примерами.
    -  Некоторые комментарии не соответствуют стандартам RST.
    -  Есть дублирование импорта `logger`.
    -  Не хватает обработки ошибок при загрузке данных.
    -  Используются конструкции  `if hasattr(_links, 'promotion_link'):`, которые могут быть упрощены.
    -  Не всегда используется форматирование строк f-строками.

**Рекомендации по улучшению**

1.  Добавить docstring в формате RST для всех функций и методов, включая примеры использования.
2.  Убрать дублирующийся импорт `logger`.
3.  Уточнить комментарии для соответствия RST.
4.  Обрабатывать ошибки при запросах к API и сохранении файлов.
5.  Использовать f-строки для форматирования строк.
6.  Переработать условную проверку `if hasattr(_links, 'promotion_link'):` для большей читаемости.
7.  Удалить избыточное использование переменных `print_flag` и `_` в названиях переменных.
8.  Добавить проверку на существование `category_root`
9. Добавить описание модуля

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для генерации партнерских товаров AliExpress.
=========================================================================================

Этот модуль содержит класс :class:`AliAffiliatedProducts`, который используется для получения
партнерских ссылок на товары AliExpress, их обработки и сохранения данных, включая изображения
и видео.

Пример использования
--------------------

Пример использования класса `AliAffiliatedProducts`:

.. code-block:: python

    from pathlib import Path
    import asyncio

    async def main():
        generator = AliAffiliatedProducts(language='ru', currency='RUB')
        product_ids = ['https://aliexpress.com/item/1005006068049905.html']
        category_path = Path('output_category')
        products = await generator.process_affiliate_products(product_ids, category_path)
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
from src.endpoints.prestashop.product_fields import ProductFields as f
from src.utils.image import save_image_from_url
from src.utils.video import save_video_from_url
from src.utils.file_async import (read_text_file,
                        get_filenames_from_directory,
                        get_directory_names,
                        save_text_file
                        )
from src.utils.jjson import j_loads_ns, j_dumps


class AliAffiliatedProducts(AliApi):
    """
    Класс для сбора полных данных о продуктах по URL-адресам или идентификаторам продуктов.

    Более подробную информацию о том, как создавать шаблоны для рекламных кампаний, смотрите в разделе
    `Managing Aliexpress Ad Campaigns`.
    """
    language: str = None
    currency: str = None

    def __init__(self,
                 language: str = 'EN',
                 currency: str = 'USD',
                 *args, **kwargs):
        """
        Инициализирует класс `AliAffiliatedProducts`.

        Args:
            language (str): Язык для кампании (по умолчанию 'EN').
            currency (str): Валюта для кампании (по умолчанию 'USD').
        """
        if not language or not currency:
            logger.critical(f"Не указан язык или валюта!")
            return
        super().__init__(language, currency)
        self.language, self.currency = language, currency


    async def process_affiliate_products(self, prod_ids: list[str], category_root: Path | str) -> list[SimpleNamespace]:
        """
        Обрабатывает список идентификаторов продуктов или URL-адресов и возвращает список продуктов
        с партнерскими ссылками и сохраненными изображениями.

        Args:
            prod_ids (list[str]): Список URL-адресов или идентификаторов продуктов.
            category_root (Path | str): Корневой путь к каталогу категории.

        Returns:
            list[SimpleNamespace]: Список обработанных продуктов с партнерскими ссылками и сохраненными изображениями.

        Example:
            >>> import asyncio
            >>> from pathlib import Path
            >>> async def main():
            ...     generator = AliAffiliatedProducts(language='ru', currency='RUB')
            ...     product_ids = ['https://aliexpress.com/item/1005006068049905.html']
            ...     category_path = Path('output_category')
            ...     products = await generator.process_affiliate_products(product_ids, category_path)
            ...     for product in products:
            ...         print(product.product_title)
            >>> if __name__ == "__main__":
            ...    asyncio.run(main())


        Raises:
            FileNotFoundError: Если `category_root` не существует.
            Exception: При возникновении других ошибок.

        Notes:
            - Получает контент страницы по URL-адресам.
            - Обрабатывает партнерские ссылки и сохранение изображений/видео.
            - Генерирует и сохраняет данные кампании и выходные файлы.
        """
        if not Path(category_root).exists():
           logger.error(f"Директория {category_root} не найдена.")
           raise FileNotFoundError(f"Директория {category_root} не найдена.")
        promotion_links: list = []
        prod_urls: list = []
        normalized_prod_urls = ensure_https(prod_ids) # <- привожу к виду `https://aliexpress.com/item/<product_id>.html`

        for prod_url in normalized_prod_urls:
            links = super().get_affiliate_links(prod_url)
            if links:
                links = links[0]
                if hasattr(links, 'promotion_link'): # проверка наличия аттрибута
                    promotion_links.append(links.promotion_link)
                    prod_urls.append(prod_url)
                    logger.info(f"Найдена партнерская ссылка для {links.promotion_link}")
            else:
                continue

        if not promotion_links:
            logger.warning(f"Партнерские продукты не найдены {prod_ids=}")
            return

        affiliated_products: List[SimpleNamespace] = self.retrieve_product_details(
            prod_urls)
        if not affiliated_products:
            return

        affiliated_products_list: list[SimpleNamespace] = []
        product_titles: list = []
        for product, promotion_link in zip(affiliated_products, promotion_links):
            product_titles.append(product.product_title)
            product.language = self.language
            product.promotion_link = promotion_link
            image_path = Path(category_root) / 'images' / f"{product.product_id}.png"
            try:
                await save_image_from_url(product.product_main_image_url, image_path)
                logger.info(f"Сохранено изображение для {product.product_id=}")
            except Exception as e:
                logger.error(f"Не удалось сохранить изображение для {product.product_id=}", exc_info=e)

            product.local_image_path = str(image_path)
            if product.product_video_url:
                parsed_url: Path = urlparse(product.product_video_url)
                suffix: str = Path(parsed_url.path).suffix

                video_path: Path = Path(category_root) / 'videos' / f'{product.product_id}{suffix}'
                try:
                    await save_video_from_url(product.product_video_url, video_path)
                    product.local_video_path = str(video_path)
                    logger.info(f"Сохранено видео для {product.product_id=}")
                except Exception as e:
                    logger.error(f"Не удалось сохранить видео для {product.product_id=}", exc_info=e)

            logger.info(f"{product.product_title}")
            try:
                j_dumps(product, Path(category_root) / f'{self.language}_{self.currency}' / f'{product.product_id}.json')
            except Exception as e:
                logger.error(f"Не удалось сохранить json файл для {product.product_id=}", exc_info=e)


            affiliated_products_list.append(product)

        product_titles_path: Path = Path(category_root) / f"{self.language}_{self.currency}" / 'product_titles.txt'
        try:
           await save_text_file(product_titles, product_titles_path)
        except Exception as e:
            logger.error(f"Не удалось сохранить product_titles.txt", exc_info=e)

        return affiliated_products_list