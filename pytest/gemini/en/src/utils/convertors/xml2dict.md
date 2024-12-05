```python
import pytest
import xml.etree.ElementTree as ET
from hypotez.src.utils.convertors.xml2dict import xml2dict, ET2dict, _parse_node, _make_dict

# Test data
valid_xml_string = """<root attr1=\"value1\" attr2=\"value2\">\n  <child>text</child>\n</root>"""
valid_xml_string_with_children = """<root>\n  <child1>value1</child1>\n  <child2>value2</child2>\n</root>"""
valid_xml_string_nested = """<root>\n  <child attr3=\"value3\">\n    <grandchild>grandchild text</grandchild>\n  </child>\n</root>"""
invalid_xml_string = "<root attr1=\"value1 attr2=\"value2\"/>"
invalid_xml_string_bad_format = "<root attr1=\"value1\" attr2 value2\"/>"
xml_with_href = '<root xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.w3.org/TR/html4/strict.dtd" href="somelink"></root>'

def test_xml2dict_valid_input():
    """Tests xml2dict with a valid XML string."""
    expected_output = {'root': {'attrs': {'attr1': 'value1', 'attr2': 'value2'}, 'child': {'value': 'text'}}}
    assert xml2dict(valid_xml_string) == expected_output

def test_xml2dict_multiple_children():
    """Tests xml2dict with XML containing multiple children."""
    expected_output = {'root': {'child1': {'value': 'value1'}, 'child2': {'value': 'value2'}}}
    assert xml2dict(valid_xml_string_with_children) == expected_output

def test_xml2dict_nested_elements():
    """Tests xml2dict with nested XML elements."""
    expected_output = {'root': {'child': {'attrs': {'attr3': 'value3'}, 'grandchild': {'value': 'grandchild text'}}}}
    assert xml2dict(valid_xml_string_nested) == expected_output


def test_xml2dict_invalid_xml():
    """Tests xml2dict with invalid XML string."""
    with pytest.raises(ET.ParseError):
        xml2dict(invalid_xml_string)

def test_xml2dict_invalid_format():
    with pytest.raises(ET.ParseError):
        xml2dict(invalid_xml_string_bad_format)

def test_ET2dict_valid_input():
  """Tests ET2dict with a valid ElementTree object."""
  root = ET.fromstring(valid_xml_string)
  expected_output = {'root': {'attrs': {'attr1': 'value1', 'attr2': 'value2'}, 'child': {'value': 'text'}}}
  assert ET2dict(root) == expected_output

def test_parse_node_no_attributes_or_children():
  """Tests _parse_node with an element having no attributes or children."""
  element = ET.Element('element')
  assert _parse_node(element) == " "


def test_parse_node_with_href_attribute():
  """Tests _parse_node with an element having href attribute."""
  element_with_href = ET.Element('element', {'{http://www.w3.org/1999/xlink}href': 'somelink'})
  assert _parse_node(element_with_href) == {}  # The href attribute should be skipped


def test_parse_node_with_multiple_children():
  """Tests _parse_node with an element having multiple children."""
  element = ET.fromstring("<root><child>value1</child><child>value2</child></root>")
  assert _parse_node(element)['child'] == [{'value': 'value1'}, {'value': 'value2'}]
  


def test_xml_with_href():
  """Tests _parse_node with href attribute."""
  element = ET.fromstring(xml_with_href)
  result = _parse_node(element)
  assert result == {}



```