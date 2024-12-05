```python
import pytest

# Class for working with a code assistant
class CodeAssistant:
    """
    Class for working with various AI models (e.g., Google Gemini, OpenAI)
    for code processing tasks.

    :param role: The role of the assistant (e.g., 'code_checker').
    :param lang: The language the assistant will work with (e.g., 'ru').
    :param model: A list of AI models in use (e.g., ['gemini']).
    """

    def __init__(self, role, lang, model):
        self.role = role
        self.lang = lang
        self.model = model

    def process_files(self, files, options={}):
        """
        Processes a list of files.

        :param files: A list of files to process.
        :param options: Additional parameters for file processing.
        :raises FileNotFoundError: If a file in the list doesn't exist.
        :returns: A list of processed data.  Returns an empty list if no files are provided.
        """
        if not files:
            return []

        results = []
        for file in files:
            try:
                # Simulate processing the file.  Replace with actual processing logic.
                result = f"Processed file: {file}"
                results.append(result)
            except FileNotFoundError as e:
                # Handles the case where a file doesn't exist
                raise FileNotFoundError(f"File '{file}' not found.") from e

        return results


# Test cases for the CodeAssistant class
def test_process_files_valid_input():
    """Tests process_files with a valid list of files."""
    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    files = ['file1.py', 'file2.py']
    results = assistant.process_files(files)
    assert len(results) == 2
    # Check that the expected output has been returned
    for result in results:
        assert result.startswith("Processed file")


def test_process_files_empty_input():
    """Tests process_files with an empty list of files."""
    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    results = assistant.process_files([])
    assert results == []


def test_process_files_invalid_file():
    """Tests process_files with a file that does not exist."""
    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    files = ['nonexistent_file.txt']
    with pytest.raises(FileNotFoundError, match="File 'nonexistent_file.txt' not found."):
        assistant.process_files(files)


def test_process_files_with_options():
    """Tests process_files with additional options."""
    assistant = CodeAssistant(role='code_checker', lang='ru', model=['gemini'])
    files = ['file1.txt']
    options = {'encoding': 'utf-8'}
    results = assistant.process_files(files, options)
    assert results[0].startswith("Processed file")


```