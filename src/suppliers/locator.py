## \file ../src/suppliers/locator.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""Module for defining locators with various selection attributes for web elements.

This module provides the Locator class, which represents different strategies
for locating elements on a web page. It supports multiple attributes and can
be initialized from a JSON file to load predefined locator settings.
"""

from dataclasses import dataclass
from types import SimpleNamespace

from src import gs
from src.utils.jjson import j_loads_ns

@dataclass
class Locator:
    """Class for representing a locator with various selection attributes.

    Attributes:
        attribute: содержит название аттрибута вебэлемента. Например: `href`,`innerText`,`src`...
        by: Method of locating the element, such as 'id', 'xpath', etc.
        selector: CSS or XPath selector for locating the element.
        if_list: Condition if there is a list of elements to consider. Может принимать значения: `all`,`first`,`last`,`even`,`odd`
        use_mouse: Indicates if a mouse action is needed, such as click.
        mandatory: Specifies if the locator is required for the operation.
        event: Event that triggers interaction, e.g., `click()`, `hover()`,`send_message()`,`sreenshot()`.
        locator_description: Description of the locator's purpose.
    """
    attribute: str | list | dict | list[dict]
    by: str | list | dict | list[dict]
    selector: str | list | dict | list[dict]
    if_list: str | list | dict | list[dict]
    use_mouse: str | list | dict | list[dict]
    mandatory: str | list | dict | list[dict]
    event: str | list | dict | list[dict]
    locator_description: str | list | dict | list[dict]

    def __post_init__(self):
        locators_path = gs.path.src / 'suppliers' / supplier_prefix / 'locators' / 'product.js'
        l: SimpleNamespace = j_loads_ns(locators_path)

        # Create a new instance of Locator with loaded attributes
        object.__setattr__(self, 'attribute', l.attribute)
        object.__setattr__(self, 'by', l.by)
        object.__setattr__(self, 'if_list', l.if_list)
        object.__setattr__(self, 'use_mouse', l.use_mouse)
        object.__setattr__(self, 'mandatory', l.mandatory)
        object.__setattr__(self, 'event', l.event)
        object.__setattr__(self, 'locator_description', l.locator_description)
