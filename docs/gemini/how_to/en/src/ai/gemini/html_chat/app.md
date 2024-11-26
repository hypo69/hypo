# Usage Guide for `hypotez/src/ai/gemini/html_chat/app.py`

This Python script implements a simple HTML chat application using FastAPI, leveraging the `Kazarinov` model for AI responses.  It allows users to submit questions, and the application retrieves responses from the model.  The application displays the responses in an HTML chat interface.

## Prerequisites

*   **Python 3.12+:** Ensure you have Python 3.12 or a later version installed.
*   **FastAPI:** Install the FastAPI framework:
    ```bash
    pip install fastapi uvicorn pydantic
    ```
*   **Jinja2:** Install Jinja2 for templating:
    ```bash
    pip install jinja2
    ```
*   **Kazarinov model:** Your Kazarinov code (likely in `src.ai.gooogle_generativeai.kazarinov`) must be functional and the required libraries installed. This example depends on `src.ai.gooogle_generativeai.kazarinov.Kazarinov`. You need to make sure this is set up properly and imported correctly.
*   **Other Libraries:** Ensure libraries like `webbrowser`, `threading`, and `pathlib` are available.

## Configuration

1.  **`MODE` Variable:** The `MODE` variable currently defaults to `'dev'`.  No specific configuration is needed for this value unless your code handles different modes.
2.  **Template and Static Files:** The application loads templates from `gs.path.src / 'ai' / 'gooogle_generativeai' / 'chat' / 'templates'` and static assets (like CSS) from `gs.path.src / 'ai' / 'gooogle_generativeai' / 'chat' / 'static'`.  **Crucially**, make sure these directories exist and contain the necessary files (e.g., `chat.html`, CSS files).  The `gs` module (`from src import gs`) likely handles paths. You need to ensure that the `gs` module is correctly defined in your `src` package.
3.  **`questions_list`:** This list holds questions from files located in the `google_drive/kazarinov/prompts/q` directory. The paths to these files are dynamic, so make sure the `google_drive` path points to the correct location.  The script reads the content of all `.txt` files, effectively loading the list of prompts.
4.  **`Kazarinov` initialization:** This code instantiates the Kazarinov model with specific configuration options (`generation_config`). Ensure you have correctly initialized your `Kazarinov` model instance.


## How to Run

1.  **Start the FastAPI server:**  Run the script from the command line:
    ```bash
    uvicorn hypotez.src.ai.gemini.html_chat.app:app --host 127.0.0.1 --port 8000
    ```
2.  **Open a web browser:** A browser window will automatically open to the address `http://127.0.0.1:8000` after a brief delay.  The delay is important so that the server has time to start. The script uses a `threading.Timer` to ensure the browser opens promptly.

## Functionality

*   **Initial Page:** The `/` route displays an empty chat interface (`chat.html`).
*   **`ask_question` Endpoint:**
    *   Handles POST requests to `/ask`.
    *   Accepts a `Question` object (containing the user's input question).
    *   If the user enters '--next', a random question from the `questions_list` is selected for the model.
    *   Passes the user's question to the `Kazarinov` model for processing.
    *   Returns a template response (`chat.html`) updating the `response` section to display the response from the model.


## Important Considerations

* **Error Handling:**  The code currently lacks robust error handling. Consider adding `try...except` blocks to catch potential issues (e.g., if the Kazarinov model fails, or the prompt files are not accessible) and display informative error messages to the user.
* **Security:** If user input is not properly sanitized, there are potential security concerns (e.g., XSS vulnerability). Input validation should be implemented.
* **`gs` Module:** You need to ensure the `gs` module is correctly defined in your project.
* **Kazarinov Model Details:** This guide assumes you understand the `Kazarinov` model's input and output expectations and how to integrate with it.

This guide provides a basic understanding of how the script functions.  More specific instructions will depend on the details of the `Kazarinov` model implementation and the `gs` module.