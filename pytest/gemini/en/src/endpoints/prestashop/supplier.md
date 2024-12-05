```python
import pytest
from types import SimpleNamespace
from hypotez.src.endpoints.prestashop.supplier import PrestaSupplier

# Fixture for credentials
@pytest.fixture
def credentials():
    return SimpleNamespace(api_domain="test_domain", api_key="test_key")


# Test valid initialization with credentials
def test_presta_supplier_valid_init(credentials):
    """Tests initialization with valid credentials."""
    supplier = PrestaSupplier(credentials=credentials)
    assert supplier.api_domain == "test_domain"
    assert supplier.api_key == "test_key"


# Test valid initialization with individual parameters
def test_presta_supplier_valid_init_individual():
    """Tests initialization with individual api_domain and api_key parameters."""
    supplier = PrestaSupplier(api_domain="test_domain", api_key="test_key")
    assert supplier.api_domain == "test_domain"
    assert supplier.api_key == "test_key"


# Test initialization with only credentials dict
def test_presta_supplier_valid_init_credentials_dict():
    """Tests initialization with credentials as a dictionary."""
    credentials_dict = {"api_domain": "test_domain", "api_key": "test_key"}
    supplier = PrestaSupplier(credentials=credentials_dict)
    assert supplier.api_domain == "test_domain"
    assert supplier.api_key == "test_key"

# Test missing api_domain
def test_presta_supplier_missing_api_domain(credentials):
    """Tests initialization with missing api_domain."""
    credentials.api_domain = None
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
        PrestaSupplier(credentials=credentials)


# Test missing api_key
def test_presta_supplier_missing_api_key(credentials):
    """Tests initialization with missing api_key."""
    credentials.api_key = None
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
        PrestaSupplier(credentials=credentials)


# Test initialization with None credentials
def test_presta_supplier_none_credentials():
    """Tests initialization with None credentials."""
    with pytest.raises(ValueError, match="Необходимы оба параметра: api_domain и api_key."):
        PrestaSupplier(credentials=None)

```