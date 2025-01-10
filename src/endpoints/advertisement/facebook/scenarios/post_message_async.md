```rst
... module:: src.endpoints.advertisement.facebook.post_message_async
```
[Русский]()

## Asynchronous Facebook Post Message Scenario

### Overview

This script is part of the `hypotez/src/endpoints/advertisement/facebook/scenarios` directory and is designed to automate the process of posting messages on Facebook. The script interacts with the Facebook page by using locators to perform various actions such as sending messages, uploading media files, and updating captions.

### Key Features

1. **Sending Title and Description**: Sends the title and description of a campaign to the Facebook post message box.
2. **Uploading Media Files**: Uploads media files (images and videos) to the Facebook post and updates their captions.
3. **Promoting Post**: Manages the entire process of promoting a post with a title, description, and media files.

### Module Structure

```mermaid
graph TD
    Start[Start] --> InitDriver[Initialize Driver]
    InitDriver --> LoadCategoryAndProducts[Load Category and Products]
    LoadCategoryAndProducts --> SendTitle[Send Title]
    SendTitle --> CheckTitleSuccess{Success?}
    CheckTitleSuccess -->|Yes| UploadMediaAndPromotePost[Upload Media and Promote Post]
    CheckTitleSuccess -->|No| TitleError[Error: Failed to Send Title]
    UploadMediaAndPromotePost --> UploadMedia[Upload Media]
    UploadMedia --> CheckMediaSuccess{Success?}
    CheckMediaSuccess -->|Yes| UpdateCaptions[Update Image Captions]
    CheckMediaSuccess -->|No| MediaError[Error: Failed to Upload Media]
    UpdateCaptions --> PromotePost[Promote Post]
    PromotePost --> CheckPromoteSuccess{Success?}
    CheckPromoteSuccess -->|Yes| End[End]
    CheckPromoteSuccess -->|No| PromoteError[Error: Failed to Promote Post]
```

### Legend

1. **Start**: Start of script execution.
2. **InitDriver**: Create an instance of the `Driver` class.
3. **LoadCategoryAndProducts**: Load category and product data.
4. **SendTitle**: Call the `post_title` function to send the title.
5. **CheckTitleSuccess**: Check if the title was sent successfully.
   - **Yes**: Proceed to upload media and promote the post.
   - **No**: Output error "Failed to send title".
6. **UploadMediaAndPromotePost**: Call the `promote_post` function.
7. **UploadMedia**: Call the `upload_media` function to upload media files.
8. **CheckMediaSuccess**: Check if media was uploaded successfully.
   - **Yes**: Proceed to update image captions.
   - **No**: Output error "Failed to upload media".
9. **UpdateCaptions**: Call the `update_images_captions` function to update captions.
10. **PromotePost**: Complete the post promotion process.
11. **CheckPromoteSuccess**: Check if the post was promoted successfully.
    - **Yes**: End of script execution.
    - **No**: Output error "Failed to promote post".

-----------------------

#### Functions

- **`post_title(d: Driver, category: SimpleNamespace) -> bool`**:
  - **Purpose**: Sends the title and description of a campaign to the Facebook post message box.
  - **Parameters**:
    - `d`: The `Driver` instance used for interacting with the webpage.
    - `category`: The category containing the title and description to be sent.
  - **Returns**: `True` if the title and description were sent successfully, otherwise `None`.

- **`upload_media(d: Driver, products: List[SimpleNamespace], no_video: bool = False) -> bool`**:
  - **Purpose**: Uploads media files to the Facebook post and updates their captions.
  - **Parameters**:
    - `d`: The `Driver` instance used for interacting with the webpage.
    - `products`: List of products containing media file paths.
    - `no_video`: Flag indicating whether to skip video uploads.
  - **Returns**: `True` if media files were uploaded successfully, otherwise `None`.

- **`update_images_captions(d: Driver, products: List[SimpleNamespace], textarea_list: List[WebElement]) -> None`**:
  - **Purpose**: Asynchronously adds descriptions to uploaded media files.
  - **Parameters**:
    - `d`: The `Driver` instance used for interacting with the webpage.
    - `products`: List of products with details to update.
    - `textarea_list`: List of textareas where captions are added.

- **`promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video: bool = False) -> bool`**:
  - **Purpose**: Manages the process of promoting a post with a title, description, and media files.
  - **Parameters**:
    - `d`: The `Driver` instance used for interacting with the webpage.
    - `category`: The category details used for the post title and description.
    - `products`: List of products containing media and details to be posted.
    - `no_video`: Flag indicating whether to skip video uploads.
  - **Returns**: `True` if the post was promoted successfully, otherwise `None`.

### Usage

To use this script, follow these steps:

1. **Initialize Driver**: Create an instance of the `Driver` class.
2. **Load Locators**: Load the locators from the JSON file.
3. **Call Functions**: Use the provided functions to send the title, upload media, and promote the post.

#### Example

```python
from src.webdriver.driver import Driver
from types import SimpleNamespace

# Initialize Driver
driver = Driver(...)

# Load category and products
category = SimpleNamespace(title="Campaign Title", description="Campaign Description")
products = [SimpleNamespace(local_image_path='path/to/image.jpg', ...)]

# Send title
post_title(driver, category)

# Upload media and promote post
await promote_post(driver, category, products)
```

### Dependencies

- `selenium`: For web automation.
- `asyncio`: For asynchronous operations.
- `pathlib`: For handling file paths.
- `types`: For creating simple namespaces.
- `typing`: For type annotations.

### Error Handling

The script includes robust error handling to ensure that the execution continues even if certain elements are not found or if there are issues with the web page. This is particularly useful for handling dynamic or unstable web pages.

### Contributing

Contributions to this script are welcome. Please ensure that any changes are well-documented and include appropriate tests.

### License

This script is licensed under the MIT License. See the `LICENSE` file for more details.