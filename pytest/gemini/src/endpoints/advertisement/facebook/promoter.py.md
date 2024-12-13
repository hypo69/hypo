```python
import pytest
from unittest.mock import MagicMock, patch
from datetime import datetime, timedelta
from pathlib import Path
from types import SimpleNamespace
from src.endpoints.advertisement.facebook.promoter import FacebookPromoter, get_event_url
from src.webdriver.driver import Driver
from src.utils.jjson import j_loads_ns, j_dumps
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src.endpoints.advertisement.facebook.scenarios import post_message, post_event, post_ad
from src.utils.file import read_text_file, get_filenames

# Fixtures
@pytest.fixture
def mock_driver():
    """Mocks the WebDriver instance."""
    mock_driver = MagicMock(spec=Driver)
    return mock_driver

@pytest.fixture
def mock_group_data():
    """Provides test group data."""
    group = SimpleNamespace(
        group_url="https://www.facebook.com/groups/12345",
        group_categories=['sales'],
        status='active',
        language='en',
        currency='USD',
        promoted_categories=[],
        promoted_events=[],
        last_promo_sended = None
    )
    return group

@pytest.fixture
def mock_item_data():
    """Provides test item data."""
    item = SimpleNamespace(
        category_name='Test Category',
        event_name='Test Event',
        language = SimpleNamespace(en='Test Message'),
        description='Test Description',
        start = datetime.now(),
        end = datetime.now() + timedelta(hours=1),
        promotional_link = 'https://test.link'
    )
    return item

@pytest.fixture
def mock_event_item_data():
    """Provides test item data."""
    item = SimpleNamespace(
        event_name='Test Event',
        language = SimpleNamespace(en='Test Event Message'),
        start = datetime.now(),
        end = datetime.now() + timedelta(hours=1),
        promotional_link = 'https://test.link'
    )
    return item

@pytest.fixture
def mock_campaign_editor():
    """Mocks the AliCampaignEditor instance."""
    mock_editor = MagicMock(spec=AliCampaignEditor)
    mock_editor.list_categories = ['Test Category']
    mock_editor.get_category.return_value = SimpleNamespace(category_name='Test Category')
    mock_editor.get_category_products.return_value = ['product1', 'product2']
    return mock_editor

# Tests for get_event_url
def test_get_event_url_valid_group_url():
    """Checks correct URL generation with a valid group URL."""
    group_url = "https://www.facebook.com/groups/12345/"
    expected_url = "https://www.facebook.com/events/create/?acontext=%7B%22event_action_history%22%3A%5B%7B%22surface%22%3A%22group%22%7D%2C%7B%22mechanism%22%3A%22upcoming_events_for_group%22%2C%22surface%22%3A%22group%22%7D%5D%2C%22ref_notif_type%22%3Anull%7D&dialog_entry_point=group_events_tab&group_id=12345"
    assert get_event_url(group_url) == expected_url

def test_get_event_url_group_url_without_trailing_slash():
    """Checks correct URL generation with a valid group URL without a trailing slash."""
    group_url = "https://www.facebook.com/groups/12345"
    expected_url = "https://www.facebook.com/events/create/?acontext=%7B%22event_action_history%22%3A%5B%7B%22surface%22%3A%22group%22%7D%2C%7B%22mechanism%22%3A%22upcoming_events_for_group%22%2C%22surface%22%3A%22group%22%7D%5D%2C%22ref_notif_type%22%3Anull%7D&dialog_entry_point=group_events_tab&group_id=12345"
    assert get_event_url(group_url) == expected_url

# Tests for FacebookPromoter.__init__
def test_facebook_promoter_init_default_group_paths(mock_driver, monkeypatch):
    """Checks initialization with default group file paths."""
    monkeypatch.setattr('src.endpoints.advertisement.facebook.promoter.get_filenames', lambda x: ["group1.json", "group2.json"])
    promoter = FacebookPromoter(d=mock_driver, promoter="test_promoter")
    assert promoter.group_file_paths == ["group1.json", "group2.json"]
    assert promoter.promoter == "test_promoter"
    assert promoter.d == mock_driver
    assert promoter.no_video == False

def test_facebook_promoter_init_custom_group_paths(mock_driver):
    """Checks initialization with custom group file paths."""
    custom_paths = ["custom_group1.json", "custom_group2.json"]
    promoter = FacebookPromoter(d=mock_driver, promoter="test_promoter", group_file_paths=custom_paths, no_video=True)
    assert promoter.group_file_paths == custom_paths
    assert promoter.no_video == True

def test_facebook_promoter_init_single_group_path(mock_driver):
    """Checks initialization with a single group file path."""
    custom_path = "custom_group.json"
    promoter = FacebookPromoter(d=mock_driver, promoter="test_promoter", group_file_paths=custom_path)
    assert promoter.group_file_paths == custom_path
    assert promoter.no_video == False

# Tests for FacebookPromoter.promote
@patch('src.endpoints.advertisement.facebook.promoter.post_event')
@patch('src.endpoints.advertisement.facebook.promoter.post_message')
@patch('src.endpoints.advertisement.facebook.promoter.post_ad')
def test_promote_event_valid(mock_post_ad, mock_post_message, mock_post_event, mock_driver, mock_group_data, mock_event_item_data):
    """Checks promotion of an event with valid inputs."""
    mock_post_event.return_value = True
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    result = promoter.promote(group=mock_group_data, item=mock_event_item_data, is_event=True, language='en', currency='USD')
    assert result is True
    mock_post_event.assert_called_once()
    mock_post_message.assert_not_called()
    mock_post_ad.assert_not_called()
    assert mock_group_data.promoted_events == ['Test Event']

@patch('src.endpoints.advertisement.facebook.promoter.post_event')
@patch('src.endpoints.advertisement.facebook.promoter.post_message')
@patch('src.endpoints.advertisement.facebook.promoter.post_ad')
def test_promote_event_post_fails(mock_post_ad, mock_post_message, mock_post_event, mock_driver, mock_group_data, mock_event_item_data):
    """Checks promotion of an event when post_event returns False"""
    mock_post_event.return_value = False
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    result = promoter.promote(group=mock_group_data, item=mock_event_item_data, is_event=True)
    assert result is None
    mock_post_event.assert_called_once()
    mock_post_message.assert_not_called()
    mock_post_ad.assert_not_called()
    assert mock_group_data.promoted_events == []

@patch('src.endpoints.advertisement.facebook.promoter.post_event')
@patch('src.endpoints.advertisement.facebook.promoter.post_message')
@patch('src.endpoints.advertisement.facebook.promoter.post_ad')
def test_promote_message_valid(mock_post_ad, mock_post_message, mock_post_event, mock_driver, mock_group_data, mock_item_data):
    """Checks promotion of a message with valid inputs."""
    mock_post_message.return_value = True
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    result = promoter.promote(group=mock_group_data, item=mock_item_data, is_event=False, language='en', currency='USD')
    assert result is True
    mock_post_message.assert_called_once()
    mock_post_event.assert_not_called()
    mock_post_ad.assert_not_called()
    assert mock_group_data.promoted_categories == ['Test Category']

@patch('src.endpoints.advertisement.facebook.promoter.post_event')
@patch('src.endpoints.advertisement.facebook.promoter.post_message')
@patch('src.endpoints.advertisement.facebook.promoter.post_ad')
def test_promote_message_post_fails(mock_post_ad, mock_post_message, mock_post_event, mock_driver, mock_group_data, mock_item_data):
    """Checks promotion of a message when post_message returns False"""
    mock_post_message.return_value = False
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    result = promoter.promote(group=mock_group_data, item=mock_item_data, is_event=False)
    assert result is None
    mock_post_message.assert_called_once()
    mock_post_event.assert_not_called()
    mock_post_ad.assert_not_called()
    assert mock_group_data.promoted_categories == []

@patch('src.endpoints.advertisement.facebook.promoter.post_event')
@patch('src.endpoints.advertisement.facebook.promoter.post_message')
@patch('src.endpoints.advertisement.facebook.promoter.post_ad')
def test_promote_message_ad_valid(mock_post_ad, mock_post_message, mock_post_event, mock_driver, mock_group_data, mock_item_data):
    """Checks promotion of a message with valid inputs."""
    mock_post_ad.return_value = True
    promoter = FacebookPromoter(d=mock_driver, promoter='emil')
    result = promoter.promote(group=mock_group_data, item=mock_item_data, is_event=False, language='en', currency='USD')
    assert result is True
    mock_post_ad.assert_called_once()
    mock_post_message.assert_not_called()
    mock_post_event.assert_not_called()
    assert mock_group_data.promoted_categories == ['Test Category']

@patch('src.endpoints.advertisement.facebook.promoter.post_event')
@patch('src.endpoints.advertisement.facebook.promoter.post_message')
@patch('src.endpoints.advertisement.facebook.promoter.post_ad')
def test_promote_message_ad_fails(mock_post_ad, mock_post_message, mock_post_event, mock_driver, mock_group_data, mock_item_data):
    """Checks promotion of a message when post_message returns False"""
    mock_post_ad.return_value = False
    promoter = FacebookPromoter(d=mock_driver, promoter='emil')
    result = promoter.promote(group=mock_group_data, item=mock_item_data, is_event=False)
    assert result is None
    mock_post_ad.assert_called_once()
    mock_post_message.assert_not_called()
    mock_post_event.assert_not_called()
    assert mock_group_data.promoted_categories == []


def test_promote_language_mismatch(mock_driver, mock_group_data, mock_item_data):
    """Checks that promotion is skipped due to language mismatch."""
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    mock_group_data.language = 'fr'
    result = promoter.promote(group=mock_group_data, item=mock_item_data, is_event=False, language='en', currency='USD')
    assert result is None

def test_promote_currency_mismatch(mock_driver, mock_group_data, mock_item_data):
    """Checks that promotion is skipped due to currency mismatch."""
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    mock_group_data.currency = 'EUR'
    result = promoter.promote(group=mock_group_data, item=mock_item_data, is_event=False, language='en', currency='USD')
    assert result is None

def test_promote_language_mismatch_event(mock_driver, mock_group_data, mock_event_item_data):
    """Checks that promotion is skipped due to language mismatch."""
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    mock_group_data.language = 'fr'
    result = promoter.promote(group=mock_group_data, item=mock_event_item_data, is_event=True, language='en', currency='USD')
    assert result is None

def test_promote_currency_mismatch_event(mock_driver, mock_group_data, mock_event_item_data):
    """Checks that promotion is skipped due to currency mismatch."""
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    mock_group_data.currency = 'EUR'
    result = promoter.promote(group=mock_group_data, item=mock_event_item_data, is_event=True, language='en', currency='USD')
    assert result is None

# Tests for FacebookPromoter.log_promotion_error
@patch('src.endpoints.advertisement.facebook.promoter.logger')
def test_log_promotion_error_event(mock_logger, mock_driver):
    """Checks correct logging of event promotion error."""
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    promoter.log_promotion_error(is_event=True, item_name='Test Event')
    mock_logger.debug.assert_called_with('Error while posting event Test Event', None, False)


@patch('src.endpoints.advertisement.facebook.promoter.logger')
def test_log_promotion_error_category(mock_logger, mock_driver):
    """Checks correct logging of category promotion error."""
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    promoter.log_promotion_error(is_event=False, item_name='Test Category')
    mock_logger.debug.assert_called_with('Error while posting category Test Category', None, False)

# Tests for FacebookPromoter.update_group_promotion_data
def test_update_group_promotion_data_category(mock_group_data, mock_driver):
    """Checks correct updating of group data for category promotion."""
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    promoter.update_group_promotion_data(group=mock_group_data, item_name='Test Category')
    assert 'Test Category' in mock_group_data.promoted_categories
    assert mock_group_data.last_promo_sended is not None

def test_update_group_promotion_data_event(mock_group_data, mock_driver):
    """Checks correct updating of group data for event promotion."""
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    promoter.update_group_promotion_data(group=mock_group_data, item_name='Test Event', is_event=True)
    assert 'Test Event' in mock_group_data.promoted_events
    assert mock_group_data.last_promo_sended is not None

def test_update_group_promotion_data_empty_list(mock_group_data, mock_driver):
    """Checks correct updating of group data for category promotion when lists are empty."""
    mock_group_data.promoted_categories = None
    mock_group_data.promoted_events = None
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    promoter.update_group_promotion_data(group=mock_group_data, item_name='Test Category')
    promoter.update_group_promotion_data(group=mock_group_data, item_name='Test Event', is_event=True)
    assert mock_group_data.promoted_categories == ['Test Category']
    assert mock_group_data.promoted_events == ['Test Event']
    assert mock_group_data.last_promo_sended is not None

# Tests for FacebookPromoter.process_groups
@patch('src.endpoints.advertisement.facebook.promoter.j_dumps')
@patch('src.endpoints.advertisement.facebook.promoter.time.sleep')
@patch('src.endpoints.advertisement.facebook.promoter.FacebookPromoter.promote')
@patch('src.endpoints.advertisement.facebook.promoter.FacebookPromoter.get_category_item')
@patch('src.endpoints.advertisement.facebook.promoter.get_event_url')
@patch('src.endpoints.advertisement.facebook.promoter.j_loads_ns')
@patch('src.endpoints.advertisement.facebook.promoter.logger')
def test_process_groups_valid_category(mock_logger, mock_j_loads_ns, mock_get_event_url, mock_get_category_item, mock_promote, mock_sleep, mock_j_dumps, mock_driver, mock_group_data, mock_item_data, monkeypatch):
    """Checks processing of groups for category promotion."""
    monkeypatch.setattr('src.endpoints.advertisement.facebook.promoter.get_filenames', lambda x: ["group1.json"])
    mock_j_loads_ns.return_value = {'https://www.facebook.com/groups/12345': mock_group_data}
    mock_get_category_item.return_value = mock_item_data
    mock_promote.return_value = True
    mock_group_data.last_promo_sended = datetime.now() - timedelta(days=2)
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    promoter.process_groups(campaign_name='test_campaign', group_file_paths=["group1.json"], language='en', currency='USD')
    mock_j_loads_ns.assert_called_once()
    mock_get_event_url.assert_not_called()
    mock_get_category_item.assert_called_once()
    mock_promote.assert_called_once()
    mock_sleep.assert_called_once()
    mock_j_dumps.assert_called_once()
    mock_logger.debug.assert_called()
    mock_driver.get_url.assert_called_once()

@patch('src.endpoints.advertisement.facebook.promoter.j_dumps')
@patch('src.endpoints.advertisement.facebook.promoter.time.sleep')
@patch('src.endpoints.advertisement.facebook.promoter.FacebookPromoter.promote')
@patch('src.endpoints.advertisement.facebook.promoter.FacebookPromoter.get_category_item')
@patch('src.endpoints.advertisement.facebook.promoter.get_event_url')
@patch('src.endpoints.advertisement.facebook.promoter.j_loads_ns')
@patch('src.endpoints.advertisement.facebook.promoter.logger')
def test_process_groups_valid_event(mock_logger, mock_j_loads_ns, mock_get_event_url, mock_get_category_item, mock_promote, mock_sleep, mock_j_dumps, mock_driver, mock_group_data, mock_event_item_data, monkeypatch):
    """Checks processing of groups for event promotion."""
    monkeypatch.setattr('src.endpoints.advertisement.facebook.promoter.get_filenames', lambda x: ["group1.json"])
    mock_j_loads_ns.return_value = {'https://www.facebook.com/groups/12345': mock_group_data}
    mock_promote.return_value = True
    mock_get_event_url.return_value = "https://www.facebook.com/events/create/?acontext=%7B%22event_action_history%22%3A%5B%7B%22surface%22%3A%22group%22%7D%2C%7B%22mechanism%22%3A%22upcoming_events_for_group%22%2C%22surface%22%3A%22group%22%7D%5D%2C%22ref_notif_type%22%3Anull%7D&dialog_entry_point=group_events_tab&group_id=12345"
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    promoter.process_groups(events=[mock_event_item_data], is_event=True, group_file_paths=["group1.json"], language='en', currency='USD')
    mock_j_loads_ns.assert_called_once()
    mock_get_event_url.assert_called_once()
    mock_get_category_item.assert_not_called()
    mock_promote.assert_called_once()
    mock_sleep.assert_called_once()
    mock_j_dumps.assert_called_once()
    mock_logger.debug.assert_called()
    mock_driver.get_url.assert_called_once()

@patch('src.endpoints.advertisement.facebook.promoter.logger')
def test_process_groups_no_campaign_no_events(mock_logger, mock_driver, monkeypatch):
    """Checks that no promotion happens when no campaign or events are provided."""
    monkeypatch.setattr('src.endpoints.advertisement.facebook.promoter.get_filenames', lambda x: ["group1.json"])
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    promoter.process_groups()
    mock_logger.debug.assert_called_with("Nothing to promote!")

@patch('src.endpoints.advertisement.facebook.promoter.logger')
def test_process_groups_invalid_group_file(mock_logger, mock_driver, monkeypatch):
    """Checks correct handling of invalid group file."""
    monkeypatch.setattr('src.endpoints.advertisement.facebook.promoter.j_loads_ns', lambda x: None)
    monkeypatch.setattr('src.endpoints.advertisement.facebook.promoter.get_filenames', lambda x: ["group1.json"])
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    promoter.process_groups(campaign_name='test_campaign', group_file_paths=["group1.json"])
    mock_logger.error.assert_called()

@patch('src.endpoints.advertisement.facebook.promoter.j_dumps')
@patch('src.endpoints.advertisement.facebook.promoter.time.sleep')
@patch('src.endpoints.advertisement.facebook.promoter.FacebookPromoter.promote')
@patch('src.endpoints.advertisement.facebook.promoter.FacebookPromoter.get_category_item')
@patch('src.endpoints.advertisement.facebook.promoter.get_event_url')
@patch('src.endpoints.advertisement.facebook.promoter.j_loads_ns')
@patch('src.endpoints.advertisement.facebook.promoter.logger')
def test_process_groups_inactive_group(mock_logger, mock_j_loads_ns, mock_get_event_url, mock_get_category_item, mock_promote, mock_sleep, mock_j_dumps, mock_driver, mock_group_data, mock_item_data, monkeypatch):
    """Checks that inactive groups are skipped."""
    monkeypatch.setattr('src.endpoints.advertisement.facebook.promoter.get_filenames', lambda x: ["group1.json"])
    mock_group_data.status = 'inactive'
    mock_j_loads_ns.return_value = {'https://www.facebook.com/groups/12345': mock_group_data}
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    promoter.process_groups(campaign_name='test_campaign', group_file_paths=["group1.json"])
    mock_j_loads_ns.assert_called_once()
    mock_get_event_url.assert_not_called()
    mock_get_category_item.assert_not_called()
    mock_promote.assert_not_called()
    mock_sleep.assert_not_called()
    mock_j_dumps.assert_not_called()
    mock_logger.debug.assert_called()

@patch('src.endpoints.advertisement.facebook.promoter.j_dumps')
@patch('src.endpoints.advertisement.facebook.promoter.time.sleep')
@patch('src.endpoints.advertisement.facebook.promoter.FacebookPromoter.promote')
@patch('src.endpoints.advertisement.facebook.promoter.FacebookPromoter.get_category_item')
@patch('src.endpoints.advertisement.facebook.promoter.get_event_url')
@patch('src.endpoints.advertisement.facebook.promoter.j_loads_ns')
@patch('src.endpoints.advertisement.facebook.promoter.logger')
def test_process_groups_category_not_in_group(mock_logger, mock_j_loads_ns, mock_get_event_url, mock_get_category_item, mock_promote, mock_sleep, mock_j_dumps, mock_driver, mock_group_data, mock_item_data, monkeypatch):
    """Checks that groups with non-matching categories are skipped."""
    monkeypatch.setattr('src.endpoints.advertisement.facebook.promoter.get_filenames', lambda x: ["group1.json"])
    mock_group_data.group_categories = ['other']
    mock_j_loads_ns.return_value = {'https://www.facebook.com/groups/12345': mock_group_data}
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    promoter.process_groups(campaign_name='test_campaign', group_file_paths=["group1.json"], group_categories_to_adv=['sales'])
    mock_j_loads_ns.assert_called_once()
    mock_get_event_url.assert_not_called()
    mock_get_category_item.assert_not_called()
    mock_promote.assert_not_called()
    mock_sleep.assert_not_called()
    mock_j_dumps.assert_not_called()
    mock_logger.debug.assert_called()

@patch('src.endpoints.advertisement.facebook.promoter.j_dumps')
@patch('src.endpoints.advertisement.facebook.promoter.time.sleep')
@patch('src.endpoints.advertisement.facebook.promoter.FacebookPromoter.promote')
@patch('src.endpoints.advertisement.facebook.promoter.FacebookPromoter.get_category_item')
@patch('src.endpoints.advertisement.facebook.promoter.get_event_url')
@patch('src.endpoints.advertisement.facebook.promoter.j_loads_ns')
@patch('src.endpoints.advertisement.facebook.promoter.logger')
def test_process_groups_skip_if_already_promoted(mock_logger, mock_j_loads_ns, mock_get_event_url, mock_get_category_item, mock_promote, mock_sleep, mock_j_dumps, mock_driver, mock_group_data, mock_item_data, monkeypatch):
    """Checks that groups are skipped if the item has already been promoted."""
    monkeypatch.setattr('src.endpoints.advertisement.facebook.promoter.get_filenames', lambda x: ["group1.json"])
    mock_group_data.promoted_categories = ['Test Category']
    mock_j_loads_ns.return_value = {'https://www.facebook.com/groups/12345': mock_group_data}
    mock_get_category_item.return_value = mock_item_data
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    promoter.process_groups(campaign_name='test_campaign', group_file_paths=["group1.json"])
    mock_j_loads_ns.assert_called_once()
    mock_get_event_url.assert_not_called()
    mock_get_category_item.assert_called_once()
    mock_promote.assert_not_called()
    mock_sleep.assert_not_called()
    mock_j_dumps.assert_not_called()
    mock_logger.debug.assert_called()

@patch('src.endpoints.advertisement.facebook.promoter.j_dumps')
@patch('src.endpoints.advertisement.facebook.promoter.time.sleep')
@patch('src.endpoints.advertisement.facebook.promoter.FacebookPromoter.promote')
@patch('src.endpoints.advertisement.facebook.promoter.FacebookPromoter.get_category_item')
@patch('src.endpoints.advertisement.facebook.promoter.get_event_url')
@patch('src.endpoints.advertisement.facebook.promoter.j_loads_ns')
@patch('src.endpoints.advertisement.facebook.promoter.logger')
def test_process_groups_skip_if_already_promoted_event(mock_logger, mock_j_loads_ns, mock_get_event_url, mock_get_category_item, mock_promote, mock_sleep, mock_j_dumps, mock_driver, mock_group_data, mock_event_item_data, monkeypatch):
    """Checks that groups are skipped if the event has already been promoted."""
    monkeypatch.setattr('src.endpoints.advertisement.facebook.promoter.get_filenames', lambda x: ["group1.json"])
    mock_group_data.promoted_events = ['Test Event']
    mock_j_loads_ns.return_value = {'https://www.facebook.com/groups/12345': mock_group_data}
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    promoter.process_groups(events=[mock_event_item_data], is_event=True, group_file_paths=["group1.json"])
    mock_j_loads_ns.assert_called_once()
    mock_get_event_url.assert_called_once()
    mock_get_category_item.assert_not_called()
    mock_promote.assert_not_called()
    mock_sleep.assert_not_called()
    mock_j_dumps.assert_not_called()
    mock_logger.debug.assert_called()

@patch('src.endpoints.advertisement.facebook.promoter.j_dumps')
@patch('src.endpoints.advertisement.facebook.promoter.time.sleep')
@patch('src.endpoints.advertisement.facebook.promoter.FacebookPromoter.promote')
@patch('src.endpoints.advertisement.facebook.promoter.FacebookPromoter.get_category_item')
@patch('src.endpoints.advertisement.facebook.promoter.get_event_url')
@patch('src.endpoints.advertisement.facebook.promoter.j_loads_ns')
@patch('src.endpoints.advertisement.facebook.promoter.logger')
def test_process_groups_skip_language_currency_mismatch(mock_logger, mock_j_loads_ns, mock_get_event_url, mock_get_category_item, mock_promote, mock_sleep, mock_j_dumps, mock_driver, mock_group_data, mock_item_data, monkeypatch):
    """Checks that groups are skipped if the language does not match."""
    monkeypatch.setattr('src.endpoints.advertisement.facebook.promoter.get_filenames', lambda x: ["group1.json"])
    mock_j_loads_ns.return_value = {'https://www.facebook.com/groups/12345': mock_group_data}
    mock_group_data.language = 'fr'
    mock_group_data.currency = 'EUR'
    promoter = FacebookPromoter(d=mock_driver, promoter='test_promoter')
    promoter.process_groups(campaign_name='test_campaign', group_file_paths=["group1.json"], language='en', currency='USD')
    mock_j_loads_ns.assert_called_once()
    mock_get_event_url.assert_not_called()
    mock_get_category_item.assert_not_called()
    mock_promote.assert_not_called()
    mock_sleep.assert_not_called()
    mock_j_dumps.assert_not_called()
    mock_logger.debug.assert_called()

# Tests for FacebookPromoter.get_category_item
@patch