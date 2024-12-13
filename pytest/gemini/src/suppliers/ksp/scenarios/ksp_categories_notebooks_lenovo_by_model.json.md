```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ksp_data():
    """Loads the JSON data from the file."""
    file_path = "hypotez/src/suppliers/ksp/scenarios/ksp_categories_notebooks_lenovo_by_model.json"
    with open(file_path, 'r') as f:
        return json.load(f)

# Test case for valid data loading
def test_data_loading(ksp_data):
    """Checks if the JSON data is loaded correctly."""
    assert isinstance(ksp_data, dict)
    assert "scenarios" in ksp_data
    assert isinstance(ksp_data["scenarios"], dict)
    assert len(ksp_data["scenarios"]) > 0

# Test case for a specific model's data
def test_specific_model_data(ksp_data):
    """Checks if the data for a specific model is correct."""
    model_name = "IdeaPad 4"
    assert model_name in ksp_data["scenarios"]
    model_data = ksp_data["scenarios"][model_name]
    assert model_data["brand"] == "LENOVO"
    assert model_data["url"] == "https://ksp.co.il/web/cat/268..271..159..29040"
    assert model_data["checkbox"] == False
    assert model_data["active"] == True
    assert model_data["condition"] == "new"
    assert "presta_categories" in model_data
    assert isinstance(model_data["presta_categories"], dict)

# Test case for a different model's data
def test_another_model_data(ksp_data):
    """Checks data for a different model."""
    model_name = "Legion 7"
    assert model_name in ksp_data["scenarios"]
    model_data = ksp_data["scenarios"][model_name]
    assert model_data["brand"] == "LENOVO"
    assert model_data["url"] == "https://ksp.co.il/web/cat/159..268..271..29352"
    assert model_data["checkbox"] == False
    assert model_data["active"] == True
    assert model_data["condition"] == "new"
    assert "presta_categories" in model_data
    assert isinstance(model_data["presta_categories"], dict)

# Test case for all model's brand
def test_all_models_brand(ksp_data):
    """Checks if all models have the correct brand."""
    for model_name, model_data in ksp_data["scenarios"].items():
        assert model_data["brand"] == "LENOVO"


# Test case for all model's active status
def test_all_models_active_status(ksp_data):
    """Checks if all models have active status set to True."""
    for model_name, model_data in ksp_data["scenarios"].items():
      assert model_data["active"] == True

# Test case for all model's checkbox status
def test_all_models_checkbox_status(ksp_data):
    """Checks if all models have checkbox set to False."""
    for model_name, model_data in ksp_data["scenarios"].items():
      assert model_data["checkbox"] == False

# Test case for all model's condition status
def test_all_models_condition_status(ksp_data):
    """Checks if all models have condition set to new."""
    for model_name, model_data in ksp_data["scenarios"].items():
      assert model_data["condition"] == "new"
# Test case for all model's presta_categories
def test_all_models_presta_categories(ksp_data):
    """Checks if all models have presta_categories."""
    for model_name, model_data in ksp_data["scenarios"].items():
        assert "presta_categories" in model_data
        assert isinstance(model_data["presta_categories"], dict)
        assert len(model_data["presta_categories"]) > 0

# Test case for missing file (edge case)
def test_missing_file():
    """Checks exception is raised when file not found"""
    file_path = "non_existent_file.json"
    with pytest.raises(FileNotFoundError):
         with open(file_path, 'r') as f:
             json.load(f)
```