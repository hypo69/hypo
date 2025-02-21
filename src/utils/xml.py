## \file /src/utils/xml.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: src.utils.xml 
	:platform: Windows, Unix
	:synopsis: 

"""

import xml.etree.ElementTree as ET
from xml.dom import minidom
import re

def clean_empty_cdata(xml_string: str) -> str:
    """! Cleans empty CDATA sections and unnecessary whitespace in XML string.

    Args:
        xml_string (str): Raw XML content.

    Returns:
        str: Cleaned and formatted XML content.
    """
    root = ET.fromstring(xml_string)
    
    def remove_empty_elements(element):
        for child in list(element):
            remove_empty_elements(child)
            if not (child.text and child.text.strip()) and not child.attrib and not list(child):
                element.remove(child)

    remove_empty_elements(root)
    cleaned_xml = ET.tostring(root, encoding="utf-8").decode("utf-8")
    cleaned_xml = re.sub(r">\s+<", "><", cleaned_xml)  # Remove unnecessary whitespace
    return cleaned_xml

def save_xml(xml_string: str, file_path: str) -> None:
    """! Saves cleaned XML data from a string to a file with indentation.

    Args:
        xml_string (str): XML content as a string.
        file_path (str): Path to the output file.

    Returns:
        None
    """
    # Очистка XML от пустых элементов
    cleaned_xml = clean_empty_cdata(xml_string)
    
    # Парсим XML-строку
    xml_tree = ET.ElementTree(ET.fromstring(cleaned_xml))
    
    # Преобразуем в строку с отступами
    rough_string = ET.tostring(xml_tree.getroot(), encoding="utf-8")
    parsed_xml = minidom.parseString(rough_string)
    pretty_xml = parsed_xml.toprettyxml(indent="  ")

    # Записываем в файл
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(pretty_xml)




if __name__ == '__main__':
    ...
    # Пример использования
    # xml_data = """<root><item>Value</item><item attr="test">Another</item></root>"""
    # save_xml(xml_data, "output.xml")
