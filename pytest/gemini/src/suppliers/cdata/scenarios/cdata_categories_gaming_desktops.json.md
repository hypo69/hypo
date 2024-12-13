```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def cdata_categories_gaming_desktops_data():
    """Loads the JSON data for testing."""
    file_path = 'hypotez/src/suppliers/cdata/scenarios/cdata_categories_gaming_desktops.json'
    with open(file_path, 'r') as f:
        return json.load(f)

def test_cdata_categories_gaming_desktops_data_structure(cdata_categories_gaming_desktops_data):
    """
    Test the overall structure of the loaded JSON data.
    Checks if the top level key is "scenarios" and that it's a dictionary.
    """
    assert "scenarios" in cdata_categories_gaming_desktops_data
    assert isinstance(cdata_categories_gaming_desktops_data["scenarios"], dict)

def test_cdata_categories_gaming_desktops_scenario_keys(cdata_categories_gaming_desktops_data):
    """
    Test that each scenario has the expected keys
    """
    expected_keys = {"brand", "url", "checkbox", "active", "condition","presta_categories"}
    for scenario_name, scenario_data in cdata_categories_gaming_desktops_data["scenarios"].items():
        assert set(scenario_data.keys()) == expected_keys

def test_cdata_categories_gaming_desktops_scenario_values(cdata_categories_gaming_desktops_data):
    """
    Test the values of the keys
    """
    for scenario_name, scenario_data in cdata_categories_gaming_desktops_data["scenarios"].items():
        assert isinstance(scenario_data["brand"], str)
        assert isinstance(scenario_data["url"], str)
        assert isinstance(scenario_data["checkbox"], bool)
        assert isinstance(scenario_data["active"], bool)
        assert isinstance(scenario_data["condition"], str)
        assert isinstance(scenario_data["presta_categories"], str)


def test_cdata_categories_gaming_desktops_brand_values(cdata_categories_gaming_desktops_data):
      """
    Test the brand values of the keys
    """
      allowed_brands = {"ASUS","DELL"}
      for scenario_name, scenario_data in cdata_categories_gaming_desktops_data["scenarios"].items():
        assert scenario_data["brand"] in allowed_brands

def test_cdata_categories_gaming_desktops_url_valid(cdata_categories_gaming_desktops_data):
    """
    Test that url values are valid or a placeholder.
    """
    for scenario_name, scenario_data in cdata_categories_gaming_desktops_data["scenarios"].items():
        url = scenario_data["url"]
        if not url.startswith("https://") and not "-------------------" in url:
           pytest.fail(f"Invalid URL format: {url}")

def test_cdata_categories_gaming_desktops_checkbox_values(cdata_categories_gaming_desktops_data):
    """
    Test that all checkbox values are false as expected.
    """
    for scenario_name, scenario_data in cdata_categories_gaming_desktops_data["scenarios"].items():
       assert scenario_data["checkbox"] == False

def test_cdata_categories_gaming_desktops_active_values(cdata_categories_gaming_desktops_data):
     """
    Test that all active values are true as expected.
    """
     for scenario_name, scenario_data in cdata_categories_gaming_desktops_data["scenarios"].items():
        assert scenario_data["active"] == True

def test_cdata_categories_gaming_desktops_condition_values(cdata_categories_gaming_desktops_data):
      """
      Test that all condition values are new as expected.
      """
      for scenario_name, scenario_data in cdata_categories_gaming_desktops_data["scenarios"].items():
        assert scenario_data["condition"] == "new"


def test_cdata_categories_gaming_desktops_presta_categories_format(cdata_categories_gaming_desktops_data):
    """
    Test that presta_categories values are strings of comma separated numbers.
    """
    for scenario_name, scenario_data in cdata_categories_gaming_desktops_data["scenarios"].items():
        presta_categories = scenario_data["presta_categories"]
        categories = presta_categories.split(',')
        for category in categories:
             assert category.isdigit()
```