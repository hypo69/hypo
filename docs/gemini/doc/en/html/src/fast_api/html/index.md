html
<!--
  Generated HTML documentation for the provided Python code.
-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form for Sending Data</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1>Module: src.fast_api.html</h1>

        <h2>Overview</h2>
        <p>This module provides an HTML form for sending data to a FastAPI endpoint.</p>

        <h2>HTML Structure</h2>
        <p>The HTML structure includes a form with input fields for first name and last name, and a submit button.  It uses Bootstrap for styling.</p>


        <h2>JavaScript Functionality</h2>
        <p>The JavaScript code handles the form submission.  Upon submission:</p>
        <ul>
          <li>It prevents the default form submission.</li>
          <li>It retrieves the values from the 'first name' and 'last name' input fields.</li>
          <li>It serializes the data into JSON format using <code>JSON.stringify</code>.</li>
          <li>It sends a POST request to the specified FastAPI endpoint (currently set to <code>/process_data</code>).</li>
          <li>It handles successful responses by logging the response to the console.</li>
          <li>It handles errors during the AJAX request by logging the error to the console.</li>
        </ul>

        <h3>JavaScript Example</h3>
        <pre><code class="language-javascript">
$(\'#dataForm\').submit(function(event) {
    event.preventDefault();
    var firstName = $(\'#firstName\').val();
    var lastName = $(\'#lastName\').val();
    $.ajax({
        type: 'POST',
        url: '/process_data',
        contentType: 'application/json',
        data: JSON.stringify({first_name: firstName, last_name: lastName}),
        success: function(response) {
            console.log('Response from server:', response);
        },
        error: function(xhr, status, error) {
            console.error('Error sending data:', error);
        }
    });
});
        </code></pre>


        <h2>Usage Instructions</h2>
        <p>To use this form, make sure you have a corresponding FastAPI endpoint defined to handle the POST request at the <code>/process_data</code> URL. The endpoint should receive the JSON data and process it accordingly.</p>



    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</body>
</html>