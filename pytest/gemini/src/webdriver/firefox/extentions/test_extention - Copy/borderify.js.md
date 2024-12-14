```python
import pytest

# Since the provided JavaScript code modifies the DOM and uses alert,
# it's not directly testable with pytest (which is for Python).
# However, we can mock the behavior using libraries like playwright/selenium with pytest and write tests based on these.
# For the purpose of this exercise, we will outline a potential pytest structure assuming we are testing an abstraction that calls this JavaScript.
# If you can provide actual Python code interacting with this JS, I can generate more relevant tests.

# Mock Fixtures (replace with actual if there's a python class that interacts with the JS)
@pytest.fixture
def mock_browser():
    """Simulates a browser object"""
    class MockBrowser:
        def __init__(self):
            self.alert_called = False
            self.body_style = {}

        def execute_script(self, script):
            if 'document.body.style.border = "5px solid red";' in script:
                self.body_style['border'] = '5px solid red'
            if 'alert()' in script:
                self.alert_called = True
    return MockBrowser()


# Mock function that interacts with JS
def apply_js_changes(browser):
    """Simulates applying the given JavaScript changes"""
    script = 'document.body.style.border = "5px solid red";\nalert()'
    browser.execute_script(script)
    return browser

# Test Cases
def test_apply_js_changes_border_applied(mock_browser):
    """Tests that applying the js sets the border style"""
    browser = apply_js_changes(mock_browser)
    assert browser.body_style.get('border') == '5px solid red', "Border style was not set correctly."

def test_apply_js_changes_alert_triggered(mock_browser):
    """Tests that applying the js triggers alert"""
    browser = apply_js_changes(mock_browser)
    assert browser.alert_called, "Alert function was not called."


def test_apply_js_changes_no_script_exception():
  """Tests if no script passed in, it does not break"""
  class MockBrowser:
      def __init__(self):
          self.alert_called = False
          self.body_style = {}

      def execute_script(self, script):
          if 'document.body.style.border = "5px solid red";' in script:
              self.body_style['border'] = '5px solid red'
          if 'alert()' in script:
              self.alert_called = True
  browser = MockBrowser()
  # Test No script
  try:
    browser.execute_script('')
  except Exception as e:
      assert False, "Unexpected error when executing empty script: {}".format(e)
  assert True

def test_apply_js_changes_empty_script(mock_browser):
    """Tests if empty string passed it works"""
    browser = mock_browser
    try:
      browser.execute_script('')
    except Exception as e:
      assert False, "Unexpected exception with empty string"

    assert not browser.alert_called
    assert not browser.body_style



def test_apply_js_changes_invalid_script(mock_browser):
    """Tests if an invalid script is provided"""
    browser = mock_browser
    try:
        browser.execute_script("invalid javascript string")
    except Exception as e:
         assert False, "Unexpected error when executing invalid javascript : {}".format(e)

```