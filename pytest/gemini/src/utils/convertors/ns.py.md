```python
import pytest
from types import SimpleNamespace
from pathlib import Path
from src.utils.convertors.ns import ns2dict, ns2csv, ns2xml, ns2xls
import json
from unittest.mock import patch
from src.utils.csv import save_csv_file
from src.utils.xls import save_xls_file

@pytest.fixture
def simple_ns_data():
    """Provides a sample SimpleNamespace object for testing."""
    return SimpleNamespace(
        name="Test",
        value=123,
        nested=SimpleNamespace(
            item1="Nested Item",
            item2=456,
            deeply_nested=SimpleNamespace(
                sub_item1="Deep Item"
            )
        ),
        list_data = [1,2, SimpleNamespace(item = 3)],
        dict_data = {"key1": 1, "key2":SimpleNamespace(item = 2)}
    )

@pytest.fixture
def simple_dict_data():
    return {
            "name": "Test",
            "value": 123,
            "nested": {
                "item1": "Nested Item",
                "item2": 456,
                 "deeply_nested": {
                    "sub_item1": "Deep Item"
                    }
                },
            "list_data" : [1,2, {'item' : 3}],
            "dict_data" : {"key1": 1, "key2": {'item' : 2}}
        }

def test_ns2dict_valid_input(simple_ns_data, simple_dict_data):
    """Checks correct conversion of a SimpleNamespace to a dictionary."""
    result = ns2dict(simple_ns_data)
    assert result == simple_dict_data

def test_ns2dict_empty_ns():
    """Checks correct conversion of an empty SimpleNamespace."""
    empty_ns = SimpleNamespace()
    assert ns2dict(empty_ns) == {}

def test_ns2dict_nested_ns(simple_ns_data):
    """Checks correct handling of nested SimpleNamespace objects."""
    result = ns2dict(simple_ns_data)
    assert isinstance(result["nested"], dict)
    assert isinstance(result["nested"]["deeply_nested"], dict)

def test_ns2csv_valid_input(simple_ns_data, tmp_path):
    """Checks successful CSV conversion and file creation."""
    csv_file = tmp_path / "test.csv"
    with patch("src.utils.convertors.ns.save_csv_file") as mock_save_csv:
        result = ns2csv(simple_ns_data, csv_file)
        assert result is True
        mock_save_csv.assert_called_once()

def test_ns2csv_exception(simple_ns_data, tmp_path):
    """Checks handling of exceptions during CSV conversion."""
    csv_file = tmp_path / "test.csv"
    with patch("src.utils.convertors.ns.save_csv_file", side_effect=Exception("Test Exception")):
       result = ns2csv(simple_ns_data, csv_file)
       assert result is None

def test_ns2xml_valid_input(simple_ns_data):
    """Checks successful XML conversion and string output."""
    result = ns2xml(simple_ns_data)
    assert isinstance(result, str)
    assert "<name>Test</name>" in result
    assert "<item1>Nested Item</item1>" in result
    assert "<sub_item1>Deep Item</sub_item1>" in result

def test_ns2xml_custom_root_tag(simple_ns_data):
    """Checks XML conversion with a custom root tag."""
    result = ns2xml(simple_ns_data, root_tag="custom_root")
    assert "<custom_root>" in result
    assert "</custom_root>" in result
    
def test_ns2xml_exception(simple_ns_data):
    """Checks handling of exceptions during XML conversion."""
    with patch("src.utils.convertors.ns.xml2dict", side_effect=Exception("Test Exception")):
        result = ns2xml(simple_ns_data)
        assert result is None

def test_ns2xls_valid_input(simple_ns_data, tmp_path):
    """Checks successful XLS conversion and file creation."""
    xls_file = tmp_path / "test.xls"
    with patch("src.utils.convertors.ns.save_xls_file") as mock_save_xls:
        result = ns2xls(simple_ns_data, xls_file)
        assert result is True
        mock_save_xls.assert_called_once()
    

def test_ns2xls_exception(simple_ns_data, tmp_path):
    """Checks handling of exceptions during XLS conversion."""
    xls_file = tmp_path / "test.xls"
    with patch("src.utils.convertors.ns.save_xls_file", side_effect=Exception("Test Exception")):
        result = ns2xls(simple_ns_data, xls_file)
        assert result is None
```