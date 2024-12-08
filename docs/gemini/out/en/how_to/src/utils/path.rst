rst
How to use the get_relative_path function
========================================================================================

Description
-------------------------
This function extracts a portion of a given file path, starting from a specified segment.  It takes a full file path and a segment as input, and returns the relative path from that segment to the end of the full path.  If the specified segment isn't found, it returns `None`.

Execution steps
-------------------------
1. The function takes two string arguments: `full_path` (the complete file path) and `relative_from` (the segment to start the relative path from).

2. It converts both input strings to `Path` objects for easier path manipulation.

3. It extracts the parts of the full path using the `.parts` attribute of the `Path` object.

4. It finds the index of the `relative_from` segment within the `parts` list.  If the segment is not found, it returns `None`.

5. If the segment is found, it creates a new `Path` object starting from the index of the found segment to the end of the `parts` list.

6. It converts the new `Path` object to a string representation using `.as_posix()`. This ensures the returned string is compatible with various operating systems.

7. The function returns the relative path string.


Usage example
-------------------------
.. code-block:: python

    from pathlib import Path
    from hypotez.src.utils.path import get_relative_path

    full_path = "/home/user/project/src/main.py"
    relative_from = "src"

    relative_path = get_relative_path(full_path, relative_from)

    if relative_path:
        print(f"Relative path from {relative_from}: {relative_path}")
    else:
        print(f"Segment '{relative_from}' not found in '{full_path}'")