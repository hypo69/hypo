Affiliated Products Generator
============================

.. automodule:: src.suppliers.aliexpress.affiliated_products_generator
   :members:
   :undoc-members:
   :show-inheritance:

Example Usage
------------

This file demonstrates how to use the `AliAffiliatedProducts` class to collect product data and process affiliate links.

.. code-block:: python
   :linenos:

   from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts

   def main():
       # Set campaign parameters
       campaign_name = "summer_sale_2024"
       campaign_category = "electronics"  # Can be None if category is not needed
       language = "EN"  # Campaign language
       currency = "USD"  # Campaign currency

       # Create an instance of AliAffiliatedProducts
       parser = AliAffiliatedProducts(
           campaign_name,
           campaign_category,
           language,
           currency
       )

       # Example of product URLs or IDs
       prod_urls = [
           '123',
           'https://www.aliexpress.com/item/123.html',
           '456',
           'https://www.aliexpress.com/item/456.html',
       ]

       # Process products and get a list of products with affiliate links
       products = parser.process_affiliate_products(prod_urls)

       # Check the results
       if products:
           print(f"Received {len(products)} affiliate products.")
           for product in products:
               print(f"Product ID: {product.product_id}")
               print(f"Affiliate link: {product.promotion_link}")
               print(f"Local image path: {product.local_saved_image}")
               if product.local_saved_video:
                   print(f"Local video path: {product.local_saved_video}")
               print()
       else:
           print("Failed to get affiliate products.")

   if __name__ == "__main__":
       main()


Explanation
-----------

- **Creating an `AliAffiliatedProducts` instance:**
  .. code-block:: python
     :linenos:
     
     parser = AliAffiliatedProducts(
         campaign_name,
         campaign_category,
         language,
         currency
     )

  Here, we create an `AliAffiliatedProducts` object, passing the campaign parameters.

- **List of product URLs or IDs:**
  .. code-block:: python
     :linenos:

     prod_urls = [
         '123',
         'https://www.aliexpress.com/item/123.html',
         '456',
         'https://www.aliexpress.com/item/456.html',
     ]

  This example shows a list of products. You can specify either IDs or full URLs.


- **Processing products:**
  .. code-block:: python
     :linenos:

     products = parser.process_affiliate_products(prod_urls)

  We call the `process_affiliate_products` method, which handles product processing, obtaining affiliate links, and saving images and videos.

- **Checking results:**
  .. code-block:: python
     :linenos:

     if products:
         print(f"Received {len(products)} affiliate products.")
         for product in products:
             print(f"Product ID: {product.product_id}")
             print(f"Affiliate link: {product.promotion_link}")
             print(f"Local image path: {product.local_saved_image}")
             if product.local_saved_video:
                 print(f"Local video path: {product.local_saved_video}")
             print()
     else:
         print("Failed to get affiliate products.")

  Here, we check for processed products and print information about each product.


This example demonstrates basic usage of the `AliAffiliatedProducts` class and its methods. You can adapt it to your needs and add more functionality if necessary.