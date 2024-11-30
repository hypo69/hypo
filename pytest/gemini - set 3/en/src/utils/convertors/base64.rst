```python
import pytest
import base64
import tempfile
import os
from hypotez.src.utils.convertors.base64 import base64_to_tmpfile

def test_base64_to_tmpfile_valid_input():
    """Tests base64_to_tmpfile with valid input."""
    base64_content = base64.b64encode(b"Hello world!").decode('utf-8')
    file_name = "example.txt"
    tmp_file_path = base64_to_tmpfile(base64_content, file_name)
    assert os.path.exists(tmp_file_path)
    with open(tmp_file_path, "r") as f:
        assert f.read() == ""  # empty since no text data was encoded
    os.remove(tmp_file_path)  # Clean up

def test_base64_to_tmpfile_valid_input_with_extension():
    """Tests base64_to_tmpfile with valid input and extension."""
    base64_content = base64.b64encode(b"image content").decode('utf-8')
    file_name = "image.png"
    tmp_file_path = base64_to_tmpfile(base64_content, file_name)
    assert os.path.exists(tmp_file_path)
    assert tmp_file_path.endswith(".png")
    os.remove(tmp_file_path)

def test_base64_to_tmpfile_invalid_base64():
    """Tests base64_to_tmpfile with invalid Base64 input."""
    invalid_base64 = "invalid_base64"
    file_name = "example.txt"
    with pytest.raises(base64.binascii.Error):
        base64_to_tmpfile(invalid_base64, file_name)


def test_base64_to_tmpfile_empty_content():
    """Tests base64_to_tmpfile with empty content."""
    base64_content = ""
    file_name = "example.txt"
    tmp_file_path = base64_to_tmpfile(base64_content, file_name)
    assert os.path.exists(tmp_file_path)
    with open(tmp_file_path, "rb") as f:
        assert f.read() == b""  # Correctly handles empty content
    os.remove(tmp_file_path)

def test_base64_to_tmpfile_no_extension():
    """Tests base64_to_tmpfile with a file name without extension."""
    base64_content = base64.b64encode(b"some data").decode('utf-8')
    file_name = "example"
    tmp_file_path = base64_to_tmpfile(base64_content, file_name)
    assert os.path.exists(tmp_file_path)
    assert tmp_file_path.endswith(".txt")
    os.remove(tmp_file_path)

def test_base64_to_tmpfile_non_string_content():
    """Tests base64_to_tmpfile with non-string content."""
    base64_content = b"test_base64"
    file_name = "file.bin"
    with pytest.raises(TypeError):
      base64_to_tmpfile(base64_content, file_name)

def test_base64_to_tmpfile_file_name_invalid():
  """Tests for invalid file_name."""
  base64_content = base64.b64encode(b"some data").decode('utf-8')
  file_name = "file/name/with/slashs"
  with pytest.raises(TypeError):
    base64_to_tmpfile(base64_content, file_name)
```