rst
How to use the GoogleGenerativeAI class
========================================================================================

Description
-------------------------
This code defines a `GoogleGenerativeAI` class for interacting with Google's Generative AI models.  It handles API key configuration, model selection, sending requests, receiving responses, and saving dialogue history.  Crucially, it includes robust error handling for various potential issues like network problems, API errors, and authentication problems.  The class also manages attempts and exponential backoff for retries. It supports saving dialogue history to text and JSON files.


Execution steps
-------------------------
1. **Import necessary libraries:** The code imports libraries like `google.generativeai`, `requests`, `json`, and others for handling API requests, data manipulation, and logging.

2. **Define the `GoogleGenerativeAI` class:** This class encapsulates the interaction logic with the Generative AI model.

3. **Initialize the class (`__init__` method):**
    * Takes the `api_key`, `model_name`, `generation_config`, and `system_instruction` as input.
    * Sets default values for `model_name` and `generation_config` if not provided.
    * Sets paths for logging dialogue and saving history files.
    * Initializes the `genai.GenerativeModel` object using the provided API key, model name, and config.
    * Calls `_start_chat` to initialize the chat session.

4. **`ask` method:**
    * Sends a text prompt (`q`) to the model.
    * Implements retry logic (up to `attempts`) with exponential backoff in case of network errors, service unavailability, resource exhaustion, and authentication errors.
    * Logs errors and attempts.
    * Saves the dialogue to text and JSON files.
    * Returns the model's response (`response.text`) or None if no response is received after retries.
    * Handles various exceptions related to API interaction.

5. **`describe_image` method:**
    * Takes the image path as input.
    * Reads the image, encodes it to base64.
    * Sends the encoded image to the model.
    * Returns the generated description or None in case of errors.

6. **`upload_file` method:**
    * Uploads files to the Google Generative AI service.
    * Handles potential errors during upload, including retrying the upload after a successful deletion of the previous file.

7. **Error Handling:** The `ask` method includes comprehensive error handling, using `try...except` blocks to catch common problems like `requests.exceptions.RequestException`, `GatewayTimeout`, `ServiceUnavailable`, `ResourceExhausted`, authentication issues (e.g., `DefaultCredentialsError`), and invalid input.  This ensures the application remains stable and responsive even when encountering problems.



Usage example
-------------------------
.. code-block:: python

    from pathlib import Path
    from hypotez.src.ai.gemini.generative_ai import GoogleGenerativeAI

    # Replace with your API key
    api_key = "your_api_key"

    ai = GoogleGenerativeAI(api_key=api_key)

    # Ask a question
    response = ai.ask("What is the capital of France?")
    if response:
        print(response)

    # Describe an image
    image_path = Path("path/to/your/image.jpg")
    description = ai.describe_image(image_path)
    if description:
        print(description)

    # Upload a file
    file_path = Path("path/to/your/file.txt")
    upload_result = ai.upload_file(file_path, file_name="uploaded_file")
    if upload_result:
        print("File uploaded successfully")