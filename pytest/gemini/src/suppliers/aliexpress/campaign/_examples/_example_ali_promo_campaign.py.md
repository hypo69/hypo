```python
import pytest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch, mock_open
from src.suppliers.aliexpress import AliPromoCampaign
from src.utils.jjson import j_loads_ns

# Mocking gs.path.google_drive for testing
@pytest.fixture
def mock_gs_path():
    with patch('src.gs.path.google_drive', new=Path('/mocked/google_drive')):
        yield

# Mocking file system interaction
@pytest.fixture
def mock_get_directory_names():
    with patch('src.utils.get_directory_names', return_value=['280624_cleararanse', 'other_campaign']) as mock:
        yield mock

@pytest.fixture
def mock_read_text_file():
    with patch('src.utils.read_text_file', return_value='{"products": [{"product_id": 123, "product_title": "Test Product"}]}') as mock:
        yield mock

@pytest.fixture
def mock_csv2dict():
    with patch('src.utils.csv2dict', return_value=[{'id': 123, 'title': 'Test Product'}]) as mock:
        yield mock

@pytest.fixture
def mock_j_loads_ns():
    with patch('src.utils.jjson.j_loads_ns', return_value=SimpleNamespace(products=[SimpleNamespace(product_id=123, product_title='Test Product')])) as mock:
        yield mock


class TestAliPromoCampaign:
    def test_ali_promo_campaign_valid_init_dict(self, mock_gs_path, mock_get_directory_names, mock_read_text_file, mock_csv2dict, mock_j_loads_ns):
        """
        Test initialization of AliPromoCampaign with valid dictionary currency input.
        """
        campaign_name = '280624_cleararanse'
        category_name = 'gaming_comuter_accessories'
        currency_map = {'EN': 'USD'}

        campaign = AliPromoCampaign(campaign_name, category_name, currency_map)
        
        assert campaign.campaign_name == campaign_name
        assert campaign.category_name == category_name
        assert campaign.language == 'EN'
        assert campaign.currency == 'USD'
        assert isinstance(campaign.campaign, SimpleNamespace)
        assert isinstance(campaign.category, SimpleNamespace)
        assert isinstance(campaign.category.products, list)
        assert len(campaign.category.products) > 0
        assert campaign.category.products[0].product_id == 123
        assert campaign.category.products[0].product_title == 'Test Product'


    def test_ali_promo_campaign_valid_init_string(self, mock_gs_path, mock_get_directory_names, mock_read_text_file, mock_csv2dict, mock_j_loads_ns):
        """
        Test initialization of AliPromoCampaign with valid string currency input.
        """
        campaign_name = '280624_cleararanse'
        category_name = 'gaming_comuter_accessories'
        language = 'EN'
        currency = 'USD'

        campaign = AliPromoCampaign(campaign_name, category_name, language, currency)
        
        assert campaign.campaign_name == campaign_name
        assert campaign.category_name == category_name
        assert campaign.language == language
        assert campaign.currency == currency
        assert isinstance(campaign.campaign, SimpleNamespace)
        assert isinstance(campaign.category, SimpleNamespace)
        assert isinstance(campaign.category.products, list)
        assert len(campaign.category.products) > 0
        assert campaign.category.products[0].product_id == 123
        assert campaign.category.products[0].product_title == 'Test Product'

    def test_ali_promo_campaign_invalid_currency_map_type(self, mock_gs_path, mock_get_directory_names, mock_read_text_file, mock_csv2dict, mock_j_loads_ns):
        """
        Test initialization of AliPromoCampaign with invalid currency map type.
        """
        campaign_name = '280624_cleararanse'
        category_name = 'gaming_comuter_accessories'
        invalid_currency_map = 123  # Invalid input type

        with pytest.raises(TypeError):
            AliPromoCampaign(campaign_name, category_name, invalid_currency_map)

    def test_ali_promo_campaign_invalid_language_type(self, mock_gs_path, mock_get_directory_names, mock_read_text_file, mock_csv2dict, mock_j_loads_ns):
        """
        Test initialization of AliPromoCampaign with invalid language type.
        """
        campaign_name = '280624_cleararanse'
        category_name = 'gaming_comuter_accessories'
        invalid_language = 123 # Invalid input type
        currency = 'USD'

        with pytest.raises(TypeError):
            AliPromoCampaign(campaign_name, category_name, invalid_language, currency)

    def test_ali_promo_campaign_invalid_currency_type(self, mock_gs_path, mock_get_directory_names, mock_read_text_file, mock_csv2dict, mock_j_loads_ns):
        """
        Test initialization of AliPromoCampaign with invalid currency type.
        """
        campaign_name = '280624_cleararanse'
        category_name = 'gaming_comuter_accessories'
        language = 'EN'
        invalid_currency = 123  # Invalid input type

        with pytest.raises(TypeError):
             AliPromoCampaign(campaign_name, category_name, language, invalid_currency)


    def test_ali_promo_campaign_missing_campaign_name(self, mock_gs_path, mock_get_directory_names, mock_read_text_file, mock_csv2dict, mock_j_loads_ns):
        """
        Test initialization of AliPromoCampaign with a missing campaign name.
        """
        category_name = 'gaming_comuter_accessories'
        language = 'EN'
        currency = 'USD'

        with pytest.raises(TypeError):
            AliPromoCampaign(category_name = category_name, language = language, currency = currency)

    def test_ali_promo_campaign_missing_category_name(self, mock_gs_path, mock_get_directory_names, mock_read_text_file, mock_csv2dict, mock_j_loads_ns):
        """
        Test initialization of AliPromoCampaign with a missing category name.
        """
        campaign_name = '280624_cleararanse'
        language = 'EN'
        currency = 'USD'
        with pytest.raises(TypeError):
             AliPromoCampaign(campaign_name = campaign_name,  language = language, currency = currency)
```