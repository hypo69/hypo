# JupyterWidgets for AliExpress Campaign Editor

## Overview

This module provides Jupyter widgets for interacting with and managing AliExpress campaigns.  It allows users to select campaigns, categories, and languages, initialize editors, save campaigns, and view products within a Jupyter Notebook environment.  It leverages existing classes like `AliCampaignEditor` and `locales` for campaign management.

## Table of Contents

* [JupyterCampaignEditorWidgets](#jupytercampaigneditoreditorwidgets)
    * [\_\_init\_\_](#__init__)
    * [initialize\_campaign\_editor](#initialize_campaign_editor)
    * [update\_category\_dropdown](#update_category_dropdown)
    * [on\_campaign\_name\_change](#on_campaign_name_change)
    * [on\_category\_change](#on_category_change)
    * [on\_language\_change](#on_language_change)
    * [save\_campaign](#save_campaign)
    * [show\_products](#show_products)
    * [open\_spreadsheet](#open_spreadsheet)
    * [setup\_callbacks](#setup_callbacks)
    * [display\_widgets](#display_widgets)


## Classes

### `JupyterCampaignEditorWidgets`

**Description**: This class manages the Jupyter widgets for interacting with AliExpress campaigns. It handles selecting campaigns, categories, languages, and actions like initialization, saving, and displaying products.

**Methods**

#### `__init__`

**Description**: Initializes the widgets and sets up the campaign editor. It creates dropdown widgets for campaigns, categories, and languages, and buttons for initialization, saving, displaying products, and opening the Google Spreadsheet.  It also initializes default values and sets up callbacks.

#### `initialize_campaign_editor`

**Description**: Initializes the `AliCampaignEditor` instance based on selected campaign, category, and language/currency.

**Parameters**:

- `_` (Any): Unused argument, required for button callback.

**Raises**:

- `FileNotFoundError`: If the campaigns directory doesn't exist.
- `Exception`: If there's an issue during the initialization process.

#### `update_category_dropdown`

**Description**: Updates the category dropdown widget with categories available for the selected campaign.

**Parameters**:

- `campaign_name` (str): The name of the campaign.

**Raises**:

- `Exception`: If there's an issue accessing campaign categories.

#### `on_campaign_name_change`

**Description**: Handles changes in the campaign name dropdown. Updates the category dropdown and reinitializes the campaign editor.

**Parameters**:

- `change` (dict): Dictionary containing the new value.

#### `on_category_change`

**Description**: Handles changes in the category dropdown. Reinitializes the campaign editor.

**Parameters**:

- `change` (dict): Dictionary containing the new value.

#### `on_language_change`

**Description**: Handles changes in the language dropdown. Updates the language and currency and reinitializes the campaign editor.

**Parameters**:

- `change` (dict): Dictionary containing the new value.

#### `save_campaign`

**Description**: Saves the selected campaign and its categories to a Google Spreadsheet.

**Parameters**:

- `_` (Any): Unused argument, required for button callback.

**Raises**:

- `Exception`: If there's an error saving the campaign.

#### `show_products`

**Description**: Displays products in the selected category.

**Parameters**:

- `_` (Any): Unused argument, required for button callback.

**Raises**:

- `Exception`: If there's an error fetching products.

#### `open_spreadsheet`

**Description**: Opens the Google Spreadsheet associated with the current campaign in a web browser.

**Parameters**:

- `_` (Any): Unused argument, required for button callback.

#### `setup_callbacks`

**Description**: Sets up the event handlers (callbacks) for the widgets.

#### `display_widgets`

**Description**: Displays the Jupyter widgets in the notebook environment, including campaign selection, category selection, language selection, initialization buttons and so on.  Immediately initializes the campaign editor with the first selected campaign.

**Raises**:

- `Exception`: If there's a problem initializing or displaying widgets.