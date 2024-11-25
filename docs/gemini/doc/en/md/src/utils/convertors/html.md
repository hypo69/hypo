# hypotez/src/utils/convertors/html.py

## Overview

This module provides utilities for converting HTML to various formats, including escape sequences, dictionaries, SimpleNamespace objects, and PDF.  It includes functions for escaping HTML tags, converting escape sequences to HTML, creating dictionaries from HTML structure, and converting HTML to SimpleNamespace objects.  The module also includes a function for converting HTML to PDF using the `weasyprint` library.


## Functions

### `html2escape`

**Description**: Converts HTML tags to their corresponding escape sequences.

**Parameters**:

- `input_str` (str): The HTML code to be converted.


**Returns**:

- str: The HTML code converted to escape sequences.


**Example**:

```python
html = "<p>Hello, world!</p>"
result = html2escape(html)
print(result)  # Output: &lt;p&gt;Hello, world!&lt;/p&gt;
```


### `escape2html`

**Description**: Converts escape sequences to their corresponding HTML tags.

**Parameters**:

- `input_str` (str): The string containing HTML escape sequences.


**Returns**:

- str: The input string with escape sequences converted to HTML tags.


**Example**:

```python
escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
result = escape2html(escaped)
print(result)  # Output: <p>Hello, world!</p>
```


### `html2dict`

**Description**: Converts HTML to a dictionary where tags are keys and content is values.

**Parameters**:

- `html_str` (str): The HTML string to convert.


**Returns**:

- dict: A dictionary representing the HTML structure with tags as keys and their content as values.


**Example**:

```python
html = "<p>Hello</p><a href='link'>World</a>"
result = html2dict(html)
print(result)  # Output: {'p': 'Hello', 'a': 'World'}
```



### `html2ns`

**Description**: Converts HTML to a SimpleNamespace object.

**Parameters**:

- `html_str` (str): The HTML string to convert.


**Returns**:

- SimpleNamespace: A `SimpleNamespace` object where HTML tags are attributes and their content is values.


**Example**:

```python
html = "<p>Hello</p><a href='link'>World</a>"
result = html2ns(html)
print(result.p)  # Output: Hello
print(result.a)  # Output: World
```


### `html2pdf`

**Description**: Converts HTML content to a PDF file using WeasyPrint.

**Parameters**:

- `html_str` (str): The HTML content to convert.
- `pdf_file` (str | Path): The path to the output PDF file.


**Returns**:

- bool | None: `True` if PDF generation is successful, `None` otherwise.

**Raises**:

- Exception: An exception if PDF generation fails.


**Example**:


```python
html_content = "<html><body><h1>Hello, World!</h1></body></html>"
pdf_output_file = "output.pdf"

success = html2pdf(html_content, pdf_output_file)

if success:
    print(f"PDF generated successfully to {pdf_output_file}")
```


```
```
```
```