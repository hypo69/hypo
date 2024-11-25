# html2text Module Documentation

## Overview

This module provides functionality to convert HTML content into equivalent Markdown-formatted text.  It handles various HTML tags, including headings, paragraphs, lists, links, images, and emphasis.  The module also supports options for customization, such as wrapping long lines, skipping internal links, and using different list markers.  Additional features include handling Google Docs export and CSS parsing.


## Classes

### `_html2text`

**Description**:  A class inheriting from `HTMLParser` that parses HTML and generates Markdown output.  It manages the state of the conversion process, including active formatting elements, nesting levels, and various options for control over the generated output.


**Methods**:

- `__init__(self, out=None, baseurl='')`: Initializes the parser.
    - `out`: Output stream (default is `outtextf`).
    - `baseurl`: Base URL for resolving relative links.
- `feed(self, data)`: Feeds HTML data to the parser.
- `outtextf(self, s)`: Appends output to the `outtextlist` before joining.
- `close(self)`: Closes the parser and returns the generated Markdown text.
- `handle_charref(self, c)`: Handles character references (e.g., `&#160;`).
- `handle_entityref(self, c)`: Handles entity references (e.g., `&nbsp;`).
- `handle_starttag(self, tag, attrs)`: Handles the start of an HTML tag.
- `handle_endtag(self, tag)`: Handles the end of an HTML tag.
- `previousIndex(self, attrs)`: Finds an attribute index based on href and title matching.
- `drop_last(self, nLetters)`: Removes last n characters from the output.
- `handle_emphasis(self, start, tag_style, parent_style)`: Handles text emphasis (bold, italic, strikethrough, etc.) in a Google Document-specific manner.
- `handle_tag(self, tag, attrs, start)`: Handles various HTML tags and their attributes based on different states and options.  Contains logic for links, images, lists, blockquotes, etc.
- `pbr(self)`:  Adds a possible blank line before a paragraph
- `p(self)`:  Adds a blank line.
- `soft_br(self)`: Adds a soft line break.
- `o(self, data, puredata=0, force=0)`: Writes output data, handling various formatting and conditions (e.g., blockquotes, preformatted text, links). Includes complex logic for wrapping, spacing, and handling of abbreviations.
- `handle_data(self, data)`: Handles regular HTML data, updating internal styles and other related state variables. Includes a check for style attributes.
- `unknown_decl(self, data)`: Handles unknown declarations.




## Functions

### `wrapwrite(text)`

**Description**: Writes the provided text to standard output while accounting for Python 2 and 3 compatibility.

**Parameters**:

- `text (str)`: The text to be written.


### `html2text_file(html, out=wrapwrite, baseurl='')`

**Description**: Converts HTML to Markdown and writes the result to the specified output stream.

**Parameters**:

- `html (str)`: The HTML content to convert.
- `out`: Output stream (default is `wrapwrite`).
- `baseurl (str)`: Base URL for resolving relative links.



### `html2text(html, baseurl='')`

**Description**: Converts HTML to Markdown.


**Parameters**:

- `html (str)`: The HTML content to convert.
- `baseurl (str)`: Base URL for resolving relative links.



### `replaceEntities(s)`
**Description**: Helper function for unescaping HTML entities within regular expressions.

**Parameters**:
- `s`: A string capturing the matched part of the entity.

**Returns**:
- The unescaped entity, or if it's not possible to unescape it, the original entity.



### `unescape(s)`
**Description**: Replaces HTML entities in a string with their corresponding characters.

**Parameters**:
- `s (str)`: The string to unescape.

**Returns**:
- A new string with HTML entities replaced.


### `onlywhite(line)`
**Description**: Checks if a line contains only whitespace characters.

**Parameters**:
- `line (str)`: The line to check.

**Returns**:
- `True` if the line contains only whitespace, `False` otherwise.



### `optwrap(text)`
**Description**: Wraps long lines in the provided text.

**Parameters**:
- `text (str)`: The text to wrap.

**Returns**:
- The wrapped text as a string.


### `hn(tag)`
**Description**: Extracts the level of a heading tag (h1-h9).

**Parameters**:
- `tag (str)`: The HTML tag to check.

**Returns**:
- An integer representing the heading level (1-9) or 0 if invalid.



### `dumb_property_dict(style)`
**Description**: Parses CSS style attributes into a dictionary.

**Parameters**:
- `style (str)`: The CSS style string.

**Returns**:
- A dictionary representing the parsed style attributes.


### `dumb_css_parser(data)`
**Description**: Parses a block of CSS code into a dictionary of selectors and their styles.


**Parameters**:
- `data (str)`: CSS code to parse.

**Returns**:
- A dictionary with CSS selectors as keys and their parsed styles as values.


### `element_style(attrs, style_def, parent_style)`
**Description**: Determines the final style attributes for an element.

**Parameters**:
- `attrs`: Attributes of the element.
- `style_def`:  A dictionary mapping CSS selectors to styles.
- `parent_style`: Styles from parent element.

**Returns**:
- `dict`: Final computed styles for the element.



### `google_list_style(style)`
**Description**: Extracts the type of list (ordered or unordered) from styles.

**Parameters**:
- `style (dict)`: Element styles as a dictionary.

**Returns**:
- `str`: 'ul' for unordered, 'ol' for ordered.



### `google_nest_count(style)`
**Description**: Calculates the nesting level of Google Docs lists.


**Parameters**:
- `style (dict)`: Element styles as a dictionary.

**Returns**:
- `int`: Nesting level of the list.


### `google_has_height(style)`
**Description**: Checks if the style explicitly defines a height.

**Parameters**:
- `style (dict)`: Element styles as a dictionary.

**Returns**:
- `bool`: `True` if height is defined, `False` otherwise.



### `google_text_emphasis(style)`
**Description**: Returns a list of emphasis modifiers.

**Parameters**:
- `style (dict)`: Element styles as a dictionary.

**Returns**:
- `list`: Emphasis modifiers (e.g., "italic", "bold").



### `google_fixed_width_font(style)`
**Description**: Checks if the style defines a fixed-width font.

**Parameters**:
- `style (dict)`: Element styles as a dictionary.

**Returns**:
- `bool`: `True` if fixed-width font, `False` otherwise.


### `list_numbering_start(attrs)`
**Description**: Extracts numbering start from list attributes.

**Parameters**:
- `attrs (dict)`: Element attributes.

**Returns**:
- `int`: The numbering start value.



## Options Handling

The module accepts command-line options to customize the conversion process. See the usage information below.



## Exception Handling

The code uses `try...except` blocks to handle potential `NameError` exceptions, ensuring compatibility across Python 2 and 3 environments. Exceptions are handled using `ex`.  Some exceptions are omitted for brevity.


## Usage

```bash
python html2text.py <filename> [encoding]
```

Replace `<filename>` with the path to your HTML file and optionally specify the encoding if it's not UTF-8.  Additional command-line options are available.  Refer to the help message using `python html2text.py -h` for details.