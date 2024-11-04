## \file src/webdriver/_experiments/test_execute_locator.py
## \file src/webdriver/_experiments/test_execute_locator.py

import unittest
from unittest.mock import MagicMock, patch
import sys
sys.path.insert(0, '../')
from src.webdriver.executor import execute_locator, \
                            execute_event, \
                            get_attribute_from_webelement

from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class TestExecuteLocator(unittest.TestCase):

    def setUp(self):
        self.mock_driver = 'mock_driver'

    def test_get_webelments_from_page(self):
        # Test when no action or attribute is provided in the locator
        locator = {'action': None, 'attribute': None}
        result = execute_locator(self.mock_driver, locator)
        self.assertEqual(result, get_webelements_from_page(
            self.mock_driver, locator))

    def test_get_attributes_from_webelements(self):
        # Test when action is not provided in the locator, but an attribute is provided
        locator = {'action': None, 'attribute': 'class'}
        result = execute_locator(self.mock_driver, locator)
        self.assertEqual(result, get_attributes_from_webelements(
            self.mock_driver, locator))

    def test_execute_event(self):
        # Test when a single action is provided in the locator
        locator = {'action': 'click', 'attribute': 'class',
                   'by': 'class_name', 'selector': 'example'}
        result = execute_locator(self.mock_driver, locator)
        self.assertEqual(result, execute_event(self.mock_driver, locator))

    def test_execute_multiple_actions(self):
        # Test when multiple actions are provided in the locator
        locator = {'action': ['move_to_element', 'click'],
                   'attribute': 'class', 'by': 'class_name', 'selector': 'example'}
        result = execute_locator(self.mock_driver, locator)
        self.assertEqual(result, [execute_event(self.mock_driver, {'action': 'move_to_element', 'attribute': 'class', 'by': 'class_name', 'selector': 'example'}),
                                  execute_event(self.mock_driver, {'action': 'click', 'attribute': 'class', 'by': 'class_name', 'selector': 'example'})])

    def test_execute_nested_locator(self):
        # Test when the locator contains nested locators
        locator = {'action': ['move_to_element', {'action': 'click', 'attribute': 'class', 'by': 'class_name', 'selector': 'example'}],
                   'attribute': 'class', 'by': 'class_name', 'selector': 'parent'}
        result = execute_locator(self.mock_driver, locator)
        self.assertEqual(result, [execute_event(self.mock_driver, {'action': 'move_to_element', 'attribute': 'class', 'by': 'class_name', 'selector': 'parent'}),
                                  execute_event(self.mock_driver, {'action': 'click', 'attribute': 'class', 'by': 'class_name', 'selector': 'example'})])


class TestExecuteAction(unittest.TestCase):


class TestGetAttributeStringFormatterromWebElementsByLocator(unittest.TestCase):

    @patch('app.get_webelements_from_page', return_value=[MagicMock(get_attribute=MagicMock(return_value='foo'))])
    def test_no_attribute_provided(self, mock_get_webelments):
        driver = MagicMock()
        locator = {"by": "id", "selector": "some_id",
                   "event": None, "attribute": None}

        result = get_attributes_from_webelements(driver, locator)

        mock_get_webelments.assert_called_once_with(driver, locator)
        self.assertEqual(result, ['foo'])

    def test_attribute_is_dict(self):
        driver = MagicMock()
        driver.get_attribute = MagicMock(return_value='foo')
        locator = {"by": "id", "selector": "some_id", "event": None,
                   "attribute": {"key1": "value1", "key2": "value2"}}

        result = get_attributes_from_webelements(driver, locator)

        driver.get_attribute.assert_any_call('key1')
        driver.get_attribute.assert_any_call('key2')
        self.assertEqual(result, [{"value1": "foo"}, {"value2": "foo"}])

    def test_attribute_is_list(self):
        driver = MagicMock()
        driver.get_attribute = MagicMock(return_value='foo')
        locator = {"by": "id", "selector": "some_id",
                   "event": None, "attribute": ["attr1", "attr2"]}

        result = get_attributes_from_webelements(driver, locator)

        driver.get_attribute.assert_any_call('attr1')
        driver.get_attribute.assert_any_call('attr2')
        self.assertEqual(result, ['foo', 'foo'])

    def test_attribute_is_string(self):
        driver = MagicMock()
        driver.get_attribute = MagicMock(return_value='foo')
        locator = {"by": "id", "selector": "some_id",
                   "event": None, "attribute": "attr"}

        result = get_attributes_from_webelements(driver, locator)

        driver.get_attribute.assert_called_once_with('attr')
        self.assertEqual(result, 'foo')


class TestGetAttributeFromWebElementByLocator(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")

    def test_get_single_attribute(self):
        locator = {'by': 'name', 'selector': 'q', 'attribute': 'placeholder'}
        result = get_attribute_from_webelement(self.driver, locator)
        self.assertEqual(result, 'Поиск')

    def test_get_multiple_attributes(self):
        locator = {'by': 'class name', 'selector': 'gb_3',
                   'attribute': ['href', 'title']}
        result = get_attribute_from_webelement(self.driver, locator)
        self.assertEqual(
            result, ['https://www.google.com/intl/en/about/products?tab=wh', 'Google apps'])

    def test_nonexistent_attribute(self):
        locator = {'by': 'name', 'selector': 'q', 'attribute': 'nonexistent'}
        result = get_attribute_from_webelement(self.driver, locator)
        self.assertEqual(result, [])

    def test_nonexistent_element(self):
        locator = {'by': 'name', 'selector': 'nonexistent',
                   'attribute': 'placeholder'}
        result = get_attribute_from_webelement(self.driver, locator)
        self.assertEqual(result, [])

    def tearDown(self):
        self.driver.quit()


class TestGetWebElementStringFormatterromPage(unittest.TestCase):
    """ Note that in the last test, we use the @patch decorator to mock the logger.error function, 
    so that we can check if it is called with the expected arguments. We also use the side_effect parameter 
    of the MagicMock object to raise an exception and test the error handling of the function."""
    def setUp(self):
        self.driver = MagicMock(spec=webdriver.Chrome)

    def tearDown(self):
        self.driver.quit()

    def test_get_webelments_from_page_with_one_element(self):
        expected = MagicMock(spec=webdriver.remote.webelement.WebElement)
        self.driver.find_elements.return_value = [expected]
        locator = {'by': 'id', 'selector': 'my_element'}
        actual = get_webelements_from_page(self.driver, locator)
        self.assertEqual(actual, expected)

    def test_get_webelments_from_page_with_multiple_elements(self):
        expected = [MagicMock(spec=webdriver.remote.webelement.WebElement),
                    MagicMock(spec=webdriver.remote.webelement.WebElement)]
        self.driver.find_elements.return_value = expected
        locator = {'by': 'class_name', 'selector': 'my_class'}
        actual = get_webelements_from_page(self.driver, locator)
        self.assertEqual(actual, expected)

    def test_get_webelments_from_page_with_no_elements(self):
        self.driver.find_elements.return_value = []
        locator = {'by': 'tag_name', 'selector': 'my_tag'}
        actual = get_webelements_from_page(self.driver, locator)
        self.assertFalse(actual)

    @patch('your_module.logger.error')
    def test_get_webelments_from_page_with_invalid_locator(self, mocklogger_console_error):
        self.driver.find_elements.side_effect = Exception()
        locator = {'by': 'invalid', 'selector': 'my_element'}
        actual = get_webelements_from_page(self.driver, locator)
        self.assertFalse(actual)
        mocklogger_console_error.assert_called_once()


class TestGetWebElementAsScreenshot(unittest.TestCase):

    def test_valid_webelement(self):
        # create a mock webelement
        mock_webelement = Mock()
        # set screenshot_as_png attribute to a valid value
        mock_webelement.screenshot_as_png = b'valid_png_data'

        # call function with mock webelement
        result = get_webelement_as_screenshot(mock_webelement)

        # check if the result is not False
        self.assertIStringNormalizerot(result, False)

    def test_invalid_webelement(self):
        # create a mock webelement
        mock_webelement = Mock()
        # set screenshot_as_png attribute to raise an exception
        mock_webelement.screenshot_as_png = Mock(
            side_effect=Exception('Error'))

        # call function with mock webelement
        result = get_webelement_as_screenshot(mock_webelement)

        # check if the result is False
        self.assertIs(result, False)


class TestClick(unittest.TestCase):


class TestGetImgsLinks(unittest.TestCase):
    
    

    def test_returns_none_when_no_imgs_found(self):
        # Arrange
        mock_driver = MagicMock()
        mock_driver.execute_locator.return_value = None
        url = "http://example.com"

        # Act
        result = get_imgs_links(mock_driver, url)

        # Assert
        self.assertIStringNormalizerone(result)

    def test_returns_dict_when_imgs_found(self):
        # Arrange
        mock_driver = MagicMock()
        mock_driver.execute_locator.return_value = {
            "img1": "http://example.com/img1.jpg",
            "img2": "http://example.com/img2.jpg"
        }
        url = "http://example.com"

        # Act
        result = get_imgs_links(mock_driver, url)

        # Assert
        self.assertIsInstance(result, dict)
        self.assertDictEqual(result, {
            "img1": "http://example.com/img1.jpg",
            "img2": "http://example.com/img2.jpg"
        })

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://example.com")

    def tearDown(self):
        self.driver.quit()

    def test_click_element(self):
        locator = {
            "by": By.XPATH,
            "selector": "//a[contains(text(),'More information')]",
            "if_list":"first","use_mouse": False
        }
        result = click(self.driver, locator)
        self.assertTrue(result)
        self.assertIn("wikipedia.org", self.driver.current_url)

    def test_click_element_with_mouse(self):
        locator = {
            "by": By.XPATH,
            "selector": "//a[contains(text(),'More information')]",
            "if_list":"first","use_mouse": false
        }
        result = click(self.driver, locator)
        self.assertTrue(result)
        self.assertIn("wikipedia.org", self.driver.current_url)

    def test_click_nonexistent_element(self):
        locator = {
            "by": By.XPATH,
            "selector": "//a[contains(text(),'Not Found')]",
            "if_list":"first","use_mouse": False
        }
        result = click(self.driver, locator)
        self.assertFalse(result)
if __name__ == '__main__':
    unittest.main()

