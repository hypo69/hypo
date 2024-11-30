### Original Code:
```python
# **PROMPT**

## Context:  
You are an advanced Python code analyzer responsible for processing and documenting code while adhering to specific formatting and documentation rules. You must generate responses in **Markdown** (`*.md`) format, analyze input data, generate detailed comments for functions, methods, and classes, and provide improved code based on these instructions.

---

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


---

### **Examples**:

#### Example 1 (Python Code):
Input:
```python
def add_numbers(a,b):
    return a+b
```

Expected Response:

```markdown
### Original Code:
```python
def add_numbers(a,b):
    return a+b
```

### Improved Code:
```python
def add_numbers(a: int, b: int) -> int:
    """
    Adds two numbers.

    :param a: The first number.
    :type a: int
    :param b: The second number.
    :type b: int
    :returns: The sum of `a` and `b`.
    :rtype: int
    """
    return a + b
```

### Changes Made:
- Added RST-style docstring to document the function.
- Added type annotations for `a` and `b`.
- Added spaces around `+` and parameters in the function definition for readability.

### Optimized Full Code:
```python
def add_numbers(a: int, b: int) -> int:
    """
    Adds two numbers.

    :param a: The first number.
    :type a: int
    :param b: The second number.
    :type b: int
    :returns: The sum of `a` and `b`.
    :rtype: int
    """
    return a + b
```
```
```python
# The user-provided code goes here
# ... (This is empty in the original prompt)
```

### Improved Code:
```python
# No code provided.  Please provide Python code for testing.
```

### Changes Made:
No changes made as no code was provided.

### Optimized Full Code:
```python
# No code provided. Please provide Python code for testing.
```
```
```
```python
import pytest

# Placeholder for the actual functions.  Replace with your functions
def my_function(input_data):
  # Example function. Replace with your actual function
  return input_data * 2

def my_other_function(input_data):
  if input_data > 10:
    return input_data * 3
  else:
    return input_data * 2

# Test functions
def test_my_function_valid_input():
    """Checks correct behavior with valid input."""
    result = my_function(5)
    assert result == 10

def test_my_function_invalid_input():
  """Tests incorrect handling of invalid input."""
  with pytest.raises(TypeError):  # Expecting TypeError if input is not int
    my_function("hello")
    
def test_my_other_function_valid_input():
    """Checks the behavior with valid input."""
    result = my_other_function(15)
    assert result == 45

def test_my_other_function_edge_case():
    """Checks the behavior with an edge case."""
    result = my_other_function(10)
    assert result == 20

def test_my_other_function_invalid_input():
    """Tests incorrect handling of invalid input."""
    with pytest.raises(TypeError):  # Expecting TypeError if input is not int
      my_other_function("hello")
```
```markdown
### Original Code:
```python
# The user-provided code goes here
# ...
```

### Improved Code:
```python
import pytest

# Placeholder for the actual functions.  Replace with your functions
def my_function(input_data):
  # Example function. Replace with your actual function
  return input_data * 2

def my_other_function(input_data):
  if input_data > 10:
    return input_data * 3
  else:
    return input_data * 2

# Test functions
def test_my_function_valid_input():
    """Checks correct behavior with valid input."""
    result = my_function(5)
    assert result == 10

def test_my_function_invalid_input():
  """Tests incorrect handling of invalid input."""
  with pytest.raises(TypeError):  # Expecting TypeError if input is not int
    my_function("hello")
    
def test_my_other_function_valid_input():
    """Checks the behavior with valid input."""
    result = my_other_function(15)
    assert result == 45

def test_my_other_function_edge_case():
    """Checks the behavior with an edge case."""
    result = my_other_function(10)
    assert result == 20

def test_my_other_function_invalid_input():
    """Tests incorrect handling of invalid input."""
    with pytest.raises(TypeError):  # Expecting TypeError if input is not int
      my_other_function("hello")
```

### Changes Made:
- Added placeholder functions `my_function` and `my_other_function` to illustrate how tests would be written.  Replace with your actual functions.
- Created test functions to cover valid input, invalid input, and edge cases.
- Used `pytest.raises` for exception handling tests.
- Added docstrings to test functions.

### Optimized Full Code:
```python
import pytest

# Placeholder for the actual functions.  Replace with your functions
def my_function(input_data):
  # Example function. Replace with your actual function
  return input_data * 2

def my_other_function(input_data):
  if input_data > 10:
    return input_data * 3
  else:
    return input_data * 2

# Test functions
def test_my_function_valid_input():
    """Checks correct behavior with valid input."""
    result = my_function(5)
    assert result == 10

def test_my_function_invalid_input():
  """Tests incorrect handling of invalid input."""
  with pytest.raises(TypeError):  # Expecting TypeError if input is not int
    my_function("hello")
    
def test_my_other_function_valid_input():
    """Checks the behavior with valid input."""
    result = my_other_function(15)
    assert result == 45

def test_my_other_function_edge_case():
    """Checks the behavior with an edge case."""
    result = my_other_function(10)
    assert result == 20

def test_my_other_function_invalid_input():
    """Tests incorrect handling of invalid input."""
    with pytest.raises(TypeError):  # Expecting TypeError if input is not int
      my_other_function("hello")
```