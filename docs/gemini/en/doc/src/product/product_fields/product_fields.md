# Module: hypotez/src/product/product_fields/product_fields.py

## Overview

This module defines the `ProductFields` class, which encapsulates data for product fields in a PrestaShop database. It provides methods to load, access, and set various product attributes, including details from the `ps_product` and `ps_product_lang` tables. The module handles multilingual data and integrates with the logging system.

## Table of Contents

* [Overview](#overview)
* [Classes](#classes)
    * [ProductFields](#productfields)
        * [Methods](#methods)
            * [`__init__`](#init)
            * [`_load_product_fields_list`](#load_product_fields_list)
            * [`_payload`](#payload)
            * [`associations`](#associations)
            * [`id_product`](#id_product)
            * [`id_supplier`](#id_supplier)
            * [`id_manufacturer`](#id_manufacturer)
            * [`id_category_default`](#id_category_default)
            * [`id_shop_default`](#id_shop_default)
            * [`id_shop`](#id_shop)
            * [`id_tax`](#id_tax)
            * ... (Many more methods)

## Classes

### `ProductFields`

**Description**: A class representing product fields in the PrestaShop format, designed to handle data access and manipulation, particularly for multilingual product attributes.


**Methods**

#### `__init__`

**Description**: Initializes the `ProductFields` object, loading product field lists and default values from files.

**Raises**:
* `ProductFieldException`: If there's an error loading default values from the JSON file.


#### `_load_product_fields_list`

**Description**: Loads a list of product field names from a text file.

**Returns**:
- `List[str]`: A list of product field names.


#### `_payload`

**Description**: Loads default values for product fields from a JSON file.

**Returns**:
- `bool`: `True` if loading was successful, `False` otherwise.


#### `associations`

**Description**: Returns the product associations dictionary.

**Returns**:
- `Optional[Dict]`: The associations dictionary or `None` if not available.


#### `id_product`

**Description**: Returns or sets the `id_product` of the product.

**Returns**:
- `Optional[int]`: The `id_product` or `None` if not available.


#### `id_supplier`

**Description**: Returns or sets the `id_supplier` of the product.

**Returns**:
- `bool`: True on success, False on failure.


#### `id_manufacturer`

**Description**: Returns or sets the `id_manufacturer` (brand) of the product.

**Returns**:
- `Optional[int]`: The `id_manufacturer` or `None`.


#### `id_category_default`

**Description**: Returns or sets the default category `id_category_default` for the product.


#### `id_shop_default`

**Description**: Returns or sets the default shop `id_shop_default` for the product.


#### `id_shop`

**Description**: Returns or sets the shop `id_shop` for the product.



#### `id_tax`

**Description**: Returns or sets the tax rule `id_tax`.



#### `on_sale`

**Description**: Returns or sets the `on_sale` flag (0 or 1).


#### `online_only`

**Description**: Returns or sets the `online_only` flag.



#### `ean13`

**Description**: Returns or sets the `ean13` value.


#### `isbn`

**Description**: Returns or sets the `isbn` value.


#### `upc`

**Description**: Returns or sets the `upc` value.


#### `mpn`

**Description**: Returns or sets the `mpn` value.


#### `ecotax`

**Description**: Returns or sets the `ecotax` value.



#### `minimal_quantity`

**Description**: Returns or sets the `minimal_quantity` value.



#### `low_stock_threshold`

**Description**: Returns or sets the `low_stock_threshold` value.


#### `low_stock_alert`

**Description**: Returns or sets the `low_stock_alert` value.



#### `price`

**Description**: Returns or sets the `price` value.


#### `wholesale_price`

**Description**: Returns or sets the `wholesale_price` value.


#### `unity`

**Description**: Returns or sets the `unity` value.



#### `unit_price_ratio`

**Description**: Returns or sets the `unit_price_ratio` value.


#### `additional_shipping_cost`

**Description**: Returns or sets the `additional_shipping_cost` value.


#### `reference`

**Description**: Returns or sets the `reference` value.


#### `supplier_reference`

**Description**: Returns or sets the `supplier_reference` value.


#### `location`

**Description**: Returns or sets the `location` value.


#### `width`

**Description**: Returns or sets the `width` value.


#### `height`

**Description**: Returns or sets the `height` value.


#### `depth`

**Description**: Returns or sets the `depth` value.


#### `weight`

**Description**: Returns or sets the `weight` value.


#### `volume`

**Description**: Returns or sets the `volume` value.



#### `out_of_stock`

**Description**: Returns or sets the `out_of_stock` value.



#### `additional_delivery_times`

**Description**: Returns or sets the `additional_delivery_times` value.


#### `quantity_discount`

**Description**: Returns or sets the `quantity_discount` value.



#### `customizable`

**Description**: Returns or sets the `customizable` value.


#### `uploadable_files`

**Description**: Returns or sets the `uploadable_files` value.


#### `text_fields`

**Description**: Returns or sets the `text_fields` value.


#### `active`

**Description**: Returns or sets the `active` flag (0 or 1).


#### `redirect_type`

**Description**: Returns or sets the `redirect_type` value.


#### `id_type_redirected`

**Description**: Returns or sets the `id_type_redirected` value.



#### `available_for_order`

**Description**: Returns or sets the `available_for_order` value.



#### `available_date`

**Description**: Returns or sets the `available_date` value.



#### `show_condition`

**Description**: Returns or sets the `show_condition` value.


#### `condition`

**Description**: Returns or sets the `condition` value (e.g., 'new', 'used').


#### `show_price`

**Description**: Returns or sets the `show_price` value.



#### `indexed`

**Description**: Returns or sets the `indexed` value.



#### `visibility`

**Description**: Returns or sets the `visibility` value.



#### `cache_is_pack`

**Description**: Returns or sets the `cache_is_pack` value.



#### `cache_has_attachments`

**Description**: Returns or sets the `cache_has_attachments` value.



#### `is_virtual`

**Description**: Returns or sets the `is_virtual` value.



#### `cache_default_attribute`

**Description**: Returns or sets the `cache_default_attribute` value.



#### `date_add`

**Description**: Returns or sets the `date_add` value.


#### `date_upd`

**Description**: Returns or sets the `date_upd` value.



#### `advanced_stock_management`

**Description**: Returns or sets the `advanced_stock_management` value.



#### `pack_stock_type`

**Description**: Returns or sets the `pack_stock_type` value.


#### `state`

**Description**: Returns or sets the `state` value.



#### `product_type`

**Description**: Returns or sets the `product_type` value.



#### `link_to_video`

**Description**: Returns or sets the `link_to_video` value.


#### `images_urls`

**Description**: Returns or sets the list of image URLs.



#### `local_saved_image`

**Description**: Returns or sets the local path to a saved image.


#### `local_saved_video`

**Description**: Returns or sets the local path to a saved video.


#### `position_in_category`

**Description**: Returns or sets the `position_in_category` value.



#### `page_lang`

**Description**: Returns or sets the language code for the page.


#### `description`, `description_short`, `link_rewrite`, `meta_description`, `meta_keywords`, `meta_title`, `name`, `available_now`, `available_later`, `delivery_in_stock`, `delivery_out_stock`, `delivery_additional_message`, `affiliate_short_link`, `affiliate_text`, `affiliate_summary`, `affiliate_summary_2`, `affiliate_image_small`, `affiliate_image_medium`, `affiliate_image_large`, `ingredients`, `how_to_use`, `specification`, `id_default_image`


(These methods have similar docstrings, returning or setting multilingual values for the corresponding `ps_product_lang` fields)