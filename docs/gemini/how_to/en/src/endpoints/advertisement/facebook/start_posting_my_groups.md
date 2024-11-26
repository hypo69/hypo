## Usage Guide for `start_posting_my_groups.py`

This script automates the posting of advertisements to Facebook groups. It utilizes the `FacebookPromoter` class to manage the process, requiring a list of group details and campaign targets.

**File:** `hypotez/src/endpoints/advertisement/facebook/start_posting_my_groups.py`

**Prerequisites:**

* **Python 3.12:**  The script is explicitly targeting Python 3.12.
* **`venv`:**  The script uses a virtual environment (`venv`).  Ensure it's activated before running the script.
* **Dependencies:**  Install the required libraries (e.g., `selenium`, `chromedriver`) for the webdriver, as well as other libraries used in the `header`, `src.webdriver`, `src.endpoints.advertisement.facebook.promoter`, and `src.logger` modules.  You'll need to look in the `requirements.txt` file (or equivalent) to determine these.
* **`my_managed_groups.json`:**  This JSON file is crucial. It should contain a list of Facebook group details (IDs or other identifiable information) for targeting.  The script will read group information from this file.  The exact format of `my_managed_groups.json` is not specified, but it's likely a list of dictionaries, each containing group data.  Example:

```json
[
  { "group_id": "1234567890", "target_audience": "some_audience_data" },
  { "group_id": "0987654321", "target_audience": "some_other_audience_data" }
]
```


**How to Use:**

1. **Configure the `my_managed_groups.json` file:** Populate this file with the details of the Facebook groups where you want to post advertisements.

2. **Run the script:** Execute the Python script from your terminal:

   ```bash
   python start_posting_my_groups.py
   ```

   This will initiate the advertisement posting process. The script will attempt to connect to Facebook, load your group details, and then proceed with the posting of advertising campaigns.  The `campaigns` list (`['brands', ...]`) defines the categories of advertisements to run.

3. **Campaign Execution:** The script iteratively calls the `promoter.run_campaigns()` method within a `while True` loop. The campaign execution continues until manually interrupted (Ctrl+C). This is a significant design consideration because there are potentially lengthy or complex operations within this loop, such as connecting to Facebook, handling advertisements, and waiting for approvals or processing.

4. **Error Handling:** The `try...except KeyboardInterrupt` block gracefully handles interruptions from the user.  This is standard practice for programs that need to be easily stopped.

5. **Logging:** The script utilizes a logger (`logger`) for recording events, which will be helpful for monitoring the progress and tracking any issues.


**Important Considerations:**

* **Facebook API and Rate Limiting:** Be mindful of Facebook's API and rate limits. The script should be designed to respect these limits to avoid account restrictions.
* **`no_video = True`:** This parameter to the `FacebookPromoter` implies that you are likely to not use video content in your advertisements.  If you plan to use videos, remove this parameter.
* **Selenium/WebDriver:** The script uses Selenium and a webdriver (likely ChromeDriver) to interact with the Facebook website.  Ensure the ChromeDriver is in the correct location and is the compatible version for your Selenium installation.
* **Maintenance:** Regularly review and update `my_managed_groups.json` to reflect changes in your target groups.

**Further Customization:**

The script can be expanded by adding features for pausing, resuming, or scheduling campaigns.  Consider adding more sophisticated error handling, reporting on campaign performance, and potentially integrating it with other systems for broader marketing automation.

This guide gives a solid foundation for understanding the script's functionality.  If specific aspects of the underlying libraries or the `FacebookPromoter` class are unclear, refer to their respective documentation.