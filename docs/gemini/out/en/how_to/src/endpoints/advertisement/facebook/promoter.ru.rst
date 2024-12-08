rst
How to use the Facebook Promoter module
========================================================================================

Description
-------------------------
The `Facebook Promoter` module automates the promotion of AliExpress products and events within Facebook groups.  It manages the posting of promotional materials on Facebook, avoiding duplication.  The module utilizes WebDriver for automated browser interaction.

Execution steps
-------------------------
1. **Import necessary modules:** Import the `FacebookPromoter` class from the `src.endpoints.advertisement.facebook.promoter` module, the `Driver` class from `src.webdriver.driver`, and the `j_loads_ns` function from `src.utils.jjson`.

2. **Initialize WebDriver:** Create an instance of the `Driver` class, replacing `"path/to/chromedriver"` with the actual path to your ChromeDriver executable. This step is crucial for browser automation.

3. **Create a FacebookPromoter instance:** Instantiate the `FacebookPromoter` class, providing the WebDriver instance (`d`), the promoter name (`promoter`), and a list of file paths (`group_file_paths`) containing the group data in JSON format. Optionally, specify `no_video` to disable video uploads.

4. **Process groups:** Call the `process_groups` method on the `FacebookPromoter` instance. This method takes various parameters, allowing you to specify the campaign name, events to promote, groups categories to promote, and language and currency settings.

5. **Promotion logic (internal):**
   - The `process_groups` method iterates through each group.
   - It checks if the group data is valid.
   - It fetches a promotional item (category or event).
   - It verifies if the group can be promoted again based on a defined interval.
   - It promotes the item in the group, handling possible errors.
   - It updates the group's promotion data.
   - If errors occur during promotion, it logs the errors.

6. **Campaign completion:** The module completes the promotion process, indicating success or failure.


Usage example
-------------------------
.. code-block:: python

    from src.endpoints.advertisement.facebook.promoter import FacebookPromoter
    from src.webdriver.driver import Driver
    from src.utils.jjson import j_loads_ns
    import pathlib

    # Replace with the actual path to your chromedriver
    chromedriver_path = pathlib.Path("./chromedriver")

    # Initialize WebDriver (replace with your webdriver setup)
    d = Driver(chromedriver_path=chromedriver_path)

    # Create a FacebookPromoter instance
    promoter = FacebookPromoter(
        d=d,
        promoter="aliexpress",
        group_file_paths=["path/to/group/file1.json", "path/to/group/file2.json"],
        no_video=True  # Disable video uploads
    )

    # Start promoting products or events
    promoter.process_groups(
        campaign_name="Campaign1",
        events=[],  # List of events to promote (optional)
        group_categories_to_adv=["sales"],
        language="en",
        currency="USD"
    )