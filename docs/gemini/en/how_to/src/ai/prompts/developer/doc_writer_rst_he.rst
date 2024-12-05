rst
How to Document Code in reStructuredText (RST) Format
=========================================================================================

Description
-------------------------
This guide outlines how to document Python code using the reStructuredText (RST) format.  It details the structure for documenting modules, classes, functions, and methods, including explanations of parameters, return values, and exception handling.  It also emphasizes clear, concise, and informative documentation.

Execution steps
-------------------------
1. **Module Documentation:**
   - Begin with a descriptive title for the module, stating its purpose.
   - Include usage examples using the `.. code-block:: python` directive.
   - Specify the platforms and synopsis of the module.
   - Use headings for features and methods as needed.

2. **Class Documentation:**
   - Document each class, explaining its purpose, attributes, and methods.
   - For significant classes, include all methods, their purpose, and usage examples.
   - For each method, provide a detailed description of parameters, return values, and any exceptions that might be raised.

3. **Function/Method Documentation:**
   - Document all functions and methods, specifying parameters and return values.
   - Include a clear description of the function's purpose.
   - Use the `.. code-block:: python` directive to show usage examples.

4. **In-Line Comments:**
   - Maintain RST formatting in comments to describe specific code sections.
   - Explain the logic, decisions, or temporary solutions within code blocks using comments.

5. **Exception Handling:**
   - Document all exceptions that might be raised within classes, methods, and functions.
   - Specify the conditions under which these exceptions occur.

Usage example (Module Example)
-------------------------
.. code-block:: rst

Module for Working with a Code Assistant
=========================================================================================

This module contains the :class:`CodeAssistant` class, used to interact with various AI models, such as Google Gemini and OpenAI, for code processing tasks.

Usage Example
--------------------

.. code-block:: python

    from code_assistant import CodeAssistant

    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    assistant.process_files()

Usage example (Class Example)
-------------------------
.. code-block:: rst

Class for Working with a Code Assistant
=========================================================================================

The :class:`CodeAssistant` class interacts with AI models like Google Gemini and provides methods for analyzing and documenting code.

Attributes
----------
- `role`: The role of the assistant (e.g., 'code_checker').
- `lang`: The language the assistant will use (e.g., 'ru').
- `model`: A list of AI models used (e.g., ['gemini']).

Methods
-------
- `process_files`: Method for processing code files.

Usage Example
--------------------

.. code-block:: python

    from code_assistant import CodeAssistant

    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    assistant.process_files()