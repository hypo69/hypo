# Tiny Utils

## Overview

**Tiny Utils** is a utility library providing a set of lightweight helper functions for various common tasks. The library includes utilities for data format conversion, text and file processing, string operations, date and time formatting, image processing, and more. It is organized into modules for easy access to specific functionalities.


## Table of Contents

- [Tiny Utils](#tiny-utils)
  - [Overview](#overview)
  - [Installation](#installation)
  - [Modules Overview](#modules-overview)
  - [Modules Description](#modules-description)
    - [Convertors](#convertors)
      - [Files:](#files)
    - [String Utilities](#string-utilities)
    - [File Utilities](#file-utilities)
    - [Date and Time Utilities](#date-and-time-utilities)
    - [FTP Utilities](#ftp-utilities)
    - [Image Utilities](#image-utilities)
    - [PDF Utilities](#pdf-utilities)
    - [Printer Utilities](#printer-utilities)
  - [Usage Examples](#usage-examples)
    - [Text to PNG Conversion](#text-to-png-conversion)
    - [XML to Dictionary Conversion](#xml-to-dictionary-conversion)
    - [JSON Parsing and Manipulation](#json-parsing-and-manipulation)
  - [Contributing](#contributing)
  - [License](#license)


## Installation

To use **Tiny Utils**, clone the repository and install the necessary dependencies as specified in the `requirements.txt` file.

```bash
git clone https://github.com/hypo69/tiny-utils.git
cd tiny_utils
pip install -r requirements.txt
```


## Modules Overview

The library contains several submodules, each handling a specific task:

- **Convertors**: Modules for converting data formats, such as text to image, WebP to PNG, JSON, XML, Base64 encoding, and more.
- **String Utilities**: Tools for advanced string manipulation.
- **File Utilities**: Functions for processing and manipulating files.
- **Date and Time Utilities**: Tools for formatting dates and times.
- **FTP Utilities**: Functions for working with FTP servers.
- **Image Utilities**: Basic image processing functions.
- **PDF Utilities**: Utilities for processing and converting PDF files.
- **Printer Utilities**: Functions for sending data to a printer.


## Modules Description

### Convertors

The `convertors` module contains utilities for converting data between formats. These modules can handle various data types, from CSV to JSON and text to images.


#### Files:

- [`text2png.py`](text2png.md): Converts text data to a PNG image.
- [`tts.py`](tts.md): Converts text to speech and saves it as an audio file.
- [`webp2png.py`](webp2png.md): Converts images from WebP to PNG format.
- [`xls.py`](xls.md): Handles transformations and manipulations with XLS files.
- [`xml2dict.py`](xml2dict.md): Converts XML data to a Python dictionary.
- [`base64.py`](base64.md): Encodes or decodes data using Base64 encoding.
- [`csv.py`](csv.md): Provides tools for parsing and manipulating CSV data.
- [`dict.py`](dict.md): Utilities for handling Python dictionaries.
- [`html.py`](html.md): Converts HTML content to various formats.
- [`json.py`](json.md): Utilities for parsing and manipulating JSON data.
- [`md2dict.py`](md2dict.md): Converts Markdown content to a dictionary.
- [`ns.py`](ns.md): Specialized utilities for converting namespace names.


### String Utilities
```
(and so on for other sections)
```
```