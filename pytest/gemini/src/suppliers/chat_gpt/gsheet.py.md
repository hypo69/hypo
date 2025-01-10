```python
import pytest
from unittest.mock import MagicMock, patch
from types import SimpleNamespace
from src.suppliers.chat_gpt.gsheet import GptGs
from src.goog.spreadsheet.spreadsheet import SpreadSheet
from gspread.worksheet import Worksheet
from src.logger.logger import logger
import time

@pytest.fixture
def gpt_gs_instance():
    """Provides an instance of GptGs with mocked dependencies."""
    with patch('src.suppliers.chat_gpt.gsheet.SpreadSheet', autospec=True) as MockSpreadSheet:
      
        mock_instance = MockSpreadSheet.return_value
        mock_instance.spreadsheet = MagicMock()
        mock_instance.get_worksheet = MagicMock()
        mock_instance.copy_worksheet = MagicMock()
        mock_instance.delete_worksheet = MagicMock()
        mock_instance.del_worksheet_by_id = MagicMock()
        
        gpt_gs = GptGs()
        gpt_gs.spreadsheet = mock_instance
        return gpt_gs

@pytest.fixture
def mock_worksheet():
    """Provides a mock Worksheet object."""
    mock_ws = MagicMock(spec=Worksheet)
    mock_ws.get_all_values.return_value = []
    return mock_ws

def test_gptgs_init(gpt_gs_instance):
    """Tests the initialization of GptGs class."""
    assert isinstance(gpt_gs_instance, GptGs)
    assert gpt_gs_instance.spreadsheet is not None

def test_clear_success(gpt_gs_instance, mock_worksheet):
    """Tests clear method with successful worksheet deletion."""
    gpt_gs_instance.spreadsheet.worksheets.return_value = [mock_worksheet]
    mock_worksheet.title = 'test_sheet'
    gpt_gs_instance.clear()
    gpt_gs_instance.spreadsheet.del_worksheet_by_id.assert_called()
    
def test_clear_exception(gpt_gs_instance, mock_worksheet):
    """Tests clear method with exception during worksheet deletion."""
    gpt_gs_instance.spreadsheet.worksheets.side_effect = Exception("Test exception")
    with pytest.raises(Exception):
        gpt_gs_instance.clear()
    
def test_update_chat_worksheet_valid_data(gpt_gs_instance, mock_worksheet):
    """Tests update_chat_worksheet with valid data."""
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = mock_worksheet
    data = SimpleNamespace(name="Test Name", title="Test Title", description="Test Description", tags=["tag1", "tag2"], products_count=5)
    conversation_name = "test_conversation"
    gpt_gs_instance.update_chat_worksheet(data, conversation_name)
    mock_worksheet.batch_update.assert_called()

def test_update_chat_worksheet_empty_data(gpt_gs_instance, mock_worksheet):
    """Tests update_chat_worksheet with empty SimpleNamespace."""
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = mock_worksheet
    data = SimpleNamespace()
    conversation_name = "test_conversation"
    gpt_gs_instance.update_chat_worksheet(data, conversation_name)
    mock_worksheet.batch_update.assert_called()

def test_update_chat_worksheet_exception(gpt_gs_instance, mock_worksheet):
    """Tests update_chat_worksheet with exception when getting worksheet."""
    gpt_gs_instance.spreadsheet.get_worksheet.side_effect = Exception("Test exception")
    data = SimpleNamespace(name="Test Name", title="Test Title", description="Test Description", tags=["tag1", "tag2"], products_count=5)
    conversation_name = "test_conversation"
    with pytest.raises(Exception):
       gpt_gs_instance.update_chat_worksheet(data, conversation_name)

def test_get_campaign_worksheet_valid_data(gpt_gs_instance, mock_worksheet):
    """Tests get_campaign_worksheet with valid data."""
    mock_worksheet.get_all_values.return_value = [
        ['Label', 'Test Campaign'],
        ['Label', 'Test Title'],
        ['Label', 'en'],
        ['Label', 'USD'],
        ['Label', 'Test Description']
    ]
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = mock_worksheet
    campaign_data = gpt_gs_instance.get_campaign_worksheet()
    assert isinstance(campaign_data, SimpleNamespace)
    assert campaign_data.name == "Test Campaign"
    assert campaign_data.title == "Test Title"
    assert campaign_data.language == "en"
    assert campaign_data.currency == "USD"
    assert campaign_data.description == "Test Description"

def test_get_campaign_worksheet_not_found(gpt_gs_instance, mock_worksheet):
    """Tests get_campaign_worksheet when worksheet is not found."""
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = None
    with pytest.raises(ValueError, match="Worksheet \'campaign\' not found."):
        gpt_gs_instance.get_campaign_worksheet()

def test_get_campaign_worksheet_exception(gpt_gs_instance):
    """Tests get_campaign_worksheet with an exception during data retrieval."""
    gpt_gs_instance.spreadsheet.get_worksheet.side_effect = Exception("Test exception")
    with pytest.raises(Exception):
        gpt_gs_instance.get_campaign_worksheet()
        
def test_set_category_worksheet_valid_data(gpt_gs_instance, mock_worksheet):
    """Tests set_category_worksheet with valid SimpleNamespace data."""
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = mock_worksheet
    category_data = SimpleNamespace(name="Test Category", title="Test Title", description="Test Description", tags=["tag1", "tag2"], products_count=5)
    gpt_gs_instance.set_category_worksheet(category_data)
    mock_worksheet.update.assert_called()

def test_set_category_worksheet_from_string(gpt_gs_instance, mock_worksheet):
     """Tests set_category_worksheet with a string as an argument."""
     gpt_gs_instance.spreadsheet.get_worksheet.return_value = mock_worksheet
     gpt_gs_instance.get_campaign_category = MagicMock(return_value=SimpleNamespace(
        name="Test Category", title="Test Title", description="Test Description", tags=["tag1", "tag2"], products_count=5
     ))
     gpt_gs_instance.set_category_worksheet("Test Category")
     mock_worksheet.update.assert_called()

def test_set_category_worksheet_invalid_input(gpt_gs_instance, mock_worksheet):
    """Tests set_category_worksheet with invalid input (not SimpleNamespace)."""
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = mock_worksheet
    with pytest.raises(TypeError, match="Expected SimpleNamespace for category."):
        gpt_gs_instance.set_category_worksheet("invalid")

def test_set_category_worksheet_exception(gpt_gs_instance):
    """Tests set_category_worksheet with exception when getting worksheet."""
    gpt_gs_instance.spreadsheet.get_worksheet.side_effect = Exception("Test exception")
    category_data = SimpleNamespace(name="Test Category", title="Test Title", description="Test Description", tags=["tag1", "tag2"], products_count=5)
    with pytest.raises(Exception):
        gpt_gs_instance.set_category_worksheet(category_data)
    
def test_get_category_worksheet_valid_data(gpt_gs_instance, mock_worksheet):
    """Tests get_category_worksheet with valid data."""
    mock_worksheet.get_all_values.return_value = [
        ['Label', 'Test'],
        ['Name', 'Test Category'],
        ['Title', 'Test Title'],
        ['Description', 'Test Description'],
        ['Tags', 'tag1, tag2'],
        ['Products Count', '5']
    ]
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = mock_worksheet
    category_data = gpt_gs_instance.get_category_worksheet()
    assert isinstance(category_data, SimpleNamespace)
    assert category_data.name == "Test Category"
    assert category_data.title == "Test Title"
    assert category_data.description == "Test Description"
    assert category_data.tags == ["tag1", "tag2"]
    assert category_data.products_count == 5

def test_get_category_worksheet_not_found(gpt_gs_instance, mock_worksheet):
    """Tests get_category_worksheet when worksheet is not found."""
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = None
    with pytest.raises(ValueError, match="Worksheet \'category\' not found."):
        gpt_gs_instance.get_category_worksheet()
        
def test_get_category_worksheet_exception(gpt_gs_instance):
    """Tests get_category_worksheet with an exception during data retrieval."""
    gpt_gs_instance.spreadsheet.get_worksheet.side_effect = Exception("Test exception")
    with pytest.raises(Exception):
       gpt_gs_instance.get_category_worksheet()

def test_set_categories_worksheet_valid_data(gpt_gs_instance, mock_worksheet):
    """Tests set_categories_worksheet with valid SimpleNamespace data."""
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = mock_worksheet
    categories_data = SimpleNamespace(
        cat1 = SimpleNamespace(name="Test Category 1", title="Test Title 1", description="Test Description 1", tags=["tag1", "tag2"], products_count=5),
        cat2 = SimpleNamespace(name="Test Category 2", title="Test Title 2", description="Test Description 2", tags=["tag3", "tag4"], products_count=10)
    )
    gpt_gs_instance.set_categories_worksheet(categories_data)
    mock_worksheet.batch_update.assert_called()
    assert mock_worksheet.batch_update.call_count == 2

def test_set_categories_worksheet_skip_invalid_attribute(gpt_gs_instance, mock_worksheet):
    """Tests set_categories_worksheet skipping non-SimpleNamespace attributes."""
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = mock_worksheet
    categories_data = SimpleNamespace(
        cat1 = SimpleNamespace(name="Test Category 1", title="Test Title 1", description="Test Description 1", tags=["tag1", "tag2"], products_count=5),
        invalid_attr = "not a SimpleNamespace",
        cat2 = SimpleNamespace(name="Test Category 2", title="Test Title 2", description="Test Description 2", tags=["tag3", "tag4"], products_count=10)
    )
    gpt_gs_instance.set_categories_worksheet(categories_data)
    mock_worksheet.batch_update.assert_called()
    assert mock_worksheet.batch_update.call_count == 2

def test_set_categories_worksheet_exception(gpt_gs_instance):
    """Tests set_categories_worksheet with exception when getting worksheet."""
    gpt_gs_instance.spreadsheet.get_worksheet.side_effect = Exception("Test exception")
    categories_data = SimpleNamespace(
        cat1 = SimpleNamespace(name="Test Category 1", title="Test Title 1", description="Test Description 1", tags=["tag1", "tag2"], products_count=5)
    )
    with pytest.raises(Exception):
        gpt_gs_instance.set_categories_worksheet(categories_data)

def test_get_categories_worksheet_valid_data(gpt_gs_instance, mock_worksheet):
    """Tests get_categories_worksheet with valid data."""
    mock_worksheet.get_all_values.return_value = [
        ['Header1', 'Header2', 'Header3', 'Header4', 'Header5','Header6'],
        ['Name1', 'Title1', 'Description1', 'tag1, tag2', '5', 'other'],
        ['Name2', 'Title2', 'Description2', 'tag3, tag4', '10','other'],
        ['Name3', 'Title3', 'Description3', 'tag3, tag4', '10','other', 'some data']
    ]
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = mock_worksheet
    categories_data = gpt_gs_instance.get_categories_worksheet()
    assert isinstance(categories_data, list)
    assert len(categories_data) == 3
    assert categories_data[0] == ['Name1', 'Title1', 'Description1', 'tag1, tag2', '5']
    assert categories_data[1] == ['Name2', 'Title2', 'Description2', 'tag3, tag4', '10']
    assert categories_data[2] == ['Name3', 'Title3', 'Description3', 'tag3, tag4', '10']

def test_get_categories_worksheet_empty_worksheet(gpt_gs_instance, mock_worksheet):
     """Tests get_categories_worksheet with empty data."""
     mock_worksheet.get_all_values.return_value = [[]]
     gpt_gs_instance.spreadsheet.get_worksheet.return_value = mock_worksheet
     categories_data = gpt_gs_instance.get_categories_worksheet()
     assert categories_data == []

def test_get_categories_worksheet_not_found(gpt_gs_instance):
    """Tests get_categories_worksheet when worksheet is not found."""
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = None
    with pytest.raises(ValueError, match="Worksheet \'categories\' not found."):
        gpt_gs_instance.get_categories_worksheet()

def test_get_categories_worksheet_exception(gpt_gs_instance):
    """Tests get_categories_worksheet with exception during retrieval."""
    gpt_gs_instance.spreadsheet.get_worksheet.side_effect = Exception("Test exception")
    with pytest.raises(Exception):
       gpt_gs_instance.get_categories_worksheet()

def test_set_product_worksheet_valid_data(gpt_gs_instance, mock_worksheet):
    """Tests set_product_worksheet with valid data."""
    gpt_gs_instance.spreadsheet.copy_worksheet.return_value = mock_worksheet
    product_data = SimpleNamespace(
        product_id=123, app_sale_price=10.0, original_price=15.0, sale_price=12.0, discount=20.0,
        product_main_image_url="url1", local_image_path="local1", product_small_image_urls=["url2", "url3"],
        product_video_url="video1", local_video_path="local_video", first_level_category_id=1,
        first_level_category_name="cat1", second_level_category_id=2, second_level_category_name="cat2",
        target_sale_price=11.0, target_sale_price_currency="USD", target_app_sale_price_currency="USD",
        target_original_price_currency="USD", original_price_currency="USD", product_title="test_product",
        evaluate_rate=4.5, promotion_link="prom_link", shop_url="shop_url", shop_id=12345, tags=["tag1", "tag2"]
    )
    category_name = "test_category"
    gpt_gs_instance.set_product_worksheet(product_data, category_name)
    mock_worksheet.update.assert_called()
    assert mock_worksheet.update.call_count == 2

def test_set_product_worksheet_exception(gpt_gs_instance, mock_worksheet):
    """Tests set_product_worksheet with exception when copy worksheet."""
    gpt_gs_instance.spreadsheet.copy_worksheet.side_effect = Exception("Test exception")
    product_data = SimpleNamespace(
        product_id=123, app_sale_price=10.0, original_price=15.0, sale_price=12.0, discount=20.0,
        product_main_image_url="url1", local_image_path="local1", product_small_image_urls=["url2", "url3"],
        product_video_url="video1", local_video_path="local_video", first_level_category_id=1,
        first_level_category_name="cat1", second_level_category_id=2, second_level_category_name="cat2",
        target_sale_price=11.0, target_sale_price_currency="USD", target_app_sale_price_currency="USD",
        target_original_price_currency="USD", original_price_currency="USD", product_title="test_product",
        evaluate_rate=4.5, promotion_link="prom_link", shop_url="shop_url", shop_id=12345, tags=["tag1", "tag2"]
    )
    category_name = "test_category"
    with pytest.raises(Exception):
        gpt_gs_instance.set_product_worksheet(product_data, category_name)

def test_get_product_worksheet_valid_data(gpt_gs_instance, mock_worksheet):
    """Tests get_product_worksheet with valid data."""
    mock_worksheet.get_all_values.return_value = [
        ['Header', 'Value'],
        ['ID', '123'],
        ['Name', 'Test Product'],
        ['Title', 'Test Title'],
        ['Description', 'Test Description'],
        ['Tags', 'tag1, tag2'],
        ['Price', '99.99']
    ]
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = mock_worksheet
    product_data = gpt_gs_instance.get_product_worksheet()
    assert isinstance(product_data, SimpleNamespace)
    assert product_data.id == "123"
    assert product_data.name == "Test Product"
    assert product_data.title == "Test Title"
    assert product_data.description == "Test Description"
    assert product_data.tags == ["tag1", "tag2"]
    assert product_data.price == 99.99

def test_get_product_worksheet_not_found(gpt_gs_instance):
    """Tests get_product_worksheet when worksheet is not found."""
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = None
    with pytest.raises(ValueError, match="Worksheet \'products\' not found."):
       gpt_gs_instance.get_product_worksheet()
       
def test_get_product_worksheet_exception(gpt_gs_instance):
    """Tests get_product_worksheet with exception during retrieval."""
    gpt_gs_instance.spreadsheet.get_worksheet.side_effect = Exception("Test exception")
    with pytest.raises(Exception):
       gpt_gs_instance.get_product_worksheet()

def test_set_products_worksheet_valid_data(gpt_gs_instance, mock_worksheet):
    """Tests set_products_worksheet with valid data."""
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = mock_worksheet
    category_name = "test_category"
    gpt_gs_instance.campaign = SimpleNamespace(
        category=SimpleNamespace(
            test_category=SimpleNamespace(
                products=[
                    SimpleNamespace(
                    product_id=1, product_title='Product 1', title='Title 1', local_image_path='image1', product_video_url='video1',
                    original_price=10.0, app_sale_price=8.0, target_sale_price=9.0
                ),
                 SimpleNamespace(
                    product_id=2, product_title='Product 2', title='Title 2', local_image_path='image2', product_video_url='video2',
                    original_price=20.0, app_sale_price=16.0, target_sale_price=18.0
                )
                ]
            )
        )
    )

    gpt_gs_instance.set_products_worksheet(category_name)
    mock_worksheet.batch_update.assert_called()
    assert mock_worksheet.batch_update.call_count == 20

def test_set_products_worksheet_no_products(gpt_gs_instance, mock_worksheet):
    """Tests set_products_worksheet when no products found."""
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = mock_worksheet
    category_name = "test_category"
    gpt_gs_instance.campaign = SimpleNamespace(
        category=SimpleNamespace(
            test_category=SimpleNamespace(
                products=[]
            )
        )
    )
    gpt_gs_instance.set_products_worksheet(category_name)
    mock_worksheet.batch_update.assert_not_called()

def test_set_products_worksheet_no_category(gpt_gs_instance):
    """Tests set_products_worksheet when category does not exist."""
    category_name = None
    gpt_gs_instance.set_products_worksheet(category_name)
    # Check that warning message is logged
    assert True

def test_set_products_worksheet_exception(gpt_gs_instance):
     """Tests set_products_worksheet with exception during batch update."""
     gpt_gs_instance.spreadsheet.get_worksheet.side_effect = Exception("Test exception")
     category_name = "test_category"
     gpt_gs_instance.campaign = SimpleNamespace(
        category=SimpleNamespace(
            test_category=SimpleNamespace(
                products=[
                    SimpleNamespace(
                    product_id=1, product_title='Product 1', title='Title 1', local_image_path='image1', product_video_url='video1',
                    original_price=10.0, app_sale_price=8.0, target_sale_price=9.0
                )
                ]
            )
        )
    )
     with pytest.raises(Exception):
          gpt_gs_instance.set_products_worksheet(category_name)
       
def test_delete_products_worksheets_success(gpt_gs_instance, mock_worksheet):
    """Tests delete_products_worksheets with successful deletion of sheets."""
    mock_worksheet1 = MagicMock(spec=Worksheet)
    mock_worksheet1.title = 'test_sheet1'
    mock_worksheet2 = MagicMock(spec=Worksheet)
    mock_worksheet2.title = 'test_sheet2'
    mock_worksheet3 = MagicMock(spec=Worksheet)
    mock_worksheet3.title = 'categories'
    mock_worksheet4 = MagicMock(spec=Worksheet)
    mock_worksheet4.title = 'product'
    mock_worksheet5 = MagicMock(spec=Worksheet)
    mock_worksheet5.title = 'category'
    mock_worksheet6 = MagicMock(spec=Worksheet)
    mock_worksheet6.title = 'campaign'
    gpt_gs_instance.spreadsheet.worksheets.return_value = [mock_worksheet1, mock_worksheet2, mock_worksheet3,mock_worksheet4,mock_worksheet5,mock_worksheet6]
    gpt_gs_instance.delete_products_worksheets()
    gpt_gs_instance.spreadsheet.del_worksheet_by_id.assert_called()
    assert gpt_gs_instance.spreadsheet.del_worksheet_by_id.call_count == 2
def test_delete_products_worksheets_exception(gpt_gs_instance):
    """Tests delete_products_worksheets with exception during worksheet retrieval."""
    gpt_gs_instance.spreadsheet.worksheets.side_effect = Exception("Test exception")
    with pytest.raises(Exception):
        gpt_gs_instance.delete_products_worksheets()

def test_save_categories_from_worksheet_valid_data(gpt_gs_instance, mock_worksheet):
    """Tests save_categories_from_worksheet with valid data."""
    mock_worksheet.get_all_values.return_value = [
        ['Name1', 'Title1', 'Description1', 'tag1,tag2', '5'],
        ['Name2', 'Title2', 'Description2', 'tag3,tag4', '10']
    ]
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = mock_worksheet
    gpt_gs_instance.campaign = SimpleNamespace(category=None)
    gpt_gs_instance.update_campaign = MagicMock()

    gpt_gs_instance.save_categories_from_worksheet(update=True)
    assert hasattr(gpt_gs_instance.campaign, 'category')
    assert isinstance(gpt_gs_instance.campaign.category, SimpleNamespace)
    assert hasattr(gpt_gs_instance.campaign.category, 'Name1')
    assert hasattr(gpt_gs_instance.campaign.category, 'Name2')
    assert gpt_gs_instance.campaign.category.Name1.name == 'Name1'
    assert gpt_gs_instance.campaign.category.Name1.title == 'Title1'
    assert gpt_gs_instance.campaign.category.Name1.description == 'Description1'
    assert gpt_gs_instance.campaign.category.Name1.tags == ['tag1', 'tag2']
    assert gpt_gs_instance.campaign.category.Name1.products_count == '5'
    assert gpt_gs_instance.update_campaign.call_count == 1
    
def test_save_categories_from_worksheet_no_update(gpt_gs_instance, mock_worksheet):
    """Tests save_categories_from_worksheet when update is set to False."""
    mock_worksheet.get_all_values.return_value = [
        ['Name1', 'Title1', 'Description1', 'tag1,tag2', '5']
    ]
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = mock_worksheet
    gpt_gs_instance.campaign = SimpleNamespace(category=None)
    gpt_gs_instance.update_campaign = MagicMock()

    gpt_gs_instance.save_categories_from_worksheet(update=False)
    assert gpt_gs_instance.update_campaign.call_count == 0

def test_save_categories_from_worksheet_exception(gpt_gs_instance):
    """Tests save_categories_from_worksheet with exception during retrieval."""
    gpt_gs_instance.spreadsheet.get_categories_worksheet.side_effect = Exception("Test exception")
    with pytest.raises(Exception):
        gpt_gs_instance.save_categories_from_worksheet()

def test_save_campaign_from_worksheet_success(gpt_gs_instance, mock_worksheet):
    """Tests save_campaign_from_worksheet with successful data saving."""
    mock_worksheet.get_all_values.return_value = [
            ['Label', 'Test Campaign'],
            ['Label', 'Test Title'],
            ['Label', 'en'],
            ['Label', 'USD'],
            ['Label', 'Test Description']
        ]
    gpt_gs_instance.spreadsheet.get_worksheet.return_value = mock_worksheet
    gpt_gs_instance.campaign = SimpleNamespace(category=None)
    gpt_gs_instance.save_categories_from_worksheet = MagicMock()
    gpt_gs_instance.update_campaign = MagicMock()
    
    gpt_gs_instance.save_campaign_from_worksheet()
    
    assert gpt_gs_instance.save_categories_from_worksheet.call_count == 1
    assert gpt_gs_instance.update_campaign.call_count == 1
    assert isinstance(gpt_gs_instance.campaign, SimpleNamespace)
    assert gpt_gs_instance.campaign.name == 'Test Campaign'
    assert gpt_gs_instance.campaign.title == 'Test Title'
    assert gpt_gs_instance.campaign.language == 'en'
    assert gpt_gs_instance.campaign.currency == 'USD'
    assert gpt_gs_instance.campaign.description == 'Test Description'

def test_save_campaign_from_worksheet_exception(gpt_gs_instance):
    """Tests save_campaign_from_worksheet with exception during retrieval."""
    gpt_gs_instance.spreadsheet.get_campaign_worksheet.side_effect = Exception("Test exception")
    with pytest.raises(Exception):
        gpt_gs_instance.save_campaign_from_worksheet()
```