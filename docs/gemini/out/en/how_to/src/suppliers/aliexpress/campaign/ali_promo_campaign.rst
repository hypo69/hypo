rst
How to use the `AliPromoCampaign` class
========================================================================================

Description
-------------------------
This Python code defines a class `AliPromoCampaign` for managing advertising campaigns on AliExpress.  It handles loading and processing campaign data, managing categories and products, generating campaign information in JSON format, and utilizing AI for data generation.  The class allows for flexibility in language and currency settings. It also provides methods to create a new campaign from scratch if a JSON configuration file is missing. This includes processing affiliate products and saving data in various formats (JSON, HTML).


Execution steps
-------------------------
1. **Import necessary modules:** The code imports various libraries like `asyncio`, `time`, `copy`, `html`, `pathlib`, `typing`, and modules from the `src` directory.  These are essential for file handling, asynchronous operations, data manipulation, and AI integration.

2. **Define the `AliPromoCampaign` class:** This class encapsulates the logic for managing a single campaign. It includes attributes to store campaign details, language, currency, path, AI models, and the campaign data itself.

3. **`__init__` method:** This constructor initializes the `AliPromoCampaign` object. It takes the campaign name, language, and currency as arguments.  Critically, it attempts to load an existing campaign JSON file. If the file doesn't exist, it triggers the creation of a new campaign using the `process_new_campaign` method.

4. **`_models_payload` method:** This method initializes and configures the AI models (currently Google Generative AI). It's crucial for AI-driven campaign processing.

5. **`process_campaign` method:** This method iterates through each category within the campaign, processes affiliate products, and invokes AI processing for each category. This involves reading category names, fetching product information for each category, and triggering AI processing.

6. **`process_category_products` method:** This method fetches product IDs within a specific category, and uses `AliAffiliatedProducts` to retrieve affiliated product data.  If no product IDs are found, an error is logged, and `None` is returned. This step is crucial for generating and processing information about products.

7. **`process_ai_category` method:** This method handles AI processing for a given category. It generates prompts based on product titles and feeds them to the initialized AI models. It then updates/creates categories with the AI-generated data.  This step utilizes AI to generate descriptions and other relevant campaign information.

8. **`process_new_campaign` method:** This method is triggered if no campaign data file is found.  It sets up a new campaign by creating directories and files for categories, products, and potentially handling the initial loading of source data.  This is a fundamental step for creating new campaigns from scratch.

9. **`generate_output` method:** This method saves various outputs of the processing (JSON product files, title lists, promotion link lists, and HTML). It also creates an index.html for the campaign, listing the categories. This is how the results are made accessible for further use.


Usage example
-------------------------
```python
from hypotez.src.suppliers.aliexpress.campaign import ali_promo_campaign
import asyncio

async def main():
    campaign = ali_promo_campaign.AliPromoCampaign(campaign_name="MyCampaign", language="EN", currency="USD")
    # Important: Replace "your_category_name" with the actual category name.
    await campaign.process_category_products("Electronics")
    await campaign.process_ai_category("Electronics")
    
    # Example of calling the generate_output method.  Note the async nature.
    await campaign.generate_output("MyCampaign", "path/to/your/output/directory", products)
    # ... further processing of products ...

asyncio.run(main())
```

**Explanation of the example:**

This example demonstrates how to create an instance of `AliPromoCampaign` with a specific campaign name, language, and currency. Then it showcases how to call asynchronous methods `process_category_products` and `process_ai_category` for a category.  Crucially, it demonstrates how to then call the `generate_output` method to save the results in a directory.  You need to replace `"path/to/your/output/directory"` with the actual path to save your results.


**Important Considerations:**

-   **Asynchronous operations:**  The `AliPromoCampaign` class utilizes `asyncio`, so you need to use `asyncio.run()` to execute the code correctly, as shown in the example.
-   **Error Handling:** The code includes some basic error handling, but robust error checking and handling should be added for production use.
-   **AI Model Setup:** The code includes placeholders for the AI model initialization. You need to replace the example with the appropriate instantiation and configuration for your AI models.
-   **File Paths:** Ensure the file paths (`gs.path`) are correctly configured in your `header` and `gs` modules to match your file system structure.

This comprehensive guide provides a clear structure for understanding and using the `AliPromoCampaign` class. Remember to adapt the example to your specific needs and file system setup.