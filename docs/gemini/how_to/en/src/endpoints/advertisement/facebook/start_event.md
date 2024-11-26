# Usage Guide for `start_event.py`

This script automates the posting of events to Facebook groups.  It uses a Facebook API wrapper and WebDriver to interact with the platform.

**File:** `hypotez/src/endpoints/advertisement/facebook/start_event.py`

**Purpose:**  Schedule and publish events in specified Facebook groups.

**Prerequisites:**

* **Python 3.12:**  Ensure you have Python 3.12 installed and accessible via the `python3.12` executable (as specified in the shebang).
* **venv:** The script relies on a virtual environment (`venv`).  Make sure it's activated before running the script.
* **Dependencies:**  The `header.py`, `jjson.py`, `webdriver.py`, `FacebookPromoter.py` and `logger.py` modules are required and are expected to be in the correct import paths.  Install any missing packages via `pip install -r requirements.txt` (if one exists).
* **JSON Files:** The script expects JSON files containing group details (IDs or URLs) for publishing events. The files (`my_managed_groups.json`, `usa.json`, etc.) must exist in the project's file structure, alongside the Python script.
* **ChromeDriver/GeckoDriver:** If using Chrome/Gecko, make sure the appropriate WebDriver executable is in the PATH or specified appropriately.
* **Facebook Account:** The script requires login credentials to access the Facebook platform (implicitly through the `FacebookPromoter` class and the webdriver interactions).  Security is crucial. Consider using secure authentication methods if this script is deployed for production.

**How to Run:**

1. **Activate your virtual environment:**
   ```bash
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

2. **Run the script:**
   ```bash
   python hypotez/src/endpoints/advertisement/facebook/start_event.py
   ```

**Explanation:**

* **`MODE = 'dev'`:**  Indicates the script's mode (likely for development or testing).  This variable might control logging levels or other behavior.
* **`filenames` & `excluded_filenames`:** Lists the JSON files containing Facebook group data.  `excluded_filenames` are omitted during the process.
* **`events_names`:**  A list of event names to be posted.
* **`FacebookPromoter`:**  Custom class for Facebook API interaction.  Ensure this class is correctly handling all the API requests, including handling potential errors during Facebook login.
* **`while True` loop:** The script enters an infinite loop, continuously checking and posting events.  Very important: the loop relies on the `time.sleep(7200)` to avoid excessive load on the Facebook API. Be cautious of rate limits.
* **`KeyboardInterrupt`:** The `try...except` block handles Ctrl+C to allow for safe termination of the script.
* **Logging:** The script uses a logger (`logger.debug`, `logger.info`) for tracking progress and errors.

**Customization:**

* **`filenames`:** Change the list of JSON files to target different groups.  Update the file paths to the correct names and locations.
* **`events_names`:**  Add or remove event names to publish.
* **`time.sleep(7200)`:** Adjust the sleep interval (7200 seconds = 2 hours) as needed to control frequency of publishing.  Monitor the API usage and adjust the sleep time to comply with Facebook's rate limits and prevent being blocked.

**Error Handling and Debugging:**

* **`FacebookPromoter` errors:**  The `FacebookPromoter` class should handle potential errors (e.g., invalid group IDs, authentication failures) gracefully and log them appropriately.  Add robust error handling to the `promoter.run_events` method.
* **Logging:** Use the logger effectively for debugging.  Monitor the log files for errors and exceptions.

**Important Considerations:**

* **API Rate Limiting:** Be mindful of Facebook's API rate limits to prevent your application from being blocked.
* **Security:**  Do not hardcode credentials directly into the script. Consider using environment variables or secure configuration files for authentication credentials.


This guide provides a high-level overview.  Detailed information on the structure and functionality of `header.py`, `jjson.py`, `webdriver.py`, and `FacebookPromoter.py` is required to fully understand the implementation and potential points of failure. Remember to consult the documentation of the external libraries.