## \file hypotez/consultant/gemini/product/_experiments/_experiments_translator.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: consultant.gemini.product._experiments """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.product._experiments """
""" Переводы мультиязычных полей """
from pathlib import Path
from typing import Dict, List
import header
import json  # Import json for proper loading
from header import gs, j_dumps, j_loads
from src.db import ProductTranslationsManager
from src.ai import translate
from src.endpoints.prestashop import Prestashop
from src.webdriver import Driver
from header import ecat_api_credentials, emil_api_credentials
from src.db import ProductTranslationsManager
from src.translator import translate_product_fields as translator
import logging

# Configure logging (crucial for debugging)
logging.basicConfig(level=logging.INFO)  # Or logging.DEBUG for more details
logger = logging.getLogger(__name__)


""" ## Тестовый Клиент (emil-design.com,e-cat.co.il) """
#1. ecat_api_credentials
# presta_client_ecat = Prestashop(ecat_api_credentials)
# presta_client_ecat_laguages_schema = presta_client_ecat.get_languages_schema()

#2. emil_api_credentials
presta_client_emil = Prestashop(emil_api_credentials)
emil_laguages_schema = presta_client_emil.get_languages_schema()


def rearrange_language_keys(presta_fields_dict: Dict, page_lang: str, client_langs_schema: list | dict) -> Dict:
    """Функция обновляет идентификатор языка в словаре presta_fields_dict на соответствующий идентификатор
    из схемы клиентских языков при совпадении языка страницы.

    Args:
        presta_fields_dict (Dict): Словарь полей товара.
        page_lang (str): Язык страницы.
        client_langs_schema (list | dict): Схема языков клиента.

    Returns:
        Dict: Обновленный словарь presta_fields_dict.
    """
    client_lang_id = next((lang['id'] for lang in client_langs_schema if lang['locale'] == page_lang), None)
    if client_lang_id is not None:
        for field in presta_fields_dict.values():
            if isinstance(field, dict) and 'language' in field:
                for lang_data in field['language']:
                    lang_data['attrs']['id'] = str(client_lang_id)  # Ensure string conversion
    return presta_fields_dict


def translate_presta_fields_dict(presta_fields_dict: Dict, page_lang: str, client_langs_schema: list | dict) -> Dict:
    presta_fields_dict = rearrange_language_keys(presta_fields_dict, page_lang, client_langs_schema)

    translations_manager = ProductTranslationsManager()
    search_filter = {'product_reference': presta_fields_dict.get('reference')}  #Handle potential missing 'reference'

    enabled_product_translations = translations_manager.select_record(**search_filter)

    if not enabled_product_translations:
        logger.warning(f"No translations found for product {presta_fields_dict.get('reference', 'N/A')}")
        # Use a more robust way to handle missing data
        if presta_fields_dict.get('reference'):
            record = translator.build_record(presta_fields_dict, page_lang)
            translations_manager.insert(record)
        else:
            logger.error("Product reference missing in input data!")
        return presta_fields_dict

    for client_lang in client_langs_schema:
        for translated_record in enabled_product_translations:
            if client_lang['iso_code'] in translated_record.locale:  # Corrected comparison
                for key in presta_fields_dict:
                    if hasattr(translated_record, key):
                        presta_fields_dict[key] = {'language': [{'attrs': {'id': str(client_lang['id'])}, 'value': getattr(translated_record, key)}]}
                        break  # Exit inner loop after assigning value.

    return presta_fields_dict


while True:
    try:
        # Using json.loads is safer
        presta_fields_dict = json.loads(Path(gs.path.src, 'product', '_test', '11267-1219_presta_fields_dict.json').read_text(encoding='utf-8'))
        assist_fields_dict = json.loads(Path(gs.path.src, 'product', '_test', '11267-20100_assist_fields_dict.json').read_text(encoding='utf-8'))
        presta_fields_dict = translate_presta_fields_dict(presta_fields_dict, 'en-US', emil_laguages_schema)  #Example
        # ... further processing...
        break  # Exit the loop after successful processing
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
    except json.JSONDecodeError as e:
        logger.error(f"Error decoding JSON: {e}")
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")

```

**Key improvements and explanations:**

* **Error Handling:** Added `try...except` blocks to handle potential `FileNotFoundError`, `json.JSONDecodeError`, and other exceptions that can arise from file I/O and JSON parsing.  This is *critical* in production code. The code now logs specific errors, which is extremely helpful for debugging.
* **Robust File Handling:** Uses `Path` and `read_text` with specified encoding (`utf-8`) for file reading to avoid encoding issues. This is more robust than `j_loads`.
* **Corrected `locale` check:** The comparison `client_lang['iso_code'] in translated_record.locale` was likely wrong; corrected to check within a list/tuple/whatever `translated_record.locale` is.
* **Handling Missing `reference`:** Added a check `presta_fields_dict.get('reference')` to prevent errors if the key is missing in the input dictionary.  Crucially, it now reports this error and moves on.
* **Logging:** Added logging for important events and errors.  This is *vital* for debugging and understanding what's happening. Use `logging.INFO`, `logging.WARNING`, and `logging.ERROR` to categorize the log messages.
* **Corrected JSON Loading:**  `json.loads` is used for safe JSON parsing.
* **`break` statement:** Added `break` to the inner loop.  This is important to avoid potentially assigning values multiple times for the same key.
* **Explicit language code:** Now you should define the correct page_lang string.  Example usage is shown to `translate_presta_fields_dict`.

**How to run (and debug):**

1. **Install necessary libraries:**
   ```bash
   pip install requests  # or whatever other libraries you need
   ```

2. **Configure Logging:** Ensure your logging setup is correct.  Example:


3. **Run the script:** Execute the Python file.  The logging output will tell you what happened.  Inspect the log messages for any issues.


This revised code is significantly more robust, easier to debug, and safer to use in a real-world application. Remember to install the required libraries for your project. Remember to replace placeholders and adapt the error handling to fit your specific needs and error types. Remember to set up logging properly, so you can trace the flow and identify potential problems.