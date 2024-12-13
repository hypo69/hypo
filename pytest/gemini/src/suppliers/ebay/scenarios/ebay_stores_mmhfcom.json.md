```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def ebay_store_data():
    """Loads the ebay store JSON data from the file."""
    file_path = "hypotez/src/suppliers/ebay/scenarios/ebay_stores_mmhfcom.json"
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Test cases for the 'store' section
def test_store_data_exists(ebay_store_data):
    """Test that the 'store' section exists in the data."""
    assert "store" in ebay_store_data

def test_store_id_is_correct(ebay_store_data):
    """Test if the 'store_id' is correctly extracted"""
    assert ebay_store_data["store"]["store_id"] == "thegasketsman75"

def test_supplier_id_is_correct(ebay_store_data):
    """Test if the 'supplier_id' is correctly extracted"""
    assert ebay_store_data["store"]["supplier_id"] == 4534

def test_get_store_banners_is_true(ebay_store_data):
    """Test if 'get store banners' flag is True"""
    assert ebay_store_data["store"]["get store banners"] is True

def test_store_description_is_correct(ebay_store_data):
    """Test if the store description is extracted"""
    assert ebay_store_data["store"]["description"] == "thegasketsman75 Gasket KIT"

def test_store_about_is_empty(ebay_store_data):
    """Test if the 'about' field is empty"""
    assert ebay_store_data["store"]["about"] == " "

def test_store_url_is_correct(ebay_store_data):
     """Test if the URL is correctly extracted"""
     assert ebay_store_data["store"]["url"] == "https://www.ebay.com/str/mmhfcom"

def test_shop_categories_page_is_empty(ebay_store_data):
    """Test if the 'shop categories page' is empty"""
    assert ebay_store_data["store"]["shop categories page"] == ""

def test_shop_categories_json_file_is_empty(ebay_store_data):
     """Test if the 'shop categories json file' is empty"""
     assert ebay_store_data["store"]["shop categories json file"] == ""

# Test cases for the 'scenarios' section
def test_scenarios_data_exists(ebay_store_data):
    """Test that the 'scenarios' section exists in the data."""
    assert "scenarios" in ebay_store_data

def test_motor_parts_scenario_exists(ebay_store_data):
    """Test that the 'motor parts' scenario exists."""
    assert "motor parts" in ebay_store_data["scenarios"]

def test_motor_parts_scenario_url_correct(ebay_store_data):
    """Test the URL of 'motor parts' scenario"""
    assert ebay_store_data["scenarios"]["motor parts"]["url"] == "https://www.ebay.com/str/mmhfcom/eBay-Motors/_i.html?_sacat=6000"

def test_motor_parts_scenario_active_is_true(ebay_store_data):
    """Test if 'motor parts' scenario is active"""
    assert ebay_store_data["scenarios"]["motor parts"]["active"] is True

def test_motor_parts_scenario_condition_is_new(ebay_store_data):
    """Test if the 'condition' for 'motor parts' scenario is 'new'"""
    assert ebay_store_data["scenarios"]["motor parts"]["condition"] == "new"

def test_motor_parts_presta_categories_template_exists(ebay_store_data):
    """Test if the 'presta_categories' template exists for 'motor parts' scenario"""
    assert "template" in ebay_store_data["scenarios"]["motor parts"]["presta_categories"]

def test_motor_parts_presta_categories_template_value_correct(ebay_store_data):
    """Test the value for 'automotive parts' in 'presta_categories' for 'motor parts'"""
    assert ebay_store_data["scenarios"]["motor parts"]["presta_categories"]["template"]["automotive parts"] == "PARTS UNSORTED"

def test_motor_parts_scenario_checkbox_is_false(ebay_store_data):
    """Test if the checkbox is False for 'motor parts' scenario"""
    assert ebay_store_data["scenarios"]["motor parts"]["checkbox"] is False

def test_motor_parts_scenario_price_rule_is_1(ebay_store_data):
    """Test if the price rule for 'motor parts' is 1"""
    assert ebay_store_data["scenarios"]["motor parts"]["price_rule"] == 1


def test_industrial_scenario_exists(ebay_store_data):
    """Test that the 'industrial' scenario exists."""
    assert "industrial" in ebay_store_data["scenarios"]

def test_industrial_scenario_url_correct(ebay_store_data):
    """Test the URL of 'industrial' scenario"""
    assert ebay_store_data["scenarios"]["industrial"]["url"] == "https://www.ebay.com/str/mmhfcom/Business-Industrial/_i.html?_sacat=12576"

def test_industrial_scenario_active_is_true(ebay_store_data):
    """Test if 'industrial' scenario is active"""
    assert ebay_store_data["scenarios"]["industrial"]["active"] is True

def test_industrial_scenario_condition_is_new(ebay_store_data):
     """Test if the 'condition' for 'industrial' scenario is 'new'"""
     assert ebay_store_data["scenarios"]["industrial"]["condition"] == "new"

def test_industrial_presta_categories_template_exists(ebay_store_data):
    """Test if the 'presta_categories' template exists for 'industrial' scenario"""
    assert "template" in ebay_store_data["scenarios"]["industrial"]["presta_categories"]

def test_industrial_presta_categories_template_value_correct(ebay_store_data):
    """Test the value for 'desktop_hardware' in 'presta_categories' for 'industrial'"""
    assert ebay_store_data["scenarios"]["industrial"]["presta_categories"]["template"]["desktop_hardware"] == "UNSORTED"


def test_industrial_scenario_checkbox_is_false(ebay_store_data):
    """Test if the checkbox is False for 'industrial' scenario"""
    assert ebay_store_data["scenarios"]["industrial"]["checkbox"] is False


def test_industrial_scenario_price_rule_is_1(ebay_store_data):
    """Test if the price rule for 'industrial' is 1"""
    assert ebay_store_data["scenarios"]["industrial"]["price_rule"] == 1


def test_industrial_2_scenario_exists(ebay_store_data):
    """Test that the 'industrial 2' scenario exists."""
    assert "industrial 2" in ebay_store_data["scenarios"]

def test_industrial_2_scenario_url_correct(ebay_store_data):
    """Test the URL of 'industrial 2' scenario"""
    assert ebay_store_data["scenarios"]["industrial 2"]["url"] == "https://www.ebay.com/str/mmhfcom/Consumer-Electronics/_i.html?_sacat=293"

def test_industrial_2_scenario_active_is_true(ebay_store_data):
    """Test if 'industrial 2' scenario is active"""
    assert ebay_store_data["scenarios"]["industrial 2"]["active"] is True

def test_industrial_2_scenario_condition_is_new(ebay_store_data):
     """Test if the 'condition' for 'industrial 2' scenario is 'new'"""
     assert ebay_store_data["scenarios"]["industrial 2"]["condition"] == "new"


def test_industrial_2_presta_categories_template_exists(ebay_store_data):
    """Test if the 'presta_categories' template exists for 'industrial 2' scenario"""
    assert "template" in ebay_store_data["scenarios"]["industrial 2"]["presta_categories"]


def test_industrial_2_presta_categories_template_value_correct(ebay_store_data):
    """Test the value for 'desktop_hardware' in 'presta_categories' for 'industrial 2'"""
    assert ebay_store_data["scenarios"]["industrial 2"]["presta_categories"]["template"]["desktop_hardware"] == "UNSORTED"

def test_industrial_2_scenario_checkbox_is_false(ebay_store_data):
    """Test if the checkbox is False for 'industrial 2' scenario"""
    assert ebay_store_data["scenarios"]["industrial 2"]["checkbox"] is False

def test_industrial_2_scenario_price_rule_is_1(ebay_store_data):
    """Test if the price rule for 'industrial 2' is 1"""
    assert ebay_store_data["scenarios"]["industrial 2"]["price_rule"] == 1

def test_health_scenario_exists(ebay_store_data):
    """Test that the 'health' scenario exists."""
    assert "health" in ebay_store_data["scenarios"]

def test_health_scenario_url_correct(ebay_store_data):
    """Test the URL of 'health' scenario"""
    assert ebay_store_data["scenarios"]["health"]["url"] == "https://www.ebay.com/str/mmhfcom/Health-Beauty/_i.html?_sacat=26395"

def test_health_scenario_active_is_true(ebay_store_data):
    """Test if 'health' scenario is active"""
    assert ebay_store_data["scenarios"]["health"]["active"] is True

def test_health_scenario_condition_is_new(ebay_store_data):
    """Test if the 'condition' for 'health' scenario is 'new'"""
    assert ebay_store_data["scenarios"]["health"]["condition"] == "new"

def test_health_presta_categories_template_exists(ebay_store_data):
    """Test if the 'presta_categories' template exists for 'health' scenario"""
    assert "template" in ebay_store_data["scenarios"]["health"]["presta_categories"]

def test_health_presta_categories_template_value_correct(ebay_store_data):
    """Test the value for 'desktop_hardware' in 'presta_categories' for 'health'"""
    assert ebay_store_data["scenarios"]["health"]["presta_categories"]["template"]["desktop_hardware"] == "UNSORTED"

def test_health_scenario_checkbox_is_false(ebay_store_data):
    """Test if the checkbox is False for 'health' scenario"""
    assert ebay_store_data["scenarios"]["health"]["checkbox"] is False

def test_health_scenario_price_rule_is_1(ebay_store_data):
    """Test if the price rule for 'health' is 1"""
    assert ebay_store_data["scenarios"]["health"]["price_rule"] == 1
```