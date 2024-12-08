# Bot Instructions

## Overview

This document outlines the available commands and their functionalities for the chatbot.

## Commands

### `!hi`

**Description**: Greets the user.

**Usage**: `!hi`

**Example**: `!hi`  (Output: Hello!)


### `!train`

**Description**: Trains the model with the provided data.

**Usage**: `!train <data> <data_dir> <positive> <attachment>`

**Parameters**:

* `<data>` (str): Path to a file containing the training data.
* `<data_dir>` (str): Path to a directory containing the training data.
* `<positive>` (str):  Specify whether it's positive data, e.g. 'positive', 'negative'.
* `<attachment>` (Optional[str | dict | str], optional): Path to a file to be attached to the data during training. Defaults to `None`.


**Example**:

```
!train data.json data_dir/ positive
```

```
!train data.json data_dir/ positive attachment.txt
```

**Note**: Only one of `<data>` or `<data_dir>` should be provided.  `<attachment>` is optional.


### `!test`

**Description**: Tests the model with provided JSON test data.

**Usage**: `!test <test_data>`

**Parameters**:

* `<test_data>` (str): Path to a JSON file containing the test data.


**Example**:

```
!test test_data.json
```

**Returns**:
- `dict | None`: A dictionary containing the results of the test. Returns `None` if there's an error.

**Raises**:
- `ValueError`: If the `test_data` is not a valid JSON file.


### `!archive`

**Description**: Archives files in the specified directory.

**Usage**: `!archive <directory>`

**Parameters**:

* `<directory>` (str): Path to the directory to archive.


**Example**:

```
!archive my_documents/
```

**Raises**:
- `FileNotFoundError`: If the directory specified does not exist.


### `!select_dataset`

**Description**: Selects a dataset for training from the specified directory.

**Usage**: `!select_dataset <path_to_dir_positive> <positive>`

**Parameters**:

* `<path_to_dir_positive>` (str): Path to the directory containing the positive dataset.
* `<positive>` (str): Indicates the type of dataset to select.


**Example**:

```
!select_dataset data/positive data
```


**Returns**:
- `dict | None`: Returns a dictionary containing metadata about the selected dataset if successful, or `None` if an error occurs.

**Raises**:
- `FileNotFoundError`: If the specified directory does not exist.


### `!instruction`

**Description**: Displays this instruction message.

**Usage**: `!instruction`

**Example**: `!instruction`
```