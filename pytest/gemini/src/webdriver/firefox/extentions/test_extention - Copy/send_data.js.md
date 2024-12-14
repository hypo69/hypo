```python
import pytest
from unittest.mock import patch, MagicMock
import json
from playwright.sync_api import Browser, Page

# Since the provided JavaScript code interacts with the browser's DOM and network,
# we'll need to simulate these interactions using libraries like Playwright for browser manipulation
# and unittest.mock for mocking network requests.

# Fixture to create a browser context and a new page
@pytest.fixture
def page(browser: Browser) -> Page:
    page = browser.new_page()
    yield page
    page.close()


# Helper function to simulate fetch behavior
def mock_fetch(expected_data: dict, status=200, json_data=None):
    mock_response = MagicMock()
    mock_response.ok = status == 200
    mock_response.status = status
    mock_response.json = MagicMock(return_value=json_data)
    return mock_response


# Test cases for the onPageLoad function's behavior.

def test_onpageload_valid_data_post_request(page: Page):
    """
    Test if the fetch request is correctly formatted with correct data
     when the page loads.
    """
    
    expected_url = 'http://127.0.0.1/hypotez.online/api/'
    expected_title = 'Test Page Title'
    expected_body = '<div>Test Body</div>'
    expected_data = {
            'title': expected_title,
            'url': "about:blank",
            'body': expected_body,
        }
    expected_json_data = {"message": "success"}
   
    page.set_content(f"<html><head><title>{expected_title}</title></head><body>{expected_body}</body></html>")
    
    with patch('playwright.sync_api.Page.evaluate', return_value=expected_data):
        with patch('playwright.sync_api.Page.evaluate_handle',return_value=page.locator('body')):
           with patch('playwright.sync_api.Page.wait_for_load_state',return_value=None):
             with patch('playwright.sync_api.Page.evaluate', return_value=expected_data):
              with patch('playwright.sync_api.Page.evaluate_handle',return_value=page.locator('body')):
                with patch("playwright.sync_api.Page.request.post", return_value=mock_fetch(expected_data, status=200, json_data=expected_json_data)) as mock_post:
                   
                    page.evaluate(
                        """
                        function onPageLoad() {
                            // Собираем информацию о странице
                            var title = document.title;
                            var url = window.location.href;
                            var body = document.body.innerHTML;

                            // Формируем объект с данными для отправки
                            var data = {
                                title: title,
                                url: url,
                                body: body
                            };

                            // Отправляем данные на указанный адрес
                            fetch('http://127.0.0.1/hypotez.online/api/', {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json'
                                },
                                body: JSON.stringify(data)
                            })
                                .then(response => {
                                    if (!response.ok) {
                                        throw new Error('Network response was not ok');
                                    }
                                    return response.json();
                                })
                                .then(json => {
                                    console.log('Response:', json);
                                })
                                .catch(error => {
                                    console.error('Error:', error);
                                });
                        }
                        window.addEventListener('load', onPageLoad);
                        """
                    )
                    
                    page.wait_for_load_state()
                    mock_post.assert_called_once()
                    actual_data = json.loads(mock_post.call_args.kwargs['data'])
                    assert mock_post.call_args[0][0] == expected_url
                    assert actual_data['title'] == expected_title
                    assert actual_data['url'] == "about:blank"
                    assert actual_data['body'] == expected_body


def test_onpageload_network_error(page: Page):
    """Test when the fetch request fails (e.g., network error)."""
    page.set_content("<html><head><title>Test</title></head><body><div>Body</div></body></html>")
    expected_data = {
            'title': 'Test',
            'url': "about:blank",
            'body': "<div>Body</div>"
        }
    
    with patch('playwright.sync_api.Page.evaluate', return_value=expected_data):
      with patch('playwright.sync_api.Page.evaluate_handle',return_value=page.locator('body')):
        with patch('playwright.sync_api.Page.wait_for_load_state',return_value=None):
           with patch("playwright.sync_api.Page.request.post",
                return_value=mock_fetch(expected_data, status=404)) as mock_post:
              with patch('playwright.sync_api.Page.on') as mock_console:
                  page.evaluate(
                     """
                        function onPageLoad() {
                            // Собираем информацию о странице
                            var title = document.title;
                            var url = window.location.href;
                            var body = document.body.innerHTML;

                            // Формируем объект с данными для отправки
                            var data = {
                                title: title,
                                url: url,
                                body: body
                            };

                            // Отправляем данные на указанный адрес
                            fetch('http://127.0.0.1/hypotez.online/api/', {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json'
                                },
                                body: JSON.stringify(data)
                            })
                                .then(response => {
                                    if (!response.ok) {
                                        throw new Error('Network response was not ok');
                                    }
                                    return response.json();
                                })
                                .then(json => {
                                    console.log('Response:', json);
                                })
                                .catch(error => {
                                    console.error('Error:', error);
                                });
                        }
                         window.addEventListener('load', onPageLoad);
                    """
                  )
                  page.wait_for_load_state()
                  mock_post.assert_called_once()
                  mock_console.assert_called_once()


def test_onpageload_invalid_json_response(page: Page):
    """Test the behavior of onPageLoad with an invalid JSON response."""
    page.set_content("<html><head><title>Test</title></head><body><div>Body</div></body></html>")
    expected_data = {
            'title': 'Test',
            'url': "about:blank",
            'body': "<div>Body</div>"
        }
    
    with patch('playwright.sync_api.Page.evaluate', return_value=expected_data):
      with patch('playwright.sync_api.Page.evaluate_handle',return_value=page.locator('body')):
        with patch('playwright.sync_api.Page.wait_for_load_state',return_value=None):
            with patch("playwright.sync_api.Page.request.post",
                    return_value=mock_fetch(expected_data, status=200, json_data="invalid json")) as mock_post:
                with patch('playwright.sync_api.Page.on') as mock_console:
                    page.evaluate(
                            """
                            function onPageLoad() {
                                // Собираем информацию о странице
                                var title = document.title;
                                var url = window.location.href;
                                var body = document.body.innerHTML;

                                // Формируем объект с данными для отправки
                                var data = {
                                    title: title,
                                    url: url,
                                    body: body
                                };

                                // Отправляем данные на указанный адрес
                                fetch('http://127.0.0.1/hypotez.online/api/', {
                                    method: 'POST',
                                    headers: {
                                        'Content-Type': 'application/json'
                                    },
                                    body: JSON.stringify(data)
                                })
                                    .then(response => {
                                        if (!response.ok) {
                                            throw new Error('Network response was not ok');
                                        }
                                        return response.json();
                                    })
                                    .then(json => {
                                        console.log('Response:', json);
                                    })
                                    .catch(error => {
                                        console.error('Error:', error);
                                    });
                            }
                            window.addEventListener('load', onPageLoad);
                        """
                        )
                    page.wait_for_load_state()
                    mock_post.assert_called_once()
                    mock_console.assert_called_once()
```