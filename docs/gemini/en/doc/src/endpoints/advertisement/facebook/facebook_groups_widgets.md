# facebook_groups_widgets.py

## Overview

This module provides a class for creating a dropdown widget that allows selecting Facebook groups for advertisement purposes.  It loads group URLs from a JSON file and displays them in a user-interactive dropdown.

## Table of Contents

* [Classes](#classes)
    * [FacebookGroupsWidget](#facebookgroupswidget)
        * [`__init__`](#init)
        * [`create_dropdown`](#createdropdown)
        * [`display_widget`](#displaywidget)

## Classes

### `FacebookGroupsWidget`

**Description**: This class creates a dropdown widget to select Facebook groups from a JSON file.

#### `__init__`

**Description**: Initializes the FacebookGroupsWidget with the path to the JSON file containing group URLs.

**Parameters**:

* `json_file_path` (Path): The path to the JSON file containing Facebook group information.


**Raises**:

* `FileNotFoundError`: If the specified `json_file_path` does not exist.
* `ValueError`: If the JSON data is not in the expected format, or if the file is empty.


#### `create_dropdown`

**Description**: Creates and returns a dropdown widget populated with Facebook group URLs.

**Returns**:

* `Dropdown`: The created dropdown widget containing group URLs.


#### `display_widget`

**Description**: Displays the created dropdown widget.

**Raises**:

* `Exception`: Any exception raised during the widget display process.


```python
import header
from IPython.display import display
from ipywidgets import Dropdown
from src.utils.jjson import j_loads_ns
from types import SimpleNamespace
from pathlib import Path

class FacebookGroupsWidget:
    """ Создает выпадающий список с URL групп Facebook из предоставленного JSON."""

    def __init__(self, json_file_path: Path):
        """
        Инициализация виджета с выпадающим списком для групп Facebook.

        Args:
            json_file_path (Path): Путь к JSON-файлу, содержащему информацию о группах Facebook.
        """
        try:
            self.groups_data: SimpleNamespace = j_loads_ns(json_file_path)
        except FileNotFoundError as ex:
            raise FileNotFoundError(f"File not found: {ex}") from ex
        except ValueError as ex:
            raise ValueError(f"Invalid JSON format: {ex}") from ex
        except Exception as ex:
            raise Exception(f"An error occurred: {ex}") from ex
        self.dropdown = self.create_dropdown()

    def create_dropdown(self) -> Dropdown:
        """ Создает и возвращает виджет выпадающего списка на основе данных групп.

        Returns:
            Dropdown: Виджет выпадающего списка с URL групп Facebook.
        """
        try:
            group_urls = list(self.groups_data.__dict__.keys())
            dropdown = Dropdown(
                options=group_urls,
                description='Facebook Groups:',
                disabled=False,
            )
            return dropdown
        except Exception as ex:
            raise Exception(f"An error occurred during dropdown creation: {ex}") from ex


    def display_widget(self):
        """ Отображает виджет выпадающего списка."""
        try:
            display(self.dropdown)
        except Exception as ex:
            raise Exception(f"Error displaying widget: {ex}") from ex
```