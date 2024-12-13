```python
import pytest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch, mock_open
from src.suppliers.aliexpress.campaign.html_generators import ProductHTMLGenerator, CategoryHTMLGenerator, CampaignHTMLGenerator

# Fixture for a sample product
@pytest.fixture
def sample_product():
    """Provides a sample product for testing."""
    return SimpleNamespace(
        product_id=123,
        product_title="Test Product",
        local_saved_image="images/test_image.jpg",
        target_sale_price=10.00,
        target_sale_price_currency="USD",
        target_original_price=20.00,
        target_original_price_currency="USD",
        second_level_category_name="Test Category",
        promotion_link="https://example.com/buy"
    )

# Fixture for a sample category path
@pytest.fixture
def sample_category_path(tmp_path):
    """Provides a sample category path for testing."""
    return tmp_path / "test_category"

# Fixture for a sample campaign path
@pytest.fixture
def sample_campaign_path(tmp_path):
    """Provides a sample campaign path for testing."""
    return tmp_path / "test_campaign"


# Tests for ProductHTMLGenerator.set_product_html
def test_set_product_html_valid_input(sample_product, sample_category_path):
    """Checks correct HTML generation for a single product with valid input."""
    ProductHTMLGenerator.set_product_html(sample_product, sample_category_path)
    html_file = sample_category_path / "html" / "123.html"
    assert html_file.exists()
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
        assert "<title>Test Product</title>" in html_content
        assert 'src="images/test_image.jpg"' in html_content
        assert 'class="product-price">10.0 USD</span>' in html_content
        assert 'class="product-original-price">20.0 USD</span>' in html_content
        assert 'class="product-category">Test Category</span>' in html_content
        assert 'href="https://example.com/buy"' in html_content

def test_set_product_html_with_html_chars(sample_category_path):
    """Checks correct HTML generation for product with special HTML characters in title."""
    product = SimpleNamespace(
        product_id=123,
        product_title="Test <Product>",
        local_saved_image="images/test_image.jpg",
        target_sale_price=10.00,
        target_sale_price_currency="USD",
        target_original_price=20.00,
        target_original_price_currency="USD",
        second_level_category_name="Test Category",
        promotion_link="https://example.com/buy"
    )
    ProductHTMLGenerator.set_product_html(product, sample_category_path)
    html_file = sample_category_path / "html" / "123.html"
    assert html_file.exists()
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
        assert "<title>Test &lt;Product&gt;</title>" in html_content
        assert 'alt="Test &lt;Product&gt;"' in html_content

def test_set_product_html_path_as_string(sample_product, tmp_path):
    """Checks if the function works when the path is given as string."""
    category_path_str = str(tmp_path / "test_category")
    ProductHTMLGenerator.set_product_html(sample_product, category_path_str)
    html_file = Path(category_path_str) / "html" / "123.html"
    assert html_file.exists()

def test_set_product_html_empty_product_title(sample_product, sample_category_path):
    """Checks HTML generation when product title is empty."""
    sample_product.product_title = ""
    ProductHTMLGenerator.set_product_html(sample_product, sample_category_path)
    html_file = sample_category_path / "html" / "123.html"
    assert html_file.exists()
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
        assert "<title></title>" in html_content


# Tests for CategoryHTMLGenerator.set_category_html
def test_set_category_html_valid_input(sample_product, sample_category_path):
    """Checks correct HTML generation for a category with valid input."""
    products_list = [sample_product, sample_product]
    CategoryHTMLGenerator.set_category_html(products_list, sample_category_path)
    html_file = sample_category_path / "html" / "index.html"
    assert html_file.exists()
    with open(html_file, 'r', encoding='utf-8') as f:
         html_content = f.read()
         assert "<title>test_category Products</title>" in html_content
         assert 'alt="Test Product"' in html_content
         assert 'class="product-price">10.0 USD</span>' in html_content
         assert 'class="product-original-price">20.0 USD</span>' in html_content
         assert 'class="product-category">Test Category</span>' in html_content
         assert 'href="https://example.com/buy"' in html_content

def test_set_category_html_single_product(sample_product, sample_category_path):
    """Checks HTML generation for a single product passed directly."""
    CategoryHTMLGenerator.set_category_html(sample_product, sample_category_path)
    html_file = sample_category_path / "html" / "index.html"
    assert html_file.exists()
    with open(html_file, 'r', encoding='utf-8') as f:
         html_content = f.read()
         assert "<title>test_category Products</title>" in html_content
         assert 'alt="Test Product"' in html_content
         assert 'class="product-price">10.0 USD</span>' in html_content
         assert 'class="product-original-price">20.0 USD</span>' in html_content
         assert 'class="product-category">Test Category</span>' in html_content
         assert 'href="https://example.com/buy"' in html_content

def test_set_category_html_empty_products_list(sample_category_path):
    """Checks HTML generation when the list of products is empty."""
    CategoryHTMLGenerator.set_category_html([], sample_category_path)
    html_file = sample_category_path / "html" / "index.html"
    assert html_file.exists()
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
        assert "<title>test_category Products</title>" in html_content
        assert '<div class="row product-grid">' in html_content
        assert '</div>' in html_content

def test_set_category_html_path_as_string(sample_product, tmp_path):
    """Checks if the function works when the path is given as string."""
    category_path_str = str(tmp_path / "test_category")
    CategoryHTMLGenerator.set_category_html([sample_product], category_path_str)
    html_file = Path(category_path_str) / "html" / "index.html"
    assert html_file.exists()

def test_set_category_html_with_html_chars(sample_category_path):
    """Checks correct HTML generation for product with special HTML characters in title and category."""
    product = SimpleNamespace(
        product_id=123,
        product_title="Test <Product>",
        local_saved_image="images/test_image.jpg",
        target_sale_price=10.00,
        target_sale_price_currency="USD",
        target_original_price=20.00,
        target_original_price_currency="USD",
        second_level_category_name="Test <Category>",
        promotion_link="https://example.com/buy"
    )
    CategoryHTMLGenerator.set_category_html([product], sample_category_path)
    html_file = sample_category_path / "html" / "index.html"
    assert html_file.exists()
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
        assert '<h5 class="card-title">Test &lt;Product&gt;</h5>' in html_content
        assert 'alt="Test &lt;Product&gt;"' in html_content
        assert 'class="product-category">Test &lt;Category&gt;</span>' in html_content

# Tests for CampaignHTMLGenerator.set_campaign_html
def test_set_campaign_html_valid_input(sample_campaign_path):
    """Checks correct HTML generation for a campaign with valid input."""
    categories = ["Category 1", "Category 2"]
    CampaignHTMLGenerator.set_campaign_html(categories, sample_campaign_path)
    html_file = sample_campaign_path / "index.html"
    assert html_file.exists()
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
        assert "<title>Campaign Overview</title>" in html_content
        assert '<a href="Category 1/index.html">Category 1</a>' in html_content
        assert '<a href="Category 2/index.html">Category 2</a>' in html_content

def test_set_campaign_html_empty_categories(sample_campaign_path):
    """Checks HTML generation when the list of categories is empty."""
    CampaignHTMLGenerator.set_campaign_html([], sample_campaign_path)
    html_file = sample_campaign_path / "index.html"
    assert html_file.exists()
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
        assert "<title>Campaign Overview</title>" in html_content
        assert '<ul class="list-group">' in html_content
        assert '</ul>' in html_content

def test_set_campaign_html_path_as_string(sample_campaign_path):
     """Checks if the function works when the path is given as string."""
     campaign_path_str = str(sample_campaign_path)
     categories = ["Category 1", "Category 2"]
     CampaignHTMLGenerator.set_campaign_html(categories, campaign_path_str)
     html_file = Path(campaign_path_str) / "index.html"
     assert html_file.exists()

def test_set_campaign_html_with_html_chars(sample_campaign_path):
    """Checks correct HTML generation for category with special HTML characters."""
    categories = ["Category <1>", "Category <2>"]
    CampaignHTMLGenerator.set_campaign_html(categories, sample_campaign_path)
    html_file = sample_campaign_path / "index.html"
    assert html_file.exists()
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
        assert '<a href="Category &lt;1&gt;/index.html">Category &lt;1&gt;</a>' in html_content
        assert '<a href="Category &lt;2&gt;/index.html">Category &lt;2&gt;</a>' in html_content
```