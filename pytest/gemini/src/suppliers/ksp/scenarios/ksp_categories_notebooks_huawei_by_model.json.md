```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_categories_data():
    """Loads the JSON data from the specified file."""
    file_path = "hypotez/src/suppliers/ksp/scenarios/ksp_categories_notebooks_huawei_by_model.json"
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def test_ksp_categories_data_structure(ksp_categories_data):
    """Checks if the loaded JSON data has the expected structure."""
    assert "scenarios" in ksp_categories_data, "The 'scenarios' key is missing in the JSON data."
    assert isinstance(ksp_categories_data["scenarios"], dict), "The 'scenarios' value should be a dictionary."
    
    # Check if each scenario has the expected keys
    for model, details in ksp_categories_data["scenarios"].items():
        assert "brand" in details, f"The 'brand' key is missing for model: {model}."
        assert "url" in details, f"The 'url' key is missing for model: {model}."
        assert "checkbox" in details, f"The 'checkbox' key is missing for model: {model}."
        assert "active" in details, f"The 'active' key is missing for model: {model}."
        assert "condition" in details, f"The 'condition' key is missing for model: {model}."
        assert "presta_categories" in details, f"The 'presta_categories' key is missing for model: {model}."
        assert isinstance(details["presta_categories"], dict), f"The 'presta_categories' value should be a dictionary for model: {model}."

def test_ksp_categories_data_values(ksp_categories_data):
    """Checks if specific values within the data are correct based on the expected structure and data provided."""
    
    # Test specific model's values
    matebook_14_data = ksp_categories_data["scenarios"]["Huawei MateBook 14"]
    assert matebook_14_data["brand"] == "HUAWEI", "Incorrect brand value for Huawei MateBook 14."
    assert matebook_14_data["url"] == "https://ksp.co.il/web/cat/268..271..583..31024", "Incorrect URL value for Huawei MateBook 14."
    assert matebook_14_data["checkbox"] == False, "Incorrect checkbox value for Huawei MateBook 14."
    assert matebook_14_data["active"] == True, "Incorrect active value for Huawei MateBook 14."
    assert matebook_14_data["condition"] == "new", "Incorrect condition value for Huawei MateBook 14."
    
    assert "3405" in matebook_14_data["presta_categories"], "Missing presta_categories for Huawei MateBook 14."
    assert matebook_14_data["presta_categories"]["3405"] == "GOOGLE PIXEL PRO", "Incorrect value for presta_categories '3405' for Huawei MateBook 14."

    # Test another specific model's values
    matebook_d14_data = ksp_categories_data["scenarios"]["Huawei Matebook D14"]
    assert matebook_d14_data["brand"] == "HUAWEI", "Incorrect brand value for Huawei Matebook D14."
    assert matebook_d14_data["url"] == "https://ksp.co.il/web/cat/268..271..583..23286", "Incorrect URL value for Huawei Matebook D14."
    assert matebook_d14_data["checkbox"] == False, "Incorrect checkbox value for Huawei Matebook D14."
    assert matebook_d14_data["active"] == True, "Incorrect active value for Huawei Matebook D14."
    assert matebook_d14_data["condition"] == "new", "Incorrect condition value for Huawei Matebook D14."
    
    assert "3405" in matebook_d14_data["presta_categories"], "Missing presta_categories for Huawei Matebook D14."
    assert matebook_d14_data["presta_categories"]["3405"] == "GOOGLE PIXEL PRO", "Incorrect value for presta_categories '3405' for Huawei Matebook D14."

def test_ksp_categories_data_empty_scenarios(ksp_categories_data):
    """Checks the scenario where the 'scenarios' dictionary is empty."""
    empty_data = {"scenarios": {}}
    assert "scenarios" in empty_data
    assert isinstance(empty_data["scenarios"], dict)
    assert len(empty_data["scenarios"]) == 0
    
def test_ksp_categories_data_missing_scenarios_key():
     """Checks for the case when the 'scenarios' key is missing."""
     missing_data = {}
     assert "scenarios" not in missing_data
    
def test_ksp_categories_data_invalid_scenarios_type():
    """Checks the scenario where the 'scenarios' value is not a dictionary."""
    invalid_data = {"scenarios": "not_a_dict"}
    assert "scenarios" in invalid_data
    assert not isinstance(invalid_data["scenarios"], dict)
    
def test_ksp_categories_data_missing_model_keys(ksp_categories_data):
    """Tests for a missing key inside of a model object"""
    modified_data = ksp_categories_data.copy()
    del modified_data["scenarios"]["Huawei MateBook 14"]["brand"]
    with pytest.raises(AssertionError):
       test_ksp_categories_data_structure(modified_data)
```