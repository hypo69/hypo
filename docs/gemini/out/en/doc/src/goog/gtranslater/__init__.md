# gtranslater

## Overview

This module provides a function for translating text using the Google Translate API. It includes automatic language detection for the input text if the source language is not explicitly specified. It also includes error handling and logging for better robustness.

## Table of Contents

* [translate](#translate)
* [main](#main)


## Functions

### `translate`

**Description**: Translates text from one language to another using the Google Translate API.  Automatically detects the input language if not provided.

**Parameters**:

* `text` (str): The text to be translated.
* `locale_in` (str, optional): The input language code. Defaults to None (auto-detected).
* `locale_out` (str, optional): The output language code. Defaults to 'EN'.

**Returns**:

* `str`: The translated text.  Returns an empty string (`""`) if translation fails.

**Raises**:

* `Exception`: Any exceptions raised during translation (e.g., network issues, invalid input).


### `main`

**Description**: This function is a simple command-line interface for testing the translation functionality. It prompts the user for input text, source language, and target language, then calls the `translate` function to perform the translation and prints the result.

**Parameters**:

* None (This function takes input from the user).


**Returns**:

* None (Prints the translated text to the console).