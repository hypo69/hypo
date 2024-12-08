# aliexpress/api/tools

## Overview

This module contains tools for interacting with the AliExpress API, specifically focused on product identification.


## Functions

### `get_product_id`

**Description**: Retrieves the product ID from AliExpress based on various input parameters.

**Parameters**:
- `keyword` (str): The search keyword(s) for the product.
- `page` (Optional[int], optional): The page number of search results to retrieve. Defaults to 1.
- `limit` (Optional[int], optional): The maximum number of results per page. Defaults to 20.

**Returns**:
- `list[dict] | None`: A list of dictionaries, where each dictionary represents a product and its associated details, or `None` if there was an error.


**Raises**:
- `Exception`: An exception raised if there's an error in the API request or processing.