# hypotez/src/suppliers/aliexpress/_pytests/test_affiliated_products_generator.py

## Overview

This Python file contains unit tests for the `AliAffiliatedProducts` class, which is part of the `aliexpress` supplier module.  It verifies the functionality of methods related to processing affiliate products from AliExpress.  The tests utilize `pytest` and mocking to isolate the tested methods and validate their interactions with external dependencies.


## Table of Contents

* [Fixtures](#fixtures)
* [Tests](#tests)
    * [`test_check_and_process_affiliate_products`](#test_check_and_process_affiliate_products)
    * [`test_process_affiliate_products`](#test_process_affiliate_products)


## Fixtures

### `ali_affiliated_products`

**Description**: This fixture creates an instance of the `AliAffiliatedProducts` class, preparing it for use in the test cases.  It utilizes sample values for the campaign name, category name, language, and currency.

**Returns**:
- `AliAffiliatedProducts`: An instance of the `AliAffiliatedProducts` class initialized with sample data.


## Tests

### `test_check_and_process_affiliate_products`

**Description**: This test verifies that the `check_and_process_affiliate_products` method correctly calls the `process_affiliate_products` method. It utilizes the `patch` decorator to mock the `process_affiliate_products` method and asserts that it was called once with the expected input parameter.

**Parameters**:
- `ali_affiliated_products`: An instance of `AliAffiliatedProducts` provided by the fixture.
- `prod_urls` (list of str): A list of product URLs to be processed.

**Raises**:
- `AssertionError`: If the `process_affiliate_products` method is not called once with the provided `prod_urls`.


### `test_process_affiliate_products`

**Description**: This test verifies the `process_affiliate_products` method, ensuring that it correctly processes the provided product URLs, retrieves product details, and returns the expected results.

**Parameters**:
- `ali_affiliated_products`: An instance of `AliAffiliatedProducts` provided by the fixture.
- `prod_urls` (list of str): A list of product URLs to be processed.

**Mocks**:
- `retrieve_product_details`: Mocks the `retrieve_product_details` method to return a list of product details.
- `ensure_https`: Mocks the `ensure_https` function to return the input URLs.
- `save_png_from_url`, `save_video_from_url`: Mocks functions for saving images and videos.
- `j_dumps`: Mocks the `json` encoding function.

**Returns**:
- `list`: A list of processed product information.

**Assertions**:
- Verifies the length of the `processed_products` list matches the number of product details retrieved.
- Checks if the `product_id` of the first processed product corresponds to the expected value.

**Raises**:
- `AssertionError`: If any of the assertions fail.