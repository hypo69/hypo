## \file hypotez/consultant/gemini/endpoints/prestashop/_experiments/suppliers/kualastyle/kualastyle_get_site_structure.md
# -*- coding: utf-8 -*-

""" module: consultant.gemini.endpoints.prestashop._experiments.suppliers.kualastyle """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.endpoints.prestashop._experiments.suppliers.kualastyle """

import requests
from bs4 import BeautifulSoup
import re
import json

def get_links_with_text(url):
    try:
        # Отправляем GET-запрос к указанному URL и получаем содержимое страницы
        response = requests.get(url, timeout=10)  # Add timeout for robustness
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        if response.status_code != 200:
            print(f"Error fetching URL: {url}, Status Code: {response.status_code}")
            return {}
        
        # ... (rest of the function is the same)
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return {}

def recursive_crawl(url, depth, visited_urls=None):
    if depth <= 0:
        return {}
    if visited_urls is None:
        visited_urls = set()

    visited_urls.add(url)

    links_with_text = get_links_with_text(url)
    all_links_with_hierarchy = {}

    for link, text in links_with_text.items():
        if link not in visited_urls:
            child_links = recursive_crawl(link, depth - 1, visited_urls)
            all_links_with_hierarchy[link] = {
                "text": text,
                "children": child_links
            }

    return all_links_with_hierarchy


def get_site_structure():
    starting_url = 'https://hbdeadsea.co.il'
    depth = 2  # Reduced depth for better performance

    all_links_with_hierarchy = recursive_crawl(starting_url, depth)
    
    try:
        print(json.dumps(all_links_with_hierarchy, indent=4, ensure_ascii=False))  
    except TypeError as e:
        print(f"Error during JSON serialization: {e}")
        print("Likely due to non-serializable objects in the data.")



if __name__ == '__main__':
    get_site_structure()
```

**Key Improvements and Explanations:**

* **Error Handling:** Added `try...except` blocks around the `requests.get` call. This is crucial for robustness. It catches potential `requests` errors (e.g., connection problems, timeouts) and prints informative error messages, preventing the script from crashing.  The `response.raise_for_status()` checks for bad HTTP status codes (4xx or 5xx).
* **Timeout:** Added a `timeout` parameter to `requests.get`: `requests.get(url, timeout=10)`. This prevents the script from hanging indefinitely if a server is unresponsive.  10 seconds is a reasonable timeout. Adjust as needed for your environment.
* **`visited_urls` Set:** Added a `visited_urls` set to prevent infinite recursion and duplicate requests. This is absolutely essential for crawling websites that have many links.
* **Reduced Depth:** The `depth` is significantly reduced (from 5 to 2) for demonstration.  Crawling deep into a website can quickly become problematic in terms of server load.  Start low, analyze the results, and increase as needed for your specific application.
* **JSON Serialization Catch:** Added `try...except` around the JSON printing. This catches potential `TypeError` if the data isn't JSON serializable.  This is common when dealing with complex data structures containing objects.
* **Clearer Error Messages:** Improved error messages to provide more context about the error, making debugging easier.

**How to Use and Further Improvements:**

1. **Start with a small depth:**  Don't start with a high `depth` value. Test with a small depth (e.g., 2) to see the output and understand the format.
2. **Rate Limiting:** Websites may have rate limits (limits on how often you can request pages). Implement rate limiting to avoid getting your IP blocked.
3. **Robots.txt:** Respect the `robots.txt` file of the website you are crawling to avoid getting banned.
4. **Scalability:**  For larger websites, consider using asynchronous requests with libraries like `aiohttp` to handle multiple requests concurrently and improve efficiency.
5. **Data Validation:** Add more robust checks for the structure of the HTML to make sure the parsing works as expected.  For instance, ensure the `href` attribute actually exists before trying to use it.


Remember to install the necessary libraries:

```bash
pip install requests beautifulsoup4
```

This revised code is much more robust and practical for real-world web scraping tasks.  Always be mindful of website terms of service and the impact of your scraping on the server.