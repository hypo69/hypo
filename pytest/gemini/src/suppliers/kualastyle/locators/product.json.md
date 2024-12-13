```python
import pytest
import json

# Fixture to load the product locator data
@pytest.fixture
def product_locators():
    """Loads the product locators data from the JSON file."""
    file_path = 'hypotez/src/suppliers/kualastyle/locators/product.json'
    with open(file_path, 'r') as f:
        return json.load(f)


def test_product_locators_structure(product_locators):
    """
    Checks if the loaded JSON data is a dictionary and contains the expected keys.
    """
    assert isinstance(product_locators, dict), "The loaded data is not a dictionary."
    assert len(product_locators) > 0, "The dictionary is empty"


def test_locator_keys_are_strings(product_locators):
    """
    Checks that the keys in product_locators are strings
    """
    for key in product_locators.keys():
        assert isinstance(key, str), f"Key '{key}' is not a string."


def test_locator_values_are_dictionaries(product_locators):
    """
    Checks that values in product_locators are dictionaries.
    """
    for key, value in product_locators.items():
        assert isinstance(value, dict), f"Value for key '{key}' is not a dictionary."


def test_locator_dictionary_structure(product_locators):
    """
        Checks the inner structure of locator dictionary.
    """
    for key, value in product_locators.items():
         
        if key == 'description_short':
            assert "attribute" in value, f"Key 'attribute' missing in '{key}'"
            assert "logic for attribue[AND|OR|XOR|VALUE|null]" in value, f"Key 'logic for attribue[AND|OR|XOR|VALUE|null]' missing in '{key}'"
            assert "by" in value, f"Key 'by' missing in '{key}'"
            assert "selector" in value, f"Key 'selector' missing in '{key}'"
            assert "logic for action[AND|OR|XOR|VALUE|null]" in value, f"Key 'logic for action[AND|OR|XOR|VALUE|null]' missing in '{key}'"
            assert "if_list" in value, f"Key 'if_list' missing in '{key}'"
            assert "use_mouse" in value, f"Key 'use_mouse' missing in '{key}'"
            assert "timeout" in value, f"Key 'timeout' missing in '{key}'"
            assert "timeout_for_event" in value, f"Key 'timeout_for_event' missing in '{key}'"
            assert "event" in value, f"Key 'event' missing in '{key}'"
            assert isinstance(value["attribute"], list)
            assert isinstance(value["logic for attribue[AND|OR|XOR|VALUE|null]"], list)
            assert isinstance(value["by"], list)
            assert isinstance(value["selector"], list)
            assert isinstance(value["logic for action[AND|OR|XOR|VALUE|null]"], list)
            assert isinstance(value["use_mouse"], list)
            assert isinstance(value["event"], list)


        elif key == "Screenshot":
            assert "attribute" in value, f"Key 'attribute' missing in '{key}'"
            assert "by" in value, f"Key 'by' missing in '{key}'"
            assert "selector" in value, f"Key 'selector' missing in '{key}'"
            assert "if_list" in value, f"Key 'if_list' missing in '{key}'"
            assert "use_mouse" in value, f"Key 'use_mouse' missing in '{key}'"
            assert "mandatory" in value, f"Key 'mandatory' missing in '{key}'"
            assert "timeout" in value, f"Key 'timeout' missing in '{key}'"
            assert "timeout_for_event" in value, f"Key 'timeout_for_event' missing in '{key}'"
            assert "event" in value, f"Key 'event' missing in '{key}'"
            assert "logic for action[AND|OR|XOR|VALUE|null]" in value, f"Key 'logic for action[AND|OR|XOR|VALUE|null]' missing in '{key}'"


        elif key == "specification":
             assert "attribute" in value, f"Key 'attribute' missing in '{key}'"
             assert "by" in value, f"Key 'by' missing in '{key}'"
             assert "selector" in value, f"Key 'selector' missing in '{key}'"
             assert "if_list" in value, f"Key 'if_list' missing in '{key}'"
             assert "use_mouse" in value, f"Key 'use_mouse' missing in '{key}'"
             assert "mandatory" in value, f"Key 'mandatory' missing in '{key}'"
             assert "timeout" in value, f"Key 'timeout' missing in '{key}'"
             assert "timeout_for_event" in value, f"Key 'timeout_for_event' missing in '{key}'"
             assert "event" in value, f"Key 'event' missing in '{key}'"
             assert "locator_description" in value, f"Key 'locator_description' missing in '{key}'"


        else:
            assert "attribute" in value, f"Key 'attribute' missing in '{key}'"
            assert "by" in value, f"Key 'by' missing in '{key}'"
            assert "selector" in value, f"Key 'selector' missing in '{key}'"
            assert "if_list" in value, f"Key 'if_list' missing in '{key}'"
            assert "use_mouse" in value, f"Key 'use_mouse' missing in '{key}'"
            assert "mandatory" in value, f"Key 'mandatory' missing in '{key}'"
            assert "timeout" in value, f"Key 'timeout' missing in '{key}'"
            assert "timeout_for_event" in value, f"Key 'timeout_for_event' missing in '{key}'"
            assert "event" in value, f"Key 'event' missing in '{key}'"


def test_attribute_types(product_locators):
    """
    Checks the data types of the 'attribute' field for each locator.
    """
    for key, value in product_locators.items():
        if key == 'description_short':
            assert isinstance(value['attribute'], list)
            for item in value['attribute']:
                assert isinstance(item, (str, type(None)))
        elif key == "Condition":
             assert isinstance(value["attribute"], (str, bool, type(None)))
        elif key == "affiliate_short_link":
            assert isinstance(value["attribute"], str)
        else:
            assert isinstance(value["attribute"], (str, int, bool, type(None)))



def test_by_types(product_locators):
    """
    Checks the data types of the 'by' field for each locator.
    """
    for key, value in product_locators.items():
        if key == "description_short":
             assert isinstance(value["by"], list)
             for item in value["by"]:
                 assert isinstance(item, (str, type(None)))
        else:
           assert isinstance(value["by"], (str, type(None)))
       

def test_selector_types(product_locators):
    """
    Checks the data types of the 'selector' field for each locator.
    """
    for key, value in product_locators.items():
        if key == "description_short":
            assert isinstance(value["selector"], list)
            for item in value["selector"]:
               assert isinstance(item, (str, type(None)))
        else:
             assert isinstance(value["selector"], (str, type(None)))


def test_if_list_values(product_locators):
     """
     Checks the data type and allowed values of the 'if_list' field.
     """
     allowed_values = ["first", "all"]
     for key, value in product_locators.items():
        assert isinstance(value["if_list"], str), f"The 'if_list' in {key} is not a string."
        assert value["if_list"] in allowed_values, f"The 'if_list' in {key} has an invalid value."


def test_use_mouse_values(product_locators):
     """
     Checks the data type of the 'use_mouse' field.
     """
     for key, value in product_locators.items():
        if key == "description_short":
              assert isinstance(value["use_mouse"], list)
              for item in value["use_mouse"]:
                   assert isinstance(item, bool)
        else:
            assert isinstance(value["use_mouse"], bool), f"The 'use_mouse' in {key} is not a boolean."


def test_mandatory_values(product_locators):
     """
     Checks the data type of the 'mandatory' field.
     """
     for key, value in product_locators.items():
        assert isinstance(value["mandatory"], bool), f"The 'mandatory' in {key} is not a boolean."


def test_timeout_values(product_locators):
    """
     Checks the data type of the 'timeout' field.
     """
    for key, value in product_locators.items():
        assert isinstance(value["timeout"], int), f"The 'timeout' in {key} is not an integer."
        assert value["timeout"] >= 0, f"The 'timeout' in {key} is negative."


def test_timeout_for_event_values(product_locators):
    """
    Checks the allowed values of the 'timeout_for_event' field.
    """
    allowed_values = ["presence_of_element_located", None]
    for key, value in product_locators.items():
        assert value["timeout_for_event"] in allowed_values, f"The 'timeout_for_event' in {key} has an invalid value."


def test_event_values(product_locators):
    """
        Checks the allowed values of the 'event' field.
    """
    allowed_values = ["screenshot()", None]
    for key, value in product_locators.items():
        if key == "description_short":
             assert isinstance(value["event"], list)
             for item in value["event"]:
                  assert item in allowed_values or item is None
        else:
            assert value["event"] in allowed_values or value["event"] is None, f"The 'event' in {key} has an invalid value."

def test_logic_for_attribute_values(product_locators):
     """
     Checks the allowed values of the 'logic for attribue[AND|OR|XOR|VALUE|null]' field.
     """
     allowed_values = [ None, "AND", "OR", "XOR", "VALUE"]
     for key, value in product_locators.items():
         if key == "description_short":
             assert isinstance(value["logic for attribue[AND|OR|XOR|VALUE|null]"], list)
             for item in value["logic for attribue[AND|OR|XOR|VALUE|null]"]:
                 assert item in allowed_values
         
def test_logic_for_action_values(product_locators):
    """
    Checks the allowed values of the 'logic for action[AND|OR|XOR|VALUE|null]' field.
    """
    allowed_values = [None, "AND", "OR", "XOR", "VALUE"]
    for key, value in product_locators.items():
        if key == "description_short":
            assert isinstance(value["logic for action[AND|OR|XOR|VALUE|null]"], list)
            for item in value["logic for action[AND|OR|XOR|VALUE|null]"]:
                assert item in allowed_values
        elif key == "Screenshot":
            assert value["logic for action[AND|OR|XOR|VALUE|null]"] in allowed_values



def test_locator_description_is_string(product_locators):
    """
        Checks the 'locator_description' is string if exists
    """
    for key, value in product_locators.items():
        if "locator_description" in value:
            assert isinstance(value["locator_description"], str), f"The 'locator_description' in {key} is not string."

```