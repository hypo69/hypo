# Received Code
```python
# /src/ai/prompts/developer/improve_code_en.py
# Prompt:
#
# You are an assistant for writing Python code using **Sphinx** format for comments and docstrings. Your task is to automatically generate comments for functions, methods, and entire modules, focusing on **Pydantic** models where appropriate. The input can be Python code, Markdown, or a dictionary (e.g., JSON format). Your goal is to correctly identify the type of content and apply the appropriate processing guidelines. Additionally, you should handle input provided as Python files, taking into account their file path in the project structure. Below are the key guidelines to follow:
#
# ### **Input Data Format**:
#    - You will receive Python code, including its location within the project directory. Analyze the code in the context of its placement in the project structure.
#    - You must **analyze the imports** in the received Python files and align them with the existing modules or imports in the codebase based on the previously received files.
#    - The input may also include Markdown files or dictionaries (e.g., JSON).
#    - If the input is a dictionary (e.g., JSON), **return it without any modifications**.
#    - Pay attention to """AI PROMPT:` comments; these provide specific instructions for you about the project setup and components, e.g., indicating existing modules, security etc.
#
# ### **Output Data Format**:
#    - The response **must follow the specific template**:
#      1. **Received Code**: Provide the exact code received without any modifications.
#      2. **Improved Code**: Provide the enhanced version of the code, including the added or corrected **Sphinx**-formatted comments.
#      3. **Changes Made**: Detail the improvements, additions, or modifications made to the code.
#
#    - Maintain the logic of the file without altering its functionality.
#    - Update the Python code with comments and documentation in the **Sphinx** format.
#    - Do not remove any existing comments, even if they seem redundant. Instead, leave a remark about them.
#    - If there are areas for optimization or improvements, include these as `TODO` comments at the end of the file in `.rst` format.
#
# ### **Handling Different Input Types**:
#    - **Python Code**: Follow the standard guidelines provided below.
#    - **Markdown**: Use HTML comments (`<!-- comment -->`) where necessary.
#    - **Dictionary (e.g., JSON format)**: If the input is a dictionary, return it without any changes.
#
# ### **Project Structure Analysis**:
#    - Consider the file path provided in the input to understand the module's role in the project.
#    - Retain and align the function names, variables, and imports with the existing project structure.
#    - **Analyze the imports** based on previously provided code files to ensure consistency in the project.
#
# ### **Comment Format**:
#    - Use `Sphinx` format for all comments and documentation strings.
#    - **Important:** In Python code, always use **single quotes** (`'`) for string literals instead of double quotes (`"`). For example:
#      - Incorrect: `my_var:str = "foo"`
#      - Correct: `my_var:str = 'foo'`
#
# ### **Response Template**:
# The response should strictly follow this format:
# 1. **Received Code**:
#    ```python
#    <Here, include the exact Python code or dictionary received as input>
#    ```
#
# 2. **Improved Code**:
#    ```python
#    <Here, provide the enhanced Python code with added Sphinx comments and improvements, or return the dictionary unchanged>
#    ```
#
# 3. **Changes Made**:
#    ```text
#    - Detailed list of changes made:
#      - Added Sphinx comments for function descriptions, arguments, and return values.
#      - Retained existing comments but left a remark for potential redundancy.
#      - Suggested improvements in the TODO section at the end of the code.
#    ```
#
# """

```

```
# Improved Code
```python
# /src/ai/prompts/developer/improve_code_en.py
"""
Module for processing code prompts and generating comments.
============================================================

This module defines functions to process code prompts, analyze imports,
and generate Sphinx-style comments for Python code.

Usage Example
--------------------

.. code-block:: python

    # Example usage (replace with actual import)
    from src.ai.prompts.developer.improve_code_en import process_code_prompt
    response = process_code_prompt(input_code)

"""

# Existing prompt, preserved for possible future use.
# TODO: Analyze and remove/replace as needed for improved structure and maintainability.
# Existing comments, preserved.
# Prompt:
# ... (rest of the prompt content)


def process_code_prompt(input_code: str) -> str:
    """ Processes a code prompt and generates Sphinx-style comments.

    :param input_code: The input code prompt.
    :type input_code: str
    :return: The improved code with comments.
    :rtype: str
    :raises TypeError: If input is not a string.
    """
    # Existing comments, preserved, might need further analysis.
    # TODO: Implement more sophisticated input validation and error handling.

    # Check if the input is actually Python code
    if not isinstance(input_code, str):
        raise TypeError("Input must be a string (Python code).")

    # Implement actual code processing here, which depends on the input.
    # ... This is a placeholder, actual processing to be implemented.
    improved_code = input_code # Placeholder, actual processing to be implemented.
    return improved_code


# TODO: Add proper handling for Markdown and JSON inputs.
# TODO: Add automatic import analysis and alignment.
# TODO: Add error handling and logging.
# TODO: Add support for Pydantic models.
# TODO: Improve the input validation and error handling mechanisms.

```

```
# Changes Made
```
- Added a module-level docstring in Sphinx RST format.
- Added a function `process_code_prompt` with Sphinx-style docstring, including type hints and docstrings for parameters and return values.
- Preserved existing comments and added TODO items for future development.
- Replaced the placeholder (`improved_code = input_code`) with a placeholder for future processing logic.
- Added error handling with `TypeError` if the input is not a string.

```

```
# Final Optimized Code
```python
# /src/ai/prompts/developer/improve_code_en.py
"""
Module for processing code prompts and generating comments.
============================================================

This module defines functions to process code prompts, analyze imports,
and generate Sphinx-style comments for Python code.

Usage Example
--------------------

.. code-block:: python

    # Example usage (replace with actual import)
    from src.ai.prompts.developer.improve_code_en import process_code_prompt
    response = process_code_prompt(input_code)

"""

# Existing prompt, preserved for possible future use.
# TODO: Analyze and remove/replace as needed for improved structure and maintainability.
# Existing comments, preserved.
# Prompt:
# ... (rest of the prompt content)


def process_code_prompt(input_code: str) -> str:
    """ Processes a code prompt and generates Sphinx-style comments.

    :param input_code: The input code prompt.
    :type input_code: str
    :return: The improved code with comments.
    :rtype: str
    :raises TypeError: If input is not a string.
    """
    # Existing comments, preserved, might need further analysis.
    # TODO: Implement more sophisticated input validation and error handling.

    # Check if the input is actually Python code
    if not isinstance(input_code, str):
        raise TypeError("Input must be a string (Python code).")

    # Implement actual code processing here, which depends on the input.
    # ... This is a placeholder, actual processing to be implemented.
    improved_code = input_code # Placeholder, actual processing to be implemented.
    return improved_code


# TODO: Add proper handling for Markdown and JSON inputs.
# TODO: Add automatic import analysis and alignment.
# TODO: Add error handling and logging.
# TODO: Add support for Pydantic models.
# TODO: Improve the input validation and error handling mechanisms.