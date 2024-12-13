```python
import pytest
import json
from pathlib import Path

# Assuming the JSON data is loaded into a Python dictionary for testing
@pytest.fixture
def dornet_data():
    """Provides the Dornet configuration data for testing."""
    return {
        "supplier": "Dornet",
        "supplier_prefix": "DRNT-",
        "price_rule": "1.4",
        "infinity_scroll": False,
        "num_items_4_flush": 300,
        "parcing method [webdriver|api]": "web",
        "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
        "scenario_files": [
            []
        ],
        "last_runned_scenario": ""
    }


def test_dornet_supplier_name(dornet_data):
    """Checks if the supplier name is correctly set to 'Dornet'."""
    assert dornet_data["supplier"] == "Dornet"


def test_dornet_supplier_prefix(dornet_data):
    """Checks if the supplier prefix is correctly set to 'DRNT-'."""
    assert dornet_data["supplier_prefix"] == "DRNT-"


def test_dornet_price_rule_is_float_str(dornet_data):
    """Checks if the price rule is a string representation of a float."""
    assert isinstance(dornet_data["price_rule"], str)
    try:
       float(dornet_data["price_rule"])
    except ValueError:
      pytest.fail("Price rule is not convertible to a float")

def test_dornet_infinity_scroll_is_bool(dornet_data):
   """Checks if 'infinity_scroll' is a boolean value."""
   assert isinstance(dornet_data["infinity_scroll"], bool)


def test_dornet_num_items_4_flush_is_int(dornet_data):
    """Checks if 'num_items_4_flush' is an integer."""
    assert isinstance(dornet_data["num_items_4_flush"], int)


def test_dornet_parcing_method(dornet_data):
    """Checks if the parsing method is set to 'web'."""
    assert dornet_data["parcing method [webdriver|api]"] == "web"


def test_dornet_about_method_web_scrapping(dornet_data):
    """Checks the 'about method' string is not empty."""
    assert isinstance(dornet_data["about method web scrapping [webdriver|api]"], str)
    assert len(dornet_data["about method web scrapping [webdriver|api]"]) > 0


def test_dornet_scenario_files_is_list_of_lists(dornet_data):
    """Checks that 'scenario_files' is a list and that its elements are lists."""
    assert isinstance(dornet_data["scenario_files"], list)
    for item in dornet_data["scenario_files"]:
        assert isinstance(item, list)


def test_dornet_last_runned_scenario_is_str(dornet_data):
    """Checks that 'last_runned_scenario' is a string."""
    assert isinstance(dornet_data["last_runned_scenario"], str)

def test_dornet_loading_from_file():
    """Tests if the dornet config can be loaded correctly from the specified JSON file."""
    file_path = Path("hypotez/src/scenario/json/dornet.json")  # Path object
    if not file_path.exists():
         pytest.skip(f"File does not exist: {file_path}")

    with open(file_path, 'r') as f:
        data = json.load(f)
    
    assert isinstance(data, dict)
    assert data["supplier"] == "Dornet"
    assert data["supplier_prefix"] == "DRNT-"
    
    try:
        float(data["price_rule"])
    except ValueError:
      pytest.fail("Price rule is not convertible to a float")

    assert isinstance(data["infinity_scroll"], bool)
    assert isinstance(data["num_items_4_flush"], int)
    assert data["parcing method [webdriver|api]"] == "web"
    assert isinstance(data["about method web scrapping [webdriver|api]"], str)
    assert len(data["about method web scrapping [webdriver|api]"]) > 0
    assert isinstance(data["scenario_files"], list)
    for item in data["scenario_files"]:
        assert isinstance(item, list)
    assert isinstance(data["last_runned_scenario"], str)
```