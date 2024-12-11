```python
import pytest
from types import SimpleNamespace
from hypotez.src.endpoints.prestashop.supplier import PrestaSupplier


@pytest.fixture
def credentials():
    """Fixture to provide credentials."""
    return SimpleNamespace(api_domain="test_domain", api_key="test_key")


def test_presta_supplier_init_with_credentials(credentials):
    """Test PrestaSupplier initialization with credentials."""
    supplier = PrestaSupplier(credentials=credentials)
    assert supplier.api_domain == "test_domain"
    assert supplier.api_key == "test_key"


def test_presta_supplier_init_with_separate_params(
    
):
    """Test PrestaSupplier initialization with separate parameters."""
    supplier = PrestaSupplier(
        api_domain="test_domain", api_key="test_key"
    )
    assert supplier.api_domain == "test_domain"
    assert supplier.api_key == "test_key"


def test_presta_supplier_init_missing_api_domain():
    """Test PrestaSupplier initialization with missing api_domain."""
    with pytest.raises(ValueError) as excinfo:
        PrestaSupplier(api_key="test_key")
    assert "Необходимы оба параметра: api_domain и api_key." in str(excinfo.value)


def test_presta_supplier_init_missing_api_key():
    """Test PrestaSupplier initialization with missing api_key."""
    with pytest.raises(ValueError) as excinfo:
        PrestaSupplier(api_domain="test_domain")
    assert "Необходимы оба параметра: api_domain и api_key." in str(excinfo.value)


def test_presta_supplier_init_credentials_none():
    """Test PrestaSupplier initialization with credentials=None."""
    with pytest.raises(ValueError) as excinfo:
        PrestaSupplier(credentials=None)
    assert "Необходимы оба параметра: api_domain и api_key." in str(excinfo.value)


def test_presta_supplier_init_credentials_invalid_format():
    """Test PrestaSupplier initialization with invalid credentials format."""
    with pytest.raises(ValueError) as excinfo:
        PrestaSupplier(credentials="invalid")
    assert "Необходимы оба параметра: api_domain и api_key." in str(excinfo.value)

    

def test_presta_supplier_init_missing_both_credentials():
    """Test PrestaSupplier initialization with missing both credentials and separate params."""
    with pytest.raises(ValueError) as excinfo:
        PrestaSupplier()
    assert "Необходимы оба параметра: api_domain и api_key." in str(excinfo.value)

```