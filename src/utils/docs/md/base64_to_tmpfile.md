# `base64_to_tmpfile` Module

## `base64_to_tmpfile()`

The `base64_to_tmpfile` function decodes Base64 encoded content and writes it to a temporary file with the same extension as the provided file name. It returns the path to the temporary file.

### How the function works:

1. **Extension Extraction**: Extracts the file extension from the provided file name.
2. **Temporary File Creation**: Creates a temporary file with the extracted extension.
3. **Content Decoding and Writing**: Decodes the Base64 content and writes it to the temporary file.
4. **Path Retrieval**: Returns the path to the created temporary file.

### Args:
- **content (str)**: Base64 encoded content to be decoded and written to the file.
- **file_name (str)**: Name of the file used to determine the extension of the temporary file.

### Returns:
- **str**: The path to the created temporary file.

### Raises:
- **Exception**: Logs errors if Base64 decoding or file operations fail.

### Examples:

```python
>>> base64_content = "SGVsbG8gd29ybGQh"  # Base64 encoded content of "Hello world!"
>>> file_name = "example.txt"
>>> tmp_file_path = base64_to_tmpfile(base64_content, file_name)
>>> print(f"Temporary file created at: {tmp_file_path}")
Temporary file created at: /tmp/tmpabcdef.txt
```
