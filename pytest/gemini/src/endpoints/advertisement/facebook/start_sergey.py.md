```python
import pytest
from unittest.mock import MagicMock, patch
import copy
from pathlib import Path

from src.endpoints.advertisement.facebook.start_sergey import (
    run_campaign,
    campaign_cycle,
    main,
    group_file_paths_ru,
    adv_file_paths_ru,
    group_file_paths_he,
    adv_file_paths_he,
    group_categories_to_adv
)
from src.webdriver.driver import Driver
from src.endpoints.advertisement.facebook import FacebookPromoter
from src.utils.file import get_directory_names
from src.logger.logger import logger
from src.utils.date_time import interval
from src import gs


# Mocking external dependencies
@pytest.fixture
def mock_driver():
    """Provides a mock Driver object."""
    mock = MagicMock(spec=Driver)
    return mock

@pytest.fixture
def mock_facebook_promoter():
    """Provides a mock FacebookPromoter object."""
    mock = MagicMock(spec=FacebookPromoter)
    return mock

@pytest.fixture
def mock_get_directory_names():
    """Provides a mock get_directory_names function."""
    with patch("src.endpoints.advertisement.facebook.start_sergey.get_directory_names") as mock:
        yield mock

@pytest.fixture
def mock_interval():
    """Provides a mock interval function."""
    with patch("src.endpoints.advertisement.facebook.start_sergey.interval") as mock:
        yield mock

@pytest.fixture
def mock_time_sleep():
    """Provides a mock time.sleep function."""
    with patch("src.endpoints.advertisement.facebook.start_sergey.time.sleep") as mock:
        yield mock


@patch("src.endpoints.advertisement.facebook.start_sergey.FacebookPromoter")
def test_run_campaign_valid_input(MockFacebookPromoter, mock_driver):
    """Checks correct behavior of run_campaign with valid input."""
    mock_promoter = MockFacebookPromoter.return_value
    campaigns = ["test_campaign"]
    group_file_paths = ["test_groups.json"]
    language = "RU"
    currency = "ILS"

    run_campaign(mock_driver, "test_promoter", campaigns, group_file_paths, language, currency)

    MockFacebookPromoter.assert_called_once_with(mock_driver, promoter="test_promoter")
    mock_promoter.run_campaigns.assert_called_once_with(
        campaigns=campaigns,
        group_file_paths=group_file_paths,
        group_categories_to_adv=group_categories_to_adv,
        language=language,
        currency=currency,
        no_video=False,
    )

@patch("src.endpoints.advertisement.facebook.start_sergey.FacebookPromoter")
def test_run_campaign_empty_campaigns(MockFacebookPromoter, mock_driver):
    """Checks correct behavior of run_campaign with empty campaigns list."""
    mock_promoter = MockFacebookPromoter.return_value
    campaigns = []
    group_file_paths = ["test_groups.json"]
    language = "RU"
    currency = "ILS"

    run_campaign(mock_driver, "test_promoter", campaigns, group_file_paths, language, currency)

    MockFacebookPromoter.assert_called_once_with(mock_driver, promoter="test_promoter")
    mock_promoter.run_campaigns.assert_called_once_with(
        campaigns=campaigns,
        group_file_paths=group_file_paths,
        group_categories_to_adv=group_categories_to_adv,
        language=language,
        currency=currency,
        no_video=False,
    )


@patch("src.endpoints.advertisement.facebook.start_sergey.FacebookPromoter")
def test_run_campaign_no_group_files(MockFacebookPromoter, mock_driver):
    """Checks correct behavior of run_campaign with empty group_file_paths."""
    mock_promoter = MockFacebookPromoter.return_value
    campaigns = ["test_campaign"]
    group_file_paths = []
    language = "RU"
    currency = "ILS"

    run_campaign(mock_driver, "test_promoter", campaigns, group_file_paths, language, currency)

    MockFacebookPromoter.assert_called_once_with(mock_driver, promoter="test_promoter")
    mock_promoter.run_campaigns.assert_called_once_with(
        campaigns=campaigns,
        group_file_paths=group_file_paths,
        group_categories_to_adv=group_categories_to_adv,
        language=language,
        currency=currency,
        no_video=False,
    )



def test_campaign_cycle_ru_campaigns(mock_driver, mock_get_directory_names, mock_facebook_promoter):
    """Checks correct execution of campaign_cycle with RU campaigns."""
    mock_get_directory_names.return_value = ["aliexpress_campaign"]
    
    result = campaign_cycle(mock_driver)

    assert result is True

    # Check if run_campaign was called correctly for RU language
    mock_facebook_promoter.assert_called()
    
    # Check if run_campaign was called with 'kazarinov_ru'
    mock_facebook_promoter.return_value.run_campaigns.assert_any_call(
        campaigns=['kazarinov_ru'],
        group_file_paths=group_file_paths_ru + adv_file_paths_ru,
        group_categories_to_adv=group_categories_to_adv,
        language="RU",
        currency="ILS",
        no_video=False
    )

    # Check if run_campaign was called with aliexpress campaigns
    mock_facebook_promoter.return_value.run_campaigns.assert_any_call(
       campaigns=["aliexpress_campaign"],
        group_file_paths=group_file_paths_ru + adv_file_paths_ru,
        group_categories_to_adv=group_categories_to_adv,
        language="RU",
        currency="ILS",
        no_video=False
    )

def test_campaign_cycle_he_campaigns(mock_driver, mock_get_directory_names, mock_facebook_promoter):
    """Checks correct execution of campaign_cycle with HE campaigns."""
    mock_get_directory_names.return_value = ["aliexpress_campaign"]
    
    result = campaign_cycle(mock_driver)

    assert result is True

    # Check if run_campaign was called correctly for HE language
    mock_facebook_promoter.assert_called()

    # Check if run_campaign was called with 'kazarinov_he'
    mock_facebook_promoter.return_value.run_campaigns.assert_any_call(
        campaigns=['kazarinov_he'],
        group_file_paths=group_file_paths_he + adv_file_paths_he,
        group_categories_to_adv=group_categories_to_adv,
        language="HE",
        currency="ILS",
        no_video=False
    )
    
     # Check if run_campaign was called with aliexpress campaigns
    mock_facebook_promoter.return_value.run_campaigns.assert_any_call(
       campaigns=["aliexpress_campaign"],
        group_file_paths=group_file_paths_he + adv_file_paths_he,
        group_categories_to_adv=group_categories_to_adv,
        language="HE",
        currency="ILS",
        no_video=False
    )


def test_campaign_cycle_empty_aliexpress_campaigns(mock_driver, mock_get_directory_names, mock_facebook_promoter):
    """Checks correct behavior when no aliexpress campaigns are found."""
    mock_get_directory_names.return_value = []
    
    result = campaign_cycle(mock_driver)

    assert result is True

    # Check if run_campaign was called correctly for both languages
    mock_facebook_promoter.assert_called()

     # Check if run_campaign was called with 'kazarinov_ru'
    mock_facebook_promoter.return_value.run_campaigns.assert_any_call(
        campaigns=['kazarinov_ru'],
        group_file_paths=group_file_paths_ru + adv_file_paths_ru,
        group_categories_to_adv=group_categories_to_adv,
        language="RU",
        currency="ILS",
        no_video=False
    )

     # Check if run_campaign was called with 'kazarinov_he'
    mock_facebook_promoter.return_value.run_campaigns.assert_any_call(
        campaigns=['kazarinov_he'],
        group_file_paths=group_file_paths_he + adv_file_paths_he,
        group_categories_to_adv=group_categories_to_adv,
        language="HE",
        currency="ILS",
        no_video=False
    )

    # Ensure run_campaign for aliexpress was not called since the list is empty
    mock_facebook_promoter.return_value.run_campaigns.assert_any_call(
        campaigns=[],
        group_file_paths=group_file_paths_ru + adv_file_paths_ru,
        group_categories_to_adv=group_categories_to_adv,
        language="RU",
        currency="ILS",
        no_video=False
    )

    mock_facebook_promoter.return_value.run_campaigns.assert_any_call(
        campaigns=[],
        group_file_paths=group_file_paths_he + adv_file_paths_he,
        group_categories_to_adv=group_categories_to_adv,
        language="HE",
        currency="ILS",
        no_video=False
    )

def test_main_keyboard_interrupt(mock_driver, mock_interval, mock_time_sleep):
    """Checks graceful exit on keyboard interrupt."""
    mock_driver.get_url.return_value = None
    mock_interval.return_value = False  # Simulate that interval check is not true


    with patch("src.endpoints.advertisement.facebook.start_sergey.campaign_cycle") as mock_cycle:
            with patch("src.endpoints.advertisement.facebook.start_sergey.logger.info") as mock_logger:
                mock_cycle.side_effect = KeyboardInterrupt()
                main()
                mock_logger.assert_called_with("Campaign promotion interrupted.")
    

@patch("src.endpoints.advertisement.facebook.start_sergey.Driver")
@patch("src.endpoints.advertisement.facebook.start_sergey.campaign_cycle")
def test_main_normal_execution(MockDriver, mock_cycle, mock_interval, mock_time_sleep):
    """Checks normal execution of main function."""
    mock_driver_instance = MockDriver.return_value
    mock_interval.return_value = False
    mock_time_sleep.return_value = None
    mock_cycle.return_value = True

    with patch("src.endpoints.advertisement.facebook.start_sergey.time.strftime", return_value="10:00:00") as mock_strftime:
         with patch("src.endpoints.advertisement.facebook.start_sergey.random.randint", return_value=60) as mock_randint:
            main()
            MockDriver.assert_called_once_with(Chrome)
            mock_driver_instance.get_url.assert_called_once_with("https://facebook.com")
            mock_cycle.assert_called()
            mock_time_sleep.assert_called_with(60)
            mock_strftime.assert_called()
            mock_randint.assert_called()



@patch("src.endpoints.advertisement.facebook.start_sergey.interval", return_value=True)
@patch("src.endpoints.advertisement.facebook.start_sergey.time.sleep")
@patch("src.endpoints.advertisement.facebook.start_sergey.Driver")
def test_main_interval_true(MockDriver, mock_sleep, mock_interval):
    """Checks main function when interval is true."""
    
    mock_driver = MockDriver.return_value
    
    with patch("src.endpoints.advertisement.facebook.start_sergey.print") as mock_print:
        with pytest.raises(KeyboardInterrupt):
            # Simulate KeyboardInterrupt after the first loop to prevent infinite looping
            mock_driver.get_url.side_effect = KeyboardInterrupt()
            main()
        mock_print.assert_called_with("Good night!")
        mock_sleep.assert_called_with(1000)

```