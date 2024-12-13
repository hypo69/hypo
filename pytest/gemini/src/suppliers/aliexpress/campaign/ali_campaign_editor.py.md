```python
import pytest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch, mock_open
from src.suppliers.aliexpress.campaign.ali_campaign_editor import AliCampaignEditor
from src.logger.logger import logger
from src.utils.file import read_text_file, save_text_file
from src.utils.jjson import j_loads, j_dumps, j_loads_ns


@pytest.fixture
def mock_ali_campaign_editor():
    """Fixture to create a mock AliCampaignEditor instance."""
    with patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.__init__", return_value=None):
        editor = AliCampaignEditor(campaign_name="test_campaign", language="EN", currency="USD")
        editor.base_path = Path("/test/path")
        editor.language = "EN"
        editor.currency = "USD"
        editor.campaign = SimpleNamespace(category=SimpleNamespace(test_category=SimpleNamespace(description="Test category")))
        editor.category_path = Path("/test/path/category/test_category/EN_USD")
        return editor

@pytest.fixture
def mock_product_data():
    return {"product_id": "12345", "title": "Test Product", "price": 100}

def test_ali_campaign_editor_initialization(mock_ali_campaign_editor):
    """Checks if the AliCampaignEditor initializes correctly."""
    assert mock_ali_campaign_editor.campaign_name == "test_campaign"
    assert mock_ali_campaign_editor.language == "EN"
    assert mock_ali_campaign_editor.currency == "USD"
    assert mock_ali_campaign_editor.base_path == Path("/test/path")
    assert hasattr(mock_ali_campaign_editor.campaign, "category")

def test_delete_product_with_affiliate_link(mock_ali_campaign_editor, tmp_path):
    """Checks deleting a product by ID that is found with an affiliate link."""
    product_path = tmp_path / "sources.txt"
    product_path.write_text("12345\n67890")
    mock_ali_campaign_editor.category_path = tmp_path
    
    mock_ali_campaign_editor.delete_product("12345")
    
    assert read_text_file(tmp_path / "_sources.txt") == ["67890"]
    
    
def test_delete_product_no_affiliate_link(mock_ali_campaign_editor, tmp_path):
    """Checks deleting a product by ID when the ID is not found with an affiliate link."""
    product_path = tmp_path / "sources.txt"
    product_path.write_text("12345\n67890")
    mock_ali_campaign_editor.category_path = tmp_path

    mock_ali_campaign_editor.delete_product("54321")
    
    assert read_text_file(tmp_path / "sources.txt") == ['12345', '67890']
    
def test_delete_product_no_sources_file(mock_ali_campaign_editor, tmp_path):
    """Checks renaming of product html file if no `sources.txt` found."""
    product_path = tmp_path / "sources"
    product_path.mkdir(exist_ok=True)
    product_file = product_path / "12345.html"
    product_file.touch()
    mock_ali_campaign_editor.category_path = tmp_path
    
    mock_ali_campaign_editor.delete_product("12345")
    
    assert (tmp_path / "sources" / "12345_.html").exists()
    
    
def test_delete_product_no_sources_file_not_found(mock_ali_campaign_editor, tmp_path, caplog):
    """Checks logging when the file to be deleted does not exist and no `sources.txt` found."""
    mock_ali_campaign_editor.category_path = tmp_path
    with caplog.at_level("ERROR"):
        mock_ali_campaign_editor.delete_product("12345")
    
    assert "not found" in caplog.text

def test_delete_product_exception(mock_ali_campaign_editor, tmp_path, caplog):
    """Checks exception handling during product deletion."""
    mock_ali_campaign_editor.category_path = tmp_path
    with patch("pathlib.Path.rename", side_effect=Exception("Rename error")):
        with caplog.at_level("CRITICAL"):
            mock_ali_campaign_editor.delete_product("12345")
    assert "An error occurred while deleting the product file" in caplog.text

def test_update_product(mock_ali_campaign_editor, mock_product_data, tmp_path):
    """Checks that update_product calls dump_category_products_files."""
    with patch.object(mock_ali_campaign_editor, "dump_category_products_files") as mock_dump:
        mock_ali_campaign_editor.update_product("test_category", "EN", mock_product_data)
    mock_dump.assert_called_once_with("test_category", "EN", mock_product_data)

def test_update_campaign(mock_ali_campaign_editor):
    """Checks that update_campaign method can be called."""
    mock_ali_campaign_editor.update_campaign()

def test_update_category_success(mock_ali_campaign_editor, tmp_path):
    """Checks successful update of a category."""
    category = SimpleNamespace(name="Test Category", description="Test Description")
    json_path = tmp_path / "test_category.json"
    j_dumps({"category": {"old_name": "Old Category", "old_description": "Old Description"}}, json_path)
    
    result = mock_ali_campaign_editor.update_category(json_path, category)
    
    assert result is True
    updated_data = j_loads(json_path)
    assert updated_data["category"]["name"] == "Test Category"
    assert updated_data["category"]["description"] == "Test Description"

def test_update_category_failure(mock_ali_campaign_editor, tmp_path, caplog):
    """Checks failure of category update due to exception."""
    category = SimpleNamespace(name="Test Category", description="Test Description")
    json_path = tmp_path / "test_category.json"
    
    with patch("src.utils.jjson.j_loads", side_effect=Exception("Load error")):
        with caplog.at_level("ERROR"):
            result = mock_ali_campaign_editor.update_category(json_path, category)
            
    assert result is False
    assert "Failed to update category" in caplog.text

def test_get_category_found(mock_ali_campaign_editor):
    """Checks retrieval of an existing category."""
    category = mock_ali_campaign_editor.get_category("test_category")
    assert category.description == "Test category"

def test_get_category_not_found(mock_ali_campaign_editor, caplog):
    """Checks retrieval of a non-existent category."""
    with caplog.at_level("WARNING"):
        category = mock_ali_campaign_editor.get_category("non_existent_category")
    assert category is None
    assert "not found in the campaign" in caplog.text

def test_get_category_exception(mock_ali_campaign_editor, caplog):
     """Checks exception handling during category retrieval."""
     with patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.__getattribute__", side_effect=Exception("Get attribute error")):
        with caplog.at_level("ERROR"):
            category = mock_ali_campaign_editor.get_category("test_category")
        assert category is None
        assert "Error retrieving category" in caplog.text

def test_list_categories_found(mock_ali_campaign_editor):
    """Checks retrieval of existing categories."""
    mock_ali_campaign_editor.campaign.category = SimpleNamespace(
        cat1 = SimpleNamespace(name = "cat1"),
        cat2 = SimpleNamespace(name = "cat2")
    )
    categories = mock_ali_campaign_editor.list_categories
    assert categories == ["cat1", "cat2"]

def test_list_categories_not_found(mock_ali_campaign_editor, caplog):
    """Checks retrieval when no categories are found."""
    mock_ali_campaign_editor.campaign.category = None
    with caplog.at_level("WARNING"):
         categories = mock_ali_campaign_editor.list_categories
    assert categories is None
    assert "No categories found in the campaign." in caplog.text

def test_list_categories_exception(mock_ali_campaign_editor, caplog):
    """Checks exception handling during categories list retrieval."""
    with patch("src.suppliers.aliexpress.campaign.ali_promo_campaign.AliPromoCampaign.__getattribute__", side_effect=Exception("Attribute Error")):
        with caplog.at_level("ERROR"):
            categories = mock_ali_campaign_editor.list_categories
    assert categories is None
    assert "Error retrieving categories list" in caplog.text

def test_get_category_products_success(mock_ali_campaign_editor, tmp_path):
    """Checks successful retrieval of products from category JSON files."""
    category_path = tmp_path / "category" / "test_category" / "EN_USD"
    category_path.mkdir(parents=True, exist_ok=True)
    (category_path / "product1.json").write_text('{"product_id": "1", "title": "Product 1"}')
    (category_path / "product2.json").write_text('{"product_id": "2", "title": "Product 2"}')
    mock_ali_campaign_editor.base_path = tmp_path
    
    products = mock_ali_campaign_editor.get_category_products("test_category")

    assert len(products) == 2
    assert products[0].product_id == "1"
    assert products[1].product_id == "2"
    
def test_get_category_products_no_files(mock_ali_campaign_editor, tmp_path, caplog):
    """Checks behavior when no JSON files are found for a category."""
    mock_ali_campaign_editor.base_path = tmp_path
    with patch.object(mock_ali_campaign_editor, "process_category_products") as mock_process:
        with caplog.at_level("ERROR"):
            products = mock_ali_campaign_editor.get_category_products("test_category")
        mock_process.assert_called_once_with("test_category")
    assert products is None
    assert "No JSON files found for category_name" in caplog.text

```