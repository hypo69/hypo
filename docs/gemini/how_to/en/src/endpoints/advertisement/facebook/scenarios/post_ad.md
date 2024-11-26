# Usage Guide for post_ad.py

This guide explains how to use the `post_ad` function to post advertisements on Facebook groups using Selenium.

**File:** `hypotez/src/endpoints/advertisement/facebook/scenarios/post_ad.py`

**Function:** `post_ad(d: Driver, message:SimpleNamespace) -> bool`

**Purpose:** This function posts an advertisement, potentially including a title and image, to a Facebook group.

**Parameters:**

*   `d (Driver)`: A Selenium WebDriver instance (`src.webdriver.Driver`) initialized and configured to interact with the Facebook group page. **Crucially, this driver needs to be correctly authenticated and navigated to the intended group.**
*   `message (SimpleNamespace)`: A `SimpleNamespace` object containing advertisement details.  It's expected to have the following attributes:
    *   `description (str)`: The advertisement's text content.
    *   `image_path (str, optional)`: The path to an image file to be uploaded with the post.  If omitted, no image will be uploaded.

**Return Value:**

*   `True`: If the advertisement was posted successfully.
*   `None` (implicitly): If the posting process fails (and fails are < 15 attempts).  After 15 consecutive failures, the function will not return anything.  The code includes error handling (logging) but does not provide a clear way to handle this failure.


**How to use:**

1.  **Initialization:** Instantiate a `Driver` object, authenticating with the Facebook account and navigating to the target Facebook group page.  The `Driver` class is assumed to handle session management, login, etc. (details not shown in this snippet)

2.  **Create message object:** Create a `SimpleNamespace` object (`message`) holding the advertisement details.  This object should contain the text you want to post (`message.description`) and the path to the image file to upload (`message.image_path`), if applicable.

3.  **Call `post_ad`:** Call the `post_ad` function, passing the `Driver` object and the `message` object.

```python
from hypotez.src.endpoints.advertisement.facebook.scenarios.post_ad import post_ad
from src.webdriver import Driver
from types import SimpleNamespace


# ... (Driver initialization and authentication) ...

message = SimpleNamespace(
    description="This is my advertisement!",
    image_path="/path/to/image.jpg"  # Optional image path
)

if post_ad(driver, message):
    print("Advertisement posted successfully!")
else:
    print("Advertisement posting failed.")
```

**Error Handling and Retry Logic:**

*   The function includes a `fails` counter. It attempts to post the advertisement up to 15 times if errors occur.  After 15 failures, it effectively stops. This behavior should be carefully considered and potentially modified to allow for more sophisticated recovery strategies.

*   Logging is used (`logger.error`) to record any errors during the process.  This is essential for troubleshooting. However, the example shows `exc_info=False`, which may be causing information loss. Using `exc_info=True` is strongly advised for debugging.


**Important Considerations:**

*   **Robust Error Handling:** The current error handling needs improvement.  It's crucial to handle potential exceptions (e.g., `TimeoutException`, `NoSuchElementException`, network errors) more comprehensively to prevent the script from crashing.
*   **Driver Management:**  Ensure the `Driver` object is properly managed (closed/quit) after use to prevent resource leaks.
*   **Image Handling:**  The code assumes the `image_path` points to a valid image file.  Error handling should be added to check if the file exists and handle potential exceptions during image upload.
*   **Facebook API:** Consider using the Facebook API for more robust and efficient advertisement posting instead of relying on Selenium.  This is generally recommended for production-level applications.


This guide provides a basic understanding.  Thorough testing and adjustments based on your specific Facebook environment are necessary for reliable execution.