Affiliated Products Generator
============================

This module provides functionality for generating affiliate products from AliExpress.
It utilizes the `AliAffiliatedProducts` class to process product data, obtain affiliate links,
and potentially save images and videos.


.. automodule:: src.suppliers.aliexpress.affiliated_products_generator
    :members:
    :undoc-members:
    :show-inheritance:


Example Usage
-------------

The following example demonstrates how to use the `AliAffiliatedProducts` class to
gather product data and handle affiliate links.


.. literalinclude:: hypotez/src/suppliers/aliexpress/_examples/affiliated_products_generator.en.md
   :language: python
   :linenos:
   :lines: 47-124
   :dedent: 4


Explanation of the Example
--------------------------

- **Creating an Instance of `AliAffiliatedProducts`**: This section creates an object of the class,
  passing required campaign parameters (name, category, language, currency).


.. literalinclude:: hypotez/src/suppliers/aliexpress/_examples/affiliated_products_generator.en.md
   :language: python
   :linenos:
   :lines: 27-33
   :dedent: 4


- **List of Product URLs or IDs**: The example shows a list of product URLs or IDs to process.
  You can provide either just the IDs or full URLs.


.. literalinclude:: hypotez/src/suppliers/aliexpress/_examples/affiliated_products_generator.en.md
   :language: python
   :linenos:
   :lines: 35-41
   :dedent: 4


- **Processing Products**: This part demonstrates calling the `process_affiliate_products` method
  to fetch affiliate links and potentially save images and videos for the listed products.


.. literalinclude:: hypotez/src/suppliers/aliexpress/_examples/affiliated_products_generator.en.md
   :language: python
   :linenos:
   :lines: 43-46
   :dedent: 4



- **Checking Results**: Finally, the example checks if any products were processed and iterates
  through the results, printing details about each product.


.. literalinclude:: hypotez/src/suppliers/aliexpress/_examples/affiliated_products_generator.en.md
   :language: python
   :linenos:
   :lines: 48-68
   :dedent: 4

This example file serves as a template for testing the functionality and can be
adapted for diverse needs.