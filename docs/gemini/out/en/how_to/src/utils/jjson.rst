rst
How to use the jjson module
==========================================================================================

Description
-------------------------
This module (`hypotez/src/utils/jjson.py`) provides functions for handling JSON and CSV files, including loading, dumping, merging, and conversion.  It offers versatile ways to work with JSON data, allowing loading from files, strings, and directories, conversion to `SimpleNamespace` objects, and merging multiple JSON files.  It includes error handling and logging capabilities.

Execution steps
-------------------------
1. **Import the module:**
   ```python
   from hypotez.src.utils.jjson import j_dumps, j_loads, j_loads_ns, process_json_file, recursive_process_json_files, extract_json_from_string
   ```

2. **Dump JSON data:**
   - Use `j_dumps` to write JSON data to a file or return it as a dictionary.
   - Specify the data to dump (`data`), the file path (`file_path`), and optional parameters like `ensure_ascii`, `mode` (file open mode, defaults to "w"), and `exc_info` (whether to log exceptions with traceback, defaults to True).
   - If `file_path` is None, `j_dumps` returns the JSON data as a Python dictionary.  Otherwise, it writes the data to the specified file.

3. **Load JSON data:**
   - Use `j_loads` to load JSON data from a file, directory, or string.
   - Provide the JSON data source (`jjson`), which can be a `Path` object, a string, or a Python dictionary or list.
   - The `ordered` parameter controls whether to return `OrderedDict` (to maintain order) or a regular `dict`.
   - `j_loads` handles CSV files in the specified directory or path, and returns a list of dictionaries. It also gracefully handles Markdown files containing JSON code blocks.

4. **Convert to SimpleNamespace:**
   - Use `j_loads_ns` to load and convert JSON data to `SimpleNamespace` objects.
   - This is particularly helpful for accessing JSON data attributes more easily.

5. **Merge JSON files:**
   - `j_loads` can merge multiple JSON files from a directory into a single JSON object.
   - It merges dictionaries and lists recursively if possible.

6. **Process and replace keys:**
   - `process_json_file` reads a JSON file, replaces a key ("name" in the example) with another (`category_name`), and writes the modified JSON to the same file.
   - This makes it straightforward to rename keys within a JSON structure.

7. **Recursive processing of JSON files:**
   - `recursive_process_json_files` efficiently processes all JSON files within a given directory and its subdirectories.

8. **Extract JSON from Markdown:**
   - `extract_json_from_string` allows you to extract JSON data that's embedded within a markdown string.


Usage example
-------------------------
```python
from hypotez.src.utils.jjson import j_dumps, j_loads, Path

# Example usage (dumping JSON to a file)
data_to_dump = {"name": "John Doe", "age": 30}
file_path = Path("output.json")
j_dumps(data_to_dump, file_path=file_path)

# Example usage (loading JSON from a file)
loaded_data = j_loads(file_path)
print(loaded_data)

# Example usage (recursive processing of JSON files in a directory)
directory_path = Path("./json_files")
recursive_process_json_files(directory_path)

# Example usage (extracting JSON from Markdown)
md_string = """
```json
{"message": "Hello, world!"}
```
"""
json_content = extract_json_from_string(md_string)
if json_content:
    print(json.loads(json_content))

```
```