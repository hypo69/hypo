rst
How to use the `post_message_async` code block
==========================================================================================

Description
-------------------------
This Python code defines functions for asynchronously posting messages to a Facebook advertisement platform.  It handles tasks like entering a post title and description, uploading media files (images and optionally videos), and then publishing the post. The code utilizes Selenium WebDriver (`Driver` class) for web interaction and asynchronous operations (`asyncio`).  It also includes error handling and logging to address potential issues during the posting process.  Crucially, it manages caption updates for uploaded media asynchronously and takes into account both left-to-right (LTR) and right-to-left (RTL) language directions.


Execution steps
-------------------------
1. **Import necessary libraries:** The code imports libraries for time management, asynchronous programming, file paths, data structures, Selenium, and custom modules for web interaction (`Driver`), JSON handling, and logging.

2. **Load locators:** It loads web element locators from a JSON file (`post_message.json`). This file defines how to find specific elements on the Facebook advertisement page.  This is a critical step that improves code maintainability.

3. **`post_title` function:** This function sends the title and description of the campaign to the Facebook post message box.  It first scrolls the page backward to ensure the necessary elements are in view.

4. **`upload_media` function:** This function handles the asynchronous uploading of media files to the post.
   - It opens the media upload form.
   - It iterates through the provided list of `products`.
   - For each product, it attempts to upload the image or video using the appropriate locator.
   - If uploading fails, it logs an error message and returns.
   - Finally, it asynchronously updates the captions for each uploaded media file.

5. **`update_images_captions` function:** This function takes asynchronous responsibility for updating captions for the uploaded media.
    - It retrieves localized strings from a JSON file.
    - It generates the caption text, including title, prices, discounts, etc., for each product, based on language direction.
    - It synchronously updates captions for each product using `asyncio.to_thread`.


6. **`promote_post` function:** This function orchestrates the entire posting process.
   - Calls `post_title` to enter the title and description.
   - Calls `upload_media` to upload media and update captions.
   - Calls functions to finish editing and publish the post.
   - Returns `True` if the post is published successfully, otherwise returns `None` or implicitly `False` if any intermediate step fails.


Usage example
-------------------------
.. code-block:: python

    import asyncio
    from pathlib import Path
    from src import gs
    from src.endpoints.advertisement.facebook.scenarios.post_message_async import promote_post
    from src.webdriver.driver import Driver

    # Replace with your actual values
    category = SimpleNamespace(title="Summer Sale", description="Amazing deals on summer clothes")
    products = [
        SimpleNamespace(local_saved_image=str(Path(gs.path.images / 'image1.jpg')), product_title='Summer Dress', original_price=100, sale_price=80, discount=20, language='en'),
        SimpleNamespace(local_saved_image=str(Path(gs.path.images / 'image2.jpg')), product_title='Beach Shorts', original_price=50, sale_price=40, discount=20, language='en'),
    ]

    async def main():
        driver = Driver()
        try:
            success = await promote_post(driver, category, products)
            if success:
                print("Post published successfully!")
            else:
                print("Failed to publish post.")
        finally:
            await driver.quit()

    if __name__ == "__main__":
        asyncio.run(main())