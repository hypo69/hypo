```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def json_data():
    """Provides the JSON data from the file."""
    file_path = 'hypotez/src/scenario/json/victorinox.json'
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def test_supplier_exists(json_data):
    """Checks if the 'supplier' key exists in the JSON and has a value."""
    assert "supplier" in json_data
    assert json_data["supplier"] == "ksp"


def test_supplier_prefix_exists(json_data):
    """Checks if the 'supplier_prefix' key exists in the JSON and has a value."""
    assert "supplier_prefix" in json_data
    assert json_data["supplier_prefix"] == "ksp"

def test_start_url_exists(json_data):
    """Checks if the 'start_url' key exists in the JSON and has a valid URL."""
    assert "start_url" in json_data
    assert json_data["start_url"] == "https://www.ksp.co.il/"

def test_price_rule_exists(json_data):
    """Checks if the 'price_rule' key exists and is a string."""
    assert "price_rule" in json_data
    assert isinstance(json_data["price_rule"], str)


def test_num_items_4_flush_exists(json_data):
    """Checks if 'num_items_4_flush' key exists and is an integer."""
    assert "num_items_4_flush" in json_data
    assert isinstance(json_data["num_items_4_flush"], int)


def test_if_login_exists(json_data):
    """Checks if the 'if_login' key exists and is a boolean."""
    assert "if_login" in json_data
    assert isinstance(json_data["if_login"], bool)

def test_collect_products_from_categorypage_exists(json_data):
    """Checks if the 'collect_products_from_categorypage' key exists and is a boolean."""
    assert "collect_products_from_categorypage" in json_data
    assert isinstance(json_data["collect_products_from_categorypage"], bool)

def test_scenarios_exists(json_data):
    """Checks if 'scenarios' key exists and is a list."""
    assert "scenarios" in json_data
    assert isinstance(json_data["scenarios"], list)

def test_scenarios_not_empty(json_data):
    """Checks if the 'scenarios' list is not empty"""
    assert len(json_data["scenarios"]) > 0

def test_scenarios_are_strings(json_data):
    """Checks if all items in 'scenarios' are strings."""
    for item in json_data["scenarios"]:
        assert isinstance(item, str)

def test_excluded_exists(json_data):
    """Checks if 'excluded' key exists and is a list."""
    assert "excluded" in json_data
    assert isinstance(json_data["excluded"], list)
    

def test_excluded_are_strings(json_data):
    """Checks if all items in 'excluded' are strings."""
    for item in json_data["excluded"]:
        assert isinstance(item, str)
    
def test_last_runned_scenario_exists(json_data):
    """Checks if the 'last_runned_scenario' key exists and is a string."""
    assert "last_runned_scenario" in json_data
    assert isinstance(json_data["last_runned_scenario"], str)

def test_price_rule_valid_format(json_data):
    """Check if price_rule is a valid string format."""
    assert json_data["price_rule"][0] in ["+", "-"]
    assert json_data["price_rule"][1:].isdigit()


def test_num_items_4_flush_positive(json_data):
    """Checks if 'num_items_4_flush' is a positive integer."""
    assert json_data["num_items_4_flush"] >= 0
```