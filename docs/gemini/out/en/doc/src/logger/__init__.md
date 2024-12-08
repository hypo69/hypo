# hypotez/src/logger/__init__.py

## Overview

This module provides logging functionality and defines exceptions for the `hypotez` project. It imports essential components from submodules within the `src.logger` package. The current logging mode is set to 'dev'.

## Constants

### `MODE`

**Description**:  A constant string representing the current logging mode.

**Value**: 'dev'


## Imports

This module imports the following:

- `logger` from `.logger`:  The primary logging object.
- `ExecuteLocatorException`, `DefaultSettingsException`, `CredentialsError`, `PrestaShopException`, and `PayloadChecksumError` from `.exceptions`:  Custom exception classes defining specific error scenarios.


## Exceptions

### `ExecuteLocatorException`

**Description**: Exception raised when an error occurs during execution locator retrieval.


### `DefaultSettingsException`

**Description**: Exception raised when there's an issue with default settings.


### `CredentialsError`

**Description**: Exception raised when credentials are invalid or missing.


### `PrestaShopException`

**Description**: Exception raised when a PrestaShop-related error occurs.


### `PayloadChecksumError`

**Description**: Exception raised when a payload checksum validation fails.