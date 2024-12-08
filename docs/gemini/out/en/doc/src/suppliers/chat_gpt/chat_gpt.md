# Chat GPT Supplier

## Overview

This module defines the `ChatGpt` class, which provides functionality related to handling conversations, likely in HTML format. It utilizes the `gs` module for file path management and `recursively_read_text_files` function (presumed from the import) for potentially processing files within conversation directories.

## Classes

### `ChatGpt`

**Description**: This class encapsulates methods for managing and potentially processing chat conversations stored as HTML files.

**Methods**:

#### `yeld_conversations_htmls`

**Description**: This method yields (presumably via a generator) HTML files from a directory of conversations.

**Parameters**:

* None

**Returns**:

* `str`: Returns the content of an HTML file.  This method is likely intended to yield, not return a single value.


## Functions

(No functions are defined in the provided snippet)


## Modules Used

- `header`
- `pathlib`
- `gs` (presumed to be a module for file system interaction)
- `src.utils.file` (presumed to contain the `recursively_read_text_files` function)


**Note**: The provided code snippet is incomplete and lacks critical details about the `gs` module, `recursively_read_text_files` function, and the intended behavior of `yield_conversations_htmls` (especially regarding error handling and the structure of the returned data).  A complete and usable documentation requires the full implementation of the class and functions.