rst
How to use the Product class
========================================================================================

Description
-------------------------
This code defines a Python class named `Product`.  It represents a product from AliExpress, encapsulating various attributes like price, category information, and URLs.  The class stores product details in attributes.

Execution steps
-------------------------
1. The code imports the `List` type from the `typing` module. This is used to define a list of strings for product image URLs.
2. It defines a class named `Product` with numerous attributes.  Each attribute represents a specific data point about a product, such as price, URLs, and category IDs.  The types of these attributes are specified (e.g., `str`, `int`).
3. The class `Product` stores the product information from AliExpress, making it easier to access and use this data in subsequent operations.

Usage example
-------------------------
.. code-block:: python

    from typing import List

    class Product:
        app_sale_price: str
        app_sale_price_currency: str
        commission_rate: str
        discount: str
        evaluate_rate: str
        first_level_category_id: int
        first_level_category_name: str
        lastest_volume: int
        hot_product_commission_rate: str
        lastest_volume: int
        original_price: str
        original_price_currency: str
        product_detail_url: str
        product_id: int
        product_main_image_url: str
        product_small_image_urls: List[str]
        product_title: str
        product_video_url: str
        promotion_link: str
        relevant_market_commission_rate: str
        sale_price: str
        sale_price_currency: str
        second_level_category_id: int
        second_level_category_name: str
        shop_id: int
        shop_url: str
        target_app_sale_price: str
        target_app_sale_price_currency: str
        target_original_price: str
        target_original_price_currency: str
        target_sale_price: str
        target_sale_price_currency: str


    # Example usage (assuming you have product data)
    product_data = {
        "product_id": 12345,
        "product_title": "Example Product",
        "sale_price": "10.99",
        "sale_price_currency": "USD",
        # ... other product attributes
    }

    # Create a Product object
    product = Product()
    product.product_id = product_data.get("product_id")
    product.product_title = product_data.get("product_title")
    product.sale_price = product_data.get("sale_price")
    product.sale_price_currency = product_data.get("sale_price_currency")

    # Access product information
    print(f"Product ID: {product.product_id}")
    print(f"Product Title: {product.product_title}")
    print(f"Sale Price: {product.sale_price} {product.sale_price_currency}")