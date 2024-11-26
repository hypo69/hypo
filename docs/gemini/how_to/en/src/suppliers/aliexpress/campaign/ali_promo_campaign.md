```python
"""
Usage Guide for `ali_promo_campaign.py`

This guide explains how to use the `AliPromoCampaign` class to manage advertising campaigns on AliExpress.  It covers initializing campaigns, processing data, generating AI-powered descriptions, and saving results.

**Module:** `hypotez/src/suppliers/aliexpress/campaign/ali_promo_campaign.py`

**Class:** `AliPromoCampaign`

**Purpose:** This module handles advertising campaigns on AliExpress. It processes category and product data, creates/edits JSON files, and leverages AI for campaign data generation.

**Key Concepts:**

* **Initialization:**  Creating an `AliPromoCampaign` object.
* **Data Processing:**  Fetching and manipulating campaign data (e.g., processing categories, products).
* **AI Integration:** Using AI models (Google Gemini and potentially OpenAI) to generate descriptions and other campaign information.
* **File Handling:** Reading and writing JSON files to store and retrieve campaign data.


**Methods and Usage Examples:**


**1. Initialization (`__init__`)**

```python
campaign = AliPromoCampaign(
    campaign_name="SummerSale", language="EN", currency="USD", model='openai'  # or 'gemini'
)
print(campaign.campaign_name)
```

   *   `campaign_name`: The name of the campaign.
   *   `language`: The language of the campaign (e.g., "EN", "RU").
   *   `currency`: The currency used in the campaign (e.g., "USD", "ILS").
   *   `model`: Specifies the AI model to use (defaults to 'openai', but can be set to 'gemini').

This initializes the campaign object. If the campaign file already exists, it loads the existing data.  If not, it initializes a new campaign.


**2. Processing the Entire Campaign (`process_campaign`)**

```python
campaign = AliPromoCampaign("new_campaign", "EN", "USD")
campaign.process_campaign()
```

This method iterates through categories, processing products in each using `process_category_products` and AI descriptions using `process_ai_category`.

**3. Processing Products in a Category (`process_category_products`)**

```python
campaign = AliPromoCampaign("new_campaign", "EN", "USD")
products = campaign.process_category_products("electronics")
```

This method retrieves affiliated products for a given category. The important part is that it creates (or reads from existing) JSON files for each product in the category.  The returned `products` are a list of `SimpleNamespace` objects, ready for further processing or saving.

**4. Processing AI Data for a Category (`process_ai_category`)**

```python
campaign = AliPromoCampaign("new_campaign", "EN", "USD")
campaign.process_ai_category("Electronics")
```

This method uses the chosen AI model (Gemini or OpenAI) to generate data (like descriptions) for a category based on product titles and other available details.


**5. Saving Product Data (`dump_category_products_files`)**

```python
campaign = AliPromoCampaign("new_campaign", "EN", "USD")
# ... (after calling process_category_products)
campaign.dump_category_products_files("electronics", products)
```

Saves processed product data to JSON files within the campaign's category structure.

**6. Generating campaign output data and HTML (`generate_output` and `generate_html`)**

```python
campaign = AliPromoCampaign("new_campaign", "EN", "USD")
# ... (after processing the campaign)
await campaign.generate_output("CampaignName", category_path, products_list)  # await for async call
await campaign.generate_html(...)
```

Generates and saves various output formats (JSON, HTML files).

**Important Considerations:**

*   **Error Handling:** The code includes `logger` statements for various error conditions.  Check the logs for any issues during processing.
*   **File Structure:** The code expects a specific file structure (e.g., `/category` subdirectory within the campaign directory).
*   **AI Model Selection:** The code is set up to handle both Gemini and OpenAI.  Choose the relevant model based on your needs.
*   **Asynchronous Operations:** The `generate_output` function is designed for asynchronous operation using `asyncio`.


**Further Improvements and Considerations:**

* **Robust Error Handling:** Add more specific error handling and validation to prevent unexpected behavior and crashes.
* **Input Validation:** Implement input validation to ensure that the `campaign_name`, `language`, and `currency` values are valid.
* **Data Cleaning:** Include data cleaning and preprocessing steps to improve the quality of AI-generated descriptions.

This guide should help you effectively use the `ali_promo_campaign.py` module for managing AliExpress campaigns. Remember to adapt the code to your specific needs and data structures.
```