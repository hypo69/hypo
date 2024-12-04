```python
import pytest
import ftplib
from pathlib import Path
from hypotez.src.utils.ftp import write, read, delete

# Fixture to simulate a connection, used in all test functions
@pytest.fixture
def ftp_session():
    """Fixture to create an FTP session for testing."""
    try:
        session = ftplib.FTP('ftp.example.com', 'username', 'password')
        yield session
        session.quit()
    except Exception as e:
        pytest.fail(f"Failed to establish FTP connection: {e}")

# Test cases for write function
def test_write_valid_input(ftp_session):
    """Tests writing a file to the FTP server."""
    # Create a temporary file for testing
    test_file = Path("test_file.txt")
    test_file.write_text("Test file content")
    dest_dir = "/test_dir"
    dest_file_name = "test_file.txt"
    
    # Attempt to create the directory if it does not exist
    try:
        ftp_session.mkd(dest_dir)
    except ftplib.error_perm:
        pass # Ignore error if directory already exists
        
    result = write(str(test_file), dest_dir, dest_file_name)
    assert result == True, "File wasn't written successfully"
    test_file.unlink()  # Clean up the temporary file

def test_write_invalid_file(ftp_session):
    """Tests writing a file that does not exist."""
    dest_dir = "/test_dir"
    dest_file_name = "nonexistent_file.txt"
    result = write("nonexistent_file.txt", dest_dir, dest_file_name)
    assert result == False, "File write should have failed"
    
def test_write_no_connection(ftp_session):
    """Tests writing a file with a failing connection."""
    with pytest.raises(ftplib.error_perm):
        write("test_file.txt", "/test_dir", "test_file.txt")


# Test cases for read function
def test_read_valid_input(ftp_session):
    """Tests reading a file from the FTP server."""
    test_file = Path("test_file.txt")
    test_file.write_text("Test file content")
    dest_dir = "/test_dir"
    dest_file_name = "test_file.txt"

    #Write the file to the server
    with open(test_file, 'rb') as f:
        ftp_session.storbinary(f'STOR {dest_file_name}', f)
    
    #Read the file
    ftp_session.cwd(dest_dir)
    result = read(str(test_file), dest_dir, dest_file_name)
    assert result == b"Test file content" , "File wasn't read successfully"
    test_file.unlink()

def test_read_file_not_found(ftp_session):
    """Tests reading a file that does not exist."""
    result = read("test_file.txt", "/test_dir", "missing_file.txt")
    assert result is None, "Should return None if file not found"
    

# Test cases for delete function
def test_delete_valid_input(ftp_session):
    """Tests deleting a file from the FTP server."""
    test_file = Path("test_file.txt")
    test_file.write_text("Test file content")
    dest_dir = "/test_dir"
    dest_file_name = "test_file.txt"
    
    #Write the file to the server
    with open(test_file, 'rb') as f:
        ftp_session.storbinary(f'STOR {dest_file_name}', f)
        
    ftp_session.cwd(dest_dir)
    result = delete(str(test_file), dest_dir, dest_file_name)
    assert result == True, "File wasn't deleted successfully"
    test_file.unlink()
    
def test_delete_file_not_found(ftp_session):
    """Tests deleting a file that does not exist."""
    result = delete("test_file.txt", "/test_dir", "missing_file.txt")
    assert result == False, "Should return False if file not found"


```