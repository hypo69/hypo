## \file hypotez/src/suppliers/aliexpress/campaign/ali_campaign_editor.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.suppliers.aliexpress.campaign 
	:platform: Windows, Unix
	:synopsis: This module provides the editor for advertising campaigns

```mermaid
graph LR
    subgraph AliCampaignEditor
        A[User Input: campaign_name, language, currency] --> B{AliCampaignEditor.__init__};
        B --> C[AliPromoCampaign.__init__];
        C --> D[Initialization: AliCampaignEditor constructor];
        D --> E[AliCampaignEditor];
        
        E --> F[delete_product: Check for affiliate link];
        F --> G[read_text_file sources.txt: Read product list];
        G --> H[Iterate & check product_id: Loop through product list];
        H -- Match --> I[remove & save: Remove product if match found];
        H -- No Match --> J[rename product file: Rename product file if no match];
        
        E --> K[update_product: Update product details];
        K --> L[Call dump_category_products_files: Update category with new product];
        
        E --> M[update_campaign: Update campaign properties like description];
        M --> N[update campaign parameters];
        
        E --> O[update_category: Update category in JSON file];
        O --> P[j_loads JSON file: Read category data];
        P --> Q[Update category: Update category data];
        Q --> R[j_dumps JSON file: Write updated category to file];
        
        E --> S[get_category: Retrieve category by name];
        S --> T[Check if category exists];
        T -- Found --> U[Return SimpleNamespace: Return category details];
        T -- Not Found --> V[Log warning: Category not found in campaign];
        
        E --> W[list_categories: List all categories in the campaign];
        W --> X[Check category attribute: Ensure categories exist in campaign];
        X -- Found --> Y[Return category list: List category names];
        X -- Not Found --> Z[Log warning: No categories found in campaign];
        
        E --> AA[get_category_products: Retrieve products for a category];
        AA --> AB[Get category path: Build path for category products];
        AB --> AC[Get JSON filenames: Retrieve all product JSON files];
        AC --> AD[Read JSON files: Load product data];
        AD --> AE[Create SimpleNamespace: Convert product data to objects];
        AE --> AF[Return products: Return list of products];
        AC -- No JSON files --> AG[Log error: No files found];
        AG --> AH[Process category: Trigger category product preparation];

        E --> AI[Other methods];
    end

  
```
"""



import re
import shutil
from pathlib import Path
from types import SimpleNamespace
from typing import List, Optional

import header
from src import gs
from src.suppliers.aliexpress.campaign.ali_promo_campaign import AliPromoCampaign
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet
from src.suppliers.aliexpress.utils import extract_prod_ids, ensure_https
from src.utils.jjson import j_loads_ns, j_loads, j_dumps
from src.utils.convertors.csv import csv2dict
from src.utils.printer import pprint
from src.utils.file import read_text_file, save_text_file, get_filenames
from src.logger.logger import logger

class AliCampaignEditor(AliPromoCampaign):
    """ Editor for advertising campaigns.
    """
    def __init__(self, 
                 campaign_name: str, 
                 language: Optional[str | dict] = None, 
                 currency: Optional[str] = None):
        """ Initialize the AliCampaignEditor with the given parameters.
        
        Args:
            campaign_name (Optional[str]): The name of the campaign. Defaults to `None`.
            language (Optional[str | dict]): The language of the campaign. Defaults to 'EN'.
            currency (Optional[str]): The currency for the campaign. Defaults to 'USD'.
            campaign_file (Optional[str | Path]): Optionally load a `<lang>_<currency>.json` file from the campaign root folder. Defaults to `None`.

        Raises:
            CriticalError: If neither `campaign_name` nor `campaign_file` is provided.
        
        Example:
        # 1. by campaign parameters
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale", language="EN", currency="USD")
        # 2. load fom file
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale", campaign_file="EN_USD.JSON")
        """
        ...
        super().__init__(campaign_name = campaign_name, language = language, currency = currency)
        #self.google_sheet = AliCampaignGoogleSheet(campaign_name = campaign_name, language = language, currency = currency, campaign_editor = self)

    def delete_product(self, product_id: str, exc_info: bool = False):
        """ Delete a product that does not have an affiliate link.
        
        Args:
            product_id (str): The ID of the product to be deleted.
            exc_info (bool): Whether to include exception information in logs. Defaults to `False`.

        Example:
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> editor.delete_product("12345")
        """
        ...
        _product_id = extract_prod_ids(product_id)
        
        product_path = self.category_path / 'sources.txt'
        prepared_product_path = self.category_path / '_sources.txt'
        products_list = read_text_file(product_path)
        if products_list:
            for record in products_list:
                if _product_id:
                    record_id = extract_prod_ids(record)
                    if record_id == str(product_id):
                        products_list.remove(record)
                        save_text_file((products_list, '\n'), prepared_product_path)
                        break
                else:
                    if record == str(product_id):
                        products_list.remove(record)
                        save_text_file((products_list, '\n'), product_path)
                    
        else:
            product_path = self.category_path / 'sources' / f'{product_id}.html'    
            try:
                product_path.rename(self.category_path / 'sources' / f'{product_id}_.html')
                logger.success(f"Product file {product_path=} renamed successfully.")
            except FileNotFoundError as ex:
                logger.error(f"Product file {product_path=} not found.", exc_info=exc_info)
            except Exception as ex:
                logger.critical(f"An error occurred while deleting the product file {product_path}.", ex)

    def update_product(self, category_name: str, lang: str, product: dict):
        """ Update product details within a category.

        Args:
            category_name (str): The name of the category where the product should be updated.
            lang (str): The language of the campaign.
            product (dict): A dictionary containing product details.

        Example:
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})
        """
        ...
        self.dump_category_products_files(category_name, lang, product)

    def update_campaign(self):
        """ Update campaign properties such as `description`, `tags`, etc.
        
        Example:
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> editor.update_campaign()
        """
        ...

    def update_category(self, json_path: Path, category: SimpleNamespace) -> bool:
        """ Update the category in the JSON file.

        Args:
            json_path (Path): Path to the JSON file.
            category (SimpleNamespace): Category object to be updated.

        Returns:
            bool: True if update is successful, False otherwise.

        Example:
            >>> category = SimpleNamespace(name="New Category", description="Updated description")
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> result = editor.update_category(Path("category.json"), category)
            >>> print(result)  # True if successful
        """
        ...
        try:
            data = j_loads(json_path)  # Read JSON data from file
            data['category'] = category.__dict__  # Convert SimpleNamespace to dict
            j_dumps(data, json_path)  # Write updated JSON data back to file
            return True
        except Exception as ex:
            logger.error(f"Failed to update category {json_path}: {ex}")
            return False

    def get_category(self, category_name: str) -> Optional[SimpleNamespace]:
        """ Returns the SimpleNamespace object for a given category name.

        Args:
            category_name (str): The name of the category to retrieve.

        Returns:
            Optional[SimpleNamespace]: SimpleNamespace object representing the category or `None` if not found.

        Example:
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> category = editor.get_category("Electronics")
            >>> print(category)  # SimpleNamespace or None
        """
        ...
        try:
            if hasattr(self.campaign.category, category_name):
                return getattr(self.campaign.category, category_name)
            else:
                logger.warning(f"Category {category_name} not found in the campaign.")
                return
        except Exception as ex:
            logger.error(f"Error retrieving category {category_name}.", ex, exc_info=True)
            return

    @property
    def list_categories(self) -> Optional[List[str]]:
        """ Retrieve a list of categories in the current campaign.

        Returns:
            Optional[List[str]]: A list of category names, or None if no categories are found.

        Example:
            >>> editor = AliCampaignEditor(campaign_name="Summer Sale")
            >>> categories = editor.categories_list
            >>> print(categories)  # ['Electronics', 'Fashion', 'Home']
        """
        try:
            # Ensure campaign has a category attribute and it is a SimpleNamespace
            if hasattr(self.campaign, 'category') and isinstance(self.campaign.category, SimpleNamespace):
                return list(vars(self.campaign.category).keys())
            else:
                logger.warning("No categories found in the campaign.")
                return
        except Exception as ex:
            logger.error(f"Error retrieving categories list: {ex}")
            return




    def get_category_products(
        self, category_name: str
    ) -> Optional[List[SimpleNamespace]]:
        """Чтение данных о товарах из JSON файлов для конкретной категории.

        Args:
            category_name (str): Имя категории.

        Returns:
            Optional[List[SimpleNamespace]]: Список объектов SimpleNamespace, представляющих товары.

        Example:
            >>> products = campaign.get_category_products("Electronics")
            >>> print(len(products))
            15
        """
        category_path = (
            self.base_path
            / "category"
            / category_name
            / f"{self.language}_{self.currency}"
        )
        json_filenames = get_filenames(category_path, extensions="json")
        products = []

        if json_filenames:
            for json_filename in json_filenames:
                product_data = j_loads_ns(category_path / json_filename)
                product = SimpleNamespace(**vars(product_data))
                products.append(product)
            return products
        else:
            logger.error(
                f"No JSON files found for {category_name=} at {category_path=}.\nStart prepare category"
            )
            self.process_category_products(category_name)
            return 
