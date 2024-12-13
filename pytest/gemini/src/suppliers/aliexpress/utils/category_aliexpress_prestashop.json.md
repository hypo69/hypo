```python
import pytest
import json

# Fixture definitions
@pytest.fixture
def category_data():
    """Provides test data for the category mapping."""
    return {
        "39": {
            "ali_category_name": "Lights & Lighting",
            "ali_parent": "",
            "PrestaShop_categories": [],
            "PrestaShop_main_category": ""
        },
        "1504": {
            "ali_category_name": "Indoor Lighting",
            "ali_parent": "39",
            "PrestaShop_categories": [],
            "PrestaShop_main_category": ""
        }
    }

@pytest.fixture
def category_data_with_prestashop():
    """Provides test data with PrestaShop categories."""
    return {
        "39": {
            "ali_category_name": "Lights & Lighting",
            "ali_parent": "",
            "PrestaShop_categories": ["10", "11"],
            "PrestaShop_main_category": "10"
        },
        "1504": {
            "ali_category_name": "Indoor Lighting",
            "ali_parent": "39",
            "PrestaShop_categories": ["20", "21"],
            "PrestaShop_main_category": "20"
        }
    }


def test_category_data_valid_structure(category_data):
    """
    Test if the category data has the expected structure.
    Checks for the existence of required keys and correct types.
    """
    for category_id, category_info in category_data.items():
        assert isinstance(category_id, str), "Category ID should be a string."
        assert isinstance(category_info, dict), "Category info should be a dictionary."
        assert "ali_category_name" in category_info, "Missing 'ali_category_name' key."
        assert "ali_parent" in category_info, "Missing 'ali_parent' key."
        assert "PrestaShop_categories" in category_info, "Missing 'PrestaShop_categories' key."
        assert "PrestaShop_main_category" in category_info, "Missing 'PrestaShop_main_category' key."
        assert isinstance(category_info["ali_category_name"], str), "'ali_category_name' should be a string."
        assert isinstance(category_info["ali_parent"], str), "'ali_parent' should be a string."
        assert isinstance(category_info["PrestaShop_categories"], list), "'PrestaShop_categories' should be a list."
        assert isinstance(category_info["PrestaShop_main_category"], str), "'PrestaShop_main_category' should be a string."



def test_category_data_empty_prestashop_categories(category_data):
    """
    Test if categories initially have empty PrestaShop categories.
    Verifies that 'PrestaShop_categories' is an empty list and main category is an empty string
    """
    for category_info in category_data.values():
         assert category_info["PrestaShop_categories"] == [], "'PrestaShop_categories' should be an empty list"
         assert category_info["PrestaShop_main_category"] == "", "'PrestaShop_main_category' should be an empty string"


def test_category_data_with_prestashop_categories(category_data_with_prestashop):
    """
    Test if the category data has correct PrestaShop categories.
    Checks that 'PrestaShop_categories' is a list with values and main category is a non empty string
    """
    for category_info in category_data_with_prestashop.values():
        assert isinstance(category_info["PrestaShop_categories"], list), "'PrestaShop_categories' should be a list."
        assert len(category_info["PrestaShop_categories"]) > 0, "'PrestaShop_categories' should have at least one value"
        assert isinstance(category_info["PrestaShop_main_category"], str), "'PrestaShop_main_category' should be a string."
        assert len(category_info["PrestaShop_main_category"]) > 0, "'PrestaShop_main_category' should not be empty"
        assert category_info["PrestaShop_main_category"] in category_info["PrestaShop_categories"] , "main category should be one of prestashop categories"


def test_category_data_ali_category_name_not_empty(category_data):
    """
    Test if ali_category_name is not empty for any category
    """
    for category_info in category_data.values():
        assert len(category_info["ali_category_name"]) > 0, "'ali_category_name' should not be empty"

def test_category_data_ali_parent_is_string(category_data):
    """
    Test if ali_parent is a string
    """
    for category_info in category_data.values():
        assert isinstance(category_info["ali_parent"], str), "'ali_parent' should be a string"

def test_category_data_parent_exists(category_data):
    """
    Test if ali_parent exists as a key, or empty string
    """
    category_ids = list(category_data.keys())
    for category_id, category_info in category_data.items():
        if category_info["ali_parent"] != "":
          assert category_info["ali_parent"] in category_ids, f"Parent '{category_info['ali_parent']}' does not exist in the category data."
```