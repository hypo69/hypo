# Module: hypotez/src/suppliers/aliexpress/campaign/_pytest/test_alipromo_campaign.py

## Overview

This module contains unit tests for the `AliPromoCampaign` class, located in the `src.suppliers.aliexpress.campaign` package.  The tests cover various aspects of the campaign initialization, data retrieval, processing, and saving.


## Fixtures

### `campaign`

**Description**: A fixture that creates an instance of `AliPromoCampaign` for use in testing.

**Returns**: An `AliPromoCampaign` object initialized with sample campaign, category, language, and currency data.

## Functions

### `test_initialize_campaign`

**Description**: Tests if the `initialize_campaign` method correctly initializes the campaign data.  Uses a mocked `j_loads_ns` function to simulate loading JSON data.

**Parameters**:

- `mocker`: (pytest.MonkeyPatch) A fixture for mocking dependencies.
- `campaign`: (`AliPromoCampaign`) Instance of the campaign class.

**Raises**:

- None


**Returns**: None


### `test_get_category_products_no_json_files`

**Description**: Tests `get_category_products` when no JSON files are present.  Uses mocked `get_filenames` and `fetch_product_data` to simulate the scenario.

**Parameters**:

- `mocker`: (pytest.MonkeyPatch) A fixture for mocking dependencies.
- `campaign`: (`AliPromoCampaign`) Instance of the campaign class.

**Raises**:

- None


**Returns**: None


### `test_get_category_products_with_json_files`

**Description**: Tests `get_category_products` when JSON files are present.  Asserts that the correct product data is retrieved.

**Parameters**:

- `mocker`: (pytest.MonkeyPatch) A fixture for mocking dependencies.
- `campaign`: (`AliPromoCampaign`) Instance of the campaign class.

**Raises**:

- None


**Returns**: None


### `test_create_product_namespace`

**Description**: Tests `create_product_namespace` function.

**Parameters**:

- `campaign`: (`AliPromoCampaign`) Instance of the campaign class.


**Raises**:

- None


**Returns**: None



### `test_create_category_namespace`

**Description**: Tests `create_category_namespace` function.

**Parameters**:

- `campaign`: (`AliPromoCampaign`) Instance of the campaign class.

**Raises**:

- None


**Returns**: None


### `test_create_campaign_namespace`

**Description**: Tests `create_campaign_namespace` function.

**Parameters**:

- `campaign`: (`AliPromoCampaign`) Instance of the campaign class.

**Raises**:

- None


**Returns**: None


### `test_prepare_products`

**Description**: Tests `prepare_products` method.  Asserts that `process_affiliate_products` is called.

**Parameters**:

- `mocker`: (pytest.MonkeyPatch) A fixture for mocking dependencies.
- `campaign`: (`AliPromoCampaign`) Instance of the campaign class.

**Raises**:

- None


**Returns**: None


### `test_fetch_product_data`

**Description**: Tests `fetch_product_data` method.  Asserts that products are correctly retrieved and their data is accessible.

**Parameters**:

- `mocker`: (pytest.MonkeyPatch) A fixture for mocking dependencies.
- `campaign`: (`AliPromoCampaign`) Instance of the campaign class.

**Raises**:

- None


**Returns**: None



### `test_save_product`

**Description**: Tests `save_product` method.  Asserts that product data is correctly saved to a file.

**Parameters**:

- `mocker`: (pytest.MonkeyPatch) A fixture for mocking dependencies.
- `campaign`: (`AliPromoCampaign`) Instance of the campaign class.

**Raises**:

- None


**Returns**: None



### `test_list_campaign_products`

**Description**: Tests `list_campaign_products` method.  Asserts that product titles are correctly extracted and returned as a list.

**Parameters**:

- `campaign`: (`AliPromoCampaign`) Instance of the campaign class.

**Raises**:

- None


**Returns**: None