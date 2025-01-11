# Анализ кода модуля `affiliated_products_generator`

## Качество кода:

- **Соответствие стандартам**: 7
- **Плюсы**:
  - Код достаточно хорошо структурирован и разбит на логические блоки.
  - Используются аннотации типов, что повышает читаемость кода.
  - Присутствует базовая обработка ошибок, хотя и не всегда оптимальная.
  - Есть примеры использования класса и методов в документации.
  - Используются `logger` для логирования различных этапов обработки.
- **Минусы**:
  -  Не везде используется `j_dumps` или `j_loads_ns` из `src.utils.jjson`.
  -  Смешанное использование кавычек в коде и документации.
  -  Не все функции имеют RST-документацию.
  -  Использование `print` вместо `logger.info` в некоторых местах.
  -  Много `...` в коде, что затрудняет его понимание.
  -  Не всегда корректно используется обработка исключений.
  -  Отсутствует `__all__` в файле.

## Рекомендации по улучшению:

1.  **Форматирование кода**:
    -  Привести все строки кода к использованию одинарных кавычек (`'`). Двойные кавычки использовать только для `print`, `input` и логирования.
2.  **Использование `j_loads`**:
    -  Заменить стандартные `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
3.  **Документация**:
    -   Добавить RST-документацию ко всем методам и функциям, включая описание параметров, возвращаемых значений, исключений и примеры использования.
    -   Улучшить описание класса и его назначения.
4.  **Логирование**:
    -   Заменить `print` на `logger.info` или `logger.debug` для вывода сообщений.
    -   Использовать `logger.error` для обработки ошибок вместо `try-except`.
5.  **Обработка исключений**:
    -  Избегать чрезмерного использования стандартных блоков `try-except`. Лучше использовать `logger.error(..., exc_info=True)` для отслеживания ошибок.
6.  **Структура кода**:
    -  Убрать `...` маркеры, добавив вместо них реальный код или логику.
    -  Проверить все импорты на наличие неиспользуемых.
    -  Добавить `__all__` в начале файла.
7.  **Улучшение комментариев**:
    -   Использовать более точные формулировки в комментариях. Вместо "получаем" использовать "извлекаем", "проверяем" и т.д.
8.  **Рефакторинг метода `delete_product`**:
    -  Сделать код более читаемым и понятным, разбив его на несколько функций, если необходимо.

## Оптимизированный код:

```python
"""
Модуль для сбора данных о партнерских продуктах AliExpress.
=============================================================

Этот модуль содержит класс :class:`AliAffiliatedProducts`,
который используется для сбора полной информации о продуктах
с использованием партнерского API AliExpress.

Он включает в себя функции для получения партнерских ссылок,
сохранения изображений, видео и данных JSON.

Пример использования
----------------------
.. code-block:: python

    parser = AliAffiliatedProducts(
        campaign_name='test_campaign',
        campaign_category='electronics',
        language='ru',
        currency='RUB'
    )
    prod_urls = ['https://www.aliexpress.com/item/123.html', '456', ...]
    products = parser.process_affiliate_products(prod_urls)
"""
import asyncio
from itertools import count
from math import log
from pathlib import Path
from typing import List, Union, Optional
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
from src.logger.logger import logger # Correct import for logger

__all__ = ['AliAffiliatedProducts']


class AliAffiliatedProducts(AliApi):
    """
    Класс для сбора полных данных о продуктах из URL-адресов или идентификаторов продуктов.

    Использует партнерский API AliExpress для обработки URL-адресов продуктов или идентификаторов
    и получения подробной информации о партнерских продуктах, включая сохранение изображений, видео и данных JSON.

    :param campaign_name: Название рекламной кампании.
    :type campaign_name: str
    :param campaign_category: Категория для кампании (по умолчанию None).
    :type campaign_category: Optional[str]
    :param language: Язык для кампании (по умолчанию 'EN').
    :type language: str
    :param currency: Валюта для кампании (по умолчанию 'USD').
    :type currency: str

    Пример использования:
    ----------------------
    .. code-block:: python

        prod_urls = ['123', '456', ...]
        prod_urls = ['https://www.aliexpress.com/item/123.html', '456', ...]

        parser = AliAffiliatedProducts(
            campaign_name='test_campaign',
            campaign_category='electronics',
            language='ru',
            currency='RUB'
        )

        products = parser.process_affiliate_products(prod_urls)
    """

    campaign_name: str
    campaign_category: Optional[str]
    campaign_path: Path
    language: str
    currency: str

    def __init__(
        self,
        campaign_name: str,
        campaign_category: Optional[str] = None,
        language: str = 'EN',
        currency: str = 'USD',
        *args, **kwargs
    ):
        """
        Инициализация класса AliAffiliatedProducts.

        :param campaign_name: Название рекламной кампании.
        :type campaign_name: str
        :param campaign_category: Категория для кампании (по умолчанию None).
        :type campaign_category: Optional[str]
        :param language: Язык для кампании (по умолчанию 'EN').
        :type language: str
        :param currency: Валюта для кампании (по умолчанию 'USD').
        :type currency: str
        """
        super().__init__(language, currency)

        self.campaign_name = campaign_name
        self.campaign_category = campaign_category
        self.language = language
        self.currency = currency
        self.locale = f'{self.language}_{self.currency}'
        self.campaign_path = gs.path.google_drive / 'aliexpress' / 'campaigns' / self.campaign_name / 'categories' / self.campaign_category

    def process_affiliate_products(self, prod_urls: List[str]) -> List[SimpleNamespace]:
        """
        Обрабатывает список URL-адресов и возвращает список продуктов с партнерскими ссылками и сохраненными изображениями.

        :param prod_urls: Список URL-адресов или идентификаторов продуктов.
        :type prod_urls: List[str]
        :return: Список обработанных продуктов.
        :rtype: List[SimpleNamespace]
        """
        _promotion_links: list = []
        _prod_urls: list = []
        promotional_prod_urls = ensure_https(prod_urls)
        print_flag = 'new_line'
        for prod_url in promotional_prod_urls:
            _link = super().get_affiliate_links(prod_url)
            if _link:
                _link = _link[0]
            if hasattr(_link, 'promotion_link'):
                _promotion_links.append(_link.promotion_link)
                _prod_urls.append(prod_url)

                pprint(f'found affiliate for: {_link.promotion_link}', end=print_flag)
                print_flag = 'inline'
            else:
                logger.info(f'Not found affiliate for {prod_url}') # Changed to logger.info

        if not _promotion_links:
            logger.error('No affiliate products returned')
            return
        logger.info('Start receiving product details...') # Changed to logger.info
        _affiliate_products: SimpleNamespace = self.retrieve_product_details(_prod_urls)
        if not _affiliate_products:
            return

        print_flag = 'new_line'
        for product, promotion_link in zip(_affiliate_products, _promotion_links):
            if not promotion_link:
                parsed_url = urlparse(product.promotion_link)
                query_params = parse_qs(parsed_url.query)
                aff_short_key = query_params.get('aff_short_key', [None])[0]
                if aff_short_key:
                    product.promotion_link = fr'https://s.click.aliexpress.com/e/{aff_short_key}'
                else:
                    """ This product is not an affiliate"""
                    self.delete_product(product.product_id)
                    continue
            else:
                product.promotion_link = promotion_link

            image_path = self.campaign_path / 'images' / f'{product.product_id}.png'
            save_png_from_url(product.product_main_image_url, image_path, exc_info=False)
            product.local_image_path = str(image_path)
            if len(product.product_video_url) > 1:
                parsed_url = urlparse(product.product_video_url)
                suffix = Path(parsed_url.path).suffix

                video_path = self.campaign_path / 'videos' / f'{product.product_id}.{suffix}'
                save_video_from_url(product.product_video_url, video_path, exc_info=False)
                product.local_video_path = str(video_path)

            pprint(f'caught product - {product.product_id}', end=print_flag)
            print_flag = 'inline'

            if not j_dumps(product, self.campaign_path / self.locale / f'{product.product_id}.json', exc_info=False):
                logger.warning(f'Failed to write dictionary: \n {pprint(product)} \n path: {self.campaign_path / self.locale / product.product_id}.json', exc_info=False)
                continue

        pprint(f'caught {len(_affiliate_products)}', end='new_line')
        return _affiliate_products

    def delete_product(self, product_id: str, exc_info: bool = False):
        """
        Удаляет продукт, у которого нет партнерской ссылки.

        :param product_id: Идентификатор продукта.
        :type product_id: str
        :param exc_info: Флаг для вывода информации об исключении (по умолчанию False).
        :type exc_info: bool
        """
        _product_id = extract_prod_ids(product_id)

        product_path = self.campaign_path / 'sources.txt'
        prepared_product_path = self.campaign_path / '_sources.txt'
        products_list = read_text_file(product_path)
        if products_list:
            products_list = convert_list_to_homogeneous_list(products_list) # Assuming this function exists
            for record in products_list:
                if _product_id:
                    record_id = extract_prod_ids(record)
                    if record_id == str(product_id):
                        products_list.remove(record)
                        save_text_file(list2string(products_list, '\n'), prepared_product_path) # Assuming this function exists
                        break
                else:
                    if record == str(product_id):
                        products_list.remove(record)
                        save_text_file(list2string(products_list, '\n'), product_path) # Assuming this function exists

        else:
            product_path = self.campaign_path / 'sources' / f'{product_id}.html'
            try:
                product_path.rename(self.campaign_path / 'sources' / f'{product_id}_.html')
                logger.info(f'Product file {product_path} renamed successfully.') # Changed to logger.info
            except FileNotFoundError:
                logger.error(f'Product file {product_path} not found.', exc_info=exc_info) # Added exc_info
            except Exception as ex:
                logger.critical(f'An error occurred while deleting the product file {product_path}.', exc_info=True) # Added exc_info
```