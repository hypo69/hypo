# hypotez/src/utils/pdf.py

## Overview

This module provides utilities for converting HTML content or files to PDF format using the `pdfkit` library and an alternative approach using `fpdf`.  It also includes a function to find the project root directory.


## Functions

### `set_project_root`

**Description**: This function searches for the root directory of the project starting from the current file's directory, moving upwards.  It checks for specific marker files (pyproject.toml, requirements.txt, .git) in each parent directory. If a matching directory is found, the function returns the path to it. Otherwise, it returns the path to the directory containing the current file.  If the root directory is not in `sys.path`, it adds the path to `sys.path` and returns the root path.

**Parameters**:
- `marker_files` (tuple, optional): A tuple of filenames or directory names to identify the project root. Defaults to ('pyproject.toml', 'requirements.txt', '.git').

**Returns**:
- `Path`: Path to the root directory if found, otherwise the directory containing the current file.


### `PDFUtils.save_pdf`

**Description**: This method saves HTML content or a file to a PDF file using the `pdfkit` library.

**Parameters**:
- `data` (str | Path): The HTML content or the path to the HTML file.
- `pdf_file` (str | Path): The path to the output PDF file.

**Returns**:
- `bool`: `True` if the PDF was saved successfully, `False` otherwise.

**Raises**:
- `pdfkit.PDFKitError`: Raised if there's an error during PDF generation with `pdfkit`.
- `OSError`: Raised if there's an error accessing the file (e.g., permission issues).


### `PDFUtils.save_pdf_v2`

**Description**: This method is an alternative for saving text content to a PDF file. It utilizes the `FPDF` library.

**Parameters**:
- `data` (str): The text to be saved to the PDF.
- `pdf_file` (str | Path): The path to the output PDF file.

**Returns**:
- `bool`: `True` if the PDF was saved successfully, `False` otherwise.

**Raises**:
- `Exception`: Catches any potential errors during PDF generation using FPDF.

## Classes

### `PDFUtils`

**Description**: A class to work with PDF files. Provides methods for saving HTML content to PDF.

**Methods**:
- `save_pdf`: Saves HTML content or a file to a PDF.


## Global Variables

### `MODE`

**Description**:  A global variable set to 'dev' (string).  Likely used for configuration.

### `wkhtmltopdf_exe`

**Description**:  Stores the path to the `wkhtmltopdf` executable file. Uses the project root directory for the path.

### `configuration`

**Description**:  Configuration for `pdfkit` that sets `wkhtmltopdf` to the detected executable.

### `options`

**Description**:  Dictionary of options passed to `pdfkit` (in this case, `{"enable-local-file-access": ""}`).


## Module Notes

- The module utilizes `pdfkit` for converting HTML content to PDF.
- It includes an alternative method (`save_pdf_v2`) using `fpdf` for saving text data to a PDF.
- It includes error handling (using `try...except` blocks) and logging functionality.
- The code includes comments about the functionality and important considerations regarding `wkhtmltopdf` installation and path setup.
- The `set_project_root` function ensures the script can operate regardless of where it is executed within the project.