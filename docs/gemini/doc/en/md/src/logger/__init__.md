# Module: hypotez/src/logger/__init__.py

## Overview

This module initializes the logger and imports various exception classes.  It sets the logging mode to 'dev'.


## Constants

### `MODE`

**Description**:  The logging mode. Currently set to 'dev'.


## Imports

### `from .logger import logger`

**Description**: Imports the logger object.


### `from .beeper import Beeper`

**Description**: Imports the Beeper class. (Currently commented out, so not documented.)


### `from .exceptions import ...`

**Description**: Imports various exception classes related to execution, settings, credentials, PrestaShop, and payload checksums.


## Exceptions

### `ExecuteLocatorException`

**Description**: Exception raised during execution locator operations.


### `DefaultSettingsException`

**Description**: Exception raised when default settings are missing or incorrect.


### `CredentialsError`

**Description**: Exception raised during credential handling.


### `PrestaShopException`

**Description**: Exception raised during PrestaShop interaction.


### `PayloadChecksumError`

**Description**: Exception raised when a payload checksum validation fails.