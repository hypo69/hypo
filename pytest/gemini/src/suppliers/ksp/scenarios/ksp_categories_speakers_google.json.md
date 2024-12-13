```python
import pytest
import json

# Fixture for loading the JSON data
@pytest.fixture
def ksp_data():
    """Loads the JSON data from the file."""
    file_location = 'hypotez/src/suppliers/ksp/scenarios/ksp_categories_speakers_google.json'
    with open(file_location, 'r') as f:
        return json.load(f)

def test_ksp_data_structure(ksp_data):
    """Checks if the loaded JSON data has the expected structure."""
    assert "scenarios" in ksp_data
    assert isinstance(ksp_data["scenarios"], dict)
    assert "Google Nest" in ksp_data["scenarios"]

def test_google_nest_data_structure(ksp_data):
    """Checks the structure of the 'Google Nest' scenario data."""
    google_nest_data = ksp_data["scenarios"]["Google Nest"]
    assert "brand" in google_nest_data
    assert "url" in google_nest_data
    assert "checkbox" in google_nest_data
    assert "active" in google_nest_data
    assert "condition" in google_nest_data
    assert "presta_categories" in google_nest_data
    assert isinstance(google_nest_data["presta_categories"], dict)


def test_google_nest_brand(ksp_data):
     """Checks if the brand is correct"""
     google_nest_data = ksp_data["scenarios"]["Google Nest"]
     assert google_nest_data["brand"] == "GOOGLE"

def test_google_nest_url(ksp_data):
    """Checks the url is correct"""
    google_nest_data = ksp_data["scenarios"]["Google Nest"]
    assert google_nest_data["url"] == "https://ksp.co.il/web/cat/1309..3887"
    
def test_google_nest_checkbox(ksp_data):
    """Checks if the checkbox is False"""
    google_nest_data = ksp_data["scenarios"]["Google Nest"]
    assert google_nest_data["checkbox"] is False

def test_google_nest_active(ksp_data):
    """Checks if active is True"""
    google_nest_data = ksp_data["scenarios"]["Google Nest"]
    assert google_nest_data["active"] is True
    
def test_google_nest_condition(ksp_data):
    """Checks if the condition is 'new' """
    google_nest_data = ksp_data["scenarios"]["Google Nest"]
    assert google_nest_data["condition"] == "new"

def test_google_nest_presta_categories_not_empty(ksp_data):
    """Checks if presta_categories dict is not empty."""
    google_nest_data = ksp_data["scenarios"]["Google Nest"]
    assert google_nest_data["presta_categories"]

def test_google_nest_presta_categories_contains_expected_keys(ksp_data):
    """Checks if presta_categories dictionary contains expected keys."""
    google_nest_data = ksp_data["scenarios"]["Google Nest"]
    expected_keys = ["3496", "3198", "3433", "3436", "3492", "2256", "1026"]
    for key in expected_keys:
        assert key in google_nest_data["presta_categories"]
    

def test_google_nest_presta_categories_values_are_strings(ksp_data):
    """Checks if values in presta_categories are strings."""
    google_nest_data = ksp_data["scenarios"]["Google Nest"]
    for value in google_nest_data["presta_categories"].values():
         assert isinstance(value, str)


def test_ksp_data_invalid_file():
    """Checks exception is raised when file not exists"""
    with pytest.raises(FileNotFoundError):
        with open("non_existent_file.json", 'r') as f:
            json.load(f)
```