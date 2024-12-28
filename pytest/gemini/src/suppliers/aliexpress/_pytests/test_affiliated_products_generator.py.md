```python
# -*- coding: utf-8 -*-
"""
.. module:: src.suppliers.aliexpress._pytests
    :platform: Windows, Unix
    :synopsis:

"""


"""
    :platform: Windows, Unix
    :synopsis:

"""

"""
    :platform: Windows, Unix
    :synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""


""" module: src.suppliers.aliexpress._pytests """


""" YOU MUST WRITE A DESCRIPTION !
This script contains the following:

#Fixtures:
 - ali_affiliated_products: A fixture that returns an instance of AliAffiliatedProducts.

#Tests:
 - test_check_and_process_affiliate_products:
Tests the check_and_process_affiliate_products method to ensure it calls process_affiliate_products correctly.

 - test_process_affiliate_products:
Tests the process_affiliate_products method to ensure it processes the products correctly.

It mocks external dependencies and verifies the output.
"""
import pytest
from unittest.mock import patch, MagicMock
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
from types import SimpleNamespace

# Sample data
campaign_name = "sample_campaign"
category_name = "sample_category"
language = "EN"
currency = "USD"
prod_urls = ["https://www.aliexpress.com/item/123.html", "456"]


@pytest.fixture
def ali_affiliated_products():
    return AliAffiliatedProducts(campaign_name, category_name, language, currency)


def test_check_and_process_affiliate_products(ali_affiliated_products):
    """
    Test that check_and_process_affiliate_products correctly calls process_affiliate_products.
    It uses a mock to verify that process_affiliate_products is called once with the correct arguments.
    """
    with patch.object(ali_affiliated_products, 'process_affiliate_products') as mock_process:
        ali_affiliated_products.check_and_process_affiliate_products(prod_urls)
        mock_process.assert_called_once_with(prod_urls)


def test_process_affiliate_products(ali_affiliated_products):
    """
    Test that process_affiliate_products correctly processes product details.
    It mocks the `retrieve_product_details`, `ensure_https`, `save_png_from_url`, and `save_video_from_url`
    methods/functions to isolate the test and verifies the output based on the mocked results.
    """
    mock_product_details = [SimpleNamespace(product_id="123", promotion_link="promo_link", product_main_image_url="image_url", product_video_url="video_url")]

    with patch.object(ali_affiliated_products, 'retrieve_product_details', return_value=mock_product_details) as mock_retrieve, \
            patch("src.suppliers.aliexpress.affiliated_products_generator.ensure_https", return_value=prod_urls), \
            patch("src.suppliers.aliexpress.affiliated_products_generator.save_png_from_url"), \
            patch("src.suppliers.aliexpress.affiliated_products_generator.save_video_from_url"), \
            patch("src.suppliers.aliexpress.affiliated_products_generator.j_dumps", return_value=True):

        processed_products = ali_affiliated_products.process_affiliate_products(prod_urls)

        assert len(processed_products) == 1
        assert processed_products[0].product_id == "123"


def test_process_affiliate_products_empty_urls(ali_affiliated_products):
    """
     Test that process_affiliate_products correctly handles empty input list of product urls.
    It checks that an empty list is returned when an empty url list is passed.
    """
    empty_urls = []
    processed_products = ali_affiliated_products.process_affiliate_products(empty_urls)
    assert len(processed_products) == 0


def test_process_affiliate_products_no_valid_url(ali_affiliated_products):
    """
    Test process_affiliate_products with no valid URL.
    If the URL is not valid and the `ensure_https` returns an empty list no products should be processed.
    """
    invalid_urls = ["invalid_url"]
    with patch("src.suppliers.aliexpress.affiliated_products_generator.ensure_https", return_value=[]), \
             patch.object(ali_affiliated_products, 'retrieve_product_details') as mock_retrieve:
        processed_products = ali_affiliated_products.process_affiliate_products(invalid_urls)
        mock_retrieve.assert_not_called()
        assert len(processed_products) == 0


def test_process_affiliate_products_retrieve_product_details_exception(ali_affiliated_products):
    """
    Test exception handling in process_affiliate_products when `retrieve_product_details` fails.
    It checks that the process returns an empty list and handles the exception.
    """
    with patch.object(ali_affiliated_products, 'retrieve_product_details', side_effect=Exception("Mocked exception")), \
         patch("src.suppliers.aliexpress.affiliated_products_generator.ensure_https", return_value=prod_urls), \
         patch("src.suppliers.aliexpress.affiliated_products_generator.save_png_from_url"), \
         patch("src.suppliers.aliexpress.affiliated_products_generator.save_video_from_url"), \
         patch("src.suppliers.aliexpress.affiliated_products_generator.j_dumps", return_value=True):
        processed_products = ali_affiliated_products.process_affiliate_products(prod_urls)
        assert len(processed_products) == 0


def test_process_affiliate_products_no_product_details(ali_affiliated_products):
    """
    Test scenario when `retrieve_product_details` returns empty list.
    If no product details are found, no products should be processed and the list returned should be empty.
    """
    with patch.object(ali_affiliated_products, 'retrieve_product_details', return_value=[]), \
        patch("src.suppliers.aliexpress.affiliated_products_generator.ensure_https", return_value=prod_urls), \
        patch("src.suppliers.aliexpress.affiliated_products_generator.save_png_from_url"), \
        patch("src.suppliers.aliexpress.affiliated_products_generator.save_video_from_url"), \
        patch("src.suppliers.aliexpress.affiliated_products_generator.j_dumps", return_value=True):
        processed_products = ali_affiliated_products.process_affiliate_products(prod_urls)
        assert len(processed_products) == 0

if __name__ == "__main__":
    pytest.main()
```