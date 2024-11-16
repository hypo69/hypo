```markdown
# hypotez/src/utils/__init__.py

This module provides a collection of utility functions for various tasks, including data conversion, file handling, and formatted output. It aims to simplify common programming tasks and improve code readability.


## Module Contents

This module imports and exposes the following functionalities:

**Data Conversion:**

*   `base64_to_tmpfile`: Converts base64 encoded data to a temporary file.
*   `base64encode`: Encodes data to base64.
*   `csv2dict`: Converts a CSV string or file to a dictionary.
*   `csv2ns`: Converts a CSV string or file to a nested structure.
*   `dict2csv`: Converts a dictionary to a CSV string.
*   `dict2html`: Converts a dictionary to HTML.
*   `dict2ns`: Converts a dictionary to a nested structure.
*   `dict2xls`: Converts a dictionary to an XLSX file.
*   `dict2xml`: Converts a dictionary to XML.
*   `dot2png`: Converts a Graphviz DOT file to a PNG image.
*   `escape2html`: Escapes special characters for HTML.
*   `html2dict`: Converts an HTML string to a dictionary.
*   `html2escape`: Unescapes HTML special characters.
*   `html2ns`: Converts HTML to nested structures.
*   `html2text`: Converts HTML to plain text.
*   `html2text_file`: Converts an HTML file to plain text.
*   `json2csv`: Converts a JSON string or file to CSV.
*   `json2ns`: Converts a JSON string or file to nested structures.
*   `json2xls`: Converts a JSON string or file to XLSX.
*   `json2xml`: Converts a JSON string or file to XML.
*   `md2dict`: Converts a markdown string to a dictionary.
*   `ns2csv`: Converts nested structures to CSV.
*   `ns2dict`: Converts nested structures to a dictionary.
*   `ns2json`: Converts nested structures to JSON.
*   `ns2xls`: Converts nested structures to XLSX.
*   `ns2xml`: Converts nested structures to XML.
*   `speech_recognizer`: (Potentially) handles speech recognition.
*   `TextToImageGenerator`:  (Potentially) Generates images from text.
*   `text2speech`: Converts text to speech.
*   `webp2png`: Converts a WEBP image to PNG.
*   `xls2dict`: Converts an XLSX file to a dictionary.


**File Handling:**

*   `read_csv_as_dict`: Reads a CSV file as a dictionary.
*   `read_csv_as_ns`: Reads a CSV file as a nested structure.
*   `read_csv_file`: Reads a CSV file.
*   `save_csv_file`: Saves a CSV file.
*   `get_directory_names`: Gets all directory names in a specified path.
*   `get_filenames`: Gets all filenames in a specified path.
*   `read_text_file`: Reads a text file.
*   `recursively_get_filenames`: Recursively gets all filenames in a directory tree.
*   `recursively_read_text_files`: Recursively reads all text files in a directory tree.
*   `save_text_file`: Saves text to a file.
*   `recursively_yield_file_path`: Yields paths to all files recursively in a directory.
*   `remove_bom`: Removes byte order marks from a file.

**Image Handling:**
*   `save_png_from_url`: Downloads an image from a URL and saves it as PNG.
*   `save_png`: Saves an image as PNG.


**JSON Handling:**
* `j_dumps`: JSON dump function.
* `j_loads`: JSON load function.
* `j_loads_ns`: JSON load to nested structures.
* `replace_key_in_json`: Replace key in JSON.


**PDF Handling:**
* `PDFUtils`:  (Potentially) a module for PDF processing.


**General Utilities:**
*   `TimeoutCheck`: (Potentially) class to handle timeouts.
*   `pprint`: Pretty prints data.
*   `ProductFieldsValidator`: (Potentially) Validates product fields.
*   `StringFormatter`: Formats strings.
*   `StringNormalizer`: Normalizes strings.
*   `extract_url_params`: Extracts URL parameters.
*   `is_url`: Checks if a string is a valid URL.

**Video Handling:**
* `save_video_from_url`: Downloads a video from a URL.


**Important notes:**
*  Add more detailed descriptions for each utility function, especially regarding input/output types. 
* Document any dependencies for each utility (e.g., `requirements.txt` packages).  
* If any function takes a file path, specify the expected file format.
* Document any potential exceptions that might be raised.



## Project Root Location

The project root is determined by the `get_project_root` function.  
The function searches upwards from the current file's location until it finds a directory containing files like `pyproject.toml`, `requirements.txt`, or `.git`.  This location is stored in `__root__`.

## Binary Paths

The module defines paths to directories containing essential binary utilities like GTK, FFmpeg, Graphviz, and wkhtmltopdf. It dynamically updates the `sys.path` variable to ensure these binaries can be found.

## Versioning
The module imports necessary classes from the `packaging.version` module.
```