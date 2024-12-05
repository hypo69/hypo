rst
How to use this HTML form for sending data to a FastAPI endpoint
========================================================================================

Description
-------------------------
This HTML code defines a form for collecting user input (first name and last name).  It uses JavaScript and jQuery to send this data to a FastAPI endpoint (`/process_data` in the example) via an AJAX POST request.  The form data is serialized as JSON. The code handles successful responses and errors during the AJAX request.

Execution steps
-------------------------
1. The user fills in the first and last name fields in the HTML form.
2. The user clicks the "Отправить" (Submit) button.
3. The JavaScript code intercepts the form submission event.
4. It retrieves the values entered in the "Имя" (First Name) and "Фамилия" (Last Name) input fields.
5. It constructs a JSON object with the extracted data.
6. It sends a POST request to the FastAPI endpoint `/process_data` with the JSON data.
7. If the request is successful, the FastAPI endpoint processes the data and returns a response.
8. The JavaScript code handles the response.  Successful responses are logged in the console.  Error responses are also logged in the console to assist with debugging.


Usage example
-------------------------
.. code-block:: html+javascript

    <!DOCTYPE html>
    <html>
    <head>
        <title>Form for sending data</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    </head>
    <body>
        <div class="container">
            <h2>Form for sending data</h2>
            <form id="dataForm">
                <div class="form-group">
                    <label for="firstName">First name:</label>
                    <input type="text" class="form-control" id="firstName" placeholder="Enter first name" required>
                </div>
                <div class="form-group">
                    <label for="lastName">Last name:</label>
                    <input type="text" class="form-control" id="lastName" placeholder="Enter last name" required>
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>

        <script>
            $('#dataForm').submit(function(event) {
                event.preventDefault();
                var firstName = $('#firstName').val();
                var lastName = $('#lastName').val();
                $.ajax({
                    type: 'POST',
                    url: '/process_data', // Replace with your FastAPI endpoint
                    contentType: 'application/json',
                    data: JSON.stringify({first_name: firstName, last_name: lastName}),
                    success: function(response) {
                        console.log('Server response:', response);
                    },
                    error: function(xhr, status, error) {
                        console.error('Error sending data:', error);
                    }
                });
            });
        </script>
    </body>
    </html>