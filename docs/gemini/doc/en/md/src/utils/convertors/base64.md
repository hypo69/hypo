# hypotez/src/utils/convertors/base64.py

## Overview

This module provides a function to decode Base64 encoded content and write it to a temporary file with the specified extension.


## Functions

### `base64_to_tmpfile`

**Description**: This function converts Base64 encoded content to a temporary file. It decodes the Base64 content and writes it to a temporary file, using the extension from the input `file_name`. The path to the temporary file is returned.

**Parameters**:

- `content` (str): Base64 encoded content to be decoded and written to the file.
- `file_name` (str): Name of the file used to extract the file extension for the temporary file.


**Returns**:

- `str`: Path to the temporary file.


**Example Usage**:

```python
>>> base64_content = "SGVsbG8gd29ybGQh"  # Base64 encoded content "Hello world!"
>>> file_name = "example.txt"
>>> tmp_file_path = base64_to_tmpfile(base64_content, file_name)
>>> print(f"Temporary file created at: {tmp_file_path}")
Temporary file created at: /tmp/tmpfile.txt
```

**Raises**:

- No exceptions are explicitly raised. However, issues with the Base64 decoding or file writing could potentially result in `IOError` or similar exceptions.




### `base64encode`

**Description**: Function to encode the image to Base64 format.

**Parameters**:

- `image_path` (str): Path to the image file to be encoded.


**Returns**:

- `str`: Base64 encoded string representation of the image.

**Raises**:


- `FileNotFoundError`: If the provided `image_path` does not exist.
- Other potential exceptions that might occur during file reading.