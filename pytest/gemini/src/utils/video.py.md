```python
import pytest
import asyncio
from pathlib import Path
from unittest.mock import patch, AsyncMock
import aiohttp
from hypotez.src.utils.video import save_video_from_url, get_video_data


# Fixture for creating a temporary file for testing
@pytest.fixture
def temp_file(tmp_path):
    """Creates a temporary file for testing file operations."""
    file_path = tmp_path / "temp_file.txt"
    with open(file_path, "w") as f:
        f.write("Test content")
    return file_path


@pytest.fixture
def mock_aiohttp_session():
    """Mocks aiohttp.ClientSession to control responses."""

    async def mock_get(url, **kwargs):
        mock_response = AsyncMock()
        mock_response.raise_for_status = AsyncMock()
        # mock_response.content.read = AsyncMock(return_value=b"video_content") # this was causing errors with chunking. using iter_content now
        mock_response.iter_chunks = AsyncMock(return_value=[b"video", b"_content"])
        
        return mock_response

    mock_session = AsyncMock()
    mock_session.get = mock_get
    return mock_session

@pytest.fixture
def mock_aiohttp_session_error():
    """Mocks aiohttp.ClientSession to simulate an error."""

    async def mock_get_error(url, **kwargs):
        mock_response = AsyncMock()
        mock_response.raise_for_status.side_effect = aiohttp.ClientError("Mocked network error")
        return mock_response

    mock_session = AsyncMock()
    mock_session.get = mock_get_error
    return mock_session


# Tests for save_video_from_url function
@pytest.mark.asyncio
async def test_save_video_from_url_valid(mock_aiohttp_session, tmp_path):
    """Checks correct behavior with valid input."""
    url = "https://example.com/video.mp4"
    save_path = str(tmp_path / "test_video.mp4")
    
    with patch("aiohttp.ClientSession", return_value=mock_aiohttp_session):
        result = await save_video_from_url(url, save_path)
    
    assert result == Path(save_path)
    assert Path(save_path).exists()
    assert Path(save_path).stat().st_size > 0


@pytest.mark.asyncio
async def test_save_video_from_url_network_error(mock_aiohttp_session_error, tmp_path):
    """Checks correct handling of network errors."""
    url = "https://example.com/video.mp4"
    save_path = str(tmp_path / "test_video_error.mp4")

    with patch("aiohttp.ClientSession", return_value=mock_aiohttp_session_error):
        result = await save_video_from_url(url, save_path)
    
    assert result is None
    assert not Path(save_path).exists()


@pytest.mark.asyncio
async def test_save_video_from_url_file_exists(mock_aiohttp_session, tmp_path):
    """Checks that it overwrites existing files."""
    url = "https://example.com/video.mp4"
    save_path = tmp_path / "test_video_exists.mp4"
    save_path.touch()  # Create the file first

    with patch("aiohttp.ClientSession", return_value=mock_aiohttp_session):
        result = await save_video_from_url(url, str(save_path))
    
    assert result == save_path
    assert save_path.exists()
    assert save_path.stat().st_size > 0


@pytest.mark.asyncio
async def test_save_video_from_url_empty_response(mock_aiohttp_session, tmp_path):
    """Tests what happens when the returned video is empty."""
    url = "https://example.com/video.mp4"
    save_path = str(tmp_path / "test_video_empty.mp4")

    # Use the default mock, but modify it so that it returns an empty result
    async def mock_get_empty(url, **kwargs):
        mock_response = AsyncMock()
        mock_response.raise_for_status = AsyncMock()
        mock_response.iter_chunks = AsyncMock(return_value=[])
        return mock_response

    mock_aiohttp_empty_session = AsyncMock()
    mock_aiohttp_empty_session.get = mock_get_empty

    with patch("aiohttp.ClientSession", return_value=mock_aiohttp_empty_session):
        result = await save_video_from_url(url, save_path)
    
    assert result is None
    assert not Path(save_path).exists()

@pytest.mark.asyncio
async def test_save_video_from_url_invalid_url(mock_aiohttp_session_error, tmp_path):
    """Checks correct handling of invalid URL."""
    url = "invalid_url"
    save_path = str(tmp_path / "invalid_url_video.mp4")

    with patch("aiohttp.ClientSession", return_value=mock_aiohttp_session_error):
      result = await save_video_from_url(url, save_path)

    assert result is None
    assert not Path(save_path).exists()

# Tests for get_video_data function
def test_get_video_data_valid(temp_file):
    """Checks correct retrieval of binary data from a valid file."""
    data = get_video_data(str(temp_file))
    assert isinstance(data, bytes)
    assert data == b"Test content"


def test_get_video_data_file_not_found():
    """Checks correct handling of a file that does not exist."""
    file_name = "non_existent_file.txt"
    data = get_video_data(file_name)
    assert data is None


def test_get_video_data_empty_file(tmp_path):
    """Checks behaviour with an empty file"""
    empty_file_path = tmp_path / "empty.txt"
    empty_file_path.touch()
    data = get_video_data(str(empty_file_path))
    assert data == b""


def test_get_video_data_read_error(temp_file):
    """Checks correct handling of a file read error."""
    
    with patch("builtins.open", side_effect=Exception("Mocked read error")):
       data = get_video_data(str(temp_file))

    assert data is None
```