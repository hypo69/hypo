Module hypotez/src/webdriver/_pytest/test_driver
==============================================

.. module:: hypotez.src.webdriver._pytest.test_driver
   :platform: Windows, Unix
   :synopsis: This module contains test cases for the DriverBase class methods.


Description
----------

This file, `test_driver.py`, contains pytest and unittest.mock-based tests for various methods of the `DriverBase` class, including `driver_payload`, `scroll`, `locale`, `get_url`, `extract_domain`, `_save_cookies_locally`, `page_refresh`, `wait`, and `delete_driver_logs`.  The tests aim to verify the functionality of these methods by simulating interactions and using mock objects to isolate the tested code.


Classes
-------

.. autoclass:: TestDriverBase
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autofunction:: test_driver_payload
.. autofunction:: test_scroll
.. autofunction:: test_locale
.. autofunction:: test_get_url
.. autofunction:: test_extract_domain
.. autofunction:: test_save_cookies_localy
.. autofunction:: test_page_refresh
.. autofunction:: test_wait
.. autofunction:: test_delete_driver_logs