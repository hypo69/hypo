# hypotez/src/gui/context_menu/qt6/header.py

## Overview

This module, `hypotez/src/gui/context_menu/qt6/header.py`, is a part of the Hypotez project. It likely contains constants, imports, and possibly some setup configurations for the Qt6-based context menu within the GUI framework.  The module appears to primarily deal with setting up paths and environment variables.


## Constants

### `MODE`

**Description**: A string variable representing the current development mode (e.g., 'dev', 'prod').

**Value**: 'dev'

## Imports

**Description**: This section lists the imported modules.

- `sys`
- `os`
- `pathlib` (specifically `Path`)


## Variables

### `__root__`

**Description**: A `pathlib.Path` object representing the root directory of the Hypotez project.

**Details**:
- Calculated by finding the index of 'hypotez' in the current working directory (`os.getcwd()`) and constructing a new path from that point.

## Functions (None defined)

## Classes (None defined)