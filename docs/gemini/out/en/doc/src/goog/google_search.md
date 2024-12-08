# Module: hypotez/src/goog/google_search.py

## Overview

This module provides a class for parsing HTML from Google Search results. It extracts various elements like organic results, featured snippets, knowledge cards, and scrolling sections, handling both mobile and desktop HTML versions.


## Classes

### `GoogleHtmlParser`

**Description**: A class for parsing HTML from Google Search results.  It parses the HTML page and converts it into a structured dictionary containing the results.  It works with both mobile and desktop versions of the Google Search HTML.

**Attributes**:

- `tree` (html.Element): The parsed HTML document tree.
- `user_agent` (str): The user agent used to retrieve the HTML. Defaults to 'desktop'.

**Methods**:

#### `__init__`

**Description**: Initializes the parser. Creates a document tree from the provided HTML string.

**Parameters**:

- `html_str` (str): The HTML string from the Google Search result page.
- `user_agent` (str, optional): The user agent to use for parsing. Can be 'mobile' or 'desktop'. Defaults to 'desktop'.

**Returns**:

- `None`


#### `_clean`

**Description**: Cleans a string by removing extra spaces and characters.

**Parameters**:

- `content` (str): The string to clean.

**Returns**:

- `str`: The cleaned string.


#### `_normalize_dict_key`

**Description**: Normalizes a string for use as a dictionary key.  Replaces spaces with underscores, removes colons, and converts to lowercase.

**Parameters**:

- `content` (str): The string to normalize.

**Returns**:

- `str`: The normalized string.


#### `_get_estimated_results`

**Description**: Extracts the estimated number of search results.

**Parameters**:

- None

**Returns**:

- `int`: The estimated number of results.


#### `_get_organic`

**Description**: Extracts organic search results.  Returns a list of dictionaries containing the URL, title, snippet, and rich snippet for each result.

**Parameters**:

- None

**Returns**:

- `list`: A list of dictionaries representing the organic search results.


#### `_get_featured_snippet`

**Description**: Extracts the featured snippet, if available.

**Parameters**:

- None

**Returns**:

- `dict | None`: A dictionary with the featured snippet's title and URL, or None if no featured snippet is found.


#### `_get_knowledge_card`

**Description**: Extracts the knowledge card, if available.

**Parameters**:

- None

**Returns**:

- `dict | None`: A dictionary containing the knowledge card's title, subtitle, description, and additional information (if any), or None if no knowledge card is found.


#### `_get_scrolling_sections`

**Description**: Extracts data from scrolling sections (e.g., top stories, tweets). Returns a list of dictionaries representing each section and its data.

**Parameters**:

- None

**Returns**:

- `list`: A list of dictionaries containing the title and data from each scrolling section.


#### `get_data`

**Description**: Retrieves all the extracted data from the parsed Google Search page.

**Parameters**:

- None

**Returns**:

- `dict`: A dictionary containing the extracted data from the Google Search page, including estimated results, featured snippet, knowledge card, organic results, and scrolling widget data.