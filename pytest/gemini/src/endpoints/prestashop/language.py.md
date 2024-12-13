```python
import pytest
from unittest.mock import patch, MagicMock
from types import SimpleNamespace
from src.endpoints.prestashop.language import PrestaLanguage
from src.logger.exceptions import PrestaShopException

# Fixture for valid credentials
@pytest.fixture
def valid_credentials():
    return SimpleNamespace(api_domain="test_domain", api_key="test_key")

# Fixture for invalid credentials (missing api_domain)
@pytest.fixture
def invalid_credentials_missing_domain():
    return SimpleNamespace(api_key="test_key")

# Fixture for invalid credentials (missing api_key)
@pytest.fixture
def invalid_credentials_missing_key():
    return SimpleNamespace(api_domain="test_domain")
    
# Fixture for a mock PrestaShop instance
@pytest.fixture
def mock_prestashop():
    with patch('src.endpoints.prestashop.language.PrestaShop') as MockPrestaShop:
        mock_instance = MockPrestaShop.return_value
        yield mock_instance

# Test for successful initialization with credentials as a SimpleNamespace
def test_init_with_credentials_simple_namespace(valid_credentials, mock_prestashop):
    """Checks successful initialization with credentials as a SimpleNamespace."""
    presta_language = PrestaLanguage(credentials=valid_credentials)
    assert presta_language.api_domain == "test_domain"
    assert presta_language.api_key == "test_key"
    mock_prestashop.__init__.assert_called_once_with("test_domain", "test_key")

# Test for successful initialization with credentials as a dictionary
def test_init_with_credentials_dict(mock_prestashop):
    """Checks successful initialization with credentials as a dictionary."""
    credentials = {"api_domain": "test_domain", "api_key": "test_key"}
    presta_language = PrestaLanguage(credentials=credentials)
    assert presta_language.api_domain == "test_domain"
    assert presta_language.api_key == "test_key"
    mock_prestashop.__init__.assert_called_once_with("test_domain", "test_key")


# Test for successful initialization with separate api_domain and api_key
def test_init_with_separate_api_params(mock_prestashop):
    """Checks successful initialization with separate api_domain and api_key."""
    presta_language = PrestaLanguage(api_domain="test_domain", api_key="test_key")
    assert presta_language.api_domain == "test_domain"
    assert presta_language.api_key == "test_key"
    mock_prestashop.__init__.assert_called_once_with("test_domain", "test_key")


# Test for missing api_domain in credentials
def test_init_missing_api_domain(invalid_credentials_missing_domain):
    """Checks exception raised when api_domain is missing."""
    with pytest.raises(ValueError, match='Необходимы оба параметра: api_domain и api_key.'):
        PrestaLanguage(credentials=invalid_credentials_missing_domain)

# Test for missing api_key in credentials
def test_init_missing_api_key(invalid_credentials_missing_key):
    """Checks exception raised when api_key is missing."""
    with pytest.raises(ValueError, match='Необходимы оба параметра: api_domain и api_key.'):
         PrestaLanguage(credentials=invalid_credentials_missing_key)

# Test for missing api_domain and api_key
def test_init_missing_both_params():
    """Checks exception raised when both api_domain and api_key are missing."""
    with pytest.raises(ValueError, match='Необходимы оба параметра: api_domain и api_key.'):
        PrestaLanguage()

# Test for credentials as None and missing api_domain and api_key
def test_init_credentials_none_missing_params():
    """Checks exception raised when credentials are None and api_domain/api_key are missing."""
    with pytest.raises(ValueError, match='Необходимы оба параметра: api_domain и api_key.'):
        PrestaLanguage(credentials=None)
```