aliexpress/locators/from_mail.json
==================================

This file defines a JSON configuration for locating product blocks on AliExpress
within a deal page. It's tailored for locating elements from an email-derived page.

Product Blocks
-------------

.. code-block:: json
   :lineno-start: 1
   :emphasize-lines: 2, 3, 5, 6, 8, 10, 12

   ```json
   {
     "product_blocks": {
       "attribute": null,
       "by": "XPATH",
       "selector": "//td[div[contains(@class, '-item-card') and not(contains(@class, 'item-card-text'))]]",
       "if_list":"first",
       "use_mouse": false,
       "mandatory": false,
       "event": "",
       "locator_description": "Товары со страницы deals, котору я делаю из почтовой рассылки. "
     }
   }
   ```

Configuration Details
--------------------

*   **attribute**: `null` - No specific attribute is used for locating elements.
*   **by**: `XPATH` -  Locators are identified using XPath expressions.
*   **selector**: `//td[div[contains(@class, '-item-card') and not(contains(@class, 'item-card-text'))]]` -  XPath expression targeting product blocks that are part of a `td` element, containing `div` elements with class `-item-card`, but not containing `item-card-text` class.
*   **if_list**: `first` - Returns only the first match in the list.
*   **use_mouse**: `false` - Does not require mouse interaction to locate.
*   **mandatory**: `false` - Element is not crucial for the process, but helpful for filtering.
*   **event**: `""` - No specific event is triggered when locating.
*   **locator_description**: `"Товары со страницы deals, котору я делаю из почтовой рассылки."` - Description (in Russian) of the locator's intended use.