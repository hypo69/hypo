```python
import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch
from ipywidgets import Dropdown, Button
from types import SimpleNamespace

from src.suppliers.aliexpress.campaign.ali_campaign_editor_jupyter_widgets import (
    JupyterCampaignEditorWidgets,
)
from src.suppliers.aliexpress.campaign.ali_campaign_editor import AliCampaignEditor
from src import gs

# Mock the logger
@pytest.fixture(autouse=True)
def mock_logger():
    with patch("src.suppliers.aliexpress.campaign.ali_campaign_editor_jupyter_widgets.logger") as mock:
        yield mock

# Mock the get_directory_names function
@pytest.fixture
def mock_get_directory_names():
    with patch(
        "src.suppliers.aliexpress.campaign.ali_campaign_editor_jupyter_widgets.get_directory_names"
    ) as mock:
        mock.return_value = ["campaign1", "campaign2"]
        yield mock


# Mock the AliCampaignEditor
@pytest.fixture
def mock_ali_campaign_editor():
    with patch(
        "src.suppliers.aliexpress.campaign.ali_campaign_editor_jupyter_widgets.AliCampaignEditor"
    ) as mock:
        mock_instance = mock.return_value
        mock_instance.get_category.return_value = SimpleNamespace(name="category1")
        mock_instance.get_category_products.return_value = [
            SimpleNamespace(name="product1"),
            SimpleNamespace(name="product2"),
        ]
        mock_instance.spreadsheet_id = "test_spreadsheet_id"
        yield mock


# Mock webbrowser.open
@pytest.fixture
def mock_webbrowser_open():
    with patch(
        "src.suppliers.aliexpress.campaign.ali_campaign_editor_jupyter_widgets.webbrowser.open"
    ) as mock:
        yield mock

# Fixture for creating a JupyterCampaignEditorWidgets instance
@pytest.fixture
def editor_widgets(mock_get_directory_names):
    gs.path = SimpleNamespace(google_drive="test_drive")
    return JupyterCampaignEditorWidgets()


def test_jupyter_campaign_editor_widgets_initialization(
    editor_widgets, mock_get_directory_names
):
    """Test initialization of JupyterCampaignEditorWidgets."""
    assert isinstance(editor_widgets.campaign_name_dropdown, Dropdown)
    assert isinstance(editor_widgets.category_name_dropdown, Dropdown)
    assert isinstance(editor_widgets.language_dropdown, Dropdown)
    assert isinstance(editor_widgets.initialize_button, Button)
    assert isinstance(editor_widgets.save_button, Button)
    assert isinstance(editor_widgets.show_products_button, Button)
    assert isinstance(editor_widgets.open_spreadsheet_button, Button)
    assert editor_widgets.campaigns_directory == Path(
        "test_drive", "aliexpress", "campaigns"
    )
    mock_get_directory_names.assert_called_once_with(
        Path("test_drive", "aliexpress", "campaigns")
    )


def test_jupyter_campaign_editor_widgets_initialization_no_dir():
    """Test initialization of JupyterCampaignEditorWidgets with no dir."""
    gs.path = SimpleNamespace(google_drive="test_drive")
    with patch(
        "src.suppliers.aliexpress.campaign.ali_campaign_editor_jupyter_widgets.Path.exists"
    ) as mock_exists:
        mock_exists.return_value = False
        with pytest.raises(FileNotFoundError, match="Directory does not exist"):
            JupyterCampaignEditorWidgets()


def test_initialize_campaign_editor_with_valid_selection(
    editor_widgets, mock_ali_campaign_editor
):
    """Test initialization with valid campaign, category, and language selection."""
    editor_widgets.campaign_name_dropdown.value = "campaign1"
    editor_widgets.category_name_dropdown.options = ["category1", "category2"]
    editor_widgets.category_name_dropdown.value = "category1"
    editor_widgets.language_dropdown.value = "EN USD"

    editor_widgets.initialize_campaign_editor(None)

    assert editor_widgets.campaign_name == "campaign1"
    assert editor_widgets.category_name == "category1"
    assert editor_widgets.language == "EN"
    assert editor_widgets.currency == "USD"
    mock_ali_campaign_editor.assert_called_once_with(
        campaign_name="campaign1", language="EN", currency="USD"
    )
    mock_ali_campaign_editor.return_value.get_category.assert_called_once_with(
        "category1"
    )
    mock_ali_campaign_editor.return_value.get_category_products.assert_called_once_with(
        "category1"
    )
    assert editor_widgets.category is not None
    assert editor_widgets.products is not None
    assert len(editor_widgets.products) == 2


def test_initialize_campaign_editor_no_campaign_selected(
    editor_widgets, mock_logger
):
    """Test initialization with no campaign selected."""
    editor_widgets.initialize_campaign_editor(None)
    mock_logger.warning.assert_called_once_with(
        "Please select a campaign name before initializing the editor."
    )
    assert editor_widgets.campaign_editor is None
    assert editor_widgets.category is None
    assert editor_widgets.products is None


def test_update_category_dropdown(editor_widgets, mock_get_directory_names):
    """Test updating the category dropdown."""
    editor_widgets.campaign_name = "test_campaign"
    mock_get_directory_names.return_value = ["category1", "category2"]
    editor_widgets.update_category_dropdown("test_campaign")
    mock_get_directory_names.assert_called_once_with(
        Path("test_drive", "aliexpress", "campaigns", "test_campaign", "category")
    )
    assert editor_widgets.category_name_dropdown.options == ["category1", "category2"]


def test_on_campaign_name_change(editor_widgets, mock_get_directory_names):
    """Test handling campaign name change."""
    editor_widgets.campaign_name_dropdown.value = "campaign1"
    editor_widgets.on_campaign_name_change({"new": "campaign2"})
    assert editor_widgets.campaign_name == "campaign2"
    mock_get_directory_names.assert_called_with(
        Path("test_drive", "aliexpress", "campaigns", "campaign2", "category")
    )


def test_on_category_change(editor_widgets, mock_ali_campaign_editor):
    """Test handling category change."""
    editor_widgets.campaign_name_dropdown.value = "campaign1"
    editor_widgets.category_name_dropdown.options = ["category1", "category2"]
    editor_widgets.category_name_dropdown.value = "category1"
    editor_widgets.on_category_change({"new": "category2"})
    assert editor_widgets.category_name == "category2"
    mock_ali_campaign_editor.assert_called_once()
    assert editor_widgets.campaign_editor is not None


def test_on_language_change(editor_widgets, mock_ali_campaign_editor):
    """Test handling language change."""
    editor_widgets.language_dropdown.value = "EN USD"
    editor_widgets.on_language_change({"new": "HE ILS"})
    assert editor_widgets.language == "HE"
    assert editor_widgets.currency == "ILS"
    mock_ali_campaign_editor.assert_called_once()
    assert editor_widgets.campaign_editor is not None


def test_save_campaign_valid(editor_widgets, mock_ali_campaign_editor):
    """Test saving a campaign with valid selection."""
    editor_widgets.campaign_name_dropdown.value = "campaign1"
    editor_widgets.category_name_dropdown.value = "category1"
    editor_widgets.language_dropdown.value = "EN USD"
    editor_widgets.save_campaign(None)
    mock_ali_campaign_editor.assert_called_once_with(
        campaign_name="campaign1", category_name="category1", language="EN"
    )
    mock_ali_campaign_editor.return_value.save_categories_from_worksheet.assert_called_once()


def test_save_campaign_no_campaign_name(editor_widgets, mock_logger):
    """Test saving a campaign with no campaign name selected."""
    editor_widgets.language_dropdown.value = "EN USD"
    editor_widgets.save_campaign(None)
    mock_logger.warning.assert_called_once_with(
        "Please select campaign name and language/currency before saving the campaign."
    )

def test_save_campaign_exception(editor_widgets, mock_ali_campaign_editor, mock_logger):
    """Test saving a campaign with an exception during save."""
    editor_widgets.campaign_name_dropdown.value = "campaign1"
    editor_widgets.category_name_dropdown.value = "category1"
    editor_widgets.language_dropdown.value = "EN USD"
    mock_ali_campaign_editor.return_value.save_categories_from_worksheet.side_effect = Exception("Test Exception")
    editor_widgets.save_campaign(None)
    mock_logger.error.assert_called_once()


def test_show_products_valid(editor_widgets, mock_ali_campaign_editor):
    """Test displaying products with valid selection."""
    editor_widgets.campaign_name_dropdown.value = "campaign1"
    editor_widgets.category_name_dropdown.value = "category1"
    editor_widgets.language = "EN"
    editor_widgets.currency = "USD"
    editor_widgets.show_products(None)
    mock_ali_campaign_editor.assert_called_once_with(
        campaign_name="campaign1", language="EN", currency="USD"
    )
    mock_ali_campaign_editor.return_value.set_products_worksheet.assert_called_once_with("category1")


def test_show_products_exception(editor_widgets, mock_ali_campaign_editor, mock_logger):
    """Test displaying products with an exception."""
    editor_widgets.campaign_name_dropdown.value = "campaign1"
    editor_widgets.category_name_dropdown.value = "category1"
    editor_widgets.language = "EN"
    editor_widgets.currency = "USD"
    mock_ali_campaign_editor.return_value.set_products_worksheet.side_effect = Exception("Test Exception")
    editor_widgets.show_products(None)
    mock_logger.error.assert_called_once()


def test_open_spreadsheet_valid(editor_widgets, mock_webbrowser_open, mock_ali_campaign_editor):
    """Test opening spreadsheet with valid editor."""
    editor_widgets.campaign_editor = mock_ali_campaign_editor.return_value
    editor_widgets.open_spreadsheet(None)
    mock_webbrowser_open.assert_called_once_with(
        "https://docs.google.com/spreadsheets/d/test_spreadsheet_id/edit"
    )


def test_open_spreadsheet_no_editor(editor_widgets, capsys):
    """Test opening spreadsheet with no editor initialized."""
    editor_widgets.open_spreadsheet(None)
    captured = capsys.readouterr()
    assert "Please initialize the campaign editor first." in captured.out

def test_setup_callbacks(editor_widgets):
    """Test setup of callbacks for widgets."""
    assert editor_widgets.campaign_name_dropdown._callbacks  # Check if callbacks are set
    assert editor_widgets.category_name_dropdown._callbacks
    assert editor_widgets.language_dropdown._callbacks
    assert editor_widgets.initialize_button._click_handlers
    assert editor_widgets.save_button._click_handlers
    assert editor_widgets.show_products_button._click_handlers
    assert editor_widgets.open_spreadsheet_button._click_handlers


def test_display_widgets(editor_widgets, mock_ali_campaign_editor, mock_get_directory_names):
    """Test display of widgets."""
    with patch(
        "src.suppliers.aliexpress.campaign.ali_campaign_editor_jupyter_widgets.display"
    ) as mock_display:
        editor_widgets.display_widgets()
        mock_display.assert_called_once()
        
        mock_ali_campaign_editor.assert_called()
        mock_get_directory_names.assert_called()
```