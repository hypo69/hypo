rst
How to use the FacebookPromoter class
========================================================================================

Description
-------------------------
This code defines a `FacebookPromoter` class for automating the promotion of AliExpress products and events in Facebook groups.  It handles fetching items to promote, navigating to Facebook groups, posting messages/events, and avoiding duplicate promotions.  The class utilizes a WebDriver instance (`d`) for browser interaction and loads group data from JSON files. It includes error handling and logging for various operations.

Execution steps
-------------------------
1. **Initialization:** The `__init__` method initializes the promoter object with a WebDriver instance (`d`), a promoter identifier (e.g., 'aliexpress'), a list of paths to JSON files containing Facebook group data, and an optional flag (`no_video`) to disable videos in posts.  If no file paths are provided, it defaults to fetching them from a specified directory.

2. **Promotion Logic (`promote` method):** This method takes a `group` object (containing group data) and an `item` object (product/event data) as input.
    - It checks if the specified language and currency match the group's settings. If not, it returns.
    - Extracts the item's name (`item_name`) based on whether it's an event or a message.
    - Based on `is_event`, it either uses the `post_event` or `post_message` function to post the item. If either fails, it logs an error and returns `False`.
    - Updates the group's promotion data (`last_promo_sended`, `promoted_events`/`promoted_categories`). Saves the updated data to the JSON file.


3. **Group Processing (`process_groups` method):** This method iterates through the provided group data files.
    - Loads group data from JSON files.
    - For each group:
        - Checks if the promotion interval has passed. If not, skips the group.
        - Checks if the group's categories are relevant and if the group is active. If not, skips the group.
        - Fetches the item to promote using `get_category_item` based on the campaign and the promoter.
        - Checks if the item has already been promoted to this group. If yes, skips the group.
        - Navigates to the Facebook group using `get_event_url` (if it's an event) or the group URL.
        - Calls `promote` to perform the actual promotion.
        - If promotion is successful, saves the updated group data.
        - Introduces a random delay.


4. **Item Retrieval (`get_category_item` method):** This method dynamically fetches the item (product/event) based on the campaign name, group details, and the specified `promoter`. It handles different promotion types, like AliExpress campaigns.

5. **Interval Check (`check_interval` method):** This method determines if enough time has elapsed since the last promotion for a given group.

6. **Group Validation (`validate_group` method):**  Validates if a group object contains necessary attributes for promotion.


Usage example
-------------------------
.. code-block:: python

    from hypotez.src.endpoints.advertisement.facebook.promoter import FacebookPromoter
    from src.webdriver.driver import Driver
    from src import gs
    import time
    # ... (other imports and setup)

    # Create a WebDriver instance (replace with your setup)
    d = Driver()
    d.start_driver()

    # Create an instance of the FacebookPromoter class
    promoter = FacebookPromoter(d, 'aliexpress', gs.path.google_drive / 'facebook' / 'groups')


    # Example usage
    campaign_name = 'Spring2024'
    group_files = [ 'group1.json', 'group2.json' ]

    promoter.process_groups(
        campaign_name=campaign_name, group_file_paths=group_files
    )

    # ... (Handle promotion results and close the WebDriver)
    d.stop_driver()