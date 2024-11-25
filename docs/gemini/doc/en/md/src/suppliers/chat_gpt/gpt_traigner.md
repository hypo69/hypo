# GPT Traigner Module Documentation

## Overview

This module provides functionality for training a chat GPT model. It retrieves conversation data from HTML files, cleans the data, and saves it to various formats (JSONL, CSV, raw text).  It also involves sentiment analysis and potentially model interaction.

## Table of Contents

* [GPT Traigner Class](#gpt-traigner-class)
    * [__init__ Method](#init-method)
    * [determine_sentiment Method](#determine-sentiment-method)
    * [save_conversations_to_jsonl Method](#save-conversations-to-jsonl-method)
    * [dump_downloaded_conversations Method](#dump-downloaded-conversations-method)


## Classes

### `GPT_Traigner`

**Description**: This class handles the training process, including data retrieval, cleaning, and saving.

**Methods**

#### `__init__`

**Description**: Initializes the `GPT_Traigner` object.

**Parameters**:
  -  None


#### `determine_sentiment`

**Description**: Determines the sentiment label for a conversation pair.


**Parameters**:
 - `conversation_pair` (dict[str, str]): The conversation pair to analyze.
 - `sentiment` (str, optional): The default sentiment label. Defaults to 'positive'.


**Returns**:
 - str: The sentiment label ('positive' or 'negative').


#### `save_conversations_to_jsonl`

**Description**: Saves conversation pairs to a JSONL file.


**Parameters**:
 - `data` (list[dict]): The conversation data to save.
 - `output_file` (str): The path to the output JSONL file.


**Raises**:
- `IOError`: If there's an error writing to the file.


#### `dump_downloaded_conversations`

**Description**: Collects conversations from downloaded HTML files, cleans them, and saves the processed data to CSV, JSONL, and raw text files.


**Parameters**:
  - None


**Raises**:
- `Exception`: If there's a problem accessing or processing files.


## Functions (global)


(Note:  There are no separate global functions defined in this file, all functionality is handled within the `GPT_Traigner` class.)

## Usage Example

```python
traigner = GPT_Traigner()
traigner.dump_downloaded_conversations()
```

This code initializes a `GPT_Traigner` object and calls the `dump_downloaded_conversations` method to retrieve, clean, and save the conversations.


```
```
```python
```


```
```
```python
```
```python