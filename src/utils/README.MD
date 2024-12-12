<TABLE >
<TR>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/README.MD'>[Root ↑]</A>
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/README.MD'>src</A>  
</TD>
<TD>
<A HREF = 'https://github.com/hypo69/hypo/blob/master/src/utils/readme.ru.md'>Русский</A>
</TD>
</TR>
</TABLE>

# Tiny Utils

**Tiny Utils** is a utility library providing a collection of lightweight helper functions for various common tasks. This library includes utilities for data format conversion, text and file manipulation, string operations, date-time formatting, image processing, and more. It is organized into several modules for easy access to specific functionalities.

## Table of Contents

- [Tiny Utils](#tiny-utils)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Modules Overview](#modules-overview)
  - [Module Descriptions](#module-descriptions)
    - [Convertors](#convertors)
      - [Files:](#files)
    - [String Utilities](#string-utilities)
    - [File Operations](#file-operations)
    - [Date-Time Utilities](#date-time-utilities)
    - [FTP Utilities](#ftp-utilities)
    - [Image Utilities](#image-utilities)
    - [PDF Utilities](#pdf-utilities)
    - [Printer Utilities](#printer-utilities)
  - [Usage Examples](#usage-examples)
    - [Convert Text to PNG Image](#convert-text-to-png-image)
    - [Convert XML to Dictionary](#convert-xml-to-dictionary)
    - [Parse and Manipulate JSON](#parse-and-manipulate-json)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

To use **Tiny Utils**, clone the repository and install any necessary dependencies as specified in the `requirements.txt` file.

```bash
git clone https://github.com/hypo69/tiny-utils.git
cd tiny_utils
pip install -r requirements.txt
```

## Modules Overview

This library contains several sub-modules, each handling a specific task:

- **Convertors**: Modules for converting data formats, such as text-to-image, webp-to-png, JSON, XML, Base64 encoding, and more.
- **String Utilities**: Tools for advanced string manipulation.
- **File Operations**: Functions for file handling and manipulation.
- **Date-Time Utilities**: Tools for date and time formatting.
- **FTP Utilities**: FTP file handling functions.
- **Image Utilities**: Basic image processing functions.
- **PDF Utilities**: PDF file manipulation and conversion.
- **Printer Utilities**: Functions for sending data to a printer.

## Module Descriptions

### Convertors

The `convertors` module contains utilities for converting data between formats. These modules can handle diverse data types, from CSV to JSON and text to images.

#### Files:

- **text2png.py**: Converts text data to a PNG image file.
- **tts.py**: Converts text to speech and saves it as an audio file.
- **webp2png.py**: Converts images from WebP format to PNG format.
- **xls.py**: Handles conversions and manipulations of XLS files.
- **xml2dict.py**: Converts XML data to a Python dictionary.
- **base64.py**: Encodes or decodes data using Base64 encoding.
- **csv.py**: Provides CSV parsing and manipulation tools.
- **dict.py**: Utilities for handling Python dictionaries.
- **html.py**: Converts HTML content to various formats.
- **json.py**: Utilities for JSON parsing and manipulation.
- **md2dict.py**: Converts Markdown content to a dictionary.
- **ns.py**: Specialized namespace conversion utilities.

### String Utilities

The `string` module includes advanced functions for string manipulation, offering tools to enhance basic Python string operations.

### File Operations

The `file.py` module includes utilities for file handling, providing functions to read, write, copy, delete, and move files with additional options for error handling and file format compatibility.

### Date-Time Utilities

The `date_time.py` module provides various date and time utilities, enabling users to parse, format, and manipulate date-time values for consistent formatting and conversions.

### FTP Utilities

The `ftp.py` module includes functions for handling FTP operations, such as connecting to servers, uploading, downloading, and managing files over FTP.

### Image Utilities

The `image.py` module provides basic image manipulation tools, such as resizing, cropping, format conversion, and applying filters.

### PDF Utilities

The `pdf.py` module offers PDF handling utilities, including PDF file conversion, merging, splitting, and text extraction.

### Printer Utilities

The `printer.py` module includes functions to send files or formatted data to a printer, supporting print job configuration options.

## Usage Examples

Here are some usage examples demonstrating how to work with the **Tiny Utils** library.

### Convert Text to PNG Image

```python
from tiny_utils.convertors import text2png

text = "Hello, World!"
output_path = "output_image.png"
text2png.convert(text, output_path)
```

### Convert XML to Dictionary

```python
from tiny_utils.convertors import xml2dict

xml_data = "<root><item>Hello</item></root>"
dictionary = xml2dict.convert(xml_data)
print(dictionary)
```

### Parse and Manipulate JSON

```python
from tiny_utils.convertors import json

json_data = '{"name": "John", "age": 30}'
parsed_data = json.parse(json_data)
print(parsed_data)
```

## For more examples and detailed documentation, please visit the 
  [Tiny Utils Wiki](https://github.com/hypo69/tiny-utils/wiki).

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Make sure to update the documentation for any new features or changes.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more information.
