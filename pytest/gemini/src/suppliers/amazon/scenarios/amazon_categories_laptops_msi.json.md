```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def amazon_msi_data():
    """Provides the JSON data for testing."""
    file_path = "hypotez/src/suppliers/amazon/scenarios/amazon_categories_laptops_msi.json"
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def test_store_data_structure(amazon_msi_data):
    """Checks if the store data structure exists and has expected keys."""
    assert "store" in amazon_msi_data
    store_data = amazon_msi_data["store"]
    assert "store_id" in store_data
    assert "supplier_id" in store_data
    assert "get store banners" in store_data
    assert "description" in store_data
    assert "about" in store_data
    assert "url" in store_data
    assert "shop categories page" in store_data
    assert "shop categories json file" in store_data
  
def test_store_data_values(amazon_msi_data):
    """Checks if the store data has the correct values."""
    store_data = amazon_msi_data["store"]
    assert store_data["description"] == "MSI laptops"
    assert store_data["about"] == "MSI laptops"
    assert store_data["url"] == "https://www.amazon.com/s?i=computers&bbn=565108&rh=n%3A565108%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3AMSI&dc&qid=1671862898&rnid=2528832011&ref=sr_nr_p_89_1&ds=v1%3AhdSOut1PjzMfOVMzl3Wtwm9ko620wPQFrd1UeaDZfzU"
    assert store_data["get store banners"] == True


def test_scenarios_data_structure(amazon_msi_data):
    """Checks if the scenarios data structure exists and has the expected keys."""
    assert "scenarios" in amazon_msi_data
    scenarios_data = amazon_msi_data["scenarios"]
    assert "Apple Wathes" in scenarios_data
    apple_watches_data = scenarios_data["Apple Wathes"]
    assert "url" in apple_watches_data
    assert "active" in apple_watches_data
    assert "condition" in apple_watches_data
    assert "presta_categories" in apple_watches_data
    assert "checkbox" in apple_watches_data
    assert "price_rule" in apple_watches_data
    
def test_scenarios_data_values(amazon_msi_data):
    """Checks if the scenarios data has the correct values"""
    scenarios_data = amazon_msi_data["scenarios"]
    apple_watches_data = scenarios_data["Apple Wathes"]
    assert apple_watches_data["url"] == "https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A2811119011%2Cn%3A2407755011%2Cn%3A7939902011%2Cp_n_is_free_shipping%3A10236242011%2Cp_89%3AApple&dc&ds=v1%3AyDxGiVC9lCk%2BzGvhkah6ZCjaellz7FcqKtRIfFA3o2A&qid=1671818889&rnid=2407755011&ref=sr_nr_n_2"
    assert apple_watches_data["active"] == True
    assert apple_watches_data["condition"] == "new"
    assert apple_watches_data["checkbox"] == False
    assert apple_watches_data["price_rule"] == 1
    assert apple_watches_data["presta_categories"]["template"]["apple"] == "WATCHES"


def test_missing_data(amazon_msi_data):
     """Checks the behavior when store or scenarios is missing"""
     with pytest.raises(KeyError):
        del amazon_msi_data['store']
        test_store_data_structure(amazon_msi_data)
     with pytest.raises(KeyError):
        del amazon_msi_data['scenarios']
        test_scenarios_data_structure(amazon_msi_data)
```