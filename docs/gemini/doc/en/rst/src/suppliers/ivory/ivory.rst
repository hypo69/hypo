ivory.json
==========

This file contains configuration data for the ivory supplier.  It defines parameters for interacting with the ivory website, including the supplier ID, prefix, URLs, pricing rules, and login requirements.


.. automodule:: hypotez.src.suppliers.ivory.ivory
    :members:
    :undoc-members:
    :show-inheritance:

Configuration Parameters
-----------------------

`supplier`
~~~~~~~~~~
^ Defines the supplier name (e.g., "ivory").

`supplier_id`
~~~~~~~~~~~~
^ Uniquely identifies the supplier (e.g., "11343").

`supplier_prefix`
~~~~~~~~~~~~~~~~~
^ String prefix used for naming elements related to the supplier.

`start_url`
~~~~~~~~~~~
^ The starting URL for the ivory website.

`login_url`
~~~~~~~~~~~
^ The URL for logging in to the ivory website.

`price_rule`
~~~~~~~~~~~~
^  Price multiplier for products (e.g., "*1.43").

`collect_products_from_categorypage`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
^ Boolean specifying if products should be collected from category pages.

`if_login`
~~~~~~~~~~
^ Boolean indicating if login is required for interaction with the website.

`scenario_files`
~~~~~~~~~~~~~~~~~
^ List of scenario files (currently empty).

`last_runned_scenario`
~~~~~~~~~~~~~~~~~~~~~~~
^ Stores the name of the last runned scenario.

`excluded`
~~~~~~~~~~
^ List of excluded items (currently empty).