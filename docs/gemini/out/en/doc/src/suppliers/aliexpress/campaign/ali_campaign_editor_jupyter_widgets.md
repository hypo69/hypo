# Module: hypotez/src/suppliers/aliexpress/campaign/ali_campaign_editor_jupyter_widgets.py

## Overview

This module provides Jupyter widgets for managing AliExpress campaigns. It allows users to select campaigns, categories, languages/currencies, initialize campaign editors, save campaigns, display products, and open Google Spreadsheets.  The module utilizes classes and functions for handling interactions with the campaign data and presenting them in an interactive Jupyter notebook environment.


## Classes

### `JupyterCampaignEditorWidgets`

**Description**: This class encapsulates the Jupyter widgets for interacting with AliExpress campaigns. It handles widget initialization, callbacks, and interactions with the campaign editor object.


**Methods**:

#### `__init__(self)`

**Description**: Initializes the widgets for selecting campaigns, categories, languages/currencies, and buttons for initialization, saving, showing products, and opening spreadsheets.  Sets up default values and callbacks for the widgets and automatically loads the first campaign.

#### `initialize_campaign_editor(self, _)`

**Description**: Initializes the campaign editor based on the selected campaign, category, and language/currency.  Sets the campaign editor object (`self.campaign_editor`) and fetches the campaign category and related products.  Handles cases where no campaign is selected.

**Parameters**:

- `_`: Unused argument, required for button callback.

**Raises**:

- `FileNotFoundError`: Raised if the specified campaigns directory does not exist.


#### `update_category_dropdown(self, campaign_name: str)`

**Description**: Updates the category dropdown based on the selected campaign. Fetches the categories from the campaign's directory.

**Parameters**:

- `campaign_name (str)`: The name of the campaign.

**Example**:
```python
>>> self.update_category_dropdown("SummerSale")
```

#### `on_campaign_name_change(self, change: dict[str, str])`

**Description**: Handles changes in the campaign name dropdown. Updates the category dropdown and reinitializes the campaign editor.

**Parameters**:

- `change (dict[str, str])`: The change dictionary containing the new value.

**Example**:
```python
>>> self.on_campaign_name_change({'new': 'SummerSale'})
```


#### `on_category_change(self, change: dict[str, str])`

**Description**: Handles changes in the category dropdown. Reinitializes the campaign editor with the new category.

**Parameters**:

- `change (dict[str, str])`: The change dictionary containing the new value.

**Example**:
```python
>>> self.on_category_change({'new': 'Electronics'})
```


#### `on_language_change(self, change: dict[str, str])`

**Description**: Handles changes in the language/currency dropdown. Updates the language and currency properties and reinitializes the campaign editor.

**Parameters**:

- `change (dict[str, str])`: The change dictionary containing the new value.

**Example**:
```python
>>> self.on_language_change({'new': 'EN USD'})
```

#### `save_campaign(self, _)`

**Description**: Saves the campaign's categories to a Google Spreadsheet.

**Parameters**:

- `_`: Unused argument, required for button callback.

**Raises**:

- `Exception`: Any exception encountered during the save operation is caught and logged.


#### `show_products(self, _)`

**Description**: Displays the products in the selected category.

**Parameters**:

- `_`: Unused argument, required for button callback.

**Raises**:

- `Exception`: Any exception encountered during the product display operation is caught and logged.


#### `open_spreadsheet(self, _)`

**Description**: Opens the Google Spreadsheet in a web browser.

**Parameters**:

- `_`: Unused argument, required for button callback.


#### `setup_callbacks(self)`

**Description**: Sets up callbacks for all widgets.


#### `display_widgets(self)`

**Description**: Displays all the initialized widgets in the Jupyter notebook. Initializes the campaign editor with the first campaign automatically.

**Example**:
```python
>>> self.display_widgets()
```


## Functions

### None


## Module Attributes

### `MODE`

**Description**: Stores a string value representing the current mode (e.g., 'dev').  This is a global variable for potentially configuring the module's behavior.

```