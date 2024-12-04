```python
import pytest

class CodeAssistant:
    """
    Class for working with different AI models for code processing.

    :param role: The role of the assistant (e.g., 'code_checker').
    :param lang: The language the assistant will work in (e.g., 'ru').
    :param model: A list of AI models in use (e.g., ['gemini']).
    :raises TypeError: If input parameters are of incorrect type.
    :raises ValueError: If input parameters have invalid values.
    """
    def __init__(self, role, lang, model):
        """
        Initializes the CodeAssistant with the given parameters.
        """
        if not isinstance(role, str):
            raise TypeError("Role must be a string")
        if not isinstance(lang, str):
            raise TypeError("Language must be a string")
        if not isinstance(model, list):
            raise TypeError("Model must be a list")
        self.role = role
        self.lang = lang
        self.model = model

    def process_files(self, files, options={}):
        """
        Processes a list of files using the configured AI models.

        :param files: A list of file paths to process.
        :param options: Additional parameters for file processing.
        :type files: list
        :type options: dict
        :raises TypeError: If the `files` parameter is not a list.
        :raises FileNotFoundError: If a file in the list doesn't exist.
        :returns: A list of processed data from each file.
        """
        if not isinstance(files, list):
            raise TypeError("Files must be a list of strings")
        results = []
        for file in files:
            try:
                # Simulate processing a file.  Replace with actual processing.
                # This example returns the file name.
                results.append(file) 
            except FileNotFoundError as ex:
                raise FileNotFoundError(f"File not found: {file}") from ex
        return results

# Tests for CodeAssistant class
def test_code_assistant_valid_input():
    """Tests CodeAssistant with valid input."""
    assistant = CodeAssistant(role='code_checker', lang='en', model=['gemini'])
    files = ['file1.txt', 'file2.txt']
    results = assistant.process_files(files)
    assert results == ['file1.txt', 'file2.txt']

def test_code_assistant_invalid_role_type():
    """Tests CodeAssistant with invalid role type."""
    with pytest.raises(TypeError):
        CodeAssistant(role=123, lang='en', model=['gemini'])

def test_code_assistant_invalid_files_type():
    """Tests CodeAssistant with invalid files type."""
    assistant = CodeAssistant(role='code_checker', lang='en', model=['gemini'])
    with pytest.raises(TypeError):
        assistant.process_files('not a list')
    
def test_code_assistant_file_not_found():
    """Tests CodeAssistant with a file that does not exist."""
    assistant = CodeAssistant(role='code_checker', lang='en', model=['gemini'])
    files = ['nonexistent_file.txt']
    with pytest.raises(FileNotFoundError) as excinfo:
        assistant.process_files(files)
    assert "nonexistent_file.txt" in str(excinfo.value)

```