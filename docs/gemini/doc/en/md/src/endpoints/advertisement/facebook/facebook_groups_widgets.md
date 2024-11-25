# Facebook Groups Widgets

## Overview

This module provides a Facebook groups widget for selecting groups for advertisement.  It uses a dropdown menu populated with URLs from a JSON file.

## Table of Contents

* [FacebookGroupsWidget](#facebookgroupswidget)
    * [__init__](#init)
    * [create_dropdown](#createdropdown)
    * [display_widget](#displaywidget)

## Classes

### `FacebookGroupsWidget`

**Description**: Creates a dropdown widget for selecting Facebook groups from a JSON file.

**Methods**:

#### `__init__`

**Description**: Initializes the FacebookGroupsWidget with a JSON file path.

**Parameters**:

- `json_file_path` (Path): Path to the JSON file containing Facebook group URLs.

**Raises**:

- `FileNotFoundError`: If the specified JSON file does not exist.
- `ValueError`: If the JSON file's format is invalid.


#### `create_dropdown`

**Description**: Creates a dropdown widget populated with Facebook group URLs.

**Parameters**: None

**Returns**:

- `Dropdown`: A dropdown widget containing the group URLs.


#### `display_widget`

**Description**: Displays the created dropdown widget.

**Parameters**: None

**Returns**: None