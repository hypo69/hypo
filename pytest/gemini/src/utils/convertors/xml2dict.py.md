```python
import pytest
import xml.etree.ElementTree as ET
from hypotez.src.utils.convertors.xml2dict import _parse_node, _make_dict, xml2dict, ET2dict

# Fixture definitions, if needed
@pytest.fixture
def example_xml_simple():
    """Provides a simple XML string for testing."""
    return "<root>text</root>"

@pytest.fixture
def example_xml_with_attributes():
    """Provides an XML string with attributes for testing."""
    return "<root attr1='value1' attr2='value2'>text</root>"

@pytest.fixture
def example_xml_with_children():
    """Provides an XML string with child elements for testing."""
    return "<root><child1>text1</child1><child2>text2</child2></root>"

@pytest.fixture
def example_xml_with_nested_children():
    """Provides an XML string with nested child elements for testing."""
    return "<root><child1><grandchild>text1</grandchild></child1></root>"

@pytest.fixture
def example_xml_with_duplicate_children():
    """Provides an XML string with duplicate child elements for testing."""
    return "<root><child>text1</child><child>text2</child></root>"

@pytest.fixture
def example_xml_with_namespace():
    """Provides an XML string with namespace for testing."""
    return '<root xmlns:ns="http://example.com"><ns:child>text</ns:child></root>'


@pytest.fixture
def example_xml_with_namespaced_attribute():
    """Provides an XML string with namespaced attribute for testing."""
    return '<root xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="some_link">text</root>'


@pytest.fixture
def example_xml_empty_text():
    """Provides an XML string with empty text"""
    return "<root></root>"

# Tests for _parse_node function
def test_parse_node_simple_element(example_xml_simple):
    """Checks correct parsing of a simple XML element."""
    root = ET.fromstring(example_xml_simple)
    result = _parse_node(root)
    assert result == "text"

def test_parse_node_element_with_attributes(example_xml_with_attributes):
    """Checks correct parsing of an XML element with attributes."""
    root = ET.fromstring(example_xml_with_attributes)
    result = _parse_node(root)
    assert result == {'attrs': {'attr1': 'value1', 'attr2': 'value2'}, 'value': 'text'}

def test_parse_node_element_with_children(example_xml_with_children):
    """Checks correct parsing of an XML element with child elements."""
    root = ET.fromstring(example_xml_with_children)
    result = _parse_node(root)
    assert result == {'child1': {'value': 'text1'}, 'child2': {'value': 'text2'}}

def test_parse_node_element_with_nested_children(example_xml_with_nested_children):
    """Checks correct parsing of an XML element with nested child elements."""
    root = ET.fromstring(example_xml_with_nested_children)
    result = _parse_node(root)
    assert result == {'child1': {'grandchild': {'value': 'text1'}}}

def test_parse_node_element_with_duplicate_children(example_xml_with_duplicate_children):
    """Checks correct parsing of an XML element with duplicate child elements."""
    root = ET.fromstring(example_xml_with_duplicate_children)
    result = _parse_node(root)
    assert result == {'child': [{'value': 'text1'}, {'value': 'text2'}]}

def test_parse_node_element_with_empty_text(example_xml_empty_text):
    """Checks correct parsing of an XML element with empty text."""
    root = ET.fromstring(example_xml_empty_text)
    result = _parse_node(root)
    assert result == {'value': ''}
    

def test_parse_node_element_with_namespaced_attribute(example_xml_with_namespaced_attribute):
    """Checks if xlink:href attribute is ignored."""
    root = ET.fromstring(example_xml_with_namespaced_attribute)
    result = _parse_node(root)
    assert result == {'value': 'text'}



# Tests for _make_dict function
def test_make_dict_simple_tag_value():
    """Checks correct dictionary creation with a simple tag and value."""
    result = _make_dict('tag', 'value')
    assert result == {'tag': 'value'}


def test_make_dict_tag_with_namespace():
    """Checks correct dictionary creation with a tag that has a namespace"""
    result = _make_dict('{http://example.com}tag', 'value')
    assert result == {'tag': {'value': 'value', 'xmlns': 'http://example.com'}}

# Tests for xml2dict function
def test_xml2dict_simple_xml(example_xml_simple):
    """Checks correct parsing of a simple XML string."""
    result = xml2dict(example_xml_simple)
    assert result == {'root': 'text'}

def test_xml2dict_xml_with_attributes(example_xml_with_attributes):
    """Checks correct parsing of an XML string with attributes."""
    result = xml2dict(example_xml_with_attributes)
    assert result == {'root': {'attrs': {'attr1': 'value1', 'attr2': 'value2'}, 'value': 'text'}}

def test_xml2dict_xml_with_children(example_xml_with_children):
    """Checks correct parsing of an XML string with child elements."""
    result = xml2dict(example_xml_with_children)
    assert result == {'root': {'child1': {'value': 'text1'}, 'child2': {'value': 'text2'}}}


def test_xml2dict_xml_with_nested_children(example_xml_with_nested_children):
    """Checks correct parsing of an XML string with nested child elements."""
    result = xml2dict(example_xml_with_nested_children)
    assert result == {'root': {'child1': {'grandchild': {'value': 'text1'}}}}
    
def test_xml2dict_xml_with_duplicate_children(example_xml_with_duplicate_children):
    """Checks correct parsing of an XML string with duplicate child elements."""
    result = xml2dict(example_xml_with_duplicate_children)
    assert result == {'root': {'child': [{'value': 'text1'}, {'value': 'text2'}]}}
    
def test_xml2dict_xml_with_namespace(example_xml_with_namespace):
    """Checks correct parsing of an XML string with namespace."""
    result = xml2dict(example_xml_with_namespace)
    assert result == {'root': {'child': {'value': 'text', 'xmlns': 'http://example.com'}}}

def test_xml2dict_invalid_xml():
    """Checks correct handling of invalid XML input."""
    with pytest.raises(ET.ParseError):
        xml2dict("<invalid_xml>")

# Tests for ET2dict function
def test_et2dict_simple_element(example_xml_simple):
    """Checks correct conversion of a simple XML element tree."""
    element_tree = ET.fromstring(example_xml_simple)
    result = ET2dict(element_tree)
    assert result == {'root': 'text'}

def test_et2dict_element_with_attributes(example_xml_with_attributes):
    """Checks correct conversion of an XML element tree with attributes."""
    element_tree = ET.fromstring(example_xml_with_attributes)
    result = ET2dict(element_tree)
    assert result == {'root': {'attrs': {'attr1': 'value1', 'attr2': 'value2'}, 'value': 'text'}}
    
def test_et2dict_element_with_children(example_xml_with_children):
    """Checks correct conversion of an XML element tree with child elements."""
    element_tree = ET.fromstring(example_xml_with_children)
    result = ET2dict(element_tree)
    assert result == {'root': {'child1': {'value': 'text1'}, 'child2': {'value': 'text2'}}}

def test_et2dict_element_with_nested_children(example_xml_with_nested_children):
    """Checks correct conversion of an XML element tree with nested child elements."""
    element_tree = ET.fromstring(example_xml_with_nested_children)
    result = ET2dict(element_tree)
    assert result == {'root': {'child1': {'grandchild': {'value': 'text1'}}}}

def test_et2dict_element_with_duplicate_children(example_xml_with_duplicate_children):
    """Checks correct conversion of an XML element tree with duplicate child elements."""
    element_tree = ET.fromstring(example_xml_with_duplicate_children)
    result = ET2dict(element_tree)
    assert result == {'root': {'child': [{'value': 'text1'}, {'value': 'text2'}]}}

def test_et2dict_element_with_namespace(example_xml_with_namespace):
    """Checks correct conversion of an XML element tree with a namespace."""
    element_tree = ET.fromstring(example_xml_with_namespace)
    result = ET2dict(element_tree)
    assert result == {'root': {'child': {'value': 'text', 'xmlns': 'http://example.com'}}}

def test_et2dict_empty_text(example_xml_empty_text):
    """Checks correct conversion of an XML element tree with empty text."""
    element_tree = ET.fromstring(example_xml_empty_text)
    result = ET2dict(element_tree)
    assert result == {'root': {'value': ''}}
```