# Module: hypotez/src/product/product_fields/product_fields.py

## Overview

This module defines the `ProductFields` class for managing product data in the PrestaShop format.  It provides methods to load, access, and set various product attributes, mirroring the structure of PrestaShop tables (`ps_product`, `ps_product_lang`, etc.).  The class includes detailed documentation for each property (getter/setter) which is used to interact with the PrestaShop database.


## Classes

### `ProductFields`

**Description**: This class encapsulates product field data, allowing for structured interaction with PrestaShop. It loads product field definitions from a file, and provides methods to access and modify the fields.


**Functions**:


### `__init__`

**Description**: Initializes the `ProductFields` class. Loads product fields from a file, and initializes necessary dictionaries.

**Raises**:
- `ProductFieldException`: if an error occurs during loading.


### `_load_product_fields_list`

**Description**: Loads a list of product field names from a text file.

**Returns**:
- `List[str]`: A list of product field names.

**Raises**:
- `ProductFieldException`: if the file is not found or cannot be read.


### `_payload`

**Description**: Loads default product field values from a JSON file.

**Returns**:
- `bool`: `True` if loading was successful, `False` otherwise.

**Raises**:
- `ProductFieldException`: if the JSON file is not found or cannot be parsed.


### `associations`

**Description**:

**Property**: Returns the associations dictionary for the product.

**Setter**: Sets the associations dictionary for the product.


### `id_product`

**Description**: Accessor/modifier for the product ID.

**Property**: Returns the product ID.

**Setter**: Sets the product ID. Includes detailed information about how product IDs are handled in PrestaShop, differentiating between new and existing products.


### `id_supplier`

**Description**: Accessor/modifier for the supplier ID.

**Property**: Returns the supplier ID for the product.

**Setter**: Sets the supplier ID.  Includes details about linking products to suppliers.


### `id_manufacturer`

**Description**: Accessor/modifier for the manufacturer ID.

**Property**: Returns the manufacturer ID.

**Setter**: Sets the manufacturer ID. Provides details on how manufacturer IDs can be specified either by ID or name.


### `id_category_default`

**Description**: Accessor/modifier for the default category ID.

**Property**: Returns the default category ID.

**Setter**: Sets the default category ID.  Contains details about linking to the primary category.


### `additional_categories`

**Description**: Property and setter for additional categories of the product.

**Property**: Returns the dictionary of additional categories.

**Setter**: Sets the additional categories dictionary, including handling of multiple categories.


### `id_shop_default`

**Description**: Accessor/modifier for the default shop ID.

**Property**: Returns the default shop ID.

**Setter**: Sets the default shop ID, handling potential `ProductFieldException`.


### `id_shop`

**Description**: Accessor/modifier for the shop ID (similar to `id_shop_default`).

**Property**: Returns the shop ID.

**Setter**: Sets the shop ID.


### `id_tax`

**Description**: Accessor/modifier for the tax ID.

**Property**: Returns the tax ID.

**Setter**: Sets the tax ID, with specific examples of tax rules in PrestaShop context (e.g., Israel's tax rule 13).


### `on_sale`

**Description**: Accessor/modifier for the on-sale flag.

**Property**: Returns the on-sale flag.

**Setter**: Sets the on-sale flag.


### `online_only`

**Description**: Accessor/modifier for the online-only flag.

**Property**: Returns the online-only flag.

**Setter**: Sets the online-only flag.


### `ean13`, `isbn`, `upc`, `mpn`, `ecotax`

**Description**: Accessor/modifier for various product identifiers.


**Property**: Returns the value.

**Setter**: Sets the value, handling potential errors, and normalizing input for validation.



### `quantity`, `minimal_quantity`, `low_stock_threshold`, `low_stock_alert`, `price`, `wholesale_price`, `unity`, `unit_price_ratio`, `additional_shipping_cost`, `reference`, `supplier_reference`, `location`, `width`, `height`, `depth`, `weight`, `volume`, `out_of_stock`, `additional_delivery_times`, `quantity_discount`, `customizable`, `uploadable_files`, `text_fields`, `active`


**Description**: Accessor/modifier for various product attributes.


**Property**: Returns the value.

**Setter**: Sets the value, including data normalization and error handling.


### `redirect_type`

**Description**: Property and setter for the product redirect type.

**Property**: Returns the redirect type.

**Setter**: Sets the redirect type, using an `EnumRedirect` for clarity and validation.  Includes comprehensive documentation about different HTTP redirect types (301, 302), their implications for SEO, and how to handle each type in your application.

### `id_type_redirected`, `available_for_order`, `available_date`, `show_condition`, `condition`, `show_price`, `indexed`, `visibility`, `cache_is_pack`, `cache_has_attachments`, `is_virtual`, `cache_default_attribute`, `date_add`, `date_upd`, `advanced_stock_management`, `pack_stock_type`, `state`, `product_type`

**Description**: Properties and setters for advanced product attributes.


**Property**: Returns the value.

**Setter**: Sets the value, including validation and error handling.  These entries are followed by extensive documentation describing each attribute and its meaning in the context of PrestaShop.

### `description`, `description_short`, `link_rewrite`, `meta_description`, `meta_keywords`, `meta_title`, `name`, `available_now`, `available_later`, `delivery_in_stock`, `delivery_out_stock`, `delivery_additional_message`, `affiliate_short_link`, `affiliate_text`, `affiliate_summary`, `affiliate_summary_2`, `affiliate_image_small`, `affiliate_image_medium`, `affiliate_image_large`, `ingredients`, `specification`, `how_to_use`, `id_default_image`, `link_to_video`, `images_urls`, `local_saved_image`, `local_saved_video`, `position_in_category`

**Description**: Accessor/modifier for multi-lingual product descriptions and other related fields. Note the use of nested dictionaries in the `setter` to support proper handling of multi-language values for PrestaShop.


**Property**: Returns the value.

**Setter**: Sets the value, handling multi-language values. This section has detailed documentation specific to handling multilingual fields (`ps_product_lang`) within PrestaShop.


### `page_lang`

**Description**: Property and setter for the page language.

**Property**: Returns the current page language.

**Setter**: Sets the page language.


## Functions (Other than class methods)

(None found in the provided code)