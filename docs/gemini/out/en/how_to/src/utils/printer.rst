rst
How to use the `printer` module
========================================================================================

Description
-------------------------
This module provides functions for pretty printing data with optional text styling (color, background, and font). It handles various data types, including dictionaries, lists, strings, and file paths (supporting .csv and .xls), allowing for customizable output.  The `pprint` function is the core utility for printing formatted data.  A helper function `_color_text` allows for combining text with styling elements.


Execution steps
-------------------------
1. **Import the `printer` module:**
   ```python
   from hypotez.src.utils.printer import pprint, _color_text
   ```

2. **Prepare the data to be printed:** This can be a dictionary, list, string, or a file path.

3. **Call the `pprint` function:**
   ```python
   pprint(print_data, text_color="color", bg_color="background_color", font_style="font_style")
   ```
   - `print_data`: The data to be printed.
   - `text_color`: Specifies the text color.  Valid options are from the `TEXT_COLORS` dictionary (e.g., "red", "green"). Defaults to "white".
   - `bg_color`:  Specifies the background color from the `BG_COLORS` dictionary. Defaults to an empty string, which is no background color.
   - `font_style`: Specifies font style from `FONT_STYLES` (e.g., "bold", "underline"). Defaults to an empty string, meaning no font style.

4. **Handle potential errors:** The `pprint` function includes error handling to catch cases where data is invalid or a file cannot be read.  Error messages will be displayed in red.

5. **Output:** The formatted data will be printed to the console according to the specified parameters.  The output format depends on the input data:
   - **Dictionaries**: The dictionary contents will be printed in a nicely formatted, indented format.
   - **Lists**:  Each list item will be printed on a separate line with the specified styling.
   - **Strings/File paths**: The string or file contents will be printed, but if the file is not a .csv or .xls file, a message indicating that the file type is not supported will be printed in the specified color.


Usage example
-------------------------
```python
from hypotez.src.utils.printer import pprint
import pandas as pd

# Example usage with a dictionary
data_dict = {"name": "Alice", "age": 30}
pprint(data_dict, text_color="green")

# Example usage with a list
data_list = ["apple", "banana", "cherry"]
pprint(data_list, text_color="blue", font_style="bold")


# Example with a CSV file
try:
    df = pd.read_csv("my_data.csv")
    pprint(df,text_color="blue", font_style="bold")

except Exception as e:
    print(e)

# Example with a non-supported file type
pprint("my_data.txt", text_color="blue")


```
```
```
```python
# Example usage with an unsupported file type
pprint("my_data.txt", text_color="blue")
```
```
```
```python
# Example with a file that doesn't exist
pprint("nonexistent_file.csv", text_color="blue")
```
```
```
Output will be as per the instructions in the function's docstring.