# hypotez/src/suppliers/aliexpress/gui/main.py

## Overview

This module defines the main application window for managing advertising campaigns on AliExpress. It provides a graphical user interface (GUI) with tabs for various functionalities, including JSON editing, campaign management, and product management.  The application includes functionalities for opening, saving, and editing JSON files, as well as basic clipboard operations.

## Table of Contents

* [Classes](#classes)
    * [`MainApp`](#class-mainapp)
* [Functions](#functions)
    * [`main`](#function-main)


## Classes

### `MainApp`

**Description**: The `MainApp` class represents the main application window. It manages tabs for different functionalities, including JSON editing, campaign management, and product management.

**Methods**:

#### `__init__(self)`

**Description**: Initializes the main application window with tabs.

**Parameters**:

* None


#### `create_menubar(self)`

**Description**: Creates a menu bar with options for file operations and edit commands.


**Parameters**:

* None


#### `open_file(self)`

**Description**: Opens a file dialog to select and load a JSON file. Loads the file into the currently active tab.


**Parameters**:

* None


#### `save_file(self)`

**Description**: Saves the current file based on the active tab.


**Parameters**:

* None


#### `exit_application(self)`

**Description**: Exits the application.


**Parameters**:

* None


#### `copy(self)`

**Description**: Copies selected text to the clipboard from the focused widget.


**Parameters**:

* None


#### `paste(self)`

**Description**: Pastes text from the clipboard into the focused widget.


**Parameters**:

* None


#### `load_file(self, campaign_file)`

**Description**: Loads a JSON file specified by the `campaign_file` path into the JSON editor tab.


**Parameters**:

* `campaign_file` (str): The path to the JSON file to load.


**Raises**:

* `Exception`: If there's an error loading the file, an exception is raised and an error message is displayed.


## Functions

### `main`

**Description**: Initializes and runs the application.


**Parameters**:

* None


**Raises**:

* None


**Returns**:

* None