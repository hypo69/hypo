```python
import pytest

# Example Code (replace with the actual Python code to be tested)
class CodeAssistant:
    """
    Class for working with a programming assistant.

    :param role: The role of the assistant (e.g., 'code_checker').
    :param lang: The language the assistant will use (e.g., 'ru').
    :param model: List of AI models used (e.g., ['gemini']).
    :vartype role: str
    :vartype lang: str
    :vartype model: list
    """
    def __init__(self, role, lang, model):
        """
        Initializes the CodeAssistant object.

        :param role: The role of the assistant.
        :param lang: The language the assistant will use.
        :param model: List of AI models to use.
        """
        self.role = role
        self.lang = lang
        self.model = model
    
    def process_files(self, files, options={}):
        """
        Processes a list of code files.

        :param files: A list of files to process.
        :type files: list
        :param options: Additional parameters for configuring processing.
        :type options: dict
        :raises FileNotFoundError: If a file in the list does not exist.
        :raises TypeError: If the input is not a list of strings.
        :return: A list of processed results.
        :rtype: list
        """
        if not isinstance(files, list):
            raise TypeError("Input 'files' must be a list")
        for file in files:
            if not isinstance(file, str):
                raise TypeError("All elements in the 'files' list must be strings")
            # Simulate processing logic
            try:
                with open(file, 'r') as f:
                    contents = f.read()
                    # Perform some processing on the file contents
                    processed_result = f"Processed {file}: {contents[:20]}"
                    yield processed_result
            except FileNotFoundError as e:
                raise FileNotFoundError(f"File not found: {file}") from e


# Test Cases
def test_process_files_valid_input():
    """Checks correct behavior with a valid list of files."""
    assistant = CodeAssistant(role='code_checker', lang='en', model=['gemini'])
    files = ['file1.txt', 'file2.txt']
    # Create dummy files for testing
    with open('file1.txt', 'w') as f:
        f.write("File one content.")
    with open('file2.txt', 'w') as f:
        f.write("File two content.")
    
    results = list(assistant.process_files(files))
    assert len(results) == 2
    assert results[0].startswith("Processed file1.txt:")
    assert results[1].startswith("Processed file2.txt:")

    # Clean up dummy files
    import os
    os.remove('file1.txt')
    os.remove('file2.txt')



def test_process_files_invalid_input_not_list():
    """Checks if it raises TypeError for non-list input."""
    assistant = CodeAssistant(role='code_checker', lang='en', model=['gemini'])
    with pytest.raises(TypeError) as excinfo:
        list(assistant.process_files("invalid_input"))
    assert "Input 'files' must be a list" in str(excinfo.value)


def test_process_files_invalid_input_not_string():
    """Checks if it raises TypeError if element in list is not a string"""
    assistant = CodeAssistant(role='code_checker', lang='en', model=['gemini'])
    files = [123, "file2.txt"]
    with pytest.raises(TypeError) as excinfo:
        list(assistant.process_files(files))
    assert "All elements in the 'files' list must be strings" in str(excinfo.value)



def test_process_files_file_not_found():
    """Checks correct handling of file not found."""
    assistant = CodeAssistant(role='code_checker', lang='en', model=['gemini'])
    files = ['nonexistent_file.txt']
    with pytest.raises(FileNotFoundError) as excinfo:
        list(assistant.process_files(files))
    assert "File not found" in str(excinfo.value.args[0])
```