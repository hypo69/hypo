# Module: hypotez/src/utils/pdf.py

## Overview

This module provides functions for converting HTML content or files to PDF format using various libraries.  It includes support for `pdfkit`, `reportlab`, `fpdf`, `WeasyPrint`, and `xhtml2pdf`.  The module also includes a function to find the project root directory.  Additional information on these libraries and potential issues is referenced.


## Table of Contents

* [Functions](#functions)
* [Class: `PDFUtils`](#class-pdfutils)


## Functions

### `set_project_root`

**Description**: This function finds the root directory of the project. It searches upwards from the current file's directory until it finds a directory containing any of the specified marker files (pyproject.toml, requirements.txt, .git).

**Parameters**:
- `marker_files` (tuple): A tuple of filenames or directory names to use as markers to identify the project root. Defaults to `('pyproject.toml', 'requirements.txt', '.git')`.

**Returns**:
- `Path`: The path to the root directory if found. Otherwise, it returns the directory where the script is located.

### `save_pdf_pdfkit`

**Description**: Saves HTML content or a file to a PDF using the `pdfkit` library.


**Parameters**:
- `data` (str | Path): HTML content as a string or a path to an HTML file.
- `pdf_file` (str | Path): The path to the output PDF file.

**Returns**:
- `bool`: `True` if the PDF was saved successfully, otherwise `False`.

**Raises**:
- `pdfkit.PDFKitError`: Raised if there's an error generating the PDF with `pdfkit`.
- `OSError`: Raised if there's an error accessing the file.
- `Exception`: Raised for unexpected errors.


### `save_pdf_fpdf`

**Description**: Saves text to a PDF using the `fpdf` library.


**Parameters**:
- `data` (str): The text to be saved in the PDF.
- `pdf_file` (str | Path): The path to the output PDF file.

**Returns**:
- `bool`: `True` if the PDF was saved successfully, otherwise `False`.

**Raises**:
- `Exception`: Raised for unexpected errors.  Includes specific `FileNotFoundError` if fonts are not found.


### `save_pdf_weasyprint`

**Description**: Saves HTML content or a file to a PDF using the `WeasyPrint` library.


**Parameters**:
- `data` (str | Path): HTML content as a string or a path to an HTML file.
- `pdf_file` (str | Path): The path to the output PDF file.

**Returns**:
- `bool`: `True` if the PDF was saved successfully, otherwise `False`.

**Raises**:
- `Exception`: Raised for unexpected errors.



### `save_pdf_xhtml2pdf`

**Description**: Saves HTML content or a file to a PDF using the `xhtml2pdf` library.

**Parameters**:
- `data` (str | Path): HTML content as a string or a path to an HTML file.
- `pdf_file` (str | Path): The path to the output PDF file.


**Returns**:
- `bool`: `True` if the PDF was saved successfully, otherwise `False`.

**Raises**:
- `Exception`: Raised for unexpected errors.  Includes specific `FileNotFoundError` if fonts are not found.


## Class: `PDFUtils`

### `PDFUtils`

**Description**: A class for working with PDF files, providing methods for saving HTML content to PDF using various libraries.


**Static Methods**:
- [`save_pdf_pdfkit`](#save_pdf_pdfkit)
- [`save_pdf_fpdf`](#save_pdf_fpdf)
- [`save_pdf_weasyprint`](#save_pdf_weasyprint)
- [`save_pdf_xhtml2pdf`](#save_pdf_xhtml2pdf)