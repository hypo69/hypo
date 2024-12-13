```python
import pytest
from unittest.mock import patch, mock_open, MagicMock
from pathlib import Path
from src.utils.file.file import (
    save_text_file,
    read_text_file,
    get_filenames,
    get_directory_names,
)

# Tests for save_text_file function
@patch("src.utils.file.file.Path.open", new_callable=mock_open)
@patch("src.utils.file.file.Path.mkdir")
@patch("src.utils.file.file.logger")
def test_save_text_file(mock_logger, mock_mkdir, mock_file_open):
    """Test saving text to a file with valid input.
    
    Verifies that the file is opened in write mode with correct encoding,
    the content is written, and the directory is created.
    """
    save_text_file("test.txt", "This is a test.")
    mock_file_open.assert_called_once_with("w", encoding="utf-8")
    mock_file_open().write.assert_called_once_with("This is a test.")
    mock_mkdir.assert_called_once()


@patch("src.utils.file.file.Path.open", new_callable=mock_open)
@patch("src.utils.file.file.Path.mkdir")
@patch("src.utils.file.file.logger")
def test_save_text_file_empty_content(mock_logger, mock_mkdir, mock_file_open):
    """Test saving empty text to a file.

    Verifies that an empty string can be written to a file without errors.
    """
    save_text_file("test.txt", "")
    mock_file_open.assert_called_once_with("w", encoding="utf-8")
    mock_file_open().write.assert_called_once_with("")
    mock_mkdir.assert_called_once()


@patch("src.utils.file.file.Path.open", new_callable=mock_open)
@patch("src.utils.file.file.Path.mkdir")
@patch("src.utils.file.file.logger")
def test_save_text_file_different_filename(mock_logger, mock_mkdir, mock_file_open):
     """Test saving text to a file with a different filename.

    Verifies that the filename is correctly used by mocking the open and mkdir call.
     """
     save_text_file("different_test.txt", "Different test content.")
     mock_file_open.assert_called_once_with("w", encoding="utf-8")
     mock_file_open().write.assert_called_once_with("Different test content.")
     mock_mkdir.assert_called_once()

# Tests for read_text_file function
@patch(
    "src.utils.file.file.Path.open", new_callable=mock_open, read_data="This is a test."
)
def test_read_text_file(mock_file_open):
    """Test reading text from a file with valid content.

    Verifies that the file is opened in read mode with correct encoding
    and the content is correctly returned.
    """
    content = read_text_file("test.txt")
    assert content == "This is a test."
    mock_file_open.assert_called_once_with("r", encoding="utf-8")


@patch(
    "src.utils.file.file.Path.open", new_callable=mock_open, read_data=""
)
def test_read_text_file_empty_file(mock_file_open):
    """Test reading from an empty file.

    Verifies that reading an empty file returns an empty string.
    """
    content = read_text_file("empty.txt")
    assert content == ""
    mock_file_open.assert_called_once_with("r", encoding="utf-8")


@patch(
    "src.utils.file.file.Path.open", new_callable=mock_open, read_data="Another content"
)
def test_read_text_file_different_content(mock_file_open):
    """Test reading a file with different content.
    
    Verifies that the returned content matches the content of the mocked file.
    """
    content = read_text_file("another_test.txt")
    assert content == "Another content"
    mock_file_open.assert_called_once_with("r", encoding="utf-8")



# Tests for get_filenames function
def test_get_filenames():
    """Test getting filenames from a directory with multiple files.

    Verifies that the correct list of filenames is returned.
    """
    with patch(
        "src.utils.file.file.Path.iterdir",
        return_value=[Path(f"file{i}.txt") for i in range(1, 3)],
    ):
        filenames = get_filenames(Path("/some/dir"))
        assert filenames == ["file1.txt", "file2.txt"]


def test_get_filenames_empty_directory():
    """Test getting filenames from an empty directory.

    Verifies that an empty list is returned when there are no files.
    """
    with patch(
        "src.utils.file.file.Path.iterdir",
        return_value=[],
    ):
        filenames = get_filenames(Path("/empty/dir"))
        assert filenames == []


def test_get_filenames_with_directories_included():
    """Test getting filenames when the directory contains directories too.

    Verifies that only the filenames are returned, not the directory names
    """
    with patch(
    "src.utils.file.file.Path.iterdir",
    return_value = [Path("file1.txt"), Path("dir1"), Path("file2.txt")]
    ):
        filenames = get_filenames(Path("/some/dir"))
        assert filenames == ["file1.txt", "file2.txt"]

# Tests for get_directory_names function
def test_get_directory_names():
    """Test getting directory names from a path with multiple directories.

    Verifies that the correct list of directory names is returned.
    """
    with patch(
        "src.utils.file.file.Path.iterdir",
        return_value=[Path(f"dir{i}") for i in range(1, 3)],
    ):
        directories = get_directory_names(Path("/some/dir"))
        assert directories == ["dir1", "dir2"]


def test_get_directory_names_empty_directory():
    """Test getting directory names from an empty directory.

    Verifies that an empty list is returned when there are no subdirectories.
    """
    with patch(
        "src.utils.file.file.Path.iterdir",
        return_value=[],
    ):
        directories = get_directory_names(Path("/empty/dir"))
        assert directories == []

def test_get_directory_names_with_files_included():
    """Test getting directory names when there are files inside too.

    Verifies that only directory names are returned and not filenames
    """
    with patch(
        "src.utils.file.file.Path.iterdir",
        return_value = [Path("dir1"), Path("file1.txt"), Path("dir2")]
    ):
        directories = get_directory_names(Path("/some/dir"))
        assert directories == ["dir1", "dir2"]
```