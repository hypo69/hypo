```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def amazon_asus_data():
    """Loads the amazon_stores_asus.json data."""
    file_path = "hypotez/src/suppliers/amazon/scenarios/amazon_stores_asus.json"
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Tests for the 'store' section
def test_store_id_is_uuid(amazon_asus_data):
    """Checks if store_id is a valid UUID format."""
    store_id = amazon_asus_data['store']['store_id']
    # Basic check, can be improved with regex or UUID library validation
    assert isinstance(store_id, str) and len(store_id) == 36, "store_id is not a valid UUID"

def test_store_supplier_id_is_int(amazon_asus_data):
    """Checks if supplier_id is an integer."""
    supplier_id = amazon_asus_data['store']['supplier_id']
    assert isinstance(supplier_id, int), "supplier_id is not an integer"

def test_store_get_store_banners_is_bool(amazon_asus_data):
    """Checks if 'get store banners' is a boolean."""
    get_store_banners = amazon_asus_data['store']['get store banners']
    assert isinstance(get_store_banners, bool), "'get store banners' is not a boolean"

def test_store_description_is_string(amazon_asus_data):
    """Checks if the description is a string."""
    description = amazon_asus_data['store']['description']
    assert isinstance(description, str), "description is not a string"

def test_store_about_is_string(amazon_asus_data):
    """Checks if the 'about' field is a string."""
    about = amazon_asus_data['store']['about']
    assert isinstance(about, str), "'about' is not a string"

def test_store_brand_is_string(amazon_asus_data):
    """Checks if the brand is a string."""
    brand = amazon_asus_data['store']['brand']
    assert isinstance(brand, str), "brand is not a string"
    assert brand == "ASUS", "brand is not ASUS"

def test_store_url_is_string(amazon_asus_data):
    """Checks if the URL is a string."""
    url = amazon_asus_data['store']['url']
    assert isinstance(url, str), "url is not a string"
    assert url.startswith("https://"), "URL does not start with https://"

def test_store_shop_categories_page_is_string(amazon_asus_data):
    """Checks if 'shop categories page' is a string."""
    shop_categories_page = amazon_asus_data['store']['shop categories page']
    assert isinstance(shop_categories_page, str), "'shop categories page' is not a string"

def test_store_shop_categories_json_file_is_string(amazon_asus_data):
    """Checks if 'shop categories json file' is a string."""
    shop_categories_json_file = amazon_asus_data['store']['shop categories json file']
    assert isinstance(shop_categories_json_file, str), "'shop categories json file' is not a string"

# Tests for the 'scenarios' section
def test_scenarios_keys_are_strings(amazon_asus_data):
    """Checks if scenario keys are strings."""
    scenarios = amazon_asus_data['scenarios']
    assert all(isinstance(key, str) for key in scenarios.keys()), "Scenario keys are not all strings"

def test_scenarios_values_are_dicts(amazon_asus_data):
      """Checks if the values in scenarios are dictionaries."""
      scenarios = amazon_asus_data['scenarios']
      assert all(isinstance(value, dict) for value in scenarios.values()), "Not all values in scenarios are dictionaries"

def test_scenario_brand_is_string(amazon_asus_data):
    """Checks if the brand in each scenario is a string and equals to ASUS."""
    scenarios = amazon_asus_data['scenarios']
    for scenario in scenarios.values():
        assert isinstance(scenario['brand'], str), "brand in scenario is not a string"
        assert scenario['brand'] == "ASUS", "brand in scenario is not ASUS"

def test_scenario_url_is_string_and_starts_with_https(amazon_asus_data):
    """Checks if the URL in each scenario is a string and starts with 'https://'."""
    scenarios = amazon_asus_data['scenarios']
    for scenario in scenarios.values():
        assert isinstance(scenario['url'], str), "url in scenario is not a string"
        assert scenario['url'].startswith("https://"), "URL in scenario does not start with https://"

def test_scenario_active_is_bool(amazon_asus_data):
    """Checks if 'active' in each scenario is a boolean."""
    scenarios = amazon_asus_data['scenarios']
    for scenario in scenarios.values():
       assert isinstance(scenario['active'], bool), "'active' in scenario is not a boolean"

def test_scenario_condition_is_string(amazon_asus_data):
    """Checks if 'condition' in each scenario is a string."""
    scenarios = amazon_asus_data['scenarios']
    for scenario in scenarios.values():
      assert isinstance(scenario['condition'], str), "'condition' in scenario is not a string"

def test_scenario_presta_categories_is_dict(amazon_asus_data):
    """Checks if 'presta_categories' in each scenario is a dict."""
    scenarios = amazon_asus_data['scenarios']
    for scenario in scenarios.values():
         assert isinstance(scenario['presta_categories'], dict), "'presta_categories' in scenario is not a dict"

def test_scenario_presta_categories_template_is_dict(amazon_asus_data):
    """Checks if 'template' within 'presta_categories' is a dict."""
    scenarios = amazon_asus_data['scenarios']
    for scenario in scenarios.values():
        assert isinstance(scenario['presta_categories']['template'], dict), "'template' in 'presta_categories' in scenario is not a dict"

def test_scenario_checkbox_is_bool(amazon_asus_data):
    """Checks if 'checkbox' in each scenario is a boolean."""
    scenarios = amazon_asus_data['scenarios']
    for scenario in scenarios.values():
         assert isinstance(scenario['checkbox'], bool), "'checkbox' in scenario is not a boolean"

def test_scenario_price_rule_is_int(amazon_asus_data):
     """Checks if 'price_rule' in each scenario is an integer."""
     scenarios = amazon_asus_data['scenarios']
     for scenario in scenarios.values():
        assert isinstance(scenario['price_rule'], int), "'price_rule' in scenario is not an integer"
```