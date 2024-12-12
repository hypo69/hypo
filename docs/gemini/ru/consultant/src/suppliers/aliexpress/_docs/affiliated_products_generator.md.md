# Анализ кода модуля `affiliated_products_generator.py`

**Качество кода**
6
- Плюсы
    - Код в целом структурирован и выполняет свою задачу по сбору данных о партнерских товарах AliExpress.
    - Используются стандартные библиотеки и некоторые кастомные утилиты.
    - Присутствует базовая обработка ошибок и логирование.
    - Используется `SimpleNamespace` для представления данных, что удобно.
    - Есть пример использования в docstring класса.
- Минусы
    - Не все функции и методы имеют docstring в формате reStructuredText (RST).
    -  Использование `j_dumps` не является консистентным, и есть избыточное использование `try-except`.
    - Код не везде следует принципу DRY (Don't Repeat Yourself), есть дублирование логики.
    - Отсутствует единый стиль форматирования.
    - Логирование не всегда консистентно использует `logger.error`.
    - Используется не консистентное форматирование f-строк и обычных строк в логах.

**Рекомендации по улучшению**
1.  **Документирование**:
    - Добавить docstring в формате reStructuredText (RST) ко всем функциям, методам и классам, включая описание параметров, возвращаемых значений и исключений.
    - Добавить описание модуля в начале файла.
2.  **Импорты**:
    - Упорядочить импорты, разделив на стандартные, сторонние и локальные.
    - Проверить и добавить отсутствующие импорты.
3.  **Обработка данных**:
    - Заменить стандартный `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson` при чтении файлов.
    - Использовать `j_dumps` для записи JSON.
4.  **Логирование**:
    - Использовать `logger.error` вместо стандартных `try-except` блоков, где это возможно.
    - Привести к одному стилю логирование, убрав избыточное использование f-строк и принтирования.
    - Использовать `logger` для логирования всех важных событий.
5.  **Рефакторинг**:
    - Вынести повторяющиеся блоки кода в отдельные функции или методы.
    - Упростить логику в `process_affiliate_products` и `delete_product`.
6.  **Обработка URL**:
   - Упростить преобразование URL используя `urljoin`.
7.  **Форматирование**:
   - Обеспечить консистентное форматирование кода, использовать линтер и форматер.
   - Привести к единому стилю f-строки в логах.
8.  **Удаление продукта**:
   - Переработать логику удаления продукта для уменьшения количества условных операторов.

**Оптимизированный код**
```python
"""
Модуль для сбора данных о партнерских товарах AliExpress.
=========================================================

Этот модуль содержит класс :class:`AliAffiliatedProducts`, который используется для сбора полных данных
о продуктах из AliExpress Affiliate API. Он обрабатывает URL-адреса или идентификаторы продуктов,
извлекает информацию о партнерских продуктах, включая сохранение изображений, видео и JSON-данных.

Пример использования
--------------------

Пример использования класса `AliAffiliatedProducts`:

.. code-block:: python

    prod_urls = ['123', '456', ...]
    parser = AliAffiliatedProducts(
        campaign_name='my_campaign',
        campaign_category='electronics',
        language='RU',
        currency='RUB'
    )
    products = parser.process_affiliate_products(prod_urls)
"""
import asyncio
from itertools import count
from math import log
from pathlib import Path
from typing import List, Union, Optional, Any
from types import SimpleNamespace
from urllib.parse import urlparse, parse_qs, urljoin

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
from src.utils.file import read_text_file, save_text_file, list2string, convert_list_to_homogeneous_list
from src.logger.logger import logger


class AliAffiliatedProducts(AliApi):
    """
    Класс для сбора полных данных о продуктах из URL-адресов или идентификаторов продуктов.

    :param campaign_name: Название рекламной кампании.
    :type campaign_name: str
    :param campaign_category: Категория кампании (по умолчанию None).
    :type campaign_category: Optional[str]
    :param language: Язык кампании (по умолчанию 'EN').
    :type language: str
    :param currency: Валюта кампании (по умолчанию 'USD').
    :type currency: str
    :ivar campaign_path: Путь к каталогу, где сохраняются материалы кампании.
    :vartype campaign_path: Path
    :ivar locale: Локаль кампании, сформированная из языка и валюты (например, 'en_USD').
    :vartype locale: str

    :Example:
    
    .. code-block:: python

        prod_urls = ['123', '456', ...]
        parser = AliAffiliatedProducts(
            campaign_name='my_campaign',
            campaign_category='electronics',
            language='RU',
            currency='RUB'
        )
        products = parser.process_affiliate_products(prod_urls)
    """

    campaign_name: str
    campaign_category: Optional[str]
    campaign_path: Path
    language: str
    currency: str
    locale: str

    def __init__(
        self,
        campaign_name: str,
        campaign_category: Optional[str] = None,
        language: str = 'EN',
        currency: str = 'USD',
        *args,
        **kwargs
    ):
        """
        Инициализация класса AliAffiliatedProducts.

        :param campaign_name: Название рекламной кампании.
        :type campaign_name: str
        :param campaign_category: Категория кампании (по умолчанию None).
        :type campaign_category: Optional[str]
        :param language: Язык кампании (по умолчанию 'EN').
        :type language: str
        :param currency: Валюта кампании (по умолчанию 'USD').
        :type currency: str
        :param tracking_id: ID отслеживания для AliExpress API.
        :type tracking_id: str
        """
        super().__init__(language, currency)
        # Инициализация атрибутов класса
        self.campaign_name = campaign_name
        self.campaign_category = campaign_category
        self.language = language
        self.currency = currency
        self.locale = f"{self.language}_{self.currency}"
        # Формирование пути к директории кампании
        self.campaign_path = gs.path.google_drive / 'aliexpress' / 'campaigns' / self.campaign_name / 'categories' / self.campaign_category

    def process_affiliate_products(self, prod_urls: List[str]) -> List[SimpleNamespace]:
        """
        Обрабатывает список URL-адресов или идентификаторов продуктов, извлекает партнерские ссылки,
        сохраняет изображения и видео, и возвращает список обработанных продуктов.

        :param prod_urls: Список URL-адресов или идентификаторов продуктов.
        :type prod_urls: List[str]
        :return: Список обработанных продуктов в виде объектов SimpleNamespace.
        :rtype: List[SimpleNamespace]
        """
        _promotion_links: list = []
        _prod_urls: list = []
        promotional_prod_urls = ensure_https(prod_urls)
        print_flag = 'new_line'
        # Цикл по всем URL-ам
        for prod_url in promotional_prod_urls:
            _link = super().get_affiliate_links(prod_url)
            if _link:
                _link = _link[0]
            # Если есть партнерская ссылка, то добавляем ее в список
            if hasattr(_link, 'promotion_link'):
                _promotion_links.append(_link.promotion_link)
                _prod_urls.append(prod_url)
                pprint(f'found affiliate for: {_link.promotion_link}', end=print_flag)
                print_flag = 'inline'
            else:
                logger.info(f'Not found affiliate for {prod_url}')
        # Если партнерских ссылок нет, то возвращаем None
        if not _promotion_links:
            logger.error('No affiliate products returned')
            return
        logger.info('Start receiving product details...')
        # Получение детальной информации по продуктам
        _affiliate_products: SimpleNamespace = self.retrieve_product_details(_prod_urls)
        if not _affiliate_products:
            return
        # Обработка каждого продукта
        print_flag = 'new_line'
        for product, promotion_link in zip(_affiliate_products, _promotion_links):
            if not promotion_link:
                parsed_url = urlparse(product.promotion_link)
                query_params = parse_qs(parsed_url.query)
                aff_short_key = query_params.get('aff_short_key', [None])[0]
                if aff_short_key:
                    product.promotion_link = f'https://s.click.aliexpress.com/e/{aff_short_key}'
                else:
                   # Удаление продукта, если нет партнерской ссылки
                   self.delete_product(product.product_id)
                   continue
            else:
                product.promotion_link = promotion_link
            # Сохранение изображения продукта
            image_path = self.campaign_path / 'images' / f"{product.product_id}.png"
            save_png_from_url(product.product_main_image_url, image_path, exc_info=False)
            product.local_saved_image = str(image_path)
            # Сохранение видео продукта
            if product.product_video_url:
                parsed_url = urlparse(product.product_video_url)
                suffix = Path(parsed_url.path).suffix
                video_path = self.campaign_path / 'videos' / f'{product.product_id}{suffix}'
                save_video_from_url(product.product_video_url, video_path, exc_info=False)
                product.local_saved_video = str(video_path)
            # Вывод информации о сохраненном продукте
            pprint(f'caught product - {product.product_id}', end=print_flag)
            print_flag = 'inline'
            # Сохранение данных о продукте в JSON
            if not j_dumps(product, self.campaign_path / self.locale / f"{product.product_id}.json", exc_info=False):
                logger.warning(f'Failed to write dictionary: \n {pprint(product)} \n path: {self.campaign_path / self.locale / product.product_id}.json', exc_info=False)
                continue

        pprint(f'caught {len(_affiliate_products)}', end='new_line')
        return _affiliate_products
    
    def delete_product(self, product_id: str, exc_info: bool = False) -> None:
        """
        Удаляет продукт, который не имеет партнерской ссылки.

        :param product_id: Идентификатор продукта для удаления.
        :type product_id: str
        :param exc_info: Флаг для логирования информации об исключении (по умолчанию False).
        :type exc_info: bool
        """
        _product_id = extract_prod_ids(product_id)

        product_path = self.campaign_path / 'sources.txt'
        prepared_product_path = self.campaign_path / '_sources.txt'
        products_list = read_text_file(product_path)
        
        if products_list:
            products_list = convert_list_to_homogeneous_list(products_list)
            for record in products_list:
                record_id = extract_prod_ids(record) if _product_id else record
                if record_id == str(product_id):
                    products_list.remove(record)
                    save_text_file(list2string(products_list, '\n'), prepared_product_path if _product_id else product_path)
                    break
        else:
            product_path = self.campaign_path / 'sources' / f'{product_id}.html'
            try:
                new_path = self.campaign_path / 'sources' / f'{product_id}_.html'
                product_path.rename(new_path)
                logger.info(f"Product file {product_path} renamed successfully.")
            except FileNotFoundError as ex:
                logger.error(f"Product file {product_path} not found.", exc_info=exc_info)
            except Exception as ex:
                logger.critical(f"An error occurred while deleting the product file {product_path}.", exc_info=exc_info)
```