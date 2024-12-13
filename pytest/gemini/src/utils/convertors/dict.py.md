```python
import pytest
from types import SimpleNamespace
from pathlib import Path
from src.utils.convertors.dict import (
    replace_key_in_dict,
    dict2pdf,
    dict2ns,
    dict2xml,
    dict2csv,
    dict2xls,
    dict2html,
)
import json
import xml.etree.ElementTree as ET
import csv
import os
from tempfile import NamedTemporaryFile


# Fixture definitions
@pytest.fixture
def sample_dict():
    """Provides a sample dictionary for testing."""
    return {
        "name": "John",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
        },
        "hobbies": ["reading", "coding"],
    }


@pytest.fixture
def sample_list_of_dicts():
    """Provides a sample list of dictionaries for testing."""
    return [
        {"name": "John", "age": 30},
        {"name": "Jane", "age": 25},
    ]


@pytest.fixture
def sample_nested_list():
    """Provides a sample nested list for testing."""
    return [
        {"inner": [{"name": "Item1"}, {"name": "Item2"}]},
        {"inner": [{"name": "Item3"}, {"name": "Item4"}]}
    ]


@pytest.fixture
def sample_simple_namespace():
    """Provides a sample SimpleNamespace for testing."""
    return SimpleNamespace(
        name="John",
        age=30,
        address=SimpleNamespace(street="123 Main St", city="Anytown"),
        hobbies=["reading", "coding"],
    )


@pytest.fixture
def temp_file_path():
    """Provides a temporary file path for testing file operations."""
    temp_file = NamedTemporaryFile(delete=False, suffix=".test")
    temp_file_path = temp_file.name
    temp_file.close()  # Close the file so it can be used by other functions.
    yield temp_file_path
    os.unlink(temp_file_path)  # Clean up the temporary file after testing.


# Tests for replace_key_in_dict function
def test_replace_key_in_dict_simple_dict(sample_dict):
    """Tests key replacement in a simple dictionary."""
    updated_dict = replace_key_in_dict(sample_dict, "name", "category_name")
    assert "category_name" in updated_dict
    assert "name" not in updated_dict
    assert updated_dict["category_name"] == "John"
    assert updated_dict["age"] == 30


def test_replace_key_in_dict_nested_dict(sample_dict):
    """Tests key replacement in a nested dictionary."""
    updated_dict = replace_key_in_dict(sample_dict, "street", "road")
    assert "road" in updated_dict["address"]
    assert "street" not in updated_dict["address"]
    assert updated_dict["address"]["road"] == "123 Main St"


def test_replace_key_in_dict_list_of_dicts(sample_list_of_dicts):
    """Tests key replacement in a list of dictionaries."""
    updated_list = replace_key_in_dict(sample_list_of_dicts, "name", "category_name")
    for item in updated_list:
        assert "category_name" in item
        assert "name" not in item
    assert updated_list[0]["category_name"] == "John"
    assert updated_list[1]["category_name"] == "Jane"


def test_replace_key_in_dict_nested_list(sample_nested_list):
    """Tests key replacement in a nested list of dictionaries."""
    updated_list = replace_key_in_dict(sample_nested_list, "name", "category_name")
    for item in updated_list:
      for inner_item in item["inner"]:
        assert "category_name" in inner_item
        assert "name" not in inner_item
    assert updated_list[0]["inner"][0]["category_name"] == "Item1"


def test_replace_key_in_dict_key_not_found(sample_dict):
    """Tests key replacement when the old key is not present."""
    updated_dict = replace_key_in_dict(sample_dict, "city_name", "category_name")
    assert updated_dict == sample_dict


def test_replace_key_in_dict_empty_dict():
    """Tests key replacement on an empty dictionary."""
    updated_dict = replace_key_in_dict({}, "name", "category_name")
    assert updated_dict == {}


def test_replace_key_in_dict_empty_list():
    """Tests key replacement on an empty list."""
    updated_list = replace_key_in_dict([], "name", "category_name")
    assert updated_list == []


# Tests for dict2pdf function
def test_dict2pdf_valid_dict(sample_dict, temp_file_path):
    """Tests PDF creation with a valid dictionary."""
    dict2pdf(sample_dict, temp_file_path)
    assert os.path.exists(temp_file_path)  # Check if the file was created


def test_dict2pdf_valid_simplenamespace(sample_simple_namespace, temp_file_path):
    """Tests PDF creation with a valid SimpleNamespace."""
    dict2pdf(sample_simple_namespace, temp_file_path)
    assert os.path.exists(temp_file_path)  # Check if the file was created


def test_dict2pdf_empty_dict(temp_file_path):
    """Tests PDF creation with an empty dictionary."""
    dict2pdf({}, temp_file_path)
    assert os.path.exists(temp_file_path)  # Check if the file was created


# Tests for dict2ns function
def test_dict2ns_valid_dict(sample_dict):
    """Tests conversion of a valid dictionary to SimpleNamespace."""
    ns = dict2ns(sample_dict)
    assert isinstance(ns, SimpleNamespace)
    assert ns.name == "John"
    assert ns.age == 30
    assert isinstance(ns.address, SimpleNamespace)
    assert ns.address.street == "123 Main St"
    assert isinstance(ns.hobbies, list)


def test_dict2ns_list_of_dicts(sample_list_of_dicts):
    """Tests conversion of a list of dictionaries to a list of SimpleNamespaces."""
    ns_list = dict2ns(sample_list_of_dicts)
    assert isinstance(ns_list, list)
    for ns in ns_list:
      assert isinstance(ns, SimpleNamespace)
    assert ns_list[0].name == "John"
    assert ns_list[1].age == 25


def test_dict2ns_nested_list(sample_nested_list):
    """Tests conversion of nested list of dictionaries to a SimpleNamespace."""
    ns_list = dict2ns(sample_nested_list)
    assert isinstance(ns_list, list)
    for item in ns_list:
      assert isinstance(item["inner"], list)
      for ns in item["inner"]:
        assert isinstance(ns, SimpleNamespace)
    assert ns_list[0]["inner"][0].name == "Item1"


def test_dict2ns_empty_dict():
    """Tests conversion of an empty dictionary to SimpleNamespace."""
    ns = dict2ns({})
    assert isinstance(ns, SimpleNamespace)
    assert not ns.__dict__  # Check if it's an empty SimpleNamespace


def test_dict2ns_empty_list():
    """Tests conversion of an empty list."""
    ns_list = dict2ns([])
    assert isinstance(ns_list, list)
    assert not ns_list  # Check if it's an empty list


# Tests for dict2xml function
def test_dict2xml_valid_dict(sample_dict):
    """Tests XML generation with a valid dictionary."""
    xml_string = dict2xml({"root": sample_dict})
    root = ET.fromstring(xml_string)
    assert root.tag == "root"
    assert root.find("name").text == "John"
    assert root.find("age").text == "30"
    assert root.find("address").find("street").text == "123 Main St"


def test_dict2xml_with_attributes():
    """Tests XML generation with attributes."""
    data = {"root": {
        "element": {"attrs": {"id": 123, "type": "example"}, "value": "Test Data"}
    }}
    xml_string = dict2xml(data)
    root = ET.fromstring(xml_string)
    element = root.find("element")
    assert element.get("id") == "123"
    assert element.get("type") == "example"
    assert element.text == "Test Data"


def test_dict2xml_list_of_elements():
    """Tests XML generation with list of elements."""
    data = {"root": {
        "items": [{"item": "item1"}, {"item": "item2"}]
    }}
    xml_string = dict2xml(data)
    root = ET.fromstring(xml_string)
    items = root.find("items")
    assert len(list(items)) == 2
    assert items[0].tag == "item"
    assert items[0].text == "item1"
    assert items[1].text == "item2"


def test_dict2xml_empty_dict():
    """Tests XML generation with an empty dictionary."""
    with pytest.raises(Exception, match="Only one root node allowed"):
        dict2xml({})


def test_dict2xml_multiple_roots():
    """Tests XML generation with multiple root nodes, which should raise an error."""
    with pytest.raises(Exception, match="Only one root node allowed"):
        dict2xml({"root1": {"key": "value1"}, "root2": {"key": "value2"}})


# Tests for dict2csv function
def test_dict2csv_valid_dict(sample_dict, temp_file_path):
    """Tests CSV creation with a valid dictionary."""
    result = dict2csv(sample_dict, temp_file_path)
    assert result is True
    assert os.path.exists(temp_file_path)
    with open(temp_file_path, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
        assert len(rows) > 0  # Check if CSV file contains data


def test_dict2csv_valid_simplenamespace(sample_simple_namespace, temp_file_path):
    """Tests CSV creation with a valid SimpleNamespace."""
    result = dict2csv(sample_simple_namespace, temp_file_path)
    assert result is True
    assert os.path.exists(temp_file_path)
    with open(temp_file_path, "r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
        assert len(rows) > 0  # Check if CSV file contains data


def test_dict2csv_empty_dict(temp_file_path):
    """Tests CSV creation with an empty dictionary."""
    result = dict2csv({}, temp_file_path)
    assert result is False # Expect False because no data can be extracted
    assert os.path.exists(temp_file_path)


# Tests for dict2xls function
def test_dict2xls_valid_dict(sample_dict, temp_file_path):
    """Tests XLS creation with a valid dictionary."""
    result = dict2xls(sample_dict, temp_file_path)
    assert result is True
    assert os.path.exists(temp_file_path)


def test_dict2xls_valid_simplenamespace(sample_simple_namespace, temp_file_path):
    """Tests XLS creation with a valid SimpleNamespace."""
    result = dict2xls(sample_simple_namespace, temp_file_path)
    assert result is True
    assert os.path.exists(temp_file_path)


def test_dict2xls_empty_dict(temp_file_path):
    """Tests XLS creation with an empty dictionary."""
    result = dict2xls({}, temp_file_path)
    assert result is False # Expect False because no data can be extracted
    assert os.path.exists(temp_file_path)


# Tests for dict2html function
def test_dict2html_valid_dict(sample_dict):
    """Tests HTML generation with a valid dictionary."""
    html_string = dict2html(sample_dict)
    assert "<table>" in html_string
    assert "John" in html_string
    assert "123 Main St" in html_string
    assert "<ul>" in html_string # Check if list formatting is correct


def test_dict2html_valid_simplenamespace(sample_simple_namespace):
    """Tests HTML generation with a valid SimpleNamespace."""
    html_string = dict2html(sample_simple_namespace)
    assert "<table>" in html_string
    assert "John" in html_string
    assert "123 Main St" in html_string


def test_dict2html_empty_dict():
    """Tests HTML generation with an empty dictionary."""
    html_string = dict2html({})
    assert "<table>" in html_string
    assert "</table>" in html_string  # Should not throw error just give an empty table


def test_dict2html_list_values(sample_dict):
    """Tests HTML generation with a list value."""
    html_string = dict2html(sample_dict)
    assert "<li>reading</li>" in html_string


def test_dict2html_nested_dict_values(sample_dict):
    """Tests HTML generation with a nested dict value."""
    html_string = dict2html(sample_dict)
    assert "<table>" in html_string
    assert "123 Main St" in html_string
    assert "city" in html_string
```