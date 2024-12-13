```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def amazon_store_data():
    """Loads the Amazon store data from the JSON file."""
    file_path = 'hypotez/src/suppliers/amazon/scenarios/amazon_stores_amazon_ref.json'
    with open(file_path, 'r') as file:
        return json.load(file)


def test_store_data_structure(amazon_store_data):
    """
    Test that the base structure of the store data is correct.
    Checks for the existence of 'store' and 'scenarios' keys.
    """
    assert "store" in amazon_store_data
    assert "scenarios" in amazon_store_data

def test_store_properties(amazon_store_data):
    """
    Test that the 'store' properties are of the correct type and have expected values.
    Checks 'store_id', 'supplier_id', 'get store banners', 'description', 'url'
    """
    store = amazon_store_data["store"]
    assert isinstance(store["store_id"], str)
    assert isinstance(store["supplier_id"], int)
    assert isinstance(store["get store banners"], bool)
    assert isinstance(store["description"], str)
    assert isinstance(store["url"], str)
    assert store["description"] == "AMAZON REF"
    assert store["url"] == "https://www.amazon.com/Amazon-Renewed/b/ref=bl_dp_s_web_12653393011?ie=UTF8&node=12653393011&field-lbr_brands_browse-bin=Amazon+Renewed"

def test_scenarios_structure(amazon_store_data):
    """
    Test that the 'scenarios' is a dictionary with string keys
    """
    scenarios = amazon_store_data["scenarios"]
    assert isinstance(scenarios, dict)
    for key in scenarios:
        assert isinstance(key, str)

def test_scenario_properties(amazon_store_data):
    """
    Test properties of each scenario, check 'url', 'active', 'condition', 'presta_categories', 'checkbox', 'price_rule'
    """
    scenarios = amazon_store_data["scenarios"]
    for scenario_name, scenario in scenarios.items():
        assert isinstance(scenario["url"], str)
        assert isinstance(scenario["active"], (bool, str))
        assert isinstance(scenario["condition"], str)
        assert isinstance(scenario["presta_categories"], dict)
        assert isinstance(scenario["checkbox"], bool)
        assert isinstance(scenario["price_rule"], int)

def test_scenario_presta_categories(amazon_store_data):
    """
    Test 'presta_categories' within each scenario for correct structure, template key and values.
    """
    scenarios = amazon_store_data["scenarios"]
    for scenario_name, scenario in scenarios.items():
        presta_categories = scenario["presta_categories"]
        assert "template" in presta_categories
        assert isinstance(presta_categories["template"], dict)
        for key, value in presta_categories["template"].items():
             assert isinstance(key, str)
             assert isinstance(value, str)

def test_scenario_active_values(amazon_store_data):
    """
    Test that 'active' has valid values of boolean or 'skip'
    """
    scenarios = amazon_store_data["scenarios"]
    for scenario_name, scenario in scenarios.items():
        assert scenario["active"] in [True, False, "skip"]

def test_scenario_conditions(amazon_store_data):
    """
    Test 'condition' to equal 'new'
    """
    scenarios = amazon_store_data["scenarios"]
    for scenario_name, scenario in scenarios.items():
        assert scenario["condition"] == "new"

def test_scenario_price_rule(amazon_store_data):
    """
    Test 'price_rule' equal to 1
    """
    scenarios = amazon_store_data["scenarios"]
    for scenario_name, scenario in scenarios.items():
         assert scenario["price_rule"] == 1

def test_scenario_specific_data(amazon_store_data):
    """
    Test specific scenario data, check Oculus is skipped, Macbook has specific url
    """
    scenarios = amazon_store_data["scenarios"]
    assert scenarios["Oculus"]["active"] == "skip"
    assert scenarios["Macbook"]["url"] == "https://www.amazon.com/-/he/s?i=electronics&srs=12653393011&bbn=565108&rh=n%3A172282%2Cn%3A541966%2Cn%3A13896617011%2Cn%3A565108%2Cp_89%3AApple%2Cp_n_is_free_shipping%3A10236242011&dc&language=he&pf_rd_i=12653393011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=b8a4c9d3-e3d7-411d-a419-b400f6bb46e9&pf_rd_r=VEKNCE5K6F8HWCYCEAWE&pf_rd_s=merchandised-search-5&pf_rd_t=101&qid=1671316261&rnid=10236241011&ref=sr_nr_p_n_is_free_shipping_1&ds=v1%3AVoePDcw%2Bea9MH3wExY9HzWe8rFQdMeibWtRFaeXHdYc"
```