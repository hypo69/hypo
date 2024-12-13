```python
import pytest
from typing import Dict, List, Union

# Define a type alias for the locator structure
Locator = Dict[str, Union[str, int, bool, list, dict, None]]

# Fixture for a sample locator
@pytest.fixture
def sample_locator() -> Locator:
    return {
        "attribute": "innerText",
        "by": "XPATH",
        "selector": "//span[@class = 'ltr sku-copy']",
        "if_list": "first",
        "use_mouse": False,
        "mandatory": True,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": None,
        "locator_description": "SKU Morlevi."
    }

# Fixture for a sample locator with multiple values
@pytest.fixture
def sample_locator_multiple_values() -> Locator:
    return {
        "attribute": [None, "href"],
        "by": ["XPATH", "XPATH"],
        "selector": ["//a[contains(@href, '#tab-description')]", "//div[@id = 'tab-description']//p"],
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": ["click()", None],
        "if_list": "first",
        "use_mouse": [False, False],
        "mandatory": [True, True],
        "locator_description": ["Нажимаю на вкладку для открытия поля description.", "Читаю данные из div."]
    }

# Fixture for a sample locator with dictionary attribute
@pytest.fixture
def sample_locator_dict_attribute() -> Locator:
   return {
        "attribute": {"href": "name"},
        "by": "XPATH",
        "selector": "//a[@id = 'mainpic']//img",
        "if_list": "first",
        "use_mouse": False,
        "mandatory": True,
        "timeout": 0,
        "timeout_for_event": "presence_of_element_located",
        "event": None,
        "locator_description": "Example with dictionary attribute."
   }


def test_locator_structure_valid(sample_locator):
    """Checks if the basic locator structure is valid."""
    assert isinstance(sample_locator, dict)
    assert "attribute" in sample_locator
    assert "by" in sample_locator
    assert "selector" in sample_locator
    assert "if_list" in sample_locator
    assert "use_mouse" in sample_locator
    assert "mandatory" in sample_locator
    assert "timeout" in sample_locator
    assert "timeout_for_event" in sample_locator
    assert "event" in sample_locator
    assert "locator_description" in sample_locator


def test_locator_attribute_types(sample_locator):
    """Checks if the attribute types in a simple locator are correct"""
    assert isinstance(sample_locator["attribute"], str) or sample_locator["attribute"] is None
    assert isinstance(sample_locator["by"], str)
    assert isinstance(sample_locator["selector"], str)
    assert isinstance(sample_locator["if_list"], str)
    assert isinstance(sample_locator["use_mouse"], bool)
    assert isinstance(sample_locator["mandatory"], bool)
    assert isinstance(sample_locator["timeout"], int)
    assert isinstance(sample_locator["timeout_for_event"], str)
    assert isinstance(sample_locator["event"], str) or sample_locator["event"] is None
    assert isinstance(sample_locator["locator_description"], str)

def test_locator_attribute_types_multiple(sample_locator_multiple_values):
    """Checks if attribute types are correct when multiple values are given."""
    assert isinstance(sample_locator_multiple_values["attribute"], list)
    assert all(isinstance(item, str) or item is None for item in sample_locator_multiple_values["attribute"])
    assert isinstance(sample_locator_multiple_values["by"], list)
    assert all(isinstance(item, str) for item in sample_locator_multiple_values["by"])
    assert isinstance(sample_locator_multiple_values["selector"], list)
    assert all(isinstance(item, str) for item in sample_locator_multiple_values["selector"])
    assert isinstance(sample_locator_multiple_values["timeout"], int)
    assert isinstance(sample_locator_multiple_values["timeout_for_event"], str)
    assert isinstance(sample_locator_multiple_values["event"], list)
    assert all(isinstance(item, str) or item is None for item in sample_locator_multiple_values["event"])
    assert isinstance(sample_locator_multiple_values["if_list"], str)
    assert isinstance(sample_locator_multiple_values["use_mouse"], list)
    assert all(isinstance(item, bool) for item in sample_locator_multiple_values["use_mouse"])
    assert isinstance(sample_locator_multiple_values["mandatory"], list)
    assert all(isinstance(item, bool) for item in sample_locator_multiple_values["mandatory"])
    assert isinstance(sample_locator_multiple_values["locator_description"], list)
    assert all(isinstance(item, str) for item in sample_locator_multiple_values["locator_description"])

def test_locator_attribute_dict(sample_locator_dict_attribute):
    """Checks if attribute is a dictionary, if it should be."""
    assert isinstance(sample_locator_dict_attribute["attribute"], dict)
    assert "href" in sample_locator_dict_attribute["attribute"]
    assert isinstance(sample_locator_dict_attribute["attribute"]["href"], str)
    
def test_locator_missing_key():
    """Checks if error is raised if mandatory key is missing"""
    with pytest.raises(KeyError):
       locator = {
            "attribute": "innerText",
            "by": "XPATH",
            # "selector": "//span[@class = 'ltr sku-copy']", # missing selector
            "if_list": "first",
            "use_mouse": False,
            "mandatory": True,
            "timeout": 0,
            "timeout_for_event": "presence_of_element_located",
            "event": None,
            "locator_description": "SKU Morlevi."
       }
       assert "selector" in locator

def test_locator_if_list_valid_values():
    """Checks if if_list has valid values"""
    valid_values = ["first", "all", "last", "even", "odd"]

    for value in valid_values:
      locator: Locator = {
            "attribute": "innerText",
            "by": "XPATH",
            "selector": "//span[@class = 'ltr sku-copy']",
            "if_list": value,
            "use_mouse": False,
            "mandatory": True,
            "timeout": 0,
            "timeout_for_event": "presence_of_element_located",
            "event": None,
            "locator_description": "SKU Morlevi."
        }
      assert locator["if_list"] == value
    
    locator_number: Locator = {
            "attribute": "innerText",
            "by": "XPATH",
            "selector": "//span[@class = 'ltr sku-copy']",
            "if_list": "1,2",
            "use_mouse": False,
            "mandatory": True,
            "timeout": 0,
            "timeout_for_event": "presence_of_element_located",
            "event": None,
            "locator_description": "SKU Morlevi."
    }
    assert locator_number["if_list"] == "1,2"

    locator_number_list: Locator = {
            "attribute": "innerText",
            "by": "XPATH",
            "selector": "//span[@class = 'ltr sku-copy']",
            "if_list": "[1,2]",
            "use_mouse": False,
            "mandatory": True,
            "timeout": 0,
            "timeout_for_event": "presence_of_element_located",
            "event": None,
            "locator_description": "SKU Morlevi."
    }
    assert locator_number_list["if_list"] == "[1,2]"
```