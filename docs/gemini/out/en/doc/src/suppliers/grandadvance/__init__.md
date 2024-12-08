# src.suppliers.grandadvance

## Overview

This module provides an interface for interacting with the GrandAdvance supplier.  It currently defines a `Graber` class to handle data retrieval.


## Classes

### `Graber`

**Description**:  The `Graber` class is responsible for retrieving data from the GrandAdvance supplier.

**Methods**:

#### `get_data(request_id: int) -> dict | None`

**Description**: Retrieves data associated with a specific request ID.

**Parameters**:

- `request_id` (int): The ID of the request.

**Returns**:

- `dict | None`: Returns a dictionary containing the retrieved data, or `None` if no data is found or an error occurs.

**Raises**:

- `APIError`: Raised for any API-related issues during data retrieval.
- `ValueError`: Raised if the `request_id` is invalid.


## Functions

(No functions defined in this file)