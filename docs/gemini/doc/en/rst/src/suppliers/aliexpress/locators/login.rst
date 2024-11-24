aliexpress Login Locators
==========================

This file contains locators for the AliExpress login page, including elements for closing banners, opening login, entering credentials, clicking the login button, and accepting cookies.  It also includes locators for selecting currency, language, and shipping destination.

.. automodule:: hypotez.src.suppliers.aliexpress.locators.login
    :members:
    :undoc-members:
    :show-inheritance:

Login Section
------------

^ Login URL
~~~
https://login.aliexpress.com
~~~

^ Closing Banner
~~~
.. automodule:: hypotez.src.suppliers.aliexpress.locators.login
    :members: close_banner
~~~
This locator is used to close the banner that appears on the AliExpress login page.  It targets the element that allows the closing of the banner with the appropriate text (e.g., "אפשר").

^ Opening Login
~~~
.. automodule:: hypotez.src.suppliers.aliexpress.locators.login
    :members: open_login
~~~
This locator is used to open the login form.  It will find an element containing the text "Sign in" or similar, depending on the language.

^ Email Locator
~~~
.. automodule:: hypotez.src.suppliers.aliexpress.locators.login
    :members: email_locator
~~~
This locator is used to locate the email input field.  The input is associated with the id 'fm-login-id'.

^ Password Locator
~~~
.. automodule:: hypotez.src.suppliers.aliexpress.locators.login
    :members: password_locator
~~~
This locator is used to locate the password input field.  The input is associated with the id 'fm-login-password'.

^ Login Button Locator
~~~
.. automodule:: hypotez.src.suppliers.aliexpress.locators.login
    :members: loginbutton_locator
~~~
This locator is used to locate the login button.  The button has a type of 'submit'.

^ Cookies Accept Locator
~~~
.. automodule:: hypotez.src.suppliers.aliexpress.locators.login
    :members: cookies_accept
~~~
This locator is used to locate the cookie acceptance button.  The button is associated with a data-role that includes 'gdpr-accept'.


Currency, Language, and Ship-To Locators
---------------------------------------

^ Currency, Language, and Ship-To Block Opener
~~~
.. automodule:: hypotez.src.suppliers.aliexpress.locators.login
    :members: currency_language_shipto_block_opener_locator
~~~
This locator opens the block for selecting currency, language, and shipping destination.

^ Ship-To Locator
~~~
.. automodule:: hypotez.src.suppliers.aliexpress.locators.login
    :members: shipto_locator
~~~
This locator targets elements for selecting the shipping destination.  It can target multiple elements, using a list of XPaths to increase the chances of finding the desired element.

^ Language Locator
~~~
.. automodule:: hypotez.src.suppliers.aliexpress.locators.login
    :members: language_locator
~~~
This locator targets elements for selecting the language.  It can target multiple elements, using a list of XPaths to increase the chances of finding the desired element.

^ Currency Locator
~~~
.. automodule:: hypotez.src.suppliers.aliexpress.locators.login
    :members: currency_locator
~~~
This locator targets elements for selecting the currency.  It can target multiple elements, using a list of XPaths to increase the chances of finding the desired element.

^ Save Button Locator
~~~
.. automodule:: hypotez.src.suppliers.aliexpress.locators.login
    :members: save_button_locator
~~~
This locator targets the save button that applies the changes for currency, language, and ship-to.