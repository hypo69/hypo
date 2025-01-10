```python
import pytest
from unittest.mock import MagicMock
from types import SimpleNamespace
from typing import List
from selenium.webdriver.remote.webelement import WebElement

# Assuming the functions are in a module named 'post_message_async'
# and the Driver class is in 'src.webdriver.driver'
from src.endpoints.advertisement.facebook import post_message_async
from src.webdriver.driver import Driver


@pytest.fixture
def mock_driver():
    """Provides a mock Driver instance for testing."""
    driver = MagicMock(spec=Driver)
    driver.find_element = MagicMock()
    driver.send_keys = MagicMock()
    driver.click = MagicMock()
    driver.upload_file = MagicMock()
    driver.wait_for_element = MagicMock()
    return driver


@pytest.fixture
def example_category():
    """Provides a sample category SimpleNamespace object."""
    return SimpleNamespace(title="Test Title", description="Test Description")


@pytest.fixture
def example_products():
    """Provides a list of sample product SimpleNamespace objects."""
    return [
        SimpleNamespace(local_image_path="path/to/image1.jpg", caption="Image 1 Caption"),
        SimpleNamespace(local_image_path="path/to/image2.jpg", caption="Image 2 Caption"),
    ]


@pytest.fixture
def mock_textarea_list():
    """Provides a list of mock WebElement objects for textareas."""
    return [MagicMock(spec=WebElement), MagicMock(spec=WebElement)]


def test_post_title_valid_input(mock_driver, example_category):
    """Tests post_title function with valid input."""
    mock_driver.find_element.return_value = MagicMock()
    mock_driver.send_keys.return_value = None

    result = post_message_async.post_title(mock_driver, example_category)
    assert result is True
    mock_driver.find_element.assert_called()
    mock_driver.send_keys.assert_called()


def test_post_title_element_not_found(mock_driver, example_category):
    """Tests post_title when element is not found."""
    mock_driver.find_element.return_value = None
    result = post_message_async.post_title(mock_driver, example_category)
    assert result is None
    mock_driver.find_element.assert_called()


def test_upload_media_valid_input(mock_driver, example_products):
    """Tests upload_media with valid input."""
    mock_driver.wait_for_element.return_value = MagicMock()
    mock_driver.upload_file.return_value = None
    
    result = post_message_async.upload_media(mock_driver, example_products)
    assert result is True
    mock_driver.wait_for_element.assert_called()
    mock_driver.upload_file.assert_called()


def test_upload_media_no_products(mock_driver):
    """Tests upload_media when no products are provided."""
    result = post_message_async.upload_media(mock_driver, [])
    assert result is True
    mock_driver.upload_file.assert_not_called()


def test_upload_media_no_video_flag(mock_driver, example_products):
    """Tests upload_media with the no_video flag set to True."""
    mock_driver.wait_for_element.return_value = MagicMock()
    mock_driver.upload_file.return_value = None
    
    result = post_message_async.upload_media(mock_driver, example_products, no_video=True)
    assert result is True
    mock_driver.upload_file.assert_called() # It will still upload images
    mock_driver.find_element.assert_not_called()


def test_upload_media_element_not_found(mock_driver, example_products):
    """Tests upload_media when the upload element is not found."""
    mock_driver.wait_for_element.return_value = None
    result = post_message_async.upload_media(mock_driver, example_products)
    assert result is None
    mock_driver.wait_for_element.assert_called()


def test_update_images_captions_valid_input(mock_driver, example_products, mock_textarea_list):
    """Tests update_images_captions with valid input."""
    mock_driver.send_keys.return_value = None

    post_message_async.update_images_captions(mock_driver, example_products, mock_textarea_list)

    mock_driver.send_keys.assert_called()
    assert mock_driver.send_keys.call_count == len(example_products)


def test_update_images_captions_no_textareas(mock_driver, example_products):
    """Tests update_images_captions with empty textarea list."""
    post_message_async.update_images_captions(mock_driver, example_products, [])
    mock_driver.send_keys.assert_not_called()


def test_update_images_captions_no_products(mock_driver, mock_textarea_list):
    """Tests update_images_captions with empty products list."""
    post_message_async.update_images_captions(mock_driver, [], mock_textarea_list)
    mock_driver.send_keys.assert_not_called()


def test_promote_post_valid_input(mock_driver, example_category, example_products):
    """Tests promote_post with valid input and successful post."""
    mock_driver.find_element.return_value = MagicMock()
    mock_driver.send_keys.return_value = None
    mock_driver.upload_file.return_value = None
    mock_driver.wait_for_element.return_value = MagicMock()
    
    
    post_message_async.post_title = MagicMock(return_value=True)
    post_message_async.upload_media = MagicMock(return_value=True)
    post_message_async.update_images_captions = MagicMock()

    result = post_message_async.promote_post(mock_driver, example_category, example_products)
    assert result is True
    post_message_async.post_title.assert_called()
    post_message_async.upload_media.assert_called()
    post_message_async.update_images_captions.assert_called()
    mock_driver.click.assert_called()

def test_promote_post_post_title_fails(mock_driver, example_category, example_products):
    """Tests promote_post when post_title fails."""
    post_message_async.post_title = MagicMock(return_value=None)
    
    result = post_message_async.promote_post(mock_driver, example_category, example_products)
    assert result is None
    post_message_async.post_title.assert_called()


def test_promote_post_upload_media_fails(mock_driver, example_category, example_products):
    """Tests promote_post when upload_media fails."""
    post_message_async.post_title = MagicMock(return_value=True)
    post_message_async.upload_media = MagicMock(return_value=None)

    result = post_message_async.promote_post(mock_driver, example_category, example_products)
    assert result is None
    post_message_async.post_title.assert_called()
    post_message_async.upload_media.assert_called()


def test_promote_post_no_products(mock_driver, example_category):
     """Tests promote_post with an empty product list."""
     mock_driver.find_element.return_value = MagicMock()
     mock_driver.send_keys.return_value = None
     mock_driver.upload_file.return_value = None
     mock_driver.wait_for_element.return_value = MagicMock()
     post_message_async.post_title = MagicMock(return_value=True)
     post_message_async.upload_media = MagicMock(return_value=True)
     post_message_async.update_images_captions = MagicMock()
     
     result = post_message_async.promote_post(mock_driver, example_category, [])
     assert result is True
     post_message_async.post_title.assert_called()
     post_message_async.upload_media.assert_called()
     post_message_async.update_images_captions.assert_not_called()
     
def test_promote_post_no_video(mock_driver, example_category, example_products):
     """Tests promote_post with no_video flag."""
     mock_driver.find_element.return_value = MagicMock()
     mock_driver.send_keys.return_value = None
     mock_driver.upload_file.return_value = None
     mock_driver.wait_for_element.return_value = MagicMock()
     
     post_message_async.post_title = MagicMock(return_value=True)
     post_message_async.upload_media = MagicMock(return_value=True)
     post_message_async.update_images_captions = MagicMock()
     
     result = post_message_async.promote_post(mock_driver, example_category, example_products, no_video = True)
     assert result is True
     post_message_async.post_title.assert_called()
     post_message_async.upload_media.assert_called_with(mock_driver, example_products, no_video=True)
     post_message_async.update_images_captions.assert_called()
     mock_driver.click.assert_called()
```