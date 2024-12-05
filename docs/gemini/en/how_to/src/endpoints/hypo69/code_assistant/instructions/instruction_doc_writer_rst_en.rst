How to Generate Python Code Documentation in reStructuredText (RST) Format

========================================================================================

Description
-------------------------

This document outlines the steps to generate reStructuredText (RST) documentation for Python code, suitable for use with Sphinx.  It details how to create well-structured documentation including module descriptions, class and function details, and proper cross-referencing.


Execution steps
-------------------------

1. **Analyze the Input Python Files:** Carefully examine each Python file, understanding its purpose, and the classes and functions it defines.


2. **Create RST Documentation for Each Module:**
    * **Module Header:**  For each Python file, create a header in RST format.  The header should include the module name, and a concise description of the module's purpose.
    * **Automodule Directive:** Use the `.. automodule::` directive to document the entire module.  This directive should be placed directly below the module name header.  Include the options `:members:`, `:undoc-members:`, and `:show-inheritance:` to document all functions, undeclared functions (functions not explicitly documented using docstrings), and inheritance hierarchies, respectively.


3. **Document Classes and Functions:**
    * **Docstring Formatting:** Ensure all classes and functions within the Python files are documented with docstrings that follow the specified format:

    ```python
    def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
        """
        Args:
            param (str): Description of the `param` parameter.
            param1 (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.

        Returns:
            dict | None: Description of the return value. Returns a dictionary or `None`.

        Raises:
            SomeError: Description of the situation in which the `SomeError` exception is raised.
        """
    ```
    * **Consistent Formatting:** Adhere strictly to this docstring format throughout the entire project to ensure uniformity in the generated documentation.


4. **TOC Tree (if applicable):**
    * **`index.rst` File:** If creating a documentation tree, ensure `index.rst` includes the `.. toctree::` directive to list the modules for navigation. This will link to each module's documentation page.


5. **Documentation Structure:**
    * **Section Headings:** Utilize various section heading levels (1-4) as defined in the instruction, using `=` for level 1, `-` for level 2, `~` for level 3, and `^` for level 4.


6. **Exception Handling (`ex`):**  For exception handling blocks, always use the `ex` instead of `e`.


7. **Example File:**  Ensure your documentation includes RST directives for all the required elements (module, function, class documentation).  For example, if the Python file `module_name.py` exists, the corresponding `rst` file will document the functions and classes of this file using `.. automodule:: module_name`.


8. **Output:** Produce the RST output files.


Usage example
-------------------------

```rst
Module Example
=============

.. automodule:: my_module
    :members:
    :undoc-members:
    :show-inheritance:


Functions
---------

.. autofunction:: my_module.my_function
```

This example shows how to document a module named `my_module` and one of its functions `my_function`.  The `autofunction` directive will automatically generate the documentation for `my_function` based on its docstring. Remember to replace `my_module` and `my_function` with the actual names from your code.
```