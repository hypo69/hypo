```python
import pytest
import xml.etree.ElementTree as ET
from hypotez.src.utils.convertors.xml2dict import xml2dict, ET2dict, _parse_node, _make_dict

# Fixture definitions
@pytest.fixture
def simple_xml():
    """Provides simple XML string for testing."""
    return "<root><child attr1='value1' attr2='value2'>text</child></root>"

@pytest.fixture
def complex_xml():
    """Provides complex XML string for testing."""
    return """
    <root xmlns="http://example.com">
        <child attr1="value1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="type1">text1</child>
        <child attr2="value2">text2</child>
        <child>text3</child>
    </root>
    """

@pytest.fixture
def empty_xml():
    """Provides empty XML string for testing."""
    return "<root></root>"

@pytest.fixture
def element_tree_fixture(complex_xml):
    """Creates an XML element tree."""
    return ET.fromstring(complex_xml)

# Tests for _parse_node
def test__parse_node_valid_input(simple_xml, complex_xml):
    """Checks correct behavior of _parse_node with valid input."""
    root = ET.fromstring(simple_xml)
    result = _parse_node(root)
    assert result == {"child": {"attrs": {"attr1": "value1", "attr2": "value2"}, "value": "text"}}
    result_2 = _parse_node(ET.fromstring(complex_xml))
    assert isinstance(result_2, dict)

def test__parse_node_empty_text(empty_xml):
    """Checks _parse_node handling of empty text nodes."""
    root = ET.fromstring(empty_xml)
    result = _parse_node(root)
    assert result == {"value": ""}

def test__parse_node_with_namespace(complex_xml):
    """Tests _parse_node with XML namespaces."""
    root = ET.fromstring(complex_xml)
    result = _parse_node(root.find('child'))
    assert 'xmlns' in result['child']['attrs']

# Tests for xml2dict
def test_xml2dict_valid_input(simple_xml):
    """Checks correct behavior of xml2dict with valid input."""
    result = xml2dict(simple_xml)
    assert result == {"root": {"child": {"attrs": {"attr1": "value1", "attr2": "value2"}, "value": "text"}}}

def test_xml2dict_complex_input(complex_xml):
    """Checks xml2dict with more complex XML structure."""
    result = xml2dict(complex_xml)
    assert isinstance(result, dict)
    assert len(result['root']['child']) > 0

def test_xml2dict_empty_input():
    """Checks xml2dict with an empty XML string."""
    with pytest.raises(Exception) as excinfo:
        xml2dict("")

# Tests for ET2dict
def test_ET2dict(element_tree_fixture):
    """Checks ET2dict function with provided xml."""
    result = ET2dict(element_tree_fixture)
    assert isinstance(result, dict)
    assert 'root' in result


# Test handling of empty XML
def test_xml2dict_empty_xml(empty_xml):
    """Test xml2dict on empty XML."""
    result = xml2dict(empty_xml)
    assert result == {"root": {}}

#Test _make_dict with namespaces
def test__make_dict_with_namespace():
    tag = '{http://example.com}child'
    value = 'value'
    result = _make_dict(tag, value)
    assert result == {tag: {'value': value, 'xmlns': 'http://example.com'}}

```