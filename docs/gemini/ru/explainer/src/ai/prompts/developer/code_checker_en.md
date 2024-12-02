### Original Code:

```markdown
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
...
```
```

### Improved Code:

```
(Empty - no code to improve)
```

### Changes Made:

(Empty - no code to improve)


### Optimized Full Code:

```
(Empty - no code to improve)
```
```

### <algorithm>

(No algorithm can be described as there is no code to analyze)


### <mermaid>

(No mermaid code can be generated as there is no code to analyze)


### <explanation>

(No explanation can be provided as there is no code to analyze)