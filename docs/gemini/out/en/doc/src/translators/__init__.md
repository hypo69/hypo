# translators/__init__.py

## Overview

This module initializes the translators package.  It currently defines a single global variable `MODE` with a value of 'dev'. This variable likely controls operational mode.


## Variables

### `MODE`

**Description**:  A global variable that sets the operational mode of the application.

**Value**: 'dev'

**Purpose**:  Presumably used to control runtime behavior and/or configuration. For example, it might direct the application towards development settings, testing or production.


## Usage Example

```python
import translators

print(translators.MODE)  # Output: dev
```