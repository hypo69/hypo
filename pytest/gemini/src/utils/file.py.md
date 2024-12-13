```python
import pytest
import os
import tempfile
from pathlib import Path
from unittest.mock import patch
from src.utils.file import (
    save_text_file,
    read_text_file,
    get_filenames,
    recursively_yield_file_path,
    recursively_get_file_path,
    recursively_read_text_files,
    get_directory_names,
    read_files_content,
    remove_bom,
    traverse_and_clean,
)
from src.logger.logger import logger  # Assuming logger is set up correctly


@pytest.fixture
def temp_dir():
    """Creates a temporary directory for testing."""
    with tempfile.TemporaryDirectory() as tmp_dir:
        yield Path(tmp_dir)


@pytest.fixture
def sample_files(temp_dir):
    """Creates sample files in the temporary directory."""
    (temp_dir / "test1.txt").write_text("test content 1")
    (temp_dir / "test2.txt").write_text("test content 2\nline2")
    (temp_dir / "test3.md").write_text("# Markdown content")
    (temp_dir / "subdir").mkdir()
    (temp_dir / "subdir" / "test4.txt").write_text("test content 4")
    (temp_dir / "subdir" / "test5.py").write_text("print('hello')")
    return temp_dir


# Tests for save_text_file
def test_save_text_file_valid_string(temp_dir):
    """Checks saving a string to a file."""
    file_path = temp_dir / "test_string.txt"
    assert save_text_file("test string data", file_path)
    assert file_path.read_text() == "test string data"


def test_save_text_file_valid_list(temp_dir):
    """Checks saving a list of strings to a file."""
    file_path = temp_dir / "test_list.txt"
    data = ["line1", "line2", "line3"]
    assert save_text_file(data, file_path)
    assert file_path.read_text() == "line1\nline2\nline3\n"


def test_save_text_file_valid_dict(temp_dir):
    """Checks saving a dictionary to a file."""
    file_path = temp_dir / "test_dict.json"
    data = {"key1": "value1", "key2": 2}
    assert save_text_file(data, file_path)
    loaded_data = json.loads(file_path.read_text())
    assert loaded_data == data

def test_save_text_file_invalid_path(temp_dir, caplog):
     """Checks handling of an invalid file path and logging."""
     file_path = temp_dir / "non_existent_dir" / "test_string.txt"
     assert not save_text_file("test string data", file_path)
     assert "Failed to save file" in caplog.text

def test_save_text_file_append_mode(temp_dir):
    """Checks appending to an existing file."""
    file_path = temp_dir / "test_append.txt"
    file_path.write_text("initial content")
    assert save_text_file(" appended content", file_path, mode="a")
    assert file_path.read_text() == "initial content appended content"


def test_save_text_file_exception_handling(temp_dir, caplog):
    """Checks exception handling during file saving."""
    with patch("pathlib.Path.open", side_effect=IOError("Test Error")):
        file_path = temp_dir / "test_error.txt"
        assert not save_text_file("test", file_path)
        assert "Failed to save file" in caplog.text


# Tests for read_text_file
def test_read_text_file_file_as_string(sample_files):
    """Checks reading a file as a string."""
    file_path = sample_files / "test1.txt"
    content = read_text_file(file_path)
    assert content == "test content 1"


def test_read_text_file_file_as_list(sample_files):
    """Checks reading a file as a list of lines."""
    file_path = sample_files / "test2.txt"
    content = read_text_file(file_path, as_list=True)
    assert content == ["test content 2\n", "line2"]


def test_read_text_file_directory_as_string(sample_files):
    """Checks reading a directory as a string."""
    dir_path = sample_files
    content = read_text_file(dir_path)
    assert "test content 1" in content
    assert "test content 2\nline2" in content
    assert "# Markdown content" in content
    assert "test content 4" in content
    assert "print('hello')" not in content


def test_read_text_file_directory_as_list(sample_files):
    """Checks reading a directory as a list of lines."""
    dir_path = sample_files
    content = read_text_file(dir_path, as_list=True)
    assert "test content 1" in content
    assert "test content 2\n" in content
    assert "line2" in content
    assert "# Markdown content" in content
    assert "test content 4" in content


def test_read_text_file_directory_with_extensions(sample_files):
    """Checks reading a directory with specified extensions."""
    dir_path = sample_files
    content = read_text_file(dir_path, extensions=[".txt"], as_list=True)
    assert len(content) == 3
    assert  "test content 1" in content
    assert "test content 2\n" in content
    assert "line2" in content
    assert "test content 4" in content


def test_read_text_file_invalid_path(temp_dir, caplog):
    """Checks handling of an invalid file path."""
    file_path = temp_dir / "non_existent.txt"
    assert read_text_file(file_path) is None
    assert "Path" in caplog.text

def test_read_text_file_exception_handling(temp_dir, caplog):
    """Checks exception handling during file reading."""
    file_path = temp_dir / "test_exception.txt"
    file_path.write_text("content")
    with patch("pathlib.Path.open", side_effect=IOError("Test Error")):
         assert read_text_file(file_path) is None
         assert "Failed to read file" in caplog.text


# Tests for get_filenames
def test_get_filenames_no_filter(sample_files):
    """Checks getting all filenames in a directory."""
    files = get_filenames(sample_files)
    assert len(files) == 3
    assert "test1.txt" in files
    assert "test2.txt" in files
    assert "test3.md" in files

def test_get_filenames_with_filter(sample_files):
    """Checks getting filenames filtered by extensions."""
    files = get_filenames(sample_files, extensions=".txt")
    assert len(files) == 2
    assert "test1.txt" in files
    assert "test2.txt" in files
    assert "test3.md" not in files

def test_get_filenames_invalid_directory(temp_dir, caplog):
    """Checks handling of an invalid directory."""
    directory = temp_dir / "non_existent_dir"
    files = get_filenames(directory)
    assert not files
    assert "Failed to list filenames" in caplog.text

def test_get_filenames_exception_handling(temp_dir, caplog):
    """Checks exception handling during get filenames."""
    with patch("pathlib.Path.iterdir", side_effect=IOError("Test Error")):
        directory = temp_dir
        assert not get_filenames(directory)
        assert "Failed to list filenames" in caplog.text


# Tests for recursively_yield_file_path
def test_recursively_yield_file_path_single_pattern(sample_files):
    """Checks yielding file paths recursively with a single pattern."""
    paths = list(recursively_yield_file_path(sample_files, "*.txt"))
    assert len(paths) == 3
    assert any(path.name == "test1.txt" for path in paths)
    assert any(path.name == "test2.txt" for path in paths)
    assert any(path.name == "test4.txt" for path in paths)


def test_recursively_yield_file_path_multiple_patterns(sample_files):
    """Checks yielding file paths recursively with multiple patterns."""
    patterns = ["*.txt", "*.md"]
    paths = list(recursively_yield_file_path(sample_files, patterns))
    assert len(paths) == 4
    assert any(path.name == "test1.txt" for path in paths)
    assert any(path.name == "test2.txt" for path in paths)
    assert any(path.name == "test3.md" for path in paths)
    assert any(path.name == "test4.txt" for path in paths)

def test_recursively_yield_file_path_exception_handling(temp_dir, caplog):
    """Checks exception handling during yielding file paths."""
    with patch("pathlib.Path.rglob", side_effect=IOError("Test Error")):
        root_dir = temp_dir
        paths = list(recursively_yield_file_path(root_dir, "*.txt"))
        assert not paths
        assert "Failed to search files" in caplog.text


# Tests for recursively_get_file_path
def test_recursively_get_file_path_single_pattern(sample_files):
    """Checks getting file paths recursively with a single pattern."""
    paths = recursively_get_file_path(sample_files, "*.txt")
    assert len(paths) == 3
    assert any(path.name == "test1.txt" for path in paths)
    assert any(path.name == "test2.txt" for path in paths)
    assert any(path.name == "test4.txt" for path in paths)

def test_recursively_get_file_path_multiple_patterns(sample_files):
     """Checks getting file paths recursively with multiple patterns."""
     patterns = ["*.txt", "*.md"]
     paths = recursively_get_file_path(sample_files, patterns)
     assert len(paths) == 4
     assert any(path.name == "test1.txt" for path in paths)
     assert any(path.name == "test2.txt" for path in paths)
     assert any(path.name == "test3.md" for path in paths)
     assert any(path.name == "test4.txt" for path in paths)


def test_recursively_get_file_path_exception_handling(temp_dir, caplog):
    """Checks exception handling during getting file paths."""
    with patch("pathlib.Path.rglob", side_effect=IOError("Test Error")):
        root_dir = temp_dir
        paths = recursively_get_file_path(root_dir, "*.txt")
        assert not paths
        assert "Failed to search files" in caplog.text

# Tests for recursively_read_text_files
def test_recursively_read_text_files_single_pattern(sample_files):
    """Checks reading text files recursively with a single pattern."""
    contents = recursively_read_text_files(sample_files, "*.txt")
    assert len(contents) == 3
    assert "test content 1" in contents
    assert "test content 2\nline2" in contents
    assert "test content 4" in contents


def test_recursively_read_text_files_multiple_patterns(sample_files):
    """Checks reading text files recursively with multiple patterns."""
    contents = recursively_read_text_files(sample_files, ["*.txt", "*.md"])
    assert len(contents) == 4
    assert "test content 1" in contents
    assert "test content 2\nline2" in contents
    assert "# Markdown content" in contents
    assert "test content 4" in contents

def test_recursively_read_text_files_as_list(sample_files):
    """Checks reading text files recursively as a list of lines."""
    contents = recursively_read_text_files(sample_files, "*.txt", as_list=True)
    assert "test content 1" in contents
    assert "test content 2\n" in contents
    assert "line2" in contents
    assert "test content 4" in contents


def test_recursively_read_text_files_invalid_dir(temp_dir, caplog):
    """Checks behavior with an invalid root directory."""
    root_dir = temp_dir / "non_existent"
    contents = recursively_read_text_files(root_dir, "*.txt")
    assert not contents
    assert "does not exist or is not a directory." in caplog.text

def test_recursively_read_text_files_exception_handling(sample_files, caplog):
    """Checks exception handling during recursive file reading."""
    with patch("pathlib.Path.open", side_effect=IOError("Test Error")):
        contents = recursively_read_text_files(sample_files, "*.txt")
        assert not contents
        assert "Failed to read file" in caplog.text

# Tests for get_directory_names
def test_get_directory_names_valid_directory(sample_files):
    """Checks retrieving directory names from a valid directory."""
    dir_names = get_directory_names(sample_files)
    assert len(dir_names) == 1
    assert "subdir" in dir_names


def test_get_directory_names_invalid_directory(temp_dir, caplog):
    """Checks handling of an invalid directory."""
    directory = temp_dir / "non_existent_dir"
    dir_names = get_directory_names(directory)
    assert not dir_names
    assert "Failed to get directory names" in caplog.text


def test_get_directory_names_exception_handling(temp_dir, caplog):
    """Checks exception handling during getting directory names."""
    with patch("pathlib.Path.iterdir", side_effect=IOError("Test Error")):
         directory = temp_dir
         dir_names = get_directory_names(directory)
         assert not dir_names
         assert "Failed to get directory names" in caplog.text


# Tests for read_files_content
def test_read_files_content_single_pattern(sample_files):
    """Checks reading file contents with a single pattern."""
    contents = read_files_content(sample_files, "*.txt")
    assert len(contents) == 3
    assert "test content 1" in contents
    assert "test content 2\nline2" in contents
    assert "test content 4" in contents


def test_read_files_content_multiple_patterns(sample_files):
    """Checks reading file contents with multiple patterns."""
    contents = read_files_content(sample_files, ["*.txt", "*.md"])
    assert len(contents) == 4
    assert "test content 1" in contents
    assert "test content 2\nline2" in contents
    assert "# Markdown content" in contents
    assert "test content 4" in contents

def test_read_files_content_as_list(sample_files):
    """Checks reading file content with as_list option."""
    contents = read_files_content(sample_files, "*.txt", as_list=True)
    assert  "test content 1" in contents
    assert "test content 2\n" in contents
    assert "line2" in contents
    assert "test content 4" in contents


def test_read_files_content_empty_result(temp_dir):
    """Checks the behavior when no files match patterns."""
    contents = read_files_content(temp_dir, "*.nonexistent")
    assert not contents

def test_read_files_content_exception_handling(sample_files, caplog):
    """Checks exception handling during reading file content."""
    with patch("src.utils.file.read_text_file", side_effect=IOError("Test Error")):
        contents = read_files_content(sample_files, "*.txt")
        assert not contents
        assert "Failed to read file" in caplog.text


# Tests for remove_bom
def test_remove_bom_with_bom(temp_dir):
    """Checks removing BOM from a file."""
    file_path = temp_dir / "test_bom.txt"
    file_path.write_text("\ufefftest content")
    remove_bom(file_path)
    assert file_path.read_text() == "test content"

def test_remove_bom_no_bom(temp_dir):
    """Checks removing BOM from a file without BOM."""
    file_path = temp_dir / "test_no_bom.txt"
    file_path.write_text("test content")
    remove_bom(file_path)
    assert file_path.read_text() == "test content"

def test_remove_bom_exception_handling(temp_dir, caplog):
    """Checks exception handling during removing BOM."""
    file_path = temp_dir / "test_error.txt"
    file_path.write_text("content")
    with patch("pathlib.Path.open", side_effect=IOError("Test Error")):
        remove_bom(file_path)
        assert "Failed to remove BOM" in caplog.text

# Tests for traverse_and_clean
def test_traverse_and_clean_with_bom(sample_files):
    """Checks traversing and cleaning BOM from Python files."""
    py_file = sample_files / "subdir" / "test5.py"
    py_file.write_text("\ufeffprint('hello')")
    traverse_and_clean(sample_files)
    assert py_file.read_text() == "print('hello')"

def test_traverse_and_clean_no_py_files(sample_files):
    """Checks traversing and cleaning when no Python files are present."""
    traverse_and_clean(sample_files)
    assert (sample_files / "test1.txt").read_text() == "test content 1"
    assert (sample_files / "test2.txt").read_text() == "test content 2\nline2"
    assert (sample_files / "test3.md").read_text() == "# Markdown content"

def test_traverse_and_clean_exception_handling(sample_files, caplog):
    """Checks exception handling during traverse and clean."""
    with patch("src.utils.file.remove_bom", side_effect=IOError("Test Error")):
         traverse_and_clean(sample_files)
         assert "Failed to remove BOM" in caplog.text
```