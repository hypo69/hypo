rst
How to use this code block for Campaign Creation and Editing
========================================================================================

Description
-------------------------
This code provides instructions for creating and editing advertising campaigns. It outlines the steps involved in initializing a campaign, creating directories, gathering product data, generating promotional materials, and saving/updating configurations. It also includes error handling and logging practices.

Execution steps for Campaign Creation
---------------------------------------
1. **Initialize the campaign:**
   - Enter the campaign name, language, and currency.
   - Example:
     .. code-block:: python
       
       campaign_name = 'example_campaign'
       language = 'EN'
       currency = 'USD'
2. **Create campaign directories:**
   - Generate directories for the campaign and its product categories.
   - Example:
     .. code-block:: python
       
       categories = ['electronics', 'fashion']
       create_directories(campaign_name, categories)
3. **Save campaign configuration:**
   - Create and save a configuration file for the campaign.
   - Example:
     .. code-block:: python
       
       campaign_config = {'name': campaign_name, 'language': language, 'currency': currency}
       save_config(campaign_name, campaign_config)
4. **Gather product data:**
   - Input the URLs or IDs of the products for the campaign.
   - Example:
     .. code-block:: python
       
       product_urls = ['https://www.aliexpress.com/item/123.html', 'https://www.aliexpress.com/item/456.html']
       product_data = collect_product_data(product_urls)
5. **Save product data:**
   - Store the collected product data.
   - Example:
     .. code-block:: python
       
       save_product_data(campaign_name, product_data)
6. **Create promotional materials:**
   - Generate promotional materials based on the gathered product data.
   - Example:
     .. code-block:: python
       
       create_promotional_materials(campaign_name, product_data)
7. **Review and publish campaign:**
   - Review the campaign details and publish it.
   - Example:
     .. code-block:: python
       
       review_campaign(campaign_name)
       publish_campaign(campaign_name)


Execution steps for Campaign Editing
-------------------------------------
1. **Load existing campaign configuration:**
   - Retrieve the configuration of the existing campaign.
   - Example:
     .. code-block:: python
       
       campaign_name = 'example_campaign'
       campaign_config = load_config(campaign_name)
2. **Update campaign configuration:**
   - Modify campaign parameters like language and currency.
   - Example:
     .. code-block:: python
       
       campaign_config['language'] = 'RU'
       save_config(campaign_name, campaign_config)
3. **Update categories and directories:**
   - Modify the list of categories and their corresponding directories.
   - Example:
     .. code-block:: python
       
       new_categories = ['home', 'beauty']
       update_categories(campaign_name, new_categories)
4. **Gather new product data:**
   - Input new product URLs or IDs for the updated campaign.
   - Example:
     .. code-block:: python
       
       new_product_urls = ['https://www.aliexpress.com/item/789.html']
       updated_product_data = collect_product_data(new_product_urls)
5. **Save updated product data:**
   - Store the newly collected product data.
   - Example:
     .. code-block:: python
       
       save_product_data(campaign_name, updated_product_data)
6. **Update promotional materials:**
   - Regenerate promotional materials based on the updated product data.
   - Example:
     .. code-block:: python
       
       update_promotional_materials(campaign_name, updated_product_data)
7. **Review and publish updated campaign:**
   - Review and publish the updated campaign.
   - Example:
     .. code-block:: python
       
       review_campaign(campaign_name)
       publish_campaign(campaign_name)


Usage example for Campaign Creation
-----------------------------------
.. code-block:: python

   def create_campaign(campaign_name, language, currency, categories, product_urls):
       # ... (implementation details) ...
```