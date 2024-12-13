```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def techorezef_data():
    """Provides the Techorezef JSON data for tests."""
    json_data = """
    {
      "supplier": "Techorezef",
      "supplier_prefix": "TRZ-",
      "price_rule": "1.4",
      "num_items_4_flush": 25,
      "parcing method [webdriver|api]": "web",
      "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
      "scenario_files": [
        [ "visualdg_categories_cases_asus.json" ],
        [ "visualdg_categories_desktops_lenovo_workstation_p.json" ],
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
        [ "visualdg_categories_minipc_asus.json" ],
        [ "visualdg_categories_mb_asus.json" ],
        [ "visualdg_categories_video_asus.json" ],
        [ "visualdg_categories_monitors_asus.json" ]

      ],
      "last_runned_scenario": ""
    }
    """
    return json.loads(json_data)


def test_techorezef_supplier_name(techorezef_data):
    """Tests if the supplier name is correct."""
    assert techorezef_data["supplier"] == "Techorezef"


def test_techorezef_supplier_prefix(techorezef_data):
    """Tests if the supplier prefix is correct."""
    assert techorezef_data["supplier_prefix"] == "TRZ-"

def test_techorezef_price_rule(techorezef_data):
    """Tests if the price rule is correct."""
    assert techorezef_data["price_rule"] == "1.4"
    
def test_techorezef_num_items_4_flush(techorezef_data):
    """Tests if the number of items for flush is correct."""
    assert techorezef_data["num_items_4_flush"] == 25

def test_techorezef_parcing_method(techorezef_data):
    """Tests if the parsing method is correct."""
    assert techorezef_data["parcing method [webdriver|api]"] == "web"


def test_techorezef_about_method(techorezef_data):
    """Tests if the 'about method' string is correct."""
    assert techorezef_data["about method web scrapping [webdriver|api]"] == "Если я работаю через API мне не нужен webdriver"


def test_techorezef_scenario_files_structure(techorezef_data):
    """Tests the structure of the scenario_files."""
    assert isinstance(techorezef_data["scenario_files"], list)
    assert all(isinstance(item, list) for item in techorezef_data["scenario_files"])
    
def test_techorezef_scenario_files_content(techorezef_data):
    """Tests the content of the scenario_files."""
    expected_files_first_group = ["visualdg_categories_cases_asus.json"]
    expected_files_second_group = ["visualdg_categories_desktops_lenovo_workstation_p.json"]
    
    assert techorezef_data["scenario_files"][0] == expected_files_first_group
    assert techorezef_data["scenario_files"][1] == expected_files_second_group
    assert len(techorezef_data["scenario_files"][2]) == 9



def test_techorezef_last_runned_scenario(techorezef_data):
    """Tests if the last run scenario is initialized as an empty string."""
    assert techorezef_data["last_runned_scenario"] == ""
```