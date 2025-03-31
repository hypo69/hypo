```markdown
# INSTRUCTION

The code provided below is part of the `hypotez` project. Task: Create developer documentation in `Markdown` format for each input Python file.
The documentation must meet the following requirements:

1. **Documentation Format**:
   - Use the `Markdown (.md)` standard.
   - Each file should start with a title and a brief description of its contents.

   Documentation Examples: Example of a module file title:

        """
        Module for working with a programming assistant
        =================================================

        The module contains the :class:`CodeAssistant` class, which is used to interact with various AI models
        (e.g., Google Gemini and OpenAI) and perform code processing tasks.

        Usage Example
        ----------------------

        >>>assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
        >>>assistant.process_files()
        """

   - For all classes and functions, use the following comment format:
     ```python
     def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
         """ The function performs some action... <Here You write what the function does> 
         Args:
             param (str): Description of the `param` parameter.
             param1 (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.

         Returns:
             dict | None: Description of the return value. Returns a dictionary or `None`.

         Raises:
             SomeError: Description of the situation in which the `SomeError` exception occurs.
            ...
            <DO NOT output the function body. Only docstring>
         """
         def inner_function():
            """ Inner function performs some action... <Here You write what the function does> 
                Args:
                    param (str): Description of the `param` parameter.
                    param1 (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.

                Returns:
                    dict | None: Description of the return value. Returns a dictionary or `None`.

                Raises:
                    SomeError: Description of the situation in which the `SomeError` exception occurs.

                ...
                    <DO NOT output the function body. Only docstring>

                """
     ```
     - All comments in the function and docstrings must be in Russian in UTF-8 format
     - If there are inner functions inside the function being considered, consider each of them in detail separately
     
   - Use `ex` instead of `e` in exception handling blocks.
   - For logging, use `logger` from my `src.logger` module. Example:
     ```python
     from src.logger import logger
     logger.info('Some information message')
     ...
     except SomeError as ex:
         logger.error('Some error message', ex, exc_info = True), where the error is passed as the second argument. exc_info determines whether to output service information.
    ```

    _ If the code uses a webdriver, know how to use it
    inherit Driver, Chrome, Firexox, Playwright
    Next define it as
    # Creating a driver instance (example with Chrome)
    driver = Drivewr(Chrome)
    The Driver and Chrome, Firexox, Playwright modules already contain all selenium settings.
    The main command that is used in the code: `driver.execute_locator(l:dict)`
    It returns the value of the webelement by locator.

   - All comments and docstrings must be in Russian in UTF-8 format. If the code's docstrings are in English, translate them to Russian

2. **Table of Contents (TOC)**:
   - At the beginning of each documentation file, add a section with a table of contents and links to functions and methods within the code
   - The structure of the table of contents should include links to all major sections of the module documentation.

3. **Documentation Formatting**:
   - Use Markdown syntax for all headers, lists, and links.
   - For documenting classes, functions, and methods, include structured sections with descriptions, details of parameters, return values, and raised exceptions. Example:

     ## Functions

     ### `function_name`

     **Purpose**: Purpose of the function.

     **How the function works**:
     1.  <Explain in detail the purpose of the function. Provide a detailed description of what transformation actions occur in the function body>

     2.  The following actions and transformations occur inside the function:
     A
     |
     -- C
     |
     D - E
     |
     F

     Where `A,B,C,D,E,F` are internal logical blocks of the function. Do not use abbreviations A,B,C,... give logical names to the blocks

     **Parameters**:
     - `param` (str): Description of the `param` parameter.
     - `param1` (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.

     **Returns**:
     - `dict | None`: Description of the return value.

     **Raises Exceptions**:
     - `SomeError`: Description of the situation in which the `SomeError` exception occurs.

     If there are inner functions inside the function, consider each of them in detail separately
     **Inner functions**: If any
     
4. **Section Headers**:
   - Use first-level (`#`), second-level (`##`), third-level (`###`) and fourth-level (`####`) headers sequentially throughout the file.

5. **File Example**:

   # Module Name

   ## Overview

   Brief description of the module's purpose.

   ## More Details

   More detailed description. Explain how and why this code is used in the project. 
   Analyze the code provided to you earlier

   ## Classes

   ### `ClassName`

   **Description**: Description of the class.

    **How the class works**:
        Explain how the class works. If the class is complex, provide a detailed code analysis

   Document EACH function or method. Explain the purpose of each variable.
   - All comments and docstrings must be in Russian in UTF-8 format. If the original code is written in English, translate it to Russian

   **Methods**: # if there are methods
   - `method_name`: Brief description of the method.   
   - `method_name`: Brief description of the method.
   **Parameters**: # if there are parameters
   - `param` (str): Description of the `param` parameter. 
   - `param1` (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.
   **Examples**
   - Examples of defining a class and working with the class

   ## Functions

   ### `function_name`

   ```python
   def my_func(param1:str, param2:Optional[int] = 0) -> bool:
       """ The function performs some action... <Here You write what the function does> 
       Args:
           param1 (str): Description of the `param1` parameter.
           param2 (Optional[int], optional): Description of the `param2` parameter. Defaults to 0.
       Returns:
           bool: Description of the return value. Returns `True` or `False`.

        Raises:
             Execution Error

        Example:
            Examples of calls with the full range of parameters that can be passed to the function

       """
       - Do not output the function body. only documentation and examples of function calls;
       - All comments and docstrings must be in Russian in UTF-8 format
   ```

    **How the function works**:
        Give a description of how the function works. If the function is complex, provide a detailed code analysis
   Document EACH function or method. Explain the purpose of each variable

   **Methods**: # if there are methods
   - `method_name`: More detailed description of the method.   
   - `method_name`: More detailed description of the method.****

   **Parameters**: # if there are parameters
   - `param` (str): More detailed Description of the `param` parameter.
   - `param1` (Optional[str | dict | str], optional): More detailed Description of the `param1` parameter. Defaults to `None`.

   **Returns**: # if there is a return value
   - `dict | None`: More detailed Description of the return value.

   **Raises Exceptions**: # if there are exceptions
   - `SomeError`: More detailed Description of the situation in which the `SomeError` exception occurs.

   **Examples**: # All possible variations of examples of calling a function with different parameters

   -------------------------------------------------------------------------------------
   


## Your behavior when analyzing code:
- Inside the code, you may encounter an expression between `<` `>`. For example: <instruction for the gemini model: Loading product descriptions into PrestaShop.>, <next, if any>. These are placeholders where you insert the relevant value
- Always refer to the system instructions for processing the `hypotez` project code;
- Analyze the file location in the project. This will help you understand its purpose and relationship to other files. You will find the file location in the very first line of code, starting with `## \file /...`;
- Remember the provided code and analyze its connection with other parts of the project;
- In this instruction, do not suggest code improvements. Strictly follow point 5. **File Example** when composing the answer

# END OF INSTRUCTION
```