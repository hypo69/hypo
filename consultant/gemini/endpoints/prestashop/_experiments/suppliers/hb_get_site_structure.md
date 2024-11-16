## \file hypotez/consultant/gemini/endpoints/prestashop/_experiments/suppliers/hb_get_site_structure.md
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: consultant.gemini.endpoints.prestashop._experiments.suppliers """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.endpoints.prestashop._experiments.suppliers """
"""  [File's Description] - Retrieves the site structure of hbdeadsea.co.il.

 @section libs imports:
  - gs 
  - helpers 
  - gs 
  - prestashop 
  - requests 
  - bs4 
  - re 
  - json 

"""
# ---------------------------------
from __init__ import gs  # Assuming this imports necessary functions
from src.utils import pprint # Assuming this imports pprint

from src.endpoints.prestashop import Product as PrestaProduct, Category as PrestaCategory
# ---------------------------------

import requests
from bs4 import BeautifulSoup
import re
import json

def get_links_with_text(url):
    """Extracts links with their text from a given URL."""
    try:
        response = requests.get(url, timeout=10) # Added timeout for robustness
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        links_with_text = {
            link['href']: link.text.strip()
            for link in links
            if link['href'] and link['href'].startswith('https://hbdeadsea.co.il/product-category')
        }
        return links_with_text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


def recursive_crawl(url, depth):
    """Recursively crawls the website and gathers links with hierarchy."""
    if depth <= 0:  # Base case: stop recursion
        return {}

    links_with_text = get_links_with_text(url)
    all_links_with_hierarchy = {}

    for link, text in links_with_text.items():
        child_links = recursive_crawl(link, depth - 1)
        all_links_with_hierarchy[link] = {"text": text, "children": child_links}

    return all_links_with_hierarchy


def get_site_structure():
    starting_url = 'https://hbdeadsea.co.il'
    depth = 2 # Reduced recursion depth for demonstration, adjust as needed.
    all_links_with_hierarchy = recursive_crawl(starting_url, depth)
    
    # Important: Handle potential empty result.
    if all_links_with_hierarchy:
        print(json.dumps(all_links_with_hierarchy, indent=4, ensure_ascii=False))
    else:
        print("No links found matching the criteria.")


if __name__ == '__main__':
    get_site_structure()

```

**Key Improvements and Explanations:**

* **Error Handling:** The code now includes `try...except` blocks to handle potential errors during the `requests.get` call and BeautifulSoup parsing. This prevents the script from crashing if a website is down or if there's an issue with the HTML structure.  Crucially, it catches `requests.exceptions.RequestException` for network issues.
* **Timeout:** Added `timeout=10` to `requests.get`. This prevents the script from hanging indefinitely if a website is slow or unresponsive.
* **`response.raise_for_status()`:**  Checks for bad HTTP status codes (e.g., 404, 500). This is important for robust web scraping.
* **Concise Link Filtering:**  The `if link['href'] and link['href'].startswith('https://hbdeadsea.co.il/product-category')` check in `get_links_with_text` is more efficient and avoids potential errors if `link['href']` is `None` or an empty string.
* **Recursion Depth Control:** The `depth` variable now controls the recursion depth. This is *vital* for preventing infinite recursion and making the script more manageable.  The example reduced the depth to 2 to make the output more concise. You might need to experiment with this.
* **Empty Result Handling:** The `if all_links_with_hierarchy:` check prevents printing an empty JSON if no links are found. This avoids a common error.
* **Clearer Variable Names:** Using more descriptive variable names (e.g., `all_links_with_hierarchy`).

**How to Use and Adapt:**

1. **Install necessary libraries:**
   ```bash
   pip install requests beautifulsoup4
   ```

2. **Adjust `depth`:** Experiment with the `depth` variable to control how many levels deep the script crawls the website. A smaller depth will be faster and use less memory.

3. **Modify Link Filtering:** The crucial `if link['href'] and link['href'].startswith('https://hbdeadsea.co.il/product-category')`  filters the links you are interested in. Change this condition if you want to target different types of links.

This improved version is significantly more robust and reliable for extracting website structure. Remember to be respectful of the website's robots.txt file and rate limits.  If you get errors, check the website's terms of service and any restrictions.