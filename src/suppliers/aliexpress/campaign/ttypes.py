""" Определение типов `campaign`, `category`, `product` """
## \file ../src/suppliers/aliexpress/campaign/ttypes.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

from types import SimpleNamespace
from typing import List, TypedDict, Optional

class ProductType(TypedDict):
    product_id: Optional[int]
    app_sale_price: Optional[float]
    original_price: Optional[float]
    sale_price: Optional[float]
    discount: Optional[float]
    product_main_image_url: Optional[str]
    local_saved_image: Optional[str]
    product_small_image_urls: Optional[List[str]]
    product_video_url: Optional[str]
    local_saved_video: Optional[str]
    first_level_category_id: Optional[int]
    first_level_category_name: Optional[str]
    second_level_category_id: Optional[int]
    second_level_category_name: Optional[str]
    target_sale_price: Optional[float]
    target_sale_price_currency: Optional[str]
    target_app_sale_price_currency: Optional[str]
    target_original_price_currency: Optional[str]
    original_price_currency: Optional[str]
    product_title: Optional[str]
    evaluate_rate: Optional[float]
    promotion_link: Optional[str]
    shop_url: Optional[str]
    shop_id: Optional[int]
    tags: Optional[List[str]]

class CampaignType(TypedDict):
    name: Optional[str]
    title: Optional[str]
    language: Optional[str]
    currency: Optional[str]
    category: SimpleNamespace  # Можно детализировать, но тут просто ссылка на SimpleNamespace

class CategoryType(TypedDict):
    name: Optional[str]
    tags: Optional[List[str]]
    products: List[SimpleNamespace]
    products_count: int

types = SimpleNamespace(
    product=SimpleNamespace(**{key: None for key in ProductType.__annotations__}),
    campaign=SimpleNamespace(
        name=None,
        title=None,
        language=None,
        currency=None,
        category=SimpleNamespace(
            name=None,
            tags=None,
            products=[],
            products_count=0
        )
    ),
    category=SimpleNamespace(
        name=None,
        tags=None,
        products=[],
        products_count=0
    )
)

