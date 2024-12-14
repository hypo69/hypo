```python
import pytest
from bs4 import BeautifulSoup

# Fixture to load the HTML content
@pytest.fixture
def html_content():
    """Provides the HTML content as a string."""
    return """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script src="../scripts/try_xpath_functions.js"></script>
<script src="options.js"></script>
</head>

<body>
<div><h1>Attributes</h1>
  <dl>
    <dt><label for="element-attribute">Resulted elements</label></dt>
    <dd><input type="text" id="element-attribute"></dd>
    <dt><label for="context-attribute">Context element</label></dt>
    <dd><input type="text" id="context-attribute"></dd>
    <dt><label for="focused-attribute">Focused element</label></dt>
    <dd><input type="text" id="focused-attribute"></dd>
    <dt><label for="ancestor-attribute">Ancestors of the focused element</label></dt>
    <dd><input type="text" id="ancestor-attribute"></dd>
    <dt><label for="frame-attribute">Frame elements</label></dt>
    <dd><input type="text" id="frame-attribute"></dd>
    <dt><label for="frame-ancestor-attribute">Ancestors of the frames</label></dt>
    <dd><input type="text" id="frame-ancestor-attribute"></dd>
  </dl>
</div>
<div><h1>Style to be inserted</h1>
  <dl>
    <dt><label for="style">Style</label></dt>
    <dd><textarea id="style"></textarea></dd>
  </dl>
</div>
<div><h1>Popup styles</h1>
  <dl>
    <dt><label for="popup-body-width">Body width(auto or px)</label></dt>
    <dd><input type="text" id="popup-body-width"></dd>
    <dt><label for="popup-body-height">Body height(auto or px)</label></dt>
    <dd><input type="text" id="popup-body-height"></dd>
  </dl>
</div>
<div><button id="save">Save</button><button id="show-default">Show default</button></div>
<div id="message"></div>
</body>
</html>
"""
@pytest.fixture
def parsed_html(html_content):
     """Parses the HTML content using BeautifulSoup."""
     return BeautifulSoup(html_content, 'html.parser')

def test_html_structure_exists(parsed_html):
    """Checks if main elements exist in HTML structure."""
    assert parsed_html.find('h1', text='Attributes') is not None
    assert parsed_html.find('h1', text='Style to be inserted') is not None
    assert parsed_html.find('h1', text='Popup styles') is not None
    assert parsed_html.find('button', {'id': 'save'}) is not None
    assert parsed_html.find('button', {'id': 'show-default'}) is not None
    assert parsed_html.find('div', {'id': 'message'}) is not None


def test_input_elements_exist(parsed_html):
    """Checks if all input elements exist with correct ids."""
    assert parsed_html.find('input', {'id': 'element-attribute'}) is not None
    assert parsed_html.find('input', {'id': 'context-attribute'}) is not None
    assert parsed_html.find('input', {'id': 'focused-attribute'}) is not None
    assert parsed_html.find('input', {'id': 'ancestor-attribute'}) is not None
    assert parsed_html.find('input', {'id': 'frame-attribute'}) is not None
    assert parsed_html.find('input', {'id': 'frame-ancestor-attribute'}) is not None
    assert parsed_html.find('textarea', {'id': 'style'}) is not None
    assert parsed_html.find('input', {'id': 'popup-body-width'}) is not None
    assert parsed_html.find('input', {'id': 'popup-body-height'}) is not None

def test_label_for_attribute_matches_input_ids(parsed_html):
  """Checks if 'for' attribute of labels match input 'id' attributes."""
  label_for_element_attribute = parsed_html.find('label', {'for': 'element-attribute'})
  assert label_for_element_attribute is not None

  label_for_context_attribute = parsed_html.find('label', {'for': 'context-attribute'})
  assert label_for_context_attribute is not None

  label_for_focused_attribute = parsed_html.find('label', {'for': 'focused-attribute'})
  assert label_for_focused_attribute is not None

  label_for_ancestor_attribute = parsed_html.find('label', {'for': 'ancestor-attribute'})
  assert label_for_ancestor_attribute is not None

  label_for_frame_attribute = parsed_html.find('label', {'for': 'frame-attribute'})
  assert label_for_frame_attribute is not None

  label_for_frame_ancestor_attribute = parsed_html.find('label', {'for': 'frame-ancestor-attribute'})
  assert label_for_frame_ancestor_attribute is not None

  label_for_style = parsed_html.find('label', {'for': 'style'})
  assert label_for_style is not None
  
  label_for_popup_body_width = parsed_html.find('label', {'for': 'popup-body-width'})
  assert label_for_popup_body_width is not None

  label_for_popup_body_height = parsed_html.find('label', {'for': 'popup-body-height'})
  assert label_for_popup_body_height is not None

def test_button_elements_exist(parsed_html):
  """Checks if buttons exists with the correct IDs"""
  save_button = parsed_html.find('button', {'id': 'save'})
  assert save_button is not None

  show_default_button = parsed_html.find('button', {'id': 'show-default'})
  assert show_default_button is not None

def test_message_div_exists(parsed_html):
  """Checks if the message div exists with the correct ID"""
  message_div = parsed_html.find('div', {'id': 'message'})
  assert message_div is not None
```