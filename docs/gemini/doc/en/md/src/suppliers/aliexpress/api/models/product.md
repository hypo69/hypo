# Product Model

## Overview

This module defines the `Product` class, representing product information scraped from AliExpress.  It contains various attributes reflecting product details, prices, categories, and more.


## Table of Contents

* [Product Class](#product-class)


## Product Class

### `Product`

**Description**: This class encapsulates the data structure for a product from AliExpress.  It stores attributes like product IDs, prices, images, and URLs related to the product.

**Attributes**:

* `app_sale_price`: Application sale price.
* `app_sale_price_currency`: Currency of the application sale price.
* `commission_rate`: Commission rate.
* `discount`: Discount applied to the product.
* `evaluate_rate`: Evaluation rate.
* `first_level_category_id`: ID of the first-level product category.
* `first_level_category_name`: Name of the first-level product category.
* `lastest_volume`: Latest product volume.
* `hot_product_commission_rate`: Commission rate for hot products (potentially).
* `lastest_volume`: Latest product volume. (Duplicate, likely a typo in the original code.)
* `original_price`: Original price.
* `original_price_currency`: Currency of the original price.
* `product_detail_url`: URL for detailed product information.
* `product_id`: Unique identifier for the product.
* `product_main_image_url`: URL for the main product image.
* `product_small_image_urls`: List of URLs for small product images.
* `product_title`: Title of the product.
* `product_video_url`: URL for any product video.
* `promotion_link`: URL for any product promotion.
* `relevant_market_commission_rate`: Commission rate for related market products.
* `sale_price`: Sale price.
* `sale_price_currency`: Currency of the sale price.
* `second_level_category_id`: ID of the second-level product category.
* `second_level_category_name`: Name of the second-level product category.
* `shop_id`: Unique identifier for the shop selling the product.
* `shop_url`: URL for the shop selling the product.
* `target_app_sale_price`: Target application sale price.
* `target_app_sale_price_currency`: Currency of the target application sale price.
* `target_original_price`: Target original price.
* `target_original_price_currency`: Currency of the target original price.
* `target_sale_price`: Target sale price.
* `target_sale_price_currency`: Currency of the target sale price.


**Note:**  The presence of `lastest_volume` twice is likely a copy/paste error in the original Python code. This documentation reflects the identified duplicate.  Also, some attributes might require further clarification regarding their precise meaning from the source code's context.