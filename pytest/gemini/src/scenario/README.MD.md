```python
import pytest
import json
from unittest.mock import patch, mock_open
import requests
from requests.exceptions import RequestException

# Assume that the module is located in src/scenario and can be imported
# For local testing you can do the following in the root folder:
# Create the src folder, then create the src/scenario folder and place the module
# you are testing inside of it. Create an empty __init__.py inside the src/scenario folder,
# then you can import like this:
try:
    from src.scenario import run_scenario_files, run_scenario_file, run_scenario, dump_journal
except ImportError:
    # For running inside the current folder
    from scenario import run_scenario_files, run_scenario_file, run_scenario, dump_journal

# --- Fixtures ---
@pytest.fixture
def mock_settings():
    """Provides a mock settings object."""
    class MockSettings:
        def __init__(self):
            self.journal_file = "journal.json"
        
    return MockSettings()

@pytest.fixture
def valid_scenario_file(tmp_path):
    """Creates a valid scenario file."""
    scenario_data = {
        "scenarios": {
            "test_scenario": {
                "url": "https://example.com/test",
                "name": "test_scenario",
                "presta_categories": {
                    "default_category": 1,
                    "additional_categories": [2, 3]
                }
            }
        }
    }
    file_path = tmp_path / "test_scenario.json"
    with open(file_path, "w") as f:
        json.dump(scenario_data, f)
    return str(file_path)

@pytest.fixture
def invalid_scenario_file(tmp_path):
     """Creates an invalid scenario file (invalid JSON)."""
     file_path = tmp_path / "invalid_scenario.json"
     with open(file_path, "w") as f:
        f.write("invalid json")
     return str(file_path)

@pytest.fixture
def mock_product_data():
    """Provides mock product data."""
    return [
        {"name": "Product 1", "price": 10.0},
        {"name": "Product 2", "price": 20.0}
    ]

@pytest.fixture
def mock_website_content(mock_product_data):
    """Provides mock html content for a website"""
    content = f"""
    <html>
    <body>
        <h1>Product list</h1>
        <div class="product-list">
        { ''.join(f'<div class="product"><h2 class="name">{product["name"]}</h2><p class="price">{product["price"]}</p></div>' for product in mock_product_data ) }
        </div>
    </body>
    </html>
    """
    return content

# --- Tests for `run_scenario_files` ---
def test_run_scenario_files_valid_list(mock_settings, valid_scenario_file, monkeypatch):
    """Checks correct execution with a valid list of scenario files."""
    with patch("src.scenario.run_scenario_file") as mock_run_scenario_file:
        run_scenario_files(mock_settings, [valid_scenario_file])
        mock_run_scenario_file.assert_called_once_with(mock_settings, valid_scenario_file)

def test_run_scenario_files_empty_list(mock_settings, monkeypatch):
    """Checks execution with an empty list of scenario files."""
    with patch("src.scenario.run_scenario_file") as mock_run_scenario_file:
        run_scenario_files(mock_settings, [])
        mock_run_scenario_file.assert_not_called()

def test_run_scenario_files_file_not_found(mock_settings, monkeypatch):
    """Checks `FileNotFoundError` when a scenario file does not exist."""
    with pytest.raises(FileNotFoundError):
       run_scenario_files(mock_settings, ["nonexistent_file.json"])

def test_run_scenario_files_json_decode_error(mock_settings, invalid_scenario_file, monkeypatch):
    """Checks `JSONDecodeError` when a scenario file contains invalid JSON."""
    with pytest.raises(json.JSONDecodeError):
        run_scenario_files(mock_settings, [invalid_scenario_file])

# --- Tests for `run_scenario_file` ---
def test_run_scenario_file_valid_file(mock_settings, valid_scenario_file, monkeypatch):
    """Checks correct execution with a valid scenario file."""
    with patch("src.scenario.run_scenario") as mock_run_scenario:
       run_scenario_file(mock_settings, valid_scenario_file)
       mock_run_scenario.assert_called_once()

def test_run_scenario_file_file_not_found(mock_settings, monkeypatch):
    """Checks `FileNotFoundError` when the scenario file does not exist."""
    with pytest.raises(FileNotFoundError):
        run_scenario_file(mock_settings, "nonexistent_file.json")

def test_run_scenario_file_json_decode_error(mock_settings, invalid_scenario_file, monkeypatch):
    """Checks `JSONDecodeError` when a scenario file contains invalid JSON."""
    with pytest.raises(json.JSONDecodeError):
        run_scenario_file(mock_settings, invalid_scenario_file)

def test_run_scenario_file_exception_during_scenario(mock_settings, valid_scenario_file, monkeypatch):
    """Checks `Exception` is raised if an exception happens during scenario execution."""
    with patch("src.scenario.run_scenario", side_effect=Exception("Test Exception")):
       with pytest.raises(Exception, match="Test Exception"):
           run_scenario_file(mock_settings, valid_scenario_file)


# --- Tests for `run_scenario` ---
def test_run_scenario_valid_scenario(mock_settings, monkeypatch, mock_website_content, mock_product_data):
    """Checks correct execution with a valid scenario."""
    mock_scenario = {
        "url": "https://example.com/test",
        "name": "test_scenario",
        "presta_categories": {
            "default_category": 1,
            "additional_categories": [2, 3]
        }
    }

    # Mock requests.get to return some test content
    monkeypatch.setattr(requests, 'get', lambda *args, **kwargs: MockResponse(mock_website_content))
    with patch("src.scenario.insert_product_to_prestashop") as mock_insert_product:
        with patch("src.scenario.get_product_data_from_html", return_value=mock_product_data):
            run_scenario(mock_settings, mock_scenario)
            assert mock_insert_product.call_count == len(mock_product_data)

def test_run_scenario_request_exception(mock_settings, monkeypatch):
    """Checks `RequestException` is raised on network issues."""
    mock_scenario = {
         "url": "https://example.com/test",
         "name": "test_scenario",
          "presta_categories": {
             "default_category": 1,
             "additional_categories": [2, 3]
         }
    }

    monkeypatch.setattr(requests, 'get', side_effect=RequestException("Network Error"))
    with pytest.raises(RequestException, match="Network Error"):
        run_scenario(mock_settings, mock_scenario)

def test_run_scenario_exception_during_processing(mock_settings, monkeypatch, mock_website_content):
    """Checks `Exception` is raised if an exception happens during scenario processing."""
    mock_scenario = {
          "url": "https://example.com/test",
          "name": "test_scenario",
          "presta_categories": {
              "default_category": 1,
              "additional_categories": [2, 3]
          }
     }
    monkeypatch.setattr(requests, 'get', lambda *args, **kwargs: MockResponse(mock_website_content))
    with patch("src.scenario.get_product_data_from_html", side_effect=Exception("Test Processing Error")):
        with pytest.raises(Exception, match="Test Processing Error"):
            run_scenario(mock_settings, mock_scenario)


# --- Tests for `dump_journal` ---
def test_dump_journal_valid_journal(mock_settings, tmp_path, monkeypatch):
    """Checks correct execution of dumping a valid journal."""
    journal = [{"message": "Test log 1"}, {"message": "Test log 2"}]
    file_path = tmp_path / mock_settings.journal_file
    with patch("builtins.open", mock_open()) as mock_file:
        dump_journal(mock_settings, journal)
        mock_file.assert_called_once_with(file_path, "w")
        mock_file().write.assert_called_once()
        args, kwargs = mock_file().write.call_args
        assert json.loads(args[0]) == journal

def test_dump_journal_exception_during_writing(mock_settings, monkeypatch):
    """Checks `Exception` raised if error during writing to file."""
    journal = [{"message": "Test log 1"}]
    with patch("builtins.open", side_effect=Exception("File error")):
       with pytest.raises(Exception, match="File error"):
            dump_journal(mock_settings, journal)

# --- Helper mock class for network requests ---
class MockResponse:
    def __init__(self, content, status_code=200):
        self.content = content
        self.status_code = status_code

    def raise_for_status(self):
       if self.status_code >= 400:
          raise RequestException()

    @property
    def text(self):
        return self.content
```