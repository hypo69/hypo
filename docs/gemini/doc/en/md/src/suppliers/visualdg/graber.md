# hypotez/src/suppliers/visualdg/graber.py

## Overview

This module defines the `Graber` class, which is responsible for grabbing product fields from the VisualDG supplier. It utilizes a driver instance for interacting with the target website and extracts various product attributes. The class inherits from the base `Graber` class, providing common functionalities for different suppliers.


## Classes

### `Graber`

**Description**: This class handles the process of collecting product fields from the VisualDG supplier.  It interacts with a `Driver` object to perform actions on the website and stores the extracted product data in `self.fields`.

**Methods**

#### `__init__`

**Description**: Initializes the `Graber` object.

**Parameters**:

- `driver` (Driver): The driver instance used for interaction.


#### `grab_page`

**Description**: Asynchronously grabs product fields from the website.

**Parameters**:

- `driver` (Driver): The driver instance to use.

**Returns**:

- `ProductFields`: A `ProductFields` object containing the extracted product data.


## Functions

(No functions are defined in this file other than methods of the Graber class.)