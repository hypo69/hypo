```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def bangood_data():
    """Provides the JSON data for the tests."""
    with open('hypotez/src/scenario/json/bangood.json', 'r') as f:
        return json.load(f)

def test_bangood_supplier(bangood_data):
    """Checks if the supplier is correctly set to 'ksp'."""
    assert bangood_data['supplier'] == 'ksp'

def test_bangood_supplier_prefix(bangood_data):
    """Checks if the supplier prefix is correctly set to 'ksp'."""
    assert bangood_data['supplier_prefix'] == 'ksp'

def test_bangood_start_url(bangood_data):
    """Checks if the start URL is a valid URL and contains the expected domain."""
    assert bangood_data['start_url'].startswith('https://www.banggood.com')
    assert 'search' in bangood_data['start_url']

def test_bangood_price_rule(bangood_data):
    """Checks if the price rule is a string and equals '+100'."""
    assert isinstance(bangood_data['price_rule'], str)
    assert bangood_data['price_rule'] == '+100'

def test_bangood_num_items_4_flush(bangood_data):
    """Checks if the number of items for flush is an integer and greater than 0."""
    assert isinstance(bangood_data['num_items_4_flush'], int)
    assert bangood_data['num_items_4_flush'] > 0

def test_bangood_if_login(bangood_data):
    """Checks if the 'if_login' flag is a boolean and its value is False."""
    assert isinstance(bangood_data['if_login'], bool)
    assert bangood_data['if_login'] == False

def test_bangood_parcing_method(bangood_data):
    """Checks if the parsing method is set to 'web'."""
    assert bangood_data['parcing method [webdriver|api]'] == 'web'

def test_bangood_about_method_web_scrapping(bangood_data):
    """
    Checks if the about method web scrapping description is correct.
    This test ensures that a specific text or a specific method is selected.
    """
    expected_message = "Если я работаю через API мне не нужен webdriver"
    assert bangood_data['about method web scrapping [webdriver|api]'] == expected_message

def test_bangood_collect_products_from_categorypage(bangood_data):
    """Checks if the 'collect_products_from_categorypage' flag is a boolean and its value is False."""
    assert isinstance(bangood_data['collect_products_from_categorypage'], bool)
    assert bangood_data['collect_products_from_categorypage'] == False

def test_bangood_scenario_files(bangood_data):
    """Checks if 'scenario_files' is a list and contains specific filenames."""
    assert isinstance(bangood_data['scenario_files'], list)
    assert "ksp_categories_consoles_microsoft.json" in bangood_data['scenario_files']
    assert "ksp_categories_wathces_apple.json" in bangood_data['scenario_files']

def test_bangood_excluded_files(bangood_data):
    """Checks if 'excluded' is a list and contains specific filenames that should be excluded."""
    assert isinstance(bangood_data['excluded'], list)
    assert "ksp_categories_speakers_google.json" in bangood_data['excluded']
    assert "ksp_categories_monitors_lg.json" in bangood_data['excluded']
    assert "ksp_categories_iphones.json" in bangood_data['excluded']
    assert "ksp_categories_notebooks_dell_by_model.json" in bangood_data['excluded']

def test_bangood_last_runned_scenario(bangood_data):
    """Checks if the 'last_runned_scenario' is a string and its value is empty."""
    assert isinstance(bangood_data['last_runned_scenario'], str)
    assert bangood_data['last_runned_scenario'] == ""
```