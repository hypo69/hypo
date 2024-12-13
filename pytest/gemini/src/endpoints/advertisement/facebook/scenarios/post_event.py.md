```python
import pytest
from unittest.mock import MagicMock, patch
from types import SimpleNamespace
from hypotez.src.endpoints.advertisement.facebook.scenarios.post_event import (
    post_title,
    post_date,
    post_time,
    post_description,
    post_event,
)
from src.webdriver.driver import Driver

# Mock the logger to avoid printing during tests
from src.logger import logger
logger.error = MagicMock()


@pytest.fixture
def mock_driver():
    """Provides a mock Driver instance."""
    driver_mock = MagicMock(spec=Driver)
    driver_mock.execute_locator.return_value = True  # Default to successful execution
    return driver_mock

@pytest.fixture
def mock_event():
    """Provides a mock SimpleNamespace event for testing."""
    event_mock = SimpleNamespace(
        title="Test Event Title",
        start="2024-03-15 10:00",
        description="Test Event Description",
        promotional_link="https://example.com"
    )
    return event_mock


def test_post_title_valid_input(mock_driver):
    """Checks if the title is sent successfully with valid input."""
    title = "Test Title"
    assert post_title(mock_driver, title) is True
    mock_driver.execute_locator.assert_called_once()


def test_post_title_failed_to_send(mock_driver):
    """Checks if the function returns None if sending the title fails."""
    mock_driver.execute_locator.return_value = False
    title = "Test Title"
    assert post_title(mock_driver, title) is None
    mock_driver.execute_locator.assert_called_once()
    logger.error.assert_called_once()

def test_post_date_valid_input(mock_driver):
    """Checks if the date is sent successfully with valid input."""
    date = "2024-03-15"
    assert post_date(mock_driver, date) is True
    mock_driver.execute_locator.assert_called_once()

def test_post_date_failed_to_send(mock_driver):
    """Checks if the function returns None if sending the date fails."""
    mock_driver.execute_locator.return_value = False
    date = "2024-03-15"
    assert post_date(mock_driver, date) is None
    mock_driver.execute_locator.assert_called_once()
    logger.error.assert_called_once()


def test_post_time_valid_input(mock_driver):
    """Checks if the time is sent successfully with valid input."""
    time = "10:00"
    assert post_time(mock_driver, time) is True
    mock_driver.execute_locator.assert_called_once()

def test_post_time_failed_to_send(mock_driver):
    """Checks if the function returns None if sending the time fails."""
    mock_driver.execute_locator.return_value = False
    time = "10:00"
    assert post_time(mock_driver, time) is None
    mock_driver.execute_locator.assert_called_once()
    logger.error.assert_called_once()

def test_post_description_valid_input(mock_driver):
    """Checks if the description is sent successfully with valid input."""
    description = "Test Description"
    assert post_description(mock_driver, description) is True
    mock_driver.execute_locator.assert_called_once()
    mock_driver.scroll.assert_called_once()


def test_post_description_failed_to_send(mock_driver):
    """Checks if the function returns None if sending the description fails."""
    mock_driver.execute_locator.return_value = False
    description = "Test Description"
    assert post_description(mock_driver, description) is None
    mock_driver.execute_locator.assert_called_once()
    mock_driver.scroll.assert_called_once()
    logger.error.assert_called_once()

def test_post_event_success(mock_driver, mock_event):
    """Test successful event posting."""
    with patch("hypotez.src.endpoints.advertisement.facebook.scenarios.post_event.time.sleep", return_value=None):
         assert post_event(mock_driver, mock_event) is True
    assert mock_driver.execute_locator.call_count == 4  # title, date, time, description
    assert mock_driver.scroll.call_count == 1 #scroll
    mock_driver.execute_locator.assert_called_with(locator=mock_driver.locator.event_send)


def test_post_event_title_fails(mock_driver, mock_event):
    """Test when posting the title fails."""
    mock_driver.execute_locator.side_effect = [False, True, True, True] # Make the first call fail
    assert post_event(mock_driver, mock_event) is None
    mock_driver.execute_locator.assert_called_once()


def test_post_event_date_fails(mock_driver, mock_event):
    """Test when posting the date fails."""
    mock_driver.execute_locator.side_effect = [True, False, True, True] # Make the second call fail
    assert post_event(mock_driver, mock_event) is None
    assert mock_driver.execute_locator.call_count == 2


def test_post_event_time_fails(mock_driver, mock_event):
    """Test when posting the time fails."""
    mock_driver.execute_locator.side_effect = [True, True, False, True]  # Make the third call fail
    assert post_event(mock_driver, mock_event) is None
    assert mock_driver.execute_locator.call_count == 3

def test_post_event_description_fails(mock_driver, mock_event):
    """Test when posting the description fails."""
    mock_driver.execute_locator.side_effect = [True, True, True, False]  # Make the forth call fail
    with patch("hypotez.src.endpoints.advertisement.facebook.scenarios.post_event.time.sleep", return_value=None):
        assert post_event(mock_driver, mock_event) is None
    assert mock_driver.execute_locator.call_count == 4
    mock_driver.scroll.assert_called_once()

def test_post_event_send_fails(mock_driver, mock_event):
    """Test when sending the event fails."""
    mock_driver.execute_locator.side_effect = [True, True, True, True, False]  # Make the last call fail
    with patch("hypotez.src.endpoints.advertisement.facebook.scenarios.post_event.time.sleep", return_value=None):
       assert post_event(mock_driver, mock_event) is None
    assert mock_driver.execute_locator.call_count == 5
    mock_driver.scroll.assert_called_once()
```