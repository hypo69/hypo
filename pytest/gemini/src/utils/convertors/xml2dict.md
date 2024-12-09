```python
import pytest
import xml.etree.ElementTree as ET
from hypotez.src.utils.convertors.xml2dict import xml2dict, ET2dict, _parse_node, _make_dict

# Fixture for creating XML strings
@pytest.fixture
def xml_strings():
    return [
        '<root><child>hello</child></root>',
        '<root><child attr="value">hello</child></root>',
        '<root><child attr="value1" attr2="value2"></child></root>',
        '<root><child>hello</child><child>world</child></root>',
        '<root><child xmlns:test="http://example.com">hello</child></root>',
        '<root><child><grandchild>hello</grandchild></child></root>',
        '<root><child><grandchild>hello</grandchild><grandchild>world</grandchild></child></root>',
        '<root><child><grandchild href="some_link">hello</grandchild></child></root>', # testing href skipping
        '<root><child><grandchild>hello</grandchild></child><child><grandchild>world</grandchild></child></root>', # testing multiple children
        '<root><child attr="value1" attr2="value2"><grandchild>hello</grandchild></child></root>',  # combining children and attributes
        '<root><tag1>val1</tag1><tag2>val2</tag2></root>',  # Testing multiple tags
        '<root><tag1>val1</tag1><tag1>val2</tag1></root>', # Testing repeated tag
        '<root/>',  # Empty root tag
        '<root></root>'  # Empty root tag with no children or attributes
    ]

# Test Cases for xml2dict
def test_xml2dict_valid_input(xml_strings):
    """Tests xml2dict with valid XML strings."""
    for xml_string in xml_strings:
        try:
            result = xml2dict(xml_string)
            assert isinstance(result, dict)
        except Exception as e:
            pytest.fail(f"Failed with XML: {xml_string} with error: {e}")

def test_xml2dict_invalid_input():
    """Tests xml2dict with invalid XML string."""
    with pytest.raises(ET.ParseError):
        xml2dict("<invalid_xml>")

def test_ET2dict_valid_input(xml_strings):
    """Test ET2dict with valid XML element trees."""
    for xml_string in xml_strings:
        try:
            element_tree = ET.fromstring(xml_string)
            result = ET2dict(element_tree)
            assert isinstance(result, dict)
        except Exception as e:
            pytest.fail(f"Failed with XML: {xml_string} with error: {e}")

def test_ET2dict_invalid_input():
    """Test ET2dict with invalid XML element tree."""
    with pytest.raises(ET.ParseError):
        element_tree = ET.fromstring("<invalid_xml>")
        ET2dict(element_tree)

# Test Cases for _parse_node
def test__parse_node_valid_input(xml_strings):
    """Tests _parse_node with valid XML element."""
    for xml_string in xml_strings:
        element_tree = ET.fromstring(xml_string)
        try:
            result = _parse_node(element_tree.getroot())
            assert isinstance(result, dict)
        except Exception as e:
            pytest.fail(f"Failed with XML: {xml_string} with error: {e}")

def test__parse_node_no_attributes_no_children():
    """Test _parse_node with element having no attributes or children."""
    element = ET.Element("node")
    result = _parse_node(element)
    assert result == ""
    

def test__parse_node_with_href():
  """Test _parse_node with element having an href attribute."""
  element = ET.Element("node", {'{http://www.w3.org/1999/xlink}href': 'some_link', 'attr': 'value'})
  result = _parse_node(element)
  assert 'attrs' in result and 'attr' in result['attrs'] and result['attrs']['attr'] == {'value': 'value'}
  assert '{http://www.w3.org/1999/xlink}href' not in result['attrs']

# Test Cases for _make_dict
def test__make_dict_with_namespace():
    """Test _make_dict with an XML element containing namespace."""
    tag = '{test}tag'
    value = 'value'
    expected_dict = {'test': {'value': 'value'}}
    result = _make_dict(tag, value)
    assert result == expected_dict
```