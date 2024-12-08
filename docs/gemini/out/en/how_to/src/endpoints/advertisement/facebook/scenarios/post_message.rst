rst
How to use the `post_message` function
========================================================================================

Description
-------------------------
This Python code defines functions for posting messages on Facebook using Selenium.  `post_message` is the main function that orchestrates the process of composing, uploading media, and publishing a post. It handles the interaction with the Facebook webpage, including sending the title and description, uploading images/videos, and finally publishing the post.  The code is designed to be robust by handling potential errors like failed uploads and pop-up dialogs.

Execution steps
-------------------------
1. **Load Locators:** The code loads locators (element identifiers) from a JSON file (`post_message.json`) using `j_loads_ns`.  These locators are crucial for interacting with specific elements on the Facebook page.

2. **Send Post Title and Description:** The `post_title` function is called to input the post title and description into the designated Facebook input fields.  The function handles both `SimpleNamespace` objects (containing `title` and `description` attributes) and plain strings as input for the message.  Error handling is included to ensure robustness during the process.

3. **Upload Media:** The `upload_media` function handles uploading image and video files, potentially managing multiple files within a list. It interacts with the Facebook media upload functionality and checks for successful uploads, or if `no_video` is set to `True`, only uploads images.

4. **Update Media Captions (Optional):**  If captions are needed, `update_images_captions` is called to add descriptions to the uploaded media.  This function handles translation to different languages, if needed, and correctly formats the captions based on language direction (LTR or RTL).

5. **Publish the Post:** The `publish` function attempts to publish the post. This function uses retry logic to handle potential issues encountered while clicking the 'Publish' button, including pop-up dialogs (e.g., 'Not now') by retrying a set number of times (default 5).

6. **Combine Actions (`post_message`):** The `post_message` function combines the preceding steps to create a complete Facebook post: sending the title and description, uploading media, and finally publishing the post.


Usage example
-------------------------
.. code-block:: python

    from selenium import webdriver
    from hypotez.src.webdriver.driver import Driver
    from hypotez.src.endpoints.advertisement.facebook.scenarios import post_message  # adjust path as needed


    # Initialize the driver (replace with your actual setup)
    driver = webdriver.Chrome()
    d = Driver(driver)


    # Define the message data.  Ensure correct attribute names.
    message = SimpleNamespace(
        title="New Product Launch",
        description="Check out our new product!",
        products=[
            SimpleNamespace(local_saved_image="path/to/image1.jpg"),
            SimpleNamespace(local_saved_image="path/to/image2.png")
        ]
    )


    # Call the post_message function.
    success = post_message(d, message)

    if success:
        print("Post was successfully published!")
    else:
        print("Failed to publish the post.")


    # Close the browser
    driver.quit()