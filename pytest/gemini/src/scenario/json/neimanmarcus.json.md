```python
import pytest
import json

# Fixture definitions, if needed
@pytest.fixture
def valid_json_data():
    """Provides a valid JSON data structure for testing."""
    return {
        "supplier": "ksp",
        "supplier_prefix": "ksp",
        "start_url": "https://www.ksp.co.il/",
        "price_rule": "+100",
        "num_items_4_flush": 300,
        "if_login": False,
        "parcing method [webdriver|api]": "web",
        "about method web scrapping [webdriver|api]": "Если я работаю через API мне не нужен webdriver",
        "collect_products_from_categorypage": False,
        "scenarios": {}
    }

@pytest.fixture
def invalid_json_data():
    """Provides an invalid JSON data structure for testing."""
    return {
        "supplier": 123,  # Invalid type for supplier
        "supplier_prefix": "ksp",
        "start_url": "invalid_url", # Invalid URL
         "price_rule": 100,
        "num_items_4_flush": "300",  # Invalid type for num_items
        "if_login": "false",
        "parcing method [webdriver|api]": 1,
        "about method web scrapping [webdriver|api]": 123,
        "collect_products_from_categorypage": "False", # Invalid type
        "scenarios": "wrong_type"
    }


def test_valid_json_data_structure(valid_json_data):
    """Checks that the valid json data has the expected keys and data types."""
    assert isinstance(valid_json_data, dict)
    assert "supplier" in valid_json_data
    assert isinstance(valid_json_data["supplier"], str)
    assert "supplier_prefix" in valid_json_data
    assert isinstance(valid_json_data["supplier_prefix"], str)
    assert "start_url" in valid_json_data
    assert isinstance(valid_json_data["start_url"], str)
    assert "price_rule" in valid_json_data
    assert isinstance(valid_json_data["price_rule"], str)
    assert "num_items_4_flush" in valid_json_data
    assert isinstance(valid_json_data["num_items_4_flush"], int)
    assert "if_login" in valid_json_data
    assert isinstance(valid_json_data["if_login"], bool)
    assert "parcing method [webdriver|api]" in valid_json_data
    assert isinstance(valid_json_data["parcing method [webdriver|api]"], str)
    assert "about method web scrapping [webdriver|api]" in valid_json_data
    assert isinstance(valid_json_data["about method web scrapping [webdriver|api]"], str)
    assert "collect_products_from_categorypage" in valid_json_data
    assert isinstance(valid_json_data["collect_products_from_categorypage"], bool)
    assert "scenarios" in valid_json_data
    assert isinstance(valid_json_data["scenarios"], dict)

def test_invalid_json_data_structure(invalid_json_data):
    """Checks the invalid json has unexpected type values"""
    assert isinstance(invalid_json_data, dict)
    assert "supplier" in invalid_json_data
    assert not isinstance(invalid_json_data["supplier"], str)
    assert "supplier_prefix" in invalid_json_data
    assert isinstance(invalid_json_data["supplier_prefix"], str)
    assert "start_url" in invalid_json_data
    assert not  (invalid_json_data["start_url"].startswith('http') or invalid_json_data["start_url"].startswith('https'))
    assert "price_rule" in invalid_json_data
    assert not isinstance(invalid_json_data["price_rule"], str)
    assert "num_items_4_flush" in invalid_json_data
    assert not isinstance(invalid_json_data["num_items_4_flush"], int)
    assert "if_login" in invalid_json_data
    assert not isinstance(invalid_json_data["if_login"], bool)
    assert "parcing method [webdriver|api]" in invalid_json_data
    assert not isinstance(invalid_json_data["parcing method [webdriver|api]"], str)
    assert "about method web scrapping [webdriver|api]" in invalid_json_data
    assert not isinstance(invalid_json_data["about method web scrapping [webdriver|api]"], str)
    assert "collect_products_from_categorypage" in invalid_json_data
    assert not isinstance(invalid_json_data["collect_products_from_categorypage"], bool)
    assert "scenarios" in invalid_json_data
    assert not isinstance(invalid_json_data["scenarios"], dict)

def test_load_valid_json_file(valid_json_data):
    """Tests loading a valid JSON structure from a file."""
    # Create a dummy file with valid JSON data
    with open("test_valid.json", "w") as f:
        json.dump(valid_json_data, f)
    
    # Load JSON data from the file
    with open("test_valid.json", "r") as f:
         loaded_data = json.load(f)
    
    # Assert data
    assert loaded_data == valid_json_data
    
def test_load_invalid_json_file(invalid_json_data):
        """Tests loading a invalid JSON structure from a file."""
        with open("test_invalid.json", "w") as f:
            json.dump(invalid_json_data, f)
        
        with pytest.raises(Exception):
             with open("test_invalid.json", "r") as f:
                 json.load(f)
```