### Original Code
```markdown
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
### Original Code
```python
def add_numbers(a,b):
    return a+b
```

### Improved Code
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

### Changes Made
- Added RST-style docstring to document the function.
- Added type annotations for `a` and `b`.
- Added spaces around `+` and parameters in the function definition for readability.

### Optimized Full Code
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
```

### <algorithm>

The provided code describes requirements and examples for code analysis and improvement, not a specific algorithm to be executed.  It outlines a process for receiving, analyzing, and documenting Python code.  There is no step-by-step execution flow as there is no executable code.

### <mermaid>

```mermaid
graph LR
    A[Input Code] --> B{Analysis};
    B --> C[Documentation];
    C --> D[Improved Code];
    D --> E[Optimized Full Code];
    E --> F[Output];
```

**Explanation of Dependencies:**

The code snippets are self-contained and don't rely on external libraries beyond the Python standard library.  It describes rules for documentation and formatting, but does not itself contain any imports or dependencies to other Python modules.


### <explanation>

The provided code is a set of instructions, examples, and guidelines, not a Python program. It details the requirements and format for analyzing and improving other Python code.  No executable code is present.

- **Imports:** There are no imports; the code is focused on defining requirements, not executing a program.
- **Classes:** There are no classes defined; the code describes requirements for documenting functions.
- **Functions:** The `add_numbers` function example is presented as a method for demonStarting the expected documentation format.
- **Variables:** The examples use variables like `a` and `b`, but their types and purpose are clearly stated in comments, showing the required level of detail for function definition improvements.
- **Possible errors/improvements:** The document correctly points out the need for clear and specific documentation, precise language, and standardized formatting in Python code. The guidelines for `j_loads` and `j_loads_ns` suggest a potential dependency on a custom function or library not included in the standard Python library. This could be a library to handle JSON data in a specific way, such as loading from an external file or resource.