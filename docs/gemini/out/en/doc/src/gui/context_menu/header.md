# hypotez/src/gui/context_menu/header.py

## Overview

This module defines paths to various binary directories (GTK, FFmpeg, Graphviz) and handles adding these paths to the system path.  It also loads the project name from a settings.json file and sets the root path for the project. Additionally, it handles potential missing paths and sets the WeasyPrint DLL directories.

## Functions

### `__init__`

**Description**: This function is implicit and handles the initialization of various paths in order to enable external modules to function correctly.

**Returns**:
- `None`: This function does not explicitly return a value.


### `Path.cwd().resolve().parents[Path.cwd().parts.index(project_name)]`


**Description**: This function resolves the current working directory and navigates up to the parent directory containing the project.

**Parameters**:

- `project_name` (str): The name of the project. This is loaded from the `settings.json` file and will be used to locate the project directory.

**Returns**:
- `Path`: Returns the absolute path to the project root directory.


### `Path(__root__ / "bin" / "gtk" / "gtk-nsis-pack" / "bin")`

**Description**: This function constructs the path to the GTK bin directory, using the absolute path of the root directory.

**Parameters**:
- `__root__` (Path):  The absolute path to the project's root directory.

**Returns**:
- `Path`: The absolute path to the GTK bin directory.


### `Path(__root__ / "bin" / "ffmpeg" / "bin")`

**Description**: This function constructs the path to the FFmpeg bin directory, using the absolute path of the root directory.

**Parameters**:
- `__root__` (Path):  The absolute path to the project's root directory.

**Returns**:
- `Path`: The absolute path to the FFmpeg bin directory.


### `Path(__root__ / "bin" / "graphviz" / "bin")`


**Description**: This function constructs the path to the Graphviz bin directory, using the absolute path of the root directory.

**Parameters**:
- `__root__` (Path):  The absolute path to the project's root directory.

**Returns**:
- `Path`: The absolute path to the Graphviz bin directory.


### `json.load(settings_file)`


**Description**: Loads the settings from the specified JSON file.


**Parameters**:
- `settings_file` (File): A file object representing the JSON file.

**Returns**:
- `settings`: A Python dictionary containing the loaded JSON settings.


### `settings.get("project_name", "hypotez")`


**Description**: Retrieves the project name from the settings.


**Parameters**:
- `settings` (dict): The loaded settings dictionary.

**Returns**:
- `str`: The project name from the settings, or "hypotez" if not found.



### `sys.path.append(str(__root__))`


**Description**: Appends the project root path to the Python system path.


**Parameters**:
- `__root__` (Path): The absolute path to the project root.


### `sys.path.insert(0, str(bin_path))`


**Description**: Inserts a path to a bin directory into the beginning of the system path list.


**Parameters**:
- `bin_path` (Path): The path to be inserted.


### `sys.path.insert(0, str(gtk_bin_path))`


**Description**: Inserts the GTK bin path into the beginning of the system path.


**Parameters**:
- `gtk_bin_path` (Path): The path to the GTK bin directory.


### `warnings.filterwarnings("ignore", category=UserWarning)`


**Description**:  Suppresses UserWarnings. This prevents warnings from certain libraries from being displayed in the console.