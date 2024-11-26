How to use the `gtranslater` module

This module provides a function for translating text using the Google Translate API.  It handles automatic language detection for the input text if you don't specify the input language.

**Core Function: `translate`**

```python
from googletrans import Translator
from langdetect import detect
from src.logger import logger

def translate(text: str, locale_in: str = None, locale_out: str = 'EN') -> str:
```

The `translate` function takes three arguments:

*   `text`: The text to be translated (string).  **Required.**
*   `locale_in`: The input language code (e.g., 'es', 'fr').  **Optional**. If not provided, the input language is automatically detected.
*   `locale_out`: The output language code (e.g., 'en'). **Optional**, defaults to 'EN' (English).


**Example Usage:**

```python
translated_text = translate("Hola, mundo!", locale_out='fr')
print(translated_text)  # Output: Bonjour, monde!
```

In this example, the input text "Hola, mundo!" is translated to French.  Since the input language is not specified, it is automatically detected as Spanish.


```python
translated_text = translate("Guten Tag", locale_in='de', locale_out='es')
print(translated_text) #Output: Hola
```

In this example, the input language is explicitly specified as German, and the output is Spanish.


**Handling Automatic Language Detection:**

If you omit the `locale_in` parameter, the function automatically detects the input language using the `langdetect` library.

```python
translated_text = translate("你好，世界！")
print(translated_text)  # Output:  Hello, world!
```

**Error Handling:**

The `translate` function includes a `try...except` block to catch potential errors during the translation process.  If an error occurs, it logs the error using the `src.logger` module and returns an empty string.  This helps prevent the script from crashing.

**`main` function:**


```python
def main():
    text = input("Enter the text to be translated: ")
    locale_in = input("Enter the source language code (leave blank for auto-detect): ")
    locale_out = input("Enter the target language code: ")

    translated_text = translate(text, locale_in, locale_out)
    print(f"Translated text: {translated_text}")
```

The `main` function provides a simple user interface for testing the translation functionality. It prompts the user for the input text, source language (optional), and target language and then prints the translated result.  This function is called if the script is run directly.

**How to run the code**

Save the code as `gtranslater.py`.  Make sure you have the necessary libraries (`googletrans`, `langdetect`, and `src.logger`) installed.  Install them using pip:

```bash
pip install googletrans==4.0.0-rc1 langdetect
```
(Ensure you have the correct `src.logger` module defined and accessible in your project.)

Run the script from your terminal:

```bash
python gtranslater.py
```

This will prompt you to enter the text and language codes.


**Important Considerations:**

* **Error Handling:** The `try...except` block is crucial to prevent unexpected crashes.
* **Language Codes:** Use valid ISO 639-1 language codes (e.g., 'en', 'es', 'fr').
* **Libraries:** Ensure that the required libraries (`googletrans`, `langdetect`, and `src.logger`) are installed and accessible.
* **`src.logger`:** The code relies on a `src.logger` module. You need to define this logger in your project for proper error reporting.


This comprehensive guide should help you understand and effectively use the `gtranslater` module. Remember to replace `"src.logger"` with the actual import path if your logger is in a different location.