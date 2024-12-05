rst
How to use the FastAPI OpenAI module
========================================================================================

Description
-------------------------
This code defines a FastAPI application for interacting with the OpenAI model.  It provides endpoints to query the model and potentially train it.  Crucially, it handles requests and responses, including error handling and logging. It mounts static files for serving HTML and other resources.  The code also uses middleware for cross-origin resource sharing (CORS).

Execution steps
-------------------------
1. **Import necessary libraries:** The code imports essential libraries like `FastAPI`, `BaseModel`, `StaticFiles`, `CORSMiddleware`, `HTMLResponse`, `OpenAIModel`, and custom modules like `gs`, `jjson`, and `logger` for file paths, data handling, and logging.  It establishes the `OpenAIModel` class, presumably containing the OpenAI API interactions.

2. **Define FastAPI application and mount static files:** A FastAPI application `app` is created.  The `/static` endpoint is configured to serve files from a specified directory (`gs.path.src / 'fast_api' / 'html' / 'openai_training'`), crucial for hosting supporting HTML/JS/CSS assets for UI elements.

3. **Enable CORS middleware:**  The application uses `CORSMiddleware` to allow requests from any origin, a critical step for browser-based integrations.

4. **Instantiate OpenAIModel:** The `OpenAIModel` object is instantiated, preparing for model interactions.

5. **Define request data model:** The `AskRequest` class uses `pydantic.BaseModel` to define the structure for requests sent to the `/ask` endpoint, specifically specifying fields for `message` and `system_instruction`.

6. **Define `/` endpoint to serve index.html:** This endpoint handles requests to the root URL (`/`) and serves the `index.html` file, likely containing UI elements for interacting with the OpenAI model.  It includes error handling for potential issues accessing the file.

7. **Define `/ask` endpoint for model queries:** This endpoint processes requests, extracting the user's message and optional system instructions. It utilizes the `model.ask` function to obtain a response from the OpenAI model.  It returns the response as a JSON object. The endpoint includes robust error handling, logging errors to the `logger` instance, and returning HTTP 500 errors with informative details.

8. **Run the application:** The application is launched using `uvicorn`, specifying the host and port for access.

Usage example
-------------------------
.. code-block:: python

    import requests
    import json

    # Replace with your actual FastAPI server address
    url = "http://127.0.0.1:8000/ask"

    # Sample request data
    data = {
        "message": "What is the capital of France?",
        "system_instruction": "Provide a concise answer."
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        # Parse the JSON response
        response_data = response.json()
        print(response_data.get("response"))

    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
    except (KeyError, json.JSONDecodeError) as e:
      print(f"Invalid response format: {e}")