```python
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from hypotez.src.suppliers.aliexpress.campaign.prepare_campaigns import process_campaign_category, process_campaign, process_all_campaigns, get_directory_names


# Fixture for a mock google_drive path
@pytest.fixture
def mock_google_drive_path(monkeypatch):
    mock_gs_path = MagicMock()
    mock_gs_path.google_drive = Path("/mock/google_drive")
    monkeypatch.setattr('hypotez.src.suppliers.aliexpress.campaign._examples._examle_prepare_campains.gs.path', mock_gs_path)
    return mock_gs_path

# Fixture for a mock directory
@pytest.fixture
def mock_directory_names():
    return ["campaign1", "campaign2", "campaign3"]


# Test for process_campaign_category
@patch('hypotez.src.suppliers.aliexpress.campaign.prepare_campaigns.process_campaign')
def test_process_campaign_category_valid_input(mock_process_campaign):
    """Test process_campaign_category with valid inputs."""
    process_campaign_category("SummerSale", "Electronics", "EN", "USD", force=True)
    mock_process_campaign.assert_called_once_with(
        "SummerSale", categories=["Electronics"], language="EN", currency="USD", force=True
    )


@patch('hypotez.src.suppliers.aliexpress.campaign.prepare_campaigns.process_campaign')
def test_process_campaign_category_invalid_input(mock_process_campaign):
    """Test process_campaign_category with invalid input (empty campaign name)."""
    with pytest.raises(ValueError, match="Campaign name cannot be empty"):
      process_campaign_category("", "Electronics", "EN", "USD", force=True)
    mock_process_campaign.assert_not_called()
    
@patch('hypotez.src.suppliers.aliexpress.campaign.prepare_campaigns.process_campaign')
def test_process_campaign_category_force_false(mock_process_campaign):
    """Test process_campaign_category with force=False."""
    process_campaign_category("SummerSale", "Electronics", "EN", "USD", force=False)
    mock_process_campaign.assert_called_once_with(
        "SummerSale", categories=["Electronics"], language="EN", currency="USD", force=False
    )


# Test for process_campaign
@patch('hypotez.src.suppliers.aliexpress.campaign.prepare_campaigns.prepare_campaign')
def test_process_campaign_valid_input(mock_prepare_campaign):
    """Test process_campaign with valid inputs."""
    process_campaign("WinterSale", categories=["Clothing", "Toys"], language="EN", currency="USD", force=False)
    mock_prepare_campaign.assert_called_once_with(
        "WinterSale", categories=["Clothing", "Toys"], language="EN", currency="USD", force=False
    )


@patch('hypotez.src.suppliers.aliexpress.campaign.prepare_campaigns.prepare_campaign')
def test_process_campaign_empty_categories(mock_prepare_campaign):
    """Test process_campaign with empty categories list."""
    process_campaign("WinterSale", categories=[], language="EN", currency="USD", force=False)
    mock_prepare_campaign.assert_called_once_with(
        "WinterSale", categories=[], language="EN", currency="USD", force=False
    )


@patch('hypotez.src.suppliers.aliexpress.campaign.prepare_campaigns.prepare_campaign')
def test_process_campaign_no_categories(mock_prepare_campaign):
    """Test process_campaign with no categories specified."""
    process_campaign("WinterSale", language="EN", currency="USD", force=True)
    mock_prepare_campaign.assert_called_once_with(
        "WinterSale", categories=None, language="EN", currency="USD", force=True
    )

@patch('hypotez.src.suppliers.aliexpress.campaign.prepare_campaigns.prepare_campaign')
def test_process_campaign_invalid_input(mock_prepare_campaign):
    """Test process_campaign with invalid input (empty campaign name)."""
    with pytest.raises(ValueError, match="Campaign name cannot be empty"):
      process_campaign("", categories=["Clothing", "Toys"], language="EN", currency="USD", force=True)
    mock_prepare_campaign.assert_not_called()

# Test for process_all_campaigns
@patch('hypotez.src.suppliers.aliexpress.campaign.prepare_campaigns.process_campaign')
def test_process_all_campaigns_valid_input(mock_process_campaign, mock_google_drive_path, mock_directory_names, monkeypatch):
    """Test process_all_campaigns with valid inputs."""
    monkeypatch.setattr('hypotez.src.suppliers.aliexpress.campaign.prepare_campaigns.get_directory_names', MagicMock(return_value=mock_directory_names))
    process_all_campaigns(language="EN", currency="USD", force=True)
    
    
    assert mock_process_campaign.call_count == len(mock_directory_names)
    
    expected_calls = [
        (('campaign1',), {'categories': None, 'language': 'EN', 'currency': 'USD', 'force': True}),
        (('campaign2',), {'categories': None, 'language': 'EN', 'currency': 'USD', 'force': True}),
        (('campaign3',), {'categories': None, 'language': 'EN', 'currency': 'USD', 'force': True})
    ]
    
    mock_process_campaign.assert_has_calls(
        [pytest.call(*args, **kwargs) for args, kwargs in expected_calls], any_order=True
    )
    
    
@patch('hypotez.src.suppliers.aliexpress.campaign.prepare_campaigns.process_campaign')
def test_process_all_campaigns_no_campaigns(mock_process_campaign, mock_google_drive_path, monkeypatch):
    """Test process_all_campaigns when there are no campaigns."""
    monkeypatch.setattr('hypotez.src.suppliers.aliexpress.campaign.prepare_campaigns.get_directory_names', MagicMock(return_value=[]))
    process_all_campaigns(language="EN", currency="USD", force=True)
    mock_process_campaign.assert_not_called()


# Test for get_directory_names
def test_get_directory_names_valid_path(mock_google_drive_path, monkeypatch, tmp_path):
    """Test get_directory_names with a valid directory."""
    # Create test directories
    (tmp_path / 'campaign1').mkdir()
    (tmp_path / 'campaign2').mkdir()
    (tmp_path / 'not_a_campaign').touch() # Create file which should not be returned
    monkeypatch.setattr('hypotez.src.suppliers.aliexpress.campaign._examples._examle_prepare_campains.gs.path.google_drive', tmp_path)

    campaigns_directory = Path(tmp_path)
    names = get_directory_names(campaigns_directory)
    
    assert set(names) == {"campaign1", "campaign2"}



def test_get_directory_names_empty_path(tmp_path):
    """Test get_directory_names with an empty directory."""
    campaigns_directory = Path(tmp_path)
    names = get_directory_names(campaigns_directory)
    assert names == []


def test_get_directory_names_invalid_path():
    """Test get_directory_names with an invalid path."""
    with pytest.raises(ValueError, match="Not a directory"):
        get_directory_names("invalid/path")
```