# Module: hypotez/src/suppliers/aliexpress/gui/category.py

## Overview

This module provides a graphical user interface (GUI) for preparing advertising campaigns on AliExpress. It allows users to select a JSON file containing campaign data, load it, and prepare categories for advertising.


## Classes

### `CategoryEditor`

**Description**: This class represents the main window of the application. It handles file loading, displaying campaign information, and providing buttons for preparing all or specific categories.

**Methods**:

#### `__init__`

**Description**: Initializes the `CategoryEditor` window.

**Parameters**:
- `parent` (Optional[QWidget], optional): Parent widget. Defaults to `None`.
- `main_app` (Optional[MainApp], optional): Main application instance. Defaults to `None`.


**Raises**:
- `Exception`: If any error occurs during initialization.

#### `setup_ui`

**Description**: Sets up the user interface of the window.

**Raises**:
- `Exception`: If any error occurs during UI setup.


#### `setup_connections`

**Description**: Sets up signal-slot connections between UI elements.


#### `open_file`

**Description**: Opens a file dialog to select and load a JSON file.


**Raises**:
- `Exception`: If any error occurs during file selection or loading.

#### `load_file`

**Description**: Loads a JSON file and parses the campaign data.


**Parameters**:
- `campaign_file (str)`: Path to the JSON file.


**Raises**:
- `Exception`: If the JSON file is invalid or cannot be parsed.

#### `create_widgets`

**Description**: Creates and adds widgets based on the loaded campaign data. This method dynamically adds labels to display campaign name, title, and each category name.

**Parameters**:
- `data (SimpleNamespace)`: Parsed campaign data from the JSON file.

**Raises**:
- `Exception`: If any error occurs during widget creation.



#### `prepare_all_categories_async`

**Description**: Asynchronously prepares all categories for advertising campaigns.

**Raises**:
- `Exception`: If an error occurs during the asynchronous preparation process.


#### `prepare_category_async`

**Description**: Asynchronously prepares a specific category for advertising campaigns.

**Parameters**:
- `campaign_name (str)`: Name of the campaign to prepare.


**Raises**:
- `Exception`: If an error occurs during the asynchronous preparation process.




## Functions


(No functions found in the provided code)


## Modules


- `header`
- `sys`
- `asyncio`
- `pathlib`
- `types`
- `PyQt6`
- `qasync`
- `src.utils.jjson`
- `src.suppliers.aliexpress.campaign`