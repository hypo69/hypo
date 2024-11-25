# hypotez/src/endpoints/kazarinov/react/pricelist_generator.py

## Overview

This module provides a class for generating HTML and PDF reports based on data from a JSON file. It utilizes Jinja2 for HTML templating and wkhtmltopdf for PDF conversion. The class handles loading data, generating HTML, saving HTML to a file, generating PDF from HTML, and running the complete report generation process.


## Classes

### `ReportGenerator`

**Description**: This class is responsible for generating HTML and PDF reports. It takes a template, base path, timestamp, and language as input and creates reports.


**Methods**

#### `generate_html`

**Description**: Generates HTML content based on the template and the provided data.

**Parameters**:

- `data` (dict): The data to be used in rendering the template.


**Returns**:

- `str`: The generated HTML content.


#### `create_report`

**Description**: This method orchestrates the complete report generation process. It generates HTML, saves it to a file, and generates a PDF from the HTML content.

**Parameters**:

- `data` (dict): The input data for the report.
- `html_file` (str | Path): The path to save the generated HTML file.
- `pdf_file` (str | Path): The path to save the generated PDF file.


**Returns**:

- None


## Functions (None)


## Usage Example

```python
base_path = gs.path.data / 'kazarinov' / 'mexironim' / '202410262326'
data = j_loads(base_path / '202410262326_ru.json')
html_file = base_path / '202410262326_ru.html'
pdf_file = base_path / '202410262326_ru.pdf'
r = ReportGenerator()
r.create_report(data, html_file, pdf_file)
```

## Notes

- Requires Jinja2, wkhtmltopdf, and other dependencies to be installed.
- The `config` variable is used to set the wkhtmltopdf path, ensuring the tool can be located correctly.
- The use of `Path` objects is recommended for better file handling.
- The code includes error handling (e.g., exception handling) using a `logger` and potentially `try...except` blocks, which are not present in the provided example but should be added for robustness.
-  The `generate_html` method utilizes `read_text_file` to retrieve template contents rather than using `self.env.get_template` directly.  This suggests better flexibility for template loading.
- The `html2pdf` function call is present, but the actual implementation of `save_pdf` and `html2pdf` needs to be examined for completeness.