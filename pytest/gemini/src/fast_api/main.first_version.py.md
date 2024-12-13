```python
import pytest
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pathlib import Path
from unittest.mock import patch, mock_open

# Assuming your main.py file is in the same directory
from hypotez.src.fast_api.main import app

# Create a test client
client = TestClient(app)

@pytest.fixture
def mock_subprocess_popen():
    """Mocks subprocess.Popen to control script execution."""
    with patch('hypotez.src.fast_api.main.Popen') as mock_popen:
        yield mock_popen

def test_process_data_valid_input(mock_subprocess_popen):
    """Tests the /process_data endpoint with valid inputs."""
    mock_process = mock_subprocess_popen.return_value
    mock_process.communicate.return_value = (b"Script output", b"")
    mock_process.returncode = 0

    response = client.post("/process_data", data={"first_name": "John", "last_name": "Doe"})
    assert response.status_code == 200
    assert response.json() == {"output": "Script output"}
    mock_subprocess_popen.assert_called_once()

def test_process_data_missing_first_name(mock_subprocess_popen):
    """Tests /process_data endpoint when first_name is missing."""
    response = client.post("/process_data", data={"last_name": "Doe"})
    assert response.status_code == 400
    assert response.json() == {"detail": "First name and last name must be provided"}
    mock_subprocess_popen.assert_not_called()


def test_process_data_missing_last_name(mock_subprocess_popen):
    """Tests /process_data endpoint when last_name is missing."""
    response = client.post("/process_data", data={"first_name": "John"})
    assert response.status_code == 400
    assert response.json() == {"detail": "First name and last name must be provided"}
    mock_subprocess_popen.assert_not_called()

def test_process_data_empty_first_name(mock_subprocess_popen):
    """Tests /process_data endpoint when first_name is empty."""
    response = client.post("/process_data", data={"first_name": "", "last_name": "Doe"})
    assert response.status_code == 400
    assert response.json() == {"detail": "First name and last name must be provided"}
    mock_subprocess_popen.assert_not_called()

def test_process_data_empty_last_name(mock_subprocess_popen):
    """Tests /process_data endpoint when last_name is empty."""
    response = client.post("/process_data", data={"first_name": "John", "last_name": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": "First name and last name must be provided"}
    mock_subprocess_popen.assert_not_called()

def test_process_data_script_error(mock_subprocess_popen):
    """Tests /process_data when the script execution fails."""
    mock_process = mock_subprocess_popen.return_value
    mock_process.communicate.return_value = (b"", b"Script error")
    mock_process.returncode = 1

    response = client.post("/process_data", data={"first_name": "John", "last_name": "Doe"})
    assert response.status_code == 500
    assert response.json() == {"detail": "Error executing the script: Script error"}

def test_open_index():
    """Tests the / endpoint redirects to index.html"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Redirecting to index.html..."}
```