Locators for Amazon Category Page
==================================

This file contains locators for the Amazon category page.  It defines various elements used for locating and interacting with the page.  The locators are structured as a JSON object.

.. code-block:: json
   :linenos:
   
   ```json
   {
     "pager": {
       "attribute": null,
       "by": "event",
       "selector": null,
       "if_list": "first",
       "use_mouse": false,
       "mandatory": true,
       "event": "scroll(5,'both')"
     },
     "product_links": {
       "attribute": "href",
       "by": "XPATH",
       "selector": "//span[@data-component-type ='s-product-image']//a",
       "if_list": "first",
       "use_mouse": false,
       "mandatory": true,
       "event": null
     }
   }
   ```

Locators
--------

Data Structure
~~~~~~~~~~~~~~

The locators are organized as a JSON object with keys representing locator types (e.g., 'pager', 'product_links') and values defining the locator details.

.. rubric:: Locator Details

The following table describes the various fields used within the JSON structure.


+-----------------+-------------------------------------------------------------------+
| Field           | Description                                                       |
+================-+-------------------------------------------------------------------+
| `attribute`     | Attribute to extract from the element.                            |
| `by`            | Method to locate the element (e.g., 'XPATH').                 |
| `selector`      | The selector used for locating the element (CSS or XPATH).    |
| `if_list`       | If the locator should select the first match (or all if not specified)|
| `use_mouse`   | If mouse interactions are necessary.                              |
| `mandatory`     | If the element is mandatory for page operation.                  |
| `event`         | If an event is triggered or needed in finding this locator.       |
+-----------------+-------------------------------------------------------------------+