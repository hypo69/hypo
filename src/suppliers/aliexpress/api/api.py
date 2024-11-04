""" AliExpress API wrapper for Python

A simple Python wrapper for the AliExpress Open Platform API. This module allows
to get product information and affiliate links from AliExpress using the official
API in an easier way.
"""
...
## \file src/suppliers/aliexpress/api/api.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
...

from typing import List, Union

from src.logger import logger
from src.utils import pprint

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
    """Provides methods to get information from AliExpress using your API credentials.

    @param key (str): Your API key.
    @param secret (str): Your API secret.
    @param language (str): Language code. Defaults to EN.
    @param currency (str): Currency code. Defaults to USD.
    @param tracking_id (str): The tracking id for link generator. Defaults to None.
    """

    def __init__(self,
        key: str,
        secret: str,
        language: model_Language,
        currency: model_Currency,
        tracking_id: str = None,
        app_signature: str = None,
        **kwargs):
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
        """ Get products information.

        Args:
            product_ids (``str | list[str]``): One or more links or product IDs.
            fields (``str | list[str]``): The fields to include in the results. Defaults to all.
            country (``str``): Filter products that can be sent to that country. Returns the price
                according to the country's tax rate policy.

        Returns:
            ``list[model_Product]``: A list of products.

        Raises:
            ``ProductsNotFoudException``
            ``InvalidArgumentException``
            ``ApiRequestException``
            ``ApiRequestResponseException``
        """
        product_ids = get_product_ids(product_ids)
        product_ids = get_list_as_string(product_ids)

        request = aliapi.rest.AliexpressAffiliateProductdetailGetRequest()
        request.app_signature = self._app_signature
        request.fields = get_list_as_string(fields)
        request.product_ids = product_ids
        request.country = country
        request.target_currency = self._currency.upper()
        request.target_language = self._language.upper()
        request.tracking_id = self._tracking_id

        response = api_request(request, 'aliexpress_affiliate_productdetail_get_response')
        try:
            if response.current_record_count > 0:
                response = parse_products(response.products.product)
                return response
            else:
                #raise ProductsNotFoudException('No products found with current parameters')
                logger.warning('No products found with current parameters')
                ...
                return
        except Exception as ex:
            logger.error(ex, exc_info=False)
            ...
            return


    def get_affiliate_links(self,
        links: str | list,
        link_type: model_LinkType = model_LinkType.NORMAL,
        **kwargs) -> List[model_AffiliateLink]:
        """ Converts a list of links in affiliate links.
        Args:
            links (``str | list[str]``): One or more links to convert.
            link_type (``model_LinkType``): Choose between normal link with standard commission
                or hot link with hot product commission. Defaults to NORMAL.
                @code
                link_type: model_LinkType = model_LinkType.HOTLINK
                @endcode

        Returns:
            ``list[model_AffiliateLink]``: A list containing the affiliate links.

        Raises:
            ``InvalidArgumentException``
            ``InvalidTrackingIdException``
            ``ProductsNotFoudException``
            ``ApiRequestException``
            ``ApiRequestResponseException``
        """
        if not self._tracking_id:
            #raise InvalidTrackingIdException('The tracking id is required for affiliate links')
            logger.error('The tracking id is required for affiliate links')
            return

        links = get_list_as_string(links)

        request = aliapi.rest.AliexpressAffiliateLinkGenerateRequest()
        request.app_signature = self._app_signature
        request.source_values = links
        request.promotion_link_type = link_type
        request.tracking_id = self._tracking_id
        ...
        response = api_request(request, 'aliexpress_affiliate_link_generate_response')
        if not response:
            return 
        if response.total_result_count > 0:
            return response.promotion_links.promotion_link
        else:
            #raise ProductsNotFoudException('Affiliate links not available')
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
        """Search for affiliated products with high commission.

        Args:
            category_ids (``str | list[str]``): One or more category IDs.
            delivery_days (``int``): Estimated delivery days.
            fields (``str | list[str]``): The fields to include in the results list. Defaults to all.
            keywords (``str``): Search products based on keywords.
            max_sale_price (``int``): Filters products with price below the specified value.
                Prices appear in lowest currency denomination. So $31.41 should be 3141.
            min_sale_price (``int``): Filters products with price above the specified value.
                Prices appear in lowest currency denomination. So $31.41 should be 3141.
            page_no (``int``):
            page_size (``int``): Products on each page. Should be between 1 and 50.
            platform_product_type (``model_ProductType``): Specify platform product type.
            ship_to_country (``str``): Filter products that can be sent to that country.
                Returns the price according to the country's tax rate policy.
            sort (``model_SortBy``): Specifies the sort method.

        Returns:
            ``model_HotProductsResponse``: Contains response information and the list of products.

        Raises:
            ``ProductsNotFoudException``
            ``ApiRequestException``
            ``ApiRequestResponseException``
        """
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

        response = api_request(request, 'aliexpress_affiliate_hotproduct_query_response')

        if response.current_record_count > 0:
            response.products = parse_products(response.products.product)
            return response
        else:
            raise ProductsNotFoudException('No products found with current parameters')


    def get_categories(self, **kwargs) -> List[model_Category | model_ChildCategory]:
        """Get all available categories, both parent and child.

        Returns:
            ``list[model_Category | model_ChildCategory]``: A list of categories.

        Raises:
            ``CategoriesNotFoudException``
            ``ApiRequestException``
            ``ApiRequestResponseException``
        """
        request = aliapi.rest.AliexpressAffiliateCategoryGetRequest()
        request.app_signature = self._app_signature

        response = api_request(request, 'aliexpress_affiliate_category_get_response')

        if response.total_result_count > 0:
            self.categories = response.categories.category
            return self.categories
        else:
            raise CategoriesNotFoudException('No categories found')


    def get_parent_categories(self, use_cache=True, **kwargs) -> List[model_Category]:
        """Get all available parent categories.

        Args:
            use_cache (``bool``): Uses cached categories to reduce API requests.

        Returns:
            ``list[model_Category]``: A list of parent categories.

        Raises:
            ``CategoriesNotFoudException``
            ``ApiRequestException``
            ``ApiRequestResponseException``
        """
        if not use_cache or not self.categories:
            self.get_categories()
        return filter_parent_categories(self.categories)


    def get_child_categories(self, parent_category_id: int, use_cache=True, **kwargs) -> List[model_ChildCategory]:
        """Get all available child categories for a specific parent category.

        Args:
            parent_category_id (``int``): The parent category id.
            use_cache (``bool``): Uses cached categories to reduce API requests.

        Returns:
            ``list[model_ChildCategory]``: A list of child categories.

        Raises:
            ``CategoriesNotFoudException``
            ``ApiRequestException``
            ``ApiRequestResponseException``
        """
        if not use_cache or not self.categories:
            self.get_categories()
        return filter_child_categories(self.categories, parent_category_id)