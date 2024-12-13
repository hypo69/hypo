```python
import pytest
from unittest.mock import MagicMock, patch
from src.endpoints.advertisement.facebook.start_posting_katia import FacebookPromoter, Driver, Chrome, logger

# Fixture for a mock Driver instance
@pytest.fixture
def mock_driver():
    """Provides a mock Driver instance for testing."""
    mock = MagicMock(spec=Driver)
    return mock


# Fixture for a mock FacebookPromoter instance
@pytest.fixture
def mock_promoter(mock_driver):
    """Provides a mock FacebookPromoter instance for testing."""
    mock = MagicMock(spec=FacebookPromoter)
    mock.driver = mock_driver
    return mock

# Test for correct initialization of FacebookPromoter
def test_facebook_promoter_initialization(mock_driver):
    """Tests that FacebookPromoter initializes correctly."""
    filenames = ['test.json']
    promoter = FacebookPromoter(mock_driver, group_file_paths = filenames, no_video = False)
    assert promoter.driver == mock_driver
    assert promoter.group_file_paths == filenames
    assert promoter.no_video == False


def test_facebook_promoter_initialization_with_no_video_true(mock_driver):
    """Tests that FacebookPromoter initializes correctly with no_video = True."""
    filenames = ['test.json']
    promoter = FacebookPromoter(mock_driver, group_file_paths = filenames, no_video = True)
    assert promoter.driver == mock_driver
    assert promoter.group_file_paths == filenames
    assert promoter.no_video == True

# Test run_campaigns with valid input
@patch('src.endpoints.advertisement.facebook.start_posting_katia.FacebookPromoter.run_campaign')
def test_run_campaigns_valid_input(mock_run_campaign, mock_promoter):
    """Tests run_campaigns with valid campaigns."""
    campaigns = ['campaign1', 'campaign2']
    mock_promoter.run_campaigns(campaigns)
    mock_run_campaign.assert_any_call('campaign1')
    mock_run_campaign.assert_any_call('campaign2')
    assert mock_run_campaign.call_count == 2
    

# Test run_campaigns with empty campaign list
@patch('src.endpoints.advertisement.facebook.start_posting_katia.FacebookPromoter.run_campaign')
def test_run_campaigns_empty_campaigns(mock_run_campaign, mock_promoter):
    """Tests run_campaigns with empty list of campaigns"""
    campaigns = []
    mock_promoter.run_campaigns(campaigns)
    mock_run_campaign.assert_not_called()


# Test run_campaigns when KeyboardInterrupt is raised
@patch('src.endpoints.advertisement.facebook.start_posting_katia.FacebookPromoter.run_campaign')
def test_run_campaigns_keyboard_interrupt(mock_run_campaign, mock_promoter):
    """Tests run_campaigns with KeyboardInterrupt exception."""
    campaigns = ['campaign1', 'campaign2']
    mock_run_campaign.side_effect = KeyboardInterrupt
    
    with patch.object(logger, 'info') as mock_logger_info:
        mock_promoter.run_campaigns(campaigns)
        mock_logger_info.assert_called_with("Campaign promotion interrupted.")
    

# Test run_campaign with a single campaign (assuming run_campaign exists in the class)
@patch('src.endpoints.advertisement.facebook.start_posting_katia.FacebookPromoter.process_group_file')
def test_run_campaign_single_campaign(mock_process_group, mock_promoter):
    """Tests run_campaign with a single campaign."""
    campaign = "test_campaign"
    mock_promoter.run_campaign(campaign)
    mock_process_group.assert_called_with(campaign)
```