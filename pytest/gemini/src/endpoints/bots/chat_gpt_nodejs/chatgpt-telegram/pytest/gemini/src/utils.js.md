```python
import pytest
from unittest.mock import patch, AsyncMock
from src.utils import removeFile

# Tests for removeFile function

@pytest.mark.asyncio
async def test_removeFile_valid_path():
    """
    Checks if removeFile removes a file successfully when a valid path is provided.
    It mocks the unlink function and verifies it was called with the correct path.
    """
    mock_unlink = AsyncMock()
    with patch('src.utils.unlink', mock_unlink):
        test_path = "test_file.txt"
        await removeFile(test_path)
        mock_unlink.assert_called_once_with(test_path)

@pytest.mark.asyncio
async def test_removeFile_file_not_found():
    """
    Checks if removeFile handles 'file not found' errors correctly.
    It mocks unlink to throw a file not found error and ensures no exception is raised.
    Additionally, verifies the error message is logged (using patch on console.log).
    """
    mock_unlink = AsyncMock(side_effect=FileNotFoundError("File not found"))
    mock_console_log = AsyncMock()
    
    with patch('src.utils.unlink', mock_unlink), patch('src.utils.console.log',mock_console_log):
        test_path = "non_existent_file.txt"
        await removeFile(test_path)
        mock_console_log.assert_called_once() #check the console.log called at least once
        # verify that console log called with error message
        mock_console_log.assert_called_with('Error while removing file', 'File not found')

@pytest.mark.asyncio
async def test_removeFile_permission_error():
    """
    Checks if removeFile handles permission errors correctly.
    It mocks unlink to throw a permission error and ensures no exception is raised.
    Additionally, verifies the error message is logged (using patch on console.log).
    """
    mock_unlink = AsyncMock(side_effect=PermissionError("Permission denied"))
    mock_console_log = AsyncMock()
    
    with patch('src.utils.unlink', mock_unlink), patch('src.utils.console.log',mock_console_log):
        test_path = "protected_file.txt"
        await removeFile(test_path)
        mock_console_log.assert_called_once() #check the console.log called at least once
        # verify that console log called with error message
        mock_console_log.assert_called_with('Error while removing file', 'Permission denied')

@pytest.mark.asyncio
async def test_removeFile_empty_path():
    """
    Checks if removeFile handles an empty path.
    In this case unlink will be called with an empty path. This does not throw an error.
    """
    mock_unlink = AsyncMock()
    with patch('src.utils.unlink', mock_unlink):
        test_path = ""
        await removeFile(test_path)
        mock_unlink.assert_called_once_with(test_path)
```