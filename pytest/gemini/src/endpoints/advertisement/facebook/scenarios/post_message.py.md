```python
import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path
from types import SimpleNamespace
from typing import List
from src.endpoints.advertisement.facebook.scenarios.post_message import (
    post_title,
    upload_media,
    update_images_captions,
    publish,
    promote_post,
    post_message,
)
from src.webdriver.driver import Driver

# Fixture for a mock Driver
@pytest.fixture
def mock_driver():
    """Provides a mock Driver instance."""
    driver = MagicMock(spec=Driver)
    driver.wait = MagicMock()
    driver.execute_locator = MagicMock(return_value=True)
    driver.scroll = MagicMock(return_value=True)
    return driver


# Fixture for test data
@pytest.fixture
def mock_category():
    """Provides a mock category SimpleNamespace."""
    return SimpleNamespace(title="Test Title", description="Test Description", tags = "tag1, tag2")


@pytest.fixture
def mock_products():
    """Provides a mock products list of SimpleNamespace."""
    return [
        SimpleNamespace(
            local_image_path="path/to/image1.jpg",
            language="EN",
            product_title="Product 1 Title",
            description="Product 1 Description",
            original_price="100",
            target_original_price_currency="$",
            sale_price="90",
            discount="10%",
            evaluate_rate="4.5%",
            promotion_link="https://example.com/product1",
            
        ),
        SimpleNamespace(
            local_image_path="path/to/image2.jpg",
            local_video_path = "path/to/video1.mp4",
            language="RU",
            product_title="Продукт 2 Название",
            description="Продукт 2 Описание",
            original_price="200",
            target_original_price_currency="₽",
            sale_price="180",
            discount="10%",
            evaluate_rate="4.8%",
            promotion_link="https://example.com/product2",
        ),
    ]
@pytest.fixture
def mock_translations_json():
        """Create a mock JSON file for translations."""
        content = {
            "LOCALE": {
                "EN": "LTR",
                "RU": "RTL"
            },
             "original_price": {
                "EN": "Original Price",
                "RU": "Первоначальная цена"
            },
            "discount": {
                 "EN": "Discount",
                 "RU": "Скидка"
            },
            "sale_price": {
                 "EN": "Sale Price",
                 "RU": "Цена со скидкой"
            },
            "evaluate_rate": {
                 "EN": "Evaluate Rate",
                 "RU": "Оценка"
            },
            "promotion_link":{
                 "EN": "Promotion Link",
                "RU": "Ссылка на акцию"
            },
             "tags":{
                "EN": "Tags",
                "RU": "Теги"
            },
              "COPYRIGHT": {
                "EN": "All rights reserved",
                "RU": "Все права защищены"
            }
        }
        
        mock_file_path = Path('mock_translations.json')
        with open(mock_file_path, 'w') as f:
            import json
            json.dump(content, f)
        yield mock_file_path
        mock_file_path.unlink()
@pytest.fixture
def mock_simple_namespace_with_products(mock_products):
    """Provides a mock simple namespace with product list"""
    return SimpleNamespace(products=mock_products, title="Test title", description="Test Description")

@pytest.fixture
def mock_web_element():
    """Provides a mock WebElement instance."""
    mock_element = MagicMock()
    mock_element.send_keys = MagicMock()
    return mock_element


# Test cases for post_title
def test_post_title_valid_input(mock_driver, mock_category):
    """Checks correct behavior of post_title with valid input."""
    assert post_title(mock_driver, mock_category) == True
    mock_driver.scroll.assert_called_once()
    mock_driver.execute_locator.assert_called()


def test_post_title_scroll_fails(mock_driver, mock_category):
    """Checks post_title returns None when scroll fails."""
    mock_driver.scroll.return_value = False
    assert post_title(mock_driver, mock_category) is None
    mock_driver.scroll.assert_called_once()


def test_post_title_open_box_fails(mock_driver, mock_category):
    """Checks post_title returns None when opening box fails."""
    mock_driver.execute_locator.side_effect = [False, True]
    assert post_title(mock_driver, mock_category) is None
    mock_driver.execute_locator.assert_called()

def test_post_title_add_message_fails(mock_driver, mock_category):
    """Checks post_title returns None when adding the message fails."""
    mock_driver.execute_locator.side_effect = [True,False]
    assert post_title(mock_driver, mock_category) is None
    mock_driver.execute_locator.assert_called()

def test_post_title_with_str_message(mock_driver):
    """Checks post_title returns true with str message."""
    message = "Test message"
    assert post_title(mock_driver, message) == True
    mock_driver.execute_locator.assert_called()


# Test cases for upload_media
def test_upload_media_valid_input(mock_driver, mock_products):
    """Checks correct behavior of upload_media with valid input."""
    with patch('src.endpoints.advertisement.facebook.scenarios.post_message.update_images_captions', return_value=None) as mock_update_images_captions:
        assert upload_media(mock_driver, mock_products) == True
        mock_driver.execute_locator.assert_called()
        mock_update_images_captions.assert_called_once()


def test_upload_media_no_media(mock_driver):
    """Checks upload_media returns None with no media."""
    assert upload_media(mock_driver, None) is None
    mock_driver.execute_locator.assert_not_called()


def test_upload_media_open_form_fails(mock_driver, mock_products):
    """Checks upload_media returns None when opening form fails."""
    mock_driver.execute_locator.side_effect = [False, True]
    assert upload_media(mock_driver, mock_products) is None
    mock_driver.execute_locator.assert_called()


def test_upload_media_upload_fails(mock_driver, mock_products):
    """Checks upload_media returns None when media upload fails."""
    mock_driver.execute_locator.side_effect = [True, False]
    assert upload_media(mock_driver, mock_products) is None
    mock_driver.execute_locator.assert_called()

def test_upload_media_no_captions(mock_driver, mock_products):
    """Checks upload_media returns True when without_captions is True."""
    with patch('src.endpoints.advertisement.facebook.scenarios.post_message.update_images_captions', return_value=None) as mock_update_images_captions:
        assert upload_media(mock_driver, mock_products, without_captions = True) == True
        mock_driver.execute_locator.assert_called()
        mock_update_images_captions.assert_not_called()
def test_upload_media_no_edit_button(mock_driver, mock_products):
    """Checks upload_media returns None when edit media button not found."""
    mock_driver.execute_locator.side_effect = [True,True, False]
    assert upload_media(mock_driver, mock_products) is None
    mock_driver.execute_locator.assert_called()
def test_upload_media_no_edit_frame(mock_driver, mock_products):
    """Checks upload_media returns None when media frame not found."""
    mock_driver.execute_locator.side_effect = [True,True, True, False]
    assert upload_media(mock_driver, mock_products) is None
    mock_driver.execute_locator.assert_called()

def test_upload_media_no_textareas(mock_driver, mock_products):
    """Checks upload_media returns None when textareas are not found."""
    mock_driver.execute_locator.side_effect = [True, True, True, True, False]
    assert upload_media(mock_driver, mock_products) is None
    mock_driver.execute_locator.assert_called()
def test_upload_media_with_string_path(mock_driver, mock_products):
    """Checks upload_media returns True with string path."""
    with patch('src.endpoints.advertisement.facebook.scenarios.post_message.update_images_captions', return_value=None) as mock_update_images_captions:
        assert upload_media(mock_driver, [mock_products[0].local_image_path]) == True
        mock_driver.execute_locator.assert_called()
        mock_update_images_captions.assert_called_once()

def test_upload_media_with_pathlib_path(mock_driver, mock_products):
    """Checks upload_media returns True with pathlib path."""
    with patch('src.endpoints.advertisement.facebook.scenarios.post_message.update_images_captions', return_value=None) as mock_update_images_captions:
        assert upload_media(mock_driver, [Path(mock_products[0].local_image_path)]) == True
        mock_driver.execute_locator.assert_called()
        mock_update_images_captions.assert_called_once()
def test_upload_media_with_video(mock_driver, mock_products):
    """Checks upload_media returns True with video path."""
    with patch('src.endpoints.advertisement.facebook.scenarios.post_message.update_images_captions', return_value=None) as mock_update_images_captions:
        assert upload_media(mock_driver, mock_products, no_video = False) == True
        mock_driver.execute_locator.assert_called()
        mock_update_images_captions.assert_called_once()
def test_upload_media_with_no_video(mock_driver, mock_products):
    """Checks upload_media returns True with video path."""
    with patch('src.endpoints.advertisement.facebook.scenarios.post_message.update_images_captions', return_value=None) as mock_update_images_captions:
        assert upload_media(mock_driver, mock_products, no_video = True) == True
        mock_driver.execute_locator.assert_called()
        mock_update_images_captions.assert_called_once()

# Test cases for update_images_captions
def test_update_images_captions_valid_input(mock_driver, mock_products, mock_web_element, mock_translations_json):
    """Checks correct behavior of update_images_captions with valid input."""
    with patch('src.endpoints.advertisement.facebook.scenarios.post_message.j_loads_ns', return_value=SimpleNamespace(LOCALE = SimpleNamespace(EN="LTR", RU="RTL"),
                  original_price = SimpleNamespace(EN="Original Price", RU="Первоначальная цена"),
                  discount = SimpleNamespace(EN="Discount", RU="Скидка"),
                  sale_price = SimpleNamespace(EN="Sale Price", RU="Цена со скидкой"),
                  evaluate_rate = SimpleNamespace(EN="Evaluate Rate", RU="Оценка"),
                  promotion_link = SimpleNamespace(EN="Promotion Link", RU="Ссылка на акцию")
                                                     )):
        update_images_captions(mock_driver, mock_products, [mock_web_element, mock_web_element])
        mock_web_element.send_keys.assert_called()
def test_update_images_captions_missing_fields(mock_driver, mock_products, mock_web_element, mock_translations_json):
    """Checks correct behavior of update_images_captions with missing fields."""
    mock_products[0].product_title = None
    mock_products[0].description = None
    mock_products[0].original_price = None
    mock_products[0].sale_price = None
    mock_products[0].discount = None
    mock_products[0].evaluate_rate = None
    mock_products[0].promotion_link = None
    
    mock_products[1].product_title = None
    mock_products[1].description = None
    mock_products[1].original_price = None
    mock_products[1].sale_price = None
    mock_products[1].discount = None
    mock_products[1].evaluate_rate = None
    mock_products[1].promotion_link = None

    with patch('src.endpoints.advertisement.facebook.scenarios.post_message.j_loads_ns', return_value=SimpleNamespace(LOCALE = SimpleNamespace(EN="LTR", RU="RTL"),
                  original_price = SimpleNamespace(EN="Original Price", RU="Первоначальная цена"),
                  discount = SimpleNamespace(EN="Discount", RU="Скидка"),
                  sale_price = SimpleNamespace(EN="Sale Price", RU="Цена со скидкой"),
                  evaluate_rate = SimpleNamespace(EN="Evaluate Rate", RU="Оценка"),
                  promotion_link = SimpleNamespace(EN="Promotion Link", RU="Ссылка на акцию")
                                                     )):
        update_images_captions(mock_driver, mock_products, [mock_web_element, mock_web_element])
        mock_web_element.send_keys.assert_called()
def test_update_images_captions_send_keys_error(mock_driver, mock_products, mock_web_element, mock_translations_json):
    """Checks update_images_captions handles send_keys errors."""
    mock_web_element.send_keys.side_effect = Exception("Send keys error")
    with patch('src.endpoints.advertisement.facebook.scenarios.post_message.j_loads_ns', return_value=SimpleNamespace(LOCALE = SimpleNamespace(EN="LTR", RU="RTL"),
                  original_price = SimpleNamespace(EN="Original Price", RU="Первоначальная цена"),
                  discount = SimpleNamespace(EN="Discount", RU="Скидка"),
                  sale_price = SimpleNamespace(EN="Sale Price", RU="Цена со скидкой"),
                  evaluate_rate = SimpleNamespace(EN="Evaluate Rate", RU="Оценка"),
                  promotion_link = SimpleNamespace(EN="Promotion Link", RU="Ссылка на акцию")
                                                     )):
        update_images_captions(mock_driver, mock_products, [mock_web_element])
        mock_web_element.send_keys.assert_called()
def test_update_images_captions_message_generation_error(mock_driver, mock_products, mock_web_element, mock_translations_json):
    """Checks update_images_captions handles send_keys errors."""
    mock_products[0].language = "GB"
    with patch('src.endpoints.advertisement.facebook.scenarios.post_message.j_loads_ns', return_value=SimpleNamespace(LOCALE = SimpleNamespace(EN="LTR", RU="RTL"),
                  original_price = SimpleNamespace(EN="Original Price", RU="Первоначальная цена"),
                  discount = SimpleNamespace(EN="Discount", RU="Скидка"),
                  sale_price = SimpleNamespace(EN="Sale Price", RU="Цена со скидкой"),
                  evaluate_rate = SimpleNamespace(EN="Evaluate Rate", RU="Оценка"),
                  promotion_link = SimpleNamespace(EN="Promotion Link", RU="Ссылка на акцию")
                                                     )):
         update_images_captions(mock_driver, mock_products, [mock_web_element,mock_web_element])
         mock_web_element.send_keys.assert_called()

# Test cases for publish
def test_publish_valid_input(mock_driver):
    """Checks correct behavior of publish with valid input."""
    assert publish(mock_driver) == True
    mock_driver.execute_locator.assert_called()


def test_publish_attempts_less_zero(mock_driver):
    """Checks publish returns None when attempts is less than zero."""
    assert publish(mock_driver, attempts=-1) is None
    mock_driver.execute_locator.assert_not_called()

def test_publish_finish_editing_fails(mock_driver):
    """Checks publish returns None when locator finish editing fails."""
    mock_driver.execute_locator.side_effect = [False, True]
    assert publish(mock_driver) is None
    mock_driver.execute_locator.assert_called()


def test_publish_publish_fails(mock_driver):
    """Checks publish returns None when publish locator fails."""
    mock_driver.execute_locator.side_effect = [True, False]
    assert publish(mock_driver) is None
    mock_driver.execute_locator.assert_called()

def test_publish_publish_fails_with_close_pop_up(mock_driver):
    """Checks publish returns None when publish locator fails and close popup is found."""
    mock_driver.execute_locator.side_effect = [True, False, True, True]
    assert publish(mock_driver, attempts=5) == True
    mock_driver.execute_locator.assert_called()

def test_publish_publish_fails_with_not_now(mock_driver):
    """Checks publish returns None when publish locator fails and not now is found."""
    mock_driver.execute_locator.side_effect = [True, False, False, True]
    assert publish(mock_driver, attempts=5) == True
    mock_driver.execute_locator.assert_called()


def test_publish_open_post_box_fails(mock_driver):
    """Checks publish returns None when open post box locator fails."""
    mock_driver.execute_locator.side_effect = [True, True, False]
    publish(mock_driver, attempts = 2)
    mock_driver.execute_locator.assert_called()

def test_publish_open_post_box_fails_with_close_pop_up(mock_driver):
    """Checks publish returns True when publish locator fails and close popup is found."""
    mock_driver.execute_locator.side_effect = [True, True, False, True, True]
    assert publish(mock_driver, attempts=2) == True
    mock_driver.execute_locator.assert_called()


def test_publish_open_post_box_fails_with_not_now(mock_driver):
    """Checks publish returns True when publish locator fails and not now is found."""
    mock_driver.execute_locator.side_effect = [True, True, False, False, True]
    assert publish(mock_driver, attempts=2) == True
    mock_driver.execute_locator.assert_called()


# Test cases for promote_post
def test_promote_post_valid_input(mock_driver, mock_category, mock_products):
    """Checks correct behavior of promote_post with valid input."""
    assert promote_post(mock_driver, mock_category, mock_products) == True
    mock_driver.execute_locator.assert_called()


def test_promote_post_post_title_fails(mock_driver, mock_category, mock_products):
    """Checks promote_post returns None when post_title fails."""
    mock_driver.scroll.return_value = False
    assert promote_post(mock_driver, mock_category, mock_products) is None
    mock_driver.execute_locator.assert_not_called()

def test_promote_post_upload_media_fails(mock_driver, mock_category, mock_products):
    """Checks promote_post returns None when upload_media fails."""
    mock_driver.execute_locator.side_effect = [True, False]
    assert promote_post(mock_driver, mock_category, mock_products) is None
    mock_driver.execute_locator.assert_called()
def test_promote_post_finish_editing_fails(mock_driver, mock_category, mock_products):
    """Checks promote_post returns None when finish_editing_button fails."""
    mock_driver.execute_locator.side_effect = [True, True, False]
    assert promote_post(mock_driver, mock_category, mock_products) is None
    mock_driver.execute_locator.assert_called()
def test_promote_post_publish_fails(mock_driver, mock_category, mock_products):
    """Checks promote_post returns None when publish fails."""
    mock_driver.execute_locator.side_effect = [True, True, True, False]
    assert promote_post(mock_driver, mock_category, mock_products) is None
    mock_driver.execute_locator.assert_called()

# Test cases for post_message
def test_post_message_valid_input(mock_driver, mock_simple_namespace_with_products):
    """Checks correct behavior of post_message with valid input."""
    assert post_message(mock_driver, mock_simple_namespace_with_products) == True
    mock_driver.execute_locator.assert_called()

def test_post_message_post_title_fails(mock_driver, mock_simple_namespace_with_products):
    """Checks post_message returns None when post_title fails."""
    mock_driver.scroll.return_value = False
    assert post_message(mock_driver, mock_simple_namespace_with_products) is None
    mock_driver.execute_locator.assert_not_called()

def test_post_message_upload_media_fails(mock_driver, mock_simple_namespace_with_products):
    """Checks post_message returns None when upload_media fails."""
    mock_driver.execute_locator.side_effect = [True, False]
    assert post_message(mock_driver, mock_simple_namespace_with_products) is None
    mock_driver.execute_locator.assert_called()
def test_post_message_one_image(mock_driver, mock_simple_namespace_with_products):
    """Checks post_message returns None when upload_media fails."""
    mock_driver.execute_locator.side_effect = [True, True]
    assert post_message(mock_driver, mock_simple_namespace_with_products) == True
    mock_driver.execute_locator.assert_called()
def test_post_message_finish_editing_fails(mock_driver, mock_simple_namespace_with_products):
    """Checks post_message returns None when finish_editing_button fails."""
    mock_driver.execute_locator.side_effect = [True, True, False]
    assert post_message(mock_driver, mock_simple_namespace_with_products) is None
    mock_driver.execute_locator.assert_called()

def test_post_message_publish_fails(mock_driver, mock_simple_namespace_with_products):
    """Checks post_message returns None when publish fails."""
    mock_driver.execute_locator.side_effect = [True, True, True, False]
    assert post_message(mock_driver, mock_simple_namespace_with_products) is None
    mock_driver.execute_locator.assert_called()
def test_post_message_with_no_video(mock_driver, mock_simple_namespace_with_products):
    """Checks post_message returns True with no_video."""
    assert post_message(mock_driver, mock_simple_namespace_with_products, no_video = True) == True
    mock_driver.execute_locator.assert_called()
def test_post_message_without_captions(mock_driver, mock_simple_namespace_with_products):
    """Checks post_message returns True without captions."""
    assert post_message(mock_driver, mock_simple_namespace_with_products, without_captions = True) == True
    mock_driver.execute_locator.assert_called()
```