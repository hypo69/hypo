rst
How to use the FacebookGroupsWidget class
========================================================================================

Description
-------------------------
This code defines a `FacebookGroupsWidget` class that creates an interactive dropdown widget in a Jupyter Notebook environment.  This widget allows the user to select a Facebook group from a list of URLs loaded from a JSON file.

Execution steps
-------------------------
1. **Import necessary libraries:** The code imports the `header` module, `IPython.display`, `ipywidgets.Dropdown`, `src.utils.jjson`, `types`, and `pathlib`.  These libraries provide functionality for displaying widgets, loading JSON data, and managing file paths.

2. **Define the `FacebookGroupsWidget` class:** This class encapsulates the logic for creating and displaying the dropdown widget.

3. **Initialization (`__init__` method):**
    - Takes a `Path` object representing the JSON file as input.
    - Loads the JSON data from the specified file using `j_loads_ns` function and stores it in the `self.groups_data` attribute as a `SimpleNamespace` object.
    - Calls the `create_dropdown` method to create the actual widget and stores it in `self.dropdown`.

4. **Create the dropdown (`create_dropdown` method):**
    - Extracts a list of group URLs (keys) from the loaded JSON data.
    - Creates a `Dropdown` widget using `ipywidgets`. The `options` argument sets the choices for the dropdown menu, which is a list of Facebook group URLs.  The `description` and `disabled` arguments are used to customize the dropdown's appearance.
    - Returns the created `Dropdown` widget.

5. **Display the widget (`display_widget` method):**
    - Uses `IPython.display.display` to render the `self.dropdown` widget in the Jupyter Notebook.

Usage example
-------------------------
.. code-block:: python

    from pathlib import Path
    from hypotez.src.endpoints.advertisement.facebook.facebook_groups_widgets import FacebookGroupsWidget

    # Replace with the actual path to your JSON file
    json_file_path = Path("./path/to/your/groups.json")

    # Create an instance of the FacebookGroupsWidget
    facebook_groups_widget = FacebookGroupsWidget(json_file_path)

    # Display the widget
    facebook_groups_widget.display_widget()