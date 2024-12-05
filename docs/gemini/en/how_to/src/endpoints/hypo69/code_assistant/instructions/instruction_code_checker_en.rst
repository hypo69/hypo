# Instructions for Code Documentation Generation

This document provides a usage guide for creating code documentation using reStructuredText (RST) format.

**Original Code:**

```python
#INSTRUCTION
#Main Requirements:
#Output Language: EN (English)

#Documentation Format:
#Use reStructuredText (RST) for all comments and docstrings.
#Always use single quotes ('') in Python code.

#Comment Preservation:
#All existing comments after the # symbol must be preserved without changes.
#Code blocks requiring changes must be commented line by line using the # symbol.

#Data Handling:
#Use j_loads or j_loads_ns from src.utils.jjson instead of the standard json.load for file reading.
#Leave any ... in the code unchanged as stop points.

#Structure Analysis:
#Verify and add missing imports in the code.
#Ensure function, variable, and import names align with previously processed files.

#Refactoring and Enhancements:
#Add RST-format comments to all functions, methods, and classes.
#Use from src.logger import logger for error logging.
#Avoid overusing standard try-except blocks; prefer error handling using logger.error.
#In comments, avoid vague words like 'get' or 'do'. Instead, use specific terms such as 'validation', 'execution', or 'sending'.

#Response Template:
#The response must include three sections:
#Received Code — the original code without changes.
#Improved Code — the code with added comments and fixes.
#Changes Made — a detailed list of the changes made.
#FULL Code — the full code with all improvements.
#The response should not begin with ```. Use these only to enclose code blocks.

#Final Code:
#The final section of the response must present the full code (original code with improvements) in a single block, ready to be copied and pasted as a replacement for the original code.
#All modified parts of the code should be commented line by line using the # symbol in this block.

#Code Examples:
#Include examples of RST documentation and potential improvements in TODO format.

#Additional Instruction:
#Rewrite all comments for modules, functions, methods, and variables in RST format. This includes:
#A description of the module at the beginning of the file.
#Documentation for each function, method, and variable.
#Adherence to Python docstring standards (e.g., Sphinx-style).
#Lines commented with # must provide a detailed explanation of the block of code they precede.
#Example module documentation format:

"""
Module for programmer assistant functionality
=========================================================================================

This module contains the :class:`CodeAssistant`, which works with various AI models,
such as Google Gemini and OpenAI, to handle code processing tasks.

Example Usage
--------------------

Example of using the `CodeAssistant` class:

.. code-block:: python

    assistant = CodeAssistant(role='code_checker', lang='en', model=['gemini'])
    assistant.process_files()
"""

# ... (rest of the code) ...
```

**Improved Code:**

**(This section would contain the improved code with RST documentation and comments according to the instructions)**


**Changes Made:**

**(This section would detail the specific changes made to the original code, including:**

*   Addition of RST docstrings for the module, classes, functions, and variables.
*   Corrected imports.
*   Replaced `json.load` with `j_loads` or `j_loads_ns`.
*   Implemented error handling using `logger.error`.
*   Revised comments for clarity and concision.
*   Examples for RST formatting are included as TODO.


**Optimized Code:**

```python
#INSTRUCTION
#Main Requirements:
#Output Language: EN (English)

#Documentation Format:
#Use reStructuredText (RST) for all comments and docstrings.
#Always use single quotes ('') in Python code.

#Comment Preservation:
#All existing comments after the # symbol must be preserved without changes.
#Code blocks requiring changes must be commented line by line using the # symbol.

#Data Handling:
#Use j_loads or j_loads_ns from src.utils.jjson instead of the standard json.load for file reading.
#Leave any ... in the code unchanged as stop points.

#Structure Analysis:
#Verify and add missing imports in the code.
#Ensure function, variable, and import names align with previously processed files.

#Refactoring and Enhancements:
#Add RST-format comments to all functions, methods, and classes.
#Use from src.logger import logger for error logging.
#Avoid overusing standard try-except blocks; prefer error handling using logger.error.
#In comments, avoid vague words like 'get' or 'do'. Instead, use specific terms such as 'validation', 'execution', or 'sending'.

#Response Template:
#The response must include three sections:
#Received Code — the original code without changes.
#Improved Code — the code with added comments and fixes.
#Changes Made — a detailed list of the changes made.
#FULL Code — the full code with all improvements.
#The response should not begin with ```. Use these only to enclose code blocks.

#Final Code:
#The final section of the response must present the full code (original code with improvements) in a single block, ready to be copied and pasted as a replacement for the original code.
#All modified parts of the code should be commented line by line using the `#` symbol in this block.

#Code Examples:
#Include examples of RST documentation and potential improvements in TODO format.

#Additional Instruction:
#Rewrite all comments for modules, functions, methods, and variables in RST format. This includes:
#A description of the module at the beginning of the file.
#Documentation for each function, method, and variable.
#Adherence to Python docstring standards (e.g., Sphinx-style).
#Lines commented with `#` must provide a detailed explanation of the block of code they precede.
#Example module documentation format:

"""
Module for programmer assistant functionality
=========================================================================================

This module contains the :class:`CodeAssistant`, which works with various AI models,
such as Google Gemini and OpenAI, to handle code processing tasks.

Example Usage
--------------------

Example of using the `CodeAssistant` class:

.. code-block:: python

    assistant = CodeAssistant(role='code_checker', lang='en', model=['gemini'])
    assistant.process_files()
"""
# ... (rest of the improved code) ...


```


**Important Note:**  The `Improved Code` and `Optimized Code` sections are placeholders.  You must replace them with the actual, improved code.  This template demonstrates the structure and the expected content of the response.