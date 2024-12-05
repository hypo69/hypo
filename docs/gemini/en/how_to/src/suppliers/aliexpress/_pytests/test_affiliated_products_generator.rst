rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python script contains unit tests for the `AliAffiliatedProducts` class, which is likely part of a system for generating affiliate product information from AliExpress.  The tests focus on verifying the correct functionality of methods related to checking and processing affiliate products, including mocking external dependencies like product retrieval and image/video saving.  It utilizes the `pytest` framework for testing and `unittest.mock` for mocking dependencies.  The tests verify that methods are called with the expected parameters and that the output conforms to the expected structure.

Execution steps
-------------------------
1. **Initialization:** The `ali_affiliated_products` fixture creates an instance of the `AliAffiliatedProducts` class, passing in parameters for campaign name, category, language, and currency.  These parameters are crucial for correctly configuring the product retrieval process.

2. **`check_and_process_affiliate_products` test:** This test verifies that the `check_and_process_affiliate_products` method correctly calls the `process_affiliate_products` method with the provided product URLs.  It utilizes `patch` to mock the `process_affiliate_products` method.

3. **`process_affiliate_products` test:** This test verifies the internal functionality of the `process_affiliate_products` method.  It mocks the `retrieve_product_details` method to return sample product data. It also mocks several other functions (e.g., `ensure_https`, `save_png_from_url`, `save_video_from_url`, `j_dumps`) to simulate their functionality.  The assertion verifies that the output `processed_products` list has the expected length and contains the expected data from the mocked `mock_product_details`.


4. **Assertions:** The tests contain assertions to validate the expected outputs and interactions.  These assertions verify that the functions behave as intended under different conditions, confirming the expected number of processed products and the data they contain.


Usage example
-------------------------
.. code-block:: python

    import pytest
    from unittest.mock import patch, MagicMock
    from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
    from types import SimpleNamespace

    # ... (Sample data definitions as in the original code) ...

    # Example usage (assuming AliAffiliatedProducts and necessary functions are defined)

    @pytest.fixture
    def ali_affiliated_products():
        return AliAffiliatedProducts(campaign_name, category_name, language, currency)

    def test_process_affiliate_products(ali_affiliated_products):
        mock_product_details = [SimpleNamespace(product_id="123", promotion_link="promo_link", product_main_image_url="image_url", product_video_url="video_url")]

        with patch.object(ali_affiliated_products, 'retrieve_product_details', return_value=mock_product_details) as mock_retrieve:

            processed_products = ali_affiliated_products.process_affiliate_products(prod_urls)

            assert len(processed_products) == 1
            assert processed_products[0].product_id == "123"

    if __name__ == "__main__":
        pytest.main()