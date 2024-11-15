## \file hypotez/consultant/gemini/endpoints/prestashop/_experiments/suppliers/kualastyle_get_site_structure.md
# -*- coding: utf-8 -*-

""" module: consultant.gemini.endpoints.prestashop._experiments.suppliers """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.endpoints.prestashop._experiments.suppliers """

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
            print(f"Error fetching URL: {url}, status code: {response.status_code}")
            return {}
        
        # Создаем объект BeautifulSoup для анализа содержимого страницы
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Находим все ссылки на странице
        links = soup.find_all('a', href=True)
        
        # Создаем словарь, где ключ - это ссылка, а значение - текст ссылки.  
        # Фильтруем ссылки, которые начинаются с https://hbdeadsea.co.il/product-category
        # и проверяем, что link['href'] существует
        links_with_text = {
            link['href']: link.text.strip()
            for link in links
            if link.get('href') and link['href'].startswith('https://hbdeadsea.co.il/product-category')
        }
        return links_with_text
    except requests.exceptions.RequestException as e:
        print(f"Error accessing URL: {url}, error: {e}")
        return {}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}



def recursive_crawl(url, depth):
    if depth <= 0:
        return {}
    
    links_with_text = get_links_with_text(url)
    all_links_with_hierarchy = {}
    for link, text in links_with_text.items():
        # Рекурсивно вызываем функцию для каждой найденной ссылки на указанной глубине
        child_links = recursive_crawl(link, depth - 1)
        all_links_with_hierarchy[link] = {
            "text": text,
            "children": child_links
        }
    
    return all_links_with_hierarchy

def get_site_structure():
    # Укажите URL, с которого начнется сбор ссылок
    starting_url = 'https://hbdeadsea.co.il'
    
    # Укажите глубину рекурсии (сколько уровней ссылок будет рекурсивно собрано)
    depth = 2  # Reduced for demonstration.  Increase cautiously
    
    # Запускаем сбор ссылок рекурсивно
    all_links_with_hierarchy = recursive_crawl(starting_url, depth)
    
    # Обработка ошибки: если словарь пустой, то выводим сообщение.
    if not all_links_with_hierarchy:
        print("No data found or there was an error during crawling.")
        return
    
    # Выводим результаты в виде словаря с иерархией
    try:
        print(json.dumps(all_links_with_hierarchy, indent=4, ensure_ascii=False))
    except Exception as e:
        print(f"Error printing JSON: {e}")


if __name__ == '__main__':
    get_site_structure()
```

**Key improvements and explanations:**

* **Error Handling:** The code now includes `try...except` blocks to handle potential errors during the request (e.g., connection problems, invalid URLs), HTTP errors from the server (4xx or 5xx responses), and other exceptions.  This is *critical* for robustness.  It prints informative error messages. The `timeout` parameter in `requests.get` is added for timeout handling.
* **Robustness:**  `link.get('href')` is used to safely access the attribute and handle cases where `link['href']` might not exist. This prevents crashes.
* **Reduced Depth:**  The default depth is reduced (to 2 for the example). Crawling too deep can quickly overload the site and/or your program. You should start with a smaller depth and increase it only if needed.
* **Checking for Empty Result:** Checks if `all_links_with_hierarchy` is empty before printing, giving a more user-friendly message if there's an error.
* **JSON Error Handling:** Includes a `try...except` block to catch potential errors while formatting the JSON output. This makes the script more resilient to unexpected issues.
* **Filtered Links:** The script now filters the `links` list, including a more restrictive condition. It ensures that only links starting with `https://hbdeadsea.co.il/product-category` are processed, preventing issues with incorrect link structures and potentially speeding up the process.
* **`raise_for_status()`:** Includes `response.raise_for_status()` to immediately raise an exception for bad HTTP responses (4xx or 5xx). This is a more Pythonic way to handle errors in a request.

**How to use it:**

1.  **Install necessary libraries:**
    ```bash
    pip install requests beautifulsoup4
    ```

2.  **Run the script:**
    ```bash
    python your_script_name.py
    ```

This improved version is significantly more reliable and less prone to crashing due to unexpected situations. Remember to adjust the `depth` parameter based on the actual site structure and your needs.