# Module: hypotez/src/suppliers/aliexpress/gapi/__init__.py

## Overview

This module initializes the AliExpress GAPI (presumably a Google API) supplier for the `hypotez` project. It defines a global `MODE` variable, imports necessary modules from the `packaging` library, and imports version information.

## Variables

### `MODE`

**Description**: A global string variable defining the operation mode (e.g., 'dev', 'prod').

**Value**: 'dev'

## Imports

### `from packaging.version import Version`

**Description**: Imports the `Version` class from the `packaging` library for version comparisons.

### `from .version import __version__, __doc__, __details__`

**Description**: Imports version information, documentation, and details specific to this module (likely located in a separate `version.py` file).