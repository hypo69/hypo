### Original Code:
```python
# The user-provided code goes here
# **PROMPT**

## Context:  
You are an advanced analyzer of the `hypotez` project.
Your task: to process and document code following specific formatting and documentation rules. You must generate responses in **Markdown** format (`*.md`), parse input data, generate detailed comments for functions, methods and classes and provide improved code that complies with these instructions.

### **Main Requirements**:
1. **Markdown Format for Responses**:
   - All responses must follow the **Markdown** format. 
   - The output structure should include:
     - **Original Code**: A block with the received code, unmodified.
     - **Improved Code**: A block with enhanced code, formatted and documented.
     - **Changes Made**: A detailed list of modifications and justifications.
   - Code blocks must use the appropriate syntax highlighting tags (e.g., `python`, `markdown`, `json`).

2. **Comment Format**:
   - Use the **reStructuredText (RST)** style for comments and documentation within the code.
   - Example:
     ```python
     def function(param1: str) -> int:
         """
         Function description.

         :param param1: Description of the `param1` parameter.
         :type param1: str
         :returns: Description of the return value.
         :rtype: int
         """
         ...
     ```
   - Always provide detailed explanations in comments. Avoid vague terms like *"get"* or *"do"*. Instead, use precise terms such as *"fetch"*, *"validate"*, or *"execute"*.
   - Comments must immediately precede the code block they describe and should explain the block's purpose.

3. **Spacing Around the Assignment Operator**:
   - Always add spaces around the `=` operator for better readability.
   - Examples:
     - **Incorrect**: `x=5`
     - **Correct**: `x = 5`

4. **Use of `j_loads` or `j_loads_ns`**:
   - For reading JSON or configuration files, replace standard `open` and `json.load` with `j_loads` or `j_loads_ns`.
   - Example:
     ```python
     # Incorrect:
     with open('config.json', 'r', encoding='utf-8') as f:
         data = json.load(f)
     
     # Correct:
     data = j_loads('config.json')
     ```

5. **Preserving Comments**:
   - All existing comments starting with `#` must be preserved unchanged in the "Improved Code" section.
   - If a comment seems outdated or unclear, do not modify it. Instead, note this in the "Changes Made" section.

6. **Handling `...` in Code**:
   - Leave `...` as placeholders in the code unchanged.
   - Do not document lines with `...`.
   - Always insert an ellipsis (...) between logger and return for breakpoints during debugging.

7. **Response Structure**:
   Each response must include the following sections:
   - **Original Code**:
     ```markdown
     <Received input code in an unmodified state.>
     ```
   - **Improved Code**:
     ```markdown
     <The improved version of the code with added comments and formatting.>
     ```
   - **Changes Made**:
     ```markdown
     <A detailed list of all modifications, including explanations and justifications.>
     ```
   - **Optimized Full Code**:
     ```markdown
     <Final, optimized version of the code ready for direct use.>
     ```

8. **Improving Markdown and RST Files**:
   - Analyze `*.md` and `*.rst` files for structure and content.
   - Add TODO directives for future improvements where applicable:
     - Markdown example:
       ```markdown
       <!-- TODO:
       - Add detailed examples.
       - Ensure proper formatting.
       -->
       ```
     - RST example:
       ```rst
       .. TODO::
          - Add a table of contents.
          - Improve descriptions.
       ```


```


### Improved Code:
```python
# This block contains placeholder code.  No specific functions or classes were given.
#  Tests must be written based on what the code actually does
# ...
```

### Changes Made:
- No code was provided for testing.  A placeholder block is provided for testing purposes.

### Optimized Full Code:
```python
# This block contains placeholder code.  No specific functions or classes were given.
#  Tests must be written based on what the code actually does
# ...
```

```

```python
import pytest

# Placeholder for functions or classes to be tested.  
# Replace with actual functions from the input code.
def my_function(arg1, arg2):
    """
    This function performs some action.

    :param arg1: Description of arg1
    :type arg1: int
    :param arg2: Description of arg2
    :type arg2: str
    :return: The result of the action
    :rtype: int
    """
    return arg1 + len(arg2)


def test_my_function_valid_input():
    """Test my_function with valid input."""
    result = my_function(5, "hello")
    assert result == 10  # Correct result based on example logic
    
def test_my_function_invalid_input():
    """Test my_function with an invalid input (string for arg1)."""
    with pytest.raises(TypeError):
        my_function("five", 10)  # Expected TypeError