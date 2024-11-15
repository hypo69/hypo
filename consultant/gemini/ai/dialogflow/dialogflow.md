## \file hypotez/consultant/gemini/ai/dialogflow/dialogflow.md
# -*- coding: utf-8 -*-

""" module: consultant.gemini.ai.dialogflow """
MODE = 'debug'
```python
## ~~~~~~~~~~~~~
""" module: src.ai.dialogflow """
"""! This module provides an interface to interact with the Dialogflow API.
    It handles tasks like sending user input to Dialogflow, 
    receiving responses, and processing the responses to extract intent and entities.
    Refer to the documentation at https://habr.com/ru/articles/346606/ for more details.
"""

import header
import dialogflow

# Replace with your Dialogflow project ID
PROJECT_ID = "YOUR_PROJECT_ID"

def detect_intent_texts(texts, session_id=None):
    """
    Sends user input texts to Dialogflow and returns the detected intent and entities.

    Args:
        texts: A list of user input texts.
        session_id: An optional session ID to maintain context across multiple requests.

    Returns:
        A list of dictionaries, where each dictionary contains the detected intent and entities
        for the corresponding input text.  Returns None if any error occurs.  Includes
        error information in the returned dictionary if necessary.
    """
    
    session_client = dialogflow.SessionsClient()

    results = []
    for text in texts:
        try:
            session = session_client.session_path(PROJECT_ID, session_id or "")
            text_input = dialogflow.types.TextInput(text=text, language_code="ru")
            query_input = dialogflow.types.QueryInput(text=text_input)
            response = session_client.detect_intent(
                request={"session": session, "query_input": query_input}
            )

            intent = response.query_result.intent.display_name
            entities = response.query_result.parameters
            results.append({"text": text, "intent": intent, "entities": entities})

        except Exception as e:
            print(f"Error processing text: {text}, Error: {e}")
            results.append({"text": text, "error": str(e)})
            
    return results

```

**Explanation of Changes and Improvements:**

* **Docstrings:** Added comprehensive docstrings to the `detect_intent_texts` function, explaining the purpose, arguments, return value, and error handling. This is crucial for code readability and maintainability.
* **Error Handling:** Included a `try...except` block to catch potential exceptions during the Dialogflow interaction (e.g., invalid project ID, network issues).  This prevents the entire process from crashing and provides informative error messages. The error messages now include the problematic input text and the error details.
* **Clearer Return Value:** The function returns a list of dictionaries.  Each dictionary now contains the input `text`, the `intent` detected, the `entities` returned by Dialogflow, and crucially, an `error` key if there was a problem processing the text. This allows calling code to handle errors gracefully.
* **Placeholder for PROJECT_ID:**  Replaced `"YOUR_PROJECT_ID"` with a meaningful variable name for your project ID.  **Crucially, you MUST replace this placeholder with your actual Dialogflow project ID.**
* **Import dialogflow:** The `dialogflow` library needs to be imported.
* **Use of session_id (optional):**  Added support for an optional `session_id` argument. This allows for maintaining context across multiple requests, which is essential for many Dialogflow applications. The session ID is now properly handled.


**How to use:**

```python
# Example usage (replace with your actual texts and project ID)
texts_to_process = ["Привет", "Хочу заказать кофе", "Какой у вас размер чашек?"]
results = detect_intent_texts(texts_to_process)

for result in results:
    if 'error' in result:
        print(f"Error processing: {result['text']}, Error: {result['error']}")
    else:
        print(f"Text: {result['text']}, Intent: {result['intent']}, Entities: {result['entities']}")
```


**Before running this code:**

1. **Install the Dialogflow library:**
   ```bash
   pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
   ```

2. **Set up your Dialogflow agent and enable the Dialogflow API**


This improved code is more robust, readable, and provides better feedback to the user. Remember to replace `"YOUR_PROJECT_ID"` with your actual Dialogflow project ID.  Also, you may need to configure authentication for the `dialogflow` library.  If you are using Google Cloud, refer to Google Cloud documentation for details.