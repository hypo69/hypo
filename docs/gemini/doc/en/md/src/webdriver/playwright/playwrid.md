# Playwrid Crawler

## Overview

This module defines the `Playwrid` class, a subclass of `PlaywrightCrawler`. It provides additional functionality for configuring browser settings, profiles, and launch options using Playwright.  This class is designed to enhance the capabilities of the `PlaywrightCrawler` by enabling customization of the Playwright browser instance.

## Table of Contents

* [Playwrid](#playwrid)
    * [\_\_init\_\_](#__init__)
    * [\_load\_settings](#_load_settings)
    * [\_set\_launch\_options](#_set_launch_options)
    * [start](#start)

## Classes

### `Playwrid`

**Description**: A subclass of `PlaywrightCrawler` for enhanced Playwright browser control.

**Methods**:

#### `__init__`

**Description**: Initializes the Playwright Crawler with custom launch options, settings, and user agent.

**Parameters**:

- `settings_name` (Optional[str], optional): Name of the settings file to use. Defaults to None.
- `user_agent` (Optional[Dict[str, Any]], optional): A dictionary containing user agent settings. Defaults to None.


**Raises**:
-  Any exceptions raised by `super().__init__`.


#### `_load_settings`

**Description**: Loads the settings for the Playwrid Crawler.

**Parameters**:

- `settings_name` (Optional[str], optional): Name of the settings file to use. Defaults to None.

**Returns**:

- `SimpleNamespace`: A `SimpleNamespace` object containing the settings.


#### `_set_launch_options`

**Description**: Configures the launch options for the Playwright Crawler.

**Parameters**:

- `settings` (SimpleNamespace): A `SimpleNamespace` object containing launch settings.

**Returns**:

- `Dict[str, Any]`: A dictionary with launch options for Playwright.


#### `start`

**Description**: Starts the Playwrid Crawler and navigates to the specified URL.

**Parameters**:

- `url` (str): The URL to navigate to.


**Raises**:

- Any exception that occurs during the crawling process.  The error is logged using `logger.critical`.


## Functions

(No functions defined in the provided code)