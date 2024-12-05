rst
How to Generate Code Documentation in reStructuredText (RST) Format
=================================================================

Description
-------------------------
This document provides instructions on how to generate reStructuredText (RST) documentation for Python code files, suitable for Sphinx compilation.  The generated documentation will include detailed explanations, step-by-step instructions, usage examples, and adherence to a specific format for code blocks, classes, functions, and exceptions.

Execution steps
-------------------------
1. **Analyze the Python Code:** Carefully review each Python file to understand its structure, classes, functions, and the logic they implement.

2. **Construct RST Documentation:** Create a corresponding RST file for each Python file.  Adhere to the following structure:

   - **File Header:** Begin each file with a descriptive title, using `=` for first-level headings.  Include a brief description underneath the title.

   - **Class/Function Documentation:**  For all classes and functions, use docstrings following the specified format, including detailed parameter descriptions, return values, and potential exceptions.

   - **RST Formatting:**  Utilize RST syntax for formatting, including first-level headings (`=`), second-level headings (`-`), and third/fourth-level headings (`~`, `^`).

   - **`.. automodule::` Directive:**  For each Python module, use the `.. automodule::` directive within an appropriate heading level, followed by `:members:`, `:undoc-members:`, and `:show-inheritance:` to document all members, undocmented members, and inheritance relationships.

   - **Exception Handling (`ex`):** Use the `ex` prefix consistently in exception handling.

   - **Usage Examples:** Include a `Usage Example` section demonstrating how to utilize the code in a practical context.  Employ the `.. code-block:: python` directive for code examples.

   - **Table of Contents:**  Include a Table of Contents (`.. toctree::`) in the main `index.rst` file to link to the documentation of each module.


3. **Examples (Key Concepts):**

    - For every function:

    ```rst
    .. autofunction:: module_name.function_name
    ```
    - Include explicit examples of class and function documentation to demonstrate the required docstrings.

    - Carefully document all exceptions with precise information.

4. **Format Consistency:** Maintain consistent formatting throughout all RST files, adhering to the specified structure, heading levels, and directives.

    - Each file should have a title.
    - Each file should include a description.
    - Functions and classes must have docstrings.
    - RST directives (`.. automodule::`, `.. autofunction::`, and `.. code-block::`) must be used correctly.


Usage example
-------------------------
.. code-block:: rst

   Module for Data Processing
   ===========================

   .. automodule:: my_module
       :members:
       :undoc-members:
       :show-inheritance:

   Data Loading Functions
   -----------------------

   .. autofunction:: my_module.load_data

   .. code-block:: python

       from my_module import load_data

       # Example usage
       data = load_data("path/to/data.csv")
       print(data)