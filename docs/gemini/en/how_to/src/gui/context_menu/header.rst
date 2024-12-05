rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code snippet configures the project environment by adding paths to GTK, FFmpeg, and Graphviz binaries to the system path. It also handles potential missing paths and sets up WeasyPrint, while suppressing GTK warnings.  It loads the project name from `settings.json` and uses the `__root__` variable to determine the absolute path to the project's bin directories.

Execution steps
-------------------------
1. **Load project settings:** The code opens the `settings.json` file and loads its content into a Python dictionary. It retrieves the `project_name` from the loaded settings, falling back to "hypotez" if not found.

2. **Determine project root path:** It calculates the absolute path (`__root__`) to the project's root directory by traversing up from the current working directory.

3. **Define binary paths:** It defines variables (`gtk_bin_path`, `ffmpeg_bin_path`, `graphviz_bin_path`) to store the paths to the respective binary directories within the project's root.

4. **Append paths to system path:** It iterates through the defined binary paths. For each path, it checks if it's already present in the system path. If a path is missing, it inserts the path at the beginning of the `sys.path` list using `sys.path.insert(0, str(bin_path))`. This ensures that the binaries are accessible when importing modules that depend on them.

5. **Set WeasyPrint environment variable:** It checks if the `WEASYPRINT_DLL_DIRECTORIES` environment variable exists in `sys.path`. If not, it adds the GTK binary path to `sys.path`.

6. **Suppress GTK warnings:** The code uses `warnings.filterwarnings` to suppress any UserWarnings originating from the GTK library, preventing those warnings from displaying in the console output.


Usage example
-------------------------
.. code-block:: python

    # Example usage (assuming settings.json exists and is correctly formatted):
    # ... (Import necessary modules here) ...
    import sys
    from pathlib import Path

    # ... (Your code that needs the configured environment) ...

    # Example to verify the path addition:
    print(sys.path)