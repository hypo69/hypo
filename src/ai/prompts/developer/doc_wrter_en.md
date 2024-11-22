
  "prompt": "You must document code in the following style. All comments in the code, including module, class, and function descriptions, should be written in reStructuredText (RST) format. For each module, class, and function, follow this template:

1. **Module**:
    - The module description should be written in the header, indicating its purpose.
    - Provide examples of using the module, if possible. Code examples should be enclosed in a `.. code-block:: python` block.
    - Specify the platforms and synopsis of the module.
    - Use headers for attributes and methods of the module where necessary.

Example of module documentation:
```
Module for working with a programming assistant
=========================================================================================

This module contains the :class:`CodeAssistant` class, which is used to interact with various AI models, 
such as Google Gemini and OpenAI, for code processing tasks.

Example usage
--------------------

Example of using the `CodeAssistant` class:

.. code-block:: python

    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    assistant.process_files()
```

2. **Classes**:
    - Each class should be described according to its purpose. Include the class description, its attributes, and methods.
    - In the class section, list all methods, their purpose, and examples of usage.
    - For each method, include descriptions of its parameters and return values, as well as examples.

Example of class documentation:
```
Class for working with the programming assistant
=========================================================================================

The :class:`CodeAssistant` class is used to interact with various AI models such as Google Gemini, 
and provides methods for analyzing and generating documentation for code.

Attributes:
----------
- `role`: The role of the assistant (e.g., 'code_checker').
- `lang`: The language the assistant will use (e.g., 'ru').
- `model`: List of AI models used (e.g., ['gemini']).

Methods:
--------
- `process_files`: Method for processing code files.

Example usage:
---------------------

.. code-block:: python

    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    assistant.process_files()
```

3. **Functions and Methods**:
    - Document each function or method by specifying parameters and return values.
    - For each function, provide a description of its purpose and usage examples in the `.. code-block:: python` format.

Example of method documentation:
```
Method for processing files
=========================================================================================

This method is used to analyze and process code files.

Parameters:
-----------
- `files`: A list of files to process.
- `options`: Additional parameters for configuring the processing.

Return value:
----------------------
- Returns the processing result as a list of analyzed data.

Example usage:
---------------------

.. code-block:: python

    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    result = assistant.process_files(files=['file1.py', 'file2.py'], options={})
```

4. **Code Comments**:
    - All comments in the code should be written in RST format and should explain what the specific part of the code does.
    - Leave comments in blocks, not in lines. Use comments to describe the logic and explain decisions or temporary solutions in the code.
    - Example:
    ```
    # Here, the exception is being handled to continue execution if the file is not found
    try:
        process_file(file)
    except FileNotFoundError as ex:
        handle_exception(ex)
    ```

5. **Exceptions**:
    - Document exceptions for classes, methods, and functions.
    - Specify which exceptions can be raised and under what circumstances.

Example of exception documentation:
```
File Not Found Exception
=========================================================================================

This exception is raised when a file is not found during processing.

Parameters:
-----------
- `file`: The path of the file that was not found.

Example usage:
---------------------

.. code-block:: python

    try:
        open(file)
    except FileNotFoundError as ex:
        raise FileNotFoundError("File not found") from ex
```

Follow these instructions for documenting your code. All comments should be clear, informative, and compliant with the RST standard."

This prompt details how to correctly write documentation for code using RST templates, including descriptions of modules, classes, methods, functions, and exceptions, along with usage examples in code blocks."
