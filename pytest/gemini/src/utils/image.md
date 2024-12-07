```python
import pytest
import asyncio
import aiohttp
import aiofiles
from pathlib import Path
from unittest.mock import patch

from hypotez.src.utils.image import save_png_from_url, save_png, get_image_data


# Fixture for creating temporary files and directories
@pytest.fixture
def temp_file(tmpdir):
    filename = "test_image.png"
    filepath = tmpdir.join(filename)
    with open(filepath, "wb") as f:
        f.write(b"test image data")
    return filepath


@pytest.fixture
def test_image_url():
    return "https://example.com/image.png"

@pytest.fixture
def dummy_image_data():
    return b"test image data"

# Test cases for save_png_from_url
def test_save_png_from_url_valid(test_image_url, tmpdir):
    """Test saving a valid image from a URL."""
    filename = tmpdir.join("downloaded_image.png")
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(
        save_png_from_url(test_image_url, filename)
    )
    assert result == str(filename)
    assert filename.exists()

@pytest.mark.asyncio
async def test_save_png_from_url_invalid_url(tmpdir):
    """Tests saving an image from an invalid URL."""
    filename = tmpdir.join("invalid_image.png")
    with pytest.raises(aiohttp.ClientError):
        await save_png_from_url("invalid_url", filename)


@pytest.mark.asyncio
async def test_save_png_from_url_io_error(mocker, tmpdir):
    """Tests saving an image with an IO error."""
    mocker.patch("aiohttp.ClientSession.get", side_effect=aiohttp.ClientError("Network error"))
    filename = tmpdir.join("failed_image.png")
    result = await save_png_from_url("https://example.com/image.png", filename)
    assert result is None



# Test cases for save_png
def test_save_png_valid(temp_file, tmpdir):
    """Test saving a valid image."""
    new_filename = tmpdir.join("saved_image.png")
    loop = asyncio.get_event_loop()
    with open(temp_file, "rb") as f:
        image_data = f.read()
    result = loop.run_until_complete(save_png(image_data, new_filename))
    assert result == str(new_filename)
    assert new_filename.exists()

def test_save_png_invalid_image_data(tmpdir):
    """Tests saving an image with invalid image data."""
    new_filename = tmpdir.join("invalid_image.png")
    with pytest.raises(IOError, match="not a valid PNG image"):
        asyncio.run(save_png(b"", new_filename))


@pytest.mark.asyncio
async def test_save_png_io_error(mocker, tmpdir):
    """Tests saving an image with an IO error."""
    mocker.patch("aiofiles.open", side_effect=IOError("File operation failed"))
    filename = tmpdir.join("failed_image.png")
    with open(filename, "wb") as f:
        f.write(b"test")
    result = await save_png(b"test image data", filename)
    assert result is None


# Test cases for get_image_data
def test_get_image_data_valid(temp_file):
    """Test retrieving valid image data."""
    data = get_image_data(temp_file)
    assert data is not None
    assert len(data) > 0

def test_get_image_data_nonexistent_file(tmpdir):
    """Test retrieving data from a non-existent file."""
    filename = tmpdir.join("missing_image.png")
    data = get_image_data(filename)
    assert data is None

def test_get_image_data_file_read_error(temp_file, mocker):
    """Tests retrieving data with an IOError."""
    mocker.patch("builtins.open", side_effect=IOError("File operation failed"))
    data = get_image_data(temp_file)
    assert data is None
```