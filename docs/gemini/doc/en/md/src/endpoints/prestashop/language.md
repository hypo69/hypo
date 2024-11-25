# PrestaShop Language Endpoint Documentation

## Overview

This module provides functionalities for managing languages within a PrestaShop store. It leverages the `PrestaShop` API to interact with the store's language settings.  The module includes methods for adding, deleting, updating, and retrieving language details.

## Table of Contents

* [PrestaLanguage](#prestalanguage)
    * [\_\_init\_\_](#__init__)
    * [add\_language\_PrestaShop](#add_language_PrestaShop)
    * [delete\_language\_PrestaShop](#delete_language_PrestaShop)
    * [update\_language\_PrestaShop](#update_language_PrestaShop)
    * [get\_language\_details\_PrestaShop](#get_language_details_PrestaShop)



## Classes

### `PrestaLanguage`

**Description**: This class handles interactions with the PrestaShop language API. It inherits from the `PrestaShop` class, providing common API functionalities.

**Methods**

#### `__init__`

**Description**: Initializes the `PrestaLanguage` object.

**Parameters**

* `credentials` (Optional[dict | SimpleNamespace], optional): A dictionary or a SimpleNamespace object containing the API domain and API key. Defaults to `None`.
* `api_domain` (Optional[str], optional): The API domain. Defaults to `None`.
* `api_key` (Optional[str], optional): The API key. Defaults to `None`.

**Raises**

* `ValueError`: If both `api_domain` and `api_key` are not provided.

**Returns**

* None


#### `add_language_PrestaShop`

**Description**: Adds a new language to the PrestaShop store.

**Parameters**

* (no parameters shown in code)

**Returns**

* None

#### `delete_language_PrestaShop`

**Description**: Deletes a language from the PrestaShop store.

**Parameters**

* (no parameters shown in code)

**Returns**

* None

#### `update_language_PrestaShop`

**Description**: Updates an existing language in the PrestaShop store.

**Parameters**

* (no parameters shown in code)

**Returns**

* None

#### `get_language_details_PrestaShop`

**Description**: Retrieves detailed information about a specific language.

**Parameters**

* (no parameters shown in code)

**Returns**

* None


## Functions

(No functions are defined in the provided code)