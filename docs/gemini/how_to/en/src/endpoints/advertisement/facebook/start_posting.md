## Usage Guide for `hypotez/src/endpoints/advertisement/facebook/start_posting.py`

This script automates the posting of advertisements to Facebook groups.  It utilizes the `FacebookPromoter` class to manage the campaign process.

**How to use:**

1. **Prerequisites:**
   - **Python Environment:** Ensure you have Python 3.12 installed and a virtual environment (`venv`) activated. The script requires the `venv/bin/python` path for execution.
   - **Dependencies:** The script relies on the `header`, `time`, `copy`, `webdriver`, `FacebookPromoter` (from `src.endpoints.advertisement.facebook`), and `logger` modules. Ensure these are correctly installed within your virtual environment.  If you have a `requirements.txt` file, use `pip install -r requirements.txt` to install the needed libraries.  Check the `src` directory for possible custom modules.
   - **ChromeDriver:** If you are using Chrome WebDriver, make sure the ChromeDriver executable is in your PATH environment variable or specify the path explicitly. The script uses a `Driver` and `Chrome` class.
   - **JSON Files:** The script expects JSON configuration files (e.g., `usa.json`, `he_ils.json`) in a specified directory (likely within the `src` folder). These files likely contain data about target groups and advertising settings.  The `filenames` variable defines which files to use.


2. **Script Execution:**

   ```bash
   # Replace with the actual path if necessary.
   python hypotez/src/endpoints/advertisement/facebook/start_posting.py 
   ```

3. **Configuration:**
   - **`filenames`:**  This list specifies the JSON file paths containing Facebook group data.  Modify this list if you have different files or need to exclude some.
   - **`excluded_filenames`:**  This list controls which files are *not* processed. Modify this list as needed.
   - **`campaigns`:** This list defines the advertising campaign types.  Change these values to run different campaigns.
   - **`MODE`:** Currently set to `'dev'`.  This likely controls debugging versus production behavior.

4. **`FacebookPromoter` Methods:**
   - The `FacebookPromoter` class is the core of the script.  It handles interactions with Facebook.  Crucially, you need to ensure it is correctly setup.  Within `FacebookPromoter` method, you will probably have:
     - `group_file_paths`: The files that contain the data for which groups to advertise.
     - `no_video`: Setting this `True` likely indicates that video ads should not be run.
     - `run_campaigns`: This is the method that actually performs the posting. It uses the `campaigns` and `group_file_paths` provided.


5. **Loop and Error Handling:**
   - The `while True` loop continuously runs the campaigns.  This implies the script is designed to run indefinitely.
   - The `try...except KeyboardInterrupt` block allows you to safely interrupt the script via Ctrl+C without crashing the program.


**Important Considerations:**

- **Facebook API Limits:**  Be extremely mindful of Facebook's API limits and rate restrictions. Excessive or inappropriate usage could lead to account restrictions. Implement appropriate delays between actions (currently set at 180 seconds) to avoid potential issues.
- **Error Handling:** The code includes basic error handling for `KeyboardInterrupt`.  You should add robust error handling for potential issues (e.g., network problems, API errors, JSON decoding errors) within the `run_campaigns` method of `FacebookPromoter`.
- **Security:**  Avoid hardcoding sensitive information (e.g., API keys) directly into the script. Use environment variables or configuration files for secure storage.
- **Logging:** The `logger` module is used.  Review its implementation to ensure appropriate logging levels are in place.
- **File Paths:**  The file paths for the JSON configuration files are important and are likely hardcoded.  Review and potentially modify them for different locations.


**Further Development:**

- Implement more sophisticated error handling.
- Add logging to provide more details on the campaign progress and any issues encountered.
- Incorporate mechanisms to handle Facebook account logins and authentication (e.g., using `facebook-sdk` or similar libraries).
- Implement scheduling to run the script automatically at specific times.
- Add a mechanism to check if campaigns have successfully run or require re-running.


By addressing these points, you can make the script more robust, efficient, and secure for production use. Remember to thoroughly test each feature and configuration to ensure the script behaves as intended. Remember to review and potentially modify parameters based on the implementation of `FacebookPromoter`.