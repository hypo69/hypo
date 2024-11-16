## \file hypotez/src/suppliers/aliexpress/campaign/_docs/campaign.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.suppliers.aliexpress.campaign._docs """
MODE = 'debug'

### Overview

The `campaign` module in the AliExpress system is designed to manage and edit promotional campaigns, interact with Google Sheets for data, and prepare campaign data for use. Below is a high-level overview of the algorithm and workflow within the module.
<pre>
AliPromoCampaign
├── __init__(campaign_name, category_name, language, currency, force_update)
│   ├── super().__init__(campaign_name, category_name, language, currency)
│   ├── gs.path.google_drive / 'aliexpress' / 'campaigns' / self.campaign_name
│   ├── self.campaign_root / 'category' / category_name
│   ├── self.campaign_root / f'{language}.json'
│   ├── j_loads_ns(self._json_path)
│   ├── self.initialize_campaign()  # <-- New method for initializing self.campaign
│   └── self.get_category_products(force_update=False)
├── initialize_campaign()
│   ├── j_loads_ns(self._json_path)  # Load JSON data
│   ├── self.campaign = self.create_campaign_namespace(**vars(campaign_data))  # Create SimpleNamespace object for self.campaign
│   ├── self.title = self.campaign.title
│   ├── self.category = self.get_category_from_campaign()  # Fix category retrieval
│   └── self.category.products = self.get_category_products(force_update=False) or []
├── get_category_from_campaign()
│   ├── Ensure that 'category' attribute exists
│   └── self.campaign.category.get(self.category_name)  # Fix category retrieval
├── get_category_products(force_update)
│   ├── get_filenames(category_path, extension='.json')
│   ├── j_loads_ns(file_path.read_text(encoding='utf-8'))
│   └── self.create_product_namespace(**vars(product_data))
├── create_product_namespace(**kwargs)
│   └── SimpleNamespace with updated kwargs
├── create_campaign_namespace(**kwargs)
│   └── SimpleNamespace with updated kwargs
└── prepare_products()
    ├── self.get_prepared_products()
    ├── read_text_file(self.category_root / 'sources.txt')
    ├── get_filenames(Path(self.category_root, 'sources'))
    ├── csv2dict(Path(self.category_root, 'sources.csv'))
    ├── extract_prod_ids(prod_ids)
    └── self.process_affiliate_products(prod_ids)

Imports:
├── Python Standard Library
│   ├── re
│   ├── shutil
│   └── from pathlib import Path
├── Typing and Data Structures
│   ├── from typing import List, Optional
│   └── from types import SimpleNamespace
├── Project Settings
│   └── from header import gs
├── AliExpress Modules
│   ├── from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
│   ├── from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids
│   └── from src.suppliers.aliexpress.utils.set_full_https import ensure_https
├── JSON Utilities
│   ├── from src.utils import j_loads_ns, j_loads
│   └── from src.utils.jjson import j_dumps
├── Converters and Helpers
│   ├── from src.utils.convertors import list2string, csv2dict
│   └── from src.utils import pprint
├── File Operations
│   └── from src.utils.file import read_text_file, get_filenames
└── Logging
    └── from src.logger import logger
</pre>
### Algorithm

1. **Initialization**:
   - The `__init__.py` file initializes the `campaign` module, making it available for import and use in other parts of the application.

2. **Editing Campaigns**:
   - The `ali_campaign_editor.py` file contains the main logic for editing campaigns. It provides functions to create, update, and manage campaign data.
   - External dependencies, such as `AliCampaignGoogleSheet` from `src.suppliers.aliexpress`, are used to interact with AliExpress campaign data.

3. **Managing Promotional Campaigns**:
   - The `ali_promo_campaign.py` file manages promotional campaigns, handling specific promotional strategies and configurations.
   - It leverages `AliCampaignGoogleSheet` for specific functionalities related to AliExpress.

4. **Google Sheets Interaction**:
   - The `gsheet.py` file manages interactions with Google Sheets. This includes reading from and writing to sheets for campaign data.
   - Dependencies such as `gspread` and `pandas` are used to facilitate these interactions.
   - The module retrieves settings from `src.settings.gs` to configure Google Sheets access.

5. **Common Functions and Classes**:
   - The `header.py` file contains common functions or classes that are used across different parts of the `campaign` module. This ensures reusability and modularity.

6. **Preparing Campaign Data**:
   - The `prepare_campaigns.py` file is responsible for setting up and organizing necessary data for campaigns. This includes preprocessing data, validating inputs, and ensuring all necessary information is prepared for campaign execution.

7. **Type Definitions**:
   - The `ttypes.py` file defines types and structures used throughout the campaign module. This helps in maintaining consistency and type safety.

8. **Version Management**:
   - The `version.py` file maintains version information for the campaign module. This can be useful for debugging and tracking updates.

### Documentation and Examples

- **Documentation**:
  - The `_docs` directory contains markdown files that provide detailed documentation for the module, coding instructions, and startup options.

- **Graphical Representations**:
  - The `_dot` and `_mermaid` directories contain graphical representations of the campaign structures in DOT and Mermaid formats respectively.

- **Examples**:
  - The `_examples` directory includes example scripts demonstrating how to use various functionalities of the campaign module.

### Testing

- **Test Scripts**:
  - The `_pytest` directory includes test scripts that verify the correctness and integration of the campaign module. These tests ensure that all functionalities work as expected and help in maintaining code quality.

### Detailed Workflow

1. **Setup and Configuration**:
   - Import necessary modules and dependencies.
   - Initialize settings and configurations.

2. **Campaign Editing**:
   - Use `ali_campaign_editor.py` to create and modify campaign data.
   - Fetch existing campaign data using `AliCampaignGoogleSheet` and apply updates.

3. **Promotional Campaign Management**:
   - Apply promotional strategies using `ali_promo_campaign.py`.
   - Manage different types of promotions and their configurations.

4. **Data Interaction with Google Sheets**:
   - Read campaign data from Google Sheets using `gsheet.py`.
   - Process the data using `pandas` and other utilities.
   - Write updated campaign data back to Google Sheets.

5. **Data Preparation**:
   - Use `prepare_campaigns.py` to preprocess and validate campaign data.
   - Ensure all necessary information is prepared for campaign execution.

6. **Common Operations**:
   - Utilize common functions from `header.py` for repeated tasks.

7. **Testing and Validation**:
   - Run test scripts from `_pytest` to ensure functionality.
   - Validate campaign data and operations through integration tests.

8. **Documentation and Examples**:
   - Refer to `_docs` for detailed documentation.
   - Use `_examples` to understand and implement specific functionalities.

This algorithm provides a comprehensive workflow of the `campaign` module, detailing how different components interact and work together to manage and edit AliExpress campaigns.

### Example Usage

1. **Process a Single Campaign Category:**
   ```python
   process_campaign_category("SummerSale", "Electronics", "EN", "USD", force=True)
   ```

2. **Process a Specific Campaign:**
   ```python
   process_campaign("WinterSale", categories=["Clothing", "Toys"], language="EN", currency="USD", force=False)
   ```

3. **Process All Campaigns:**
   ```python
   process_all_campaigns(language="EN", currency="USD", force=True)
   ```

These examples show how to use the provided functions to process campaign categories and campaigns for different languages and currencies.
