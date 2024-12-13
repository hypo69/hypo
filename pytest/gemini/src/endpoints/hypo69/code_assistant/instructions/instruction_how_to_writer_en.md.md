```python
import pytest

# No fixtures needed for this particular instruction set, as it's a guide, not executable code.

def test_instruction_description():
    """
    Checks if the instruction guide has a clear description section.
    """
    instruction_text = """**Instructions for Code Documentation Generation**\n\n1. **Analyze the code**: Understand the logic and actions performed by the given code block.\n  \n2. **Create a step-by-step guide**:\n    - **Description**: Explain what the code block does.\n    - **Execution steps**: Outline the sequence of actions in the code.\n    - **Usage example**: Provide a code example showing how to use this block in a project.\n\n3. **Formatting**: Follow the structure in `reStructuredText (RST)`:\n\n```rst\nHow to use this code block\n=========================================================================================\n\nDescription\n-------------------------\n[Explain what the code does.]\n\nExecution steps\n-------------------------\n1. [First step description.]\n2. [Second step description.]\n3. [Continue as necessary...]\n\nUsage example\n-------------------------\n.. code-block:: python\n\n    [Example usage code]\n```\n\n4. **Avoid vague terms** like "getting" or "doing." Be specific about what the code does, e.g., "checks," "validates," or "sends."\n\n```"""
    
    assert "Description\n-------------------------" in instruction_text, "Description section is missing"
    assert "[Explain what the code does.]" in instruction_text, "Description placeholder is missing or incorrect"


def test_instruction_execution_steps():
    """
    Checks if the instruction guide has a clear Execution steps section.
    """
    instruction_text = """**Instructions for Code Documentation Generation**\n\n1. **Analyze the code**: Understand the logic and actions performed by the given code block.\n  \n2. **Create a step-by-step guide**:\n    - **Description**: Explain what the code block does.\n    - **Execution steps**: Outline the sequence of actions in the code.\n    - **Usage example**: Provide a code example showing how to use this block in a project.\n\n3. **Formatting**: Follow the structure in `reStructuredText (RST)`:\n\n```rst\nHow to use this code block\n=========================================================================================\n\nDescription\n-------------------------\n[Explain what the code does.]\n\nExecution steps\n-------------------------\n1. [First step description.]\n2. [Second step description.]\n3. [Continue as necessary...]\n\nUsage example\n-------------------------\n.. code-block:: python\n\n    [Example usage code]\n```\n\n4. **Avoid vague terms** like "getting" or "doing." Be specific about what the code does, e.g., "checks," "validates," or "sends."\n\n```"""

    assert "Execution steps\n-------------------------" in instruction_text, "Execution steps section is missing"
    assert "1. [First step description.]" in instruction_text, "First step placeholder is missing or incorrect"
    assert "2. [Second step description.]" in instruction_text, "Second step placeholder is missing or incorrect"
    assert "3. [Continue as necessary...]" in instruction_text, "Third step placeholder is missing or incorrect"



def test_instruction_usage_example():
     """
     Checks if the instruction guide has a clear Usage example section with a code block.
     """
     instruction_text = """**Instructions for Code Documentation Generation**\n\n1. **Analyze the code**: Understand the logic and actions performed by the given code block.\n  \n2. **Create a step-by-step guide**:\n    - **Description**: Explain what the code block does.\n    - **Execution steps**: Outline the sequence of actions in the code.\n    - **Usage example**: Provide a code example showing how to use this block in a project.\n\n3. **Formatting**: Follow the structure in `reStructuredText (RST)`:\n\n```rst\nHow to use this code block\n=========================================================================================\n\nDescription\n-------------------------\n[Explain what the code does.]\n\nExecution steps\n-------------------------\n1. [First step description.]\n2. [Second step description.]\n3. [Continue as necessary...]\n\nUsage example\n-------------------------\n.. code-block:: python\n\n    [Example usage code]\n```\n\n4. **Avoid vague terms** like "getting" or "doing." Be specific about what the code does, e.g., "checks," "validates," or "sends."\n\n```"""
     
     assert "Usage example\n-------------------------" in instruction_text, "Usage example section is missing"
     assert ".. code-block:: python" in instruction_text, "Code block marker is missing"
     assert "    [Example usage code]" in instruction_text, "Usage example code placeholder is missing or incorrect"


def test_instruction_formatting():
    """
    Checks if the instruction specifies reStructuredText (RST) formatting.
    """
    instruction_text = """**Instructions for Code Documentation Generation**\n\n1. **Analyze the code**: Understand the logic and actions performed by the given code block.\n  \n2. **Create a step-by-step guide**:\n    - **Description**: Explain what the code block does.\n    - **Execution steps**: Outline the sequence of actions in the code.\n    - **Usage example**: Provide a code example showing how to use this block in a project.\n\n3. **Formatting**: Follow the structure in `reStructuredText (RST)`:\n\n```rst\nHow to use this code block\n=========================================================================================\n\nDescription\n-------------------------\n[Explain what the code does.]\n\nExecution steps\n-------------------------\n1. [First step description.]\n2. [Second step description.]\n3. [Continue as necessary...]\n\nUsage example\n-------------------------\n.. code-block:: python\n\n    [Example usage code]\n```\n\n4. **Avoid vague terms** like "getting" or "doing." Be specific about what the code does, e.g., "checks," "validates," or "sends."\n\n```"""

    assert "reStructuredText (RST)" in instruction_text, "RST format is not specified"

def test_instruction_vague_terms_avoidance():
    """
    Checks if the instruction advises against using vague terms like "getting" or "doing".
    """
    instruction_text = """**Instructions for Code Documentation Generation**\n\n1. **Analyze the code**: Understand the logic and actions performed by the given code block.\n  \n2. **Create a step-by-step guide**:\n    - **Description**: Explain what the code block does.\n    - **Execution steps**: Outline the sequence of actions in the code.\n    - **Usage example**: Provide a code example showing how to use this block in a project.\n\n3. **Formatting**: Follow the structure in `reStructuredText (RST)`:\n\n```rst\nHow to use this code block\n=========================================================================================\n\nDescription\n-------------------------\n[Explain what the code does.]\n\nExecution steps\n-------------------------\n1. [First step description.]\n2. [Second step description.]\n3. [Continue as necessary...]\n\nUsage example\n-------------------------\n.. code-block:: python\n\n    [Example usage code]\n```\n\n4. **Avoid vague terms** like "getting" or "doing." Be specific about what the code does, e.g., "checks," "validates," or "sends."\n\n```"""

    assert "Avoid vague terms" in instruction_text, "Advice against vague terms is missing"
    assert "getting" in instruction_text, "Example vague term 'getting' is missing"
    assert "doing" in instruction_text, "Example vague term 'doing' is missing"
    assert "checks" in instruction_text, "Example specific term 'checks' is missing"
    assert "validates" in instruction_text, "Example specific term 'validates' is missing"
    assert "sends" in instruction_text, "Example specific term 'sends' is missing"
```