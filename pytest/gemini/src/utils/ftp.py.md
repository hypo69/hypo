```python
import pytest
import ftplib
from pathlib import Path
from unittest.mock import patch, mock_open
from hypotez.src.utils import ftp
from hypotez.src.logger.logger import logger

# Mock FTP connection details to avoid actual FTP interaction
_connection = {
    'server': 'test.example.com',
    'port': 21,
    'user': 'test_user',
    'password': 'test_password'
}
ftp._connection = _connection

# Fixtures
@pytest.fixture
def mock_ftp_session():
    """Mocks ftplib.FTP to simulate FTP session."""
    with patch('ftplib.FTP') as mock_ftp:
      mock_session = mock_ftp.return_value
      yield mock_session

@pytest.fixture
def mock_logger():
    """Mocks logger to verify log output."""
    with patch('hypotez.src.utils.ftp.logger') as mock_log:
      yield mock_log

@pytest.fixture
def temp_file(tmp_path):
    """Creates a temporary file for testing."""
    file_path = tmp_path / "test_file.txt"
    with open(file_path, "w") as f:
        f.write("Test content")
    return str(file_path)

# Test cases for write function
def test_write_success(mock_ftp_session, temp_file):
    """Checks successful file upload."""
    mock_ftp_session.cwd.return_value = None
    mock_ftp_session.storbinary.return_value = None
    
    result = ftp.write(temp_file, '/test_dir', 'test_file.txt')
    
    assert result is True
    mock_ftp_session.cwd.assert_called_once_with('/test_dir')
    mock_ftp_session.storbinary.assert_called_once()
    mock_ftp_session.quit.assert_called_once()

def test_write_ftp_connection_error(mock_ftp_session, mock_logger, temp_file):
  """Checks handling of FTP connection error."""
  mock_ftp_session.side_effect = Exception('Connection failed')
  result = ftp.write(temp_file, '/test_dir', 'test_file.txt')
  assert result is False
  mock_logger.error.assert_called_once()
  mock_ftp_session.assert_called_once()

def test_write_file_transfer_error(mock_ftp_session, mock_logger, temp_file):
    """Checks handling of file transfer error."""
    mock_ftp_session.cwd.return_value = None
    mock_ftp_session.storbinary.side_effect = Exception('Transfer failed')
    
    result = ftp.write(temp_file, '/test_dir', 'test_file.txt')

    assert result is False
    mock_logger.error.assert_called_once()
    mock_ftp_session.quit.assert_called_once()
    

def test_write_close_ftp_session_error(mock_ftp_session, mock_logger, temp_file):
  """Checks handling of error when closing the FTP session."""
  mock_ftp_session.cwd.return_value = None
  mock_ftp_session.storbinary.return_value = None
  mock_ftp_session.quit.side_effect = Exception('Quit failed')

  result = ftp.write(temp_file, '/test_dir', 'test_file.txt')

  assert result is True
  mock_logger.error.assert_called_once()
  mock_ftp_session.quit.assert_called_once()

# Test cases for read function
def test_read_success(mock_ftp_session, tmp_path):
    """Checks successful file download."""
    dest_file_path = str(tmp_path / 'downloaded_file.txt')
    mock_ftp_session.cwd.return_value = None
    mock_ftp_session.retrbinary.side_effect = lambda cmd, callback: callback(b'Test content')

    result = ftp.read(dest_file_path, '/test_dir', 'test_file.txt')
    
    assert result == b'Test content'
    mock_ftp_session.cwd.assert_called_once_with('/test_dir')
    mock_ftp_session.retrbinary.assert_called_once()
    mock_ftp_session.quit.assert_called_once()

def test_read_ftp_connection_error(mock_ftp_session, mock_logger, tmp_path):
    """Checks handling of FTP connection error."""
    dest_file_path = str(tmp_path / 'downloaded_file.txt')
    mock_ftp_session.side_effect = Exception('Connection failed')
    result = ftp.read(dest_file_path, '/test_dir', 'test_file.txt')

    assert result is None
    mock_logger.error.assert_called_once()
    mock_ftp_session.assert_called_once()
    
def test_read_file_retrieval_error(mock_ftp_session, mock_logger, tmp_path):
    """Checks handling of file retrieval error."""
    dest_file_path = str(tmp_path / 'downloaded_file.txt')
    mock_ftp_session.cwd.return_value = None
    mock_ftp_session.retrbinary.side_effect = Exception('Retrieval failed')
    
    result = ftp.read(dest_file_path, '/test_dir', 'test_file.txt')

    assert result is None
    mock_logger.error.assert_called_once()
    mock_ftp_session.quit.assert_called_once()

def test_read_close_ftp_session_error(mock_ftp_session, mock_logger, tmp_path):
  """Checks handling of error when closing the FTP session."""
  dest_file_path = str(tmp_path / 'downloaded_file.txt')
  mock_ftp_session.cwd.return_value = None
  mock_ftp_session.retrbinary.side_effect = lambda cmd, callback: callback(b'Test content')
  mock_ftp_session.quit.side_effect = Exception('Quit failed')

  result = ftp.read(dest_file_path, '/test_dir', 'test_file.txt')

  assert result == b'Test content'
  mock_logger.error.assert_called_once()
  mock_ftp_session.quit.assert_called_once()
  

# Test cases for delete function
def test_delete_success(mock_ftp_session):
    """Checks successful file deletion."""
    mock_ftp_session.cwd.return_value = None
    mock_ftp_session.delete.return_value = None

    result = ftp.delete('/local_path', '/test_dir', 'test_file.txt')
    
    assert result is True
    mock_ftp_session.cwd.assert_called_once_with('/test_dir')
    mock_ftp_session.delete.assert_called_once_with('test_file.txt')
    mock_ftp_session.quit.assert_called_once()

def test_delete_ftp_connection_error(mock_ftp_session, mock_logger):
    """Checks handling of FTP connection error."""
    mock_ftp_session.side_effect = Exception('Connection failed')
    result = ftp.delete('/local_path', '/test_dir', 'test_file.txt')
    
    assert result is False
    mock_logger.error.assert_called_once()
    mock_ftp_session.assert_called_once()


def test_delete_file_deletion_error(mock_ftp_session, mock_logger):
    """Checks handling of file deletion error."""
    mock_ftp_session.cwd.return_value = None
    mock_ftp_session.delete.side_effect = Exception('Deletion failed')

    result = ftp.delete('/local_path', '/test_dir', 'test_file.txt')
    
    assert result is False
    mock_logger.error.assert_called_once()
    mock_ftp_session.quit.assert_called_once()

def test_delete_close_ftp_session_error(mock_ftp_session, mock_logger):
    """Checks handling of error when closing the FTP session."""
    mock_ftp_session.cwd.return_value = None
    mock_ftp_session.delete.return_value = None
    mock_ftp_session.quit.side_effect = Exception('Quit failed')

    result = ftp.delete('/local_path', '/test_dir', 'test_file.txt')
    
    assert result is True
    mock_logger.error.assert_called_once()
    mock_ftp_session.quit.assert_called_once()
```