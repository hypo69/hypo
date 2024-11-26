How to use the FacebookGroupsWidget

This guide explains how to use the `FacebookGroupsWidget` class from the `facebook_groups_widgets.py` file to create and display a dropdown widget for selecting Facebook groups.

**1. Installation:**

Ensure that the necessary libraries are installed.  The code uses `IPython` and `ipywidgets`.  You should be able to install them via pip:

```bash
pip install ipython ipywidgets
```

**2. Data Preparation:**

The `FacebookGroupsWidget` expects a JSON file containing the list of Facebook group URLs.  This JSON should have a structure like this:

```json
{
  "group1_url": "https://facebook.com/group1",
  "group2_url": "https://facebook.com/group2",
  "group3_url": "https://facebook.com/group3"
}
```

Save this data as a `.json` file (e.g., `groups.json`).  Replace the example URLs with your actual group URLs.


**3. Import and Initialization:**

Import the `FacebookGroupsWidget` class and `Path` object from the appropriate modules:

```python
from pathlib import Path
from hypotez.src.endpoints.advertisement.facebook.facebook_groups_widgets import FacebookGroupsWidget
```

Create an instance of `FacebookGroupsWidget` by passing the path to your JSON file:

```python
json_file_path = Path("groups.json")
facebook_groups_widget = FacebookGroupsWidget(json_file_path)
```

**4. Displaying the Widget:**

Call the `display_widget()` method to show the dropdown:

```python
facebook_groups_widget.display_widget()
```

**Example Usage:**

```python
from pathlib import Path
from hypotez.src.endpoints.advertisement.facebook.facebook_groups_widgets import FacebookGroupsWidget

# Assuming you have a JSON file named 'groups.json'
json_file_path = Path("groups.json")

# Create the widget
facebook_groups_widget = FacebookGroupsWidget(json_file_path)

# Display the widget
facebook_groups_widget.display_widget()
```

**Important Considerations:**

* **Error Handling:** The code doesn't include error handling for invalid JSON formats.  Consider adding `try...except` blocks to handle potential `json.JSONDecodeError` or similar exceptions.
* **File Existence:** Ensure that the specified JSON file (`groups.json` in the example) exists in the expected location.  Otherwise, you'll get a `FileNotFoundError`.
* **File Path:**  The `Path` object is crucial for handling file paths correctly, especially across different operating systems.
* **JSON structure:**  The JSON structure must be exactly as expected, e.g., keys are group URLs and values are the corresponding Facebook group URLs.

This complete guide walks through all necessary steps, from preparing the data to displaying the widget, along with important points about error handling and file paths.  Remember to replace placeholders like `"groups.json"` with your actual file name and path.