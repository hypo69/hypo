```python
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
import json
from types import SimpleNamespace
from src.suppliers.aliexpress.aliapi import AliApi
from src.db.manager_categories import CategoryManager
from src.db.manager_coupons_and_sales import ProductCampaignsManager
from src.utils.jjson import j_loads_ns
from src import gs


# Mock gs.credentials.aliexpress for testing
@pytest.fixture
def mock_gs_credentials():
    with patch('src.suppliers.aliexpress.aliapi.gs.credentials') as mock_credentials:
        mock_credentials.aliexpress = SimpleNamespace(
            api_key='test_api_key',
            secret='test_secret',
            tracking_id='test_tracking_id'
        )
        yield mock_credentials

# Mock the base class AliexpressApi
@pytest.fixture
def mock_aliexpress_api():
    with patch('src.suppliers.aliexpress.aliapi.AliexpressApi') as mock_api:
        yield mock_api


# Fixture for creating AliApi instance with mocked credentials
@pytest.fixture
def ali_api_instance(mock_gs_credentials):
    return AliApi()


def test_aliapi_init(mock_gs_credentials):
    """
    Test the initialization of AliApi class.
    Verifies that the base class constructor is called with correct arguments,
    and that database managers are not initialized (removed in the provided code).
    """
    
    api = AliApi()
    mock_gs_credentials.assert_called
    assert api.api_key == 'test_api_key'
    assert api.secret == 'test_secret'
    assert api.language == 'en'
    assert api.currency == 'usd'
    assert api.tracking_id == 'test_tracking_id'
    assert api.manager_categories == None
    assert api.manager_campaigns == None

def test_retrieve_product_details_as_dict_valid_input(ali_api_instance, mock_aliexpress_api):
    """
    Test retrieve_product_details_as_dict with valid product IDs.
    Verifies that the method converts SimpleNamespace objects to dictionaries correctly.
    """
    mock_api = mock_aliexpress_api.return_value
    mock_api.retrieve_product_details.return_value = [
         SimpleNamespace(a=1, b=2),
         SimpleNamespace(c=3, d=4)
    ]
    
    product_ids = [123, 456]
    result = ali_api_instance.retrieve_product_details_as_dict(product_ids)
    
    mock_api.retrieve_product_details.assert_called_with(product_ids)
    assert result == [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]


def test_retrieve_product_details_as_dict_empty_list(ali_api_instance, mock_aliexpress_api):
    """
    Test retrieve_product_details_as_dict with an empty list of product IDs.
    Verifies the behavior when an empty list of ids is passed.
    """
    mock_api = mock_aliexpress_api.return_value
    mock_api.retrieve_product_details.return_value = []
    
    product_ids = []
    result = ali_api_instance.retrieve_product_details_as_dict(product_ids)
    
    mock_api.retrieve_product_details.assert_called_with(product_ids)
    assert result == []


def test_get_affiliate_links_valid_input(ali_api_instance, mock_aliexpress_api):
    """
    Test get_affiliate_links with valid inputs.
    Verifies that the method correctly calls the base class method and returns the expected result.
    """
    mock_api = mock_aliexpress_api.return_value
    mock_api.get_affiliate_links.return_value = [SimpleNamespace(link='test_link')]
    
    links = ['test_url_1', 'test_url_2']
    link_type = 1
    result = ali_api_instance.get_affiliate_links(links, link_type)
    
    mock_api.get_affiliate_links.assert_called_with(links, link_type, **{})
    assert result == [SimpleNamespace(link='test_link')]


def test_get_affiliate_links_with_str_input(ali_api_instance, mock_aliexpress_api):
    """
    Test get_affiliate_links with a string input for links.
    Verifies that the method correctly calls the base class method with the string and returns the expected result.
    """
    mock_api = mock_aliexpress_api.return_value
    mock_api.get_affiliate_links.return_value = [SimpleNamespace(link='test_link')]
    
    links = 'test_url'
    link_type = 0
    result = ali_api_instance.get_affiliate_links(links, link_type)
    
    mock_api.get_affiliate_links.assert_called_with(links, link_type, **{})
    assert result == [SimpleNamespace(link='test_link')]


def test_get_affiliate_links_kwargs(ali_api_instance, mock_aliexpress_api):
    """
    Test get_affiliate_links with kwargs.
    Verifies that kwargs are correctly passed to the base class method.
    """
    mock_api = mock_aliexpress_api.return_value
    mock_api.get_affiliate_links.return_value = [SimpleNamespace(link='test_link')]
    
    links = ['test_url_1', 'test_url_2']
    link_type = 1
    kwargs = {'param1': 'value1', 'param2': 'value2'}
    result = ali_api_instance.get_affiliate_links(links, link_type, **kwargs)
    
    mock_api.get_affiliate_links.assert_called_with(links, link_type, **kwargs)
    assert result == [SimpleNamespace(link='test_link')]
```