```python
import pytest
import time
from unittest.mock import MagicMock, patch
from hypotez.src.endpoints.advertisement.facebook.start_posting import FacebookPromoter
from hypotez.src.webdriver.driver import Driver, Chrome
from hypotez.src.logger.logger import logger



@pytest.fixture
def mock_driver():
    """Provides a mock Driver object for testing."""
    mock_driver = MagicMock(spec=Driver)
    mock_driver.get_url = MagicMock()
    return mock_driver

@pytest.fixture
def mock_promoter(mock_driver):
    """Provides a mock FacebookPromoter object for testing."""
    return FacebookPromoter(mock_driver, group_file_paths=["test_groups.json"], no_video=True)

@patch('hypotez.src.endpoints.advertisement.facebook.start_posting.time.sleep', return_value=None)
def test_start_posting_loop_keyboard_interrupt(mock_sleep, mock_driver, caplog):
    """Tests the main loop interruption by KeyboardInterrupt"""
    
    promoter = FacebookPromoter(mock_driver, group_file_paths=["test_groups.json"], no_video=True)
    mock_run_campaigns = MagicMock()
    promoter.run_campaigns = mock_run_campaigns
    
    with pytest.raises(KeyboardInterrupt):
        
        try:
          while True:
              promoter.run_campaigns(campaigns=['test_campaign'], group_file_paths=['test_groups.json'])
              print(f"Going sleep {time.localtime()}")
              time.sleep(1)
              raise KeyboardInterrupt  # Simulate KeyboardInterrupt
        except KeyboardInterrupt:
            logger.info("Campaign promotion interrupted.")
            raise  # Re-raise KeyboardInterrupt to let pytest capture it


    mock_run_campaigns.assert_called_once()
    assert "Campaign promotion interrupted." in caplog.text



@patch('hypotez.src.endpoints.advertisement.facebook.start_posting.time.sleep', return_value=None)
def test_start_posting_loop_runs_with_valid_input(mock_sleep, mock_driver, mock_promoter):
    """Tests the main loop execution with valid inputs."""
    mock_run_campaigns = MagicMock()
    mock_promoter.run_campaigns = mock_run_campaigns

    try:
        # Simulate two iterations of the loop
        for _ in range(2):  
            mock_promoter.run_campaigns(campaigns=['brands'], group_file_paths =['usa.json'])
            time.sleep(1)
            raise KeyboardInterrupt # exit the loop
    except KeyboardInterrupt:
      pass # to not raise an exception

    assert mock_run_campaigns.call_count == 2
    mock_run_campaigns.assert_called_with(campaigns=['brands'], group_file_paths =['usa.json'])


def test_facebook_promoter_initialization(mock_driver):
    """Tests the initialization of FacebookPromoter with valid inputs."""
    group_file_paths = ["test_groups1.json", "test_groups2.json"]
    promoter = FacebookPromoter(mock_driver, group_file_paths=group_file_paths, no_video=False)
    assert promoter.driver == mock_driver
    assert promoter.group_file_paths == group_file_paths
    assert promoter.no_video == False
    
def test_facebook_promoter_initialization_with_default_no_video(mock_driver):
    """Tests the initialization of FacebookPromoter with default no_video"""
    promoter = FacebookPromoter(mock_driver, group_file_paths=["test_groups1.json"])
    assert promoter.no_video == True

def test_facebook_promoter_run_campaigns_calls_post_to_groups(mock_promoter):
    """Test that run_campaigns calls post_to_groups"""
    mock_post_to_groups = MagicMock()
    mock_promoter.post_to_groups = mock_post_to_groups
    mock_promoter.run_campaigns(campaigns=["test_campaign"], group_file_paths=["test_groups.json"])

    mock_post_to_groups.assert_called_once()

def test_facebook_promoter_post_to_groups_with_empty_groups(mock_promoter):
    """Test the post_to_groups method with empty groups."""
    mock_promoter.group_file_paths = []
    mock_post = MagicMock()
    mock_promoter.post_to_group = mock_post

    mock_promoter.post_to_groups(campaign="test_campaign", groups=[])
    mock_post.assert_not_called()
    
@patch('hypotez.src.endpoints.advertisement.facebook.start_posting.FacebookPromoter.post_to_group', return_value=True)
def test_facebook_promoter_post_to_groups_with_groups(mock_post_to_group, mock_promoter):
    """Test the post_to_groups method with groups."""
    mock_promoter.group_file_paths = ["test_groups.json"]

    mock_promoter.post_to_groups(campaign="test_campaign", groups=["group1", "group2"])
    mock_post_to_group.assert_called()
    assert mock_post_to_group.call_count == 2
    

def test_facebook_promoter_post_to_group_success(mock_promoter):
    """Test successful posting to a group"""
    mock_promoter.driver.get_url = MagicMock()
    mock_promoter.driver.find_element = MagicMock()
    mock_promoter.driver.send_keys_to_element = MagicMock()
    mock_promoter.driver.click_element = MagicMock()
    mock_promoter.driver.get_text_from_element = MagicMock(return_value="Post")
    mock_promoter.driver.wait_for_element = MagicMock()
    
    assert mock_promoter.post_to_group(campaign = "test_campaign", group="test_group") == True

def test_facebook_promoter_post_to_group_fails(mock_promoter):
    """Test posting to a group fails"""
    mock_promoter.driver.get_url = MagicMock()
    mock_promoter.driver.find_element = MagicMock(side_effect=Exception("Element not found"))
    mock_promoter.driver.send_keys_to_element = MagicMock()
    mock_promoter.driver.click_element = MagicMock()
    mock_promoter.driver.get_text_from_element = MagicMock(return_value="Post")
    mock_promoter.driver.wait_for_element = MagicMock()

    assert mock_promoter.post_to_group(campaign = "test_campaign", group="test_group") == False
    
def test_facebook_promoter_post_to_group_no_post_button(mock_promoter):
    """Test posting to a group fails if no post button"""
    mock_promoter.driver.get_url = MagicMock()
    mock_promoter.driver.find_element = MagicMock()
    mock_promoter.driver.send_keys_to_element = MagicMock()
    mock_promoter.driver.click_element = MagicMock()
    mock_promoter.driver.get_text_from_element = MagicMock(return_value="something_else")
    mock_promoter.driver.wait_for_element = MagicMock()
    
    assert mock_promoter.post_to_group(campaign = "test_campaign", group="test_group") == False
```