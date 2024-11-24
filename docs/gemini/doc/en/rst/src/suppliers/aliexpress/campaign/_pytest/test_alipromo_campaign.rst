test_alipromo_campaign.py
=========================

.. module:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_alipromo_campaign
    :platform: Windows, Unix
    :synopsis: This module contains unit tests for the AliPromoCampaign class.

Module Contents
---------------

Fixtures
^^^^^^^^^

.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_alipromo_campaign.campaign
    :noindex:
    :specialization: Fixture for creating a campaign instance.


Tests
^^^^^

.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_alipromo_campaign.test_initialize_campaign
    :noindex:
    :specialization: Tests if the initialize_campaign method correctly initializes the campaign data.

.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_alipromo_campaign.test_get_category_products_no_json_files
    :noindex:
    :specialization: Tests get_category_products when no JSON files are present.

.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_alipromo_campaign.test_get_category_products_with_json_files
    :noindex:
    :specialization: Tests get_category_products when JSON files are present.

.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_alipromo_campaign.test_create_product_namespace
    :noindex:
    :specialization: Tests if create_product_namespace correctly creates a product namespace.

.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_alipromo_campaign.test_create_category_namespace
    :noindex:
    :specialization: Tests if create_category_namespace correctly creates a category namespace.

.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_alipromo_campaign.test_create_campaign_namespace
    :noindex:
    :specialization: Tests if create_campaign_namespace correctly creates a campaign namespace.

.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_alipromo_campaign.test_prepare_products
    :noindex:
    :specialization: Tests if prepare_products calls process_affiliate_products.

.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_alipromo_campaign.test_fetch_product_data
    :noindex:
    :specialization: Tests if fetch_product_data correctly fetches product data.

.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_alipromo_campaign.test_save_product
    :noindex:
    :specialization: Tests if save_product correctly saves product data.

.. autofunction:: hypotez.src.suppliers.aliexpress.campaign._pytest.test_alipromo_campaign.test_list_campaign_products
    :noindex:
    :specialization: Tests if list_campaign_products correctly lists product titles.