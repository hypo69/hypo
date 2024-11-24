Category Locator Configuration
=============================

This file defines the configuration for locating category links on a website.  It specifies the attributes, selectors, and other parameters for finding both product and category links.

Product Links
------------

^ Product Link Locator
~~~~

.. code-block:: json
   :linenos:

   {
     "product_links": {
       "attribute": "href",
       "by": "XPATH",
       "selector": "//a[contains(@class,\'image-link\')]",
       "if_list":"first",
       "use_mouse": false,
       "mandatory": true,
       "event": false
     }
   }


Category Links
-------------

^ Category Link Locator
~~~~

.. code-block:: json
   :linenos:

   {
     "categories_links": {
       "attribute": { "text": "href" },
       "by": "XPATH",
       "selector": "//nav[contains(@class, \'site-navigation\')]//a",
       "event": false,
       "mandatory": false,
       "locator_description": ""
     }
   }