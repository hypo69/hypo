```## File hypotez/src/endpoints/advertisement/facebook/promoter.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""\n.. module: src.endpoints.advertisement.facebook \n\t:platform: Windows, Unix\n\t:synopsis: module handles the promotion of messages and events in Facebook groups.\nIt processes campaigns and events, posting them to Facebook groups while avoiding duplicate promotions.\n\n"""\nMODE = \'dev\'\n\n...\nimport time\nimport random\nfrom datetime import datetime, timedelta\nfrom pathlib import Path\nimport re\nfrom urllib.parse import urlencode\nfrom types import SimpleNamespace\nfrom typing import Optional\n\nfrom src import gs\nfrom src.endpoints.advertisement import facebook\nfrom src.webdriver import Driver, Chrome\nfrom src.suppliers.aliexpress.campaign import AliCampaignEditor\nfrom src.endpoints.advertisement.facebook.scenarios import (post_message, \n                                                  post_event, \n                                                  post_message_title, \n                                                  upload_post_media,\n                                                  message_publish,\n                                                  post_ad,\n                                                    )\n\nfrom src.utils import (read_text_file,\n                        get_filenames,\n                        get_directory_names,\n                        )\nfrom src.utils import j_loads_ns, j_dumps\nfrom src.utils.cursor_spinner import spinning_cursor\nfrom src.logger import logger\n\ndef get_event_url(group_url: str) -> str:\n    """\n    Returns the modified URL for creating an event on Facebook, replacing `group_id` with the value from the input URL.\n\n    Args:\n        group_url (str): Facebook group URL containing `group_id`.\n        event_id (str): Event identifier.\n\n    Returns:\n        str: Modified URL for creating the event.\n    """\n    group_id = group_url.rstrip(\'/\').split(\'/\')[-1]\n    base_url = "https://www.facebook.com/events/create/"\n    params = {\n        "acontext": \'{"event_action_history":[{"surface":"group"},{"mechanism":"upcoming_events_for_group","surface":"group"}],"ref_notif_type":null}\',\n        "dialog_entry_point": "group_events_tab",\n        "group_id": group_id\n    }\n\n    query_string = urlencode(params)\n    return f"{base_url}?{query_string}"\n\nclass FacebookPromoter:\n    """ Class for promoting AliExpress products and events in Facebook groups.\n    \n    This class automates the posting of promotions to Facebook groups using a WebDriver instance,\n    ensuring that categories and events are promoted while avoiding duplicates.\n    """\n    d:Driver = None\n    group_file_paths: str | Path = None\n    no_video:bool = False\n    promoter:str\n\n    def __init__(self, d: Driver, promoter: str, group_file_paths: Optional[list[str | Path] | str | Path] = None, no_video: bool = False):\n        """ Initializes the promoter for Facebook groups.\n\n        Args:\n            d (Driver): WebDriver instance for browser automation.\n            group_file_paths (list[str | Path] | str | Path): List of file paths containing group data.\n            no_video (bool, optional): Flag to disable videos in posts. Defaults to False.\n        """\n        self.promoter = promoter\n        self.d = d\n        self.group_file_paths = group_file_paths if group_file_paths else get_filenames(gs.path.google_drive / \'facebook\' / \'groups\')\n        self.no_video = no_video\n        self.spinner = spinning_cursor()\n```

2. <algorithm>

```mermaid
graph TD
    A[Input: Campaign Name, Events (optional), Group Files, Language, Currency] --> B{Initialization};
    B --> C[Load Group Data];
    C --> D[Iterate through Groups];
    D --> E{Check Interval};
    E -- Yes --> F{Check Categories/Event, Language, Currency Match};
    E -- No --> D;
    F -- Yes --> G[Get Item (Category or Event)];
    F -- No --> D;
    G --> H{Check Duplicates};
    H -- No --> I[Navigate to Group];
    H -- Yes --> D;
    I --> J[Promote Item];
    J -- Success --> K[Update Group Data];
    J -- Failure --> D;
    K --> L[Save Group Data];
    L --> M[Delay];
    M --> D;
    D --> N[End of Groups?];
    N -- Yes --> O[End];
    N -- No --> D;
```

**Examples:**

* **B (Initialization):**  `FacebookPromoter(driver, 'aliexpress', ['group1.json', 'group2.json'])`
* **C (Load Group Data):** Loads JSON data for groups from specified files into `SimpleNamespace` objects.
* **E (Check Interval):** Checks if the last promotion time is within the specified interval for the group. Example: If `group.interval` is '1H' and last promotion was 1 hour ago, interval is met.
* **G (Get Item):**  Retrieves promotion item (category or event) from a JSON file based on the campaign and group's language/currency.
* **H (Check Duplicates):** Verifies if the item has already been promoted to this group.
* **J (Promote Item):** Uses the `post_message` or `post_event` functions from the `scenarios` module to post the item to the group in Facebook.  Example: `post_message(d=self.d, message=item, no_video=self.no_video)`
* **K (Update Group Data):** Updates the `group` data structure to store the promotion history, including the last promotion time and list of promoted items (categories/events).

3. <explanation>

**Imports:**

*   `time`, `random`, `datetime`, `timedelta`, `pathlib`, `re`, `urllib.parse`, `types`, `typing`: Standard Python libraries for time management, random selection, date/time manipulation, file system interaction, regular expressions, URL parsing, type hinting.
*   `gs`: Likely a custom module (`src.gs`) for Google Drive interaction (file system paths and loading).
*   `facebook`:  A `src` module for Facebook-related functions (Likely, but not specified).
*   `Driver`, `Chrome`:  Classes from the `src.webdriver` module for browser automation.
*   `AliCampaignEditor`: A class from `src.suppliers.aliexpress.campaign` for handling AliExpress campaigns.
*   `post_message`, `post_event`, etc.: Functions from the `src.endpoints.advertisement.facebook.scenarios` module for posting messages/events on Facebook.
*   `read_text_file`, `get_filenames`, `get_directory_names`: Utilities from the `src.utils` module (for file operations and potentially for other purposes).
*   `j_loads_ns`, `j_dumps`: Likely custom JSON parsing/dumping functions from the `src.utils` module handling `SimpleNamespace` objects (more explicit conversion and handling than standard json).
*   `spinning_cursor`:  A spinner function from the `src.utils.cursor_spinner` module for a visual feedback during the process (progress indication).
*   `logger`: A logger from `src.logger` module for logging.

**Classes:**

*   `FacebookPromoter`: Manages the promotion of categories/events.
    *   `d`: WebDriver instance, required for interacting with the browser.
    *   `group_file_paths`: File paths to JSONs storing group information.
    *   `no_video`: Controls whether to disable videos in posts.
    *   `promoter`: String indicating the source of promotion (e.g., 'aliexpress').
    *   `__init__`: Initializes the promoter with a driver, promoter type, group file list, and no_video flag.  Crucially, if `group_file_paths` is not given it automatically reads group data from a pre-defined directory.
    *   `promote`: The core logic for posting an item to a specific group, checking for language and currency matches, and avoiding duplicates.
    *   `log_promotion_error`: Logs errors during promotion attempts.
    *   `update_group_promotion_data`: Updates promotion history for a group after successful promotion.
    *   `process_groups`: Handles promotion across multiple groups in a campaign.
    *   `get_category_item`: Fetches categories based on `self.promoter`.
    *   `check_interval`: Checks if the time interval for the next promotion is met. Uses `parse_interval` to convert string to `timedelta` for easier comparison.
    *   `parse_interval`: Parses interval strings like '1H' or '6M' into `timedelta` objects.
    *   `run_campaigns`: Runs promotion for specified campaigns.
    *   `run_events`: Runs promotion for specified events.
    *   `stop`: Quits the WebDriver instance.

**Functions:**

*   `get_event_url`: Creates the URL for Facebook event creation within a group.
*   `check_interval`: Checks if the defined interval has passed between promotions.  Error handling for bad input is critical.
*   `parse_interval`: Takes a string ("1H", "6M") and returns a `timedelta` object, handling parsing errors.


**Variables:**

*   `MODE`:  A global variable indicating the mode (e.g., 'dev', 'prod').
*   `group`: `SimpleNamespace` object representing group data loaded from JSON (contains group URL, categories, language, currency, etc.).
*   `item`: `SimpleNamespace` representing campaign category or event data.


**Potential Errors/Improvements:**

*   **Error Handling:** More robust error handling (e.g., `try...except` blocks) is needed for file reading, URL parsing, and other potential issues.  Checking for empty or malformed JSON data is vital.
*   **Logging:**  Clearer logging of successes and failures would enhance debugging and monitoring.
*   **Robustness:**  The `parse_interval` function is a good example of handling different string formats.  More checks should be added to ensure data integrity.
*   **Concurrency:** Promoting across many groups can be slow. Threading or multiprocessing could improve performance.
*   **Rate Limiting:** Facebook has API limits; rate limiting should be implemented to avoid getting blocked.
*   **Testability:** Adding unit tests for individual functions would improve code quality.
*   **Data Structure:** Using a more structured data model (e.g., a database) to store and manage campaign and group data instead of relying solely on JSON files could improve scalability and maintainability in a larger application.
*   **External Dependencies:** Using `requests` and/or other libraries for API calls instead of webdriver may be more efficient and less error-prone.


**Relationships:**

This code interacts with several other parts of the project:

*   `src.gs`: For Google Drive file system interaction.
*   `src.webdriver`: For browser automation.
*   `src.endpoints.advertisement.facebook`: Likely related functionality.
*   `src.suppliers.aliexpress.campaign`: For accessing AliExpress data.
*   `src.utils`: For general utility functions.
*   `src.endpoints.advertisement.facebook.scenarios`: For actions to be taken on Facebook (message posting, event creation, etc.).
*   `src.logger`: For logging promotion events.


The project structure suggests a modular architecture with a well-defined workflow for advertising operations, which includes loading data, validating inputs, automating actions on Facebook, recording and reporting outcomes. The emphasis is on data persistence and campaign management, leveraging external APIs for promotion tasks.