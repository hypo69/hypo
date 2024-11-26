```
## File hypotez/src/endpoints/advertisement/facebook/scenarios/post_message_async.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.advertisement.facebook.scenarios 
	:platform: Windows, Unix
	:synopsis: Публикация сообщения из `aliexpress` промо

"""
MODE = 'dev'

import time
import asyncio
from pathlib import Path
from types import SimpleNamespace
from typing import Dict, List
from selenium.webdriver.remote.webelement import WebElement
from src import gs
from src.webdriver import Driver
from src.utils import j_loads_ns, pprint
from src.logger import logger

# Load locators from JSON file.
locator: SimpleNamespace = j_loads_ns(
    Path(gs.path.src / 'endpoints' / 'advertisement' / 'facebook' / 'locators' / 'post_message.json')
)


def post_title(d: Driver, category: SimpleNamespace) -> bool:
    """ Sends the title and description of a campaign to the post message box.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        category (SimpleNamespace): The category containing the title and description to be sent.

    Returns:
        bool: `True` if the title and description were sent successfully, otherwise `None`.

    Examples:
        >>> driver = Driver(...)
        >>> category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
        >>> post_title(driver, category)
        True
    """
    # Scroll backward in the page
    if not d.scroll(1, 1200, 'backward'):
        logger.error("Scroll failed during post title", exc_info=False)
        return
    # Open the 'add post' box
    if not d.execute_locator(locator.open_add_post_box):
        logger.error("Failed to open 'add post' box", exc_info=False)
        return
    # Construct the message with title and description
    message = f"{category.title}; {category.description};"
    # Add the message to the post box
    if not d.execute_locator(locator.add_message, message):
        logger.error(f"Failed to add message to post box: {message=}", exc_info=False)
        return
    return True


async def upload_media(d: Driver, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    """ Uploads media files to the images section and updates captions.

    Args:
        d (Driver): The driver instance used for interacting with the webpage.
        products (List[SimpleNamespace]): List of products containing media file paths.

    Returns:
        bool: True if media files were uploaded successfully, otherwise None.

    Raises:
        Exception: If there is an error during media upload or caption update.
    """
    # Step 1: Open the 'add media' form
    if not d.execute_locator(locator.open_add_foto_video_form):
        return
    d.wait(0.5)
    # Step 2: Ensure products is a list
    products = products if isinstance(products, list) else [products]
    ret = True
    for product in products:
        media_path = product.local_saved_video if hasattr(product, 'local_saved_video') and not no_video else product.local_saved_image
        try:
            if d.execute_locator(locator.foto_video_input, media_path):
                d.wait(1.5)
            else:
                logger.error(f"Ошибка загрузки изображения {media_path=}")
                return
        except Exception as ex:
            logger.error("Error in media upload", ex, exc_info=True)
            return
    # Step 3: Update captions for the uploaded media
    if not d.execute_locator(locator.edit_uloaded_media_button):
        logger.error(f"Ошибка загрузки изображения {media_path=}")
        return
    uploaded_media_frame = d.execute_locator(locator.uploaded_media_frame)
    uploaded_media_frame = uploaded_media_frame[0] if isinstance(uploaded_media_frame, list) else uploaded_media_frame
    d.wait(0.3)
    textarea_list = d.execute_locator(locator.edit_image_properties_textarea)
    if not textarea_list:
        logger.error("Не нашлись пля ввода подписи к изображениям")
        return
    await update_images_captions(d, products, textarea_list)
    return ret

# ... (rest of the code)
```

```
<algorithm>
**Block Diagram (High-Level):**

```
+-----------------+     +-----------------+
|   promote_post   | --> |  post_title     |
+-----------------+     +-----------------+
        |                 |
        |                 V
        |       +--------+--------+
        |       |  upload_media |
        |       +--------+--------+
        |                 |
        +-----------------+
```

**Data Flow:**

1. `promote_post` takes `Driver`, `category`, and `products` as input.
2. Calls `post_title` to set the post title and description.
3. Calls `upload_media` to upload media files.
4. Calls `d.execute_locator` functions for buttons, potentially executing other actions.
5. Returns `True` if all steps successful, `None` otherwise.


**Example Usage:**

```python
driver = Driver(...)
category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
products = [SimpleNamespace(local_saved_image='image1.jpg', product_title='Product A')]
await promote_post(driver, category, products)
```
```

<explanation>

**Imports:**

- `time`, `asyncio`, `pathlib`, `types`, `typing`, `selenium.webdriver.remote.webelement`: Standard Python libraries for time management, asynchronous operations, file paths, data types, and Selenium interaction.  These are fundamental parts of the Python ecosystem and are not specific to the project.

- `gs`, `src.webdriver`, `src.utils`, `src.logger`: These imports indicate the project's own custom modules. `gs` likely provides global settings, `src.webdriver` handles web driver interactions (crucial for automation), `src.utils` has helper functions, and `src.logger` handles logging.  This implies a well-structured Python project with modularity.


**Classes:**

- `Driver`:  This class is not defined in the snippet. We only see its usage. It is crucial for the web automation logic.  It likely encapsulates methods for interacting with the browser (e.g., `scroll`, `execute_locator`, `wait`).

**Functions:**

- `post_title(d: Driver, category: SimpleNamespace) -> bool`: Takes a driver and a category (containing title and description) to set the post title and description. Returns `True` on success.  Crucially, it handles potential errors during the process and logs them, improving robustness.


- `upload_media(d: Driver, products: List[SimpleNamespace], no_video: bool = False) -> bool`: Uploads media (images/videos) and adds captions. The `no_video` argument is a great addition for flexibility.  Error handling and asynchronous processing (`asyncio.to_thread`) are present, demonstrating awareness of potential slow operations.  Importantly, it handles cases where only one product is passed or where a list of products needs to be iterated through.

- `update_images_captions(d: Driver, products: List[SimpleNamespace], textarea_list: List[WebElement]) -> None`: This function asynchronously updates captions on uploaded media by iterating through the `products` list. `handle_product` handles the individual update of product captions, effectively improving performance. The use of `asyncio.to_thread` to execute `handle_product` asynchronously within the main `upload_media` thread is good practice for efficiency.

- `promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video:bool = False) -> bool`: Orchestrates the entire process of creating and publishing a Facebook advertisement post. It calls the `post_title` and `upload_media` functions to ensure these steps are performed in the correct sequence, handling errors along the way.

**Variables:**

- `locator`: A `SimpleNamespace` object containing locators (selectors) for elements on the Facebook page. This is loaded from a JSON file, making the code maintainable and reducing hardcoding.

- `MODE`: A string variable, likely used for different execution modes (e.g., development, production).

- `products`: List of `SimpleNamespace` objects, each representing a product with details, including the image/video path and product details. This variable is passed to `upload_media` and `update_images_captions`.


**Error Handling:**

The code includes `logger.error` calls with `exc_info=True` or `exc_info=False` to log errors properly, and the functions often return `None` to indicate failures. This ensures that errors are caught and reported, crucial in automation scripts.  Returning `None` is a common practice to indicate failure.

**Potential Improvements:**

- **Robust Error Handling:** While there's error handling, consider adding more specific exception types to handle different failure cases during media upload.

- **Explicit Type Checking:** Consider using type hinting more explicitly, including types for other variables like `media_path`.

- **Asynchronous `post_title`:** The `post_title` function is synchronous. Consider making it asynchronous (`async def`) to allow for potential parallel operations.

- **Resource Management:**  The `Driver` class should manage the WebDriver instance properly to prevent resource leaks.

**Relationships:**

- `post_message_async.py` relies on the `gs` module for global settings, `src.webdriver` for web interactions, `src.utils` for helper functions, `src.logger` for logging, and `post_message.json` for locator definitions. There might be other supporting modules as well.

- This file likely interacts with other files in `hypotez/src` (likely other advertisement endpoints) in a project dedicated to automated advertisement campaigns, specifically targeting Facebook advertising.