```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def facebook_locators_data():
    """Loads the facebook_locators.json data."""
    with open("hypotez/src/scenario/json/facebook_locators.json", 'r') as f:
        return json.load(f)

# Test cases for the 'login' section
def test_login_email(facebook_locators_data):
    """Checks if the email is correct"""
    assert facebook_locators_data["login"]["email"] == "one.last.bit@gmail.com"

def test_login_password(facebook_locators_data):
    """Checks if the password is correct"""
    assert facebook_locators_data["login"]["password"] == "@o533368048"

def test_login_email_selector(facebook_locators_data):
    """Checks if the email selector is correct"""
    assert facebook_locators_data["login"]["email_selector"]["by"] == "ID"
    assert facebook_locators_data["login"]["email_selector"]["selector"] == "email"

def test_login_password_locator(facebook_locators_data):
    """Checks if the password locator is correct"""
    assert facebook_locators_data["login"]["password_locator"]["by"] == "ID"
    assert facebook_locators_data["login"]["password_locator"]["selector"] == "..."

def test_login_button_locator(facebook_locators_data):
    """Checks if the login button locator is correct"""
    assert facebook_locators_data["login"]["loginbutton_locator"]["by"] == "ID"
    assert facebook_locators_data["login"]["loginbutton_locator"]["selector"] == "u_0_b"


# Test cases for the 'locators' section
def test_btn_send_message_locator(facebook_locators_data):
    """Checks if the send message button locator is correct"""
    assert facebook_locators_data["locators"]["btn_send_message"]["by"] == "CSS_SELECTOR"
    assert facebook_locators_data["locators"]["btn_send_message"]["selector"] == "._1mf7._4jy0._4jy3._4jy1._51sy"

def test_btn_start_write_message_locator(facebook_locators_data):
    """Checks if the start write message button locator is correct"""
    assert facebook_locators_data["locators"]["btn_start_write_message"]["by"] == "css selector"
    assert facebook_locators_data["locators"]["btn_start_write_message"]["selector"] == "span._5qtp"

def test_btn_upload_image_locator(facebook_locators_data):
    """Checks if the upload image button locator is correct"""
    assert facebook_locators_data["locators"]["btn_upload_image"]["by"] == "CSS_SELECTOR"
    assert facebook_locators_data["locators"]["btn_upload_image"]["selector"] == "._n._5f0v"

def test_div_before_btn_upload_image_text_locator(facebook_locators_data):
    """Checks if the div before upload image text locator is correct"""
    assert facebook_locators_data["locators"]["div_before_btn_upload_image_text"]["by"] == "CSS_SELECTOR"
    assert facebook_locators_data["locators"]["div_before_btn_upload_image_text"]["selector"] == "text^='�����/�����'"

def test_div_before_btn_upload_image_class_locator(facebook_locators_data):
    """Checks if the div before upload image class locator is correct"""
    assert facebook_locators_data["locators"]["div_before_btn_upload_image_class"]["by"] == "CSS_SELECTOR"
    assert facebook_locators_data["locators"]["div_before_btn_upload_image_class"]["selector"] == "._5qtp"

def test_input_image_element_id(facebook_locators_data):
    """Checks if the input image element ids is correct"""
    assert facebook_locators_data["locators"]["input_image_element_id"] == ["js_r", "js_31"]

def test_input_text_message_locator_deprecated(facebook_locators_data):
    """Checks if the deprecated input text message locator is correct"""
    assert facebook_locators_data["locators"]["input_text_message___"]["by"] == "css selector"
    assert facebook_locators_data["locators"]["input_text_message___"]["selector"] == "._1mf._1mk"

def test_input_text_message_locator(facebook_locators_data):
     """Checks if the input text message locator is correct"""
     assert facebook_locators_data["locators"]["input_text_message"]["by"] == "css selector"
     assert facebook_locators_data["locators"]["input_text_message"]["selector"] == "._2cuy._3dgx"

def test_textarea_navigationFocus_locator(facebook_locators_data):
    """Checks if the textarea navigation focus locator is correct"""
    assert facebook_locators_data["locators"]["textarea_navigationFocus"]["by"] == "css selector"
    assert facebook_locators_data["locators"]["textarea_navigationFocus"]["selector"] == "js_1z"

# Test cases for the 'govno-vsjqko-razno' section
def test_govno_vsjqko_razno_input_text_message(facebook_locators_data):
    """Checks if the 'govno-vsjqko-razno' input text message locators are correct"""
    expected_selectors = [ "._1mf._1mk", "._1p1v", "textarea[placeholder*=\\"���� ����\\"]" ]
    assert facebook_locators_data["govno-vsjqko-razno"]["input_text_message"] == expected_selectors

# Test case if the file is not json format.
def test_invalid_json_file():
    with open("test.txt", "w") as f:
        f.write("Invalid json file")
    with pytest.raises(json.JSONDecodeError):
        with open("test.txt", 'r') as f:
            json.load(f)

```