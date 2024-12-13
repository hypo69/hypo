```python
import pytest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch, mock_open
import asyncio
import copy
import json

from hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign import AliPromoCampaign
from hypotez.src import gs


# Mocking gs.path and other dependencies for tests
@pytest.fixture(autouse=True)
def mock_gs_path(monkeypatch):
    monkeypatch.setattr(gs, "path", SimpleNamespace(
        google_drive=Path("/mocked/google_drive"),
        src=Path("/mocked/src")
    ))
    monkeypatch.setattr(gs, "now", "test_time")
    monkeypatch.setattr(gs, "credentials", SimpleNamespace(
        openai=SimpleNamespace(assistant=SimpleNamespace(category_descriptions="test_assistant_id"))
    ))
    monkeypatch.setattr(gs.path, 'temp', Path('/tmp/test_temp'))
    
    # Mock logger
    def mock_logger_info(msg, *args, **kwargs):
      print(f'INFO: {msg}')
    def mock_logger_warning(msg, *args, **kwargs):
        print(f'WARNING: {msg}')
    def mock_logger_error(msg, *args, **kwargs):
      print(f'ERROR: {msg}')
    monkeypatch.setattr('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.logger.info', mock_logger_info)
    monkeypatch.setattr('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.logger.warning', mock_logger_warning)
    monkeypatch.setattr('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.logger.error', mock_logger_error)
    
    
    
@pytest.fixture
def mock_read_text_file(monkeypatch):
    def mock_read(path, as_list=False, exc_info=True):
        if 'system_instruction.txt' in str(path):
            return "Mocked system instruction"
        elif "product_titles.txt" in str(path):
            return ["product1", "product2"] if as_list else "product1\nproduct2"
        elif "sources.txt" in str(path):
            return ["https://example.com/product/123", "https://example.com/product/456"] if as_list else "https://example.com/product/123\nhttps://example.com/product/456"
        return ""
    monkeypatch.setattr('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.read_text_file', mock_read)


@pytest.fixture
def mock_j_loads_ns(monkeypatch):
    def mock_load(path, exc_info=False):
        if isinstance(path, Path) and "EN_USD.json" in str(path):
            return SimpleNamespace(
                language="EN",
                currency="USD",
                category=SimpleNamespace(
                    electronics=SimpleNamespace(
                        category_name="electronics", title="Electronics", description="Test Description"
                    ),
                    clothing = SimpleNamespace(
                        category_name="clothing", title="Clothing", description="Test Clothing Description"
                    )
                )
            )
        return None
    monkeypatch.setattr('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.j_loads_ns', mock_load)

@pytest.fixture
def mock_j_dumps(monkeypatch):
  def mock_dump(data, path, exc_info = True):
    print(f"JSON dump: {data=}, {path=}")
    return "JSON dumped string"
  monkeypatch.setattr('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.j_dumps', mock_dump)

@pytest.fixture
def mock_get_directory_names(monkeypatch):
    def mock_get_dirs(path):
        if "category" in str(path):
            return ["electronics", "clothing"]
        return []
    monkeypatch.setattr('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.get_directory_names', mock_get_dirs)

@pytest.fixture
def mock_get_filenames(monkeypatch):
  def mock_get_files(path, extensions, exc_info=False):
    if "sources" in str(path):
      return [Path("/mocked/google_drive/aliexpress/campaigns/test_campaign/category/electronics/sources/123.html"),
              Path("/mocked/google_drive/aliexpress/campaigns/test_campaign/category/electronics/sources/456.html")]
    if 'category' in str(path):
       return [Path("/mocked/google_drive/aliexpress/campaigns/test_campaign/category/electronics"), 
                Path("/mocked/google_drive/aliexpress/campaigns/test_campaign/category/clothing")] 
    return []
  monkeypatch.setattr('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.get_filenames', mock_get_files)

@pytest.fixture
def mock_extract_prod_ids(monkeypatch):
  def mock_extract(data):
    if isinstance(data, list) and any('html' in str(item) for item in data):
        return ["123", "456"]
    elif isinstance(data, list):
      return ["123", "456"]
    return []
  monkeypatch.setattr('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.extract_prod_ids', mock_extract)

@pytest.fixture
def mock_ali_affiliated_products(monkeypatch):
  async def mock_process_affiliate_products(prod_ids, category_root):
    return [SimpleNamespace(product_id="123", product_title="Test Product", promotion_link="https://example.com/product/123")]
  
  monkeypatch.setattr('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.AliAffiliatedProducts',
                     lambda language, currency: SimpleNamespace(process_affiliate_products = mock_process_affiliate_products)
                     )

@pytest.fixture
def mock_save_text_file(monkeypatch):
  def mock_save(content, path, exc_info = True):
    print(f"Save text file: {content=}, {path=}")
    return None
  monkeypatch.setattr('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.save_text_file', mock_save)

@pytest.fixture
def mock_google_generative_ai(monkeypatch):
  def mock_ask(prompt):
    return json.dumps({
      "electronics": {
      "title": "Electronics Category AI",
      "description": "AI generated description for electronics",
      },
       "clothing": {
      "title": "Clothing Category AI",
      "description": "AI generated description for clothing",
      }
    })
  monkeypatch.setattr('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.GoogleGenerativeAI', 
                    lambda system_instruction: SimpleNamespace(ask=mock_ask)
                    )

@pytest.fixture
def mock_openai_model(monkeypatch):
  def mock_ask(prompt):
     return json.dumps({
      "electronics": {
      "title": "Electronics Category AI",
      "description": "AI generated description for electronics",
      },
       "clothing": {
      "title": "Clothing Category AI",
      "description": "AI generated description for clothing",
      }
    })
  monkeypatch.setattr('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.OpenAIModel', 
                     lambda system_instruction, assistant_id: SimpleNamespace(ask=mock_ask)
                     )
# Test cases
def test_ali_promo_campaign_init_existing_campaign(mock_j_loads_ns, mock_read_text_file, mock_google_generative_ai):
    """Test initialization with an existing campaign file."""
    campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
    assert campaign.campaign_name == "test_campaign"
    assert campaign.language == "EN"
    assert campaign.currency == "USD"
    assert campaign.campaign.language == "EN"
    assert campaign.campaign.currency == "USD"
    assert campaign.gemini is not None
    #assert campaign.openai is not None


def test_ali_promo_campaign_init_new_campaign(mock_j_loads_ns, mock_read_text_file, mock_google_generative_ai, mock_get_directory_names, mock_extract_prod_ids, mock_ali_affiliated_products, mock_j_dumps):
    """Test initialization with a new campaign (no existing JSON file)."""
    campaign = AliPromoCampaign(campaign_name="new_campaign", language="EN", currency="USD")
    assert campaign.campaign_name == "new_campaign"
    assert campaign.language == "EN"
    assert campaign.currency == "USD"
    assert hasattr(campaign.campaign, 'category')
    assert campaign.gemini is not None
    #assert campaign.openai is not None

def test_ali_promo_campaign_init_new_campaign_no_locale(mock_j_loads_ns, mock_read_text_file, mock_google_generative_ai, mock_get_directory_names, mock_extract_prod_ids, mock_ali_affiliated_products, mock_j_dumps):
    """Test initialization with a new campaign (no existing JSON file)."""
    campaign = AliPromoCampaign(campaign_name="new_campaign")
    assert campaign.campaign_name == "new_campaign"
    assert campaign.language == "EN"
    assert campaign.currency == "USD"
    assert hasattr(campaign.campaign, 'category')
    assert campaign.gemini is not None
    #assert campaign.openai is not None


def test_models_payload(mock_read_text_file, mock_google_generative_ai):
    """Test the _models_payload method."""
    campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
    assert campaign.gemini is not None
    #assert campaign.openai is not None

def test_process_campaign(mock_get_directory_names, mock_ali_affiliated_products, mock_google_generative_ai, mock_read_text_file, mock_extract_prod_ids, mock_j_dumps):
    """Test the process_campaign method."""
    campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
    campaign.process_campaign()
    
def test_process_campaign_category(mock_ali_affiliated_products, mock_google_generative_ai, mock_read_text_file, mock_extract_prod_ids, mock_j_dumps):
    """Test the process_campaign_category method."""
    campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
    campaign.process_campaign_category(category_name="electronics")
    
    
def test_process_new_campaign(mock_get_directory_names, mock_ali_affiliated_products, mock_j_dumps, mock_read_text_file, mock_extract_prod_ids):
  """Test the process_new_campaign method."""
  campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
  campaign.process_new_campaign(campaign_name="test_campaign", language="EN", currency="USD")
  assert campaign.language == "EN"
  assert campaign.currency == "USD"
  assert hasattr(campaign.campaign, 'category')
  assert hasattr(campaign, 'campaign_ai')

def test_process_new_campaign_no_locale(mock_get_directory_names, mock_ali_affiliated_products, mock_j_dumps, mock_read_text_file, mock_extract_prod_ids):
  """Test the process_new_campaign method."""
  campaign = AliPromoCampaign(campaign_name="test_campaign")
  campaign.process_new_campaign(campaign_name="test_campaign")
  assert campaign.language == "EN"
  assert campaign.currency == "USD"
  assert hasattr(campaign.campaign, 'category')
  assert hasattr(campaign, 'campaign_ai')


def test_process_ai_category(mock_google_generative_ai, mock_read_text_file, mock_j_dumps):
    """Test the process_ai_category method."""
    campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
    campaign.campaign = SimpleNamespace(
        language="EN",
        currency="USD",
        category=SimpleNamespace(
            electronics=SimpleNamespace(
                category_name="electronics", title="Electronics", description="Test Description"
            ),
             clothing=SimpleNamespace(
                category_name="clothing", title="Clothing", description="Test Description"
            )
        )
    )
    campaign.process_ai_category(category_name="electronics")
    assert hasattr(campaign.campaign_ai, "category")
    assert hasattr(campaign.campaign_ai.category, "electronics")
    assert hasattr(campaign.campaign_ai.category.electronics, "title")


def test_process_ai_category_no_category(mock_google_generative_ai, mock_read_text_file, mock_j_dumps):
  """Test the process_ai_category method without category_name."""
  campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
  campaign.campaign = SimpleNamespace(
        language="EN",
        currency="USD",
        category=SimpleNamespace(
            electronics=SimpleNamespace(
                category_name="electronics", title="Electronics", description="Test Description"
            ),
            clothing=SimpleNamespace(
                category_name="clothing", title="Clothing", description="Test Description"
            )
        )
    )
  campaign.process_ai_category()
  assert hasattr(campaign.campaign_ai, "category")
  assert hasattr(campaign.campaign_ai.category, "electronics")
  assert hasattr(campaign.campaign_ai.category.electronics, "title")
  assert hasattr(campaign.campaign_ai.category, "clothing")
  assert hasattr(campaign.campaign_ai.category.clothing, "title")

def test_process_category_products_no_products(mock_read_text_file):
  """Test process_category_products method with no products found"""
  campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
  products = campaign.process_category_products(category_name="electronics")
  assert products is None

def test_process_category_products(mock_read_text_file, mock_extract_prod_ids, mock_ali_affiliated_products):
    """Test process_category_products method with valid data."""
    campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
    products = campaign.process_category_products(category_name="electronics")
    assert products is not None
    assert isinstance(products, list)
    assert len(products) > 0

def test_dump_category_products_files(mock_j_dumps):
    """Test the dump_category_products_files method."""
    campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
    products = [SimpleNamespace(product_id="123", product_title="Test Product")]
    campaign.dump_category_products_files(category_name="electronics", products=products)
    
def test_dump_category_products_files_no_products(mock_j_dumps):
  """Test the dump_category_products_files method with no products."""
  campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
  products = []
  campaign.dump_category_products_files(category_name="electronics", products=products)
  
def test_dump_category_products_files_no_product_id(mock_j_dumps):
    """Test the dump_category_products_files method with no product_id."""
    campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
    products = [SimpleNamespace(product_title="Test Product")]
    campaign.dump_category_products_files(category_name="electronics", products=products)


def test_set_categories_from_directories(mock_get_directory_names):
    """Test the set_categories_from_directories method."""
    campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
    campaign.set_categories_from_directories()
    assert hasattr(campaign.campaign.category, "electronics")
    assert hasattr(campaign.campaign.category, "clothing")
    assert campaign.campaign.category.electronics.category_name == "electronics"
    assert campaign.campaign.category.clothing.category_name == "clothing"
    assert campaign.campaign.category.electronics.title == ""


@pytest.mark.asyncio
async def test_generate_output(mock_save_text_file, mock_j_dumps):
    """Test the generate_output method."""
    campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
    products_list = [
        SimpleNamespace(
            product_id="123",
            product_title="Product A",
            promotion_link="http://example.com/product_a",
            first_level_category_id=1,
            first_level_category_name="Category1",
            second_level_category_id=2,
            second_level_category_name="Subcategory1",
            product_main_image_url="http://example.com/image.png",
            product_video_url="http://example.com/video.mp4",
             target_sale_price= 100,
             target_sale_price_currency= "USD",
            target_original_price = 120,
            target_original_price_currency = "USD",
            local_saved_image = "/mocked/google_drive/aliexpress/campaigns/test_campaign/category/electronics/123.png"
        ),
         SimpleNamespace(
            product_id="124",
            product_title="Product B",
            promotion_link="http://example.com/product_b",
            first_level_category_id=1,
            first_level_category_name="Category1",
            second_level_category_id=3,
            second_level_category_name="Subcategory2",
            product_main_image_url="http://example.com/image.png",
            product_video_url="http://example.com/video.mp4",
            target_sale_price= 200,
            target_sale_price_currency= "USD",
            target_original_price = 220,
            target_original_price_currency = "USD",
            local_saved_image = "/mocked/google_drive/aliexpress/campaigns/test_campaign/category/electronics/124.png"
        )
    ]
    await campaign.generate_output(campaign_name="test_campaign", category_path=Path("/mocked/google_drive/aliexpress/campaigns/test_campaign/category/electronics"), products_list=products_list)

@pytest.mark.asyncio
async def test_generate_output_single_product(mock_save_text_file, mock_j_dumps):
    """Test the generate_output method with single product."""
    campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
    product = SimpleNamespace(
            product_id="123",
            product_title="Product A",
            promotion_link="http://example.com/product_a",
            first_level_category_id=1,
            first_level_category_name="Category1",
            second_level_category_id=2,
            second_level_category_name="Subcategory1",
            product_main_image_url="http://example.com/image.png",
            product_video_url="http://example.com/video.mp4",
             target_sale_price= 100,
             target_sale_price_currency= "USD",
            target_original_price = 120,
            target_original_price_currency = "USD",
            local_saved_image = "/mocked/google_drive/aliexpress/campaigns/test_campaign/category/electronics/123.png"
        )
    await campaign.generate_output(campaign_name="test_campaign", category_path=Path("/mocked/google_drive/aliexpress/campaigns/test_campaign/category/electronics"), products_list=product)

@pytest.mark.asyncio
async def test_generate_html(mock_save_text_file, mock_get_directory_names):
  """Test the generate_html method."""
  campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
  products_list = [
        SimpleNamespace(
            product_id="123",
            product_title="Product A",
            promotion_link="http://example.com/product_a",
            first_level_category_id=1,
            first_level_category_name="Category1",
            second_level_category_id=2,
            second_level_category_name="Subcategory1",
            product_main_image_url="http://example.com/image.png",
            product_video_url="http://example.com/video.mp4",
            target_sale_price= 100,
             target_sale_price_currency= "USD",
            target_original_price = 120,
            target_original_price_currency = "USD",
            local_saved_image = "/mocked/google_drive/aliexpress/campaigns/test_campaign/category/electronics/123.png"
        ),
         SimpleNamespace(
            product_id="124",
            product_title="Product B",
            promotion_link="http://example.com/product_b",
            first_level_category_id=1,
            first_level_category_name="Category1",
            second_level_category_id=3,
            second_level_category_name="Subcategory2",
            product_main_image_url="http://example.com/image.png",
            product_video_url="http://example.com/video.mp4",
             target_sale_price= 200,
             target_sale_price_currency= "USD",
            target_original_price = 220,
            target_original_price_currency = "USD",
            local_saved_image = "/mocked/google_drive/aliexpress/campaigns/test_campaign/category/electronics/124.png"
        )
    ]
  await campaign.generate_html(campaign_name="test_campaign", category_path=Path("/mocked/google_drive/aliexpress/campaigns/test_campaign/category/electronics"), products_list=products_list)

@pytest.mark.asyncio
async def test_generate_html_single_product(mock_save_text_file, mock_get_directory_names):
    """Test the generate_html method with a single product."""
    campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
    product = SimpleNamespace(
            product_id="123",
            product_title="Product A",
            promotion_link="http://example.com/product_a",
            first_level_category_id=1,
            first_level_category_name="Category1",
            second_level_category_id=2,
            second_level_category_name="Subcategory1",
            product_main_image_url="http://example.com/image.png",
            product_video_url="http://example.com/video.mp4",
            target_sale_price= 100,
            target_sale_price_currency= "USD",
            target_original_price = 120,
            target_original_price_currency = "USD",
            local_saved_image = "/mocked/google_drive/aliexpress/campaigns/test_campaign/category/electronics/123.png"
        )
    await campaign.generate_html(campaign_name="test_campaign", category_path=Path("/mocked/google_drive/aliexpress/campaigns/test_campaign/category/electronics"), products_list=product)


def test_generate_html_for_campaign(mock_get_filenames):
    """Test the generate_html_for_campaign method."""
    campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
    with patch('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.ProductHTMLGenerator.set_product_html') as mock_set_product_html, \
         patch('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.CategoryHTMLGenerator.set_category_html') as mock_set_category_html, \
        patch('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.CampaignHTMLGenerator.set_campaign_html') as mock_set_campaign_html, \
        patch.object(AliPromoCampaign, 'get_category_products', return_value=[SimpleNamespace(product_id="123")]):
        campaign.generate_html_for_campaign(campaign_name="test_campaign")
        mock_set_product_html.assert_called()
        mock_set_category_html.assert_called()
        mock_set_campaign_html.assert_called()
        
def test_generate_html_for_campaign_no_products(mock_get_filenames):
    """Test the generate_html_for_campaign method with no products."""
    campaign = AliPromoCampaign(campaign_name="test_campaign", language="EN", currency="USD")
    with patch('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.ProductHTMLGenerator.set_product_html') as mock_set_product_html, \
         patch('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.CategoryHTMLGenerator.set_category_html') as mock_set_category_html, \
        patch('hypotez.src.suppliers.aliexpress.campaign.ali_promo_campaign.CampaignHTMLGenerator.set_campaign_html') as mock_set_campaign_html, \
        patch.object(AliPromoCampaign, 'get_category_products', return_value=None):
            campaign.generate_html_for_campaign(campaign_name="test_campaign")
            mock_set_product_html.assert_not_called()
            mock_set_category_html.assert_not_called()
            mock_set_campaign_html.assert_called()
```