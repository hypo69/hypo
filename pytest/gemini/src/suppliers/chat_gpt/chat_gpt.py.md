```python
import pytest
from pathlib import Path
from unittest.mock import patch, mock_open
from src.suppliers.chat_gpt.chat_gpt import ChatGpt
from src import gs

# Mocking gs.path.data for consistent test environment
@pytest.fixture(autouse=True)
def mock_gs_path_data(monkeypatch):
    """Mocks gs.path.data for consistent test environment."""
    monkeypatch.setattr(gs.path, 'data', Path("/test_data"))

# Mocking file system interaction
@pytest.fixture
def mock_glob(monkeypatch):
    """Mocks Path.glob for predictable test results."""
    def mock_glob_impl(pattern):
        if pattern == "*.html":
          return [Path("/test_data/chat_gpt/conversations/file1.html"),
                 Path("/test_data/chat_gpt/conversations/file2.html")]
        return []
    monkeypatch.setattr(Path, 'glob', mock_glob_impl)


def test_yeld_conversations_htmls_valid_files(mock_glob):
    """
    Test that yeld_conversations_htmls returns a generator of file paths when HTML files are found.
    """
    chat_gpt = ChatGpt()
    result = chat_gpt.yeld_conversations_htmls()
    expected_paths = [Path("/test_data/chat_gpt/conversations/file1.html"),
                      Path("/test_data/chat_gpt/conversations/file2.html")]

    assert list(result) == expected_paths

def test_yeld_conversations_htmls_no_files(monkeypatch):
    """
    Test that yeld_conversations_htmls returns an empty generator when no HTML files are found.
    """
    def mock_glob_no_files(pattern):
      return []
    monkeypatch.setattr(Path, 'glob', mock_glob_no_files)
    chat_gpt = ChatGpt()
    result = chat_gpt.yeld_conversations_htmls()
    assert list(result) == []


def test_yeld_conversations_htmls_wrong_directory(monkeypatch):
  """
  Test that yeld_conversations_htmls returns an empty list if the directory doesn't exist.
  """
  def mock_glob_wrong_dir(pattern):
    return []
  monkeypatch.setattr(Path, 'glob', mock_glob_wrong_dir)
  chat_gpt = ChatGpt()
  result = chat_gpt.yeld_conversations_htmls()
  assert list(result) == []


def test_yeld_conversations_htmls_empty_directory(monkeypatch):
  """
    Test that yeld_conversations_htmls returns an empty list if the directory is empty.
  """
  def mock_glob_empty_dir(pattern):
    return []
  monkeypatch.setattr(Path, 'glob', mock_glob_empty_dir)
  chat_gpt = ChatGpt()
  result = chat_gpt.yeld_conversations_htmls()
  assert list(result) == []
```