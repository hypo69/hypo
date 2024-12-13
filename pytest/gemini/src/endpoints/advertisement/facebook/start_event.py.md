```python
import pytest
from unittest.mock import MagicMock, patch
import time
from src.endpoints.advertisement.facebook.start_event import FacebookPromoter, Driver, Chrome, logger

# Fixture for a mock driver
@pytest.fixture
def mock_driver():
    """Provides a mock Driver object for testing."""
    mock_driver = MagicMock(spec=Driver)
    mock_driver.get_url = MagicMock()
    return mock_driver

# Fixture for a mock promoter
@pytest.fixture
def mock_promoter(mock_driver):
    """Provides a mock FacebookPromoter object for testing."""
    mock_promoter = MagicMock(spec=FacebookPromoter)
    mock_promoter.run_events = MagicMock()
    return mock_promoter

# Fixture for mock time
@pytest.fixture
def mock_time():
    with patch('src.endpoints.advertisement.facebook.start_event.time') as mock_time:
        yield mock_time

# Test case for successful promoter run
def test_successful_promoter_run(mock_driver, mock_promoter, mock_time):
    """
    Tests the main loop execution when the promoter runs successfully
    and is interrupted by a KeyboardInterrupt.
    """
    
    mock_time.strftime.return_value = "00:00:00"
    mock_time.sleep = MagicMock()

    with patch('src.endpoints.advertisement.facebook.start_event.FacebookPromoter', return_value=mock_promoter):
      with patch('src.endpoints.advertisement.facebook.start_event.Driver', return_value=mock_driver):
        with pytest.raises(KeyboardInterrupt):
            # Simulate the loop and interruption
            try:
                while True:
                    logger.debug(f"waikig up {time.strftime('%H:%M:%S')}",None,False)
                    mock_promoter.run_events.return_value = None
                    mock_promoter.run_events(events_names=["choice_day_01_10"], group_file_paths=["my_managed_groups.json",
                                            "usa.json",
                                            "he_il.json",
                                            "ru_il.json",
                                            "katia_homepage.json",
                                            
                                            "ru_usd.json",
                                            "ger_en_eur.json",])
                    logger.debug(f"going to sleep at {time.strftime('%H:%M:%S')}",None,False)
                    time.sleep(7200)
            except KeyboardInterrupt as e:
                logger.info("Campaign promotion interrupted.")
                raise e
    
    mock_driver.get_url.assert_called_once_with(r"https://facebook.com")
    mock_promoter.run_events.assert_called()
    mock_time.sleep.assert_called_once_with(7200)
    
# Test case for KeyboardInterrupt
def test_keyboard_interrupt_handling(mock_driver, mock_promoter, mock_time):
    """
    Tests the handling of a KeyboardInterrupt during the main loop.
    """
    mock_time.strftime.return_value = "00:00:00"
    mock_time.sleep = MagicMock()

    with patch('src.endpoints.advertisement.facebook.start_event.FacebookPromoter', return_value=mock_promoter):
      with patch('src.endpoints.advertisement.facebook.start_event.Driver', return_value=mock_driver):
        with pytest.raises(KeyboardInterrupt) as excinfo:
            try:
              while True:
                logger.debug(f"waikig up {time.strftime('%H:%M:%S')}",None,False)
                mock_promoter.run_events(events_names=["choice_day_01_10"], group_file_paths=["my_managed_groups.json",
                                            "usa.json",
                                            "he_il.json",
                                            "ru_il.json",
                                            "katia_homepage.json",
                                            
                                            "ru_usd.json",
                                            "ger_en_eur.json",])
                logger.debug(f"going to sleep at {time.strftime('%H:%M:%S')}",None,False)
                time.sleep(7200)
            except KeyboardInterrupt as e:
              logger.info("Campaign promotion interrupted.")
              raise e
            
    assert excinfo.type == KeyboardInterrupt
    mock_driver.get_url.assert_called_once_with(r"https://facebook.com")
    mock_promoter.run_events.assert_called()
    mock_time.sleep.assert_called_once_with(7200)
    
# Test case for exception during promoter.run_events
def test_exception_during_run_events(mock_driver, mock_promoter, mock_time):
    """
    Tests when an exception occurs during promoter.run_events.
    """
    mock_time.strftime.return_value = "00:00:00"
    mock_time.sleep = MagicMock()
    mock_promoter.run_events.side_effect = Exception("Test exception")


    with patch('src.endpoints.advertisement.facebook.start_event.FacebookPromoter', return_value=mock_promoter):
      with patch('src.endpoints.advertisement.facebook.start_event.Driver', return_value=mock_driver):
        with pytest.raises(Exception, match="Test exception"):
          try:
              while True:
                logger.debug(f"waikig up {time.strftime('%H:%M:%S')}",None,False)
                mock_promoter.run_events(events_names=["choice_day_01_10"], group_file_paths=["my_managed_groups.json",
                                            "usa.json",
                                            "he_il.json",
                                            "ru_il.json",
                                            "katia_homepage.json",
                                            
                                            "ru_usd.json",
                                            "ger_en_eur.json",])
                logger.debug(f"going to sleep at {time.strftime('%H:%M:%S')}",None,False)
                time.sleep(7200)
          except Exception as e:
                raise e
    mock_driver.get_url.assert_called_once_with(r"https://facebook.com")
    mock_promoter.run_events.assert_called()
    mock_time.sleep.assert_not_called()
```