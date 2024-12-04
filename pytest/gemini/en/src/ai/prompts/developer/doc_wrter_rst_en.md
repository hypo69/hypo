```python
import pytest

# Example Code (replace with your actual code)
class CodeAssistant:
    """
    Class for interacting with AI models for code processing tasks.

    :param role: The role of the assistant (e.g., 'code_checker').
    :type role: str
    :param lang: The language the assistant will use (e.g., 'ru').
    :type lang: str
    :param model: List of AI models used (e.g., ['gemini']).
    :type model: list
    """
    def __init__(self, role, lang, model):
        """
        Initializes the CodeAssistant with specified parameters.

        :param role: The role of the assistant.
        :param lang: The language to use.
        :param model: A list of AI models.
        """
        self.role = role
        self.lang = lang
        self.model = model

    def process_files(self, files, options={}):
        """
        Processes a list of files.

        :param files: A list of files to process.
        :type files: list
        :param options: Optional parameters for processing.
        :type options: dict
        :raises FileNotFoundError: If a file in the list is not found.
        :return: A list of processing results.
        :rtype: list
        """
        results = []
        for file in files:
            try:
                # Simulate processing a file
                result = f"Processed {file}"
                results.append(result)
            except FileNotFoundError as ex:
                raise FileNotFoundError(f"File not found: {file}") from ex
        return results

# Fixtures (if needed)
@pytest.fixture
def assistant_instance():
    """Provides a CodeAssistant instance for tests."""
    return CodeAssistant(role='code_checker', lang='en', model=['gemini'])

@pytest.fixture
def test_files():
    """Provides test files for the process_files method."""
    return ['file1.py', 'file2.py']

# Tests
def test_process_files_valid_input(assistant_instance, test_files):
    """Checks correct behavior with a valid list of files."""
    results = assistant_instance.process_files(files=test_files)
    assert len(results) == len(test_files)
    for result in results:
        assert isinstance(result, str)


def test_process_files_empty_input(assistant_instance):
    """Tests process_files with an empty file list."""
    results = assistant_instance.process_files(files=[])
    assert results == []

def test_process_files_invalid_file(assistant_instance, test_files):
    """Tests handling of a non-existent file."""
    with pytest.raises(FileNotFoundError, match="File not found: non_existent_file.py"):
        assistant_instance.process_files(files=test_files + ['non_existent_file.py'])
```