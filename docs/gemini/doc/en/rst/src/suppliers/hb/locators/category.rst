Category Locator Configuration
=============================

This file defines the locators for retrieving product links, pagination, and category links from a web page.  It utilizes XPath selectors for element identification.

.. code-block:: json
   :linenos:

   ```json
   {
     "product_links": {
       "attribute": "href",
       "by": "XPATH",
       "selector": "//h3[@class = 'post-title']//a",
       "if_list": "first",
       "use_mouse": false,
       "mandatory": true,
       "event": false,
       "locator_description": "Список ссылок на товары со страницы категории"
     },
     "pagination": {
       "<-": {
         "attribute": false,
         "by": "XPATH",
         "selector": "//ul[@class='pagination']",
         "event": "click()",
         "mandatory": false,
         "locator_description": ""
       }
     },
     "categories_links": {
       "attribute": { "text": "href" },
       "by": "XPATH",
       "selector": "//a[contains(@class, 'menu-item')]",
       "event": false,
       "mandatory": false,
       "locator_description": ""
     }
   }
   ```

Locators
--------

.. automodule:: hypotez.src.suppliers.hb.locators.category
    :members:
    :undoc-members:
    :show-inheritance: