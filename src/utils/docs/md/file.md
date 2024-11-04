

```markdown
# `save_text_file()` Function

The `save_text_file()` function is used to save various types of data to a specified file. It can handle strings, lists, and dictionaries, and allows specifying the file mode (write or append). This function also handles exceptions and logs errors if they occur.

## How the function works:

1. **String Data**: If the `data` argument is a string, the function writes the string directly to the file at the specified `file_path`.

2. **List Data**: If `data` is a list, the function writes each item in the list as a new line in the file.

3. **Dictionary Data**: If `data` is a dictionary, the function converts the dictionary to a JSON-formatted string and writes it to the file.

4. **File Modes**: The `mode` argument determines whether the data is written to the file by overwriting existing content (`'w'`) or appending to it (`'a'`).

5. **Error Handling**: If an error occurs while saving the file, the function logs the error and returns `False`.

## Examples of `save_text_file()` usage:

### Example 1: Saving String Data

```python
# Saving a simple string to a file
success = save_text_file(data="Hello, World!", file_path="output.txt")
```

**Output**: `True` if the operation was successful, `False` otherwise.

### Example 2: Saving List Data

```python
# Saving a list of strings to a file
data = ["Hello, World!", "This is a new line."]
success = save_text_file(data=data, file_path="list_output.txt")
```

**Output**: `True` if the operation was successful, `False` otherwise.

### Example 3: Saving Dictionary Data

```python
import json

# Saving a dictionary to a file in JSON format
data = {
    "name": "Alice",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Wonderland"
    }
}
success = save_text_file(data=json.dumps(data, indent=4), file_path="dict_output.json")
```

**Output**: `True` if the operation was successful, `False` otherwise.

### Example 4: Appending Data to a File

```python
# Appending data to an existing file
success = save_text_file(data="Appending new line.", file_path="output.txt", mode="a")
```

**Output**: `True` if the operation was successful, `False` otherwise.

# `read_text_file()` Function

The `read_text_file()` function reads the contents of a text file and returns it as either a single string or a list of lines. It handles files with different encodings and includes error handling.

## How the function works

1. **Reading as String**: If `get_list` is `False`, the function reads the entire file content as a single string.

2. **Reading as List**: If `get_list` is `True`, the function reads the file content and returns each line as a list element.

3. **Error Handling**: If an error occurs while reading the file, the function logs the error and returns `None`.

## Examples of `read_text_file()` usage

### Example 1: Reading as a Single String

```python
# Reading the entire content of a file as a single string
content = read_text_file(file_path="example.txt")
print(content)
```

**Output**:

```
Content of the file as a single string.
```

### Example 2: Reading as a List of Lines

```python
# Reading the file content as a list of lines
lines = read_text_file(file_path="example.txt", get_list=True)
print(lines)
```

**Output**:

```
['Line 1', 'Line 2', 'Line 3']
```

### Example 3: Handling Non-Existent Files

```python
# Reading a non-existent file
content = read_text_file(file_path="nonexistent.txt")
print(content)
```

**Output**:

```
None
```

# `get_filenames()` Function

The `get_filenames()` function retrieves all filenames from a specified directory. It supports filtering by file extension and handles errors gracefully.

## How the function works

1. **File Extensions**: The function can filter filenames based on their extensions. You can specify a single extension or a list of extensions.

2. **Retrieving Filenames**: It iterates over the files in the specified directory and collects filenames that match the given extensions.

3. **Error Handling**: If an error occurs while retrieving filenames, the function logs the error and returns an empty list.

## Examples of `get_filenames()` usage

### Example 1: Retrieving All Filenames

```python
# Retrieving all filenames from the current directory
filenames = get_filenames(directory=".")
print(filenames)
```

**Output**:

```
['file1.txt', 'file2.py', 'file3.md']
```

### Example 2: Filtering by Extension

```python
# Retrieving filenames with a specific extension
python_files = get_filenames(directory=".", extensions="*.py")
print(python_files)
```

**Output**:

```
['script1.py', 'module.py']
```

### Example 3: Handling Errors

```python
# Attempting to retrieve filenames from a non-existent directory
filenames = get_filenames(directory="/nonexistent/path")
print(filenames)
```

**Output**:

```
[]
```

# `get_directory_names()` Function

The `get_directory_names()` function retrieves all directory names from a specified directory. It handles errors and logs them if they occur.

## How the function works

1. **Retrieving Directory Names**: It iterates over the contents of the specified directory and collects names of all subdirectories.

2. **Error Handling**: If an error occurs while retrieving directory names, the function logs the error and returns an empty list.

## Examples of `get_directory_names()` usage

### Example 1: Retrieving Directory Names

```python
# Retrieving all directory names from the current directory
directory_names = get_directory_names(directory=".")
print(directory_names)
```

**Output**:

```
['dir1', 'dir2']
```

### Example 2: Handling Errors

```python
# Attempting to retrieve directory names from a non-existent directory
directory_names = get_directory_names(directory="/nonexistent/path")
print(directory_names)
```

**Output**:

```
[]
```

```

