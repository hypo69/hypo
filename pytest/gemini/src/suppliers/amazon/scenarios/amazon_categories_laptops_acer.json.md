```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def json_data():
    file_path = "hypotez/src/suppliers/amazon/scenarios/amazon_categories_laptops_acer.json"
    with open(file_path, 'r') as f:
        return json.load(f)

# Test for the structure of the loaded JSON
def test_json_structure(json_data):
    """
    Tests that the json data has the expected top-level keys: 'store' and 'scenarios'.
    """
    assert "store" in json_data
    assert "scenarios" in json_data

# Test for the store section
def test_store_section(json_data):
    """
    Tests that the 'store' section has the required keys.
    """
    store_data = json_data["store"]
    assert "store_id" in store_data
    assert "supplier_id" in store_data
    assert "get store banners" in store_data
    assert "description" in store_data
    assert "about" in store_data
    assert "url" in store_data
    assert "shop categories page" in store_data
    assert "shop categories json file" in store_data


# Test for the scenarios section
def test_scenarios_section(json_data):
    """
     Tests that the 'scenarios' section is a dictionary.
    """
    assert isinstance(json_data["scenarios"], dict)

# Test for the keys of each scenario and their types
def test_scenario_keys(json_data):
    """
    Tests each scenario within 'scenarios' section for the expected keys and their data types.
    """
    scenarios = json_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        assert "brand" in scenario_data
        assert isinstance(scenario_data["brand"], str)
        assert "url" in scenario_data
        assert isinstance(scenario_data["url"], str)
        assert "active" in scenario_data
        assert isinstance(scenario_data["active"], bool)
        assert "condition" in scenario_data
        assert isinstance(scenario_data["condition"], str)
        assert "presta_categories" in scenario_data
        assert isinstance(scenario_data["presta_categories"], dict)
        assert "template" in scenario_data["presta_categories"]
        assert isinstance(scenario_data["presta_categories"]["template"], dict)
        assert "checkbox" in scenario_data
        assert isinstance(scenario_data["checkbox"], bool)
        assert "price_rule" in scenario_data
        assert isinstance(scenario_data["price_rule"], int)

# Test for presta_categories template values
def test_presta_categories_template_values(json_data):
    """
    Tests that the 'template' values within 'presta_categories' are lists.
    """
    scenarios = json_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
         template = scenario_data["presta_categories"]["template"]
         for key, value in template.items():
            assert isinstance(value, list)
            assert len(value) == 2, f"Expected 2 values in the list for {key} in {scenario_name}, but got {len(value)}"
            assert all(isinstance(item, str) for item in value)
# Test for valid URLs
def test_valid_urls(json_data):
        """
        Tests that URLs are valid strings and contain 'amazon.com'.
        """
        scenarios = json_data["scenarios"]
        for scenario_name, scenario_data in scenarios.items():
            url = scenario_data["url"]
            assert isinstance(url,str)
            assert "amazon.com" in url , f"Invalid URL {url} in scenario: {scenario_name}"
        store_url = json_data["store"]["url"]
        assert isinstance(store_url,str)
        assert "amazon.com" in store_url , f"Invalid URL {store_url} in store section"
# Test for valid price_rule
def test_valid_price_rule(json_data):
    """
     Tests that price_rule is 1
    """
    scenarios = json_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        price_rule = scenario_data["price_rule"]
        assert price_rule == 1 , f"Invalid price_rule {price_rule} in scenario: {scenario_name}"
# Test for all values of checkbox being false
def test_checkbox_is_false(json_data):
    """
     Tests that all values of checkbox are false
    """
    scenarios = json_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
      checkbox = scenario_data["checkbox"]
      assert checkbox == False , f"Invalid checkbox value {checkbox} in scenario: {scenario_name}"

#Test for all values of condition being "new"
def test_condition_is_new(json_data):
    """
     Tests that all values of condition are 'new'
    """
    scenarios = json_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        condition = scenario_data["condition"]
        assert condition == "new" , f"Invalid condition value {condition} in scenario: {scenario_name}"
#Test for all values of active being True
def test_active_is_true(json_data):
    """
     Tests that all values of active are True
    """
    scenarios = json_data["scenarios"]
    for scenario_name, scenario_data in scenarios.items():
        active = scenario_data["active"]
        assert active == True , f"Invalid active value {active} in scenario: {scenario_name}"

```