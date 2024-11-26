How to use the `emil_design.py` script

This guide explains how to use the `emil_design.py` script, which handles image design, description, promotion to Facebook, and upload to PrestaShop.

**1. Project Structure and Dependencies:**

The script assumes a specific project structure.  Crucially, it relies on various modules and libraries, including:

*   `src.gs`: likely handles Google Services (e.g., Google Drive).
*   `src.logger`:  A custom logging module.
*   `src.endpoints.PrestaShop.api.api`:  A PrestaShop API client.
*   `src.webdriver`: A webdriver module (likely for browser automation).
*   `src.ai.gemini`, `src.ai.openai.model`:  AI models (likely Gemini and OpenAI).
*   `src.product`: A product handling module.
*   `src.endpoints.advertisement.facebook.scenarios.post_message`: Facebook posting functions.
*   `src.utils.file`, `src.utils.jjson`: Utility functions for file I/O and JSON handling.

**Ensure all these dependencies are installed and correctly configured.**  The shebang lines (`#! venv/Scripts/python.exe`) point to the correct Python interpreter within a virtual environment (recommended).

**2. Data Preparation:**

*   **Image Directory:**  The script expects images to be placed in a directory under the base path, specified by `gs.path.google_drive / "emil" / "images"`.
*   **Instructions and Examples:** The script uses text files (`hand_made_furniture_he.txt`, `examples_he.txt`) for AI instructions and examples related to the images.  Ensure these are in the specified `emil`  directory under `instructions`.
*   **Updated Images:** The `updated_images.txt` file tracks images already processed. This prevents redundant processing.  The script initializes or reads the content of this file.


**3. Running the `describe_images` function:**

```python
e = EmilDesign()
e.describe_images(from_url=False) # use images from local directory
```
  
*   **`from_url=False`:** This is the default and uses the local images.  If you have image URLs, set `from_url=True` to describe images from the provided URLs.
*   **Error Handling:** The code includes `if not response:` checks.  Critically, this script needs robust error handling.  If an API call or AI request fails, the program might continue processing the rest of the images incorrectly.  You should implement proper error logging and potentially retry mechanisms.
*   **Important:**  Ensure that the OpenAI API key is properly configured.  The script hardcodes `'asst_uDr5aVY3qRByRwt5qFiMDk43'` as an assistant ID.  You must update the assistant_id if your OpenAI model is different.
* **`images_descritions_he.json`:**  The output will be a JSON file containing descriptions for each image at the specified `base_path`.


**4. Running the `promote_to_facebook` function:**

```python
e.promote_to_facebook()
```

*   **Facebook Login:** The script uses a webdriver (`Driver(Chrome)`) to automate interactions with Facebook.  **This requires a webdriver capable of logging into Facebook.**  This is often the most complex part to setup. Ensure that the Facebook account has proper permissions set up.
*   **Important:**  Modify the Facebook group URL (`https://www.facebook.com/groups/1080630957030546`) as necessary.
*   **`images_descritions_he.json`:** This function relies on the data created by the `describe_images` step.

**5. Running the `upload_to_PrestaShop` function:**

```python
e.upload_to_PrestaShop()
```

*   **PrestaShop Configuration:** Ensure that you have the necessary configurations for connecting to PrestaShop.

**Important Considerations:**

*   **Error Handling:**  Implement comprehensive error handling for all API calls and AI requests.
*   **Rate Limiting:** Be mindful of rate limits for the API services being used (OpenAI, Facebook).  Insert delays where appropriate to prevent being throttled.
*   **Robustness:**  The script's structure should be improved for robust error handling, input validation, and potential retries.
*   **Security:**  Do not hardcode API keys or credentials directly into your code. Use environment variables or configuration files.
*   **Testing:**  Thoroughly test the script with sample data to ensure it works as expected.
*   **Timeouts:**  Add proper timeouts to avoid indefinite waits.

This enhanced guide provides a more detailed and actionable explanation of how to use the code, emphasizing the critical steps and potential issues. Remember to adapt these instructions to your specific environment and project requirements.