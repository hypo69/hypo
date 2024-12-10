
# INSTRUCTION

For each input Python file, create developer documentation in `Markdown` format for subsequent use. 
The documentation must meet the following requirements:

1. **Documentation Format**:
   - Use the `Markdown (.md)` standard.
   - Each file should begin with a header and a brief description of its contents.
   - For all classes and functions, use the following comment format:
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
   - Use `ex` instead of `e` in exception handling blocks.

2. **TOC (Table of Contents)**:
   - Include a table of contents section at the beginning of each documentation file.
   - The structure should include links to all major sections of the module documentation.

3. **Documentation Formatting**:
   - Use proper Markdown syntax for all headers, lists, and links.
   - For documenting classes, functions, and methods, include structured sections with descriptions, parameter details, return values, and raised exceptions. Example:
     ```markdown
     ## Functions

     ### `function_name`

     **Description**: Brief description of the function.

     **Parameters**:
     - `param` (str): Description of the `param` parameter.
     - `param1` (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.

     **Returns**:
     - `dict | None`: Description of the return value.

     **Raises**:
     - `SomeError`: Description of the situation in which the `SomeError` exception is raised.
     ```

4. **Section Headings**:
   - Use level 1 headers (`#`), level 2 headers (`##`), level 3 headers (`###`), and level 4 headers (`####`) consistently throughout the file.

5. **Example File**:
   ```markdown
   # Module Name

   ## Overview

   Brief description of the module's purpose.

   ## Classes

   ### `ClassName`

   **Description**: Brief description of the class.

   **Methods**:
   - `method_name`: Brief description of the method.

   ## Functions

   ### `function_name`

   **Description**: Brief description of the function.

   **Parameters**:
   - `param` (str): Description of the `param` parameter.
   - `param1` (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.

   **Returns**:
   - `dict | None`: Description of the return value.

   **Raises**:
   - `SomeError`: Description of the situation in which the `SomeError` exception is raised.
   ```

Generate the corresponding documentation for each input Python file in `Markdown` format.
## Response format: `.md` (markdown)
# END OF INSTRUCTION
