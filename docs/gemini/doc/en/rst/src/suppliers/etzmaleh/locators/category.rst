Category Locator Configuration
=============================

This file defines locators for retrieving product and category links from a webpage.  It uses JSON format to specify the strategies for locating elements.


.. code-block:: json
   :linenos:

   ```json
   {
     "pager": {
       "attribute": null,
       "by": "event",
       "selector": null,
       "if_list":"first","use_mouse": false,
       "mandatory": true,
       "event": "scroll(5,\'both\')"
     },
     "product_links": {
       "attribute": "href",
       "by": "XPATH",
       "selector": "//span[@data-component-type ='s-product-image']//a",
       "if_list":"first","use_mouse": false,
       "mandatory": true,
       "event": null
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