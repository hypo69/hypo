# Usage Guide for `hypotez/src/utils/convertors/tts.py`

This module provides functions for speech recognition and text-to-speech conversion. It leverages libraries like `speech_recognition`, `pydub`, and `gtts`.

## Speech Recognition (`speech_recognizer`)

This function takes an audio file (either a URL or a local path) and returns the recognized text.

**Function Signature:**

```python
def speech_recognizer(audio_url: str = None, audio_file_path: Path = None, language: str = 'ru-RU') -> str:
```

**Parameters:**

*   `audio_url` (str, optional): The URL of the audio file.  If provided, the function downloads the audio. Defaults to `None`.
*   `audio_file_path` (Path, optional):  The local path to the audio file.  If provided, the function uses the file directly. Defaults to `None`.
*   `language` (str): The language code for speech recognition (e.g., 'ru-RU', 'en-US'). Defaults to `'ru-RU'`.

**Returns:**

*   str: The recognized text if successful, or an error message string.

**Error Handling:**

The function includes robust error handling using `try...except` blocks to catch potential issues during audio download, conversion, or speech recognition.  It logs errors with detailed messages, which is crucial for debugging.

**Example Usage:**

```python
import asyncio
from pathlib import Path
from hypotez.src.utils.convertors import tts

# Using a URL
recognized_text = tts.speech_recognizer(audio_url='https://example.com/audio.ogg')
print(recognized_text)

# Using a local file
audio_file = Path('path/to/your/audio.ogg')
recognized_text = tts.speech_recognizer(audio_file_path=audio_file)
print(recognized_text)

```


## Text-to-Speech (`text2speech`)

This function converts text to speech and saves the audio to a WAV file in a temporary directory.

**Function Signature:**

```python
async def text2speech(text: str, lang: str = 'ru') -> str:
```

**Parameters:**

*   `text` (str): The text to convert to speech.
*   `lang` (str, optional): The language code for the speech (e.g., 'ru', 'en'). Defaults to `'ru'`.


**Returns:**

*   str: The path to the generated WAV audio file in the temporary directory.  Returns an error message string on failure.

**Asyncronicity:**

This function is `async` for better responsiveness and to avoid blocking the main thread.  Use `asyncio` to call this function.

**Example Usage:**

```python
import asyncio
from hypotez.src.utils.convertors import tts

async def main():
    text_to_convert = "Hello, world!"
    audio_path = await tts.text2speech(text_to_convert)
    print(audio_path)

asyncio.run(main())
```

**Important Notes:**

*   Install necessary libraries: `pip install speech_recognition pydub gtts requests`
*   Ensure the correct language codes are used for both speech recognition and text-to-speech conversion.
*   The generated audio file is saved to a temporary directory.


## Troubleshooting

If you encounter errors, check the error messages logged by the `logger`. The error messages provide valuable context for debugging. Ensure that the audio file format and the provided language codes are correct. Also, ensure the necessary libraries are installed.