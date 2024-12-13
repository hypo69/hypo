```python
import pytest
import os
import base64
from hypotez.src.utils.convertors.base64 import base64_to_tmpfile, base64encode


@pytest.fixture
def example_base64_content():
    """Provides example base64 encoded content."""
    return "SGVsbG8gV29ybGQh"  # Base64 for "Hello World!"

@pytest.fixture
def example_file_name():
    """Provides example file name with an extension."""
    return "example.txt"

@pytest.fixture
def example_image_path(tmp_path):
    """Provides an example image file path."""
    image_path = tmp_path / "test_image.jpg"
    with open(image_path, "wb") as f:
        f.write(b"test image data")
    return str(image_path)



def test_base64_to_tmpfile_valid_input(example_base64_content, example_file_name):
    """Checks if a temporary file is correctly created from valid base64 input."""
    tmp_file_path = base64_to_tmpfile(example_base64_content, example_file_name)
    assert os.path.exists(tmp_file_path)
    
    # check file content
    with open(tmp_file_path, "rb") as f:
      content = f.read()
      assert content == base64.b64decode(example_base64_content)

    os.remove(tmp_file_path) #clean up the tmp file

def test_base64_to_tmpfile_empty_content(example_file_name):
    """Checks if the function works with empty base64 content."""
    tmp_file_path = base64_to_tmpfile("", example_file_name)
    assert os.path.exists(tmp_file_path)
    with open(tmp_file_path, "rb") as f:
      content = f.read()
      assert content == b""
    os.remove(tmp_file_path)


def test_base64_to_tmpfile_file_name_without_extension(example_base64_content):
    """Checks if the function handles file names without an extension."""
    file_name = "example"
    tmp_file_path = base64_to_tmpfile(example_base64_content, file_name)
    assert os.path.exists(tmp_file_path)
    os.remove(tmp_file_path)


def test_base64_to_tmpfile_file_name_with_multiple_dots(example_base64_content):
    """Checks if the function correctly extracts the extension with multiple dots in the filename."""
    file_name = "example.test.txt"
    tmp_file_path = base64_to_tmpfile(example_base64_content, file_name)
    assert os.path.exists(tmp_file_path)
    assert tmp_file_path.endswith(".txt")
    os.remove(tmp_file_path)
    

def test_base64_to_tmpfile_invalid_base64_content(example_file_name):
    """Checks if the function raises exception with invalid base64 string."""
    invalid_base64_content = "This is not a base64 string"
    with pytest.raises(Exception):
        base64_to_tmpfile(invalid_base64_content, example_file_name)


def test_base64encode_valid_image(example_image_path):
    """Checks if an image is correctly encoded to base64."""
    encoded_content = base64encode(example_image_path)
    assert isinstance(encoded_content, str)
    assert len(encoded_content) > 0

def test_base64encode_nonexistent_image():
    """Checks if an exception is raised when an image does not exists"""
    non_existent_path = "nonexistent.jpg"
    with pytest.raises(FileNotFoundError):
        base64encode(non_existent_path)

def test_base64encode_empty_image(tmp_path):
    """Checks if the function works with an empty image file."""
    empty_file_path = tmp_path / "empty.txt"
    open(empty_file_path, "w").close() #create empty file
    encoded_content = base64encode(str(empty_file_path))
    assert isinstance(encoded_content, str)
    assert len(encoded_content) > 0 # empty file still creates a base64 string.
```