# test_affiliated_products_generator.py

## Overview

This module contains unit tests for the `AliAffiliatedProducts` class, which is responsible for generating affiliated products from AliExpress.  The tests cover the `check_and_process_affiliate_products` and `process_affiliate_products` methods, verifying correct functionality and interaction with external dependencies.

## Table of Contents

* [Fixtures](#fixtures)
* [Tests](#tests)
    * [test_check_and_process_affiliate_products](#test_check_and_process_affiliate_products)
    * [test_process_affiliate_products](#test_process_affiliate_products)


## Fixtures

### `ali_affiliated_products`

**Description**: This fixture creates an instance of `AliAffiliatedProducts` with sample campaign, category, language, and currency parameters.

**Returns**:
- `AliAffiliatedProducts`: An instance of the `AliAffiliatedProducts` class.


## Tests

### `test_check_and_process_affiliate_products`

**Description**: This test verifies that `check_and_process_affiliate_products` correctly calls the `process_affiliate_products` method with the provided product URLs.

**Parameters**:
- `ali_affiliated_products`: An instance of `AliAffiliatedProducts` (provided by the fixture).

**Assertions**:
- `mock_process.assert_called_once_with(prod_urls)`: Asserts that the `process_affiliate_products` method was called exactly once with the `prod_urls` parameter.

### `test_process_affiliate_products`

**Description**: This test verifies that `process_affiliate_products` correctly retrieves, processes, and returns product details.

**Parameters**:
- `ali_affiliated_products`: An instance of `AliAffiliatedProducts` (provided by the fixture).

**Mocking**:
- `retrieve_product_details`: Mocks the `retrieve_product_details` method to return a sample list of product details.
- `ensure_https`: Mocks `ensure_https` to return the input `prod_urls`.
- `save_png_from_url`: Mocks the `save_png_from_url` function.
- `save_video_from_url`: Mocks the `save_video_from_url` function.
- `j_dumps`: Mocks the `j_dumps` function to return `True`.

**Assertions**:
- `len(processed_products) == 1`: Asserts that the length of the `processed_products` list is 1, indicating that one product was processed successfully.
- `processed_products[0].product_id == "123"`: Asserts that the `product_id` of the first processed product is "123".