# Code Documentation Generation Instructions

## Overview

This document outlines the instructions for generating documentation for Python code files. The generated documentation will be in Markdown format, adhering to a specific structure and style for clarity and ease of understanding.

## Instructions

### 1. Analyze the Code

Carefully review the Python code to understand its functionality, logic, and intended actions.  Identify the input parameters, internal computations, and outputs.

### 2. Create a Step-by-Step Guide

*   **Description:** Provide a clear and concise description of what the code block does.  Avoid ambiguity and use precise language.
*   **Execution Steps:** Outline the sequence of actions performed by the code.  Describe each step in detail, referencing variables and functions as appropriate.
*   **Usage Example:** Offer a complete example of how to use the code block within a larger project. This should include the necessary imports and function calls.  Include input data and expected output.


### 3. Formatting (reStructuredText)

Structure the documentation using the reStructuredText (RST) format as shown in the example below:

```rst
How to use this code block
=========================================================================================

Description
-------------------------
[Explain what the code does. E.g., This code block validates user input.]

Execution steps
-------------------------
1. [First step description. E.g., It reads the input from the user.]
2. [Second step description. E.g., It validates the input against predefined rules.]
3. [Continue as necessary...]

Usage example
-------------------------
.. code-block:: python

    # Example usage code
    # Import necessary modules
    import your_module

    # Example input data
    user_input = "your input data"

    # Function call
    result = your_module.function_name(user_input)

    # Output result
    print(result)
```

### 4. Avoid Vague Language

Be specific and precise in your descriptions. Avoid general terms like "getting" or "doing." Instead, use action verbs that accurately reflect the code's operation, such as "validates," "calculates," "processes," or "sends."  For example, instead of "Getting the input," say "Reads the input from the user."


## Example

```rst
How to validate user input
=========================================================================================

Description
-------------------------
This code block validates user input against predefined rules.

Execution steps
-------------------------
1. It reads the input from the user.
2. It validates the input against a predefined regular expression pattern.
3. It returns 'Valid' if the input matches the pattern, otherwise returns 'Invalid'.

Usage example
-------------------------
.. code-block:: python

    import re

    def validate_input(input_string):
        pattern = r"^[a-zA-Z0-9]+$"  # Example pattern: Alphanumeric characters only
        if re.match(pattern, input_string):
            return "Valid"
        else:
            return "Invalid"

    # Example usage
    user_input = input("Enter your input: ")
    result = validate_input(user_input)
    print(result)
```
```