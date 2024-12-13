```python
import pytest
import json

# Fixture for loading the JSON data
@pytest.fixture
def sparkfun_config():
    """Loads the JSON configuration data for testing."""
    config_data = {
        "supplier": "sparkfun",
        "supplier_prefix": "sparkfun",
        "start_url": "https://www.sparkfun.com/categories",
        "price_rule": "+0",
        "if_login": False,
        "collect_products_from_categorypage": False,
        "parcing method [webdriver|api]": "web",
        "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
        "root_category": 3,
        "scenarios": {}
    }
    return config_data


def test_sparkfun_config_supplier_name(sparkfun_config):
    """Checks if the 'supplier' field is correctly set to 'sparkfun'."""
    assert sparkfun_config["supplier"] == "sparkfun"

def test_sparkfun_config_supplier_prefix(sparkfun_config):
    """Checks if the 'supplier_prefix' field is correctly set to 'sparkfun'."""
    assert sparkfun_config["supplier_prefix"] == "sparkfun"

def test_sparkfun_config_start_url(sparkfun_config):
    """Checks if the 'start_url' field is correctly set to the Sparkfun categories URL."""
    assert sparkfun_config["start_url"] == "https://www.sparkfun.com/categories"

def test_sparkfun_config_price_rule(sparkfun_config):
    """Checks if the 'price_rule' field is correctly set to '+0'."""
    assert sparkfun_config["price_rule"] == "+0"

def test_sparkfun_config_if_login_false(sparkfun_config):
    """Checks if the 'if_login' field is correctly set to False."""
    assert sparkfun_config["if_login"] == False

def test_sparkfun_config_collect_products_false(sparkfun_config):
     """Checks if the 'collect_products_from_categorypage' field is correctly set to False."""
     assert sparkfun_config["collect_products_from_categorypage"] == False

def test_sparkfun_config_parcing_method(sparkfun_config):
    """Checks if the 'parcing method [webdriver|api]' field is correctly set to 'web'."""
    assert sparkfun_config["parcing method [webdriver|api]"] == "web"

def test_sparkfun_config_about_method(sparkfun_config):
     """Checks if the 'about method web scrapping [webdriver|api]' field contains the expected Russian text."""
     assert sparkfun_config["about method web scrapping [webdriver|api]"] == "Если я работаю через API мне не нужен webdriver"

def test_sparkfun_config_root_category(sparkfun_config):
    """Checks if the 'root_category' field is correctly set to 3."""
    assert sparkfun_config["root_category"] == 3

def test_sparkfun_config_scenarios_empty(sparkfun_config):
    """Checks if the 'scenarios' field is an empty dictionary."""
    assert sparkfun_config["scenarios"] == {}

def test_sparkfun_config_invalid_type_supplier():
    """Checks if the supplier name is a string, if not, catch an error"""
    with pytest.raises(TypeError):
        config_data = {
        "supplier": 123,
        "supplier_prefix": "sparkfun",
        "start_url": "https://www.sparkfun.com/categories",
        "price_rule": "+0",
        "if_login": False,
        "collect_products_from_categorypage": False,
        "parcing method [webdriver|api]": "web",
        "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
        "root_category": 3,
        "scenarios": {}
        }
        assert config_data["supplier"] == "sparkfun"
def test_sparkfun_config_invalid_type_start_url():
    """Checks if the start url is a string, if not, catch an error"""
    with pytest.raises(TypeError):
        config_data = {
        "supplier": "sparkfun",
        "supplier_prefix": "sparkfun",
        "start_url": 123,
        "price_rule": "+0",
        "if_login": False,
        "collect_products_from_categorypage": False,
        "parcing method [webdriver|api]": "web",
        "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
        "root_category": 3,
        "scenarios": {}
        }
        assert config_data["start_url"] == "https://www.sparkfun.com/categories"

def test_sparkfun_config_invalid_type_price_rule():
    """Checks if the price rule is a string, if not, catch an error"""
    with pytest.raises(TypeError):
        config_data = {
        "supplier": "sparkfun",
        "supplier_prefix": "sparkfun",
        "start_url": "https://www.sparkfun.com/categories",
        "price_rule": 0,
        "if_login": False,
        "collect_products_from_categorypage": False,
        "parcing method [webdriver|api]": "web",
        "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
        "root_category": 3,
        "scenarios": {}
        }
        assert config_data["price_rule"] == "+0"

def test_sparkfun_config_invalid_type_if_login():
    """Checks if the if_login is a boolean, if not, catch an error"""
    with pytest.raises(TypeError):
        config_data = {
        "supplier": "sparkfun",
        "supplier_prefix": "sparkfun",
        "start_url": "https://www.sparkfun.com/categories",
        "price_rule": "+0",
        "if_login": "False",
        "collect_products_from_categorypage": False,
        "parcing method [webdriver|api]": "web",
        "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
        "root_category": 3,
        "scenarios": {}
        }
        assert config_data["if_login"] == False

def test_sparkfun_config_invalid_type_collect_products():
    """Checks if the collect_products is a boolean, if not, catch an error"""
    with pytest.raises(TypeError):
        config_data = {
        "supplier": "sparkfun",
        "supplier_prefix": "sparkfun",
        "start_url": "https://www.sparkfun.com/categories",
        "price_rule": "+0",
        "if_login": False,
        "collect_products_from_categorypage": "False",
        "parcing method [webdriver|api]": "web",
        "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
        "root_category": 3,
        "scenarios": {}
        }
        assert config_data["collect_products_from_categorypage"] == False

def test_sparkfun_config_invalid_type_parcing_method():
      """Checks if the parcing method is a string, if not, catch an error"""
      with pytest.raises(TypeError):
        config_data = {
        "supplier": "sparkfun",
        "supplier_prefix": "sparkfun",
        "start_url": "https://www.sparkfun.com/categories",
        "price_rule": "+0",
        "if_login": False,
        "collect_products_from_categorypage": False,
        "parcing method [webdriver|api]": 123,
        "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
        "root_category": 3,
        "scenarios": {}
        }
        assert config_data["parcing method [webdriver|api]"] == "web"
def test_sparkfun_config_invalid_type_about_method():
      """Checks if the about method is a string, if not, catch an error"""
      with pytest.raises(TypeError):
        config_data = {
        "supplier": "sparkfun",
        "supplier_prefix": "sparkfun",
        "start_url": "https://www.sparkfun.com/categories",
        "price_rule": "+0",
        "if_login": False,
        "collect_products_from_categorypage": False,
        "parcing method [webdriver|api]": "web",
        "about method web scrapping [webdriver|api]": 123,
        "root_category": 3,
        "scenarios": {}
        }
        assert config_data["about method web scrapping [webdriver|api]"] == "Если я работаю через API мне не нужен webdriver"
def test_sparkfun_config_invalid_type_root_category():
      """Checks if the root_category is a int, if not, catch an error"""
      with pytest.raises(TypeError):
        config_data = {
        "supplier": "sparkfun",
        "supplier_prefix": "sparkfun",
        "start_url": "https://www.sparkfun.com/categories",
        "price_rule": "+0",
        "if_login": False,
        "collect_products_from_categorypage": False,
        "parcing method [webdriver|api]": "web",
        "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
        "root_category": "3",
        "scenarios": {}
        }
        assert config_data["root_category"] == 3

def test_sparkfun_config_invalid_type_scenarios():
        """Checks if the scenarios is a dict, if not, catch an error"""
        with pytest.raises(TypeError):
            config_data = {
            "supplier": "sparkfun",
            "supplier_prefix": "sparkfun",
            "start_url": "https://www.sparkfun.com/categories",
            "price_rule": "+0",
            "if_login": False,
            "collect_products_from_categorypage": False,
            "parcing method [webdriver|api]": "web",
            "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
            "root_category": 3,
            "scenarios": 123
            }
            assert config_data["scenarios"] == {}
```