## \file hypotez/src/suppliers/aliexpress/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.suppliers.aliexpress """

""" supplier `aliexpress`

Here is the list of files and directories that are included in the `aliexpress` module, excluding those that start with multiple underscores or are within `_experiments`:
@rst
### Files and Directories

1. **spreadsheet.py**
2. **aliexpress/**
   - **\_\_init\_\_.py**
   - **affiliate_links_shortener_via_webdriver.py**
   - **affiliated_products_generator.py**
   - **aliapi.py**
   - **aliexpress.json**
   - **aliexpress.py**
   - **alirequests.py**
   - **category.py**
   - **desktop.ini**
   - **graber.py**
   - **version.py**
   - **_docs/**
     - affiliated_products_generator.md
   - **_dot/**
     - affiliated_products_generator.dot
     - aliapi.dot
   - **_examples/**
     - affiliated_products_generator.en.md
     - affiliated_products_generator.py
     - affiliated_products_generator.ru.md
   - **_pytests/**
     - test_affiliated_products_generator.py
   - **api/**
     - \_\_init\_\_.py
     - api.py
     - version.py
     - **_examples/iop/**
       - .DS_Store
       - \_\_init\_\_.py
       - base.py
       - test_get.py
       - test_internal.py
       - test_iop.ipynb
   - **campaign/**
     - \_\_init\_\_.py
     - campaign.py
     - gsheet.py
     - **_mermaid/**
       - AliAffiliatedProducts.mer
       - aliexpress_campaign.mer
     - **_pytest/**
       - guide_test.md
       - test_alipromo_campaign.py
       - test_campaign_integration.py
       - test_edit_campaign.py
       - test_prepare_campaigns.py
   - **gapi/**
     - \_\_init\_\_.py
     - campaign_editor.py
     - header.py
     - version.py
   - **gui/**
     - \_\_init\_\_.py
     - campaign.py
     - category.py
     - header.py
     - main.py
     - product.py
     - styles.py
     - version.py
   - **locators/**
     - affiliate_links_shortener.json
     - category.json
     - deals.json
     - from_mail.json
     - login.json
     - product.json
     - store.json
   - **utils/**
     - extract_product_id.py
     - set_full_https.py

### Explanation of the `aliexpress` Module

The `aliexpress` module appears to be a comprehensive package designed to interact with the AliExpress platform, handle various data processing tasks, and manage Google Sheets for organizing and manipulating campaign data. Here's a breakdown of its primary components:

- **Core Scripts and Modules**:
  - **\_\_init\_\_.py**: Initializes the package.
  - **affiliate_links_shortener_via_webdriver.py**: Shortens affiliate links using WebDriver.
  - **affiliated_products_generator.py**: Generates affiliated products.
  - **aliapi.py**: Interacts with the AliExpress API.
  - **aliexpress.py**: Main script for AliExpress-related operations.
  - **alirequests.py**: Manages HTTP requests to AliExpress.
  - **category.py**: Handles category data.
  - **graber.py**: Script for grabbing data.
  - **version.py**: Manages versioning.

- **Documentation and Examples**:
  - **_docs/**: Contains documentation files.
  - **_dot/**: Contains DOT files for graph descriptions.
  - **_examples/**: Includes example scripts and documentation.

- **Testing**:
  - **_pytests/**: Contains pytest scripts for testing various components.

- **API**:
  - **api/**: Contains API-related scripts and examples.
  - **\_\_init\_\_.py**: Initializes the API package.
  - **api.py**: Main API script.
  - **version.py**: Manages API versioning.
  - **_examples/iop/**: Includes internal examples for API operations.

- **Campaign Management**:
  - **campaign/**: Contains scripts and resources for managing campaigns.
  - **\_\_init\_\_.py**: Initializes the campaign package.
  - **campaign.py**: Main script for campaign management.
  - **gsheet.py**: Manages Google Sheets for campaign data.
  - **_mermaid/**: Contains Mermaid files for diagram descriptions.
  - **_pytest/**: Contains pytest scripts for testing campaign-related components.

- **Google API Integration**:
  - **gapi/**: Contains scripts for integrating with Google APIs.
  - **\_\_init\_\_.py**: Initializes the Google API package.
  - **campaign_editor.py**: Edits campaign data using Google APIs.
  - **header.py**: Manages headers for API requests.
  - **version.py**: Manages versioning for Google API scripts.

- **Graphical User Interface**:
  - **gui/**: Contains scripts for the graphical user interface.
  - **\_\_init\_\_.py**: Initializes the GUI package.
  - **campaign.py**: Manages the campaign interface.
  - **category.py**: Manages the category interface.
  - **header.py**: Manages headers for the GUI.
  - **main.py**: Main script for the GUI.
  - **product.py**: Manages product interface.
  - **styles.py**: Contains styles for the GUI.
  - **version.py**: Manages versioning for GUI scripts.

- **Locators**:
  - **locators/**: Contains JSON files with locators for various AliExpress elements.
  - **affiliate_links_shortener.json**
  - **category.json**
  - **deals.json**
  - **from_mail.json**
  - **login.json**
  - **product.json**
  - **store.json**

- **Utilities**:
  - **utils/**: Contains utility scripts.
  - **extract_product_id.py**: Extracts product IDs.
  - **set_full_https.py**: Ensures URLs use HTTPS.
@endrst
This structure and the explanation provide an overview of the `aliexpress` module's functionalities and organization.
"""
...
from packaging.version import Version
from .version import __version__, __doc__, __details__  

from .aliexpress import Aliexpress
from .aliapi import AliApi
from .alirequests import AliRequests
from .campaign import AliCampaignEditor
from .campaign.html_generators import ProductHTMLGenerator, CategoryHTMLGenerator, CampaignHTMLGenerator 
