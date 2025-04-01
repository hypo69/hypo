```markdown
### **System Instructions for Processing the `hypotez` Project Code**

=========================================================================================

Description of functionality and rules for generating, analyzing, and improving code. Aims to ensure a consistent and readable coding style that meets requirements.

---

### **Key Principles**

#### **1. General Guidelines**:
- Maintain a clear and understandable coding style.
- All changes must be justified and comply with the established requirements.

#### **2. Comments**:
- Use `#` for internal comments.
- The documentation for all functions, methods, and classes should follow this format:
    ```python
        def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
            """
            Args:
                param (str): Description of the `param` parameter.
                param1 (Optional[str | dict | str], optional): Description of the `param1` parameter. Defaults to `None`.
    
            Returns:
                dict | None: Description of the return value. Returns a dictionary or `None`.
    
            Raises:
                SomeError: Description of the situation in which the `SomeError` exception occurs.

            Example:
                >>> function('param', 'param1')
                {'param': 'param1'}
            """
    ```
- Comments and documentation should be clear, concise, and accurate.

#### **3. Code Formatting**:
- Use single quotes. `a:str = 'value'`, `print('Hello World!')`;
- Add spaces around operators. For example, `x = 5`;
- All parameters must be type-annotated. `def function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:`;
- Do not use `Union`. Use `|` instead.

#### **4. Logging**:
- Always use the `logger` module from `src.logger.logger` for logging.
- Errors should be logged using `logger.error`.
Example:
    ```python
        try:
            ...
        except Exception as ex:
            logger.error('Error while processing data', ех, exc_info=True)
    ```
#### **5. Do not use `Union[]` in the code. Instead, use `|`**
For example:
```python
x: str | int ...
```

---

### **Main Requirements**:

#### **1. Markdown Response Format**:
- All answers must be provided in **Markdown** format.

#### **2. Comment Format**:
- Use the specified style for comments and documentation in the code.
- Example:

```python
from typing import Generator, Optional, List
from pathlib import Path


def read_text_file(
    file_path: str | Path,
    as_list: bool = False,
    extensions: Optional[List[str]] = None,
    chunk_size: int = 8192,
) -> Generator[str, None, None] | str | None:
    """
    Reads the content of a file (or files from a directory) using a generator to save memory.

    Args:
        file_path (str | Path): Path to the file or directory.
        as_list (bool): If `True`, returns a generator of strings.
        extensions (Optional[List[str]]): List of file extensions to read from the directory.
        chunk_size (int): Size of chunks to read the file in bytes.

    Returns:
        Generator[str, None, None] | str | None: Generator of strings, concatenated string, or `None` in case of error.

    Raises:
        Exception: If an error occurs while reading the file.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> content = read_text_file(file_path)
        >>> if content:
        ...    print(f'File content: {content[:100]}...')
        File content: Example text...
    """
    ...
```
- Always provide detailed explanations in the comments. Avoid vague terms such as *«get»* or *«do»*. Instead, use precise terms such as *«extract»*, *«check»*, *«execute»*.
- Instead of: *«we get»*, *«we return»*, *«we transform»*, use the object name *«function gets»*, *«variable returns»*, *«code transforms»*
- Comments should directly precede the described code block and explain its purpose.

#### **3. Spaces Around Assignment Operators**:
- Always add spaces around the `=` operator to improve readability.
- Examples:
  - **Incorrect**: `x=5`
  - **Correct**: `x = 5`

#### **4. Using `j_loads` or `j_loads_ns`**:
- For reading JSON or configuration files, replace the standard use of `open` and `json.load` with `j_loads` or `j_loads_ns`.
- Example:

```python
# Incorrect:
with open('config.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Correct:
data = j_loads('config.json')
```

#### **5. Preserving Comments**:
- All existing comments starting with `#` must be preserved without changes in the "Improved Code" section.
- If a comment seems outdated or unclear, do not modify it. Instead, mark it in the "Changes" section.

#### **6. Handling `...` in Code**:
- Leave `...` as placeholders in the code unchanged.
- Do not document lines with `...`.
```