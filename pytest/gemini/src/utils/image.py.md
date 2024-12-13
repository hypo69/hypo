```python
import pytest
import asyncio
import os
from pathlib import Path
from unittest.mock import patch
from PIL import Image
from hypotez.src.utils.image import save_png_from_url, save_png, get_image_data, random_image
from hypotez.src.logger.logger import logger

# Mock the logger to avoid logging during tests
@pytest.fixture(autouse=True)
def mock_logger():
    with patch.object(logger, "error") as mock_error, \
         patch.object(logger, "warning") as mock_warning, \
         patch.object(logger, "critical") as mock_critical:
        yield mock_error, mock_warning, mock_critical

# Fixture for creating a temporary directory
@pytest.fixture
def temp_dir(tmp_path):
    """Provides a temporary directory for tests."""
    yield tmp_path

# Fixture to create a sample image file for testing
@pytest.fixture
def sample_image(temp_dir):
    """Creates a sample image file for testing."""
    image_path = temp_dir / "test_image.png"
    Image.new("RGB", (60, 30), color="red").save(image_path)
    return image_path

# Fixture for sample image data
@pytest.fixture
def sample_image_data(sample_image):
    """Provides sample binary image data."""
    with open(sample_image, "rb") as f:
        return f.read()

# Fixture for creating multiple sample image files for random_image test
@pytest.fixture
def sample_image_files(temp_dir):
    """Creates multiple sample image files for testing random_image function."""
    image_paths = []
    for i in range(3):
        image_path = temp_dir / f"test_image_{i}.png"
        Image.new("RGB", (60, 30), color="red").save(image_path)
        image_paths.append(image_path)
    # Create a subdirectory and image in the subdirectoy
    sub_dir_path = temp_dir / "subdir"
    sub_dir_path.mkdir(exist_ok=True)
    sub_image_path = sub_dir_path / "sub_image.jpg"
    Image.new("RGB", (60, 30), color="blue").save(sub_image_path)
    image_paths.append(sub_image_path)
    return image_paths

@pytest.mark.asyncio
async def test_save_png_from_url_valid_url(temp_dir, mock_logger):
    """Checks correct behavior with a valid URL."""
    test_url = "https://via.placeholder.com/150"
    filename = temp_dir / "test_downloaded_image.png"
    result = await save_png_from_url(test_url, filename)
    assert result is not None
    assert Path(result).exists()
    assert Path(result).stat().st_size > 0
    assert mock_logger[0].call_count == 0 # no errors
    
@pytest.mark.asyncio
async def test_save_png_from_url_invalid_url(temp_dir, mock_logger):
    """Checks correct handling of an invalid URL."""
    test_url = "https://invalid-url.com/image.png"
    filename = temp_dir / "test_invalid_url.png"
    result = await save_png_from_url(test_url, filename)
    assert result is None
    assert not filename.exists()
    assert mock_logger[0].call_count == 1  # Check if logger.error was called

@pytest.mark.asyncio
async def test_save_png_valid_data(temp_dir, sample_image_data, mock_logger):
    """Checks correct behavior with valid image data."""
    filename = temp_dir / "test_saved_image.png"
    result = await save_png(sample_image_data, filename)
    assert result is not None
    assert Path(result).exists()
    assert Path(result).stat().st_size > 0
    assert mock_logger[0].call_count == 0 # no errors

@pytest.mark.asyncio
async def test_save_png_empty_data(temp_dir, mock_logger):
    """Checks behavior with empty image data."""
    filename = temp_dir / "test_empty_image.png"
    result = await save_png(b"", filename)
    assert result is None
    assert not filename.exists()
    assert mock_logger[0].call_count == 1 # Check if logger.error was called


@pytest.mark.asyncio
async def test_save_png_invalid_filename(temp_dir, sample_image_data, mock_logger):
    """Checks handling of invalid filename."""
    filename = temp_dir / "invalid/path/test_image.png" # should not exist
    result = await save_png(sample_image_data, filename)
    assert result is not None
    assert Path(result).exists()
    assert mock_logger[0].call_count == 0  # check that there were no error logging

def test_get_image_data_existing_file(sample_image, mock_logger):
    """Checks correct behavior with an existing file."""
    result = get_image_data(sample_image)
    assert result is not None
    assert isinstance(result, bytes)
    assert len(result) > 0
    assert mock_logger[0].call_count == 0 # no errors

def test_get_image_data_non_existing_file(temp_dir, mock_logger):
    """Checks handling of a non-existing file."""
    file_path = temp_dir / "non_existing_file.png"
    result = get_image_data(file_path)
    assert result is None
    assert mock_logger[0].call_count == 1 # Check if logger.error was called

def test_get_image_data_invalid_file_path(temp_dir, mock_logger):
    """Checks correct handling of invalid file path."""
    file_path = temp_dir / "invalid/path/file.png"  # should not exist
    result = get_image_data(file_path)
    assert result is None
    assert mock_logger[0].call_count == 1 # Check if logger.error was called

def test_random_image_with_images(sample_image_files, mock_logger):
    """Checks correct behavior with images in directory."""
    root_path = sample_image_files[0].parent # using the parent dir for search
    result = random_image(root_path)
    assert result is not None
    assert isinstance(result, str)
    assert Path(result).exists()
    assert mock_logger[1].call_count == 0  # no warnings

def test_random_image_no_images(temp_dir, mock_logger):
    """Checks behavior when no images are present."""
    result = random_image(temp_dir)
    assert result is None
    assert mock_logger[1].call_count == 1  # Check if logger.warning was called

def test_random_image_invalid_root_path(mock_logger):
    """Checks handling of invalid root path."""
    invalid_path = "/invalid/path/"
    result = random_image(invalid_path)
    assert result is None
    assert mock_logger[1].call_count == 1 # Check if logger.warning was called

def test_random_image_empty_root_path(mock_logger):
    """Checks handling of empty root path."""
    empty_path = ""
    result = random_image(empty_path)
    assert result is None
    assert mock_logger[1].call_count == 1 # Check if logger.warning was called
```