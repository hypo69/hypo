# hypotez/src/endpoints/kazarinov/react/pricelist_generator.py

## Overview

This module provides a class for generating HTML and PDF reports for Mekhiron data from Kazarinove.  It utilizes Jinja2 for HTML templating and wkhtmltopdf for PDF conversion.  Data is loaded from a JSON file, and the generated HTML is saved to a file, followed by conversion to PDF.

## Table of Contents

* [Classes](#classes)
    * [`ReportGenerator`](#reportgenerator)
* [Functions](#functions)
    * [`main`](#main)

## Classes

### `ReportGenerator`

**Description**: A class responsible for generating HTML and PDF reports from data loaded from JSON.

**Methods**

#### `generate_html(self, data: dict) -> str`

**Description**: Generates HTML content based on a Jinja2 template and provided data.

**Parameters**:

- `data` (dict): Dictionary containing the data to be rendered in the template.

**Returns**:

- `str`: Generated HTML content.

#### `create_report(self, data: dict, html_file: str | Path, pdf_file: str | Path) -> None`

**Description**: Executes the complete report generation process, from HTML generation to PDF creation.

**Parameters**:

- `data` (dict): Data dictionary to be used for HTML generation.
- `html_file` (str | Path): The path to the output HTML file.
- `pdf_file` (str | Path): The path to the output PDF file.

**Returns**:

- `None`

## Functions

### `main(mexiron: str, lang: str) -> bool`

**Description**: This function orchestrates the entire process of report generation.  It loads data, generates HTML, and creates the PDF document.

**Parameters**:

- `mexiron` (str): The identifier (e.g., filename) of the Mekhiron record.
- `lang` (str): Language code for the report (e.g., 'ru').

**Returns**:

- `bool`:  The function's success status (though not explicitly used in the example).

**Raises**:
- `FileNotFoundError`: If the input JSON file is not found.
- Any exceptions raised during PDFKit conversion (implicitly handled).


## Usage Example

```python
mexiron = '24_12_01_03_18_24_269'
lang = 'ru'
main(mexiron, lang)
```

This example demonstrates how to use the `main` function to generate a report for a given Mekhiron and language.  Ensure the necessary input JSON file (e.g., `ru.json`) exists in the designated directory.


```
```
```
```
```