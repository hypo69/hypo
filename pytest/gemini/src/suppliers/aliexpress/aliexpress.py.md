```python
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from requests.cookies import RequestsCookieJar

from src.suppliers.aliexpress.aliexpress import Aliexpress


@pytest.fixture
def mock_supplier_init():
    """Mocks the Supplier.__init__ method to avoid its execution."""
    with patch('src.suppliers.supplier.Supplier.__init__', return_value=None) as mock:
        yield mock

@pytest.fixture
def mock_ali_requests_init():
    """Mocks the AliRequests.__init__ method to avoid its execution."""
    with patch('src.suppliers.aliexpress.alirequests.AliRequests.__init__', return_value=None) as mock:
        yield mock
    
@pytest.fixture
def mock_ali_api_init():
    """Mocks the AliApi.__init__ method to avoid its execution."""
    with patch('src.suppliers.aliexpress.aliapi.AliApi.__init__', return_value=None) as mock:
        yield mock


class TestAliexpress:
    def test_aliexpress_init_no_webdriver(self, mock_supplier_init, mock_ali_requests_init, mock_ali_api_init):
        """Test initialization with no webdriver."""
        aliexpress = Aliexpress()
        mock_supplier_init.assert_called_once_with(supplier_prefix='aliexpress', locale={'EN': 'USD'}, webdriver=False)
        
    def test_aliexpress_init_with_chrome_webdriver(self, mock_supplier_init, mock_ali_requests_init, mock_ali_api_init):
        """Test initialization with chrome webdriver."""
        aliexpress = Aliexpress(webdriver='chrome')
        mock_supplier_init.assert_called_once_with(supplier_prefix='aliexpress', locale={'EN': 'USD'}, webdriver='chrome')

    def test_aliexpress_init_with_mozilla_webdriver(self, mock_supplier_init, mock_ali_requests_init, mock_ali_api_init):
        """Test initialization with mozilla webdriver."""
        aliexpress = Aliexpress(webdriver='mozilla')
        mock_supplier_init.assert_called_once_with(supplier_prefix='aliexpress', locale={'EN': 'USD'}, webdriver='mozilla')

    def test_aliexpress_init_with_edge_webdriver(self, mock_supplier_init, mock_ali_requests_init, mock_ali_api_init):
        """Test initialization with edge webdriver."""
        aliexpress = Aliexpress(webdriver='edge')
        mock_supplier_init.assert_called_once_with(supplier_prefix='aliexpress', locale={'EN': 'USD'}, webdriver='edge')
    
    def test_aliexpress_init_with_default_webdriver(self, mock_supplier_init, mock_ali_requests_init, mock_ali_api_init):
        """Test initialization with default webdriver."""
        aliexpress = Aliexpress(webdriver='default')
        mock_supplier_init.assert_called_once_with(supplier_prefix='aliexpress', locale={'EN': 'USD'}, webdriver='default')

    def test_aliexpress_init_with_custom_locale_str(self, mock_supplier_init, mock_ali_requests_init, mock_ali_api_init):
      """Test initialization with custom locale str."""
      aliexpress = Aliexpress(locale='RU')
      mock_supplier_init.assert_called_once_with(supplier_prefix='aliexpress', locale='RU', webdriver=False)

    def test_aliexpress_init_with_custom_locale_dict(self, mock_supplier_init, mock_ali_requests_init, mock_ali_api_init):
        """Test initialization with custom locale dict."""
        custom_locale = {'ES': 'EUR'}
        aliexpress = Aliexpress(locale=custom_locale)
        mock_supplier_init.assert_called_once_with(supplier_prefix='aliexpress', locale=custom_locale, webdriver=False)
    
    def test_aliexpress_init_with_args_and_kwargs(self, mock_supplier_init, mock_ali_requests_init, mock_ali_api_init):
        """Test initialization with additional args and kwargs."""
        aliexpress = Aliexpress('chrome', locale={'FR':'EUR'}, test_arg='test', test_kwarg='test')
        mock_supplier_init.assert_called_once_with(supplier_prefix='aliexpress', locale={'FR':'EUR'}, webdriver='chrome', test_arg='test', test_kwarg='test')

```