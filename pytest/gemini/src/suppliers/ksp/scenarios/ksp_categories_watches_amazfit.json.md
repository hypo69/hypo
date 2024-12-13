```python
import pytest
import json

# Fixture to load the JSON data from the specified file location
@pytest.fixture
def ksp_data():
    file_location = "hypotez/src/suppliers/ksp/scenarios/ksp_categories_watches_amazfit.json"
    with open(file_location, 'r') as f:
        return json.load(f)


def test_ksp_data_structure(ksp_data):
    """
    Checks that the loaded JSON has the expected structure (dictionary with a "scenarios" key).
    """
    assert isinstance(ksp_data, dict), "Data should be a dictionary"
    assert "scenarios" in ksp_data, "Data should contain a 'scenarios' key"


def test_ksp_scenario_exists(ksp_data):
    """
    Checks that the 'AMAZFIT' scenario exists within the 'scenarios' dictionary.
    """
    assert "AMAZFIT" in ksp_data["scenarios"], "The 'AMAZFIT' scenario should exist"


def test_ksp_scenario_brand_value(ksp_data):
    """
    Checks if the 'brand' key in the 'AMAZFIT' scenario is set to 'AMAZFIT'.
    """
    assert ksp_data["scenarios"]["AMAZFIT"]["brand"] == "AMAZFIT", "The brand should be 'AMAZFIT'"


def test_ksp_scenario_url_value(ksp_data):
    """
    Checks if the 'url' key in the 'AMAZFIT' scenario is correct.
    """
    expected_url = "https://ksp.co.il/web/cat/2085..14295"
    assert ksp_data["scenarios"]["AMAZFIT"]["url"] == expected_url, "The url should match the expected value"

def test_ksp_scenario_checkbox_value(ksp_data):
    """
    Checks if the 'checkbox' key in the 'AMAZFIT' scenario is set to False.
    """
    assert ksp_data["scenarios"]["AMAZFIT"]["checkbox"] == False, "The checkbox should be False"

def test_ksp_scenario_active_value(ksp_data):
    """
    Checks if the 'active' key in the 'AMAZFIT' scenario is set to True.
    """
    assert ksp_data["scenarios"]["AMAZFIT"]["active"] == True, "The 'active' should be True"

def test_ksp_scenario_condition_value(ksp_data):
     """
    Checks if the 'condition' key in the 'AMAZFIT' scenario is set to "new".
    """
     assert ksp_data["scenarios"]["AMAZFIT"]["condition"] == "new", "The condition should be new"

def test_ksp_scenario_presta_categories_exists(ksp_data):
    """
    Checks that the 'presta_categories' key exists within the 'AMAZFIT' scenario.
    """
    assert "presta_categories" in ksp_data["scenarios"]["AMAZFIT"], "presta_categories should exist"

def test_ksp_scenario_presta_categories_is_dict(ksp_data):
      """
     Checks if the 'presta_categories' key in the 'AMAZFIT' scenario is a dictionary.
     """
      assert isinstance(ksp_data["scenarios"]["AMAZFIT"]["presta_categories"], dict), "presta_categories should be a dictionary"


def test_ksp_scenario_presta_categories_values(ksp_data):
    """
    Checks a few values inside the presta_categories dictionary to ensure they are correct.
    """
    presta_categories = ksp_data["scenarios"]["AMAZFIT"]["presta_categories"]
    assert "3405" in presta_categories and presta_categories["3405"] == "GOOGLE PIXEL PRO" , "presta category key 3405 should exist and match value"
    assert "3198" in presta_categories and presta_categories["3198"] == "CONSUMER ELECTRONICS", "presta category key 3198 should exist and match value"
    assert "3202" in presta_categories and presta_categories["3202"] == "computer,smartphone,gaming console,smart device", "presta category key 3202 should exist and match value"
    assert "6471" in presta_categories and presta_categories["6471"] == "Smartphones", "presta category key 6471 should exist and match value"
    assert "3403" in presta_categories and presta_categories["3403"] == "GOOGLE", "presta category key 3403 should exist and match value"
```