```markdown
# INSTRUCTION

The code provided below is part of the `hypotez` project. Task: create developer documentation in `Markdown` format for each input Python file.
The documentation must meet the following requirements:

1. **Documentation Format**:
   - Use the `Markdown (.md)` standard.
   - Each file must start with a header and a brief description of its contents.

   Documentation examples: Module file header example:

        """
        Модуль для работы с ассистентом программиста
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
         """ Функция выполняет некоторое действия... <Тут Ты пишешь что именно делает функция>
         Args:
             param (str): Описание параметра `param`.
             param1 (Optional[str | dict | str], optional): Описание параметра `param1`. Defaults to `None`.

         Returns:
             dict | None: Description of the returned value. Returns a dictionary or `None`.

         Raises:
             SomeError: Description of the situation in which the `SomeError` exception occurs.
            ...
            <DO NOT output the function body. Only docstring>
         """
         def inner_function():
            """ Внутрняя функция Функция выполняет некоторое действия... <Тут Ты пишешь что именно делает функция>
                Args:
                    param (str): Описание параметра `param`.
                    param1 (Optional[str | dict | str], optional): Описание параметра `param1`. Defaults to `None`.

                Returns:
                    dict | None: Description of the returned value. Returns a dictionary or `None`.

                Raises:
                    SomeError: Description of the situation in which the `SomeError` exception occurs.

                ...
                  
                  DO NOT OUTPUT THE FUNCTION CODE. ONLY DOCSTR

                """
     ```
     - All comments in the function and docstring must be in Russian in UTF-8 format.
     - If there are inner functions inside the function under consideration, consider each of them separately.
   - Use `ex` instead of `e` in exception handling blocks.
   - For logging, use `logger` from my `src.logger` module. For example:
     ```python
     from src.logger import logger
     logger.info('Some information message')
     ...
     except SomeError as ex:
         logger.error('Some error message', ex, exc_info = True), where the error is passed as the second argument. exc_info determines whether to output service information.
    ```

    _ If the code uses a webdriver, know how to use it.
    inherit Driver, Chrome, Firexox, Playwright
    Next define like this
    # Creating a driver instance (example with Chrome)
    driver = Drivewr(Chrome)
    The Driver and Chrome, Firexox, Playwright modules already contain all the selenium settings.
    The main command that is used in the code: `driver.execute_locator(l:dict)`
    It returns the value of the web element by the locator.

   - All comments and docstrings must be in Russian in UTF-8 format. If the docstring is in English in the code, translate it into Russian.

2. **Table of Contents (TOC)**:
   - At the beginning of each documentation file, add a section with a table of contents and links to the functions and methods within the code.
   - The table of contents structure should include links to all major sections of the module documentation.

3. **Documentation Formatting**:
   - Use Markdown syntax for all headers, lists, and links.
   - For documenting classes, functions, and methods, include structured sections with descriptions, parameter details, return values, and exceptions raised. Example:

     ## Functions

     ### `function_name`

     **Purpose**: Function purpose.

     **Parameters**:
     - `param` (str): Description of the `param` parameter.
     - `param1` (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.

     **Returns**:
     - `dict | None`: Description of the return value.

     **Raises exceptions**:
     - `SomeError`: Description of the situation in which the `SomeError` exception occurs.

     If there are internal functions inside the function, consider them separately.
     **Internal functions**: If any

     **How the function works**:
     1. <Explain in detail the purpose of the function. Make a detailed description of what actions and transformations occur in the body of the function>

     2. Inside the function, the following actions and transformations occur:
     A
     |
     -- C
     |
     D - E
     |
     F

     Where `A,B,C,D,E,F` are internal logical blocks of the function. Do not use abbreviations A,B,C,... give logical names to the blocks.

     **Examples**:
     - Create several examples with different parameters that are passed to the function

4. **Section Headers**:
   - Use first-level headers (`#`), second-level headers (`##`), third-level headers (`###`), and fourth-level headers (`####`) sequentially throughout the file.

5. **Example File**:

   # Module Name

   ## Overview

   Brief description of the module's purpose.

   ## More Details

   A more detailed description. Explain how and why this code is used in the project.
   Analyze the code previously provided to you

   ## Classes

   ### `ClassName`

   **Description**: Class description.

   **Working principle**:
       Explain the work of the class. If the class is complex, make a detailed analysis of the code

   Create documentation for EACH function or method. Explain the purpose of each variable.
   - All comments and docstrings must be in Russian in UTF-8 format. If the text is written in English in the original code, translate it into Russian

   **Methods**: # if there are methods
   - `method_name`: Brief description of the method.
   - `method_name`: Brief description of the method.
   **Parameters**: # if there are parameters
   - `param` (str): Description of the `param` parameter.
   - `param1` (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.
   **Examples**
   - Examples of defining a class and working with a class

   ## Functions

   ### `function_name`

   ```python
   def my_func(param1:str, param2:Optional[int] = 0) -> bool:
       """ Функция выполняет некоторое действия... <Тут Ты пишешь что именно делает функция>
       Args:
           param1 (str): Description of the `param1` parameter.
           param2 (Optional[int], optional): Description of the `param2` parameter. Defaults to 0.
       Returns:
           bool: Description of the returned value. Returns `True` or `False`.

        Raises:
             Execution error

        Example:
            Examples of calls with the entire range of parameters that can be passed to the function

       """
       - Do not give the function code. Only documentation and examples of calling the function;
       - All comments and docstrings must be in Russian in UTF-8 format
   ```

   **Methods**: # if there are methods
   - `method_name`: More detailed description of the method.
   - `method_name`: More detailed description of the method.

   **Parameters**: # if there are parameters
   - `param` (str): More detailed Description of the `param` parameter.
   - `param1` (Optional[str | dict | str], optional): More detailed Description of the `param1` parameter. Defaults to `None`.

   **Returns**: # if there is a return value
   - `dict | None`: More detailed Description of the returned value.

   **Raises exceptions**: # if there are exceptions
   - `SomeError`: More detailed Description of the situation in which the `SomeError` exception occurs.

   **How the function works**:
    - 1. <Explain in detail the purpose of the function. Make a detailed description of what actions and transformations occur in the body of the function>

    - 2. Inside the function, the following actions and transformations occur:
     A
     |
     -- C
     |
     D - E
     |
     F

     Where `A,B,C,D,E,F` are internal logical blocks of the function. Do not use abbreviations A,B,C,... give logical names to the blocks.

   **Examples**: # All possible examples of calling a function with different parameters

   -------------------------------------------------------------------------------------

## Your behavior when analyzing the code:
- inside the code you may find an expression between `<` `>`. For example: <instruction for the gemini model: Loading product descriptions to PrestaShop.>, <next, if any>. These are blanks where you insert the relevant value
- always look at the system instruction for processing the code of the `hypotez` project;
- analyze the location of the file in the project. This will help to understand its purpose and relationship with other files. You will find the location of the file in the very first line of code, starting with `## \file /...`;
- memorize the provided code and analyze its connection with other parts of the project;
- In this instruction, you do not need to propose code improvement. Clearly follow point 5. **Example file** when composing the answer

# END OF INSTRUCTION
```