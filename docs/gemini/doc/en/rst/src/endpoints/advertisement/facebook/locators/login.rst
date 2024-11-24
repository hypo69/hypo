Facebook Login Locators
=========================

This file defines locators for Facebook login elements.  It uses XPath selectors to locate elements on the Facebook login page.

Locators
--------

.. code-block:: json
   :caption: Login Locators

   ```json
   {
     "email": {
       "attribute": null,
       "by": "XPATH",
       "selector": "//input[@name = 'email']",
       "if_list": "first",
       "use_mouse": false,
       "event": "click()",
       "mandatory": true,
       "locator_description": "user email or phone"
     },
     "password": {
       "attribute": null,
       "by": "XPATH",
       "selector": "//input[@name = 'pass']",
       "if_list": "first",
       "use_mouse": [ false, false ],
       "event": "click()",
       "mandatory": [ true, true ],
       "locator_description": "user email or phone"
     },
     "button": {
       "attribute": null,
       "by": "XPATH",
       "selector": "//button[@name = 'login']",
       "if_list": "first",
       "use_mouse": false,
       "event": "click()",
       "mandatory": true,
       "locator_description": "send button"
     }
   }
   ```