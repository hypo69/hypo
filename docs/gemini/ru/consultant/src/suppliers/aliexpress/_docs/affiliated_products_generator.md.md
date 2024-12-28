# Анализ кода модуля `affiliated_products_generator.py`

**Качество кода**
7
-   Плюсы
    - Код хорошо структурирован и разбит на логические блоки.
    - Используются аннотации типов, что улучшает читаемость и поддержку кода.
    - Присутствует базовая обработка ошибок с использованием `try-except`.
    - Логирование событий выполняется с помощью `logger`.
    - Код использует `pprint` для форматированного вывода.
-   Минусы
    - Некоторые комментарии не соответствуют reStructuredText (RST) стандарту.
    - Используются стандартные блоки `try-except`, вместо рекомендованной обработки ошибок через `logger.error` в некоторых местах.
    - Не все функции и методы имеют docstring в формате RST.
    - Присутствуют потенциальные места для улучшения производительности, например, асинхронные запросы.
    - Не везде используется `j_dumps` или `j_loads_ns` вместо стандартного `json.load`.
    - Код содержит `...` как точки остановки, которые должны быть проработаны.
    - Дублирование кода в `delete_product` при обработке разных типов `product_id`.

**Рекомендации по улучшению**

1.  **Документация в формате RST:**
    -   Переписать все комментарии и docstring в формате reStructuredText (RST).
    -   Добавить docstring к каждой функции и методу, включая описание параметров и возвращаемых значений.
    -   Использовать аннотации типов для параметров и возвращаемых значений функций.

2.  **Улучшенное логирование:**
    -   Заменить стандартные блоки `try-except` на обработку ошибок с помощью `logger.error` для более централизованного логирования.
    -   Добавить больше информативных сообщений в лог.

3.  **Использование `j_dumps`:**
    -   Убедиться, что для всех операций записи JSON используется `j_dumps` вместо стандартного `json.dumps`.

4.  **Рефакторинг `delete_product`:**
    -   Упростить логику функции `delete_product` для избежания дублирования кода.
    -   Использовать более понятные имена переменных.

5.  **Асинхронность:**
    -   Рассмотреть возможность использования асинхронных запросов для повышения производительности, особенно при обработке большого количества продуктов.

6.  **Обработка `...`:**
    -   Убрать или заменить `...` на реальную логику или обработку исключений.

7.  **Унификация импортов:**
    -   Привести в соответствие импорты с ранее обработанными файлами (при наличии) для единообразия.

8. **Улучшить читаемость**
   - Добавить в начало модуля описание модуля в формате RST.
   - Разбить длинные строки кода на несколько строк для лучшей читаемости.

**Оптимизированный код**

```python
"""
Модуль для генерации партнерских продуктов AliExpress.
===================================================

Этот модуль содержит класс :class:`AliAffiliatedProducts`, который используется для сбора полных данных о продуктах
с использованием API партнерской программы AliExpress. Он позволяет получать информацию о продуктах по их URL или ID,
сохранять изображения, видео и JSON-данные.

Пример использования
--------------------

Пример использования класса `AliAffiliatedProducts`:

.. code-block:: python

    parser = AliAffiliatedProducts(
        campaign_name="test_campaign",
        campaign_category="electronics",
        language="RU",
        currency="RUB"
    )

    product_urls = [
        "https://www.aliexpress.com/item/123456789.html",
        "987654321",
    ]

    products = parser.process_affiliate_products(product_urls)
"""
import asyncio
from itertools import count
from math import log
from pathlib import Path
from typing import List, Union, Optional, Any
from types import SimpleNamespace
from urllib.parse import urlparse, parse_qs

from src import gs
from src.suppliers.aliexpress import AliApi
from src.suppliers.aliexpress import Aliexpress
from src.suppliers.aliexpress.affiliate_links_shortener_via_webdriver import AffiliateLinksShortener
from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids
from src.suppliers.aliexpress.utils.set_full_https import ensure_https
from src.utils.convertor.csv2json import csv2dict
from src.utils.jjson import j_dumps
from src.utils import save_png_from_url, save_video_from_url
from src.utils.printer import pprint
from src.utils.file import read_text_file, save_text_file
from src.utils.convertor.list2string import list2string
from src.utils.convertor.list import convert_list_to_homogeneous_list
from src.logger.logger import logger


class AliAffiliatedProducts(AliApi):
    """
    Класс для сбора полных данных о продуктах AliExpress по URL или ID.

    :param campaign_name: Название рекламной кампании.
    :param campaign_category: Категория кампании (необязательно).
    :param language: Язык кампании (по умолчанию 'EN').
    :param currency: Валюта кампании (по умолчанию 'USD').

    :ivar campaign_name: Название рекламной кампании.
    :vartype campaign_name: str
    :ivar campaign_category: Категория кампании (может быть None).
    :vartype campaign_category: Optional[str]
    :ivar campaign_path: Путь к директории кампании.
    :vartype campaign_path: Path
    :ivar language: Язык кампании.
    :vartype language: str
    :ivar currency: Валюта кампании.
    :vartype currency: str

    .. code-block:: python

        # Пример использования:
        prod_urls = ['123','456',...]
        prod_urls = ['https://www.aliexpress.com/item/123.html','456',...]

        parser = AliAffiliatedProducts(
                                    campaign_name,
                                    campaign_category,
                                    language,
                                    currency)

        products = parser._affiliate_product(prod_urls)
    """
    campaign_name: str
    campaign_category: Optional[str]
    campaign_path: Path
    language: str
    currency: str

    def __init__(self,
                 campaign_name: str,
                 campaign_category: Optional[str] = None,
                 language: str = 'EN',
                 currency: str = 'USD',
                 *args, **kwargs):
        """
        Инициализирует класс AliAffiliatedProducts.

        :param campaign_name: Название рекламной кампании.
        :type campaign_name: str
        :param campaign_category: Категория кампании (необязательно).
        :type campaign_category: Optional[str]
        :param language: Язык кампании (по умолчанию 'EN').
        :type language: str
        :param currency: Валюта кампании (по умолчанию 'USD').
        :type currency: str
        :param tracking_id: Tracking ID для Aliexpress API.
        :type tracking_id: str
        """
        super().__init__(language, currency)

        self.campaign_name = campaign_name
        self.campaign_category = campaign_category
        self.language = language
        self.currency = currency
        self.locale = f"{self.language}_{self.currency}"
        self.campaign_path = gs.path.google_drive / 'aliexpress' / 'campaigns' / self.campaign_name / 'categories' / self.campaign_category

    def process_affiliate_products(self, prod_urls: List[str]) -> List[SimpleNamespace]:
        """
        Обрабатывает список URL-адресов или ID продуктов, возвращая список продуктов с партнерскими ссылками и сохраненными изображениями.

        :param prod_urls: Список URL-адресов или ID продуктов.
        :type prod_urls: List[str]
        :return: Список обработанных продуктов.
        :rtype: List[SimpleNamespace]
        """
        _promotion_links: list = []
        _prod_urls: list = []
        promotional_prod_urls = ensure_https(prod_urls)
        print_flag = 'new_line'
        # Код итерируется по списку URL-адресов продуктов
        for prod_url in promotional_prod_urls:
            # Код получает партнерские ссылки для каждого URL
            _link = super().get_affiliate_links(prod_url)
            if _link:
                _link = _link[0]
            # Код проверяет наличие атрибута `promotion_link` в объекте ссылки
            if hasattr(_link, 'promotion_link'):
                _promotion_links.append(_link.promotion_link)
                _prod_urls.append(prod_url)
                pprint(f'found affiliate for: {_link.promotion_link}', end=print_flag)
                print_flag = 'inline'
            else:
                logger.info_red(f'Not found affiliate for {prod_url}')
        # Код проверяет, что список партнерских ссылок не пуст
        if not _promotion_links:
            logger.error('No affiliate products returned')
            return
        logger.info_red('Start receiving product details...')
        # Код получает детали продуктов
        _affiliate_products: SimpleNamespace = self.retrieve_product_details(_prod_urls)
        if not _affiliate_products:
            return

        print_flag = 'new_line'
        # Код итерируется по деталям продуктов и партнерским ссылкам
        for product, promotion_link in zip(_affiliate_products, _promotion_links):
            # Код проверяет наличие партнерской ссылки
            if not promotion_link:
                # Код парсит URL-адрес продукта
                parsed_url = urlparse(product.promotion_link)
                query_params = parse_qs(parsed_url.query)
                aff_short_key = query_params.get('aff_short_key', [None])[0]
                # Код проверяет наличие `aff_short_key`
                if aff_short_key:
                    # Код устанавливает партнерскую ссылку в сокращенном виде
                    product.promotion_link = fr'https://s.click.aliexpress.com/e/{aff_short_key}'
                else:
                    # Если продукт не партнерский, код удаляет его
                    self.delete_product(product.product_id)
                    continue
            else:
                # Код устанавливает партнерскую ссылку
                product.promotion_link = promotion_link
            # Код сохраняет изображение продукта
            image_path = self.campaign_path / 'images' / f"{product.product_id}.png"
            save_png_from_url(product.product_main_image_url, image_path, exc_info=False)
            product.local_saved_image = str(image_path)
            # Код проверяет наличие видео продукта
            if len(product.product_video_url) > 1:
                # Код получает расширение видео
                parsed_url = urlparse(product.product_video_url)
                suffix = Path(parsed_url.path).suffix
                # Код сохраняет видео продукта
                video_path = self.campaign_path / 'videos' / f'{product.product_id}.{suffix}'
                save_video_from_url(product.product_video_url, video_path, exc_info=False)
                product.local_saved_video = str(video_path)

            pprint(f'caught product - {product.product_id}', end=print_flag)
            print_flag = 'inline'
            # Код сохраняет данные продукта в JSON файл
            if not j_dumps(product, self.campaign_path / self.locale / f"{product.product_id}.json", exc_info=False):
                 logger.warning(
                     f"""Failed to write dictionary: \\n {pprint(product)} \\n path: {self.campaign_path / self.locale / product.product_id}.json""",
                     exc_info=False)
                 continue
            

        pprint(f'caught {len(_affiliate_products)}', end='new_line')
        return _affiliate_products

    def delete_product(self, product_id: str, exc_info: bool = False):
        """
        Удаляет продукт, у которого нет партнерской ссылки.

        :param product_id: ID продукта для удаления.
        :type product_id: str
        :param exc_info: Флаг для вывода информации об исключении.
        :type exc_info: bool
        """
        _product_id = extract_prod_ids(product_id)

        product_path = self.campaign_path / 'sources.txt'
        prepared_product_path = self.campaign_path / '_sources.txt'
        products_list = read_text_file(product_path)
        if products_list:
            products_list = convert_list_to_homogeneous_list(products_list)
            for record in products_list:
                if _product_id:
                    record_id = extract_prod_ids(record)
                    if record_id == str(product_id):
                        products_list.remove(record)
                        save_text_file(list2string(products_list, '\n'), prepared_product_path)
                        break
                else:
                    if record == str(product_id):
                        products_list.remove(record)
                        save_text_file(list2string(products_list, '\n'), product_path)
        else:
            product_path = self.campaign_path / 'sources' / f'{product_id}.html'
            try:
                product_path.rename(self.campaign_path / 'sources' / f'{product_id}_.html')
                logger.success(f"Product file {product_path} renamed successfully.")
            except FileNotFoundError as ex:
                logger.error(f"Product file {product_path} not found.", exc_info=exc_info)
            except Exception as ex:
                logger.critical(f"An error occurred while deleting the product file {product_path}.", ex)
```