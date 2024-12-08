rst
How to use the FastAPI application
========================================================================================

Description
-------------------------
This code defines a FastAPI application that receives input from an HTML form, executes a Python script (`script.py`) with the input, and returns the output to the user. It also serves static files (like HTML) from a specified directory.  It handles potential errors during script execution and provides proper HTTP responses.


Execution steps
-------------------------
1. **Set up the application:**
   - The code initializes a FastAPI application instance (`app`).
   - It mounts the 'html' directory as static files, making the HTML content accessible.
   - Opens the default index.html page in the browser automatically.

2. **Define endpoints:**
   - `process_data` endpoint:
     - Receives `first_name` and `last_name` data from a form submission.
     - **Input Validation:** Checks if both `first_name` and `last_name` are provided.  Returns a 400 Bad Request error if not.
     - **Input Formatting:** Creates a string `input_data` by concatenating the input names.
     - **Script Execution:** Executes the external Python script (`script.py`) using `subprocess.Popen`. It passes the `input_data` as input.
     - **Error Handling:** Checks if the script execution was successful (`process.returncode`).  Returns a 500 Internal Server Error with an error message if the script execution failed.
     - **Output Return:** Returns the output from the executed script as the response.
   - `open_index` endpoint:
     - This endpoint simply redirects the user to the index.html page.

3. **External Script (`script.py`):**
   - This script (not included in the provided code) is expected to take input from standard input, process it, and return its output to standard output.


Usage example
-------------------------
.. code-block:: html
    <!DOCTYPE html>
    <html>
    <head>
        <title>FastAPI Form</title>
    </head>
    <body>
        <h1>Enter Your Name</h1>
        <form method="post" action="/process_data">
            <input type="text" name="first_name" placeholder="First Name">
            <input type="text" name="last_name" placeholder="Last Name">
            <button type="submit">Submit</button>
        </form>
    </body>
    </html>

.. code-block:: python
    # Example usage in a Python script to test the API
    import requests
    import json
    
    # Replace with your actual API endpoint URL
    url = "http://localhost:8000/process_data"
    
    # Example input data
    first_name = "John"
    last_name = "Doe"
    data = {"first_name": first_name, "last_name": last_name}
    
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        result = response.json()
        print(f"Output from the script: {result['output']}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")