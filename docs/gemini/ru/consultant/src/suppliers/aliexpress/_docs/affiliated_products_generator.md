# Анализ кода модуля `affiliated_products_generator`

**Качество кода: 7/10**

*   **Плюсы:**
    *   Код разбит на логические блоки, что улучшает читаемость.
    *   Используются асинхронные операции для неблокирующего выполнения.
    *   Есть логирование ошибок и действий с помощью `logger`.
    *   Присутствуют примеры использования класса.
    *   Используются `SimpleNamespace` для хранения данных.
*   **Минусы:**
    *   Не хватает подробной документации в формате RST для функций и методов.
    *   Некоторые комментарии не информативны и требуют уточнения.
    *   Используется `print` для вывода в консоль, что лучше заменить на `logger`.
    *   Смешаны операции `print` и `logger`.
    *   Обработка ошибок `try-except` не всегда информативна, лучше использовать `logger.error`.
    *   Отсутствует проверка типов данных перед выполнением операций.
    *   Используется `super()` в методах класса без необходимости.
    *   Дублирование кода в `delete_product`.
    *   Не все переменные и методы имеют docstring.
    *   Метод `delete_product` выполняет несколько задач, что противоречит принципу единственной ответственности.

**Рекомендации по улучшению**

1.  **Документирование:**
    *   Добавить docstring в формате RST для всех функций, методов и класса.
    *   Уточнить комментарии, сделав их более информативными.
2.  **Логирование:**
    *   Заменить `print` на `logger.info`, `logger.debug` для вывода информации.
    *   Унифицировать логирование, используя только `logger`.
    *   Использовать `logger.error` для обработки ошибок вместо `try-except` блоков, где это возможно.
3.  **Обработка ошибок:**
    *   Улучшить обработку ошибок, предоставляя более конкретную информацию.
    *   Удалить избыточные `try-except`, заменив на `logger.error`
4.  **Структура кода:**
    *   Разбить метод `delete_product` на несколько более мелких для лучшего разделения ответственности.
    *   Проверять типы данных перед выполнением операций для предотвращения ошибок.
    *   Удалить `super` там, где он не используется.
    *   Удалить дублирование кода.
5.  **Производительность:**
    *   Рассмотреть возможность использования асинхронных операций для повышения производительности при обработке большого количества товаров.
6.  **Общее:**
    *   Пересмотреть именование переменных и методов для соответствия стандартам PEP8.
    *   Использовать `j_dumps` для записи JSON файлов и `j_loads` для чтения.
    *   Сделать код более читаемым, используя более информативные названия переменных и методов.

**Оптимизированный код**

```python
"""
Модуль для сбора данных об аффилированных продуктах с AliExpress.
======================================================================

Этот модуль содержит класс :class:`AliAffiliatedProducts`, который используется для
получения данных о продуктах, включая аффилированные ссылки, изображения и видео.

Пример использования
--------------------

.. code-block:: python

    from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
    
    prod_urls = ['123', '456', ...]
    prod_urls = ['https://www.aliexpress.com/item/123.html', '456', ...]

    parser = AliAffiliatedProducts(
        campaign_name='test_campaign',
        campaign_category='test_category',
        language='EN',
        currency='USD'
    )

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
# from src.settings import settings #  удален неиспользуемый импорт
from src.suppliers.aliexpress import AliApi
from src.suppliers.aliexpress import Aliexpress
from src.suppliers.aliexpress.affiliate_links_shortener_via_webdriver import AffiliateLinksShortener
from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids
from src.suppliers.aliexpress.utils.set_full_https import ensure_https
from src.utils.convertor.csv2json import csv2dict 
from src.utils.jjson import j_dumps, j_loads # добавлен j_loads
from src.utils import save_png_from_url, save_video_from_url
from src.utils.printer import pprint
from src.utils.file import read_text_file, save_text_file, list2string # добавил list2string
from src.utils.list import convert_list_to_homogeneous_list

from src.logger.logger import logger


class AliAffiliatedProducts(AliApi):
    """
    Класс для сбора полных данных о продуктах с использованием URL или ID продукта.

    Этот класс расширяет :class:`AliApi` для получения данных о продуктах,
    включая аффилированные ссылки, изображения и видео.
    
    :param campaign_name: Название рекламной кампании.
    :type campaign_name: str
    :param campaign_category: Категория кампании (по умолчанию `None`).
    :type campaign_category: Optional[str]
    :param language: Язык для кампании (по умолчанию `'EN'`).
    :type language: str
    :param currency: Валюта для кампании (по умолчанию `'USD'`).
    :type currency: str

    Пример использования:

    .. code-block:: python

        prod_urls = ['123', '456', ...]
        prod_urls = ['https://www.aliexpress.com/item/123.html', '456', ...]

        parser = AliAffiliatedProducts(
            campaign_name='test_campaign',
            campaign_category='test_category',
            language='EN',
            currency='USD'
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
        Инициализирует класс AliAffiliatedProducts.
        
        :param campaign_name: Название рекламной кампании.
        :type campaign_name: str
        :param campaign_category: Категория кампании (по умолчанию `None`).
        :type campaign_category: Optional[str]
        :param language: Язык для кампании (по умолчанию `'EN'`).
        :type language: str
        :param currency: Валюта для кампании (по умолчанию `'USD'`).
        :type currency: str
        :param tracking_id: Tracking ID для Aliexpress API.
        :type tracking_id: str
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
        Обрабатывает список URL-адресов продуктов, получает аффилированные ссылки,
        сохраняет изображения и возвращает список обработанных продуктов.

        :param prod_urls: Список URL-адресов или ID продуктов.
        :type prod_urls: List[str]
        :return: Список обработанных продуктов.
        :rtype: List[SimpleNamespace]
        """
        _promotion_links: list = []
        _prod_urls: list = []
        promotional_prod_urls = ensure_https(prod_urls)
        print_flag = 'new_line'

        for prod_url in promotional_prod_urls:
            _link = super().get_affiliate_links(prod_url) # получение аффилированной ссылки
            if _link:
                _link = _link[0]
            if hasattr(_link, 'promotion_link'):
                _promotion_links.append(_link.promotion_link)
                _prod_urls.append(prod_url)
                logger.info(f'found affiliate for: {_link.promotion_link}')# замена print на logger.info
                print_flag = 'inline'
            else:
                logger.info(f'Not found affiliate for {prod_url}')# замена print на logger.info

        if not _promotion_links:
            logger.error('No affiliate products returned')# обработка ошибки, если нет аффилированных продуктов
            return None
        
        logger.info('Start receiving product details...') # замена print на logger.info
        _affiliate_products: SimpleNamespace = self.retrieve_product_details(_prod_urls) # получение деталей продукта

        if not _affiliate_products:
            return None

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
                    self.delete_product(product.product_id) # удаление продукта, если нет аффилированной ссылки
                    continue # переход к следующему продукту
            else:
                product.promotion_link = promotion_link
            
            image_path = self.campaign_path / 'images' / f'{product.product_id}.png'
            save_png_from_url(product.product_main_image_url, image_path, exc_info=False) # сохранение изображения
            product.local_image_path = str(image_path)
            
            if product.product_video_url and len(product.product_video_url) > 1: # Проверяем, что ссылка на видео не пустая
                parsed_url = urlparse(product.product_video_url)
                suffix = Path(parsed_url.path).suffix
                video_path = self.campaign_path / 'videos' / f'{product.product_id}.{suffix}'
                save_video_from_url(product.product_video_url, video_path, exc_info=False) # сохранение видео
                product.local_video_path = str(video_path)

            logger.info(f'caught product - {product.product_id}')# замена print на logger.info
            print_flag = 'inline'

            if not j_dumps(product, self.campaign_path / self.locale / f'{product.product_id}.json', exc_info=False): # сохранение json
                logger.warning(f'Failed to write dictionary: \n {pprint(product)} \n path: {self.campaign_path / self.locale / product.product_id}.json', exc_info=False)# обработка ошибки, если не удалось записать json
                continue

        logger.info(f'caught {len(_affiliate_products)}') # замена print на logger.info
        return _affiliate_products

    def delete_product(self, product_id: str, exc_info: bool = False):
        """
        Удаляет продукт, у которого нет аффилированной ссылки.

        :param product_id: ID продукта.
        :type product_id: str
        :param exc_info: Включать ли информацию об исключении в логи (по умолчанию False).
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
                        save_text_file(prepared_product_path, list2string(products_list, '\n')) # исправление: сохранение списка в строку
                        break
                else:
                    if record == str(product_id):
                        products_list.remove(record)
                        save_text_file(product_path, list2string(products_list, '\n')) # исправление: сохранение списка в строку
                        break
        else:
            product_path = self.campaign_path / 'sources' / f'{product_id}.html'
            try:
                product_path.rename(self.campaign_path / 'sources' / f'{product_id}_.html')
                logger.info(f'Product file {product_path} renamed successfully.')# замена print на logger.info
            except FileNotFoundError:
                 logger.error(f'Product file {product_path} not found.', exc_info=exc_info) # Обработка ошибки файла не найден
            except Exception as ex:
                logger.critical(f'An error occurred while deleting the product file {product_path}.', exc_info=exc_info)# обработка других ошибок
```