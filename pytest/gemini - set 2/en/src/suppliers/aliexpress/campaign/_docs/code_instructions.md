```python
import pytest
import os

# Mock functions for testing (replace with actual implementations if available)
def create_directories(campaign_name, categories):
    os.makedirs(f"campaigns/{campaign_name}/", exist_ok=True)
    for category in categories:
        os.makedirs(f"campaigns/{campaign_name}/{category}", exist_ok=True)
    return True

def save_config(campaign_name, campaign_config):
    with open(f"campaigns/{campaign_name}/config.json", "w") as f:
        import json
        json.dump(campaign_config, f)
    return True

def collect_product_data(product_urls):
    # Mock data collection.  Replace with actual logic.
    product_data = [{'url': url, 'name': 'Product ' + url[-10:]} for url in product_urls]
    return product_data

def save_product_data(campaign_name, product_data):
  #Mock save data. Replace with actual logic.
  with open(f"campaigns/{campaign_name}/products.json","w") as f:
    import json
    json.dump(product_data, f)
  return True

def create_promotional_materials(campaign_name, product_data):
    # Mock function to create promotional materials
    return True

def review_campaign(campaign_name):
    # Mock function to review campaign
    return True

def publish_campaign(campaign_name):
    # Mock function to publish campaign
    return True

def load_config(campaign_name):
  #Mock function to load config
  try:
    with open(f"campaigns/{campaign_name}/config.json", "r") as f:
      import json
      return json.load(f)
  except FileNotFoundError:
      return None

def update_categories(campaign_name, categories):
  #Mock function to update categories
  os.makedirs(f"campaigns/{campaign_name}/",exist_ok=True)
  for category in categories:
    os.makedirs(f"campaigns/{campaign_name}/{category}", exist_ok=True)
  return True

def update_promotional_materials(campaign_name, updated_product_data):
    # Mock function to update promotional materials
    return True



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
    if campaign_config:
        campaign_config['language'] = language
        save_config(campaign_name, campaign_config)
        update_categories(campaign_name,categories)
        updated_product_data = collect_product_data(product_urls)
        save_product_data(campaign_name,updated_product_data)
        update_promotional_materials(campaign_name, updated_product_data)
        review_campaign(campaign_name)
        publish_campaign(campaign_name)
    else:
        return False #or raise exception


def test_create_campaign_valid_input():
    campaign_name = 'test_campaign'
    language = 'EN'
    currency = 'USD'
    categories = ['electronics', 'fashion']
    product_urls = ['https://www.aliexpress.com/item/123.html', 'https://www.aliexpress.com/item/456.html']
    create_campaign(campaign_name, language, currency, categories, product_urls)
    assert os.path.exists(f"campaigns/{campaign_name}/config.json")
    assert os.path.exists(f"campaigns/{campaign_name}/electronics")

def test_edit_campaign_valid_input():
  campaign_name = 'test_campaign'
  language = 'RU'
  categories = ['home', 'beauty']
  product_urls = ['https://www.aliexpress.com/item/789.html']
  assert edit_campaign(campaign_name, language, categories, product_urls) == True
  assert os.path.exists(f"campaigns/{campaign_name}/config.json")
  assert os.path.exists(f"campaigns/{campaign_name}/home")

def test_edit_campaign_nonexistent_campaign():
  campaign_name = 'nonexistent_campaign'
  language = 'RU'
  categories = ['home', 'beauty']
  product_urls = ['https://www.aliexpress.com/item/789.html']
  assert edit_campaign(campaign_name, language, categories, product_urls) == False

#Cleanup. Remove test files after the tests
import shutil

def teardown_module():
  try:
    shutil.rmtree("campaigns")
  except FileNotFoundError:
    pass

```