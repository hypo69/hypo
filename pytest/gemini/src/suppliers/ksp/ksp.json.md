```python
import pytest
import json

# Fixture to load the ksp.json data
@pytest.fixture
def ksp_data():
    """Loads the ksp.json data for testing."""
    file_path = "hypotez/src/suppliers/ksp/ksp.json"
    with open(file_path, 'r') as f:
        return json.load(f)

def test_ksp_data_structure(ksp_data):
    """
    Test if the ksp.json data has the correct structure with required keys.
    """
    assert "supplier_id" in ksp_data
    assert "supplier" in ksp_data
    assert "supplier_prefix" in ksp_data
    assert "start_url" in ksp_data
    assert "price_rule" in ksp_data
    assert "scenario_files" in ksp_data
    assert "excluded" in ksp_data
    assert "last_runned_scenario" in ksp_data

def test_ksp_supplier_id_type(ksp_data):
    """
    Test if the 'supplier_id' is a string.
    """
    assert isinstance(ksp_data["supplier_id"], str)

def test_ksp_supplier_name_type(ksp_data):
    """
    Test if the 'supplier' is a string and equals to 'KSP'.
    """
    assert isinstance(ksp_data["supplier"], str)
    assert ksp_data["supplier"] == "KSP"

def test_ksp_supplier_prefix_type(ksp_data):
    """
    Test if the 'supplier_prefix' is a string and equals to 'ksp'.
    """
    assert isinstance(ksp_data["supplier_prefix"], str)
    assert ksp_data["supplier_prefix"] == "ksp"

def test_ksp_start_url_type(ksp_data):
    """
    Test if the 'start_url' is a string and a valid URL (basic check).
    """
    assert isinstance(ksp_data["start_url"], str)
    assert ksp_data["start_url"].startswith("https://")

def test_ksp_price_rule_type(ksp_data):
     """
     Test if 'price_rule' is a string and starts with '+'.
     """
     assert isinstance(ksp_data["price_rule"], str)
     assert ksp_data["price_rule"].startswith("+")

def test_ksp_scenario_files_type(ksp_data):
    """
    Test if 'scenario_files' is a list and contains strings.
    """
    assert isinstance(ksp_data["scenario_files"], list)
    for item in ksp_data["scenario_files"]:
        assert isinstance(item, str)

def test_ksp_excluded_type(ksp_data):
    """
    Test if 'excluded' is a list and contains strings.
    """
    assert isinstance(ksp_data["excluded"], list)
    for item in ksp_data["excluded"]:
        assert isinstance(item, str)


def test_ksp_last_runned_scenario_type(ksp_data):
    """
    Test if 'last_runned_scenario' is a string.
    """
    assert isinstance(ksp_data["last_runned_scenario"], str)


def test_ksp_scenario_files_not_empty(ksp_data):
    """
    Test if 'scenario_files' list is not empty.
    """
    assert len(ksp_data["scenario_files"]) > 0

def test_ksp_excluded_valid_values(ksp_data):
     """
    Test if each value in 'excluded' is present in 'scenario_files'.
     """
     for item in ksp_data["excluded"]:
        assert item in ksp_data["scenario_files"]
```