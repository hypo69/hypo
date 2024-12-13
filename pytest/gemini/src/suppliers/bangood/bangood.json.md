```python
import pytest
import json

# Fixture for loading the JSON data
@pytest.fixture
def bangood_data():
    """Loads the bangood.json data."""
    with open("hypotez/src/suppliers/bangood/bangood.json", "r") as f:
        return json.load(f)

def test_bangood_supplier_name(bangood_data):
    """Checks if the supplier name is 'ksp'."""
    assert bangood_data["supplier"] == "ksp"

def test_bangood_supplier_prefix(bangood_data):
    """Checks if the supplier prefix is 'ksp'."""
    assert bangood_data["supplier_prefix"] == "ksp"

def test_bangood_start_url(bangood_data):
    """Checks if the start URL is a valid URL string."""
    assert isinstance(bangood_data["start_url"], str)
    assert bangood_data["start_url"].startswith("https://")

def test_bangood_price_rule(bangood_data):
    """Checks if the price rule is a valid string representing a price adjustment rule."""
    assert isinstance(bangood_data["price_rule"], str)
    # Basic check that the price rule starts with '+' or '-'
    assert bangood_data["price_rule"][0] in ('+', '-') 

def test_bangood_num_items_4_flush(bangood_data):
    """Checks if the number of items for flush is an integer greater than 0."""
    assert isinstance(bangood_data["num_items_4_flush"], int)
    assert bangood_data["num_items_4_flush"] > 0
    
def test_bangood_if_login(bangood_data):
    """Checks if the if_login value is a boolean."""
    assert isinstance(bangood_data["if_login"], bool)

def test_bangood_parcing_method(bangood_data):
    """Checks if the parsing method is a valid string, either 'web' or 'api'."""
    assert bangood_data["parcing method [webdriver|api]"] in ["web", "api"]

def test_bangood_about_method_web_scrapping(bangood_data):
    """
    Checks if the about method web scrapping message is a string. 
    This checks the message but not the specific content of the string
    """
    assert isinstance(bangood_data["about method web scrapping [webdriver|api]"], str)
    
def test_bangood_collect_products_from_categorypage(bangood_data):
     """Checks if the collect_products_from_categorypage value is a boolean."""
     assert isinstance(bangood_data["collect_products_from_categorypage"], bool)
     
def test_bangood_scenario_files(bangood_data):
    """Checks if scenario_files is a list and all items are strings ending with '.json'."""
    assert isinstance(bangood_data["scenario_files"], list)
    for file in bangood_data["scenario_files"]:
        assert isinstance(file, str)
        assert file.endswith(".json")

def test_bangood_excluded(bangood_data):
    """Checks if excluded is a list and all items are strings ending with '.json'."""
    assert isinstance(bangood_data["excluded"], list)
    for file in bangood_data["excluded"]:
        assert isinstance(file, str)
        assert file.endswith(".json")

def test_bangood_last_runned_scenario(bangood_data):
    """Checks if last_runned_scenario is a string."""
    assert isinstance(bangood_data["last_runned_scenario"], str)
```