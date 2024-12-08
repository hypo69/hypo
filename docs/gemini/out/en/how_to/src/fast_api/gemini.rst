rst
How to use the gemini.py code block
========================================================================================

Description
-------------------------
This Python code defines a Flask API endpoint (`/ask`) that utilizes a Google Generative AI model (presumably via the `GoogleGenerativeAI` class) to generate responses to user prompts. It handles requests using the `POST` method, expecting a JSON payload containing a 'prompt' key.  The code validates for the presence of the prompt.  If the prompt is missing or there's an error during the generation process, it returns appropriate error responses.

Execution steps
-------------------------
1. **Import necessary libraries:** The code imports the Flask framework for creating web APIs, and the `GoogleGenerativeAI` class, likely from a custom module (`src.ai.google_generativeai.generative_ai`). It also imports `request` and `jsonify` for handling HTTP requests and responses.

2. **Initialize Flask app and AI model:** A Flask application (`app`) is created, and an instance of the `GoogleGenerativeAI` class is initialized.

3. **Define API endpoint (`/ask`):**  A route (`/ask`) is defined using the `@app.route` decorator. This endpoint expects `POST` requests.

4. **Retrieve and validate the prompt:** The code retrieves the JSON data from the request (`request.get_json()`) and extracts the 'prompt' value. It checks if the prompt is present. If not, it returns a 400 Bad Request error with an appropriate message.

5. **Generate the AI response:**  The `ai_model.ask(prompt)` function is called to generate a reply from the AI model.

6. **Handle potential errors:** A `try...except` block handles potential errors during the AI request. If an error occurs (e.g., the AI model is unavailable or has an internal error), it returns a 500 Internal Server Error with the error message.

7. **Return the reply:** If successful, the generated reply is packaged into a JSON response and returned with a 200 OK status code.

8. **Run the application:** The code starts the Flask application in debug mode using `app.run(debug=True)`. This enables automatic code reloading and helpful error messages during development.

Usage example
-------------------------
.. code-block:: python

    import requests

    # Example payload (JSON data)
    payload = {
        "prompt": "Write a short story about a cat."
    }

    # Send a POST request to the API endpoint
    response = requests.post("http://127.0.0.1:5000/ask", json=payload)

    # Check the response status
    if response.status_code == 200:
        # Decode the JSON response
        data = response.json()
        print(f"Reply: {data['reply']}")
    else:
        print(f"Error: {response.json()['error']}")