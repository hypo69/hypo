rst
How to use the gtranslater module
========================================================================================

Description
-------------------------
This module provides a function `translate` for translating text using the Google Translate API.  It automatically detects the input language if not explicitly specified.  Error handling is included, logging any translation failures.

Execution steps
-------------------------
1. **Import necessary libraries:** The code imports the `Translator` class from the `googletrans` library, the `detect` function from `langdetect`, and the `logger` object from a custom `logger` module.

2. **Define the `translate` function:** This function takes the text to be translated, an optional input language code (`locale_in`), and an output language code (`locale_out`) as parameters.

3. **Initialize the translator:** A `Translator` object is created.

4. **Handle input language detection:**
   - If `locale_in` is not provided, it detects the input language using the `detect` function from `langdetect`.
   - Logs the detected input language.

5. **Perform the translation:**  The `translate` function from the `Translator` object performs the translation using the provided input and output language codes.

6. **Error handling:** A `try...except` block catches any exceptions during the translation process.  If an error occurs, it logs the error and returns an empty string.

7. **Return the translated text:** The function returns the translated text.

8. **Define the `main` function:**  This function handles user input for the text, input and output languages, and calls the `translate` function.

9. **Print the translated text:** Displays the translated text.


Usage example
-------------------------
.. code-block:: python

    from goog.gtranslater import translate

    # Example usage, translating "Hello, world!" from English to Spanish.
    translated_text = translate("Hello, world!", locale_out="ES")
    print(f"Translated text: {translated_text}")


    # Example usage, translating a paragraph and automatically detecting the input language.
    paragraph = "Bonjour le monde!"
    translated_text = translate(paragraph, locale_out="EN")  # Translate to English.
    print(f"Translated text: {translated_text}")