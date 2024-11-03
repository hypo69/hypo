## \file ../src/suppliers/locator.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""Module for defining locators with various selection attributes for web elements.

This module provides the Locator class, which represents different strategies
for locating elements on a web page. It supports multiple attributes and can
be initialized from a JSON file to load predefined locator settings.
"""

from dataclasses import dataclass, field
from types import SimpleNamespace
from src import gs
from src.utils.jjson import j_loads_ns

@dataclass
class Locator:
    """Class for representing a locator with various selection attributes.

    Attributes:
        attribute (str | list | dict | list[dict]): The attribute of the web element to be located, 
            such as 'href', 'innerText', 'src', etc.
        by (str | list | dict | list[dict]): Method used to locate the element, such as 'id', 'xpath', etc.
        selector (str | list | dict | list[dict]): CSS or XPath selector string for locating the element.
        if_list (str | list | dict | list[dict]): Condition to specify which element to consider in a list, 
            e.g., 'all', 'first', 'last', 'even', 'odd'.
        use_mouse (str | list | dict | list[dict]): Specifies whether a mouse action is required, 
            such as a click action.
        mandatory (str | list | dict | list[dict]): Specifies if the locator is required for the operation.
        event (str | list | dict | list[dict]): Event that triggers interaction, 
            such as 'click()', 'hover()', 'send_message()', 'screenshot()'.
        locator_description (str | list | dict | list[dict]): Description of the locator's purpose or intended use.
    
    Example:
        ```python
        # Initialize the Locator class with a specific supplier prefix
        locator = Locator('example_supplier')

        # Access attributes after loading from a JSON file
        print(locator.attribute)  # Output could be 'href'
        print(locator.by)  # Output could be 'id' or 'xpath'
        print(locator.selector)  # Output could be '//*[@id="element_id"]'
        print(locator.if_list)  # Output could be 'first'
        ```
    """
    
    presta_fields_list: List[str] = field(default_factory=lambda: [
        'active',
        'additional_delivery_times',
        'additional_shipping_cost',
        'advanced_stock_management',
        'affiliate_short_link',
        'affiliate_summary',
        'affiliate_summary_2',
        'affiliate_text',
        'affiliate_image_large',
        'affiliate_image_medium',
        'affiliate_image_small',
        'associations',
        'available_date',
        'available_for_order',
        'available_later',
        'available_now',
        'cache_default_attribute',
        'cache_has_attachments',
        'cache_is_pack',
        'condition',
        'customizable',
        'date_add',
        'date_upd',
        'delivery_in_stock',
        'delivery_out_stock',
        'depth',
        'description',
        'description_short',
        'ean13',
        'ecotax',
        'height',
        'how_to_use',
        'specification',
        'id_category_default',
        'id_default_combination',
        'id_default_image',
        'locale',
        'id_manufacturer',
        'id_product',
        'id_shop_default',
        'id_shop',
        'id_supplier',
        'id_tax',
        'id_type_redirected',
        'indexed',
        'ingredients',
        'is_virtual',
        'isbn',
        'link_rewrite',
        'location',
        'low_stock_alert',
        'low_stock_threshold',
        'meta_description',
        'meta_keywords',
        'meta_title',
        'minimal_quantity',
        'mpn',
        'name',
        'online_only',
        'on_sale',
        'out_of_stock',
        'pack_stock_type',
        'price',
        'product_type',
        'quantity_discount',
        'redirect_type',
        'reference',
        'show_condition',
        'show_price',
        'state',
        'supplier_reference',
        'text_fields',
        'unit_price_ratio',
        'unity',
        'upc',
        'uploadable_files',
        'visibility',
        'volume',
        'weight',
        'wholesale_price',
        'width',
        'local_saved_image',
        'local_saved_video',
    ])

    def __init__(self, supplier_prefix: str):
        """Initializes a new Locator instance by loading settings from a JSON file.

        Args:
            supplier_prefix (str): The prefix identifying the supplier folder from which
                to load locator configuration files.

        Raises:
            FileNotFoundError: If the JSON file with locator definitions is not found.

        Example:
            ```python
            # Initialize with the supplier prefix
            locator = Locator("example_supplier")

            # Access the loaded attributes
            print(locator.attribute)  # Could output 'href' or another attribute
            ```
        """
        # Define the path to the locator configuration file
        locators_path = gs.path.src / 'suppliers' / supplier_prefix / 'locators' / 'product.json'
        l: SimpleNamespace = j_loads_ns(locators_path)

