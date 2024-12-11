# <input code>

```python
"prompt": "You must document code in the following style. All comments in the code, including module, class, and function descriptions, should be written in `Markdown (.md)` format. For each module, class, and function, follow this template:\n\n1. **Module**:\n    - The module description should be written at the top, indicating its purpose.\n    - Provide examples of using the module, if possible. Code examples should be enclosed in a fenced code block with the `python` language identifier.\n    - Specify the platforms and synopsis of the module.\n    - Use headers to describe attributes and methods of the module where necessary.\n\nExample of module documentation:\n```markdown\n# Module: Programming Assistant\n\nThis module contains the `CodeAssistant` class, which is used to interact with various AI models, such as Google Gemini and OpenAI, for code processing tasks.\n\n## Example Usage\n\nExample of using the `CodeAssistant` class:\n\n```python\nassistant = CodeAssistant(role=\'code_checker\', lang=\'ru\', model=[\'gemini\'])\nassistant.process_files()\n```\n```\n\n2. **Classes**:\n    - Each class should be described according to its purpose. Include the class description, its attributes, and methods.\n    - In the class section, list all methods, their purpose, and examples of usage.\n    - For each method, include descriptions of its parameters and return values, as well as examples.\n\nExample of class documentation:\n```markdown\n# Class: CodeAssistant\n\nThe `CodeAssistant` class is used to interact with various AI models such as Google Gemini and provides methods for analyzing and generating documentation for code.\n\n## Attributes\n- `role`: The role of the assistant (e.g., \'code_checker\').\n- `lang`: The language the assistant will use (e.g., \'ru\').\n- `model`: List of AI models used (e.g., `[\'gemini\']`).\n\n## Methods\n### `process_files`\n\nMethod for processing code files.\n\n## Example Usage\n\n```python\nassistant = CodeAssistant(role=\'code_checker\', lang=\'ru\', model=[\'gemini\'])\nassistant.process_files()\n```\n```\n\n3. **Functions and Methods**:\n    - Document each function or method by specifying parameters and return values.\n    - For each function, provide a description of its purpose and usage examples in fenced code blocks with the `python` language identifier.\n\nExample of method documentation:\n```markdown\n# Method: process_files\n\nThis method is used to analyze and process code files.\n\n## Parameters\n- `files`: A list of files to process.\n- `options`: Additional parameters for configuring the processing.\n\n## Return Value\n- Returns the processing result as a list of analyzed data.\n\n## Example Usage\n\n```python\nassistant = CodeAssistant(role=\'code_checker\', lang=\'ru\', model=[\'gemini\'])\nresult = assistant.process_files(files=[\'file1.py\', \'file2.py\'], options={})\n```\n```\n\n4. **Code Comments**:\n    - All comments in the code should be written in Markdown format and should explain what the specific part of the code does.\n    - Leave comments in blocks, not in lines. Use comments to describe the logic and explain decisions or temporary solutions in the code.\n    - Example:\n    ```markdown\n    # Here, the exception is being handled to continue execution if the file is not found\n    try:\n        process_file(file)\n    except FileNotFoundError as ex:\n        handle_exception(ex)\n    ```\n5. **Exceptions**:\n    - Document exceptions for classes, methods, and functions.\n    - Specify which exceptions can be raised and under what circumstances.\n\nExample of exception documentation:\n```markdown\n# Exception: File Not Found\n\nThis exception is raised when a file is not found during processing.\n\n## Parameters\n- `file`: The path of the file that was not found.\n\n## Example Usage\n\n```python\ntry:\n    open(file)\nexcept FileNotFoundError as ex:\n    raise FileNotFoundError("File not found") from ex\n```\n```\n\nFollow these instructions for documenting your code. All comments should be clear, informative, and compliant with the Markdown standard."\n```

```markdown
# <algorithm>

No algorithm can be derived from this code snippet. It is a descriptive prompt, not executable code.

# <mermaid>

```mermaid
graph TD
    A[Prompt] --> B(Documentation);
    B --> C{Module};
    C -- Module Description --> D[Module Description];
    C -- Example Usage --> E[Example Usage (Python)];
    C -- Attributes --> F[Attributes];
    C -- Methods --> G[Methods];
    B --> H{Class};
    H -- Class Description --> I[Class Description];
    H -- Attributes --> J[Attributes];
    H -- Methods --> K[Methods (e.g., process_files)];
    K -- Parameters --> L[Parameters];
    K -- Return Value --> M[Return Value];
    K -- Example Usage --> N[Example Usage (Python)];

```

# <explanation>

The provided code is a *prompt* instructing on how to document code using Markdown. It outlines a specific style for commenting on modules, classes, functions, and methods.  It doesn't contain executable code itself.  It defines a documentation template that should be followed when writing comments in code.  There are no imports, classes, or functions to analyze.

**Possible Improvements:**

* The prompt could be more concise by focusing on specific markdown syntax and formatting examples rather than providing lengthy prose descriptions for each documentation level.  This would improve its applicability for use in code.
* It should include more practical examples of how to document code (including actual code blocks) to illuStarte the usage of markdown and python syntax.


**Relationships with other parts of the project (since there's no code to analyze):**

N/A. This prompt acts as a guide for a separate codebase to adhere to certain documentation standards.