rst
How to use the Google Text-to-Speech Module
=========================================================================================

Description
-------------------------
This Python module (`hypotez/src/goog/text_to_speech/__init__.py`) provides a class (`TTS`) for utilizing the Google Text-to-Speech API (`gtts`) and the `pyttsx3` library for voice configuration.  The module initializes a `pyttsx3` engine and prints details of available voices.  Crucially, it establishes a `TTS` object, storing it as `_tts` for later use.

Execution steps
-------------------------
1. The module imports necessary libraries: `pyttsx3` for voice control and `gtts` for the Google Text-to-Speech API.  A custom header file (`header`) is also imported.
2. A `MODE` variable is set to 'dev'. This is likely for development configuration.
3. A `TTS` class is defined to encapsulate the TTS functionality.
4. The `__init__` method of the `TTS` class initializes a `pyttsx3` engine.
5. The `__init__` method retrieves and prints the available voices from the `pyttsx3` engine.
6. The module then creates an instance of the `TTS` class, storing it in the `_tts` variable.

Usage example
-------------------------
.. code-block:: python

    from hypotez.src.goog.text_to_speech import TTS

    # Access the initialized TTS object
    tts_instance = TTS()

    # This line is crucial.  Example usage will follow
    # Note that currently, the code only prints available voices and doesn't perform any text-to-speech conversion.