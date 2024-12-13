```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def kualastyle_data():
    """Loads the kualastyle.json data."""
    return {
        "supplier": "kualastyle",
        "supplier_id": "11028",
        "supplier_prefix": "kualastyle",
        "start_url": "https://kualastyle.com",
        "login_url": "https://kualastyle.com",
        "if_login": True,
        "price_rule": "*1",
        "if_list":"first",
        "use_mouse": False,
        "id_category_default": 11036,
        "compare_categorie_dict": True,
        "collect_products_from_categorypage": False,
        "scenario_files": ["bedroom.json"],
        "last_runned_scenario": "",
        "excluded": [
            "bedroom.json",
            "bathroom.json",
            "livingroom.json",
            "kualastyle_categories_accessories.json",
            "kualastyle_categories_appliances.json",
            "kualastyle_categories_carpets.json",
            "kualastyle_categories_children_and_youth.json",
            "kualastyle_categories_furniture.json",
            "kualastyle_categories_lighting.json",
            "kualastyle_categories_mattresses.json",
            "kualastyle_categories_mirrors.json",
            "kualastyle_categories_photos.json",
            "kualastyle_categories_textile.json",
        ],
    }


def test_kualastyle_supplier_name(kualastyle_data):
    """Tests if the supplier name is correct."""
    assert kualastyle_data["supplier"] == "kualastyle"

def test_kualastyle_supplier_id(kualastyle_data):
    """Tests if the supplier ID is correct."""
    assert kualastyle_data["supplier_id"] == "11028"

def test_kualastyle_supplier_prefix(kualastyle_data):
    """Tests if the supplier prefix is correct."""
    assert kualastyle_data["supplier_prefix"] == "kualastyle"


def test_kualastyle_start_url(kualastyle_data):
    """Tests if the start URL is correct."""
    assert kualastyle_data["start_url"] == "https://kualastyle.com"


def test_kualastyle_login_url(kualastyle_data):
     """Tests if the login URL is correct."""
     assert kualastyle_data["login_url"] == "https://kualastyle.com"

def test_kualastyle_if_login(kualastyle_data):
    """Tests if the if_login flag is set correctly."""
    assert kualastyle_data["if_login"] is True

def test_kualastyle_price_rule(kualastyle_data):
    """Tests if the price rule is correct."""
    assert kualastyle_data["price_rule"] == "*1"

def test_kualastyle_if_list(kualastyle_data):
    """Tests if the if_list is correct."""
    assert kualastyle_data["if_list"] == "first"

def test_kualastyle_use_mouse(kualastyle_data):
    """Tests if the use_mouse flag is set correctly."""
    assert kualastyle_data["use_mouse"] is False

def test_kualastyle_id_category_default(kualastyle_data):
    """Tests if the default category ID is correct."""
    assert kualastyle_data["id_category_default"] == 11036

def test_kualastyle_compare_categorie_dict(kualastyle_data):
    """Tests if the compare category dictionary flag is set correctly."""
    assert kualastyle_data["compare_categorie_dict"] is True

def test_kualastyle_collect_products_from_categorypage(kualastyle_data):
    """Tests if the collect products from category page flag is set correctly."""
    assert kualastyle_data["collect_products_from_categorypage"] is False

def test_kualastyle_scenario_files(kualastyle_data):
    """Tests if the scenario files are correct."""
    assert kualastyle_data["scenario_files"] == ["bedroom.json"]

def test_kualastyle_last_runned_scenario(kualastyle_data):
    """Tests if the last run scenario is correct"""
    assert kualastyle_data["last_runned_scenario"] == ""

def test_kualastyle_excluded_categories(kualastyle_data):
    """Tests if the excluded categories list is correct."""
    expected_excluded = [
        "bedroom.json",
        "bathroom.json",
        "livingroom.json",
        "kualastyle_categories_accessories.json",
        "kualastyle_categories_appliances.json",
        "kualastyle_categories_carpets.json",
        "kualastyle_categories_children_and_youth.json",
        "kualastyle_categories_furniture.json",
        "kualastyle_categories_lighting.json",
        "kualastyle_categories_mattresses.json",
        "kualastyle_categories_mirrors.json",
        "kualastyle_categories_photos.json",
        "kualastyle_categories_textile.json",
    ]
    assert kualastyle_data["excluded"] == expected_excluded


def test_kualastyle_data_type(kualastyle_data):
    """Tests if the loaded data is a dictionary."""
    assert isinstance(kualastyle_data, dict)

def test_kualastyle_data_not_empty(kualastyle_data):
    """Tests if the loaded data is not empty."""
    assert kualastyle_data

def test_kualastyle_missing_key():
     """Tests if the missing key will raise KeyError"""
     data = {
        "supplier": "kualastyle",
        "supplier_id": "11028",
    }
     with pytest.raises(KeyError):
        data["start_url"]
```