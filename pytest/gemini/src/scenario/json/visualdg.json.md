```python
import pytest
import json

# Fixture for loading the JSON data
@pytest.fixture
def visualdg_data():
    """Provides the JSON data for testing."""
    json_data = """
{
  "supplier": "visualdg",
  "supplier_prefix": "VDG-",
  "start_url": "https://www.visualdg.co.il/",
  "price_rule": "*1.43",
  "if_list":"first","use_mouse": false, "mandatory": true,
  "num_items_4_flush": 25,
  "collect_products_from_categorypage": false,
  "parcing method [webdriver|api]": "web",
  "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
  "scenario_files": [

    [
      "visualdg_categories_laptops_asus.json",
      "visualdg_categories_laptops_lenovo_thinkbook.json",
      "visualdg_categories_laptops_lenovo_thinkpad_e.json",
      "visualdg_categories_laptops_lenovo_thinkpad_l.json",
      "visualdg_categories_laptops_lenovo_thinkpad_p.json",
      "visualdg_categories_laptops_lenovo_thinkpad_t.json",
      "visualdg_categories_laptops_lenovo_thinkpad_x.json",
      "visualdg_categories_laptops_lenovo_v_essentials.json",
      "visualdg_categories_laptops_lenovo_yoga.json"
    ],
    [ "visualdg_categories_desktops_lenovo_workstation_p.json" ],
    [ "visualdg_categories_cases_asus.json" ],
    [ "visualdg_categories_minipc_asus.json" ],
    [ "visualdg_categories_mb_asus.json" ],
    [ "visualdg_categories_video_asus.json" ],
    [ "visualdg_categories_monitors_asus.json" ]

  ],
  "last_runned_scenario": ""
}
"""
    return json.loads(json_data)

def test_supplier_name(visualdg_data):
    """Checks if the supplier name is correct."""
    assert visualdg_data["supplier"] == "visualdg"

def test_supplier_prefix(visualdg_data):
    """Checks if the supplier prefix is correct."""
    assert visualdg_data["supplier_prefix"] == "VDG-"

def test_start_url(visualdg_data):
    """Checks if the start URL is correct."""
    assert visualdg_data["start_url"] == "https://www.visualdg.co.il/"

def test_price_rule(visualdg_data):
    """Checks if the price rule is correct."""
    assert visualdg_data["price_rule"] == "*1.43"

def test_if_list(visualdg_data):
    """Checks the value of the 'if_list' key."""
    assert visualdg_data["if_list"] == "first"

def test_use_mouse(visualdg_data):
    """Checks if 'use_mouse' is set to false."""
    assert visualdg_data["use_mouse"] == False

def test_mandatory(visualdg_data):
    """Checks if 'mandatory' is set to true."""
    assert visualdg_data["mandatory"] == True

def test_num_items_4_flush(visualdg_data):
    """Checks if num_items_4_flush is set correctly."""
    assert visualdg_data["num_items_4_flush"] == 25

def test_collect_products_from_categorypage(visualdg_data):
    """Checks if 'collect_products_from_categorypage' is set to false."""
    assert visualdg_data["collect_products_from_categorypage"] == False

def test_parcing_method(visualdg_data):
    """Checks the value of 'parcing method' key."""
    assert visualdg_data["parcing method [webdriver|api]"] == "web"

def test_about_method(visualdg_data):
    """Checks the value of 'about method' key."""
    assert visualdg_data["about method web scrapping [webdriver|api]"] == "Если я работаю через API мне не нужен webdriver"

def test_scenario_files_is_list(visualdg_data):
    """Checks if 'scenario_files' is a list."""
    assert isinstance(visualdg_data["scenario_files"], list)

def test_scenario_files_not_empty(visualdg_data):
    """Checks if the scenario_files list is not empty."""
    assert len(visualdg_data["scenario_files"]) > 0
    
def test_scenario_files_inner_lists(visualdg_data):
    """Checks if each element in scenario_files is a list."""
    for item in visualdg_data["scenario_files"]:
        assert isinstance(item, list)

def test_last_runned_scenario_is_string(visualdg_data):
    """Checks if 'last_runned_scenario' is a string."""
    assert isinstance(visualdg_data["last_runned_scenario"], str)

def test_last_runned_scenario_empty(visualdg_data):
    """Checks if 'last_runned_scenario' is initialized to an empty string."""
    assert visualdg_data["last_runned_scenario"] == ""

def test_scenario_files_content(visualdg_data):
    """Checks if the content of scenario_files are strings."""
    for file_list in visualdg_data["scenario_files"]:
        for file_name in file_list:
             assert isinstance(file_name, str)

def test_scenario_files_nested_lists_are_not_empty(visualdg_data):
    """Checks if the nested lists in scenario_files are not empty."""
    for file_list in visualdg_data["scenario_files"]:
        assert len(file_list) > 0
```