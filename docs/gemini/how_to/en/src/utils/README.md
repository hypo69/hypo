# Tiny Utils Usage Guide

**Tiny Utils** is a utility library for various common tasks. This guide provides instructions on how to use the library's modules.

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/hypo69/tiny-utils.git
    cd tiny_utils
    ```

2.  Install required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Modules Overview

Tiny Utils is organized into modules, each handling a specific task:

- **Convertors:** Data format conversion (e.g., text to image, JSON, XML).
- **String Utilities:** Advanced string manipulation.
- **File Operations:** File handling (read, write, copy, delete).
- **Date-Time Utilities:** Date and time formatting.
- **FTP Utilities:** FTP file management.
- **Image Utilities:** Basic image processing.
- **PDF Utilities:** PDF file manipulation.
- **Printer Utilities:** Printing data.


## Module-Specific Usage Examples

### Convertors

The `convertors` module contains functions for converting data between formats.

#### `text2png.py` - Convert Text to PNG

```python
from tiny_utils.convertors import text2png

text_to_convert = "Hello, World!"
output_filename = "output.png"
text2png.convert(text_to_convert, output_filename)
```

This code converts the string "Hello, World!" to a PNG image file named "output.png".

#### `xml2dict.py` - Convert XML to Dictionary

```python
from tiny_utils.convertors import xml2dict

xml_data = "<root><item>Hello</item></root>"
converted_dict = xml2dict.convert(xml_data)
print(converted_dict)
```

This code converts the XML string to a Python dictionary and prints it.

#### `json.py` - Parse and Manipulate JSON

```python
from tiny_utils.convertors import json

json_data = '{"name": "John", "age": 30}'
parsed_data = json.parse(json_data)
print(parsed_data['name'])  # Accessing data
```

This example parses a JSON string and then accesses the `name` field in the parsed dictionary.


### File Operations

The `file.py` module provides file handling tools.

```python
from tiny_utils.file import copy_file

source_file = "source.txt"
destination_file = "destination.txt"
copy_file(source_file, destination_file)  #Copies source.txt to destination.txt
```


### Other Modules (Example snippets)

These snippets demonstrate the general approach to using the other modules:

```python
# String Utilities
from tiny_utils.string import format_string
formatted_string = format_string("Hello, {name}!", name="John")


# Date-Time Utilities
from tiny_utils.date_time import format_date_time
formatted_datetime = format_date_time(datetime.now(), '%Y-%m-%d %H:%M:%S')


# Image Utilities (resize)
from tiny_utils.image import resize_image
resize_image("input.jpg", "output.jpg", width=200, height=150)
```


## More Examples and Documentation

For comprehensive usage examples and detailed documentation, please refer to the [Tiny Utils Wiki](https://github.com/hypo69/tiny-utils/wiki).

## Contributing

Contributions are welcome! Please follow the guidelines in the [Contributing](./CONTRIBUTING.md) file.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.