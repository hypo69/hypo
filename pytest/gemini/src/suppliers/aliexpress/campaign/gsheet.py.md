```python
import pytest
from unittest.mock import MagicMock, patch
from types import SimpleNamespace
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet
from gspread.worksheet import Worksheet
from src.goog.spreadsheet.spreadsheet import SpreadSheet
from src.logger.logger import logger


@pytest.fixture
def mock_spreadsheet():
    """Provides a mock SpreadSheet object."""
    mock_spreadsheet = MagicMock(spec=SpreadSheet)
    mock_worksheet = MagicMock(spec=Worksheet)
    mock_worksheet.id = 1
    mock_worksheet.title = 'test_sheet'
    mock_spreadsheet.worksheets.return_value = [mock_worksheet]
    mock_spreadsheet.get_worksheet.return_value = mock_worksheet
    mock_spreadsheet.copy_worksheet.return_value = mock_worksheet
    return mock_spreadsheet


@pytest.fixture
def mock_ali_campaign_gsheet(mock_spreadsheet):
    """Provides an instance of AliCampaignGoogleSheet with a mock SpreadSheet."""
    with patch('src.suppliers.aliexpress.campaign.gsheet.SpreadSheet', return_value=mock_spreadsheet):
        return AliCampaignGoogleSheet(campaign_name='test_campaign', language='en', currency='USD')

@pytest.fixture
def sample_campaign_data():
    """Provides a sample campaign SimpleNamespace object."""
    return SimpleNamespace(
        campaign_name='Test Campaign',
        title='Test Title',
        language='en',
        currency='USD',
        description='Test Description'
    )

@pytest.fixture
def sample_categories_data():
    """Provides a sample categories SimpleNamespace object."""
    return SimpleNamespace(
        category1 = SimpleNamespace(
            name = 'category1',
            title = 'Category 1',
            description = 'Description 1',
            tags = ['tag1', 'tag2'],
            products_count = 10
        ),
        category2 = SimpleNamespace(
            name = 'category2',
            title = 'Category 2',
            description = 'Description 2',
            tags = ['tag3', 'tag4'],
            products_count = 20
        )
    )

@pytest.fixture
def sample_products_data():
    """Provides a sample products list of SimpleNamespace objects."""
    return [
        SimpleNamespace(
            product_id='123',
            app_sale_price='10.0',
            original_price='20.0',
            sale_price='15.0',
            discount='5.0',
            product_main_image_url='url1',
            local_image_path='local1',
            product_small_image_urls=['small_url1', 'small_url2'],
            product_video_url='video1',
            local_video_path='local_video1',
            first_level_category_id='cat1',
            first_level_category_name='Category 1',
            second_level_category_id='subcat1',
            second_level_category_name='Sub Category 1',
            target_sale_price='12.0',
            target_sale_price_currency='USD',
            target_app_sale_price_currency='USD',
            target_original_price_currency='USD',
            original_price_currency='USD',
            product_title='Test Product 1',
            evaluate_rate='4.5',
            promotion_link='promo1',
            shop_url='shop1',
            shop_id='shop_id_1',
            tags=['tagA', 'tagB']
        ),
        SimpleNamespace(
            product_id='456',
            app_sale_price='20.0',
            original_price='30.0',
            sale_price='25.0',
            discount='5.0',
            product_main_image_url='url2',
            local_image_path='local2',
            product_small_image_urls=['small_url3', 'small_url4'],
            product_video_url='video2',
            local_video_path='local_video2',
            first_level_category_id='cat2',
            first_level_category_name='Category 2',
            second_level_category_id='subcat2',
            second_level_category_name='Sub Category 2',
            target_sale_price='22.0',
            target_sale_price_currency='EUR',
            target_app_sale_price_currency='EUR',
            target_original_price_currency='EUR',
            original_price_currency='EUR',
            product_title='Test Product 2',
            evaluate_rate='4.8',
            promotion_link='promo2',
            shop_url='shop2',
            shop_id='shop_id_2',
            tags=['tagC', 'tagD']
        )
    ]
@pytest.fixture
def mock_campaign_editor(sample_categories_data, sample_products_data):
    """Provides mock campaign editor with category and products data"""
    mock_editor = MagicMock()
    mock_editor.campaign = MagicMock()
    mock_editor.campaign.category = sample_categories_data
    mock_editor.campaign.category.category1.products = sample_products_data
    mock_editor.campaign.category.category2.products = sample_products_data

    return mock_editor



def test_ali_campaign_gsheet_init(mock_spreadsheet):
    """Test initialization of AliCampaignGoogleSheet."""
    with patch('src.suppliers.aliexpress.campaign.gsheet.SpreadSheet', return_value=mock_spreadsheet):
        ali_gsheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='en', currency='USD')
        assert ali_gsheet.spreadsheet_id == '1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0'
        assert ali_gsheet.spreadsheet == mock_spreadsheet

def test_clear_success(mock_ali_campaign_gsheet, mock_spreadsheet):
    """Test successful clearing of worksheets."""
    mock_worksheet = MagicMock()
    mock_worksheet.title = 'test_sheet'
    mock_spreadsheet.worksheets.return_value = [mock_worksheet]
    mock_ali_campaign_gsheet.clear()
    mock_spreadsheet.del_worksheet_by_id.assert_called()

def test_clear_exception(mock_ali_campaign_gsheet, mock_spreadsheet):
    """Test exception during clear operation."""
    mock_spreadsheet.worksheets.side_effect = Exception("Test Exception")
    with pytest.raises(Exception):
        mock_ali_campaign_gsheet.clear()
    logger.error.assert_called()

def test_delete_products_worksheets_success(mock_ali_campaign_gsheet, mock_spreadsheet):
    """Test successful deletion of product worksheets."""
    mock_worksheet1 = MagicMock()
    mock_worksheet1.title = 'test_sheet1'
    mock_worksheet1.id = 1
    mock_worksheet2 = MagicMock()
    mock_worksheet2.title = 'categories'
    mock_worksheet2.id = 2

    mock_spreadsheet.worksheets.return_value = [mock_worksheet1, mock_worksheet2]
    mock_ali_campaign_gsheet.delete_products_worksheets()
    mock_spreadsheet.del_worksheet_by_id.assert_called_once_with(1)

def test_delete_products_worksheets_exception(mock_ali_campaign_gsheet, mock_spreadsheet):
    """Test exception during deletion of product worksheets."""
    mock_spreadsheet.worksheets.side_effect = Exception("Test Exception")
    with pytest.raises(Exception):
        mock_ali_campaign_gsheet.delete_products_worksheets()
    logger.error.assert_called()


def test_set_campaign_worksheet_success(mock_ali_campaign_gsheet, mock_spreadsheet, sample_campaign_data):
    """Test successful writing of campaign data to worksheet."""
    mock_worksheet = MagicMock()
    mock_spreadsheet.get_worksheet.return_value = mock_worksheet
    mock_ali_campaign_gsheet.set_campaign_worksheet(sample_campaign_data)
    mock_worksheet.batch_update.assert_called()


def test_set_campaign_worksheet_exception(mock_ali_campaign_gsheet, mock_spreadsheet, sample_campaign_data):
    """Test exception during writing of campaign data to worksheet."""
    mock_spreadsheet.get_worksheet.side_effect = Exception("Test Exception")
    with pytest.raises(Exception):
        mock_ali_campaign_gsheet.set_campaign_worksheet(sample_campaign_data)
    logger.error.assert_called()


def test_set_products_worksheet_with_category_success(mock_ali_campaign_gsheet, mock_spreadsheet, sample_products_data, mock_campaign_editor):
    """Test successful setting of products data to worksheet with valid category."""
    mock_ali_campaign_gsheet.editor = mock_campaign_editor
    mock_worksheet = MagicMock()
    mock_spreadsheet.copy_worksheet.return_value = mock_worksheet
    mock_ali_campaign_gsheet.set_products_worksheet('category1')
    mock_worksheet.update.assert_called()

def test_set_products_worksheet_with_no_category(mock_ali_campaign_gsheet, mock_spreadsheet, mock_campaign_editor):
    """Test setting products worksheet when no products are found for category."""
    mock_ali_campaign_gsheet.editor = mock_campaign_editor
    mock_ali_campaign_gsheet.set_products_worksheet(None)
    logger.warning.assert_called()


def test_set_products_worksheet_exception(mock_ali_campaign_gsheet, mock_spreadsheet, sample_products_data, mock_campaign_editor):
    """Test exception during setting of products data to worksheet."""
    mock_ali_campaign_gsheet.editor = mock_campaign_editor
    mock_spreadsheet.copy_worksheet.side_effect = Exception("Test Exception")
    with pytest.raises(Exception):
        mock_ali_campaign_gsheet.set_products_worksheet('category1')
    logger.error.assert_called()



def test_set_categories_worksheet_success(mock_ali_campaign_gsheet, mock_spreadsheet, sample_categories_data):
    """Test successful writing of categories data to worksheet."""
    mock_worksheet = MagicMock()
    mock_spreadsheet.get_worksheet.return_value = mock_worksheet
    mock_ali_campaign_gsheet.set_categories_worksheet(sample_categories_data)
    mock_worksheet.update.assert_called()

def test_set_categories_worksheet_missing_attributes(mock_ali_campaign_gsheet, mock_spreadsheet):
    """Test handling of category objects with missing attributes."""
    mock_worksheet = MagicMock()
    mock_spreadsheet.get_worksheet.return_value = mock_worksheet
    categories_data = SimpleNamespace(
        category1 = SimpleNamespace(
            name = 'category1',
            title = 'Category 1',
            description = 'Description 1',
        ),
    )
    mock_ali_campaign_gsheet.set_categories_worksheet(categories_data)
    logger.warning.assert_called()

def test_set_categories_worksheet_exception(mock_ali_campaign_gsheet, mock_spreadsheet, sample_categories_data):
    """Test exception during writing of categories data to worksheet."""
    mock_spreadsheet.get_worksheet.side_effect = Exception("Test Exception")
    with pytest.raises(Exception):
         mock_ali_campaign_gsheet.set_categories_worksheet(sample_categories_data)
    logger.error.assert_called()

def test_get_categories_success(mock_ali_campaign_gsheet, mock_spreadsheet):
    """Test successful retrieval of categories data from worksheet."""
    mock_worksheet = MagicMock()
    mock_worksheet.get_all_records.return_value = [{"Name": "Category 1"}]
    mock_spreadsheet.get_worksheet.return_value = mock_worksheet
    data = mock_ali_campaign_gsheet.get_categories()
    assert data == [{"Name": "Category 1"}]
    mock_worksheet.get_all_records.assert_called()


def test_set_category_products_success(mock_ali_campaign_gsheet, mock_spreadsheet, sample_products_data, mock_campaign_editor):
    """Test successful setting of category products data to worksheet."""
    mock_ali_campaign_gsheet.editor = mock_campaign_editor
    mock_worksheet = MagicMock()
    mock_spreadsheet.copy_worksheet.return_value = mock_worksheet
    mock_ali_campaign_gsheet.set_category_products('category1', [product.__dict__ for product in sample_products_data])
    mock_worksheet.update.assert_called()

def test_set_category_products_no_category(mock_ali_campaign_gsheet, mock_spreadsheet, sample_products_data, mock_campaign_editor):
    """Test setting category products when no products are found for category."""
    mock_ali_campaign_gsheet.editor = mock_campaign_editor
    mock_ali_campaign_gsheet.set_category_products(None, [product.__dict__ for product in sample_products_data])
    logger.warning.assert_called()

def test_set_category_products_exception(mock_ali_campaign_gsheet, mock_spreadsheet, sample_products_data, mock_campaign_editor):
    """Test exception during setting of category products data to worksheet."""
    mock_ali_campaign_gsheet.editor = mock_campaign_editor
    mock_spreadsheet.copy_worksheet.side_effect = Exception("Test Exception")
    with pytest.raises(Exception):
        mock_ali_campaign_gsheet.set_category_products('category1', [product.__dict__ for product in sample_products_data])
    logger.error.assert_called()


def test_format_categories_worksheet_success(mock_ali_campaign_gsheet, mock_spreadsheet):
    """Test successful formatting of the categories worksheet."""
    mock_worksheet = MagicMock()
    mock_spreadsheet.get_worksheet.return_value = mock_worksheet
    with patch('src.suppliers.aliexpress.campaign.gsheet.set_column_width') as mock_set_column_width, \
         patch('src.suppliers.aliexpress.campaign.gsheet.set_row_height') as mock_set_row_height, \
         patch('src.suppliers.aliexpress.campaign.gsheet.format_cell_range') as mock_format_cell_range:
        mock_ali_campaign_gsheet._format_categories_worksheet(mock_worksheet)
        mock_set_column_width.assert_called()
        mock_set_row_height.assert_called()
        mock_format_cell_range.assert_called()

def test_format_categories_worksheet_exception(mock_ali_campaign_gsheet, mock_spreadsheet):
    """Test exception during formatting of the categories worksheet."""
    mock_worksheet = MagicMock()
    mock_spreadsheet.get_worksheet.return_value = mock_worksheet
    with patch('src.suppliers.aliexpress.campaign.gsheet.set_column_width', side_effect=Exception("Test Exception")):
        with pytest.raises(Exception):
            mock_ali_campaign_gsheet._format_categories_worksheet(mock_worksheet)
    logger.error.assert_called()


def test_format_category_products_worksheet_success(mock_ali_campaign_gsheet, mock_spreadsheet):
    """Test successful formatting of the category products worksheet."""
    mock_worksheet = MagicMock()
    mock_spreadsheet.get_worksheet.return_value = mock_worksheet
    with patch('src.suppliers.aliexpress.campaign.gsheet.set_column_width') as mock_set_column_width, \
         patch('src.suppliers.aliexpress.campaign.gsheet.set_row_height') as mock_set_row_height, \
         patch('src.suppliers.aliexpress.campaign.gsheet.format_cell_range') as mock_format_cell_range:
        mock_ali_campaign_gsheet._format_category_products_worksheet(mock_worksheet)
        mock_set_column_width.assert_called()
        mock_set_row_height.assert_called()
        mock_format_cell_range.assert_called()

def test_format_category_products_worksheet_exception(mock_ali_campaign_gsheet, mock_spreadsheet):
    """Test exception during formatting of the category products worksheet."""
    mock_worksheet = MagicMock()
    mock_spreadsheet.get_worksheet.return_value = mock_worksheet
    with patch('src.suppliers.aliexpress.campaign.gsheet.set_column_width', side_effect=Exception("Test Exception")):
        with pytest.raises(Exception):
            mock_ali_campaign_gsheet._format_category_products_worksheet(mock_worksheet)
    logger.error.assert_called()
```