rst
How to use the translate function
========================================================================================

Description
-------------------------
This Python code defines a function `translate` that performs text translation using the OpenAI API.  It takes the input text, source language, and target language as arguments and returns the translated text. The function handles potential errors during the API call and logs them.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports the `openai` library for interacting with the OpenAI API, `gs` likely for accessing credentials, and `logger` for logging errors.

2. **Set API key:** It sets the OpenAI API key using `openai.api_key = gs.credentials.openai`.  This step assumes `gs.credentials.openai` contains the API key.

3. **Define the translate function:**  The `translate` function takes the text to be translated, the source language, and the target language as input.

4. **Construct the prompt:** It constructs a prompt for the OpenAI API, including the source and target languages and the input text.  This prompt is crucial for guiding the API's translation process.

5. **Make the API call:** It uses the `openai.Completion.create` function to send the constructed prompt to the OpenAI API, specifying the model ("text-davinci-003"), maximum tokens, and other parameters.

6. **Extract the translation:**  It retrieves the translated text from the API response and removes leading/trailing whitespace.

7. **Error Handling:**  A `try...except` block is included to catch potential errors during the API call. If an error occurs, it logs the error using the `logger` and returns `None` instead of raising the exception. This improves robustness.

8. **Return the translation:** If no error occurs, the translated text is returned.


Usage example
-------------------------
.. code-block:: python

    import openai
    from src import gs
    from src.logger import logger
    # ... (assuming these imports work correctly) ...

    openai.api_key = gs.credentials.openai


    def translate(text, source_language, target_language):
        # ... (the function code as shown in the example code) ...


    source_text = "Привет, как дела?"
    source_language = "Russian"
    target_language = "English"

    translation = translate(source_text, source_language, target_language)

    if translation:
        print(f"Translated text: {translation}")
    else:
      print("Translation failed.")