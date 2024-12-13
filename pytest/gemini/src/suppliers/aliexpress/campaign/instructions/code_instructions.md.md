```python
import pytest
import os
import json
from unittest.mock import patch

# Mock functions for testing
def create_directories(campaign_name, categories):
    os.makedirs(os.path.join(campaign_name, "data"), exist_ok=True)
    for category in categories:
        os.makedirs(os.path.join(campaign_name, "data", category), exist_ok=True)

def save_config(campaign_name, campaign_config):
    with open(os.path.join(campaign_name, "config.json"), "w") as f:
        json.dump(campaign_config, f)

def load_config(campaign_name):
     try:
        with open(os.path.join(campaign_name, "config.json"), "r") as f:
            return json.load(f)
     except FileNotFoundError:
         return {}


def collect_product_data(product_urls):
    return [{"url": url, "title": f"Product {i}"} for i, url in enumerate(product_urls)]

def save_product_data(campaign_name, product_data):
    with open(os.path.join(campaign_name, "products.json"), "w") as f:
        json.dump(product_data, f)

def create_promotional_materials(campaign_name, product_data):
    with open(os.path.join(campaign_name, "promotional_materials.txt"), "w") as f:
      for item in product_data:
        f.write(f"Promotional material for {item['title']}\n")

def update_promotional_materials(campaign_name, product_data):
    with open(os.path.join(campaign_name, "promotional_materials.txt"), "a") as f:
        for item in product_data:
          f.write(f"Updated material for {item['title']}\n")

def review_campaign(campaign_name):
    pass
def publish_campaign(campaign_name):
    pass
def update_categories(campaign_name, categories):
    for category in categories:
      os.makedirs(os.path.join(campaign_name, "data", category), exist_ok=True)

def create_campaign(campaign_name, language, currency, categories, product_urls):
    create_directories(campaign_name, categories)
    campaign_config = {'name': campaign_name, 'language': language, 'currency': currency}
    save_config(campaign_name, campaign_config)
    product_data = collect_product_data(product_urls)
    save_product_data(campaign_name, product_data)
    create_promotional_materials(campaign_name, product_data)
    review_campaign(campaign_name)
    publish_campaign(campaign_name)

def edit_campaign(campaign_name, language, categories, product_urls):
    campaign_config = load_config(campaign_name)
    campaign_config['language'] = language
    save_config(campaign_name, campaign_config)
    update_categories(campaign_name, categories)
    updated_product_data = collect_product_data(product_urls)
    save_product_data(campaign_name, updated_product_data)
    update_promotional_materials(campaign_name, updated_product_data)
    review_campaign(campaign_name)
    publish_campaign(campaign_name)

# Fixture for creating a test campaign directory
@pytest.fixture
def test_campaign_dir():
    campaign_name = "test_campaign"
    os.makedirs(campaign_name, exist_ok=True)
    yield campaign_name
    os.remove(os.path.join(campaign_name, "config.json"))
    os.remove(os.path.join(campaign_name, "products.json"))
    os.remove(os.path.join(campaign_name, "promotional_materials.txt"))
    os.removedirs(os.path.join(campaign_name,"data"))
    os.rmdir(campaign_name)

# Tests for create_directories
def test_create_directories_valid_input(test_campaign_dir):
    """Checks if directories are created correctly with valid input."""
    campaign_name = test_campaign_dir
    categories = ["electronics", "fashion"]
    create_directories(campaign_name, categories)
    assert os.path.exists(os.path.join(campaign_name, "data"))
    for category in categories:
      assert os.path.exists(os.path.join(campaign_name, "data", category))

def test_create_directories_empty_categories(test_campaign_dir):
    """Checks if it works fine with empty category list"""
    campaign_name = test_campaign_dir
    categories = []
    create_directories(campaign_name, categories)
    assert os.path.exists(os.path.join(campaign_name, "data"))

def test_create_directories_already_exists(test_campaign_dir):
    """Checks if it works fine if directories already exists"""
    campaign_name = test_campaign_dir
    categories = ["electronics", "fashion"]
    os.makedirs(os.path.join(campaign_name, "data"), exist_ok=True)
    for category in categories:
        os.makedirs(os.path.join(campaign_name, "data", category), exist_ok=True)
    create_directories(campaign_name, categories)
    assert os.path.exists(os.path.join(campaign_name, "data"))
    for category in categories:
      assert os.path.exists(os.path.join(campaign_name, "data", category))

# Tests for save_config
def test_save_config_valid_data(test_campaign_dir):
    """Checks if configuration is saved correctly."""
    campaign_name = test_campaign_dir
    campaign_config = {'name': 'test_campaign', 'language': 'EN', 'currency': 'USD'}
    save_config(campaign_name, campaign_config)
    with open(os.path.join(campaign_name, "config.json"), "r") as f:
        saved_config = json.load(f)
    assert saved_config == campaign_config

def test_save_config_empty_data(test_campaign_dir):
    """Checks if it works fine with empty config"""
    campaign_name = test_campaign_dir
    campaign_config = {}
    save_config(campaign_name, campaign_config)
    with open(os.path.join(campaign_name, "config.json"), "r") as f:
        saved_config = json.load(f)
    assert saved_config == campaign_config

def test_save_config_overwrite_data(test_campaign_dir):
    """Checks if data can be overwritten."""
    campaign_name = test_campaign_dir
    campaign_config = {'name': 'test_campaign', 'language': 'EN', 'currency': 'USD'}
    save_config(campaign_name, campaign_config)
    new_config = {'name': 'new_name', 'language': 'RU', 'currency': 'EUR'}
    save_config(campaign_name, new_config)
    with open(os.path.join(campaign_name, "config.json"), "r") as f:
        saved_config = json.load(f)
    assert saved_config == new_config

# Tests for load_config
def test_load_config_existing_file(test_campaign_dir):
  """Checks if config is loaded correctly from existing file"""
  campaign_name = test_campaign_dir
  campaign_config = {'name': 'test_campaign', 'language': 'EN', 'currency': 'USD'}
  save_config(campaign_name, campaign_config)
  loaded_config = load_config(campaign_name)
  assert loaded_config == campaign_config

def test_load_config_nonexistent_file(test_campaign_dir):
  """Checks if it handles not existing config file"""
  campaign_name = test_campaign_dir
  loaded_config = load_config(campaign_name)
  assert loaded_config == {}

def test_load_config_empty_file(test_campaign_dir):
    """Checks if config can be loaded from empty file"""
    campaign_name = test_campaign_dir
    open(os.path.join(campaign_name, "config.json"), 'w').close()
    loaded_config = load_config(campaign_name)
    assert loaded_config == {}

# Tests for collect_product_data
def test_collect_product_data_valid_urls():
    """Checks if it collects product data correctly."""
    product_urls = ["https://www.aliexpress.com/item/123.html", "https://www.aliexpress.com/item/456.html"]
    product_data = collect_product_data(product_urls)
    assert len(product_data) == 2
    assert product_data[0]["url"] == product_urls[0]
    assert product_data[1]["url"] == product_urls[1]
    assert product_data[0]["title"] == "Product 0"
    assert product_data[1]["title"] == "Product 1"

def test_collect_product_data_empty_urls():
    """Checks if it handles empty url list correctly."""
    product_urls = []
    product_data = collect_product_data(product_urls)
    assert len(product_data) == 0


# Tests for save_product_data
def test_save_product_data_valid_data(test_campaign_dir):
    """Checks if product data is saved correctly."""
    campaign_name = test_campaign_dir
    product_data = [{"url": "https://www.aliexpress.com/item/123.html", "title": "Product 1"},
                    {"url": "https://www.aliexpress.com/item/456.html", "title": "Product 2"}]
    save_product_data(campaign_name, product_data)
    with open(os.path.join(campaign_name, "products.json"), "r") as f:
        saved_data = json.load(f)
    assert saved_data == product_data

def test_save_product_data_empty_data(test_campaign_dir):
  """Checks if it saves correctly with empty data"""
  campaign_name = test_campaign_dir
  product_data = []
  save_product_data(campaign_name, product_data)
  with open(os.path.join(campaign_name, "products.json"), "r") as f:
    saved_data = json.load(f)
  assert saved_data == product_data

def test_save_product_data_overwrite_data(test_campaign_dir):
    """Checks if data can be overwritten."""
    campaign_name = test_campaign_dir
    product_data = [{"url": "https://www.aliexpress.com/item/123.html", "title": "Product 1"},
                    {"url": "https://www.aliexpress.com/item/456.html", "title": "Product 2"}]
    save_product_data(campaign_name, product_data)
    new_product_data = [{"url": "https://www.aliexpress.com/item/789.html", "title": "Product 3"}]
    save_product_data(campaign_name, new_product_data)
    with open(os.path.join(campaign_name, "products.json"), "r") as f:
        saved_data = json.load(f)
    assert saved_data == new_product_data

# Tests for create_promotional_materials
def test_create_promotional_materials_valid_data(test_campaign_dir):
    """Checks if promotional materials are created correctly."""
    campaign_name = test_campaign_dir
    product_data = [{"url": "https://www.aliexpress.com/item/123.html", "title": "Product 1"},
                    {"url": "https://www.aliexpress.com/item/456.html", "title": "Product 2"}]
    create_promotional_materials(campaign_name, product_data)
    with open(os.path.join(campaign_name, "promotional_materials.txt"), "r") as f:
        content = f.readlines()
    assert len(content) == len(product_data)
    assert "Promotional material for Product 1\n" in content
    assert "Promotional material for Product 2\n" in content

def test_create_promotional_materials_empty_data(test_campaign_dir):
    """Checks if it works fine with empty data"""
    campaign_name = test_campaign_dir
    product_data = []
    create_promotional_materials(campaign_name, product_data)
    with open(os.path.join(campaign_name, "promotional_materials.txt"), "r") as f:
        content = f.readlines()
    assert len(content) == 0

# Tests for update_promotional_materials
def test_update_promotional_materials_valid_data(test_campaign_dir):
    """Checks if promotional materials are updated correctly."""
    campaign_name = test_campaign_dir
    #create base file for update
    product_data_base = [{"url": "https://www.aliexpress.com/item/123.html", "title": "Product 1"},
                    {"url": "https://www.aliexpress.com/item/456.html", "title": "Product 2"}]
    create_promotional_materials(campaign_name, product_data_base)
    product_data = [{"url": "https://www.aliexpress.com/item/789.html", "title": "Product 3"},
                    {"url": "https://www.aliexpress.com/item/910.html", "title": "Product 4"}]
    update_promotional_materials(campaign_name, product_data)
    with open(os.path.join(campaign_name, "promotional_materials.txt"), "r") as f:
        content = f.readlines()
    assert len(content) == len(product_data) + len(product_data_base)
    assert "Promotional material for Product 1\n" in content
    assert "Promotional material for Product 2\n" in content
    assert "Updated material for Product 3\n" in content
    assert "Updated material for Product 4\n" in content

def test_update_promotional_materials_empty_data(test_campaign_dir):
    """Checks if it works fine with empty data"""
    campaign_name = test_campaign_dir
    #create base file for update
    product_data_base = [{"url": "https://www.aliexpress.com/item/123.html", "title": "Product 1"},
                    {"url": "https://www.aliexpress.com/item/456.html", "title": "Product 2"}]
    create_promotional_materials(campaign_name, product_data_base)
    product_data = []
    update_promotional_materials(campaign_name, product_data)
    with open(os.path.join(campaign_name, "promotional_materials.txt"), "r") as f:
        content = f.readlines()
    assert len(content) == len(product_data_base)
    assert "Promotional material for Product 1\n" in content
    assert "Promotional material for Product 2\n" in content


# Tests for update_categories
def test_update_categories_valid_input(test_campaign_dir):
    """Checks if directories are created for new categories."""
    campaign_name = test_campaign_dir
    categories = ["home", "beauty"]
    update_categories(campaign_name, categories)
    for category in categories:
        assert os.path.exists(os.path.join(campaign_name, "data", category))

def test_update_categories_empty_categories(test_campaign_dir):
    """Checks if it works fine with empty categories"""
    campaign_name = test_campaign_dir
    categories = []
    update_categories(campaign_name, categories)
    assert os.path.exists(os.path.join(campaign_name,"data"))

def test_update_categories_already_exists(test_campaign_dir):
  """Checks if it works fine if category already exists"""
  campaign_name = test_campaign_dir
  categories = ["home", "beauty"]
  os.makedirs(os.path.join(campaign_name, "data"), exist_ok=True)
  for category in categories:
    os.makedirs(os.path.join(campaign_name, "data", category), exist_ok=True)
  update_categories(campaign_name, categories)
  for category in categories:
    assert os.path.exists(os.path.join(campaign_name, "data", category))
# Tests for create_campaign
def test_create_campaign_valid_input(test_campaign_dir):
    """Checks if a campaign is created correctly with valid input."""
    campaign_name = test_campaign_dir
    language = "EN"
    currency = "USD"
    categories = ["electronics", "fashion"]
    product_urls = ["https://www.aliexpress.com/item/123.html", "https://www.aliexpress.com/item/456.html"]
    create_campaign(campaign_name, language, currency, categories, product_urls)

    assert os.path.exists(os.path.join(campaign_name, "data"))
    for category in categories:
      assert os.path.exists(os.path.join(campaign_name, "data", category))

    with open(os.path.join(campaign_name, "config.json"), "r") as f:
        config = json.load(f)
    assert config["name"] == campaign_name
    assert config["language"] == language
    assert config["currency"] == currency

    with open(os.path.join(campaign_name, "products.json"), "r") as f:
        products = json.load(f)
    assert len(products) == len(product_urls)

    with open(os.path.join(campaign_name, "promotional_materials.txt"), "r") as f:
      content = f.readlines()
    assert len(content) == len(product_urls)

def test_create_campaign_empty_product_urls(test_campaign_dir):
  """Checks if it works fine with empty product urls"""
  campaign_name = test_campaign_dir
  language = "EN"
  currency = "USD"
  categories = ["electronics", "fashion"]
  product_urls = []
  create_campaign(campaign_name, language, currency, categories, product_urls)

  assert os.path.exists(os.path.join(campaign_name, "data"))
  for category in categories:
    assert os.path.exists(os.path.join(campaign_name, "data", category))

  with open(os.path.join(campaign_name, "config.json"), "r") as f:
      config = json.load(f)
  assert config["name"] == campaign_name
  assert config["language"] == language
  assert config["currency"] == currency

  with open(os.path.join(campaign_name, "products.json"), "r") as f:
      products = json.load(f)
  assert len(products) == len(product_urls)

  with open(os.path.join(campaign_name, "promotional_materials.txt"), "r") as f:
    content = f.readlines()
  assert len(content) == len(product_urls)

# Tests for edit_campaign
def test_edit_campaign_valid_input(test_campaign_dir):
    """Checks if an existing campaign is edited correctly with valid input."""
    campaign_name = test_campaign_dir
    #create base campaign
    language_base = "EN"
    currency = "USD"
    categories_base = ["electronics", "fashion"]
    product_urls_base = ["https://www.aliexpress.com/item/123.html", "https://www.aliexpress.com/item/456.html"]
    create_campaign(campaign_name, language_base, currency, categories_base, product_urls_base)
    #edit campaign
    language = "RU"
    categories = ["home", "beauty"]
    product_urls = ["https://www.aliexpress.com/item/789.html"]
    edit_campaign(campaign_name, language, categories, product_urls)

    assert os.path.exists(os.path.join(campaign_name, "data"))
    for category in categories:
        assert os.path.exists(os.path.join(campaign_name, "data", category))

    with open(os.path.join(campaign_name, "config.json"), "r") as f:
        config = json.load(f)
    assert config["name"] == campaign_name
    assert config["language"] == language

    with open(os.path.join(campaign_name, "products.json"), "r") as f:
        products = json.load(f)
    assert len(products) == len(product_urls)

    with open(os.path.join(campaign_name, "promotional_materials.txt"), "r") as f:
        content = f.readlines()
    assert len(content) == len(product_urls) + len(product_urls_base)


def test_edit_campaign_empty_product_urls(test_campaign_dir):
    """Checks if it works fine with empty product urls"""
    campaign_name = test_campaign_dir
    #create base campaign
    language_base = "EN"
    currency = "USD"
    categories_base = ["electronics", "fashion"]
    product_urls_base = ["https://www.aliexpress.com/item/123.html", "https://www.aliexpress.com/item/456.html"]
    create_campaign(campaign_name, language_base, currency, categories_base, product_urls_base)
    #edit campaign
    language = "RU"
    categories = ["home", "beauty"]
    product_urls = []
    edit_campaign(campaign_name, language, categories, product_urls)

    assert os.path.exists(os.path.join(campaign_name, "data"))
    for category in categories:
        assert os.path.exists(os.path.join(campaign_name, "data", category))

    with open(os.path.join(campaign_name, "config.json"), "r") as f:
        config = json.load(f)
    assert config["name"] == campaign_name
    assert config["language"] == language

    with open(os.path.join(campaign_name, "products.json"), "r") as f:
        products = json.load(f)
    assert len(products) == len(product_urls)

    with open(os.path.join(campaign_name, "promotional_materials.txt"), "r") as f:
      content = f.readlines()
    assert len(content) == len(product_urls) + len(product_urls_base)
```