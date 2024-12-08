rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code snippet defines a function to obtain the relative path of a file or directory, specifically within a project structure. It leverages the `pathlib` module for path manipulation and a custom `get_relative_path` function from the `src.utils.path` module. The code demonstrates how to use this custom function to find the relative path of a file (`__file__`) relative to a specified directory ('hypotez').  It then prints the calculated relative path to the console. The code also includes import statements from the `header` module and `src.utils.path`.


Execution steps
-------------------------
1. Imports necessary modules: The code imports the `Path` object from the `pathlib` module and potentially other modules, such as `header` and `get_relative_path` from custom modules.


2. Sets a mode variable: The code sets the variable `MODE` to 'dev'. This variable likely indicates the current environment.


3. Calls `get_relative_path`: The code calls the function `get_relative_path`, passing the resolved absolute path of the current file (`Path(__file__).resolve()`) and the target directory ('hypotez') as arguments.


4. Calculates the relative path: `get_relative_path` determines the relative path of the current file ('hypotez/src/_examples/get_relative_path.py') relative to the base directory 'hypotez'.


5. Prints the relative path: The calculated relative path is then printed to the console.


Usage example
-------------------------
.. code-block:: python

    import pathlib
    from pathlib import Path
    #Replace with actual module path
    from src.utils.path import get_relative_path


    def get_relative_path_example():
        # Example usage. Replace with your actual file path and target directory
        current_file = Path(__file__).resolve()  
        target_directory = "hypotez"

        relative_path = get_relative_path(current_file, target_directory)
        print(relative_path)



    if __name__ == "__main__":
        get_relative_path_example()