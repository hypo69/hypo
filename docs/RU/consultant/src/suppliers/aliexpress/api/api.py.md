# Анализ кода модуля `api`

## Качество кода
8
- Плюсы
    - Код хорошо структурирован, с разделением на классы и функции.
    - Используются аннотации типов, что улучшает читаемость и поддержку.
    - Присутствует документация в формате docstring для большинства функций.
    - Используется кастомный логгер `src.logger.logger`.
    - Выделены кастомные исключения в отдельном файле.
    - Код разбит на логические блоки, что облегчает его понимание и модификацию.

- Минусы
    - Не везде используется `logger.error` для обработки исключений.
    - Есть использование `...` для пропуска кода, что затрудняет понимание полного потока выполнения.
    - Некоторые комментарии не соответствуют стандарту RST.
    - Есть повторяющийся код для получения и обработки данных.
    - Не хватает обработки ошибок в некоторых местах.
    - Не везде используется f-строки для форматирования строк.
    - Некоторые docstring не соответствуют стандарту.

## Рекомендации по улучшению

1.  **Импорты**:
    -   Добавить недостающие импорты, если они есть.
2.  **Обработка ошибок**:
    -   Заменить `try-except` блоки на использование `logger.error` для логирования ошибок.
    -   Убрать `...` и добавить конкретную логику обработки ошибок или возврата значений по умолчанию.
3.  **Форматирование**:
    -   Использовать f-строки для форматирования строк, где это возможно.
    -   Привести в соответствие имена переменных и функций.
    -   Дополнить docstring для всех методов и классов согласно стандартам RST.
4.  **Комментарии**:
    -   Привести все комментарии в соответствие с RST.
    -   Заменить общие фразы в комментариях на более конкретные описания действий кода.
5.  **Общие улучшения**:
    -   Удалить или заменить `...` на конкретный код.
    -   Использовать константы для повторяющихся значений.
    -   Рефакторинг повторяющегося кода.

## Оптимизированный код

```python
"""
Модуль для работы с API AliExpress.
=========================================================================================

Этот модуль предоставляет класс `AliexpressApi`, который используется для взаимодействия с AliExpress Open Platform API.
Он позволяет получать информацию о товарах, генерировать партнерские ссылки и работать с категориями товаров.

Пример использования
--------------------

Пример использования класса `AliexpressApi`:

.. code-block:: python

    api = AliexpressApi(
        key='your_api_key',
        secret='your_api_secret',
        language='en',
        currency='USD',
        tracking_id='your_tracking_id'
    )
    products = api.retrieve_product_details(product_ids=['1234567890', '0987654321'])
    print(products)
"""
# -*- coding: utf-8 -*-
# <- venv win
# ~~~~~~~~~~~~
from typing import List, Union
from pathlib import Path

from src.logger.logger import logger
# from src.utils.printer import pprint # todo remove
from src.utils.jjson import j_loads, j_loads_ns  # todo import

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
    SortBy as model_SortBy,
)

from .errors.exceptions import CategoriesNotFoudException
from .helpers.categories import filter_child_categories, filter_parent_categories
from .skd import setDefaultAppInfo
from .skd import api as aliapi
from .errors import ProductsNotFoudException, InvalidTrackingIdException
from .helpers import api_request, parse_products, get_list_as_string, get_product_ids


class AliexpressApi:
    """
    Предоставляет методы для получения информации из AliExpress, используя API credentials.

    :param key: (str) Ваш API key.
    :param secret: (str) Ваш API secret.
    :param language: (str) Код языка. По умолчанию 'EN'.
    :param currency: (str) Код валюты. По умолчанию 'USD'.
    :param tracking_id: (str) ID отслеживания для генератора ссылок. По умолчанию None.
    :param app_signature: (str) Подпись приложения. По умолчанию None.
    """

    def __init__(
        self,
        key: str,
        secret: str,
        language: model_Language,
        currency: model_Currency,
        tracking_id: str = None,
        app_signature: str = None,
        **kwargs,
    ):
        """
        Инициализирует класс AliexpressApi.

        :param key: (str) Ваш API key.
        :param secret: (str) Ваш API secret.
        :param language: (model_Language) Код языка.
        :param currency: (model_Currency) Код валюты.
        :param tracking_id: (str) ID отслеживания для генератора ссылок.
        :param app_signature: (str) Подпись приложения.
        """
        self._key = key
        self._secret = secret
        self._tracking_id = tracking_id
        self._language = language
        self._currency = currency
        self._app_signature = app_signature
        self.categories = None
        setDefaultAppInfo(self._key, self._secret)

    def retrieve_product_details(
        self,
        product_ids: str | list,
        fields: str | list = None,
        country: str = None,
        **kwargs,
    ) -> List[model_Product]:
        """
        Получает информацию о продуктах.

        :param product_ids: (str | list[str]) Один или несколько ID или ссылок на продукты.
        :param fields: (str | list[str]) Поля для включения в результаты. По умолчанию все.
        :param country: (str) Фильтр продуктов, которые могут быть отправлены в эту страну.
                       Возвращает цену в соответствии с налоговой политикой страны.
        :return: (list[model_Product]) Список продуктов.
        :raises ProductsNotFoudException: Если продукты не найдены.
        :raises InvalidArgumentException: Если аргументы не корректны.
        :raises ApiRequestException: Если произошла ошибка API запроса.
        :raises ApiRequestResponseException: Если произошла ошибка ответа API.
        """
        # код преобразует идентификаторы продуктов в строку
        product_ids = get_product_ids(product_ids)
        product_ids = get_list_as_string(product_ids)

        # код создает объект запроса для получения деталей продукта
        request = aliapi.rest.AliexpressAffiliateProductdetailGetRequest()
        request.app_signature = self._app_signature
        request.fields = get_list_as_string(fields)
        request.product_ids = product_ids
        request.country = country
        request.target_currency = self._currency.upper()
        request.target_language = self._language.upper()
        request.tracking_id = self._tracking_id

        # код отправляет запрос и обрабатывает ответ
        response = api_request(request, 'aliexpress_affiliate_productdetail_get_response')

        try:
            #  проверяем, есть ли записи в ответе
            if response.current_record_count > 0:
                # код преобразует продукты из ответа
                response = parse_products(response.products.product)
                return response
            else:
                #  логируем предупреждение, если продукты не найдены
                logger.warning('No products found with current parameters')
                return
        except Exception as ex:
             # код логирует ошибку и возвращает None
            logger.error(f'Ошибка при получении деталей продукта: {ex}', exc_info=False)
            return

    def get_affiliate_links(
        self,
        links: str | list,
        link_type: model_LinkType = model_LinkType.NORMAL,
        **kwargs,
    ) -> List[model_AffiliateLink]:
        """
        Преобразует список ссылок в партнерские ссылки.

        :param links: (str | list[str]) Одна или несколько ссылок для преобразования.
        :param link_type: (model_LinkType) Тип ссылки: NORMAL (стандартная комиссия) или HOTLINK (высокая комиссия).
                         По умолчанию NORMAL.
        :return: (list[model_AffiliateLink]) Список партнерских ссылок.
        :raises InvalidArgumentException: Если аргументы не корректны.
        :raises InvalidTrackingIdException: Если tracking_id не указан.
        :raises ProductsNotFoudException: Если продукты не найдены.
        :raises ApiRequestException: Если произошла ошибка API запроса.
        :raises ApiRequestResponseException: Если произошла ошибка ответа API.
        """
        #  проверяем, установлен ли tracking_id
        if not self._tracking_id:
             #  логируем ошибку, если tracking_id не установлен
            logger.error('The tracking id is required for affiliate links')
            return

        # код преобразует ссылки в строку
        links = get_list_as_string(links)

        # код создает объект запроса для получения партнерских ссылок
        request = aliapi.rest.AliexpressAffiliateLinkGenerateRequest()
        request.app_signature = self._app_signature
        request.source_values = links
        request.promotion_link_type = link_type
        request.tracking_id = self._tracking_id
        # ... # todo remove

        # код отправляет запрос и обрабатывает ответ
        response = api_request(request, 'aliexpress_affiliate_link_generate_response')
        #  проверяем, есть ли ответ
        if not response:
            return
        # проверяем, есть ли результаты в ответе
        if response.total_result_count > 0:
            return response.promotion_links.promotion_link
        else:
            # код логирует предупреждение, если партнерские ссылки недоступны
            logger.warning('Affiliate links not available')
            return

    def get_hotproducts(
        self,
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
        **kwargs,
    ) -> model_HotProductsResponse:
        """
        Ищет партнерские продукты с высокой комиссией.

        :param category_ids: (str | list[str]) Один или несколько ID категорий.
        :param delivery_days: (int) Расчетные дни доставки.
        :param fields: (str | list[str]) Поля для включения в результаты. По умолчанию все.
        :param keywords: (str) Поиск продуктов по ключевым словам.
        :param max_sale_price: (int) Фильтр продуктов с ценой ниже указанного значения.
                              Цены в наименьшей валютной деноминации. Например, $31.41 должно быть 3141.
        :param min_sale_price: (int) Фильтр продуктов с ценой выше указанного значения.
                              Цены в наименьшей валютной деноминации. Например, $31.41 должно быть 3141.
        :param page_no: (int) Номер страницы.
        :param page_size: (int) Количество продуктов на странице. Должно быть от 1 до 50.
        :param platform_product_type: (model_ProductType) Тип продукта платформы.
        :param ship_to_country: (str) Фильтр продуктов, которые могут быть отправлены в эту страну.
                               Возвращает цену в соответствии с налоговой политикой страны.
        :param sort: (model_SortBy) Метод сортировки.
        :return: (model_HotProductsResponse) Объект с информацией об ответе и списком продуктов.
        :raises ProductsNotFoudException: Если продукты не найдены.
        :raises ApiRequestException: Если произошла ошибка API запроса.
        :raises ApiRequestResponseException: Если произошла ошибка ответа API.
        """
        # код создает объект запроса для получения горячих продуктов
        request = aliapi.rest.AliexpressAffiliateHotproductQueryRequest()
        request.app_signature = self._app_signature
        request.category_ids = get_list_as_string(category_ids)
        request.delivery_days = str(delivery_days)
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

        # код отправляет запрос и обрабатывает ответ
        response = api_request(request, 'aliexpress_affiliate_hotproduct_query_response')

        #  проверяем, есть ли записи в ответе
        if response.current_record_count > 0:
             # код преобразует продукты из ответа
            response.products = parse_products(response.products.product)
            return response
        else:
            # код возбуждает исключение, если продукты не найдены
            raise ProductsNotFoudException('No products found with current parameters')

    def get_categories(self, **kwargs) -> List[model_Category | model_ChildCategory]:
        """
        Получает все доступные категории, как родительские, так и дочерние.

        :return: (list[model_Category | model_ChildCategory]) Список категорий.
        :raises CategoriesNotFoudException: Если категории не найдены.
        :raises ApiRequestException: Если произошла ошибка API запроса.
        :raises ApiRequestResponseException: Если произошла ошибка ответа API.
        """
        # код создает объект запроса для получения категорий
        request = aliapi.rest.AliexpressAffiliateCategoryGetRequest()
        request.app_signature = self._app_signature

         # код отправляет запрос и обрабатывает ответ
        response = api_request(request, 'aliexpress_affiliate_category_get_response')

        # проверяем, есть ли результаты в ответе
        if response.total_result_count > 0:
            # код сохраняет категории и возвращает их
            self.categories = response.categories.category
            return self.categories
        else:
             # код возбуждает исключение, если категории не найдены
            raise CategoriesNotFoudException('No categories found')

    def get_parent_categories(self, use_cache=True, **kwargs) -> List[model_Category]:
        """
        Получает все доступные родительские категории.

        :param use_cache: (bool) Использовать кэшированные категории для уменьшения количества API запросов.
        :return: (list[model_Category]) Список родительских категорий.
        :raises CategoriesNotFoudException: Если категории не найдены.
        :raises ApiRequestException: Если произошла ошибка API запроса.
        :raises ApiRequestResponseException: Если произошла ошибка ответа API.
        """
        # проверяем, нужно ли использовать кеш или если категории не загружены
        if not use_cache or not self.categories:
             #  код получает категории, если нужно обновить кеш или его нет
            self.get_categories()
        # код фильтрует и возвращает родительские категории
        return filter_parent_categories(self.categories)

    def get_child_categories(self, parent_category_id: int, use_cache=True, **kwargs) -> List[model_ChildCategory]:
        """
        Получает все доступные дочерние категории для конкретной родительской категории.

        :param parent_category_id: (int) ID родительской категории.
        :param use_cache: (bool) Использовать кэшированные категории для уменьшения количества API запросов.
        :return: (list[model_ChildCategory]) Список дочерних категорий.
        :raises CategoriesNotFoudException: Если категории не найдены.
        :raises ApiRequestException: Если произошла ошибка API запроса.
        :raises ApiRequestResponseException: Если произошла ошибка ответа API.
        """
        # проверяем, нужно ли использовать кеш или если категории не загружены
        if not use_cache or not self.categories:
             #  код получает категории, если нужно обновить кеш или его нет
            self.get_categories()
        # код фильтрует и возвращает дочерние категории
        return filter_child_categories(self.categories, parent_category_id)