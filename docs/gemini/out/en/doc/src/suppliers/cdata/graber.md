# hypotez/src/suppliers/cdata/graber.py

## Overview

This module defines the `Graber` class, which is responsible for collecting product data from the `cdata.co.il` website.  It provides a structure for handling various product fields, allowing for customization of data extraction logic through overridden methods.  The class supports asynchronous operations and incorporates a decorator for handling pop-up windows before data retrieval.

## Classes

### `Graber`

**Description**: This class is designed to gather product details from the `cdata.co.il` website. It extends the base `Graber` class, providing the necessary methods for extracting specific product data and handling potentially complex operations such as pop-up window closures.


**Methods**:

#### `__init__`

**Description**: Initializes the Graber class, setting the supplier prefix and calling the parent class's initialization method. It also handles the configuration for the pop-up window closure decorator.

**Parameters**:

- `driver` (Driver): The WebDriver instance for interacting with the website.


#### `grab_page`

**Description**: Asynchronous function to grab product fields from the `cdata.co.il` page.

**Parameters**:

- `driver` (Driver): The WebDriver instance to use for accessing the page.

**Returns**:

- `ProductFields`: A `ProductFields` object containing the collected product data.

**Raises**:

- `ExecuteLocatorException`:  If there's an issue executing a locator command.

## Functions

(None defined in this file, only methods)


## Module Variables

(None defined in this file.)