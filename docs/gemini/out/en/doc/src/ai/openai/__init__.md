# openai

## Overview

This module provides functionality related to interacting with the OpenAI API. It includes a translator and an OpenAI model.


## Modules

### `translator`

**Description**:  This module contains the translation functionality.


### `model`

**Description**: This module contains the OpenAI model class.


## Classes

### `OpenAIModel`

**Description**:  This class represents an OpenAI model.


## Functions

### `translate`

**Description**:  This function handles the translation process using an appropriate translation method.

**Parameters**:
- `text` (str): The text to be translated.
- `source_lang` (str): The source language code (e.g., 'en', 'fr').
- `target_lang` (str): The target language code (e.g., 'es', 'de').

**Returns**:
- `str | None`: The translated text if successful, otherwise `None`.


**Raises**:
- `ValueError`: If the input text is empty or if the source or target language codes are invalid.
- `OpenAIAPIError`: If there's an error interacting with the OpenAI API.


```python
def translate(text: str, source_lang: str, target_lang: str) -> str | None:
    """
    Args:
        text (str): The text to be translated.
        source_lang (str): The source language code (e.g., 'en', 'fr').
        target_lang (str): The target language code (e.g., 'es', 'de').

    Returns:
        str | None: The translated text if successful, otherwise `None`.

    Raises:
        ValueError: If the input text is empty or if the source or target language codes are invalid.
        OpenAIAPIError: If there's an error interacting with the OpenAI API.
    """
    pass
```