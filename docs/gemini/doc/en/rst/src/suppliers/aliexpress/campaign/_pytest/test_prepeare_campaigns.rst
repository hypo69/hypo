hypotez/src/suppliers/aliexpress/campaign/_pytest/test_prepeare_campaigns.py
============================================================================

.. module:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_prepeare_campaigns
   :platform: Windows, Unix
   :synopsis: Test suite for the `prepare_campaigns` module.

This module contains unit tests for the `prepare_campaigns` module, focusing on functions like `update_category`, `process_campaign_category`, `process_campaign`, and `main`.  It utilizes `pytest` for testing and mocks various dependencies using `unittest.mock`.  The tests cover both successful and failure scenarios.


Functions
---------

.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_prepeare_campaigns.test_update_category_success
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_prepeare_campaigns.test_update_category_failure
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_prepeare_campaigns.test_process_campaign_category_success
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_prepeare_campaigns.test_process_campaign_category_failure
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_prepeare_campaigns.test_process_campaign
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_prepeare_campaigns.test_main


Fixtures
--------

.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_prepeare_campaigns.mock_j_loads
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_prepeare_campaigns.mock_j_dumps
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_prepeare_campaigns.mock_logger
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_prepeare_campaigns.mock_get_directory_names
.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_prepeare_campaigns.mock_ali_promo_campaign