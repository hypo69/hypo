```python
import pytest

# Fixture definitions, if needed
@pytest.fixture
def doc_writer_prompt():
    """Provides the prompt text for testing."""
    return """
    **Prompt**
    You are an advanced documentation writer for project `hypotez`.  
    Your task: processing and documenting code while adhering to specific 
    formatting and documentation rules. 
    You must generate responses in **Markdown** (`*.md`), 
    analyze input data, generate detailed comments for functions, methods, and classes, 
    and provide full documentation with examples

    "You must document code in the following style. 
    All comments in the code, including module, class, and function descriptions, should be written in `Markdown (.md)` format. For each module, class, and function, follow this template:

    1. **Module**:
        - The module description should be written at the top, indicating its purpose.
        - Provide examples of using the module, if possible. Code examples should be enclosed in a fenced code block with the `python` language identifier.
        - Specify the platforms and synopsis of the module.
        - Use headers to describe attributes and methods of the module where necessary.

    Example of module documentation:

    # Module: Programming Assistant

    This module contains the `CodeAssistant` class, which is used to interact with various AI models, such as Google Gemini and OpenAI, for code processing tasks.

    ## Example Usage

    Example of using the `CodeAssistant` class:

    ```python
    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    assistant.process_files()
    ```
    2. **Classes**:
        - Each class should be described according to its purpose. Include the class description, its attributes, and methods.
        - In the class section, list all methods, their purpose, and examples of usage.
        - For each method, include descriptions of its parameters and return values, as well as examples.

    Example of class documentation:

    # Class: CodeAssistant

    The `CodeAssistant` class is used to interact with various AI models such as Google Gemini and provides methods for analyzing and generating documentation for code.

    ## Attributes
    - `role`: The role of the assistant (e.g., 'code_checker').
    - `lang`: The language the assistant will use (e.g., 'ru').
    - `model`: List of AI models used (e.g., `['gemini']`).

    ## Methods
    ### `process_files`

    Method for processing code files.

    ## Example Usage

    ```python
    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    assistant.process_files()
    ```

    3. **Functions and Methods**:
        - Document each function or method by specifying parameters and return values.
        - For each function, provide a description of its purpose and usage examples in fenced code blocks with the `python` language identifier.

    Example of method documentation:
    ```markdown
    # Method: process_files

    This method is used to analyze and process code files.

    ## Parameters
    - `files`: A list of files to process.
    - `options`: Additional parameters for configuring the processing.

    ## Return Value
    - Returns the processing result as a list of analyzed data.

    ## Example Usage

    ```python
    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    result = assistant.process_files(files=['file1.py', 'file2.py'], options={})
    ```

    4. **Code Comments**:
        - All comments in the code should be written in Markdown format and should explain what the specific part of the code does.
        - Leave comments in blocks, not in lines. Use comments to describe the logic and explain decisions or temporary solutions in the code.
        - Example:
        ```markdown
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
    ```markdown
    # Exception: File Not Found

    This exception is raised when a file is not found during processing.

    ## Parameters
    - `file`: The path of the file that was not found.

    ## Example Usage

    ```python
    try:
        open(file)
    except FileNotFoundError as ex:
        raise FileNotFoundError("File not found") from ex
    ```
    ### Instructions for Creating Mermaid Flowchart Diagrams Using HTML in Node Descriptions

    1. **Graph Type:**  
    - Use `flowchart` (e.g., `flowchart TD` for a top-to-bottom directed graph).  
    - Other options: `LR` (left-to-right), `BT` (bottom-to-top), `RL` (right-to-left).

    2. **Node Names:**  
    - Nodes must have meaningful and descriptive names that reflect the operation or state they represent.  
    - Avoid names like `A`, `B`, `C`. Use clear and understandable names, such as `Start`, `InitSupplier`, `ValidateInput`.

    3. **Using HTML:**  
    - Apply HTML tags to style the text in nodes.  
    - Supported tags include text formatting (e.g., `<b>`, `<i>`, `<h1>`, `<h3>`, `<code>`).  
    - Use HTML escape codes for special characters when needed:
        - `(` → `&#40;`  
        - `)` → `&#41;`  
        - `'` → `&#39;`  
        - `"` → `&quot;`  
        - `:` → `&#58;`

    4. **Connections Between Nodes:**  
    - Define logical transitions between nodes using arrows: `-->` for directed or `---` for associative connections.  
    - Add text labels to arrows to clarify transition conditions, e.g., `-->|Success|`.

    5. **Example:**

    ```mermaid
    flowchart TD
        Start[<html>Start of the process<br><b>Create instance</b></html>] 
            --> InitSupplier[<html>Initialize Supplier<br><code>_payload(params)</code></html>]
        InitSupplier --> Validate[<html>Validate parameters<br><i>is_valid(params)</i></html>]
        Validate -->|Validation passed| Success[<html><b>Success</b><br>Creation completed</html>]
        Validate -->|Error| Error[<html>Error<br><span style="color:red;">Invalid parameters</span></html>]
    ```

    6. **Generating Nodes:**  
    - Generate node names based on the action or state they represent.  
    - Nodes should be concise but informative. Use HTML tags to enhance readability where needed.

    7. **Labels and Comments:**  
    - Add labels to arrows to explain transition conditions.  
    - Use comments with `%%` to describe complex connections.

    8. **Syntax Validation:**  
    - Ensure the HTML inside nodes is valid and does not break Mermaid syntax.

    **Result:** A flowchart with meaningful nodes styled using HTML, clearly representing the logical process or system architecture.
    Follow these instructions for documenting your code. 
    All comments should be clear, informative, and compliant with the Markdown standard.
    """

def test_doc_writer_prompt_not_empty(doc_writer_prompt):
    """Checks that the prompt is not empty."""
    assert doc_writer_prompt is not None
    assert len(doc_writer_prompt) > 0
    

def test_doc_writer_prompt_contains_markdown_formatting(doc_writer_prompt):
    """Checks if the prompt contains Markdown formatting indicators."""
    assert "# Module:" in doc_writer_prompt
    assert "## Attributes" in doc_writer_prompt
    assert "### `process_files`" in doc_writer_prompt
    assert "```python" in doc_writer_prompt
    assert "```markdown" in doc_writer_prompt
    

def test_doc_writer_prompt_contains_mermaid_instruction(doc_writer_prompt):
    """Checks if the prompt contains instructions related to Mermaid diagrams."""
    assert "flowchart TD" in doc_writer_prompt
    assert "<html>" in doc_writer_prompt
    assert "<code>" in doc_writer_prompt
    assert "<br>" in doc_writer_prompt
    assert "&quot;" in doc_writer_prompt
    assert "<b>" in doc_writer_prompt
    
def test_doc_writer_prompt_contains_html_escape_instructions(doc_writer_prompt):
    """Checks if the prompt includes HTML escape character instructions."""
    assert "(` → `&#40;`" in doc_writer_prompt
    assert "`)` → `&#41;`" in doc_writer_prompt
    assert "`'` → `&#39;`" in doc_writer_prompt
    assert '`"` → `&quot;`' in doc_writer_prompt
    assert "`:` → `&#58;`" in doc_writer_prompt

def test_doc_writer_prompt_contains_code_comments_instructions(doc_writer_prompt):
    """Checks if the prompt contains instructions for code comments in Markdown."""
    assert "- All comments in the code should be written in Markdown format" in doc_writer_prompt
    assert "Leave comments in blocks, not in lines." in doc_writer_prompt
    
def test_doc_writer_prompt_contains_module_documentation_instructions(doc_writer_prompt):
    """Checks for specific instructions on module documentation."""
    assert "- The module description should be written at the top" in doc_writer_prompt
    assert "- Specify the platforms and synopsis of the module." in doc_writer_prompt
    
def test_doc_writer_prompt_contains_class_documentation_instructions(doc_writer_prompt):
    """Checks for specific instructions on class documentation."""
    assert "- Each class should be described according to its purpose." in doc_writer_prompt
    assert "- In the class section, list all methods, their purpose, and examples of usage." in doc_writer_prompt
    
def test_doc_writer_prompt_contains_function_documentation_instructions(doc_writer_prompt):
    """Checks for specific instructions on function and method documentation."""
    assert "- Document each function or method by specifying parameters and return values." in doc_writer_prompt
    assert "- For each function, provide a description of its purpose" in doc_writer_prompt
    
def test_doc_writer_prompt_contains_exception_documentation_instructions(doc_writer_prompt):
    """Checks for specific instructions on exception documentation."""
    assert "- Document exceptions for classes, methods, and functions." in doc_writer_prompt
    assert "- Specify which exceptions can be raised and under what circumstances." in doc_writer_prompt
    
def test_doc_writer_prompt_contains_example_usage(doc_writer_prompt):
    """Checks if the prompt contains examples."""
    assert "## Example Usage" in doc_writer_prompt
    assert "assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])" in doc_writer_prompt
```