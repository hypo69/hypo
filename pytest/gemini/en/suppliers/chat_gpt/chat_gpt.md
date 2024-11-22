```python
import pytest
import os
from pathlib import Path
from unittest.mock import patch

from src import gs
from src.suppliers.chat_gpt.chat_gpt import ChatGpt


# Replace with a dummy implementation if 'gs' module is not available
class DummyGs:
    path = Path("./dummy_data")


@pytest.fixture
def chatgpt_instance():
    """Creates an instance of ChatGpt."""
    return ChatGpt()


@pytest.fixture
def dummy_gs():
    """Mocked gs object for testing."""
    gs.path = DummyGs().path
    return gs


def test_yeld_conversations_htmls_valid_input(dummy_gs):
    """
    Checks correct behavior with a valid directory containing HTML files.
    """
    # Create dummy data directory and files.
    dummy_data_dir = dummy_gs.path.data / 'chat_gpt' / 'conversations'
    os.makedirs(dummy_data_dir, exist_ok=True)
    (dummy_data_dir / 'conversation1.html').touch()
    (dummy_data_dir / 'conversation2.html').touch()

    chatgpt = ChatGpt()
    html_files = list(chatgpt.yeld_conversations_htmls())

    assert len(html_files) == 2
    assert isinstance(html_files[0], Path)
    assert isinstance(html_files[1], Path)


def test_yeld_conversations_htmls_empty_directory(dummy_gs):
    """Checks behavior when the directory is empty."""
    dummy_data_dir = dummy_gs.path.data / 'chat_gpt' / 'conversations'
    os.makedirs(dummy_data_dir, exist_ok=True)
    chatgpt = ChatGpt()
    html_files = list(chatgpt.yeld_conversations_htmls())
    assert len(html_files) == 0


def test_yeld_conversations_htmls_invalid_directory(dummy_gs):
    """
    Checks behavior when the directory doesn't exist or
    is not a directory. 
    """
    #Simulates an invalid gs.path setup.
    dummy_gs.path.data = Path("invalid_path")


    chatgpt = ChatGpt()
    html_files = list(chatgpt.yeld_conversations_htmls())
    assert len(html_files) == 0



def test_yeld_conversations_htmls_non_html_files(dummy_gs):
    """Checks handling of non-HTML files in the directory."""
    dummy_data_dir = dummy_gs.path.data / 'chat_gpt' / 'conversations'
    os.makedirs(dummy_data_dir, exist_ok=True)
    (dummy_data_dir / 'conversation1.html').touch()
    (dummy_data_dir / 'conversation2.txt').touch()
    chatgpt = ChatGpt()
    html_files = list(chatgpt.yeld_conversations_htmls())
    assert len(html_files) == 1
    assert html_files[0].name == "conversation1.html"
```

**Explanation and Improvements:**

* **Dummy `gs` and Data:**  The code now includes a `DummyGs` class to mock the `gs` module. This is crucial for testing in isolation, preventing dependencies on external resources.  Crucially, it creates temporary dummy data directories and files for tests.

* **`pytest.raises` not needed**: The original code did not have any exception raising to test. No longer needed in the revised tests.

* **Clearer Test Names:** Test names are more descriptive, indicating the input type (valid/empty/invalid directory)

* **Comprehensive Edge Cases:** The tests now cover empty directories and cases where the directory doesn't exist. The crucial test cases (invalid `gs.path` or no html files).

* **`os.makedirs`:** Correctly creates directories to house the temporary data.

* **`assert isinstance(html_files[0], Path)`**:  Verifies that the return value is indeed a `Path` object, ensuring the correct type is returned.


**How to Run the Tests:**

1.  **Install pytest:**
    ```bash
    pip install pytest
    ```

2.  **Save the tests** in a file named, for example, `test_chat_gpt.py`

3.  **Run the tests:**
    ```bash
    pytest test_chat_gpt.py
    ```


Remember to adapt the dummy data directory creation if your `gs` module interacts with a different file path structure. Also, if your `gs` module has a more complex structure for data retrieval, you may need to further adjust the fixture and test logic to properly mock or simulate those interactions.