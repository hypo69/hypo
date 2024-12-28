# Анализ кода модуля `api.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разбит на функции, что делает его более читаемым и поддерживаемым.
    - Используются аннотации типов, что улучшает понимание кода и облегчает отладку.
    - Присутствует базовая обработка ошибок с использованием `try-except` и логирование с `logger`.
    - Код использует кастомные модели данных и исключения, что способствует лучшей организации и пониманию предметной области.
    - Есть описание модуля, классов и функций с помощью docstrings.
-  Минусы
    - Не все docstrings соответствуют стандарту reStructuredText (RST), некоторые аргументы описаны не в формате Sphinx.
    - В некоторых местах используется избыточное `try-except` с последующим `return`, что можно упростить с помощью логирования и возврата значения по умолчанию.
    - В коде есть много `...`, что не очень хорошо, так как их наличие не всегда ясно
    - Не все функции имеют подробные комментарии с объяснением логики кода.
    - Отсутствует единое оформление исключений.
    - Некоторые переменные не имеют документации.

**Рекомендации по улучшению**
1.  **Документация**:
    -   Переписать все docstrings в формате RST, включая параметры, возвращаемые значения и исключения.
    -   Добавить описание ко всем переменным и атрибутам класса.

2.  **Обработка ошибок**:
    -   Избегать избыточного использования `try-except`. В большинстве случаев достаточно логировать ошибку и возвращать `None` или пустой список.
    -   Унифицировать обработку исключений, используя `logger.error` для логирования и возврата значений по умолчанию.

3.  **Логирование**:
    -   Убедиться, что все значимые ошибки и предупреждения логируются.
    -   Включить в логи сообщения об ошибках и контекст, например, значения переменных и локаторы.

4.  **Импорты**:
    -   Проверить и добавить отсутствующие импорты, если такие есть.
    -   Упорядочить импорты в соответствии со стандартом PEP8 (сначала стандартные библиотеки, потом сторонние, потом локальные).

5.  **Общие улучшения**:
    -   Избавиться от `...` в коде и заменить их на реальную логику или заглушки.
    -   Привести имена переменных и функций в соответствие с ранее обработанными файлами.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
"""
Модуль для работы с API AliExpress.
=========================================================================================

Этот модуль предоставляет класс :class:`AliexpressApi`, который используется для взаимодействия
с API AliExpress для получения информации о продуктах, партнерских ссылок и категорий.
Модуль использует SDK для работы с API AliExpress.

Пример использования
--------------------

Пример использования класса `AliexpressApi`:

.. code-block:: python

    api = AliexpressApi(
        key='your_api_key',
        secret='your_api_secret',
        language='EN',
        currency='USD',
        tracking_id='your_tracking_id'
    )
    products = api.retrieve_product_details(product_ids=['123456789', '987654321'])
"""
from typing import List, Union

from src.logger.logger import logger
#from src.utils.printer import pprint # TODO: удалить неиспользуемый импорт

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
    SortBy as model_SortBy
)

from .errors.exceptions import CategoriesNotFoudException
from .helpers.categories import filter_child_categories, filter_parent_categories
from .skd import setDefaultAppInfo
from .skd import api as aliapi
from .errors import ProductsNotFoudException, InvalidTrackingIdException
from .helpers import api_request, parse_products, get_list_as_string, get_product_ids


class AliexpressApi:
    """
    Предоставляет методы для получения информации от AliExpress, используя учетные данные API.

    :param key: Ваш API ключ.
    :type key: str
    :param secret: Ваш API секрет.
    :type secret: str
    :param language: Код языка. По умолчанию 'EN'.
    :type language: str
    :param currency: Код валюты. По умолчанию 'USD'.
    :type currency: str
    :param tracking_id: Идентификатор отслеживания для генератора ссылок. По умолчанию None.
    :type tracking_id: str, optional
    :param app_signature: Подпись приложения.
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

        :param key: API ключ.
        :type key: str
        :param secret: API секрет.
        :type secret: str
        :param language: Язык.
        :type language: model_Language
        :param currency: Валюта.
        :type currency: model_Currency
        :param tracking_id: Идентификатор отслеживания, defaults to None
        :type tracking_id: str, optional
        :param app_signature: Подпись приложения, defaults to None
        :type app_signature: str, optional
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
        product_ids: Union[str, list],
        fields: Union[str, list] = None,
        country: str = None,
        **kwargs) -> List[model_Product]:
        """
        Получает информацию о продуктах.

        :param product_ids: Один или несколько идентификаторов продуктов или ссылок.
        :type product_ids: str | list[str]
        :param fields: Поля для включения в результаты. По умолчанию все.
        :type fields: str | list[str], optional
        :param country: Фильтрует продукты, которые могут быть отправлены в эту страну. Возвращает цену
            в соответствии с налоговой политикой страны.
        :type country: str, optional
        :return: Список продуктов.
        :rtype: list[model_Product]
        :raises ProductsNotFoudException: Если продукты не найдены.
        """
        # Код преобразует идентификаторы продуктов в список
        product_ids = get_product_ids(product_ids)
        # Код преобразует список идентификаторов продуктов в строку
        product_ids = get_list_as_string(product_ids)

        # Код создает запрос для получения деталей продукта
        request = aliapi.rest.AliexpressAffiliateProductdetailGetRequest()
        request.app_signature = self._app_signature
        request.fields = get_list_as_string(fields)
        request.product_ids = product_ids
        request.country = country
        request.target_currency = self._currency.upper()
        request.target_language = self._language.upper()
        request.tracking_id = self._tracking_id

        # Код отправляет запрос и получает ответ
        response = api_request(request, 'aliexpress_affiliate_productdetail_get_response')
        try:
            # Код проверяет наличие данных в ответе
            if response.current_record_count > 0:
                # Код обрабатывает полученные данные
                response = parse_products(response.products.product)
                return response
            else:
                # Код логирует предупреждение, если продукты не найдены
                logger.warning('No products found with current parameters')
                return [] # Возвращает пустой список, если продукты не найдены
        except Exception as ex:
            # Код логирует ошибку, если при обработке произошла ошибка
            logger.error(f'Error retrieving product details: {ex}', exc_info=True)
            return [] # Возвращает пустой список в случае ошибки


    def get_affiliate_links(self,
        links: Union[str, list],
        link_type: model_LinkType = model_LinkType.NORMAL,
        **kwargs) -> List[model_AffiliateLink]:
        """
        Преобразует список ссылок в партнерские ссылки.

        :param links: Одна или несколько ссылок для преобразования.
        :type links: str | list[str]
        :param link_type: Выберите между обычной ссылкой со стандартной комиссией
            или горячей ссылкой с комиссией на горячий продукт. По умолчанию NORMAL.
        :type link_type: model_LinkType, optional
        :return: Список партнерских ссылок.
        :rtype: list[model_AffiliateLink]
        :raises InvalidTrackingIdException: Если не указан идентификатор отслеживания.
        :raises ProductsNotFoudException: Если партнерские ссылки не найдены.
        """
        # Проверяем наличие tracking_id
        if not self._tracking_id:
            logger.error('The tracking id is required for affiliate links')
            return [] # Возвращаем пустой список, если tracking_id отсутствует

        # Код преобразует список ссылок в строку
        links = get_list_as_string(links)

        # Код создает запрос для генерации партнерских ссылок
        request = aliapi.rest.AliexpressAffiliateLinkGenerateRequest()
        request.app_signature = self._app_signature
        request.source_values = links
        request.promotion_link_type = link_type
        request.tracking_id = self._tracking_id
        
        # Код отправляет запрос и получает ответ
        response = api_request(request, 'aliexpress_affiliate_link_generate_response')
        # Проверяем наличие ответа
        if not response:
            return [] # Возвращаем пустой список, если ответа нет
        # Код проверяет наличие результатов
        if response.total_result_count > 0:
            return response.promotion_links.promotion_link
        else:
            # Код логирует предупреждение если ссылки не доступны
            logger.warning('Affiliate links not available')
            return [] # Возвращаем пустой список, если ссылки не доступны


    def get_hotproducts(self,
        category_ids: Union[str, list] = None,
        delivery_days: int = None,
        fields: Union[str, list] = None,
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
        Поиск партнерских продуктов с высокой комиссией.

        :param category_ids: Один или несколько идентификаторов категорий.
        :type category_ids: str | list[str], optional
        :param delivery_days: Предполагаемые дни доставки.
        :type delivery_days: int, optional
        :param fields: Поля для включения в список результатов. По умолчанию все.
        :type fields: str | list[str], optional
        :param keywords: Поиск продуктов по ключевым словам.
        :type keywords: str, optional
        :param max_sale_price: Фильтрует продукты с ценой ниже указанного значения.
            Цены указаны в наименьшей валюте. Например, $31.41 следует указать как 3141.
        :type max_sale_price: int, optional
        :param min_sale_price: Фильтрует продукты с ценой выше указанного значения.
             Цены указаны в наименьшей валюте. Например, $31.41 следует указать как 3141.
        :type min_sale_price: int, optional
        :param page_no: Номер страницы.
        :type page_no: int, optional
        :param page_size: Количество продуктов на странице. Должно быть от 1 до 50.
        :type page_size: int, optional
        :param platform_product_type: Указать тип продукта платформы.
        :type platform_product_type: model_ProductType, optional
        :param ship_to_country: Фильтрует продукты, которые могут быть отправлены в эту страну.
            Возвращает цену в соответствии с налоговой политикой страны.
        :type ship_to_country: str, optional
        :param sort: Указывает метод сортировки.
        :type sort: model_SortBy, optional
        :return: Содержит информацию об ответе и список продуктов.
        :rtype: model_HotProductsResponse
        :raises ProductsNotFoudException: Если продукты не найдены.
        """
        # Код создает запрос для поиска горячих продуктов
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

        # Код отправляет запрос и получает ответ
        response = api_request(request, 'aliexpress_affiliate_hotproduct_query_response')

        # Код проверяет наличие результатов
        if response.current_record_count > 0:
            # Код обрабатывает полученные данные
            response.products = parse_products(response.products.product)
            return response
        else:
            # Код выбрасывает исключение если продукты не найдены
            raise ProductsNotFoudException('No products found with current parameters')


    def get_categories(self, **kwargs) -> List[Union[model_Category, model_ChildCategory]]:
        """
        Получает все доступные категории, как родительские, так и дочерние.

        :return: Список категорий.
        :rtype: list[model_Category | model_ChildCategory]
        :raises CategoriesNotFoudException: Если категории не найдены.
        """
        # Код создает запрос для получения категорий
        request = aliapi.rest.AliexpressAffiliateCategoryGetRequest()
        request.app_signature = self._app_signature

        # Код отправляет запрос и получает ответ
        response = api_request(request, 'aliexpress_affiliate_category_get_response')

        # Код проверяет наличие категорий в ответе
        if response.total_result_count > 0:
            # Код сохраняет категории и возвращает их
            self.categories = response.categories.category
            return self.categories
        else:
            # Код выбрасывает исключение если категории не найдены
            raise CategoriesNotFoudException('No categories found')


    def get_parent_categories(self, use_cache=True, **kwargs) -> List[model_Category]:
        """
        Получает все доступные родительские категории.

        :param use_cache: Использует кэшированные категории для уменьшения запросов к API.
        :type use_cache: bool, optional
        :return: Список родительских категорий.
        :rtype: list[model_Category]
        :raises CategoriesNotFoudException: Если категории не найдены.
        """
        # Код проверяет нужно ли использовать кэш или нужно получить категории
        if not use_cache or not self.categories:
            self.get_categories()
        # Код фильтрует родительские категории и возвращает их
        return filter_parent_categories(self.categories)


    def get_child_categories(self, parent_category_id: int, use_cache=True, **kwargs) -> List[model_ChildCategory]:
        """
        Получает все доступные дочерние категории для конкретной родительской категории.

        :param parent_category_id: Идентификатор родительской категории.
        :type parent_category_id: int
        :param use_cache: Использует кэшированные категории для уменьшения запросов к API.
        :type use_cache: bool, optional
        :return: Список дочерних категорий.
        :rtype: list[model_ChildCategory]
        :raises CategoriesNotFoudException: Если категории не найдены.
        """
        # Код проверяет нужно ли использовать кэш или нужно получить категории
        if not use_cache or not self.categories:
            self.get_categories()
        # Код фильтрует дочерние категории и возвращает их
        return filter_child_categories(self.categories, parent_category_id)
```