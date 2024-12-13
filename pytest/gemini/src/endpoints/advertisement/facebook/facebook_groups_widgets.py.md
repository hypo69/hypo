```python
import pytest
from pathlib import Path
from unittest.mock import patch, mock_open
from src.endpoints.advertisement.facebook.facebook_groups_widgets import FacebookGroupsWidget
from types import SimpleNamespace
from ipywidgets import Dropdown


@pytest.fixture
def mock_json_data():
    """Provides mock JSON data for testing."""
    return '{"group1": {"url": "https://facebook.com/group1"}, "group2": {"url": "https://facebook.com/group2"}}'


@pytest.fixture
def temp_json_file(tmp_path, mock_json_data):
    """Creates a temporary JSON file for testing."""
    file_path = tmp_path / "test_groups.json"
    with open(file_path, "w") as f:
        f.write(mock_json_data)
    return file_path


def test_facebook_groups_widget_initialization(temp_json_file):
    """Checks if the widget is initialized correctly."""
    widget = FacebookGroupsWidget(temp_json_file)
    assert isinstance(widget.groups_data, SimpleNamespace)
    assert hasattr(widget.groups_data, 'group1')
    assert hasattr(widget.groups_data, 'group2')
    assert isinstance(widget.dropdown, Dropdown)
    assert widget.dropdown.options == ['group1', 'group2']


def test_create_dropdown(temp_json_file):
    """Checks if the dropdown is created correctly with data from the json."""
    widget = FacebookGroupsWidget(temp_json_file)
    dropdown = widget.create_dropdown()
    assert isinstance(dropdown, Dropdown)
    assert dropdown.options == ['group1', 'group2']
    assert dropdown.description == 'Facebook Groups:'
    assert dropdown.disabled == False


def test_create_dropdown_with_empty_json(tmp_path):
    """Checks if the dropdown handles an empty json."""
    file_path = tmp_path / "empty_groups.json"
    with open(file_path, "w") as f:
        f.write('{}')
    widget = FacebookGroupsWidget(file_path)
    dropdown = widget.create_dropdown()
    assert isinstance(dropdown, Dropdown)
    assert dropdown.options == []
    assert dropdown.description == 'Facebook Groups:'
    assert dropdown.disabled == False


def test_display_widget(temp_json_file):
    """Checks if display_widget calls the display function with the dropdown."""
    widget = FacebookGroupsWidget(temp_json_file)
    with patch('src.endpoints.advertisement.facebook.facebook_groups_widgets.display') as mock_display:
        widget.display_widget()
        mock_display.assert_called_once_with(widget.dropdown)


def test_initialization_with_invalid_json_path():
    """Checks if the constructor handles invalid json file path gracefully"""
    with pytest.raises(FileNotFoundError):
        FacebookGroupsWidget(Path('invalid_path.json'))


def test_initialization_with_malformed_json(tmp_path):
    """Checks if the constructor handles malformed json gracefully."""
    file_path = tmp_path / "malformed_groups.json"
    with open(file_path, "w") as f:
        f.write('{"group1": {"url": "https://facebook.com/group1"') # missing closing bracket
    with pytest.raises(Exception): # Expecting json.decoder.JSONDecodeError or similar
        FacebookGroupsWidget(file_path)
```