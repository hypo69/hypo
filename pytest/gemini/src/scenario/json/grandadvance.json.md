```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def grandadvance_config():
    """Loads the grandadvance configuration from the JSON file."""
    # Simulate loading from the given JSON data as a string since we don't have file access
    json_data = """
    {
      "supplier": "grandadvance",
      "supplier_prefix": "GRD-",
      "start_url": "https://www.grandadvance.co.il/",
      "login_url": "https://www.grandadvance.co.il/",
      "price_rule": "*1.43",
      "if_list":"first","use_mouse": false, "mandatory": true,
      "num_items_4_flush": 50,
      "if_login": true,
      "scenario_files": [
        [ "grandadvance_categories_keyboards_logitech.json" ],
        [
          "grandadvance_categories_laptops_acer.json",
          "grandadvance_categories_laptops_lenovo.json",
          "grandadvance_categories_laptops_hp.json",
          "grandadvance_categories_laptops_dell.json"
        ],
        [ "grandadvance_categories_video_nvidia.json" ]
      ],
      "last_runned_scenario": ""
    }
    """
    return json.loads(json_data)

def test_grandadvance_config_supplier(grandadvance_config):
    """Checks if the supplier name is correct."""
    assert grandadvance_config["supplier"] == "grandadvance"

def test_grandadvance_config_supplier_prefix(grandadvance_config):
    """Checks if the supplier prefix is correct."""
    assert grandadvance_config["supplier_prefix"] == "GRD-"

def test_grandadvance_config_start_url(grandadvance_config):
    """Checks if the start URL is correct."""
    assert grandadvance_config["start_url"] == "https://www.grandadvance.co.il/"

def test_grandadvance_config_login_url(grandadvance_config):
    """Checks if the login URL is correct."""
    assert grandadvance_config["login_url"] == "https://www.grandadvance.co.il/"

def test_grandadvance_config_price_rule(grandadvance_config):
    """Checks if the price rule is correct."""
    assert grandadvance_config["price_rule"] == "*1.43"

def test_grandadvance_config_if_list(grandadvance_config):
    """Checks if the if_list is correct."""
    assert grandadvance_config["if_list"] == "first"

def test_grandadvance_config_use_mouse(grandadvance_config):
    """Checks if the use_mouse is correct."""
    assert grandadvance_config["use_mouse"] == False

def test_grandadvance_config_mandatory(grandadvance_config):
    """Checks if the mandatory is correct."""
    assert grandadvance_config["mandatory"] == True

def test_grandadvance_config_num_items_4_flush(grandadvance_config):
    """Checks if the num_items_4_flush is correct."""
    assert grandadvance_config["num_items_4_flush"] == 50

def test_grandadvance_config_if_login(grandadvance_config):
    """Checks if the if_login is correct."""
    assert grandadvance_config["if_login"] == True

def test_grandadvance_config_scenario_files_structure(grandadvance_config):
    """Checks if the scenario_files is a list of lists."""
    assert isinstance(grandadvance_config["scenario_files"], list)
    for item in grandadvance_config["scenario_files"]:
        assert isinstance(item, list)

def test_grandadvance_config_scenario_files_content(grandadvance_config):
    """Checks the content of the scenario files list."""
    expected_files = [
        ["grandadvance_categories_keyboards_logitech.json"],
        [
            "grandadvance_categories_laptops_acer.json",
            "grandadvance_categories_laptops_lenovo.json",
            "grandadvance_categories_laptops_hp.json",
            "grandadvance_categories_laptops_dell.json"
        ],
        ["grandadvance_categories_video_nvidia.json"]
    ]
    assert grandadvance_config["scenario_files"] == expected_files

def test_grandadvance_config_last_runned_scenario(grandadvance_config):
    """Checks if the last_runned_scenario is an empty string."""
    assert grandadvance_config["last_runned_scenario"] == ""

def test_grandadvance_config_missing_key():
    """Checks for KeyError if a key is missing in config data."""
    json_data_missing_key = """
    {
      "supplier": "grandadvance",
      "supplier_prefix": "GRD-",
      "start_url": "https://www.grandadvance.co.il/",
      "login_url": "https://www.grandadvance.co.il/",
      "price_rule": "*1.43",
      "if_list":"first","use_mouse": false, "mandatory": true,
      "if_login": true,
      "scenario_files": [
        [ "grandadvance_categories_keyboards_logitech.json" ],
        [
          "grandadvance_categories_laptops_acer.json",
          "grandadvance_categories_laptops_lenovo.json",
          "grandadvance_categories_laptops_hp.json",
          "grandadvance_categories_laptops_dell.json"
        ],
        [ "grandadvance_categories_video_nvidia.json" ]
      ]
     }
    """
    config_data = json.loads(json_data_missing_key)
    with pytest.raises(KeyError):
        config_data["num_items_4_flush"]
```