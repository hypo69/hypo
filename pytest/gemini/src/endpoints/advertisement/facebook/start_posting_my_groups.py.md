```python
import pytest
import copy
from unittest.mock import patch, MagicMock
from src.endpoints.advertisement.facebook.start_posting_my_groups import FacebookPromoter
from src.webdriver.driver import Driver, Chrome

# Mock the logger for tests
@pytest.fixture(autouse=True)
def mock_logger():
    with patch('src.endpoints.advertisement.facebook.start_posting_my_groups.logger') as mock:
        yield mock

# Mock the Driver and Chrome classes
@pytest.fixture
def mock_driver():
    mock_driver_instance = MagicMock(spec=Driver)
    mock_chrome_instance = MagicMock(spec=Chrome)
    with patch('src.endpoints.advertisement.facebook.start_posting_my_groups.Driver', return_value=mock_driver_instance), \
         patch('src.endpoints.advertisement.facebook.start_posting_my_groups.Chrome', return_value=mock_chrome_instance):
        yield mock_driver_instance
        
@pytest.fixture
def mock_facebook_promoter(mock_driver):
    mock_promoter = MagicMock(spec=FacebookPromoter)
    with patch('src.endpoints.advertisement.facebook.start_posting_my_groups.FacebookPromoter', return_value=mock_promoter):
        yield mock_promoter

# Test case for the run_campaigns method in FacebookPromoter
def test_run_campaigns_valid_input(mock_facebook_promoter):
    """
    Tests the run_campaigns method with valid input to ensure it's called correctly.
    """
    campaigns = ['brands', 'mom_and_baby']
    filenames = ['my_managed_groups.json']

    mock_facebook_promoter.run_campaigns.return_value = None

    promoter = FacebookPromoter(MagicMock(), group_file_paths = filenames, no_video = True)
    promoter.run_campaigns(campaigns = copy.copy(campaigns), group_file_paths = filenames)

    mock_facebook_promoter.run_campaigns.assert_called_once_with(campaigns = campaigns, group_file_paths = filenames)


def test_run_campaigns_empty_campaigns(mock_facebook_promoter):
    """
    Tests the run_campaigns method with an empty list of campaigns, ensuring it doesn't raise any errors
    """
    campaigns = []
    filenames = ['my_managed_groups.json']

    mock_facebook_promoter.run_campaigns.return_value = None

    promoter = FacebookPromoter(MagicMock(), group_file_paths = filenames, no_video = True)
    promoter.run_campaigns(campaigns = copy.copy(campaigns), group_file_paths = filenames)

    mock_facebook_promoter.run_campaigns.assert_called_once_with(campaigns = [], group_file_paths = filenames)
    

def test_run_campaigns_empty_filenames(mock_facebook_promoter):
    """
    Tests the run_campaigns method with an empty list of filenames, ensuring it doesn't raise any errors.
    """
    campaigns = ['brands', 'mom_and_baby']
    filenames = []

    mock_facebook_promoter.run_campaigns.return_value = None
    
    promoter = FacebookPromoter(MagicMock(), group_file_paths = filenames, no_video = True)
    promoter.run_campaigns(campaigns = copy.copy(campaigns), group_file_paths = filenames)
    
    mock_facebook_promoter.run_campaigns.assert_called_once_with(campaigns=campaigns, group_file_paths=filenames)

def test_keyboard_interrupt_handling(mock_logger, mock_driver, mock_facebook_promoter):
    """
    Tests the handling of KeyboardInterrupt to ensure the logger is called correctly.
    This test simulates a KeyboardInterrupt during the execution loop.
    """

    mock_facebook_promoter.run_campaigns.side_effect = KeyboardInterrupt
    
    promoter = FacebookPromoter(mock_driver, group_file_paths = ['my_managed_groups.json'], no_video = True)

    try:
        while True:
          promoter.run_campaigns(campaigns = copy.copy(['brands']), group_file_paths = ['my_managed_groups.json'])
    except KeyboardInterrupt:
        pass
        
    mock_logger.info.assert_called_once_with("Campaign promotion interrupted.")

def test_facebook_promoter_initialization(mock_driver):
    """
    Test if FacebookPromoter initializes correctly with provided driver, filepaths and no_video
    """
    filenames = ['my_managed_groups.json']
    promoter = FacebookPromoter(mock_driver, group_file_paths = filenames, no_video = True)
    
    assert promoter.driver == mock_driver
    assert promoter.group_file_paths == filenames
    assert promoter.no_video == True

    filenames = ['my_managed_groups.json', 'my_groups.json']
    promoter = FacebookPromoter(mock_driver, group_file_paths = filenames, no_video = False)

    assert promoter.driver == mock_driver
    assert promoter.group_file_paths == filenames
    assert promoter.no_video == False
```