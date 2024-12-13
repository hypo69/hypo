```python
import pytest
import json

# Fixture to load the JSON data
@pytest.fixture
def locators_data():
    """Loads the locator data from the JSON file."""
    with open("hypotez/src/endpoints/advertisement/facebook/locators/post_message.json", "r") as f:
        return json.load(f)

def test_open_add_post_box_valid(locators_data):
    """
    Checks if 'open_add_post_box' locator is correctly defined.
    Verifies the presence of all mandatory keys and expected values for specific keys.
    """
    locator = locators_data.get("open_add_post_box")
    assert locator is not None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//span[contains(text(), 'Что у вас нового') or contains(text(), 'Напишите что-нибудь...')]"\
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] is False
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["mandatory"] is True
    assert "locator_description" in locator


def test_add_message_valid(locators_data):
    """
    Checks if 'add_message' locator is correctly defined.
    Verifies the presence of all mandatory keys and expected values for specific keys.
    """
    locator = locators_data.get("add_message")
    assert locator is not None
    assert locator["attribute"] == "None"
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "(//div[@role='textbox'])[last()]"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] == "None"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "pause(1);%EXTERNAL_MESSAGE%"
    assert locator["mandatory"] == "True"
    assert "locator_description" in locator
    assert "deprecated" in locator

def test_open_add_foto_video_form_valid(locators_data):
    """
    Checks if 'open_add_foto_video_form' locator is correctly defined.
    Verifies the presence of all mandatory keys and expected values for specific keys.
    """
    locator = locators_data.get("open_add_foto_video_form")
    assert locator is not None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//div[@aria-label='Фото/видео']"
    assert locator["if_list"] == "first"
    assert locator["use_mouse"] is True
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["mandatory"] is True
    assert "locator_description" in locator

def test_foto_video_input_valid(locators_data):
    """
    Checks if 'foto_video_input' locator is correctly defined.
    Verifies the presence of all mandatory keys and expected values for specific keys.
    """
    locator = locators_data.get("foto_video_input")
    assert locator is not None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//div[@role='dialog']//input[@type = 'file']"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "upload_media()"
    assert locator["mandatory"] is True
    assert "locator_description" in locator
    
def test_edit_uloaded_media_button_valid(locators_data):
    """
    Checks if 'edit_uloaded_media_button' locator is correctly defined.
    Verifies the presence of all mandatory keys and expected values for specific keys.
    """
    locator = locators_data.get("edit_uloaded_media_button")
    assert locator is not None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//div[@role='button' and contains(@aria-label,'Редактировать всё')]"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["mandatory"] is True
    assert "locator_description" in locator
    
def test_uploaded_media_frame_valid(locators_data):
    """
    Checks if 'uploaded_media_frame' locator is correctly defined.
    Verifies the presence of all mandatory keys and expected values for specific keys.
    """
    locator = locators_data.get("uploaded_media_frame")
    assert locator is not None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//div[@aria-label='Фото/видео']"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None
    assert locator["mandatory"] is True
    assert "locator_description" in locator
    
def test_edit_image_properties_textarea_valid(locators_data):
    """
    Checks if 'edit_image_properties_textarea' locator is correctly defined.
    Verifies the presence of all mandatory keys and expected values for specific keys.
    """
    locator = locators_data.get("edit_image_properties_textarea")
    assert locator is not None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//textarea"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] is None
    assert locator["mandatory"] is True
    assert "locator_description" in locator
    
def test_finish_editing_button_valid(locators_data):
    """
    Checks if 'finish_editing_button' locator is correctly defined.
    Verifies the presence of all mandatory keys and expected values for specific keys.
    """
    locator = locators_data.get("finish_editing_button")
    assert locator is not None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//span[contains(text(),'Готово')]"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["mandatory"] is True
    assert "locator_description" in locator
    
def test_publish_valid(locators_data):
    """
    Checks if 'publish' locator is correctly defined.
    Verifies the presence of all mandatory keys and expected values for specific keys.
    """
    locator = locators_data.get("publish")
    assert locator is not None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//div[@aria-label='Опубликовать' or @aria-label='Отправить' or @aria-label='Далее']"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["mandatory"] is True
    assert "locator_description" in locator
    
def test_send_valid(locators_data):
    """
    Checks if 'send' locator is correctly defined.
    Verifies the presence of all mandatory keys and expected values for specific keys.
    """
    locator = locators_data.get("send")
    assert locator is not None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "(//span[contains(text(),'Отправить')])[last()]"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["mandatory"] is True
    assert "locator_description" in locator
    
def test_not_now_valid(locators_data):
    """
    Checks if 'not_now' locator is correctly defined.
    Verifies the presence of all mandatory keys and expected values for specific keys.
    """
    locator = locators_data.get("not_now")
    assert locator is not None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//span[contains(text(),'Не сейчас')]"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["mandatory"] is True
    
def test_close_pop_up_valid(locators_data):
    """
    Checks if 'close_pop_up' locator is correctly defined.
    Verifies the presence of all mandatory keys and expected values for specific keys.
    """
    locator = locators_data.get("close_pop_up")
    assert locator is not None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//div[@aria-label = 'Закрыть']"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["mandatory"] is True

def test_edit_posts_valid(locators_data):
    """
    Checks if 'edit_posts' locator is correctly defined.
    Verifies the presence of all mandatory keys and expected values for specific keys.
    """
    locator = locators_data.get("edit_posts")
    assert locator is not None
    assert locator["by"] == "XPATH"
    assert locator["selector"] == "//span[@text = 'Управление публикациями']"
    assert locator["timeout"] == 0
    assert locator["timeout_for_event"] == "presence_of_element_located"
    assert locator["event"] == "click()"
    assert locator["mandatory"] is True

def test_locator_missing_keys(locators_data):
    """
    Checks for missing mandatory keys in any of the locators.
    This is to ensure that no mandatory keys are missing from any of the locator definitions.
    """
    mandatory_keys = ["by", "selector", "timeout", "timeout_for_event", "event", "mandatory"]
    for locator_name, locator_data in locators_data.items():
        for key in mandatory_keys:
             assert key in locator_data, f"Locator '{locator_name}' is missing the mandatory key: '{key}'"
        
def test_locator_invalid_type_keys(locators_data):
     """
    Checks for incorrect data types of values associated with specific keys in all locators.
    """
     for locator_name, locator_data in locators_data.items():
        assert isinstance(locator_data.get("by"), str), f"Locator '{locator_name}': 'by' key must be a string."
        assert isinstance(locator_data.get("selector"), str), f"Locator '{locator_name}': 'selector' key must be a string."
        assert isinstance(locator_data.get("timeout"), int), f"Locator '{locator_name}': 'timeout' key must be an integer."
        assert isinstance(locator_data.get("timeout_for_event"), str), f"Locator '{locator_name}': 'timeout_for_event' key must be a string."
        assert isinstance(locator_data.get("event"), str) or locator_data.get("event") is None, f"Locator '{locator_name}': 'event' key must be a string or None."
        assert isinstance(locator_data.get("mandatory"), bool) or isinstance(locator_data.get("mandatory"),str), f"Locator '{locator_name}': 'mandatory' key must be a bool or string."
        if "if_list" in locator_data:
            assert isinstance(locator_data.get("if_list"), str), f"Locator '{locator_name}': 'if_list' key must be a string."
        if "use_mouse" in locator_data:
             assert isinstance(locator_data.get("use_mouse"), bool) or isinstance(locator_data.get("use_mouse"), str) or locator_data.get("use_mouse") is None , f"Locator '{locator_name}': 'use_mouse' key must be a bool or string or None."
        if "attribute" in locator_data:
            assert isinstance(locator_data.get("attribute"), str) or locator_data.get("attribute") is None, f"Locator '{locator_name}': 'attribute' key must be a string or None."
        if "locator_description" in locator_data:
           assert isinstance(locator_data.get("locator_description"), str) , f"Locator '{locator_name}': 'locator_description' key must be a string."
        if "deprecated" in locator_data:
           assert isinstance(locator_data.get("deprecated"), str), f"Locator '{locator_name}': 'deprecated' key must be a string."
```