# Module: google_search.py

## Overview

This module provides a class for parsing HTML from Google Search results.  It extracts various elements from the HTML, including organic results, featured snippets, knowledge cards, and potentially scrolling sections, and returns them as a structured dictionary.  It handles both mobile and desktop versions of the Google search page HTML.


## Classes

### `GoogleHtmlParser`

**Description**: This class parses HTML from Google Search results and converts it into a structured dictionary. It works with both mobile and desktop versions of the Google search page.

**Attributes**:

- `tree (html.Element)`: The parsed HTML document tree.
- `user_agent (str)`: The user agent used to retrieve the HTML (defaults to 'desktop').


**Methods**:

#### `__init__`

**Description**: Initializes the `GoogleHtmlParser`.

**Parameters**:

- `html_str (str)`: The HTML content as a string.
- `user_agent (str, optional):` The user agent for the request (either 'mobile' or 'desktop'). Defaults to 'desktop'.

**Returns**:
- `None`


#### `_clean`

**Description**: Cleans a string by removing extra whitespace and characters.

**Parameters**:

- `content (str)`: The string to clean.

**Returns**:
- `str`: The cleaned string.


#### `_normalize_dict_key`

**Description**: Normalizes a string for use as a dictionary key.

**Parameters**:

- `content (str)`: The string to normalize.

**Returns**:
- `str`: The normalized string.


#### `_get_estimated_results`

**Description**: Retrieves the estimated number of search results.

**Returns**:
- `int`: The estimated number of search results.


#### `_get_organic`

**Description**: Extracts organic search results.

**Returns**:
- `list`: A list of dictionaries, each representing an organic search result.


#### `_get_featured_snippet`

**Description**: Retrieves the featured snippet, if present.

**Returns**:
- `dict | None`: A dictionary containing the featured snippet information (title and URL) or `None` if not found.


#### `_get_knowledge_card`

**Description**: Retrieves the knowledge card, if present.

**Returns**:
- `dict | None`: A dictionary containing the knowledge card information (title, subtitle, description, and more information) or `None` if not found.


#### `_get_scrolling_sections`

**Description**: Retrieves data from scrolling sections on the page (e.g., top stories).

**Returns**:
- `list`: A list of dictionaries, each representing a scrolling section with its title and data.


#### `get_data`

**Description**: Retrieves all the data from the Google Search page.

**Returns**:
- `dict`: A dictionary containing the extracted data, including estimated results, featured snippet, knowledge card, organic results, and scrolling sections.


## Functions

**(None)**


## Module Variables


### `MODE`

**Description**: Stores the current mode (e.g., 'dev' for development).


## Notes

The code utilizes the `lxml` library for HTML parsing.  Error handling is present, but not explicitly documented as exceptions are handled internally.