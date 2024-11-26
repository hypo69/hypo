# AliExpress Campaign Module Usage Guide

This guide details how to use the `campaign` module for managing and editing AliExpress promotional campaigns. It interacts with Google Sheets for data retrieval and manipulation.

## Prerequisites

- Python 3.x
- Required libraries: `gspread`, `pandas`, `requests` (if external API calls are involved).  Install using `pip install gspread pandas requests`.
- Google Sheet access setup:  Configure Google Sheets API credentials (see Google Cloud documentation).  The `src.settings.gs` file likely holds these configurations.

## Module Structure

The `campaign` module is organized into several files, each with specific responsibilities:

- **`ali_promo_campaign.py`**:  The core module for managing AliExpress promotional campaigns. This file houses the main logic.

- **`gsheet.py`**: Handles interactions with Google Sheets. Includes functions for reading data from specified sheets, writing updated data, and managing spreadsheet connections.

- **`header.py`**: Contains reusable functions and classes (e.g., for data validation, error handling, or common utilities).

- **`prepare_campaigns.py`**: Prepares data for campaign execution. Validates inputs, performs necessary preprocessing, and ensures all required information is ready.

- **`ttypes.py`**: Defines types and structures used within the campaign module (e.g., dataclasses).

- **`utils`**: A folder potentially containing supporting modules (e.g., `jjson.py`, `convertors.py`, `file.py`, etc.) for JSON handling, conversions, file operations.

## Key Concepts

- **`AliPromoCampaign` Class:** The primary class for managing a single campaign.
- **`campaign_data` (Likely a dictionary or object):** Contains details about the campaign (name, category, language, currency, etc.). This object is likely passed as an argument.
- **`gs.path.google_drive / 'aliexpress' / 'campaigns' / campaign_name`:** Defines the path to the Google Sheet storing campaign data. Adjust this according to the specific structure used in the provided code.
- **`self.campaign_root / 'category' / category_name`:** Refers to the specific campaign category's directory or data storage location within the Google Sheet.

## How to Use

The provided examples illustrate how to interact with the module.

**Example 1: Processing a Single Campaign Category**

```python
from src.suppliers.aliexpress.campaign import ali_promo_campaign

def process_campaign_category(campaign_name, category_name, language, currency, force_update=False):
    """Processes a specific campaign category."""
    campaign = ali_promo_campaign.AliPromoCampaign(campaign_name, category_name, language, currency, force_update)
    campaign.prepare_products()  # Prepares products for the campaign

process_campaign_category("SummerSale", "Electronics", "EN", "USD", force=True)
```

**Example 2: Processing a Specific Campaign**

```python
def process_campaign(campaign_name, categories, language, currency, force_update=False):
  """Processes a specific campaign."""
  campaign = ali_promo_campaign.AliPromoCampaign(campaign_name, categories, language, currency, force_update)  # Assuming categories is a list
  campaign.prepare_products()  # Prepares products
```

**Example 3: Processing All Campaigns**

```python
def process_all_campaigns(language, currency, force_update=True):
  """Processes all campaigns."""
  # Replace this with the logic to retrieve all campaign names and categories
  # ... code to fetch campaign names and categories ...

  for campaign_name, category_name in all_campaigns_data:
    process_campaign(campaign_name, category_name, language, currency, force_update)
```

**Explanation and Important Considerations:**

- **Error Handling:**  Implement robust error handling (e.g., `try...except` blocks) to catch potential issues with Google Sheet access, file operations, or data formats.
- **Data Validation:**  Ensure that the input `campaign_data` is correctly structured and contains the necessary information.
- **`force_update`:**  This flag in the constructor controls whether the campaign data is retrieved from Google Sheets or processed from existing files (if data hasn't changed).
- **External Dependencies:** Ensure that `AliCampaignGoogleSheet`, `AliAffiliatedProducts`, `extract_prod_ids`, etc. are correctly imported and function as expected.
- **File Paths:** Verify that file paths are correctly constructed and point to the appropriate directories and files.

**Key Improvements & Recommendations:**

- Add clear docstrings to functions explaining parameters, return values, and any exceptions.
- Implement more comprehensive error handling, logging, and validation to make the code more robust and user-friendly.


This expanded guide clarifies the usage, structure, and best practices for working with the AliExpress campaign module. Remember to adapt the code examples and paths to your specific project setup. Remember to install the necessary libraries.