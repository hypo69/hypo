```python
import pytest
import json

# Fixture for loading the JSON data
@pytest.fixture
def ivory_data():
    """Provides the ivory supplier data from the JSON file."""
    json_data = """
    {
      "supplier": "ivory",
      "supplier_id": "11343",
      "supplier_prefix": "ivory",
      "start_url": "https://www.ivory.co.il/",
      "login_url": "https://www.ivory.co.il/",
      "price_rule": "*1.43",
      "collect_products_from_categorypage": false,
      "if_login": true,
      "scenario_files": [],
      "last_runned_scenario": "",
      "excluded": []
    }
    """
    return json.loads(json_data)

# Tests for the supplier data structure
def test_ivory_supplier_name(ivory_data):
    """Checks if the supplier name is correct."""
    assert ivory_data["supplier"] == "ivory"

def test_ivory_supplier_id(ivory_data):
    """Checks if the supplier ID is correct."""
    assert ivory_data["supplier_id"] == "11343"

def test_ivory_supplier_prefix(ivory_data):
    """Checks if the supplier prefix is correct."""
    assert ivory_data["supplier_prefix"] == "ivory"

def test_ivory_start_url(ivory_data):
    """Checks if the start URL is correct."""
    assert ivory_data["start_url"] == "https://www.ivory.co.il/"

def test_ivory_login_url(ivory_data):
    """Checks if the login URL is correct."""
    assert ivory_data["login_url"] == "https://www.ivory.co.il/"

def test_ivory_price_rule(ivory_data):
    """Checks if the price rule is correct."""
    assert ivory_data["price_rule"] == "*1.43"

def test_ivory_collect_products_from_categorypage(ivory_data):
    """Checks if 'collect_products_from_categorypage' is set to false."""
    assert ivory_data["collect_products_from_categorypage"] is False

def test_ivory_if_login(ivory_data):
    """Checks if 'if_login' is set to true."""
    assert ivory_data["if_login"] is True

def test_ivory_scenario_files(ivory_data):
    """Checks if 'scenario_files' is an empty list."""
    assert isinstance(ivory_data["scenario_files"], list)
    assert not ivory_data["scenario_files"]

def test_ivory_last_runned_scenario(ivory_data):
    """Checks if 'last_runned_scenario' is an empty string."""
    assert ivory_data["last_runned_scenario"] == ""

def test_ivory_excluded(ivory_data):
    """Checks if 'excluded' is an empty list."""
    assert isinstance(ivory_data["excluded"], list)
    assert not ivory_data["excluded"]

def test_ivory_data_structure(ivory_data):
    """Checks if the data is a dictionary."""
    assert isinstance(ivory_data, dict)

def test_ivory_data_keys(ivory_data):
    """Checks if all expected keys are present in the data."""
    expected_keys = ["supplier", "supplier_id", "supplier_prefix", "start_url",
                     "login_url", "price_rule", "collect_products_from_categorypage",
                     "if_login", "scenario_files", "last_runned_scenario", "excluded"]
    assert set(ivory_data.keys()) == set(expected_keys)
```