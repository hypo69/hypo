```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def morlevi_data():
    """Loads the morlevi.json data for testing."""
    with open("hypotez/src/scenario/json/morlevi.json", 'r') as f:
        return json.load(f)

# Test case for supplier
def test_supplier_name(morlevi_data):
    """Verifies the supplier name."""
    assert morlevi_data["supplier"] == "morlevi"

# Test case for supplier ID
def test_supplier_id(morlevi_data):
    """Verifies the supplier ID."""
    assert morlevi_data["supplier_id"] == "2784"

# Test case for supplier prefix
def test_supplier_prefix(morlevi_data):
    """Verifies the supplier prefix."""
    assert morlevi_data["supplier_prefix"] == "mlv"

# Test case for start URL
def test_start_url(morlevi_data):
    """Verifies the start URL."""
    assert morlevi_data["start_url"] == "https://www.morlevi.co.il/"

# Test case for login URL
def test_login_url(morlevi_data):
    """Verifies the login URL."""
    assert morlevi_data["login_url"] == "https://www.morlevi.co.il/"

# Test case for price rule
def test_price_rule(morlevi_data):
    """Verifies the price rule."""
    assert morlevi_data["price_rule"] == "*1.43"

# Test case for if_list
def test_if_list(morlevi_data):
    """Verifies the if_list value."""
    assert morlevi_data["if_list"] == "first"

# Test case for use_mouse
def test_use_mouse(morlevi_data):
    """Verifies the use_mouse value."""
    assert morlevi_data["use_mouse"] is False

# Test case for mandatory
def test_mandatory(morlevi_data):
    """Verifies the mandatory value."""
    assert morlevi_data["mandatory"] is True

# Test case for collect_products_from_categorypage
def test_collect_products_from_categorypage(morlevi_data):
    """Verifies collect_products_from_categorypage value."""
    assert morlevi_data["collect_products_from_categorypage"] is False

# Test case for num_items_4_flush
def test_num_items_4_flush(morlevi_data):
    """Verifies num_items_4_flush value."""
    assert morlevi_data["num_items_4_flush"] == 500

# Test case for if_login
def test_if_login(morlevi_data):
    """Verifies if_login value."""
    assert morlevi_data["if_login"] is True

# Test case for parcing method
def test_parcing_method(morlevi_data):
    """Verifies the parsing method."""
    assert morlevi_data["parcing method [webdriver|api]"] == "web"

# Test case for about method web scrapping
def test_about_method_web_scrapping(morlevi_data):
  """Verifies the about method web scrapping information."""
  assert morlevi_data["about method web scrapping [webdriver|api]"] == "Если я работаю через API мне не нужен webdriver"


# Test case for scenario_files is a list and not empty
def test_scenario_files_is_list(morlevi_data):
    """Verifies that scenario_files is a list and not empty."""
    assert isinstance(morlevi_data["scenario_files"], list)
    assert len(morlevi_data["scenario_files"]) > 0

# Test case for last_runned_scenario
def test_last_runned_scenario(morlevi_data):
    """Verifies last_runned_scenario is a string."""
    assert isinstance(morlevi_data["last_runned_scenario"], str)

# Test case for excluded is a list of lists
def test_excluded_is_list_of_lists(morlevi_data):
    """Verifies that 'excluded' is a list of lists."""
    assert isinstance(morlevi_data["excluded"], list)
    for item in morlevi_data["excluded"]:
        assert isinstance(item, list)

# Test case for scenario_files contains a $ref
def test_scenario_files_contains_ref(morlevi_data):
    """Verifies if scenario_files contains a $ref item"""
    assert any("$ref" in item for item in morlevi_data["scenario_files"] if isinstance(item,str))

# Test case to ensure scenario files are of correct type
def test_scenario_files_type(morlevi_data):
    """Verifies all items in scenario_files are either strings or dicts."""
    for item in morlevi_data["scenario_files"]:
        assert isinstance(item, str) or isinstance(item, dict)
```