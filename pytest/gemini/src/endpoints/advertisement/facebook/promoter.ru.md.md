```python
import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path
from types import SimpleNamespace
from datetime import datetime, timedelta
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
from src.webdriver.driver import Driver  # Assuming Driver class exists


# Fixtures
@pytest.fixture
def mock_driver():
    """Mocks a Driver instance for testing."""
    return MagicMock(spec=Driver)


@pytest.fixture
def valid_group_data():
    """Provides valid group data."""
    return SimpleNamespace(
        id="group123",
        last_promotion_time=None,
        promoted_categories=[],
        promoted_events=[],
        interval_between_promotions=10,
        data={"some": "data"},
    )

@pytest.fixture
def group_data_with_last_promotion():
    """Provides group data with a last_promotion_time."""
    return SimpleNamespace(
        id="group123",
        last_promotion_time=datetime.now() - timedelta(seconds=5),
        promoted_categories=[],
        promoted_events=[],
        interval_between_promotions=10,
        data={"some": "data"},
    )


@pytest.fixture
def invalid_group_data():
    """Provides invalid group data."""
    return SimpleNamespace(id="group123", last_promotion_time=None, promoted_categories=[], interval_between_promotions=None)


@pytest.fixture
def valid_item_data():
    """Provides valid item data."""
    return SimpleNamespace(name="item1", link="http://example.com/item1")


@pytest.fixture
def promoter(mock_driver):
    """Creates a FacebookPromoter instance with mocked dependencies."""
    return FacebookPromoter(d=mock_driver, promoter="aliexpress")

@pytest.fixture
def promoter_with_group_files(mock_driver):
    """Creates a FacebookPromoter instance with mocked dependencies."""
    return FacebookPromoter(d=mock_driver, promoter="aliexpress", group_file_paths=["path/to/group/file1.json"])

@pytest.fixture
def mock_j_loads_ns():
    with patch("src.endpoints.advertisement.facebook.promoter.j_loads_ns") as mock:
        mock.return_value = [SimpleNamespace(id="group123", last_promotion_time=None, promoted_categories=[], interval_between_promotions=10)]
        yield mock

def test_facebook_promoter_init(mock_driver):
    """Checks if FacebookPromoter is initialized correctly."""
    promoter = FacebookPromoter(
        d=mock_driver,
        promoter="aliexpress",
        group_file_paths=["path/to/group/file1.json", "path/to/group/file2.json"],
        no_video=True,
    )
    assert promoter.driver == mock_driver
    assert promoter.promoter_name == "aliexpress"
    assert promoter.group_file_paths == ["path/to/group/file1.json", "path/to/group/file2.json"]
    assert promoter.no_video is True
    assert promoter.group_data == []


def test_facebook_promoter_init_no_group_files(mock_driver):
    """Checks if FacebookPromoter is initialized correctly without group_file_paths."""
    promoter = FacebookPromoter(
        d=mock_driver,
        promoter="aliexpress",
    )
    assert promoter.group_file_paths == []
    assert promoter.group_data == []


def test_promote_successful(promoter, mock_driver, valid_group_data, valid_item_data):
    """Checks successful promotion."""
    mock_driver.get_current_url.return_value = "https://facebook.com/some-group"
    promoter.driver.post_message = MagicMock()  # Mock post_message
    result = promoter.promote(
        group=valid_group_data,
        item=valid_item_data,
        is_event=False,
        language="en",
        currency="USD",
    )
    assert result is True
    promoter.driver.post_message.assert_called_once()


def test_promote_unsuccessful(promoter, mock_driver, valid_group_data, valid_item_data):
    """Checks unsuccessful promotion."""
    mock_driver.get_current_url.return_value = "https://not-facebook.com/some-group"
    promoter.driver.post_message = MagicMock()
    result = promoter.promote(
        group=valid_group_data,
        item=valid_item_data,
        is_event=True,
        language="en",
        currency="USD",
    )
    assert result is False
    promoter.driver.post_message.assert_not_called()


def test_log_promotion_error_event(promoter):
    """Checks logging promotion errors for events."""
    with patch("src.endpoints.advertisement.facebook.promoter.logging") as mock_logging:
        promoter.log_promotion_error(is_event=True, item_name="event1")
        mock_logging.error.assert_called_once()


def test_log_promotion_error_category(promoter):
    """Checks logging promotion errors for categories."""
    with patch("src.endpoints.advertisement.facebook.promoter.logging") as mock_logging:
        promoter.log_promotion_error(is_event=False, item_name="category1")
        mock_logging.error.assert_called_once()

def test_update_group_promotion_data_category(promoter, valid_group_data, valid_item_data):
    """Checks updating group data after category promotion."""
    promoter.update_group_promotion_data(
        group=valid_group_data, item_name=valid_item_data.name, is_event=False
    )
    assert valid_group_data.promoted_categories == [valid_item_data.name]
    assert valid_group_data.promoted_events == []


def test_update_group_promotion_data_event(promoter, valid_group_data, valid_item_data):
    """Checks updating group data after event promotion."""
    promoter.update_group_promotion_data(
        group=valid_group_data, item_name=valid_item_data.name, is_event=True
    )
    assert valid_group_data.promoted_events == [valid_item_data.name]
    assert valid_group_data.promoted_categories == []

def test_process_groups_no_files(promoter, valid_group_data, mock_j_loads_ns):
    """Checks processing groups when no group files are provided."""
    promoter.promote = MagicMock(return_value=True)
    promoter.check_interval = MagicMock(return_value=True)
    promoter.validate_group = MagicMock(return_value=True)
    promoter.get_category_item = MagicMock(return_value=SimpleNamespace(name="test_category"))

    promoter.process_groups(
        campaign_name="test_campaign",
        events=[],
        group_categories_to_adv=["sales"],
        language="en",
        currency="USD"
    )
    
    promoter.promote.assert_not_called()


def test_process_groups_with_files(promoter_with_group_files, mock_j_loads_ns):
    """Checks processing groups when group files are provided."""
    promoter_with_group_files.promote = MagicMock(return_value=True)
    promoter_with_group_files.check_interval = MagicMock(return_value=True)
    promoter_with_group_files.validate_group = MagicMock(return_value=True)
    promoter_with_group_files.get_category_item = MagicMock(return_value=SimpleNamespace(name="test_category"))
    
    promoter_with_group_files.process_groups(
        campaign_name="test_campaign",
        events=[],
        group_categories_to_adv=["sales"],
        language="en",
        currency="USD",
    )
    promoter_with_group_files.promote.assert_called_once()


def test_process_groups_with_no_interval(promoter_with_group_files, mock_j_loads_ns):
    """Checks that promotion does not occur when interval check returns False."""
    promoter_with_group_files.promote = MagicMock(return_value=True)
    promoter_with_group_files.check_interval = MagicMock(return_value=False)
    promoter_with_group_files.validate_group = MagicMock(return_value=True)
    promoter_with_group_files.get_category_item = MagicMock(return_value=SimpleNamespace(name="test_category"))
    
    promoter_with_group_files.process_groups(
        campaign_name="test_campaign",
        events=[],
        group_categories_to_adv=["sales"],
        language="en",
        currency="USD",
    )
    promoter_with_group_files.promote.assert_not_called()


def test_process_groups_invalid_group_data(promoter_with_group_files, mock_j_loads_ns):
    """Checks that promotion does not occur with invalid group data."""
    promoter_with_group_files.promote = MagicMock(return_value=True)
    promoter_with_group_files.check_interval = MagicMock(return_value=True)
    promoter_with_group_files.validate_group = MagicMock(return_value=False)
    promoter_with_group_files.get_category_item = MagicMock(return_value=SimpleNamespace(name="test_category"))
    
    promoter_with_group_files.process_groups(
        campaign_name="test_campaign",
        events=[],
        group_categories_to_adv=["sales"],
        language="en",
        currency="USD",
    )
    promoter_with_group_files.promote.assert_not_called()



def test_get_category_item(promoter, valid_group_data):
    """Checks getting a category item."""
    with patch("src.endpoints.advertisement.facebook.promoter.j_loads_ns") as mock_j_loads_ns:
       mock_j_loads_ns.return_value = [SimpleNamespace(name="test_category")]
       item = promoter.get_category_item(
            campaign_name="test_campaign",
            group=valid_group_data,
            language="en",
            currency="USD",
        )
    assert item is not None
    assert item.name == "test_category"



def test_check_interval_valid(promoter, group_data_with_last_promotion):
    """Checks interval check when enough time has passed."""
    assert promoter.check_interval(group_data_with_last_promotion) is False



def test_check_interval_not_valid(promoter, valid_group_data):
    """Checks interval check when not enough time has passed."""
    assert promoter.check_interval(valid_group_data) is True


def test_validate_group_valid(promoter, valid_group_data):
    """Checks validation of valid group data."""
    assert promoter.validate_group(valid_group_data) is True

def test_validate_group_invalid(promoter, invalid_group_data):
    """Checks validation of invalid group data."""
    assert promoter.validate_group(invalid_group_data) is False
```