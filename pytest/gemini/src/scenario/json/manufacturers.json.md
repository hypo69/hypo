```python
import pytest
import json

# Fixture definitions, if needed
@pytest.fixture
def sample_json_data():
    """Provides sample JSON data for testing."""
    return {
        "pemco-hardware": {
            "descripiton": "heavy industry",
            "url": "https://www.pemco-hardware.com"
        }
    }

@pytest.fixture
def invalid_json_data():
    """Provides invalid JSON data for testing."""
    return {
         "pemco-hardware": {
             "descripiton": 123,  #invalid data
             "url": "https://www.pemco-hardware.com"
        }
    }

# Tests for loading and parsing the JSON data
def test_load_json_valid_data(sample_json_data):
    """Checks if valid JSON data is loaded correctly."""
    # In a real application, this might involve reading the file using 'with open(...) as f:'
    # and parsing with json.load(f). For now, we'll use the fixture directly.
    assert isinstance(sample_json_data, dict)
    assert "pemco-hardware" in sample_json_data
    assert sample_json_data["pemco-hardware"]["descripiton"] == "heavy industry"
    assert sample_json_data["pemco-hardware"]["url"] == "https://www.pemco-hardware.com"


def test_load_json_with_invalid_data(invalid_json_data):
  """Checks if invalid JSON data (wrong type) throws error."""
  with pytest.raises(TypeError):
    assert invalid_json_data["pemco-hardware"]["descripiton"] == "heavy industry"


def test_load_json_empty_data():
    """Checks if an empty JSON object is handled correctly."""
    empty_data = {}
    assert isinstance(empty_data, dict)
    assert len(empty_data) == 0

def test_load_json_missing_key(sample_json_data):
   """Checks if missing data is handled correctly"""
   with pytest.raises(KeyError):
       assert sample_json_data["non_existent_key"]

def test_load_json_invalid_format():
    """Checks if invalid JSON format raises exception."""
    invalid_json_string = "invalid json string"
    with pytest.raises(json.JSONDecodeError):
        json.loads(invalid_json_string)
```