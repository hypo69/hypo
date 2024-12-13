```python
import pytest
from pathlib import Path
from unittest.mock import patch, mock_open
from src.suppliers.aliexpress.campaign.prepare_campaigns import (
    process_campaign_category,
    process_campaign,
    process_all_campaigns,
    main_process,
    main,
    AliCampaignEditor,
    campaigns_directory,
    locales
)
from src import gs
import argparse
import logging


# Mocking logger for tests
logger = logging.getLogger()
logger.setLevel(logging.INFO)


@pytest.fixture
def mock_ali_campaign_editor():
    """Mocks AliCampaignEditor for tests."""
    with patch("src.suppliers.aliexpress.campaign.prepare_campaigns.AliCampaignEditor") as mock:
        yield mock
        

@pytest.fixture
def mock_get_directory_names():
    """Mocks get_directory_names for tests."""
    with patch("src.suppliers.aliexpress.campaign.prepare_campaigns.get_directory_names") as mock:
        yield mock


@pytest.fixture
def mock_pprint():
    """Mocks pprint for tests."""
    with patch("src.suppliers.aliexpress.campaign.prepare_campaigns.pprint") as mock:
        yield mock
        

@pytest.fixture
def mock_logger_info():
    """Mocks logger.info for tests."""
    with patch("src.suppliers.aliexpress.campaign.prepare_campaigns.logger.info") as mock:
        yield mock
        

@pytest.fixture
def mock_argparse(monkeypatch):
    """Mocks argparse for testing command-line arguments."""
    def mock_parse_args(args=None, namespace=None):
        # Default values
        class Args:
            campaign_name = 'test_campaign'
            categories = None
            language = None
            currency = None
            all = False

        if args is not None:
            for i, arg in enumerate(args):
                if arg == 'test_campaign':
                   Args.campaign_name = arg
                elif arg == '--all':
                    Args.all = True
                elif arg == '-c':
                    Args.categories = args[i+1:]
                elif arg == '-l':
                   Args.language = args[i+1]
                elif arg == '-cu':
                    Args.currency = args[i+1]


        return Args()

    monkeypatch.setattr(argparse.ArgumentParser, 'parse_args', mock_parse_args)
    yield


def test_process_campaign_category_valid_input(mock_ali_campaign_editor):
    """Checks process_campaign_category with valid input."""
    mock_editor = mock_ali_campaign_editor.return_value
    mock_editor.process_campaign_category.return_value = ["Product 1", "Product 2"]
    titles = process_campaign_category("summer_sale", "electronics", "EN", "USD")
    assert titles == ["Product 1", "Product 2"]
    mock_ali_campaign_editor.assert_called_once_with(campaign_name="summer_sale", language="EN", currency="USD")
    mock_editor.process_campaign_category.assert_called_once_with("electronics")


def test_process_campaign_valid_input(mock_ali_campaign_editor, mock_logger_info):
    """Checks process_campaign with valid input."""
    mock_editor = mock_ali_campaign_editor.return_value
    result = process_campaign("summer_sale", "EN", "USD")
    assert result is True
    mock_ali_campaign_editor.assert_called_once_with(campaign_name="summer_sale", language="EN", currency="USD")
    mock_editor.process_campaign.assert_called_once()
    mock_logger_info.assert_called_once()


def test_process_campaign_all_locales(mock_ali_campaign_editor, mock_logger_info):
    """Checks process_campaign with no language and currency, using all locales."""
    mock_editor = mock_ali_campaign_editor.return_value
    result = process_campaign("summer_sale")
    assert result is True
    assert mock_ali_campaign_editor.call_count == len([lc for locale in locales for lc in locale.items()])
    mock_editor.process_campaign.call_count == len([lc for locale in locales for lc in locale.items()])
    assert mock_logger_info.call_count == len([lc for locale in locales for lc in locale.items()])


def test_process_all_campaigns_specific_locale(mock_ali_campaign_editor, mock_get_directory_names, mock_pprint, mock_logger_info):
    """Checks process_all_campaigns with a specific locale."""
    mock_get_directory_names.return_value = ["campaign1", "campaign2"]
    mock_editor = mock_ali_campaign_editor.return_value
    process_all_campaigns("EN", "USD")
    mock_get_directory_names.assert_called_once_with(campaigns_directory)
    assert mock_pprint.call_count == 2 # one for _l and one for campaigns_dir
    assert mock_ali_campaign_editor.call_count == 2
    mock_ali_campaign_editor.assert_called_with(campaign_name="campaign2", language="EN", currency="USD")
    assert mock_logger_info.call_count == 2
    mock_logger_info.assert_called_with("Start processing campaign_name='campaign2', lang='EN', curr='USD'")


def test_process_all_campaigns_all_locales(mock_ali_campaign_editor, mock_get_directory_names, mock_pprint, mock_logger_info):
    """Checks process_all_campaigns with no language or currency, processing all locales."""
    mock_get_directory_names.return_value = ["campaign1", "campaign2"]
    mock_editor = mock_ali_campaign_editor.return_value
    process_all_campaigns()
    mock_get_directory_names.assert_called_once_with(campaigns_directory)
    assert mock_pprint.call_count == 2
    assert mock_ali_campaign_editor.call_count == len([lc for locale in locales for lc in locale.items()])*2
    assert mock_logger_info.call_count == len([lc for locale in locales for lc in locale.items()])*2

def test_main_process_with_categories(mock_ali_campaign_editor, mock_logger_info):
    """Checks main_process with specific categories."""
    mock_editor = mock_ali_campaign_editor.return_value
    categories = ["electronics", "books"]
    main_process("summer_sale", categories, "EN", "USD")
    assert mock_editor.process_campaign_category.call_count == 2
    mock_logger_info.assert_called()
    assert mock_logger_info.call_count == 2


def test_main_process_no_categories(mock_ali_campaign_editor, mock_logger_info):
    """Checks main_process with no specific categories."""
    mock_editor = mock_ali_campaign_editor.return_value
    main_process("summer_sale", [], "EN", "USD")
    mock_ali_campaign_editor.assert_called_once_with(campaign_name="summer_sale", language="EN", currency="USD")
    mock_editor.process_campaign.assert_called_once()
    mock_logger_info.assert_called()
    assert mock_logger_info.call_count == 1


def test_main_process_all_locales(mock_ali_campaign_editor, mock_logger_info):
    """Checks main_process with no language or currency, processing all locales."""
    mock_editor = mock_ali_campaign_editor.return_value
    main_process("summer_sale", ["electronics"])
    assert mock_editor.process_campaign_category.call_count == len([lc for locale in locales for lc in locale.items()])
    assert mock_logger_info.call_count == len([lc for locale in locales for lc in locale.items()])
    
def test_main_process_all_locales_no_category(mock_ali_campaign_editor, mock_logger_info):
    """Checks main_process with no language or currency, processing all locales."""
    mock_editor = mock_ali_campaign_editor.return_value
    main_process("summer_sale", [])
    assert mock_editor.process_campaign.call_count == len([lc for locale in locales for lc in locale.items()])
    assert mock_logger_info.call_count == len([lc for locale in locales for lc in locale.items()])


def test_main_with_all_flag(mock_argparse, mock_ali_campaign_editor, mock_get_directory_names, mock_pprint, mock_logger_info):
    """Checks main function with --all flag."""
    mock_get_directory_names.return_value = ["campaign1"]
    mock_editor = mock_ali_campaign_editor.return_value
    main()
    mock_get_directory_names.assert_called_once_with(campaigns_directory)
    assert mock_pprint.call_count == 2
    assert mock_ali_campaign_editor.call_count == len([lc for locale in locales for lc in locale.items()])
    assert mock_logger_info.call_count == len([lc for locale in locales for lc in locale.items()])


def test_main_without_all_flag(mock_argparse, mock_ali_campaign_editor, mock_logger_info):
    """Checks main function without --all flag."""
    mock_editor = mock_ali_campaign_editor.return_value
    main()
    mock_ali_campaign_editor.assert_called_once()
    assert mock_logger_info.call_count == 1
    mock_editor.process_campaign.assert_called_once()

def test_main_with_args_language_currency(mock_argparse, mock_ali_campaign_editor, mock_logger_info):
    """Checks main function with language and currency args."""
    mock_editor = mock_ali_campaign_editor.return_value
    main()
    mock_ali_campaign_editor.assert_called_once_with(campaign_name="test_campaign", language=None, currency=None)
    assert mock_logger_info.call_count == 1
    mock_editor.process_campaign.assert_called_once()


def test_main_with_args_language_currency_all_flag(mock_argparse, mock_ali_campaign_editor, mock_get_directory_names, mock_pprint, mock_logger_info):
    """Checks main function with language and currency args."""
    mock_get_directory_names.return_value = ["campaign1"]
    mock_editor = mock_ali_campaign_editor.return_value
    main()
    mock_get_directory_names.assert_called_once_with(campaigns_directory)
    assert mock_pprint.call_count == 2
    assert mock_ali_campaign_editor.call_count == len([lc for locale in locales for lc in locale.items()])
    assert mock_logger_info.call_count == len([lc for locale in locales for lc in locale.items()])
```