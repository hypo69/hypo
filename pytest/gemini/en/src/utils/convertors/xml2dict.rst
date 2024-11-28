```python
import pytest
import xml.etree.ElementTree as ET
from hypotez.src.utils.convertors.xml2dict import xml2dict, ET2dict, _parse_node, _make_dict

# Test data
valid_xml = """<root attr1='value1' attr2='value2'>\n  <child>text1</child>\n  <child>text2</child>\n</root>"""
valid_xml_nested = """<root>\n  <child attr='val1'>text1</child>\n  <child attr='val2'>\n    <grandchild>text3</grandchild>\n  </child>\n</root>"""
empty_xml = "<root/>"
xml_with_href = "<root xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xsi:schemaLocation='http://www.w3.org/2001/XMLSchema-instance http://www.w3.org/2001/XMLSchema-instance' {http://www.w3.org/1999/xlink}href='example.com'/>"
invalid_xml = "<root attr='value' > <child>text1</child>"


def test_xml2dict_valid_input():
    """Tests xml2dict with valid XML string."""
    expected_dict = {'root': {'attrs': {'attr1': 'value1', 'attr2': 'value2'}, 'child': [{'value': 'text1'}, {'value': 'text2'}]}}
    assert xml2dict(valid_xml) == expected_dict


def test_xml2dict_nested_structure():
    """Tests xml2dict with nested XML structure."""
    expected_dict = {'root': {'child': [{'attrs': {'attr': 'val1'}, 'value': 'text1'}, {'attrs': {'attr': 'val2'}, 'grandchild': [{'value': 'text3'}]}]}}
    assert xml2dict(valid_xml_nested) == expected_dict

def test_xml2dict_empty_xml():
    """Tests xml2dict with empty XML string."""
    expected_dict = {'root': {}}
    assert xml2dict(empty_xml) == expected_dict

def test_xml2dict_href_attribute():
    """Tests xml2dict with href attribute (should be skipped)."""
    expected_dict = {'root': {}}
    assert xml2dict(xml_with_href) == expected_dict

def test_xml2dict_invalid_xml():
    """Tests xml2dict with invalid XML string."""
    with pytest.raises(ET.ParseError):
        xml2dict(invalid_xml)

def test_ET2dict_valid_input():
    """Tests ET2dict with valid ElementTree."""
    element_tree = ET.fromstring(valid_xml)
    expected_dict = {'root': {'attrs': {'attr1': 'value1', 'attr2': 'value2'}, 'child': [{'value': 'text1'}, {'value': 'text2'}]}}
    assert ET2dict(element_tree) == expected_dict


def test_parse_node_valid_input():
    """Tests _parse_node with valid XML node."""
    element_tree = ET.fromstring(valid_xml)
    root_element = element_tree.getroot()
    result = _parse_node(root_element)
    expected_dict = {'attrs': {'attr1': 'value1', 'attr2': 'value2'}, 'child': [{'value': 'text1'}, {'value': 'text2'}]}
    assert result == expected_dict

def test_parse_node_no_children():
    """Tests _parse_node with node having no children."""
    element = ET.Element('node', attr='value')
    element.text = "text"
    result = _parse_node(element)
    expected_dict = {'attrs': {'attr': 'value'}, 'value': 'text'}
    assert result == expected_dict


def test_make_dict_basic():
    """Tests _make_dict with basic tag and value."""
    result = _make_dict("tag", "value")
    assert result == {"tag": "value"}


def test_make_dict_with_namespace():
    """Tests _make_dict with a tag containing namespace."""
    result = _make_dict("{http://example.com}tag", "value")
    assert result == {"tag": {"value": "value"}}



```