```python
import pytest
from unittest.mock import patch, MagicMock
from src.endpoints.prestashop.category import PrestaCategory
from src.utils.jjson import j_loads
from types import SimpleNamespace
from src.logger.logger import logger


@pytest.fixture
def mock_prestashop_instance():
    """Provides a mock PrestaShop instance for testing."""
    with patch('src.endpoints.prestashop.category.PrestaShop.__init__', return_value=None) as mock_init:
        instance = PrestaCategory(api_domain='test_domain', api_key='test_key')
        yield instance
        mock_init.assert_called_once_with('test_domain', 'test_key')


@pytest.fixture
def mock_prestashop_get():
    """Provides a mock for PrestaShop's get method."""
    with patch('src.endpoints.prestashop.category.PrestaShop.get') as mock_get:
        yield mock_get


class TestPrestaCategory:

    def test_init_with_credentials_dict(self):
        """Checks correct initialization with credentials dictionary."""
        credentials = {'api_domain': 'test_domain', 'api_key': 'test_key'}
        instance = PrestaCategory(credentials=credentials)
        assert instance.api_domain == 'test_domain'
        assert instance.api_key == 'test_key'

    def test_init_with_credentials_simplenamespace(self):
        """Checks correct initialization with credentials SimpleNamespace object."""
        credentials = SimpleNamespace(api_domain='test_domain', api_key='test_key')
        instance = PrestaCategory(credentials=credentials)
        assert instance.api_domain == 'test_domain'
        assert instance.api_key == 'test_key'


    def test_init_with_separate_params(self):
         """Checks correct initialization with separate api_domain and api_key parameters."""
         instance = PrestaCategory(api_domain='test_domain', api_key='test_key')
         assert instance.api_domain == 'test_domain'
         assert instance.api_key == 'test_key'

    def test_init_missing_credentials(self):
        """Checks if ValueError is raised when credentials are missing."""
        with pytest.raises(ValueError, match='Необходимы оба параметра: api_domain и api_key.'):
            PrestaCategory()
        with pytest.raises(ValueError, match='Необходимы оба параметра: api_domain и api_key.'):
            PrestaCategory(api_domain='test_domain')
        with pytest.raises(ValueError, match='Необходимы оба параметра: api_domain и api_key.'):
            PrestaCategory(api_key='test_key')


    def test_get_parent_categories_list_valid_category(self, mock_prestashop_instance, mock_prestashop_get):
        """Checks correct behavior when a valid category is provided."""
        mock_prestashop_get.return_value = {'id_parent': '10', 'id': '11'}
        result = mock_prestashop_instance.get_parent_categories_list(id_category=11)
        assert result == [10]
        mock_prestashop_get.assert_called_once_with('categories', resource_id=11, display='full', io_format='JSON')
        
    def test_get_parent_categories_list_root_category(self, mock_prestashop_instance, mock_prestashop_get):
        """Checks correct behavior when the root category is reached."""
        mock_prestashop_get.return_value = {'id_parent': '2', 'id': '10'}
        result = mock_prestashop_instance.get_parent_categories_list(id_category=10)
        assert result == [2]
        mock_prestashop_get.assert_called_once_with('categories', resource_id=10, display='full', io_format='JSON')

    def test_get_parent_categories_list_nested_categories(self, mock_prestashop_instance, mock_prestashop_get):
        """Checks correct behavior for nested categories."""
        mock_prestashop_get.side_effect = [
            {'id_parent': '10', 'id': '11'},
            {'id_parent': '5', 'id': '10'},
            {'id_parent': '2', 'id': '5'},
        ]
        result = mock_prestashop_instance.get_parent_categories_list(id_category=11)
        assert result == [10, 5, 2]
        assert mock_prestashop_get.call_count == 3
    
    def test_get_parent_categories_list_invalid_category(self, mock_prestashop_instance, mock_prestashop_get, caplog):
        """Checks correct handling of an invalid category (no category data returned)."""
        mock_prestashop_get.return_value = None
        result = mock_prestashop_instance.get_parent_categories_list(id_category=123)
        assert result is None
        assert "Что-то не так с категориями" in caplog.text

    def test_get_parent_categories_list_no_category_id(self, mock_prestashop_instance, mock_prestashop_get, caplog):
        """Checks correct behavior when no category id is provided."""
        result = mock_prestashop_instance.get_parent_categories_list(id_category=None)
        assert result == []
        assert "Нет id категории!!!" in caplog.text
        mock_prestashop_get.assert_not_called()
```