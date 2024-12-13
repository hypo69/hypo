```python
import pytest
import json

# Fixture definitions, if needed
@pytest.fixture
def ksp_categories_watches_xiaomi_data():
    """Provides test data for the ksp_categories_watches_xiaomi.json file."""
    return {
        "scenarios": {
            "Xiaomi Redmi Watch": {
                "brand": "XIAOMI",
                "url": "https://ksp.co.il/web/cat/2085..2202..34255",
                "checkbox": False,
                "active": True,
                "condition": "new",
                "presta_categories": {
                    "3405": "GOOGLE PIXEL PRO",
                    "3198": "CONSUMER ELECTRONICS",
                    "3202": "computer,smartphone,gaming console,smart device",
                    "6471": "Smartphones",
                    "3403": "GOOGLE"
                }
            },
            "Xiaomi Mi Watch": {
                "brand": "XIAOMI",
                "url": "https://ksp.co.il/web/cat/2085..2202..29146..29145",
                "checkbox": False,
                "active": True,
                "condition": "new",
                "presta_categories": {
                    "3405": "GOOGLE PIXEL PRO",
                    "3198": "CONSUMER ELECTRONICS",
                    "3202": "computer,smartphone,gaming console,smart device",
                    "6471": "Smartphones",
                    "3403": "GOOGLE"
                }
            }
        }
    }


def test_ksp_categories_watches_xiaomi_valid_structure(ksp_categories_watches_xiaomi_data):
    """Checks if the loaded JSON data has the expected 'scenarios' key."""
    assert "scenarios" in ksp_categories_watches_xiaomi_data, "The 'scenarios' key is missing."

def test_ksp_categories_watches_xiaomi_scenarios_not_empty(ksp_categories_watches_xiaomi_data):
    """Checks if the 'scenarios' dictionary is not empty."""
    assert ksp_categories_watches_xiaomi_data["scenarios"], "The 'scenarios' dictionary is empty."


def test_ksp_categories_watches_xiaomi_scenario_keys(ksp_categories_watches_xiaomi_data):
    """Checks if each scenario has the expected keys."""
    for scenario_name, scenario_data in ksp_categories_watches_xiaomi_data["scenarios"].items():
        assert "brand" in scenario_data, f"The 'brand' key is missing in scenario: {scenario_name}"
        assert "url" in scenario_data, f"The 'url' key is missing in scenario: {scenario_name}"
        assert "checkbox" in scenario_data, f"The 'checkbox' key is missing in scenario: {scenario_name}"
        assert "active" in scenario_data, f"The 'active' key is missing in scenario: {scenario_name}"
        assert "condition" in scenario_data, f"The 'condition' key is missing in scenario: {scenario_name}"
        assert "presta_categories" in scenario_data, f"The 'presta_categories' key is missing in scenario: {scenario_name}"


def test_ksp_categories_watches_xiaomi_scenario_brand_value(ksp_categories_watches_xiaomi_data):
  """Checks if the brand is 'XIAOMI' for both scenarios."""
  for scenario_name, scenario_data in ksp_categories_watches_xiaomi_data["scenarios"].items():
    assert scenario_data["brand"] == "XIAOMI", f"The 'brand' key is not 'XIAOMI' in scenario: {scenario_name}"

def test_ksp_categories_watches_xiaomi_scenario_checkbox_value(ksp_categories_watches_xiaomi_data):
  """Checks if the checkbox is False for both scenarios."""
  for scenario_name, scenario_data in ksp_categories_watches_xiaomi_data["scenarios"].items():
    assert scenario_data["checkbox"] == False, f"The 'checkbox' key is not False in scenario: {scenario_name}"


def test_ksp_categories_watches_xiaomi_scenario_active_value(ksp_categories_watches_xiaomi_data):
  """Checks if the active is True for both scenarios."""
  for scenario_name, scenario_data in ksp_categories_watches_xiaomi_data["scenarios"].items():
    assert scenario_data["active"] == True, f"The 'active' key is not True in scenario: {scenario_name}"

def test_ksp_categories_watches_xiaomi_scenario_condition_value(ksp_categories_watches_xiaomi_data):
  """Checks if the condition is 'new' for both scenarios."""
  for scenario_name, scenario_data in ksp_categories_watches_xiaomi_data["scenarios"].items():
    assert scenario_data["condition"] == "new", f"The 'condition' key is not 'new' in scenario: {scenario_name}"


def test_ksp_categories_watches_xiaomi_scenario_presta_categories_not_empty(ksp_categories_watches_xiaomi_data):
    """Checks if the 'presta_categories' dictionary is not empty."""
    for scenario_name, scenario_data in ksp_categories_watches_xiaomi_data["scenarios"].items():
        assert scenario_data["presta_categories"], f"The 'presta_categories' dictionary is empty in scenario: {scenario_name}"

def test_ksp_categories_watches_xiaomi_scenario_presta_categories_keys(ksp_categories_watches_xiaomi_data):
    """Checks if each presta_category has the expected keys."""
    for scenario_name, scenario_data in ksp_categories_watches_xiaomi_data["scenarios"].items():
        presta_categories = scenario_data["presta_categories"]
        assert "3405" in presta_categories, f"'3405' key missing in 'presta_categories' for scenario: {scenario_name}"
        assert "3198" in presta_categories, f"'3198' key missing in 'presta_categories' for scenario: {scenario_name}"
        assert "3202" in presta_categories, f"'3202' key missing in 'presta_categories' for scenario: {scenario_name}"
        assert "6471" in presta_categories, f"'6471' key missing in 'presta_categories' for scenario: {scenario_name}"
        assert "3403" in presta_categories, f"'3403' key missing in 'presta_categories' for scenario: {scenario_name}"


def test_ksp_categories_watches_xiaomi_scenario_presta_categories_values(ksp_categories_watches_xiaomi_data):
    """Checks if each presta_category has the expected values."""
    for scenario_name, scenario_data in ksp_categories_watches_xiaomi_data["scenarios"].items():
        presta_categories = scenario_data["presta_categories"]
        assert presta_categories["3405"] == "GOOGLE PIXEL PRO", f"'3405' value is incorrect in 'presta_categories' for scenario: {scenario_name}"
        assert presta_categories["3198"] == "CONSUMER ELECTRONICS", f"'3198' value is incorrect in 'presta_categories' for scenario: {scenario_name}"
        assert presta_categories["3202"] == "computer,smartphone,gaming console,smart device", f"'3202' value is incorrect in 'presta_categories' for scenario: {scenario_name}"
        assert presta_categories["6471"] == "Smartphones", f"'6471' value is incorrect in 'presta_categories' for scenario: {scenario_name}"
        assert presta_categories["3403"] == "GOOGLE", f"'3403' value is incorrect in 'presta_categories' for scenario: {scenario_name}"

def test_ksp_categories_watches_xiaomi_url_format(ksp_categories_watches_xiaomi_data):
    """Checks if the url is in the correct format"""
    for scenario_name, scenario_data in ksp_categories_watches_xiaomi_data["scenarios"].items():
      url = scenario_data["url"]
      assert url.startswith("https://"), f"URL does not start with 'https://' in scenario: {scenario_name}"
      assert "ksp.co.il" in url, f"URL does not contain 'ksp.co.il' in scenario: {scenario_name}"
      assert "web/cat/" in url, f"URL does not contain 'web/cat/' in scenario: {scenario_name}"
      assert url.count("..") >= 2 , f"URL does not have correct format in scenario: {scenario_name}"
```