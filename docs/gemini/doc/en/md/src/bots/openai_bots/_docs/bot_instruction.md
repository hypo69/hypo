# OpenAI Bots - Instruction Bot

## Overview

This bot provides instructions for interacting with the OpenAI model.  It details commands, expected input, and potential outputs.

## Commands

### `!hi`

**Description**: Greets the user.

**Example Usage**: `!hi`

**Output**: A greeting message.


### `!train <data> <data_dir> <positive> <attachment>`

**Description**: Trains the model with the provided data. Use `data` for a file, `data_dir` for a directory, or `attachment` for a file attachment.

**Parameters**:

* `<data>` (str): The path to the data file (if using a file).
* `<data_dir>` (str): The path to the directory containing the data (if using a directory).
* `<positive>` (str): A label or indicator for positive examples within the data.
* `<attachment>` (str): The name of the attached file (if applicable).

**Example Usage**: `!train my_training_data.json my_training_directory positive`


### `!test <test_data>`

**Description**: Tests the model with provided JSON test data.

**Parameters**:

* `<test_data>` (str): Path to the JSON file containing the test data.


**Example Usage**: `!test test_data.json`


### `!archive <directory>`

**Description**: Archives files in the specified directory.

**Parameters**:

* `<directory>` (str): The path to the directory to be archived.

**Example Usage**: `!archive my_archive_directory`


### `!select_dataset <path_to_dir_positive> <positive>`

**Description**: Selects a dataset for training from the specified directory.

**Parameters**:

* `<path_to_dir_positive>` (str): Path to the directory containing positive examples.
* `<positive>` (str):  The positive label for this dataset.

**Example Usage**: `!select_dataset my_positive_dataset_dir positive`


### `!instruction`

**Description**: Displays this instruction message.

**Example Usage**: `!instruction`

**Output**: The complete instruction set.