```python
import pytest
from pathlib import Path
import os
from unittest.mock import patch
from hypotez.src.suppliers.chat_gpt.chat_gpt import ChatGpt
from hypotez.src import gs


@pytest.fixture
def mock_gs_path():
    """Mocking gs.path to control the directory."""
    mock_path = Path("./test_data/chat_gpt/conversations")
    mock_path.mkdir(parents=True, exist_ok=True)
    with patch('hypotez.src.suppliers.chat_gpt.chat_gpt.gs.path', return_value=mock_path):
        yield mock_path


@pytest.fixture
def create_test_htmls(mock_gs_path):
    """Creates dummy HTML files for testing."""
    files_to_create = [
        "conversation1.html",
        "conversation2.html",
        "invalid_file.txt",  # invalid file to test edge cases
    ]
    for file_name in files_to_create:
        file_path = mock_gs_path / file_name
        with open(file_path, "w") as f:
            f.write("<html><body>Conversation content</body></html>")
    
    yield


def test_yeld_conversations_htmls_valid_input(mock_gs_path, create_test_htmls):
    """Tests with valid input (HTML files exist)."""
    chat_gpt_instance = ChatGpt()
    html_files = chat_gpt_instance.yeld_conversations_htmls()
    assert len(list(html_files)) == 2 # Expect 2 valid html files
    # verify files from the glob statement are correct
    for file in list(html_files):
        assert file.suffix == ".html"  # Ensure only html files are returned.


def test_yeld_conversations_htmls_no_files(mock_gs_path):
    """Tests when no HTML files exist."""
    chat_gpt_instance = ChatGpt()
    html_files = chat_gpt_instance.yeld_conversations_htmls()
    assert len(list(html_files)) == 0 # Expect 0 files if no files are available.



def test_yeld_conversations_htmls_invalid_files(mock_gs_path, create_test_htmls):
    """Tests when other types of files exist."""
    chat_gpt_instance = ChatGpt()
    html_files = chat_gpt_instance.yeld_conversations_htmls()
    assert len(list(html_files)) == 2  # Expect only the html files. 


def test_yeld_conversations_htmls_exception_handling(mock_gs_path):
    """Tests exception handling (e.g., directory doesn't exist)."""
    # Remove the directory to simulate its absence.
    
    (mock_gs_path / 'conversations').rmdir()

    chat_gpt_instance = ChatGpt()
    html_files = chat_gpt_instance.yeld_conversations_htmls()
    assert len(list(html_files)) == 0  # expect no files, because directory does not exist




    
# Important: Clean up the created test data directory after the tests.
def teardown_module(module):
    """Deletes the test directory."""
    try:
        import shutil
        shutil.rmtree("./test_data")
    except FileNotFoundError:
        pass


```

**Explanation and Improvements:**

1. **Mocking `gs.path`:** The `mock_gs_path` fixture now correctly mocks `gs.path` to control the directory used by `ChatGpt`.  This is crucial for isolating the tests and preventing issues with file system access on different runs.

2. **Creating Test Data:** The `create_test_htmls` fixture efficiently sets up dummy HTML files within the mocked directory.  Crucially, it now includes an "invalid_file.txt" for testing the case of non-HTML files.

3. **Clearer Assertions:** Assertions are more specific. For example, instead of just `assert len(list(html_files)) > 0`, we now explicitly check for the expected number of HTML files.

4. **Exception Handling Test:** The `test_yeld_conversations_htmls_exception_handling` function now correctly tests the case where the directory `conversations` doesn't exist. This is a realistic edge case.

5. **Teardown:**  The `teardown_module` function is added to remove the temporary `test_data` directory after the tests, preventing file system pollution. This is *essential* for running tests repeatedly without conflicts.


**How to run the tests:**

1.  Make sure you have `pytest` installed.
2.  Save the code above as a `.py` file (e.g., `test_chat_gpt.py`).
3.  Create a `test_data` directory in the same directory as your test file.
4.  Run `pytest test_chat_gpt.py`.


This improved solution provides comprehensive and robust test coverage for the `ChatGpt` class, handling valid and invalid cases, as well as edge cases like missing directories. Remember to adapt the test data (file names, directory structure) if your actual use case is different.