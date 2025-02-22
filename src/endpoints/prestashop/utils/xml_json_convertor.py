## \file /src/endpoints/prestashop/utils/xml_json_convertor.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: src.endpoints.prestashop.utils.xml_json_convertor
	:platform: Windows, Unix
	:synopsis: provides utilities for converting XML data into dictionaries. It includes functions for parsing XML strings and converting XML element trees into dictionary representations.
"""
import json
import re
import xml.etree.ElementTree as ET

def dict2xml(json_obj: dict, root_name: str = "product") -> str:
    """! Converts a JSON dictionary to an XML string.

    Args:
        json_obj (dict): JSON dictionary to convert.
        root_name (str, optional): Root element name. Defaults to "product".

    Returns:
        str: XML string representation of the JSON.
    """
    
    def build_xml_element(parent, data):
        """Recursively constructs XML elements from JSON data."""
        if isinstance(data, dict):
            for key, value in data.items():
                if key.startswith("@"):  # Attribute
                    parent.set(key[1:], value)
                elif key == "#text":  # Text value
                    parent.text = value
                else:
                    if isinstance(value, list):
                        for item in value:
                            child = ET.SubElement(parent, key)
                            build_xml_element(child, item)
                    else:
                        child = ET.SubElement(parent, key)
                        build_xml_element(child, value)
        elif isinstance(data, list):
            for item in data:
                build_xml_element(parent, item)
        else:
            parent.text = str(data)

    # Create root element
    root = ET.Element(root_name)
    build_xml_element(root, json_obj[root_name])

    # Convert XML tree to string
    return ET.tostring(root, encoding="utf-8").decode("utf-8")

def _parse_node(node: ET.Element) -> dict | str:
    """Parse an XML node into a dictionary.

    Args:
        node (ET.Element): The XML element to parse.

    Returns:
        dict | str: A dictionary representation of the XML node, or a string if the node has no attributes or children.
    """
    tree = {}
    attrs = {}
    for attr_tag, attr_value in node.attrib.items():
        # Skip href attributes, not supported when converting to dict
        if attr_tag == '{http://www.w3.org/1999/xlink}href':
            continue
        attrs.update(_make_dict(attr_tag, attr_value))

    value = node.text.strip() if node.text is not None else ''

    if attrs:
        tree['attrs'] = attrs

    # Save children
    has_child = False
    for child in list(node):
        has_child = True
        ctag = child.tag
        ctree = _parse_node(child)
        cdict = _make_dict(ctag, ctree)

        # No value when there are child elements
        if ctree:
            value = ''

        # First time an attribute is found
        if ctag not in tree:  # First time found
            tree.update(cdict)
            continue

        # Many times the same attribute, change to a list
        old = tree[ctag]
        if not isinstance(old, list):
            tree[ctag] = [old]  # Change to list
        tree[ctag].append(ctree)  # Add new entry

    if not has_child:
        tree['value'] = value

    # If there is only a value; no attribute, no child, return directly the value
    if list(tree.keys()) == ['value']:
        tree = tree['value']
    return tree

def _make_dict(tag: str, value: any) -> dict:
    """Generate a new dictionary with tag and value.

    Args:
        tag (str): The tag name of the XML element.
        value (any): The value associated with the tag.

    Returns:
        dict: A dictionary with the tag name as the key and the value as the dictionary value.
    """
    tag_values = value
    result = re.compile(r"\{(.*)\}(.*)").search(tag)
    if result:
        tag_values = {'value': value}
        tag_values['xmlns'], tag = result.groups()  # We have a @namespace src!
    return {tag: tag_values}

def xml2dict(xml: str) -> dict:
    """Parse XML string into a dictionary.

    Args:
        xml (str): The XML string to parse.

    Returns:
        dict: The dictionary representation of the XML.
    """
    element_tree = ET.fromstring(xml)
    return ET2dict(element_tree)

def ET2dict(element_tree: ET.Element) -> dict:
    """Convert an XML element tree into a dictionary.

    Args:
        element_tree (ET.Element): The XML element tree.

    Returns:
        dict: The dictionary representation of the XML element tree.
    """
    return _make_dict(element_tree.tag, _parse_node(element_tree))


import xml.etree.ElementTree as ET

def presta_fields_to_xml(presta_fields_dict: dict) -> str:
    """! Converts a JSON dictionary to an XML string with a fixed root name 'prestashop'.

    Args:
        presta_fields_dict (dict): JSON dictionary containing the data (without 'prestashop' key).

    Returns:
        str: XML string representation of the JSON.
    """

    def build_xml_element(parent, data):
        """Recursively constructs XML elements from JSON data."""
        if isinstance(data, dict):
            for key, value in data.items():
                if key.startswith("@"):  # Attribute
                    parent.set(key[1:], value)
                elif key == "#text":  # Text value
                    parent.text = value
                else:
                    if isinstance(value, list):
                        for item in value:
                            child = ET.SubElement(parent, key)
                            build_xml_element(child, item)
                    else:
                        child = ET.SubElement(parent, key)
                        build_xml_element(child, value)
        elif isinstance(data, list):
            for item in data:
                build_xml_element(parent, item)
        else:
            parent.text = str(data)

    if not presta_fields_dict:
        return ""

    dynamic_key = next(iter(presta_fields_dict))  # Берём первый ключ (например, 'product', 'category' и т. д.)

    # Создаём корневой элемент "prestashop"
    root = ET.Element("prestashop")
    dynamic_element = ET.SubElement(root, dynamic_key)
    build_xml_element(dynamic_element, presta_fields_dict[dynamic_key])

    # Конвертируем в строку
    return ET.tostring(root, encoding="utf-8").decode("utf-8")


# Пример JSON 
"""
json_data = {
    "product": {
        "name": {
            "language": [
                {
                    "@id": "1",
                    "#text": "Test Product"
                },
                {
                    "@id": "2",
                    "#text": "Test Product"
                },
                {
                    "@id": "3",
                    "#text": "Test Product"
                }
            ]
        },
        "price": "10.00",
        "id_tax_rules_group": "13",
        "id_category_default": "2"
    }
}

xml_output = presta_fields_to_xml(json_data)
print(xml_output)
"""
