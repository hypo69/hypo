```python
import pytest
import re
import shutil
from pathlib import Path
from typing import List, Optional, Union
from types import SimpleNamespace
from unittest.mock import patch

from src import gs
from src.suppliers.aliexpress.scenarios.campaigns import AliPromoCampaign
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids
from src.suppliers.aliexpress.utils.set_full_https import ensure_https
from src.utils.jjson import j_loads_ns, j_loads
from src.utils.convertors import list2string, csv2dict
from src.utils.printer import pprint
from src.utils.jjson import j_dumps, j_loads, j_loads_ns
from utils.interface import read_text_file, get_filenames
from src.logger.logger import logger

# Assuming the AliCampaignEditor class is defined as per the provided code
class AliCampaignEditor(AliPromoCampaign):
    """ Редактор реклманой камапнии """
    def __init__(self, campaign_name: str, category_name: str, language: str = 'EN', currency: str = 'USD'):
        """"""
        super().__init__(campaign_name, category_name, language, currency)


@pytest.fixture
def mock_ali_promo_campaign():
    """Mocks the AliPromoCampaign class to isolate the AliCampaignEditor."""
    with patch('src.suppliers.aliexpress.scenarios.campaigns.AliPromoCampaign.__init__', return_value=None) as mock:
        yield mock

def test_ali_campaign_editor_init_valid_input(mock_ali_promo_campaign):
    """
    Test case to check if AliCampaignEditor initializes correctly with valid inputs.
    Verifies that the super class constructor is called with the same arguments.
    """
    campaign_name = "test_campaign"
    category_name = "test_category"
    language = "RU"
    currency = "EUR"
    
    editor = AliCampaignEditor(campaign_name, category_name, language, currency)
    
    mock_ali_promo_campaign.assert_called_once_with(campaign_name, category_name, language, currency)


def test_ali_campaign_editor_init_default_language_and_currency(mock_ali_promo_campaign):
    """
    Test case to check if AliCampaignEditor initializes correctly with default language and currency.
    Verifies that the super class constructor is called with the default values for language and currency.
    """
    campaign_name = "default_campaign"
    category_name = "default_category"
    
    editor = AliCampaignEditor(campaign_name, category_name)
    
    mock_ali_promo_campaign.assert_called_once_with(campaign_name, category_name, 'EN', 'USD')


def test_ali_campaign_editor_init_empty_campaign_name(mock_ali_promo_campaign):
    """
    Test case to check behavior with an empty campaign name.
    Verifies that the initialization still works and calls the parent constructor.
    """
    campaign_name = ""
    category_name = "test_category"
    editor = AliCampaignEditor(campaign_name, category_name)
    mock_ali_promo_campaign.assert_called_once_with(campaign_name, category_name, 'EN', 'USD')

def test_ali_campaign_editor_init_empty_category_name(mock_ali_promo_campaign):
    """
    Test case to check behavior with an empty category name.
    Verifies that the initialization still works and calls the parent constructor.
    """
    campaign_name = "test_campaign"
    category_name = ""
    editor = AliCampaignEditor(campaign_name, category_name)
    mock_ali_promo_campaign.assert_called_once_with(campaign_name, category_name, 'EN', 'USD')
```