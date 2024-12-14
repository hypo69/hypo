```python
import pytest
from pathlib import Path
from bs4 import BeautifulSoup


@pytest.fixture
def html_content():
    """Provides the HTML content as a string."""
    file_path = Path(__file__).parent / "hypotez/src/webdriver/firefox/extentions/try_path_1.3.5/popup/popup.html"
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


@pytest.fixture
def soup(html_content):
    """Provides a BeautifulSoup object for parsing the HTML."""
    return BeautifulSoup(html_content, 'html.parser')


def test_popup_html_structure(soup):
    """Checks for the basic structure of the HTML: head, body, divs, buttons, inputs, etc."""
    assert soup.head is not None, "The HTML should have a <head> section."
    assert soup.body is not None, "The HTML should have a <body> section."
    assert soup.find("div", id="execute") is not None, "The HTML should have a div with id 'execute'."
    assert soup.find("button", id="execute") is not None, "The HTML should have a button with id 'execute'."
    assert soup.find("input", id="help-switch") is not None, "The HTML should have an input with id 'help-switch'."
    assert soup.find("label", attrs={"for": "help-switch"}) is not None, "The HTML should have a label with for 'help-switch'."
    assert soup.find("select", id="main-way") is not None, "The HTML should have a select with id 'main-way'."
    assert soup.find("textarea", id="main-expression") is not None, "The HTML should have a textarea with id 'main-expression'."
    assert soup.find("div", id="context-body") is not None, "The HTML should have a div with id 'context-body'."
    assert soup.find("div", id="resolver-body") is not None, "The HTML should have a div with id 'resolver-body'."
    assert soup.find("div", id="frame-designation-body") is not None, "The HTML should have a div with id 'frame-designation-body'."
    assert soup.find("div", id="frame-id-body") is not None, "The HTML should have a div with id 'frame-id-body'."
    assert soup.find("div", id="results-message") is not None, "The HTML should have a div with id 'results-message'."
    assert soup.find("table", id="context-detail") is not None, "The HTML should have a table with id 'context-detail'."
    assert soup.find("table", id="results-details") is not None, "The HTML should have a table with id 'results-details'."


def test_main_way_select_options(soup):
    """Checks if the main-way select element has the correct options."""
    main_way_select = soup.find("select", id="main-way")
    assert main_way_select is not None, "The HTML should have a select with id 'main-way'."
    
    expected_options = [
        ("evaluate", "ANY_TYPE"),
        ("evaluate", "NUMBER_TYPE"),
        ("evaluate", "STRING_TYPE"),
        ("evaluate", "BOOLEAN_TYPE"),
        ("evaluate", "UNORDERED_NODE_ITERATOR_TYPE"),
        ("evaluate", "ORDERED_NODE_ITERATOR_TYPE"),
        ("evaluate", "UNORDERED_NODE_SNAPSHOT_TYPE"),
        ("evaluate", "ORDERED_NODE_SNAPSHOT_TYPE"),
        ("evaluate", "ANY_UNORDERED_NODE_TYPE"),
        ("evaluate", "FIRST_ORDERED_NODE_TYPE"),
        ("querySelector", ""),
        ("querySelectorAll", "")
    ]
    
    options = main_way_select.find_all("option")
    assert len(options) == len(expected_options), "The number of options in main-way select does not match the expected."
    
    for option, (method, type) in zip(options, expected_options):
        assert option.get("data-method") == method, f"Option has incorrect data-method attribute, expected '{method}', got '{option.get('data-method')}'."
        assert option.get("data-type") == type, f"Option has incorrect data-type attribute, expected '{type}', got '{option.get('data-type')}'."


def test_context_way_select_options(soup):
    """Checks if the context-way select element has the correct options."""
    context_way_select = soup.find("select", id="context-way")
    assert context_way_select is not None, "The HTML should have a select with id 'context-way'."

    expected_options = [
        ("evaluate", "ANY_TYPE"),
        ("evaluate", "UNORDERED_NODE_ITERATOR_TYPE"),
        ("evaluate", "ORDERED_NODE_ITERATOR_TYPE"),
        ("evaluate", "UNORDERED_NODE_SNAPSHOT_TYPE"),
        ("evaluate", "ORDERED_NODE_SNAPSHOT_TYPE"),
        ("evaluate", "ANY_UNORDERED_NODE_TYPE"),
        ("evaluate", "FIRST_ORDERED_NODE_TYPE"),
        ("querySelector", ""),
        ("querySelectorAll", "")
    ]

    options = context_way_select.find_all("option")
    assert len(options) == len(expected_options), "The number of options in context-way select does not match the expected."
    
    for option, (method, type) in zip(options, expected_options):
        assert option.get("data-method") == method, f"Option has incorrect data-method attribute, expected '{method}', got '{option.get('data-method')}'."
        assert option.get("data-type") == type, f"Option has incorrect data-type attribute, expected '{type}', got '{option.get('data-type')}'."


def test_popup_html_ids(soup):
    """Checks the uniqueness of HTML IDs."""
    ids = [tag.get('id') for tag in soup.find_all(id=True)]
    assert len(ids) == len(set(ids)), "Duplicate IDs found in the HTML."
    
def test_popup_html_classes(soup):
    """checks if the classes are valid in HTML"""
    classes = [tag.get('class') for tag in soup.find_all(class_=True)]
    
    for class_list in classes:
        assert isinstance(class_list, list), "The class is not a list"
        for class_name in class_list:
            assert isinstance(class_name, str), "The class name is not a string"


def test_popup_html_form_elements(soup):
    """check that all form elements have id and label are connected correctly"""
    form_elements_ids = [tag.get('id') for tag in soup.find_all(['input', 'select', 'textarea']) if tag.get('id')]
    labels = soup.find_all('label')
    
    for label in labels:
        assert label.get('for') in form_elements_ids, f"label with for attribute:{label.get('for')} is not related to an input element"
```