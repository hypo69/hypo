Affiliated Products Generator
============================

.. automodule:: hypotez.src.suppliers.aliexpress.affiliated_products_generator
    :members:
    :undoc-members:
    :show-inheritance:


Overview
--------

This module contains the `AliAffiliatedProducts` class, responsible for generating complete product data from the AliExpress Affiliate API.  It retrieves product information, including affiliate links, images, and videos, and saves this data locally.  The class builds upon the `AliApi` class.


Imports and Dependencies
-----------------------

The following libraries and modules are imported:

- Standard Libraries: `asyncio`, `itertools`, `math`, `pathlib`, `typing`, `types`, `urllib.parse`
- External Libraries: `src`, `src.suppliers.aliexpress`, `src.suppliers.aliexpress.affiliate_links_shortener_via_webdriver`, `src.suppliers.aliexpress.utils.extract_product_id`, `src.suppliers.aliexpress.utils.set_full_https`, `src.utils.convertor.csv2json`, `src.utils`, `src.utils.file`, `src.logger`


`AliAffiliatedProducts` Class
----------------------------

.. autoclass:: hypotez.src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts
    :members:
    :undoc-members:
    :show-inheritance:

    
    Methods
    ~~~~~~~

    .. automethod:: hypotez.src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts.process_affiliate_products
        :noindex:
    
    .. automethod:: hypotez.src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts.delete_product
        :noindex:


Class Attributes
~~~~~~~~~~~~~~~

The `AliAffiliatedProducts` class has the following attributes:


.. autoattribute:: hypotez.src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts.campaign_name
.. autoattribute:: hypotez.src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts.campaign_category
.. autoattribute:: hypotez.src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts.campaign_path
.. autoattribute:: hypotez.src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts.language
.. autoattribute:: hypotez.src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts.currency
.. autoattribute:: hypotez.src.suppliers.aliexpress.affiliated_products_generator.AliAffiliatedProducts.locale


Function Details (Inline)
-------------------------

The following provides a more detailed description of the `process_affiliate_products` and `delete_product` methods, including parameter details and functionality:

**`process_affiliate_products`**

*   Processes a list of URLs and returns a list of `SimpleNamespace` objects representing products with affiliate links and saved media.
*   Fetches affiliate links, retrieves product details, saves images and videos locally.
*   Handles cases where no affiliate link is found for a particular product.

**`delete_product`**

*   Removes a product from the processed data that lacks an affiliate link.
*   Saves the updated list to the `sources.txt` file within the campaign directory.


Example Usage (from Docstring)
------------------------------

The example usage within the class docstring demonstrates how to create an instance of `AliAffiliatedProducts` and use its methods to process a list of product URLs. This is crucial for understanding the intended usage pattern.


Further Considerations
---------------------

- **Error Handling**: The code includes some error handling, but more robust error handling is recommended to gracefully manage various issues (e.g., network problems, invalid URLs).
- **Testing**:  Thorough unit tests should be implemented to cover various scenarios, such as successful processing, no affiliate links, and no products returned.
- **Asynchronous Operations**: For high volumes of products, asynchronous operations (`asyncio`) can significantly improve processing time.
- **Documentation**: Add detailed documentation for all private methods.
- **Data Validation**: Implement checks to ensure data integrity and consistency.