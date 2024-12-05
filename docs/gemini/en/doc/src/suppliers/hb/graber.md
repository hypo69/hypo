# Module: hypotez/src/suppliers/hb/graber.py

## Overview

This module defines the `Graber` class, a subclass of `Grbr`, responsible for extracting product data from the `hb.co.il` website. It provides functions to handle specific fields, allowing for customized data extraction logic.  It includes a decorator (`@close_pop_up`) for handling pop-up windows before executing core logic, allowing for potential customization in each `Supplier` class.  The module leverages asynchronous operations using `asyncio` and `Driver` class from the `src.webdriver` module for interacting with the web driver.  Data is extracted into a structured `ProductFields` object.

## Classes

### `Graber`

**Description**: This class encapsulates the logic for grabbing product fields from the `hb.co.il` website.  It extends the `Graber` base class and includes methods for fetching data from specific elements of the product page.


**Methods**

- `__init__(self, driver: Driver)`:
    **Description**: Initializes the `Graber` instance with the provided web driver. Sets the `supplier_prefix` to 'hb' and initializes the parent class.

    **Parameters**:
        - `driver (Driver)`: The web driver instance to use for interaction with the page.


- `grab_page(self, driver: Driver) -> ProductFields`:
    **Description**: Asynchronous function to gather all product fields from the webpage.

    **Parameters**:
        - `driver (Driver)`: The web driver instance to use for grabbing product details.

    **Returns**:
        - `ProductFields`: A structured object containing the extracted product data.  Returns `None` if any error occurs during the data extraction process.

    **Raises**:
        - `SomeError`: Raised in case of any error during the asynchronous operation or data fetching.

## Functions

### `close_pop_up(value: Any = None) -> Callable`

**Description**: A decorator for handling pop-up windows before executing the main logic of another function.  This allows for the ability to customize the pop-up handling in each supplier class.

**Parameters**:
    - `value (Any, optional):` Additional value for the decorator. Defaults to `None`.

**Returns**:
    - `Callable`: A decorator function.