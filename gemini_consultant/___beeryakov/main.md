```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
## \file hypotez/src/___beeryakov/main.py
# ~~~~~~~~~~~~~
""" module: src.___beeryakov """
"""  KSP to GTables

@section libs imports:
  - gs 
  
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""

# ------------------------------
from __init__ import gs
from src.logger import logger, WebDriverException, pprint
from src.webdriver import Driver as d
from src.beeryakov.suppliers import ksp
import GSpreadsheet, GWorksheet
import time

# -------------------------------


def run():
    """
    Старт парсера
    """
    sh_id = '1ZcK74BCgWKVr4kODjPmSvjp5IyO0OxhXdbeHKWzLQiM'
    root_url = 'https://ksp.co.il'
    
    try:
        d.get(root_url)
        worlds_dic = ksp.get_worlds()

        sh = GSpreadsheet(sh_id)

        for url, ws_title in worlds_dic.items():
            ws = GWorksheet(sh, ws_title)
            
            # Crucial:  Clear the worksheet to prevent duplicates
            ws.clear_content()
            ws.header(ws_title, 'A1:Z1')  # Correct header specification
            
            try:
                d.get(url)
                subs = ksp.get_subs_from_world()

                for sub_url, category_title in subs.items():
                    d.get(sub_url)  # Navigate to each sub-category
                    
                    try:
                        ws.append_row(ws.category(category_title))
                        
                        brands = ksp.get_all_brands_list()
                        print(f"\t\t\t BRANDS:")
                        
                        for brand, qty in brands.items():
                            ws.append_row([brand, qty])  
                        
                        print(f'Added data for {category_title}')
                        time.sleep(2)  # Important delay to avoid rate limiting
                    except Exception as e:
                        logger.error(f"Error processing sub-category '{category_title}': {e}")

                print(f' ********************************')
            
            except Exception as e:
                logger.error(f"Error processing world '{ws_title}': {e}")
                # Important:  Handle errors gracefully
                continue # Skip to the next world if there's a problem

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")


# Example usage (uncomment if you want to run the function)
if __name__ == "__main__":
    run()
```

**Key Improvements and Explanations:**

* **Error Handling:** The code now includes `try...except` blocks at multiple levels (world, sub-category) to catch and log errors.  This is *critical* for robustness.  If one world or sub-category fails, the script doesn't crash; it logs the error and moves on.  This makes the script much more reliable.
* **`ws.clear_content()`:** This line is **absolutely essential**. It clears the worksheet before adding new data.  Without this, you'd get duplicate data.
* **`time.sleep(2)`:** Added a delay.  Web scraping often hits rate limits.  This small delay helps avoid getting blocked.  Adjust the delay if necessary.
* **Clearer Logging:** Improved error messages to include more context about which world or sub-category caused the problem.
* **`if __name__ == "__main__":` block:** This is good practice to ensure the `run()` function is called only when the script is executed directly, not when imported as a module.
* **Consistent `print` statements:** Improved the structure of print statements to enhance readability.
* **Corrected `header` function call:**  `ws.header(ws_title, 'A1:Z1')` is correct.

**How to Run:**

1.  **Install necessary libraries:**
    ```bash
    pip install gspread
    ```
    (Make sure you have the correct `gs` library, the `GSpreadsheet` and `GWorksheet` objects were probably imported from the `gspread` library).  Make sure you have the `chromedriver` installed.

2.  **Ensure your `venv` is activated.**

3.  **Run the script:**
    ```bash
    python your_script_name.py
    ```

**Important Considerations:**

* **Rate Limiting:** Be aware of the website's rate limits when scraping.  Use `time.sleep()` to avoid getting your IP blocked.
* **Robustness:** Always include error handling (try...except blocks) in web scraping scripts.  If the website structure changes, your script will be more resilient.
* **Website Structure:**  If the structure of the website changes, your `ksp` functions (`get_subs_from_world`, `get_all_brands_list`, etc.) need to be updated to reflect those changes.

This revised solution is significantly more robust and reliable than the original. Remember to adapt the `time.sleep()` value and the error handling strategy to the specific website and your needs. Always respect the website's terms of service and avoid overloading their servers.