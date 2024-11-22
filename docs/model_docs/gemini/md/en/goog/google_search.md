```markdown
# Module: hypotez/src/goog/google_search.py

## Overview

This module provides a class for parsing HTML from Google Search results.  It extracts various information, including organic results, featured snippets, knowledge cards, and scrolling sections, and structures the output as a Python dictionary.  It supports both mobile and desktop versions of the Google search results page.


## Classes

### `GoogleHtmlParser`

**Description**: This class parses the HTML content of a Google Search result page and extracts relevant information.  It handles both mobile and desktop layouts.


**Methods**:

#### `__init__`

**Description**: Initializes the `GoogleHtmlParser` object. Parses the provided HTML string into an lxml Element tree.

**Parameters**:
- `html_str` (str): The HTML string of the Google Search results page.
- `user_agent` (str, optional): The user agent used to fetch the HTML. Defaults to 'desktop'.  Valid values are 'mobile' or 'desktop'.

**Returns**:
- None


#### `_clean`

**Description**: Removes extra whitespace and characters from a string.


**Parameters**:
- `content` (str): The string to clean.

**Returns**:
- str: The cleaned string.


#### `_normalize_dict_key`

**Description**: Normalizes a string to be used as a dictionary key (e.g., converts spaces to underscores, removes colons).


**Parameters**:
- `content` (str): The string to normalize.

**Returns**:
- str: The normalized string.


#### `_get_estimated_results`

**Description**: Extracts the estimated number of search results from the page.

**Returns**:
- int: The estimated number of results.


#### `_get_organic`

**Description**: Extracts the organic search results from the page.


**Returns**:
- list: A list of dictionaries, where each dictionary represents a search result (containing URL, title, snippet, rich snippet).


#### `_get_featured_snippet`

**Description**: Extracts the featured snippet (if present).


**Returns**:
- dict | None: A dictionary containing the snippet title and URL, or None if no featured snippet is found.


#### `_get_knowledge_card`

**Description**: Extracts the knowledge card (if present).

**Returns**:
- dict | None: A dictionary containing the knowledge card information (title, subtitle, description, more_info), or None if no knowledge card is found.


#### `_get_scrolling_sections`

**Description**: Extracts data from scrolling sections on the page.

**Returns**:
- list: A list of dictionaries representing the scrolling sections (with titles and associated data).


#### `get_data`

**Description**: Collects all the extracted data from the page into a single dictionary.

**Returns**:
- dict: A dictionary containing the estimated results, featured snippet, knowledge card, organic results, and scrolling widget data.


## Functions

(None)


```
