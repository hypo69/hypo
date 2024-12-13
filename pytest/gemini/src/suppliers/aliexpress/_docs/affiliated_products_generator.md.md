```python
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from types import SimpleNamespace
import asyncio
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
from src.utils.jjson import j_dumps
from src.utils.file import read_text_file, save_text_file


@pytest.fixture
def mock_ali_api():
    """Mocks the AliApi class and its methods."""
    with patch('src.suppliers.aliexpress.affiliated_products_generator.AliApi', autospec=True) as MockAliApi:
        mock_api = MockAliApi.return_value
        mock_api.get_affiliate_links.return_value = [SimpleNamespace(promotion_link="https://example.com/affiliate_link")]
        mock_api.retrieve_product_details.return_value = [SimpleNamespace(product_id='123', product_main_image_url='http://example.com/image.png', product_video_url='http://example.com/video.mp4', promotion_link=None)]
        yield mock_api
        
@pytest.fixture
def mock_save_png():
    """Mocks the save_png_from_url function."""
    with patch('src.suppliers.aliexpress.affiliated_products_generator.save_png_from_url', autospec=True) as mock:
        yield mock

@pytest.fixture
def mock_save_video():
    """Mocks the save_video_from_url function."""
    with patch('src.suppliers.aliexpress.affiliated_products_generator.save_video_from_url', autospec=True) as mock:
        yield mock

@pytest.fixture
def mock_pprint():
    """Mocks the pprint function."""
    with patch('src.suppliers.aliexpress.affiliated_products_generator.pprint', autospec=True) as mock:
        yield mock
        
@pytest.fixture
def mock_j_dumps():
    """Mocks the j_dumps function."""
    with patch('src.suppliers.aliexpress.affiliated_products_generator.j_dumps', autospec=True) as mock:
        mock.return_value = True
        yield mock

@pytest.fixture
def mock_logger():
    """Mocks the logger."""
    with patch('src.suppliers.aliexpress.affiliated_products_generator.logger', autospec=True) as mock:
        yield mock
        
@pytest.fixture
def mock_extract_prod_ids():
    """Mocks the extract_prod_ids function."""
    with patch('src.suppliers.aliexpress.affiliated_products_generator.extract_prod_ids', autospec=True) as mock:
        mock.return_value = '123'
        yield mock


@pytest.fixture
def mock_urlparse():
     """Mocks the urlparse function."""
     with patch('src.suppliers.aliexpress.affiliated_products_generator.urlparse', autospec=True) as mock:
        mock.return_value =  MagicMock(query='aff_short_key=short_key', path='/test.mp4')
        yield mock


@pytest.fixture
def mock_parse_qs():
    """Mocks the parse_qs function."""
    with patch('src.suppliers.aliexpress.affiliated_products_generator.parse_qs', autospec=True) as mock:
        mock.return_value = {'aff_short_key': ['short_key']}
        yield mock
        
@pytest.fixture
def mock_read_text_file():
    """Mocks the read_text_file function."""
    with patch('src.suppliers.aliexpress.affiliated_products_generator.read_text_file', autospec=True) as mock:
        mock.return_value = ['123','456']
        yield mock

@pytest.fixture
def mock_save_text_file():
    """Mocks the save_text_file function."""
    with patch('src.suppliers.aliexpress.affiliated_products_generator.save_text_file', autospec=True) as mock:
        yield mock

@pytest.fixture
def mock_path_rename():
    """Mocks the path.rename function."""
    with patch('pathlib.Path.rename', autospec=True) as mock:
        yield mock


def test_process_affiliate_products_valid_input(mock_ali_api, mock_save_png, mock_save_video, mock_pprint, mock_j_dumps,mock_logger, mock_urlparse, mock_parse_qs):
    """
    Test the successful processing of affiliate products with valid input.
    It checks if the affiliate links, images, and videos are processed correctly.
    """
    
    parser = AliAffiliatedProducts(campaign_name='test_campaign', campaign_category='test_category')
    prod_urls = ["http://example.com/123.html"]
    
    products = parser.process_affiliate_products(prod_urls)

    assert products is not None
    assert len(products) == 1
    assert products[0].product_id == '123'
    assert products[0].local_saved_image == str(parser.campaign_path / 'images' / '123.png')
    assert products[0].local_saved_video == str(parser.campaign_path / 'videos' / '123.mp4')
    assert products[0].promotion_link == 'https://s.click.aliexpress.com/e/short_key'

    mock_ali_api.get_affiliate_links.assert_called_once()
    mock_ali_api.retrieve_product_details.assert_called_once()
    mock_save_png.assert_called_once()
    mock_save_video.assert_called_once()
    mock_j_dumps.assert_called_once()
    mock_logger.error.assert_not_called()


def test_process_affiliate_products_no_affiliate_links(mock_ali_api, mock_logger, mock_pprint):
    """
    Test the scenario where no affiliate links are found for the given product URLs.
    It should log an error and return None.
    """
    mock_ali_api.get_affiliate_links.return_value = []
    parser = AliAffiliatedProducts(campaign_name='test_campaign', campaign_category='test_category')
    prod_urls = ["http://example.com/123.html"]
    
    products = parser.process_affiliate_products(prod_urls)
    
    assert products is None
    mock_ali_api.get_affiliate_links.assert_called_once()
    mock_logger.error.assert_called_once_with('No affiliate products returned')
    mock_logger.info_red.assert_not_called()
    mock_pprint.assert_not_called()
    
def test_process_affiliate_products_no_products_returned(mock_ali_api, mock_logger,mock_pprint):
    """
    Test the case where product details retrieval returns None.
     It should return None.
    """
    mock_ali_api.retrieve_product_details.return_value = None
    parser = AliAffiliatedProducts(campaign_name='test_campaign', campaign_category='test_category')
    prod_urls = ["http://example.com/123.html"]
    
    products = parser.process_affiliate_products(prod_urls)
    
    assert products is None
    mock_ali_api.get_affiliate_links.assert_called_once()
    mock_ali_api.retrieve_product_details.assert_called_once()
    mock_logger.error.assert_not_called()
    mock_pprint.assert_not_called()
    
def test_process_affiliate_products_no_aff_short_key(mock_ali_api, mock_save_png, mock_save_video, mock_pprint, mock_j_dumps, mock_logger, mock_urlparse, mock_parse_qs, mock_extract_prod_ids):
    """
     Test the scenario when no aff_short_key is present in query params.
    It verifies that the product is deleted, and no affiliate link is set.
    """
    mock_parse_qs.return_value = {}
    mock_ali_api.retrieve_product_details.return_value = [SimpleNamespace(product_id='123', product_main_image_url='http://example.com/image.png', product_video_url='http://example.com/video.mp4', promotion_link='https://s.click.aliexpress.com/e/test_aff_key')]

    parser = AliAffiliatedProducts(campaign_name='test_campaign', campaign_category='test_category')
    prod_urls = ["http://example.com/123.html"]

    products = parser.process_affiliate_products(prod_urls)
    
    mock_extract_prod_ids.assert_called_once()
    mock_logger.success.assert_not_called()
    mock_logger.error.assert_not_called()
    assert products[0].promotion_link is None
    assert mock_j_dumps.call_count == 1

def test_delete_product_from_sources_txt(mock_read_text_file, mock_save_text_file, mock_extract_prod_ids):
    """
    Test `delete_product` method when a product ID exists in `sources.txt`.
    It checks that the product is removed from the list and the file is updated.
    """
    parser = AliAffiliatedProducts(campaign_name='test_campaign', campaign_category='test_category')
    product_id = '123'
    
    parser.delete_product(product_id)
    
    mock_read_text_file.assert_called_once()
    mock_save_text_file.assert_called_once()
    mock_extract_prod_ids.assert_called()

def test_delete_product_from_sources_txt_no_id(mock_read_text_file, mock_save_text_file, mock_extract_prod_ids):
    """
    Test `delete_product` method when a product ID exists in `sources.txt`.
    It checks that the product is removed from the list and the file is updated.
    """
    mock_extract_prod_ids.return_value = None
    parser = AliAffiliatedProducts(campaign_name='test_campaign', campaign_category='test_category')
    product_id = '123'
    
    parser.delete_product(product_id)
    
    mock_read_text_file.assert_called_once()
    mock_save_text_file.assert_called_once()
    mock_extract_prod_ids.assert_called()
    
def test_delete_product_file_not_found(mock_read_text_file, mock_logger,mock_extract_prod_ids, mock_path_rename):
    """
    Test the `delete_product` method when a product file is not found.
    It should log an error.
    """
    mock_read_text_file.return_value = None
    mock_path_rename.side_effect = FileNotFoundError
    parser = AliAffiliatedProducts(campaign_name='test_campaign', campaign_category='test_category')
    product_id = '123'
    parser.delete_product(product_id)
    
    mock_logger.error.assert_called_once()
    mock_logger.success.assert_not_called()

def test_delete_product_exception(mock_read_text_file, mock_logger, mock_extract_prod_ids, mock_path_rename):
    """
    Test `delete_product` method when an exception occurs during file deletion.
    It should log a critical error.
    """
    mock_read_text_file.return_value = None
    mock_path_rename.side_effect = Exception("Test Exception")
    parser = AliAffiliatedProducts(campaign_name='test_campaign', campaign_category='test_category')
    product_id = '123'
    parser.delete_product(product_id)
    
    mock_logger.critical.assert_called_once()
    mock_logger.success.assert_not_called()

def test_delete_product_file_success(mock_read_text_file, mock_logger,mock_extract_prod_ids, mock_path_rename):
    """
    Test `delete_product` method when a product file is successfully renamed.
    It should log success message.
    """
    mock_read_text_file.return_value = None
    parser = AliAffiliatedProducts(campaign_name='test_campaign', campaign_category='test_category')
    product_id = '123'
    
    parser.delete_product(product_id)
    
    mock_logger.success.assert_called_once()
    mock_logger.critical.assert_not_called()
    mock_logger.error.assert_not_called()
```