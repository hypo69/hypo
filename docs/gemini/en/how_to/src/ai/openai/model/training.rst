rst
How to use the OpenAIModel class
========================================================================================

Description
-------------------------
This code defines a class `OpenAIModel` for interacting with the OpenAI API.  It handles tasks like sending messages to the model, retrieving responses, performing sentiment analysis, dynamically loading models and assistants, and training the model.  It includes methods for handling both text and image inputs.  The class manages the dialogue log and saves it to a JSON file.  Importantly, it incorporates error handling and retry mechanisms for robustness.

Execution steps
-------------------------
1. **Initialization:**
    - The `OpenAIModel` class is initialized with an OpenAI API key (obtained from `gs.credentials.openai.api_key`), an optional `system_instruction` for the model, and an optional `assistant_id`.
    - It retrieves the assistant using the provided or default `assistant_id` and creates a thread for conversation.
    - Optionally, the system instruction and model name can be customized.
2. **Loading Models and Assistants:**
    - The `list_models` method dynamically fetches and returns a list of available OpenAI models.
    - The `list_assistants` method retrieves a list of assistant names from a JSON file.
3. **Setting an Assistant:**
    - The `set_assistant` method allows updating the active assistant to a different one using its ID.
4. **Sending a Message and Receiving a Response:**
    - The `ask` method sends a message to the model, handling optional system instructions.
    - It escapes quotes within the message and instructions.
    - It performs sentiment analysis on the response.
    - It appends the message, response, and sentiment to the dialogue log.
    - It saves the dialogue log to a JSON file.  
    - Includes error handling to retry sending if necessary.
5. **Describing an Image:**
    - The `describe_image` method allows describing an image by passing the image path and optional prompt or system instructions.
    - It encodes the image to base64 format.
    - It creates a formatted message for the OpenAI API request including the image.
    - It handles the API response, decoding the result from the API response.
6. **Image Description using Requests (Alternative):**
    - The `describe_image_by_requests` method provides an alternative way to send image descriptions using the `requests` library. This method follows similar steps as describe_image method, using a different library for interaction with the OpenAI API
7. **Dynamic Training:**
    - The `dynamic_train` method loads past dialogue from a JSON file and optionally fine-tunes the model using the loaded dialogue data.
8. **Training the Model:**
    - The `train` method trains the model on data from a CSV file or directory.
    - `documents` are loaded from the specified source (e.g., CSV file or directory).
    - Training labels (`positive`/`negative`) are automatically determined based on the presence of the positive flag.
    - The training job ID is stored.
9. **Saving Job ID:**
    - The `save_job_id` method saves the training job ID along with its description to a JSON file.

Usage example
-------------------------
.. code-block:: python

    import hypotez.src.ai.openai.model as openai_model
    import src.utils.google_storage as gs

    # ... (Ensure gs.credentials and gs.path are properly initialized) ...

    # Initialize the model
    model = openai_model.OpenAIModel(system_instruction="You are a helpful assistant.", assistant_id="asst_dr5AgQnhhhnef5OSMzQ9zdk9")

    # Example usage: Ask a question
    user_input = "What is the capital of France?"
    response = model.ask(user_input)
    print("Model Response:", response)

    # Example usage: Describe an image
    image_path = gs.path.google_drive / "images" / "example_image.jpg"
    image_description = model.describe_image(image_path)
    print("Image Description:", image_description)
    

    # Example of training
    training_job_id = model.train(data_file=gs.path.google_drive / "AI" / "training_data.csv")
    print(f"Training job ID: {training_job_id}")

    # ... (Example saving job ID - complete as above) ...