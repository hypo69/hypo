```
## File hypotez/src/utils/file.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""\n.. module: src.utils \n\t:platform: Windows, Unix\n\t:synopsis:  Module for file operations\n\n"""\nMODE = 'dev'\n\n\nimport os\nimport json\nimport fnmatch\nfrom pathlib import Path\nfrom typing import List, Optional, Union, Generator\nfrom src.logger import logger\n\n\ndef save_text_file(\n    data: str | list[str] | dict,\n    file_path: Union[str, Path],\n    mode: str = "w",\n    exc_info: bool = True,\n) -> bool:\n    """\n    Save data to a text file.\n\n    Args:\n        data (str | list[str] | dict): Data to write (can be string, list of strings, or dictionary).\n        file_path (str | Path): Path where the file will be saved.\n        mode (str, optional): Write mode (`w` for write, `a` for append). Defaults to \'w\'.\n        exc_info (bool, optional): If True, logs traceback on error. Defaults to True.\n\n    Returns:\n        bool: True if the file was successfully saved, False otherwise.\n    """\n    try:\n        file_path = Path(file_path)\n        file_path.parent.mkdir(parents=True, exist_ok=True)\n\n        with file_path.open(mode, encoding="utf-8") as file:\n            if isinstance(data, list):\n                file.writelines(f"{line}\\n" for line in data)\n            elif isinstance(data, dict):\n                json.dump(data, file, ensure_ascii=False, indent=4)\n            else:\n                file.write(data)\n        return True\n    except Exception as ex:\n        logger.error(f"Failed to save file {file_path}.", ex, exc_info=exc_info)\n        return False\n\ndef read_text_file(\n    file_path: Union[str, Path],\n    as_list: bool = False,\n    extensions: Optional[list[str]] = None,\n    exc_info: bool = True,\n) -> Union[str, list[str], None]:\n    # ... (rest of the code)\n```

**<algorithm>**

```mermaid
graph TD
    A[Input: file_path, as_list, extensions] --> B{Is file?};
    B -- Yes --> C[Open file];
    C --> D[Read lines (as_list=True) or read all (as_list=False)];
    D --> E[Return content];
    B -- No --> F{Is directory?};
    F -- Yes --> G[Get all files (with extensions)];
    G --> H[Read each file recursively];
    H --> I[Collect results];
    I --> E;
    F -- No --> J[Invalid path];
    J --> K[Log warning];
    K --> E;
    subgraph Error Handling
        D -- Error --> L[Log error];
        L --> M[Return None];
        G -- Error --> L;
        H -- Error --> L;
    end
```

**Example:**

If `file_path` is a file, the content will be read line by line or as a single string.

If `file_path` is a directory, all files within it and its subdirectories will be read (optionally filtering by extensions), and their contents concatenated into a single list or string.


**<explanation>**

**Imports:**

* `os`: Provides operating system-related functions (like file system operations).
* `json`: Used for handling JSON data.
* `fnmatch`: Provides functions to match filenames against patterns.
* `pathlib`: Provides a more object-oriented way to work with file paths (using `Path`).
* `typing`: Provides type hints for better code clarity and maintainability.
* `src.logger`: Likely a custom logger module, probably handles logging messages. This relationship shows the module depends on logging facilities for error/warning reporting.

**Classes:**

There are no classes defined in this file.  All functionality is contained within functions.

**Functions:**

* `save_text_file(data, file_path, mode="w", exc_info=True)`: Saves data to a file.  Takes various data types (string, list of strings, or dictionary) and writes it to the specified file path in the specified mode. Handles potential errors and uses the logger if `exc_info` is `True`.
    * **Example:**
      ```python
      save_text_file(["line 1", "line 2"], "my_file.txt")
      save_text_file({"key": "value"}, "my_file.json")
      ```

* `read_text_file(file_path, as_list=False, extensions=None, exc_info=True)`: Reads a file or a directory of files and returns its contents. If the input is a directory, it reads all files within the directory and subdirectories, filtering by extensions if provided.
    * **Example:**
      ```python
      content = read_text_file("my_file.txt")  # Reads the entire file
      lines = read_text_file("my_dir", as_list=True) #Reads all files within and subdirectories
      ```


* `get_filenames(directory, extensions="*", exc_info=True)`: Returns a list of filenames in a directory, optionally filtered by extension.
    * **Example:**
      ```python
      filenames = get_filenames("my_dir", "*.txt") #Get all .txt files
      ```
* `recursively_yield_file_path(root_dir, patterns="*", exc_info=True)`:  A generator function to yield file paths matching given patterns.  This is useful for iterating over results without loading them all into memory.

* `recursively_get_file_path(root_dir, patterns="*", exc_info=True)`: Returns a list of file paths matching given patterns (recursive).

* `recursively_read_text_files(root_dir, patterns, as_list=False, exc_info=True)`: Recursively reads files in a directory matching specified patterns into a list.  Crucially handles both single and multiple patterns and supports returning files as a list of lines or entire file contents.
    * **Example:**
        ```python
        contents = recursively_read_text_files("/path/to/root", ["*.txt", "*.md"])
        ```


* `get_directory_names(directory, exc_info=True)`:  Retrieves all directory names within a given directory.

* `read_files_content(root_dir, patterns, as_list=False, exc_info=True)`:  Reads content from multiple files matching given patterns. Uses `recursively_get_files` to find files.


* `remove_bom(file_path)`: Removes BOM (Byte Order Mark) from a text file.


* `traverse_and_clean(directory)`: Traverses a directory, finds all Python files, and removes BOM.


* `main()`: Entry point for BOM removal.  Sets the root directory and calls `traverse_and_clean`.

**Variables:**

* `MODE`: A string variable probably used to control logging behaviors.
* `logger`: A reference to a logger object, likely from the `src.logger` module.  Used for error and warning messages.

**Potential Errors/Improvements:**

* **Robustness:** The code includes `try...except` blocks, which is good for error handling, but exception messages could be more informative in specific cases.
* **Efficiency (for `recursively_read_text_files`):** Reading the entire file contents in a loop might not be efficient for very large files.  Consider using `file.readline()` or `file.readlines()` for line-by-line processing and file handles when appropriate.
* **Clarity:** The functions could use even more comprehensive docstrings to describe the different edge cases and possible errors, especially the `recursively_read_text_files` and `read_files_content` functions.  Clearer variable naming (like `target_dir` instead of `root_dir` in some cases) could improve readability.

**Relationships:**

The `file.py` module interacts strongly with the `logger` module (imported from `src.logger`).  The dependency on `src.logger` is explicit. It could also be related to other modules in the `hypotez` project if it's designed to save or read data to files that other components need. The relationships are shown by the import statements.