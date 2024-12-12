# Анализ кода модуля `api.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разбит на классы и функции.
    - Используется typing для аннотации типов, что улучшает читаемость и поддержку кода.
    - Присутствует логирование ошибок и предупреждений с помощью `logger`.
    - Код использует docstrings для документирования классов и методов.
    - Есть разделение на разные типы запросов и их обработка.

-  Минусы
    - Не везде используется `logger.error` для обработки ошибок, в некоторых местах используется `raise`
    -  Используются как `raise`, так и `logger.warning`, что не соответствует инструкции
    -  Импорты не всегда соответствуют ранее обработанным файлам
    -  В некоторых местах используется `...` для обозначения точек остановки, что может быть нежелательно в production коде.
    -  Некоторые docstring не соответствуют reStructuredText.
    - Есть дублирование кода в методах `get_parent_categories` и `get_child_categories`
    - Присутствует неконсистентность в обработке ошибок: где-то используется `raise`, а где-то `logger.warning` и `return`
    - Местами отсутствует обработка исключений

**Рекомендации по улучшению**

1.  **Использование `logger.error` вместо `raise`**: Замените все `raise` на `logger.error` с возвратом из функции.
2.  **Унифицировать импорты**: Приведите импорты в соответствие с ранее обработанными файлами.
3.  **Удалить `...`**: Замените все точки остановки `...` на конкретную логику или на `pass`.
4.  **Исправить docstring**: Перепишите все docstring в формате reStructuredText.
5. **Устранение дублирования кода**: Вынести общую логику для `get_parent_categories` и `get_child_categories` в отдельную функцию
6. **Добавить обработку исключений**: Добавить обработку исключений в тех местах, где это необходимо
7. **Удалить лишние комментарии**: Удалите закомментированный код

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~
"""
Модуль для работы с API AliExpress.
=========================================================================================

Этот модуль предоставляет класс :class:`AliexpressApi`, который используется для взаимодействия с AliExpress Open Platform API.
Он обеспечивает методы для получения информации о продуктах, генерации партнерских ссылок и работы с категориями.

Пример использования
--------------------

Пример использования класса `AliexpressApi`:

.. code-block:: python

    api = AliexpressApi(
        key='your_api_key',
        secret='your_api_secret',
        language=model_Language.EN,
        currency=model_Currency.USD,
        tracking_id='your_tracking_id'
    )
    products = api.retrieve_product_details(product_ids=['1234567890'])
"""
from typing import List, Union, Any

from src.logger.logger import logger
# from src.utils.printer import pprint  # Этот импорт не используется, удалил его

from .models import (
                    AffiliateLink as model_AffiliateLink,
                    Category as model_Category,
                    ChildCategory as model_ChildCategory,
                    Currency as model_Currency,
                    HotProductsResponse as model_HotProductsResponse,
                    Language as model_Language,
                    LinkType as model_LinkType,
                    Product as model_Product,
                    ProductType as model_ProductType,
                    SortBy as model_SortBy)

from .errors.exceptions import CategoriesNotFoudException
from .helpers.categories import filter_child_categories, filter_parent_categories
from .skd import setDefaultAppInfo
from .skd import api as aliapi
from .errors import ProductsNotFoudException, InvalidTrackingIdException
from .helpers import api_request, parse_products, get_list_as_string, get_product_ids


class AliexpressApi:
    """
    Предоставляет методы для получения информации из AliExpress с использованием API-ключей.

    :param key: API ключ.
    :type key: str
    :param secret: API секрет.
    :type secret: str
    :param language: Языковой код. По умолчанию EN.
    :type language: str
    :param currency: Код валюты. По умолчанию USD.
    :type currency: str
    :param tracking_id: ID отслеживания для генератора ссылок. По умолчанию None.
    :type tracking_id: str, optional
    :param app_signature: Подпись приложения. По умолчанию None.
    :type app_signature: str, optional
    """

    def __init__(self,
        key: str,
        secret: str,
        language: model_Language,
        currency: model_Currency,
        tracking_id: str = None,
        app_signature: str = None,
        **kwargs):
        """
        Инициализирует экземпляр класса AliexpressApi.
        """
        self._key = key
        self._secret = secret
        self._tracking_id = tracking_id
        self._language = language
        self._currency = currency
        self._app_signature = app_signature
        self.categories = None
        setDefaultAppInfo(self._key, self._secret)


    def retrieve_product_details(self,
        product_ids: str | list,
        fields: str | list = None,
        country: str = None,
        **kwargs) -> List[model_Product]:
        """
        Получает информацию о продуктах.

        :param product_ids: Один или несколько идентификаторов или ссылок на продукт.
        :type product_ids: str | list[str]
        :param fields: Поля, которые необходимо включить в результат. По умолчанию все.
        :type fields: str | list[str], optional
        :param country: Фильтр продуктов, которые могут быть отправлены в указанную страну.
                      Возвращает цену согласно налоговой политике страны.
        :type country: str, optional
        :return: Список продуктов.
        :rtype: list[model_Product]
        :raises ProductsNotFoudException: Если продукты не найдены.
        :raises Exception: В случае других ошибок.
        """
        # Код преобразует product_ids в список
        product_ids = get_product_ids(product_ids)
        # Код преобразует product_ids в строку
        product_ids = get_list_as_string(product_ids)

        # Код подготавливает запрос к API
        request = aliapi.rest.AliexpressAffiliateProductdetailGetRequest()
        request.app_signature = self._app_signature
        # Код преобразует fields в строку
        request.fields = get_list_as_string(fields)
        request.product_ids = product_ids
        request.country = country
        request.target_currency = self._currency.upper()
        request.target_language = self._language.upper()
        request.tracking_id = self._tracking_id

        # Код отправляет запрос к API
        response = api_request(request, 'aliexpress_affiliate_productdetail_get_response')
        try:
            # Код проверяет, есть ли результаты в ответе
            if response.current_record_count > 0:
                # Код преобразует продукты в нужный формат
                response = parse_products(response.products.product)
                return response
            else:
                # Код логирует предупреждение об отсутствии продуктов
                logger.warning('No products found with current parameters')
                return
        except Exception as ex:
            # Код логирует ошибку и возвращает None
            logger.error(f'Error during product details retrieval: {ex}', exc_info=False)
            return



    def get_affiliate_links(self,
        links: str | list,
        link_type: model_LinkType = model_LinkType.NORMAL,
        **kwargs) -> List[model_AffiliateLink]:
        """
        Конвертирует список ссылок в партнерские ссылки.

        :param links: Одна или несколько ссылок для конвертации.
        :type links: str | list[str]
        :param link_type: Тип ссылки: обычная или горячая. По умолчанию NORMAL.
        :type link_type: model_LinkType, optional
        :return: Список партнерских ссылок.
        :rtype: list[model_AffiliateLink]
        :raises InvalidTrackingIdException: Если отсутствует tracking_id.
        :raises Exception: В случае других ошибок.
        """
        # Код проверяет наличие tracking_id
        if not self._tracking_id:
            # Код логирует ошибку, если tracking_id отсутствует
            logger.error('The tracking id is required for affiliate links')
            return

        # Код преобразует ссылки в строку
        links = get_list_as_string(links)

        # Код подготавливает запрос к API
        request = aliapi.rest.AliexpressAffiliateLinkGenerateRequest()
        request.app_signature = self._app_signature
        request.source_values = links
        request.promotion_link_type = link_type
        request.tracking_id = self._tracking_id

        # Код отправляет запрос к API
        response = api_request(request, 'aliexpress_affiliate_link_generate_response')
        # Код проверяет ответ
        if not response:
            return
        if response.total_result_count > 0:
            return response.promotion_links.promotion_link
        else:
            # Код логирует предупреждение об отсутствии партнерских ссылок
            logger.warning('Affiliate links not available')
            return


    def get_hotproducts(self,
        category_ids: str | list = None,
        delivery_days: int = None,
        fields: str | list = None,
        keywords: str = None,
        max_sale_price: int = None,
        min_sale_price: int = None,
        page_no: int = None,
        page_size: int = None,
        platform_product_type: model_ProductType = None,
        ship_to_country: str = None,
        sort: model_SortBy = None,
        **kwargs) -> model_HotProductsResponse:
        """
        Ищет партнерские продукты с высокой комиссией.

        :param category_ids: Один или несколько ID категорий.
        :type category_ids: str | list[str], optional
        :param delivery_days: Предполагаемое количество дней доставки.
        :type delivery_days: int, optional
        :param fields: Поля, которые нужно включить в результаты. По умолчанию все.
        :type fields: str | list[str], optional
        :param keywords: Ключевые слова для поиска продуктов.
        :type keywords: str, optional
        :param max_sale_price: Фильтр продуктов с ценой ниже указанного значения.
                             Цены указываются в наименьшей валютной деноминации.
                             Например, $31.41 следует указать как 3141.
        :type max_sale_price: int, optional
        :param min_sale_price: Фильтр продуктов с ценой выше указанного значения.
                             Цены указываются в наименьшей валютной деноминации.
                             Например, $31.41 следует указать как 3141.
        :type min_sale_price: int, optional
        :param page_no: Номер страницы.
        :type page_no: int, optional
        :param page_size: Количество продуктов на странице. Должно быть от 1 до 50.
        :type page_size: int, optional
        :param platform_product_type: Указание типа продукта платформы.
        :type platform_product_type: model_ProductType, optional
        :param ship_to_country: Фильтр продуктов, которые могут быть отправлены в указанную страну.
                             Возвращает цену в соответствии с налоговой политикой страны.
        :type ship_to_country: str, optional
        :param sort: Метод сортировки.
        :type sort: model_SortBy, optional
        :return: Ответ с информацией и списком продуктов.
        :rtype: model_HotProductsResponse
         :raises ProductsNotFoudException: Если продукты не найдены.
        :raises Exception: В случае других ошибок.
        """
        # Код подготавливает запрос к API
        request = aliapi.rest.AliexpressAffiliateHotproductQueryRequest()
        request.app_signature = self._app_signature
        # Код преобразует category_ids в строку
        request.category_ids = get_list_as_string(category_ids)
        request.delivery_days = str(delivery_days)
         # Код преобразует fields в строку
        request.fields = get_list_as_string(fields)
        request.keywords = keywords
        request.max_sale_price = max_sale_price
        request.min_sale_price = min_sale_price
        request.page_no = page_no
        request.page_size = page_size
        request.platform_product_type = platform_product_type
        request.ship_to_country = ship_to_country
        request.sort = sort
        request.target_currency = self._currency
        request.target_language = self._language
        request.tracking_id = self._tracking_id

        # Код отправляет запрос к API
        response = api_request(request, 'aliexpress_affiliate_hotproduct_query_response')

        # Код проверяет, есть ли результаты в ответе
        if response.current_record_count > 0:
            response.products = parse_products(response.products.product)
            return response
        else:
            # Код логирует ошибку, если продукты не найдены
           logger.error('No products found with current parameters')
           return None


    def _fetch_categories(self) -> List[model_Category | model_ChildCategory]:
        """
        Получает все доступные категории (родительские и дочерние).

        :return: Список категорий.
        :rtype: list[model_Category | model_ChildCategory]
        :raises CategoriesNotFoudException: Если категории не найдены.
        :raises Exception: В случае других ошибок.
        """
        # Код подготавливает запрос к API
        request = aliapi.rest.AliexpressAffiliateCategoryGetRequest()
        request.app_signature = self._app_signature

        # Код отправляет запрос к API
        response = api_request(request, 'aliexpress_affiliate_category_get_response')

        # Код проверяет, есть ли результаты в ответе
        if response.total_result_count > 0:
            self.categories = response.categories.category
            return self.categories
        else:
            # Код логирует ошибку, если категории не найдены
            logger.error('No categories found')
            return None

    def get_categories(self, **kwargs) -> List[model_Category | model_ChildCategory]:
        """
        Получает все доступные категории, как родительские, так и дочерние.

        :return: Список категорий.
        :rtype: list[model_Category | model_ChildCategory]
        :raises CategoriesNotFoudException: Если категории не найдены.
        :raises Exception: В случае других ошибок.
        """
        if not self.categories:
            return self._fetch_categories()
        return self.categories

    def get_parent_categories(self, use_cache=True, **kwargs) -> List[model_Category]:
        """
        Получает все доступные родительские категории.

        :param use_cache: Использовать ли кешированные категории для уменьшения запросов к API.
        :type use_cache: bool, optional
        :return: Список родительских категорий.
        :rtype: list[model_Category]
         :raises CategoriesNotFoudException: Если категории не найдены.
        :raises Exception: В случае других ошибок.
        """
        # Код проверяет, нужно ли использовать кэш или нужно обновить данные
        if not use_cache or not self.categories:
            self.get_categories()
        return filter_parent_categories(self.categories)


    def get_child_categories(self, parent_category_id: int, use_cache=True, **kwargs) -> List[model_ChildCategory]:
        """
        Получает все доступные дочерние категории для указанной родительской категории.

        :param parent_category_id: ID родительской категории.
        :type parent_category_id: int
        :param use_cache: Использовать ли кешированные категории для уменьшения запросов к API.
        :type use_cache: bool, optional
        :return: Список дочерних категорий.
        :rtype: list[model_ChildCategory]
        :raises CategoriesNotFoudException: Если категории не найдены.
        :raises Exception: В случае других ошибок.
        """
        # Код проверяет, нужно ли использовать кэш или нужно обновить данные
        if not use_cache or not self.categories:
            self.get_categories()
        return filter_child_categories(self.categories, parent_category_id)
```