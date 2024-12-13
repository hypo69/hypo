```python
import pytest

from hypotez.src.endpoints.prestashop import (
    PrestaShop,
    PrestaProduct,
    PrestaSupplier,
    PrestaCategory,
    PrestaWarehouse,
    PrestaLanguage,
    PrestaShopShop,
    PriceListRequester,
    PrestaCustomer,
    MODE
)


def test_mode_is_dev():
    """
    Checks if the MODE variable is correctly set to 'dev'.
    """
    assert MODE == "dev"


def test_prestashop_import():
    """
    Checks if PrestaShop class is imported.
    """
    assert PrestaShop is not None


def test_presta_product_import():
    """
    Checks if PrestaProduct class is imported.
    """
    assert PrestaProduct is not None


def test_presta_supplier_import():
    """
    Checks if PrestaSupplier class is imported.
    """
    assert PrestaSupplier is not None


def test_presta_category_import():
    """
    Checks if PrestaCategory class is imported.
    """
    assert PrestaCategory is not None


def test_presta_warehouse_import():
    """
    Checks if PrestaWarehouse class is imported.
    """
    assert PrestaWarehouse is not None


def test_presta_language_import():
    """
    Checks if PrestaLanguage class is imported.
    """
    assert PrestaLanguage is not None


def test_presta_shop_shop_import():
    """
    Checks if PrestaShopShop class is imported.
    """
    assert PrestaShopShop is not None


def test_price_list_requester_import():
    """
    Checks if PriceListRequester class is imported.
    """
    assert PriceListRequester is not None


def test_presta_customer_import():
    """
    Checks if PrestaCustomer class is imported.
    """
    assert PrestaCustomer is not None
```