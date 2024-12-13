```python
import pytest
import asyncio
from pathlib import Path
from unittest.mock import patch, mock_open
from src.utils.image import save_png_from_url, save_png, get_image_data, random_image

# Fixture definitions
@pytest.fixture
def mock_async_session():
    """Mocks aiohttp.ClientSession for testing."""
    class MockResponse:
        def __init__(self, content, status):
            self._content = content
            self.status = status
        async def read(self):
            return self._content
        async def __aexit__(self, exc_type, exc, tb):
            pass
        async def __aenter__(self):
            return self
    
    class MockSession:
        async def get(self, url):
            if url == "https://example.com/image.png":
                return MockResponse(b"test image data", 200)
            elif url == "https://error.com/image.png":
                 return MockResponse(b"", 404)
            else:
                raise ValueError("Unexpected URL")
        async def __aexit__(self, exc_type, exc, tb):
            pass
        async def __aenter__(self):
            return self
    return MockSession()


@pytest.fixture
def image_data():
    """Provides test image data as bytes."""
    return b"test image data"

@pytest.fixture
def temp_file_path(tmp_path):
    """Provides a temporary file path for testing."""
    return tmp_path / "test_image.png"


# Tests for save_png_from_url
@pytest.mark.asyncio
async def test_save_png_from_url_valid(mock_async_session, temp_file_path):
    """Checks correct behavior with valid URL."""
    with patch("aiohttp.ClientSession", return_value=mock_async_session):
        result = await save_png_from_url("https://example.com/image.png", temp_file_path)
    assert result == str(temp_file_path)
    assert Path(temp_file_path).exists()
    with open(temp_file_path, "rb") as f:
        assert f.read() == b"test image data"


@pytest.mark.asyncio
async def test_save_png_from_url_invalid_url(mock_async_session, temp_file_path):
    """Checks handling of invalid URL."""
    with patch("aiohttp.ClientSession", return_value=mock_async_session):
         result = await save_png_from_url("https://error.com/image.png", temp_file_path)
    assert result is None
    assert not Path(temp_file_path).exists()


@pytest.mark.asyncio
async def test_save_png_from_url_connection_error(mock_async_session, temp_file_path):
    """Checks handling of connection error."""
    with patch("aiohttp.ClientSession", side_effect=Exception("Connection error")):
        result = await save_png_from_url("https://example.com/image.png", temp_file_path)
    assert result is None
    assert not Path(temp_file_path).exists()


@pytest.mark.asyncio
async def test_save_png_from_url_empty_url(mock_async_session, temp_file_path):
    """Checks handling of empty URL."""
    with patch("aiohttp.ClientSession", return_value=mock_async_session):
      result = await save_png_from_url("", temp_file_path)
    assert result is None
    assert not Path(temp_file_path).exists()


# Tests for save_png
@pytest.mark.asyncio
async def test_save_png_valid(image_data, temp_file_path):
    """Checks correct behavior with valid image data."""
    result = await save_png(image_data, temp_file_path)
    assert result == str(temp_file_path)
    assert Path(temp_file_path).exists()
    with open(temp_file_path, "rb") as f:
        assert f.read() == image_data


@pytest.mark.asyncio
async def test_save_png_empty_data(temp_file_path):
    """Checks handling of empty image data."""
    result = await save_png(b"", temp_file_path)
    assert result == str(temp_file_path) #Expect to create a empty file
    assert Path(temp_file_path).exists()
    with open(temp_file_path, "rb") as f:
        assert f.read() == b""


@pytest.mark.asyncio
async def test_save_png_invalid_filename():
   """Checks handling of invalid file path."""
   with pytest.raises(Exception):
      await save_png(b"test", "/invalid/path/file.png")

# Tests for get_image_data
def test_get_image_data_valid(image_data, temp_file_path):
    """Checks correct behavior with existing file."""
    with open(temp_file_path, "wb") as f:
        f.write(image_data)
    result = get_image_data(temp_file_path)
    assert result == image_data

def test_get_image_data_nonexistent_file(temp_file_path):
    """Checks handling of non-existent file."""
    result = get_image_data(temp_file_path)
    assert result is None


def test_get_image_data_empty_file(temp_file_path):
  """Checks handling of empty file."""
  open(temp_file_path, 'a').close() # Create a empty file
  result = get_image_data(temp_file_path)
  assert result == b""


# Tests for random_image
def test_random_image_valid(tmp_path):
    """Checks correct behavior with a directory containing image files."""
    image_files = [tmp_path / "image1.png", tmp_path / "image2.jpg"]
    for file in image_files:
        file.touch()

    result = random_image(tmp_path)
    assert result in [str(f) for f in image_files]

def test_random_image_no_images(tmp_path):
    """Checks handling of directory with no image files."""
    result = random_image(tmp_path)
    assert result is None

def test_random_image_empty_directory(tmp_path):
  """Checks handling of empty directory."""
  result = random_image(tmp_path)
  assert result is None


def test_random_image_nested_directories(tmp_path):
    """Checks handling of nested directories with images."""
    nested_dir = tmp_path / "nested"
    nested_dir.mkdir()
    image_files = [nested_dir / "image1.png", tmp_path / "image2.jpg"]
    for file in image_files:
      file.touch()
    result = random_image(tmp_path)
    assert result in [str(f) for f in image_files]

def test_random_image_invalid_path():
   """Checks handling of invalid root path"""
   result = random_image("/invalid/path")
   assert result is None
```