```python
import pytest
import json

# Fixture to load the JSON data (mimicking reading from a file)
@pytest.fixture
def ebay_store_data():
    """Provides test data loaded from the JSON structure."""
    json_data = """
    {
      "store": {
        "store_id": "thegasketsman75",
        "supplier_id": 4534,
        "get store banners": true,
        "description": "thegasketsman75 Gasket KIT",
        "about": " ",
        "url": "https://www.ebay.com/str/himaio12",
        "shop categories page": "",
        "shop categories json file": ""
      },
    
      "scenarios": {
        "Gaming Concoles": {
          "url": "https://www.ebay.com/str/himaio12",
          "active": true,
          "condition":"new",
          "presta_categories": {
            "template": { "gaming": "CONSOLES" }
          },
          "checkbox": false,
          "price_rule": 1
        }
      }
    }
    """
    return json.loads(json_data)

# Test cases for the 'store' section
def test_store_data_valid(ebay_store_data):
    """Checks if the 'store' section contains correct data."""
    store = ebay_store_data["store"]
    assert store["store_id"] == "thegasketsman75"
    assert store["supplier_id"] == 4534
    assert store["get store banners"] is True
    assert store["description"] == "thegasketsman75 Gasket KIT"
    assert store["about"] == " "
    assert store["url"] == "https://www.ebay.com/str/himaio12"
    assert store["shop categories page"] == ""
    assert store["shop categories json file"] == ""

def test_store_data_missing_key(ebay_store_data):
    """Checks if access to a missing key in 'store' raises KeyError."""
    store = ebay_store_data["store"]
    with pytest.raises(KeyError):
         _ = store["non_existent_key"]

# Test cases for the 'scenarios' section
def test_scenarios_data_valid(ebay_store_data):
    """Checks if the 'scenarios' section contains correct data."""
    scenarios = ebay_store_data["scenarios"]
    assert "Gaming Concoles" in scenarios
    gaming_consoles = scenarios["Gaming Concoles"]
    assert gaming_consoles["url"] == "https://www.ebay.com/str/himaio12"
    assert gaming_consoles["active"] is True
    assert gaming_consoles["condition"] == "new"
    assert gaming_consoles["presta_categories"]["template"]["gaming"] == "CONSOLES"
    assert gaming_consoles["checkbox"] is False
    assert gaming_consoles["price_rule"] == 1

def test_scenarios_data_missing_key(ebay_store_data):
     """Checks if access to a missing key in 'scenarios' raises KeyError."""
     scenarios = ebay_store_data["scenarios"]
     with pytest.raises(KeyError):
         _ = scenarios["non_existent_scenario"]

def test_scenarios_nested_missing_key(ebay_store_data):
    """Checks if access to a missing nested key in 'scenarios' raises KeyError."""
    scenarios = ebay_store_data["scenarios"]
    gaming_consoles = scenarios["Gaming Concoles"]
    with pytest.raises(KeyError):
        _ = gaming_consoles["presta_categories"]["template"]["non_existent"]

def test_scenarios_empty(ebay_store_data):
    """Checks behavior when 'scenarios' is empty."""
    ebay_store_data["scenarios"] = {}
    assert ebay_store_data["scenarios"] == {}

def test_scenarios_no_scenarios(ebay_store_data):
    """Checks behavior when the 'scenarios' key is missing."""
    del ebay_store_data["scenarios"]
    with pytest.raises(KeyError):
        _ = ebay_store_data["scenarios"]
```