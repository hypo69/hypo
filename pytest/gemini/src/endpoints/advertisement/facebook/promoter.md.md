```python
import pytest
from unittest.mock import MagicMock, patch
from datetime import datetime, timedelta
from types import SimpleNamespace
from pathlib import Path
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads_ns

# Mock the Driver class and its methods
@pytest.fixture
def mock_driver():
    mock_driver = MagicMock(spec=Driver)
    return mock_driver


@pytest.fixture
def mock_group_data():
    """Provides a sample group data for testing."""
    return SimpleNamespace(
        id="123",
        last_promotion_time=None,
        promoted_categories=[],
        promoted_events=[],
        interval_hours=1,
        valid=True,
    )


@pytest.fixture
def mock_item_data():
    """Provides a sample item data for testing."""
    return SimpleNamespace(name="Test Item", url="https://test.com/item")

@pytest.fixture
def mock_j_loads_ns():
    """Mocks j_loads_ns"""
    with patch("src.endpoints.advertisement.facebook.promoter.j_loads_ns") as mock:
       yield mock

def test_facebook_promoter_init(mock_driver, mock_j_loads_ns):
    """Checks correct initialization of the FacebookPromoter class."""
    promoter = FacebookPromoter(
        d=mock_driver,
        promoter="aliexpress",
        group_file_paths=["test_path1", "test_path2"],
        no_video=True,
    )
    assert promoter.driver == mock_driver
    assert promoter.promoter == "aliexpress"
    assert promoter.group_file_paths == ["test_path1", "test_path2"]
    assert promoter.no_video == True
    mock_j_loads_ns.assert_called()


def test_facebook_promoter_init_with_pathlib_paths(mock_driver, mock_j_loads_ns):
    """Checks initialization with pathlib paths."""
    path1 = Path("test_path1")
    path2 = Path("test_path2")
    promoter = FacebookPromoter(
        d=mock_driver,
        promoter="aliexpress",
        group_file_paths=[path1, path2],
        no_video=False
    )
    assert promoter.group_file_paths == [path1, path2]
    mock_j_loads_ns.assert_called()

def test_facebook_promoter_init_with_single_path(mock_driver, mock_j_loads_ns):
    """Checks initialization with a single string path"""
    promoter = FacebookPromoter(
       d=mock_driver,
       promoter="aliexpress",
       group_file_paths="test_path1",
       no_video=False
    )
    assert promoter.group_file_paths == ["test_path1"]
    mock_j_loads_ns.assert_called()
    
def test_facebook_promoter_init_with_single_pathlib_path(mock_driver, mock_j_loads_ns):
    """Checks initialization with a single pathlib path"""
    path = Path("test_path1")
    promoter = FacebookPromoter(
        d=mock_driver,
        promoter="aliexpress",
        group_file_paths=path,
        no_video=False
    )
    assert promoter.group_file_paths == [path]
    mock_j_loads_ns.assert_called()


def test_promote_success(mock_driver, mock_group_data, mock_item_data):
    """Checks successful promotion."""
    promoter = FacebookPromoter(d=mock_driver, promoter="aliexpress")
    mock_driver.post_to_group.return_value = True
    result = promoter.promote(
        group=mock_group_data,
        item=mock_item_data,
        is_event=False,
        language="en",
        currency="USD",
    )
    assert result == True
    mock_driver.post_to_group.assert_called_once()


def test_promote_failure(mock_driver, mock_group_data, mock_item_data):
    """Checks handling of a failed promotion."""
    promoter = FacebookPromoter(d=mock_driver, promoter="aliexpress")
    mock_driver.post_to_group.return_value = False
    result = promoter.promote(
        group=mock_group_data,
        item=mock_item_data,
        is_event=False,
        language="en",
        currency="USD",
    )
    assert result == False
    mock_driver.post_to_group.assert_called_once()


def test_log_promotion_error_event(mock_driver):
    """Checks logging of event promotion errors."""
    promoter = FacebookPromoter(d=mock_driver, promoter="aliexpress")
    promoter.log_promotion_error(is_event=True, item_name="Test Event")
    # Cannot directly assert logging was called
    # This test ensures that the function runs without errors

def test_log_promotion_error_category(mock_driver):
    """Checks logging of category promotion errors."""
    promoter = FacebookPromoter(d=mock_driver, promoter="aliexpress")
    promoter.log_promotion_error(is_event=False, item_name="Test Category")
    # Cannot directly assert logging was called
    # This test ensures that the function runs without errors

def test_update_group_promotion_data_category(mock_driver, mock_group_data, mock_item_data):
    """Checks updating group data after a category promotion."""
    promoter = FacebookPromoter(d=mock_driver, promoter="aliexpress")
    promoter.update_group_promotion_data(
        group=mock_group_data, item_name=mock_item_data.name, is_event=False
    )
    assert mock_group_data.promoted_categories == [mock_item_data.name]


def test_update_group_promotion_data_event(mock_driver, mock_group_data, mock_item_data):
    """Checks updating group data after an event promotion."""
    promoter = FacebookPromoter(d=mock_driver, promoter="aliexpress")
    promoter.update_group_promotion_data(
        group=mock_group_data, item_name=mock_item_data.name, is_event=True
    )
    assert mock_group_data.promoted_events == [mock_item_data.name]

def test_process_groups_no_groups(mock_driver, mock_j_loads_ns):
    """Checks processing groups with no groups configured."""
    mock_j_loads_ns.return_value = []
    promoter = FacebookPromoter(d=mock_driver, promoter="aliexpress")
    promoter.process_groups(
        campaign_name="Test Campaign",
        events=[],
        group_categories_to_adv=["sales"],
        language="en",
        currency="USD",
    )
    mock_j_loads_ns.assert_called()


def test_process_groups_with_valid_group_and_category(mock_driver, mock_group_data, mock_item_data, mock_j_loads_ns):
    """Checks processing with a valid group and category to advertise."""
    mock_j_loads_ns.return_value = [mock_group_data]
    mock_driver.post_to_group.return_value = True
    promoter = FacebookPromoter(d=mock_driver, promoter="aliexpress")
    with patch.object(promoter, 'get_category_item', return_value=mock_item_data) as mock_get_category:
        promoter.process_groups(
            campaign_name="Test Campaign",
            events=[],
            group_categories_to_adv=["sales"],
            language="en",
            currency="USD",
        )
    mock_get_category.assert_called_once()
    mock_j_loads_ns.assert_called()
    assert mock_group_data.promoted_categories == [mock_item_data.name]
    mock_driver.post_to_group.assert_called_once()


def test_process_groups_with_valid_group_and_event(mock_driver, mock_group_data, mock_item_data, mock_j_loads_ns):
    """Checks processing with a valid group and an event."""
    mock_j_loads_ns.return_value = [mock_group_data]
    mock_driver.post_to_group.return_value = True
    promoter = FacebookPromoter(d=mock_driver, promoter="aliexpress")
    with patch.object(promoter, 'get_category_item', return_value=mock_item_data) as mock_get_category:
        promoter.process_groups(
            campaign_name="Test Campaign",
            events=[mock_item_data],
            is_event=True,
            group_categories_to_adv=[],
            language="en",
            currency="USD",
        )
    mock_get_category.assert_not_called()
    mock_j_loads_ns.assert_called()
    assert mock_group_data.promoted_events == [mock_item_data.name]
    mock_driver.post_to_group.assert_called_once()


def test_get_category_item(mock_driver, mock_group_data, mock_item_data):
    """Checks fetching of category item for promotion."""
    promoter = FacebookPromoter(d=mock_driver, promoter="aliexpress")
    with patch("src.endpoints.advertisement.facebook.promoter.get_ali_item_for_promotion", return_value=mock_item_data) as mock_get_ali_item:
      item = promoter.get_category_item(
          campaign_name="Test Campaign",
          group=mock_group_data,
          language="en",
          currency="USD",
      )
    assert item == mock_item_data
    mock_get_ali_item.assert_called_once()


def test_check_interval_eligible(mock_driver, mock_group_data):
    """Checks a group is eligible for promotion."""
    promoter = FacebookPromoter(d=mock_driver, promoter="aliexpress")
    mock_group_data.last_promotion_time = datetime.now() - timedelta(hours=2)
    assert promoter.check_interval(group=mock_group_data) == True


def test_check_interval_not_eligible(mock_driver, mock_group_data):
    """Checks if a group is not eligible for promotion because it has not been long enough."""
    promoter = FacebookPromoter(d=mock_driver, promoter="aliexpress")
    mock_group_data.last_promotion_time = datetime.now() - timedelta(minutes=30)
    assert promoter.check_interval(group=mock_group_data) == False


def test_check_interval_no_last_promotion(mock_driver, mock_group_data):
    """Checks the case when the group has never been promoted before."""
    promoter = FacebookPromoter(d=mock_driver, promoter="aliexpress")
    assert promoter.check_interval(group=mock_group_data) == True


def test_validate_group_valid(mock_driver, mock_group_data):
    """Checks validation of valid group data."""
    promoter = FacebookPromoter(d=mock_driver, promoter="aliexpress")
    assert promoter.validate_group(group=mock_group_data) == True


def test_validate_group_invalid(mock_driver):
    """Checks validation of invalid group data missing id"""
    promoter = FacebookPromoter(d=mock_driver, promoter="aliexpress")
    invalid_group_data = SimpleNamespace(
        last_promotion_time=None,
        promoted_categories=[],
        promoted_events=[],
        interval_hours=1,
        valid=True,
    )
    assert promoter.validate_group(group=invalid_group_data) == False


def test_validate_group_invalid_missing_interval_hours(mock_driver):
    """Checks validation of invalid group data missing interval_hours"""
    promoter = FacebookPromoter(d=mock_driver, promoter="aliexpress")
    invalid_group_data = SimpleNamespace(
       id="123",
        last_promotion_time=None,
        promoted_categories=[],
        promoted_events=[],
       valid=True,
    )
    assert promoter.validate_group(group=invalid_group_data) == False
```