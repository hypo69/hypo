```python
import pytest
from bs4 import BeautifulSoup

# Since the input is an HTML file, we'll focus on testing the structure and expected behavior of the HTML and JavaScript
# For this, we'll primarily use BeautifulSoup to parse the HTML and assert on its elements,
# And partially using JavaScript mocking for AJAX calls for JavaScript behavior.

# Fixture to load the HTML content
@pytest.fixture
def html_content():
    """Provides the HTML content for the test."""
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Форма для отправки данных</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container">
            <h2>Форма для отправки данных</h2>
            <form id="dataForm">
                <div class="form-group">
                    <label for="firstName">Имя:</label>
                    <input type="text" class="form-control" id="firstName" placeholder="Введите имя" required>
                </div>
                <div class="form-group">
                    <label for="lastName">Фамилия:</label>
                    <input type="text" class="form-control" id="lastName" placeholder="Введите фамилию" required>
                </div>
                <button type="submit" class="btn btn-primary">Отправить</button>
            </form>
        </div>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script>
            $('#dataForm').submit(function(event) {
                event.preventDefault();
                var firstName = $('#firstName').val();
                var lastName = $('#lastName').val();
                $.ajax({
                    type: 'POST',
                    url: '/process_data',
                    contentType: 'application/json',
                    data: JSON.stringify({first_name: firstName, last_name: lastName}),
                    success: function(response) {
                        console.log('Ответ от сервера:', response);
                    },
                    error: function(xhr, status, error) {
                        console.error('Ошибка при отправке данных:', error);
                    }
                });
            });
        </script>
    </body>
    </html>
    """


def test_html_structure(html_content):
    """
    Tests the basic structure of the HTML document.
    It checks for the presence of key elements like the form, inputs, and button.
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # Check for the form element
    form = soup.find('form', id='dataForm')
    assert form is not None, "Form element with id='dataForm' not found."

    # Check for input elements
    first_name_input = form.find('input', id='firstName')
    assert first_name_input is not None, "Input element with id='firstName' not found."

    last_name_input = form.find('input', id='lastName')
    assert last_name_input is not None, "Input element with id='lastName' not found."

    # Check for the submit button
    submit_button = form.find('button', type='submit')
    assert submit_button is not None, "Submit button not found."
    assert submit_button.text.strip() == 'Отправить', "Submit button text is not correct."


def test_html_form_inputs(html_content):
    """
    Tests attributes of HTML form input fields like required and placeholder.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    form = soup.find('form', id='dataForm')

    # Assert on required attribute of input elements
    first_name_input = form.find('input', id='firstName')
    assert first_name_input.get('required') == '', "First name input should have 'required' attribute."
    assert first_name_input.get('placeholder') == 'Введите имя', "First name placeholder text is incorrect."

    last_name_input = form.find('input', id='lastName')
    assert last_name_input.get('required') == '', "Last name input should have 'required' attribute."
    assert last_name_input.get('placeholder') == 'Введите фамилию', "Last name placeholder text is incorrect."



def test_html_has_js_scripts(html_content):
    """
    Tests if the html contains required script tags and the JavaScript submits the form and sends AJAX
    request to '/process_data'
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    scripts = soup.find_all('script')

    # Check if jQuery script and the inline script are found
    assert len(scripts) >= 2, "Not enough script tags found."

    # Basic check if ajax call is inside the script tag
    found_ajax_call = False
    for script in scripts:
        if script.string and '$.ajax' in script.string:
            found_ajax_call = True
            break

    assert found_ajax_call, "No $.ajax call found within script tags."

    # Basic check if the AJAX call contains the correct URL
    found_url = False
    for script in scripts:
        if script.string and "url: '/process_data'" in script.string:
            found_url = True
            break

    assert found_url, "URL '/process_data' not found in AJAX call."


# Mocking an AJAX request function (This part needs more setup with libraries like 'jsdom' for complete JavaScript testing)
# This is a simplified mock for demonstration in a test environment
# In real testing environment, you should consider using "jsdom" or other JavaScript testing tools.
def mock_ajax(type, url, contentType, data, success, error):
    """
    A mock for the $.ajax function.
    """
    if type == 'POST' and url == '/process_data' and contentType == 'application/json':
         if data:
            # Successfully send data
            success({'status': 'success', 'message': 'Data processed'})
         else:
            # Failed sending data
             error({'status': 'error', 'message': 'Invalid data'})


def test_javascript_form_submission_ajax_call(monkeypatch, html_content):
    """
    Tests the form submission by using mocking the AJAX call.
    This is very basic test - consider using 'jsdom' for comprehensive testing
    """
    # Apply a mock for the jQuery AJAX call
    monkeypatch.setattr('builtins.print', lambda *args: None)  # Suppress print output
    monkeypatch.setattr('js', mock_ajax) # For example purpose - should use jsdom and a virtual browser

    soup = BeautifulSoup(html_content, 'html.parser')
    script_content = soup.find_all('script')[-1].string  # grab the last script tag which is the inline script


    # Use simple approach to mock the values of the input
    class MockElement:
        def __init__(self, value):
            self.value = value

        def val(self):
           return self.value

    class MockJquery:
        def __init__(self):
             self.element_data = {}

        def __call__(self, selector):
            if selector == '#firstName':
                return MockElement("John")
            elif selector == '#lastName':
                return MockElement("Doe")
            return self

        def submit(self,callback):
            callback({'preventDefault': lambda : None}) # Call the callback
            return self
        
        def ajax(self, args):
            # Verify the ajax call based on the mock
            mock_ajax(args['type'], args['url'], args['contentType'], args['data'], args['success'], args['error'])

            return self

    # Mock jQuery function
    monkeypatch.setattr("js.$", MockJquery)

    # Execute the submit
    MockJquery().submit(lambda event: None ) # mock submit function

    # The mock ajax will be called inside the `submit` function.
    # Check if success or error based on the mock function if needed

```