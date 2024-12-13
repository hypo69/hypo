```python
import pytest
from unittest.mock import MagicMock, patch
from types import SimpleNamespace
from src.suppliers.aliexpress.campaign.gsheets_check_this_code import AliCampaignGoogleSheet
from src.webdriver.driver import Driver
from gspread.worksheet import Worksheet
from src.goog.spreadsheet.spreadsheet import SpreadSheet
from src.suppliers.aliexpress.campaign.ali_campaign_editor import AliCampaignEditor
from src.logger.logger import logger
from gspread_formatting import cellFormat, textFormat, Color

# Fixture definitions
@pytest.fixture
def mock_spreadsheet():
    """Provides a mock SpreadSheet object."""
    mock = MagicMock(spec=SpreadSheet)
    mock.worksheets.return_value = [
        MagicMock(title='categories', id=1),
        MagicMock(title='product', id=2),
        MagicMock(title='campaign', id=3),
        MagicMock(title='test_sheet', id=4),
    ]
    mock.get_worksheet.return_value = MagicMock(spec=Worksheet)
    return mock

@pytest.fixture
def mock_ali_campaign_editor():
    """Provides a mock AliCampaignEditor object."""
    mock = MagicMock(spec=AliCampaignEditor)
    mock.campaign = SimpleNamespace(
        name='test_campaign',
        title='Test Campaign Title',
        language='en',
        currency='USD',
        description='Test campaign description',
        category=SimpleNamespace(
            category1=SimpleNamespace(
                name='category1',
                title='Category 1 Title',
                description='Category 1 Description',
                tags=['tag1', 'tag2'],
                products_count=2,
                products=[
                    SimpleNamespace(product_id=123, product_title='Product 1',promotion_link='link1',app_sale_price=10, original_price=20, sale_price=15, discount=5, product_main_image_url='url1', local_saved_image='local1', product_small_image_urls=['url2', 'url3'],product_video_url='v_url1', local_saved_video='local_v1',first_level_category_id=1,first_level_category_name='cat1',second_level_category_id=2,second_level_category_name='cat2',target_sale_price=12,target_sale_price_currency='USD',target_app_sale_price_currency='USD',target_original_price_currency='USD',original_price_currency='USD', evaluate_rate='5', shop_url='shop_url1', shop_id='shop_id1', tags=['tag3','tag4']),
                     SimpleNamespace(product_id=456, product_title='Product 2',promotion_link='link2',app_sale_price=11, original_price=21, sale_price=16, discount=6, product_main_image_url='url4', local_saved_image='local2', product_small_image_urls=['url5', 'url6'],product_video_url='v_url2', local_saved_video='local_v2',first_level_category_id=3,first_level_category_name='cat3',second_level_category_id=4,second_level_category_name='cat4',target_sale_price=13,target_sale_price_currency='EUR',target_app_sale_price_currency='EUR',target_original_price_currency='EUR',original_price_currency='EUR', evaluate_rate='4.5', shop_url='shop_url2', shop_id='shop_id2', tags=['tag5','tag6'])
                 ],
            ),
             category2=SimpleNamespace(
                 name='category2',
                title='Category 2 Title',
                 description='Category 2 Description',
                tags=['tag7', 'tag8'],
                 products_count=0,
                products=[]
            )
        )
    )
    return mock

@pytest.fixture
def mock_driver():
    """Provides a mock Driver object."""
    mock = MagicMock(spec=Driver)
    return mock

@pytest.fixture
def ali_gsheet(mock_ali_campaign_editor, mock_spreadsheet, mock_driver):
    """Provides an instance of AliCampaignGoogleSheet with mocked dependencies."""
    with patch('src.suppliers.aliexpress.campaign.gsheets_check_this_code.Driver', return_value=mock_driver):
        with patch('src.suppliers.aliexpress.campaign.gsheets_check_this_code.SpreadSheet', return_value=mock_spreadsheet):
             ali_gsheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='en', currency='USD')
    ali_gsheet.spreadsheet = mock_spreadsheet # assign to mock obj
    return ali_gsheet

# Tests for AliCampaignGoogleSheet class

def test_ali_campaign_google_sheet_initialization(mock_ali_campaign_editor, mock_driver, mock_spreadsheet):
    """Checks if the AliCampaignGoogleSheet is initialized correctly."""
    with patch('src.suppliers.aliexpress.campaign.gsheets_check_this_code.Driver', return_value=mock_driver):
        with patch('src.suppliers.aliexpress.campaign.gsheets_check_this_code.SpreadSheet', return_value=mock_spreadsheet):
             ali_gsheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='en', currency='USD')
    assert ali_gsheet.spreadsheet_id == '1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0'
    mock_ali_campaign_editor.assert_called_with(campaign_name='test_campaign', language='en', currency='USD')
    mock_driver.get_url.assert_called_with(f'https://docs.google.com/spreadsheets/d/{ali_gsheet.spreadsheet_id}')
    assert isinstance(ali_gsheet.editor, MagicMock)
    
def test_clear_success(ali_gsheet, mock_spreadsheet):
    """Checks if the clear method calls delete_products_worksheets."""
    ali_gsheet.delete_products_worksheets = MagicMock()
    ali_gsheet.clear()
    ali_gsheet.delete_products_worksheets.assert_called_once()
    
def test_clear_exception(ali_gsheet, mock_spreadsheet):
    """Checks if the clear method handles an exception from delete_products_worksheets."""
    ali_gsheet.delete_products_worksheets = MagicMock(side_effect=Exception("Test exception"))
    with patch('src.logger.logger.error') as mock_error:
        ali_gsheet.clear()
        mock_error.assert_called_once()

def test_delete_products_worksheets_success(ali_gsheet, mock_spreadsheet):
    """Checks if delete_products_worksheets deletes correct worksheets."""
    ali_gsheet.spreadsheet = mock_spreadsheet
    with patch('src.logger.logger.success') as mock_success:
            ali_gsheet.delete_products_worksheets()
            mock_spreadsheet.del_worksheet_by_id.assert_called_once_with(4) # id of "test_sheet"
            mock_success.assert_called_with("Worksheet 'test_sheet' deleted.")

def test_delete_products_worksheets_exception(ali_gsheet, mock_spreadsheet):
    """Checks if delete_products_worksheets handles exceptions correctly."""
    mock_spreadsheet.worksheets.side_effect = Exception("Test exception")
    with pytest.raises(Exception, match="Test exception"):
        with patch('src.logger.logger.error') as mock_error:
            ali_gsheet.delete_products_worksheets()
            mock_error.assert_called_once()

def test_set_campaign_worksheet_success(ali_gsheet, mock_ali_campaign_editor, mock_spreadsheet):
    """Checks if campaign data is written correctly to the worksheet."""
    mock_worksheet = mock_spreadsheet.get_worksheet()
    ali_gsheet.set_campaign_worksheet(mock_ali_campaign_editor.campaign)

    expected_updates = [
        {'range': 'A1', 'values': [['Campaign Name']]},
        {'range': 'B1', 'values': [['test_campaign']]},
        {'range': 'A2', 'values': [['Campaign Title']]},
        {'range': 'B2', 'values': [['Test Campaign Title']]},
        {'range': 'A3', 'values': [['Campaign Language']]},
        {'range': 'B3', 'values': [['en']]},
        {'range': 'A4', 'values': [['Campaign Currency']]},
         {'range': 'B4', 'values': [['USD']]},
        {'range': 'A5', 'values': [['Campaign Description']]},
        {'range': 'B5', 'values': [['Test campaign description']]}
    ]
    mock_worksheet.batch_update.assert_called_with(expected_updates)

def test_set_campaign_worksheet_exception(ali_gsheet, mock_ali_campaign_editor, mock_spreadsheet):
    """Checks if set_campaign_worksheet handles exceptions correctly."""
    mock_spreadsheet.get_worksheet.side_effect = Exception("Test exception")
    with pytest.raises(Exception, match="Test exception"):
        with patch('src.logger.logger.error') as mock_error:
            ali_gsheet.set_campaign_worksheet(mock_ali_campaign_editor.campaign)
            mock_error.assert_called_once()

def test_set_products_worksheet_with_category(ali_gsheet, mock_ali_campaign_editor, mock_spreadsheet):
    """Checks if set_products_worksheet writes data for a valid category."""
    ali_gsheet.copy_worksheet = MagicMock(return_value=mock_spreadsheet.get_worksheet())
    ali_gsheet._format_category_products_worksheet = MagicMock()
    ali_gsheet.set_products_worksheet('category1')
    mock_spreadsheet.get_worksheet().update.assert_called()
    assert mock_spreadsheet.get_worksheet().update.call_count == 2
    ali_gsheet._format_category_products_worksheet.assert_called_once()

def test_set_products_worksheet_no_category(ali_gsheet, mock_ali_campaign_editor, mock_spreadsheet):
    """Checks if set_products_worksheet handles case with no category."""
    with patch('src.logger.logger.warning') as mock_warning:
        ali_gsheet.set_products_worksheet(None)
        mock_warning.assert_called_once_with('No products found for category.')

def test_set_products_worksheet_exception(ali_gsheet, mock_ali_campaign_editor, mock_spreadsheet):
    """Checks if set_products_worksheet handles exceptions correctly."""
    ali_gsheet.copy_worksheet = MagicMock(return_value=mock_spreadsheet.get_worksheet())
    mock_spreadsheet.get_worksheet().update.side_effect = Exception("Test exception")
    with pytest.raises(Exception, match="Test exception"):
        with patch('src.logger.logger.error') as mock_error:
              ali_gsheet.set_products_worksheet('category1')
              mock_error.assert_called_once()
    
def test_set_categories_worksheet_success(ali_gsheet, mock_ali_campaign_editor, mock_spreadsheet):
    """Checks if category data is written correctly to the worksheet."""
    mock_worksheet = mock_spreadsheet.get_worksheet()
    ali_gsheet._format_categories_worksheet = MagicMock()
    ali_gsheet.set_categories_worksheet(mock_ali_campaign_editor.campaign.category)
    mock_worksheet.update.assert_called()
    assert mock_worksheet.update.call_count == 2
    ali_gsheet._format_categories_worksheet.assert_called_once()

def test_set_categories_worksheet_missing_attributes(ali_gsheet, mock_ali_campaign_editor, mock_spreadsheet):
     """Checks if set_categories_worksheet handles missing attributes in category objects."""
     mock_worksheet = mock_spreadsheet.get_worksheet()
     invalid_categories = SimpleNamespace(
         category1 = SimpleNamespace(
                name='category1',
                title='Category 1 Title',
                description='Category 1 Description',
                tags=['tag1', 'tag2'],
                # missing products_count,
             )
     )
     with patch('src.logger.logger.warning') as mock_warning:
        ali_gsheet.set_categories_worksheet(invalid_categories)
        mock_warning.assert_called_once_with("One or more category objects do not contain all required attributes.")

def test_set_categories_worksheet_exception(ali_gsheet, mock_ali_campaign_editor, mock_spreadsheet):
    """Checks if set_categories_worksheet handles exceptions correctly."""
    mock_spreadsheet.get_worksheet.side_effect = Exception("Test exception")
    with pytest.raises(Exception, match="Test exception"):
        with patch('src.logger.logger.error') as mock_error:
            ali_gsheet.set_categories_worksheet(mock_ali_campaign_editor.campaign.category)
            mock_error.assert_called_once()
            
def test_get_categories_success(ali_gsheet, mock_spreadsheet):
    """Checks if get_categories retrieves data correctly."""
    mock_worksheet = mock_spreadsheet.get_worksheet()
    mock_worksheet.get_all_records.return_value = [{'Name': 'test_category'}]
    result = ali_gsheet.get_categories()
    mock_worksheet.get_all_records.assert_called_once()
    assert result == [{'Name': 'test_category'}]

def test_set_category_products_with_category(ali_gsheet, mock_ali_campaign_editor, mock_spreadsheet):
    """Checks if set_category_products writes data for a valid category."""
    ali_gsheet.copy_worksheet = MagicMock(return_value=mock_spreadsheet.get_worksheet())
    ali_gsheet._format_category_products_worksheet = MagicMock()
    products = [
                SimpleNamespace(product_id=123, product_title='Product 1',promotion_link='link1',app_sale_price=10, original_price=20, sale_price=15, discount=5, product_main_image_url='url1', local_saved_image='local1', product_small_image_urls=['url2', 'url3'],product_video_url='v_url1', local_saved_video='local_v1',first_level_category_id=1,first_level_category_name='cat1',second_level_category_id=2,second_level_category_name='cat2',target_sale_price=12,target_sale_price_currency='USD',target_app_sale_price_currency='USD',target_original_price_currency='USD',original_price_currency='USD', evaluate_rate='5', shop_url='shop_url1', shop_id='shop_id1', tags=['tag3','tag4']),
                SimpleNamespace(product_id=456, product_title='Product 2',promotion_link='link2',app_sale_price=11, original_price=21, sale_price=16, discount=6, product_main_image_url='url4', local_saved_image='local2', product_small_image_urls=['url5', 'url6'],product_video_url='v_url2', local_saved_video='local_v2',first_level_category_id=3,first_level_category_name='cat3',second_level_category_id=4,second_level_category_name='cat4',target_sale_price=13,target_sale_price_currency='EUR',target_app_sale_price_currency='EUR',target_original_price_currency='EUR',original_price_currency='EUR', evaluate_rate='4.5', shop_url='shop_url2', shop_id='shop_id2', tags=['tag5','tag6'])
              ]
    ali_gsheet.set_category_products('category1', products)
    mock_spreadsheet.get_worksheet().update.assert_called()
    assert mock_spreadsheet.get_worksheet().update.call_count == 2
    ali_gsheet._format_category_products_worksheet.assert_called_once()

def test_set_category_products_no_category(ali_gsheet, mock_ali_campaign_editor, mock_spreadsheet):
     """Checks if set_category_products handles case with no category."""
     with patch('src.logger.logger.warning') as mock_warning:
          ali_gsheet.set_category_products(None, {})
          mock_warning.assert_called_once_with('No products found for category.')

def test_set_category_products_exception(ali_gsheet, mock_ali_campaign_editor, mock_spreadsheet):
     """Checks if set_category_products handles exceptions correctly."""
     ali_gsheet.copy_worksheet = MagicMock(return_value=mock_spreadsheet.get_worksheet())
     mock_spreadsheet.get_worksheet().update.side_effect = Exception("Test exception")
     with pytest.raises(Exception, match="Test exception"):
          with patch('src.logger.logger.error') as mock_error:
              ali_gsheet.set_category_products('category1', {})
              mock_error.assert_called_once()

def test_format_categories_worksheet_success(ali_gsheet, mock_spreadsheet):
    """Checks if _format_categories_worksheet formats correctly."""
    mock_worksheet = mock_spreadsheet.get_worksheet()
    ali_gsheet._format_categories_worksheet(mock_worksheet)
    mock_set_column_width = mock_worksheet.set_column_width
    mock_set_row_height = mock_worksheet.set_row_height
    mock_format_cell_range = mock_worksheet.format_cell_range
    mock_set_column_width.assert_called()
    assert mock_set_column_width.call_count == 5
    mock_set_row_height.assert_called_with('1:1', 40)
    mock_format_cell_range.assert_called_with('A1:E1', cellFormat(
        textFormat=textFormat(bold=True, fontSize=12),
        horizontalAlignment='CENTER',
        verticalAlignment='MIDDLE',
        backgroundColor=Color(0.8, 0.8, 0.8)
    ))


def test_format_categories_worksheet_exception(ali_gsheet, mock_spreadsheet):
     """Checks if _format_categories_worksheet handles exceptions correctly."""
     mock_worksheet = mock_spreadsheet.get_worksheet()
     mock_worksheet.set_column_width.side_effect = Exception("Test exception")
     with pytest.raises(Exception, match="Test exception"):
          with patch('src.logger.logger.error') as mock_error:
               ali_gsheet._format_categories_worksheet(mock_worksheet)
               mock_error.assert_called_once()
               
def test_format_category_products_worksheet_success(ali_gsheet, mock_spreadsheet):
    """Checks if _format_category_products_worksheet formats correctly."""
    mock_worksheet = mock_spreadsheet.get_worksheet()
    ali_gsheet._format_category_products_worksheet(mock_worksheet)
    mock_set_column_width = mock_worksheet.set_column_width
    mock_set_row_height = mock_worksheet.set_row_height
    mock_format_cell_range = mock_worksheet.format_cell_range
    mock_set_column_width.assert_called()
    assert mock_set_column_width.call_count == 25
    mock_set_row_height.assert_called_with('1:1', 40)
    mock_format_cell_range.assert_called_with('A1:Y1', cellFormat(
         textFormat=textFormat(bold=True, fontSize=12),
         horizontalAlignment='CENTER',
         verticalAlignment='TOP',
         backgroundColor=Color(0.8, 0.8, 0.8)
     ))

def test_format_category_products_worksheet_exception(ali_gsheet, mock_spreadsheet):
     """Checks if _format_category_products_worksheet handles exceptions correctly."""
     mock_worksheet = mock_spreadsheet.get_worksheet()
     mock_worksheet.set_column_width.side_effect = Exception("Test exception")
     with pytest.raises(Exception, match="Test exception"):
         with patch('src.logger.logger.error') as mock_error:
              ali_gsheet._format_category_products_worksheet(mock_worksheet)
              mock_error.assert_called_once()
```