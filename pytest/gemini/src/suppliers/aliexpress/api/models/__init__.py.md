```python
import pytest

from hypotez.src.suppliers.aliexpress.api.models import (
    Language,
    Currency,
    ProductType,
    SortBy,
    LinkType,
    AffiliateLink,
    HotProductsResponse,
    Product,
    Category,
    ChildCategory
)


def test_language_enum_members():
    """
    Test that the Language enum has expected members and values.
    """
    assert Language.EN == "en"
    assert Language.RU == "ru"
    assert Language.PT == "pt"


def test_currency_enum_members():
    """
    Test that the Currency enum has expected members and values.
    """
    assert Currency.USD == "USD"
    assert Currency.RUB == "RUB"
    assert Currency.EUR == "EUR"
    assert Currency.BRL == "BRL"


def test_product_type_enum_members():
    """
    Test that the ProductType enum has expected members and values.
    """
    assert ProductType.HOT_PRODUCTS == "hotproducts"
    assert ProductType.PRODUCTS == "products"


def test_sort_by_enum_members():
    """
    Test that the SortBy enum has expected members and values.
    """
    assert SortBy.RELEVANCE == "relevance"
    assert SortBy.PRICE_ASC == "price-asc"
    assert SortBy.PRICE_DESC == "price-desc"
    assert SortBy.ORDERS_DESC == "orders-desc"
    assert SortBy.NEWEST == "newest"


def test_link_type_enum_members():
    """
    Test that the LinkType enum has expected members and values.
    """
    assert LinkType.AFFILIATE == "affiliate"
    assert LinkType.NORMAL == "normal"


def test_affiliate_link_model_creation():
    """
    Test the creation of AffiliateLink instance.
    """
    link = AffiliateLink(
        promotion_url="http://example.com/promo",
        tracking_id="12345",
        commission_rate=0.05,
        source="test",
        landing_page="http://example.com/product",
    )
    assert link.promotion_url == "http://example.com/promo"
    assert link.tracking_id == "12345"
    assert link.commission_rate == 0.05
    assert link.source == "test"
    assert link.landing_page == "http://example.com/product"


def test_hot_products_response_model_creation():
    """
    Test the creation of HotProductsResponse instance.
    """
    hot_products_response = HotProductsResponse(
        total_results=10,
        products=[
            {"id": 1, "title": "Product 1"},
            {"id": 2, "title": "Product 2"}
        ]
    )
    assert hot_products_response.total_results == 10
    assert len(hot_products_response.products) == 2
    assert hot_products_response.products[0]["id"] == 1
    assert hot_products_response.products[1]["title"] == "Product 2"

def test_product_model_creation():
    """
    Test the creation of Product instance.
    """
    product_data = {
        "productId": 123,
        "title": "Test Product",
        "imageUrl": "http://example.com/image.jpg",
        "price": 10.00,
        "originalPrice": 12.00,
        "discount": 0.15,
        "orders": 100,
        "rating": 4.5
    }

    product = Product(**product_data)

    assert product.productId == 123
    assert product.title == "Test Product"
    assert product.imageUrl == "http://example.com/image.jpg"
    assert product.price == 10.00
    assert product.originalPrice == 12.00
    assert product.discount == 0.15
    assert product.orders == 100
    assert product.rating == 4.5

def test_category_model_creation():
    """
    Test the creation of Category instance.
    """
    category_data = {
        "id": 1,
        "name": "Electronics",
        "children": [
            {"id": 10, "name": "Phones"},
            {"id": 11, "name": "Tablets"},
        ]
    }

    category = Category(**category_data)
    assert category.id == 1
    assert category.name == "Electronics"
    assert len(category.children) == 2
    assert isinstance(category.children[0], ChildCategory)
    assert category.children[0].id == 10
    assert category.children[0].name == "Phones"

def test_child_category_model_creation():
    """
    Test the creation of ChildCategory instance.
    """
    child_category = ChildCategory(id=10, name="Phones")
    assert child_category.id == 10
    assert child_category.name == "Phones"
```