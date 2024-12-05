# hypotez/src/suppliers/aliexpress/gui/main.py

## Overview

This module defines the main application window for managing advertising campaigns. It utilizes a tabbed interface, providing separate tabs for JSON editing, campaign management, and product editing.  The application includes features for opening, saving, copying, and pasting content within various text widgets.

## Table of Contents

* [MainApp](#mainapp)
* [Functions](#functions)
    * [open_file](#open_file)
    * [save_file](#save_file)
    * [exit_application](#exit_application)
    * [copy](#copy)
    * [paste](#paste)
    * [load_file](#load_file)
    * [main](#main)



## Classes

### `MainApp`

**Description**: The main application class, responsible for creating and managing the application's window and tabs.

**Methods**

#### `__init__`

**Description**: Initializes the `MainApp` with the main window, tab widget, and various editor tabs.

**Parameters**:
- None


#### `create_menubar`

**Description**: Creates the application's menu bar with options for file operations and editing.

**Parameters**:
- None


#### `open_file`

**Description**: Opens a file dialog to select a JSON file and loads it into the JSON editor tab.

**Parameters**:
- None


**Raises**:
-  `None`: No exception raised directly in this method but will raise exception if file is not a JSON.


#### `save_file`

**Description**: Saves the current file in the selected tab.

**Parameters**:
- None


**Raises**:
-  `None`: No exceptions raised directly in this method but will raise exception if file is not a JSON or if there's an issue with saving.



#### `exit_application`

**Description**: Closes the application.

**Parameters**:
- None


#### `copy`

**Description**: Copies selected text from the focused widget to the clipboard.

**Parameters**:
- None


**Raises**:
- `None`: No exceptions raised directly but will raise exception if no widget is in focus.


#### `paste`

**Description**: Pastes text from the clipboard into the focused widget.

**Parameters**:
- None


**Raises**:
- `None`: No exceptions raised directly but will raise exception if no widget is in focus.



#### `load_file`

**Description**: Loads a JSON file into the JSON editor.

**Parameters**:
  - `campaign_file` (str): The path to the JSON file.

**Raises**:
- `Exception`:  An exception is raised if there's a problem loading the file.


## Functions

### `main`

**Description**: Initializes and runs the application.

**Parameters**:
- None


**Raises**:
- `None`: No exception is raised directly in the method.