```python
import pytest
import json

# Fixture to load the brands data from the JSON file
@pytest.fixture
def brands_data():
    """Loads brand data from the json file."""
    with open("hypotez/src/scenario/json/brands.json", "r") as f:
        return json.load(f)

# Test cases for valid inputs
def test_brand_exists(brands_data):
    """Checks if a brand exists in the data."""
    assert "ACER" in brands_data["brand"]
    assert "APPLE" in brands_data["brand"]
    assert "ZALMAN" in brands_data["brand"]
    assert "NON_EXISTENT_BRAND" not in brands_data["brand"]

def test_brand_active_status(brands_data):
    """Checks if a brand's 'active' status is correct."""
    assert brands_data["brand"]["ACER"]["active"] == True
    assert brands_data["brand"]["AMD"]["active"] == True
    assert brands_data["brand"]["ZALMAN"]["active"] == True


def test_brand_condition(brands_data):
    """Checks if a brand's 'condition' is correct."""
    assert brands_data["brand"]["ACER"]["condition"] == "new"
    assert brands_data["brand"]["AMD"]["condition"] == "new"
    assert brands_data["brand"]["ZALMAN"]["condition"] == "new"


def test_brand_presta_categories(brands_data):
    """Checks if a brand's 'presta_categories' is correct."""
    assert brands_data["brand"]["ACER"]["presta_categories"] == 24
    assert brands_data["brand"]["AMD"]["presta_categories"] == 9
    assert brands_data["brand"]["ZALMAN"]["presta_categories"] == 31


# Test cases for edge cases
def test_brand_empty_data():
    """Checks behavior with an empty JSON object."""
    empty_data = {"brand": {}}
    assert not empty_data["brand"]

def test_brand_special_characters_brand_name(brands_data):
    """Checks brands with special characters in the name. Test case for AOURUS BY GIGABYTE"""
    assert "AOURUS BY GIGABYTE" in brands_data["brand"]
    assert brands_data["brand"]["AOURUS BY GIGABYTE"]["active"] == True
    assert brands_data["brand"]["AOURUS BY GIGABYTE"]["condition"] == "new"
    assert brands_data["brand"]["AOURUS BY GIGABYTE"]["presta_categories"] == 33

def test_brand_WD_and_WESTERN_DIGITAL(brands_data):
    """Checks the 'WD' and 'WESTERN DIGITAL' brands since they have the same presta_categories."""
    assert brands_data["brand"]["WD"]["presta_categories"] == brands_data["brand"]["WESTERN DIGITAL"]["presta_categories"]
    assert brands_data["brand"]["WD"]["presta_categories"] == 30


# Test cases for invalid/unexpected input

def test_brand_missing_keys(brands_data):
    """Checks if missing keys from the brand raises a key error."""
    with pytest.raises(KeyError):
       brands_data["brand"]["ACER"]["non_existent_key"]

def test_brand_invalid_type(brands_data):
    """Checks if value has the wrong type"""
    with pytest.raises(TypeError):
      brands_data["brand"]["ACER"]["active"] = 1
    with pytest.raises(TypeError):
       brands_data["brand"]["ACER"]["condition"] = 1
    with pytest.raises(TypeError):
        brands_data["brand"]["ACER"]["presta_categories"] = "a"
```