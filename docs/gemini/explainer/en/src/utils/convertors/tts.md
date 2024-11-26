## File: hypotez/src/utils/convertors/tts.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils.convertors
	:platform: Windows, Unix
	:synopsis: speech recognition and text-to-speech conversion

"""
MODE = 'dev'

from pathlib import Path
import tempfile
import asyncio
import requests
import speech_recognition as sr  # Библиотека для распознавания речи
from pydub import AudioSegment  # Library for audio conversion
from gtts import gTTS  # Генерация текста в речь

from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger import logger


def speech_recognizer(audio_url: str = None, audio_file_path: Path = None, language: str = 'ru-RU') -> str:
    """ Download an audio file and recognize speech in it.

    Args:
        audio_url (str, optional): URL of the audio file to be downloaded. Defaults to `None`.
        audio_file_path (Path, optional): Local path to an audio file. Defaults to `None`.
        language (str): Language code for recognition (e.g., 'ru-RU'). Defaults to 'ru-RU'.

    Returns:
        str: Recognized text from the audio or an error message.

    Example:
        .. code::

            recognized_text = speech_recognizer(audio_url='https://example.com/audio.ogg')
            print(recognized_text)  # Output: "Привет"
    """
    try:
        if audio_url:
            # Download the audio file
            response = requests.get(audio_url)
            audio_file_path = Path(tempfile.gettempdir()) / 'recognized_audio.ogg'

            with open(audio_file_path, 'wb') as f:
                f.write(response.content)

        # Convert OGG to WAV
        wav_file_path = audio_file_path.with_suffix('.wav')
        audio = AudioSegment.from_file(audio_file_path)  # Load the OGG file
        audio.export(wav_file_path, format='wav')  # Export as WAV

        # Initialize the recognizer
        recognizer = sr.Recognizer()
        with sr.AudioFile(str(wav_file_path)) as source:
            audio_data = recognizer.record(source)
            try:
                # Recognize speech using Google Speech Recognition
                text = recognizer.recognize_google(audio_data, language=language)
                logger.info(f'Recognized text: {text}')
                return text
            except sr.UnknownValueError:
                logger.error('Google Speech Recognition could not understand audio')
                return 'Sorry, I could not understand the audio.'
            except sr.RequestError as ex:
                logger.error('Could not request results from Google Speech Recognition service:', ex)
                return 'Could not request results from the speech recognition service.'
    except Exception as ex:
        logger.error('Error in speech recognizer:', ex)
        return 'Error during speech recognition.'


async def text2speech(text: str, lang: str = 'ru') -> str:
    """ Convert text to speech and save it as an audio file.

    Args:
        text (str): The text to be converted into speech.
        lang (str, optional): Language code for the speech (e.g., 'ru'). Defaults to 'ru'.

    Returns:
        str: Path to the generated audio file.

    Example:
        .. code::

            audio_path = await text2speech('Привет', lang='ru')
            print(audio_path)  # Output: "/tmp/response.mp3"
    """
    try:
        # Generate speech using gTTS
        tts = gTTS(text=text, lang=lang)
        audio_file_path = f'{tempfile.gettempdir()}/response.mp3'
        tts.save(audio_file_path)  # Save the audio file

        # Load and export audio using pydub
        audio = AudioSegment.from_file(audio_file_path, format='mp3')
        wav_file_path = audio_file_path.replace('.mp3', '.wav')
        audio.export(wav_file_path, format='wav')

        logger.info(f'TTS audio saved at: {wav_file_path}')
        return wav_file_path
    except Exception as ex:
        logger.error('Error in text2speech:', ex)
        return 'Error during text-to-speech conversion.'
```

```algorithm
**Speech Recognition:**

1. **Input:** `audio_url` (optional) or `audio_file_path` (optional).
2. **Download (if audio_url):** Download audio from the URL to a temporary file.
3. **Convert to WAV:** Convert the input audio (OGG or other format) to WAV using `pydub`.
4. **Recognize Speech:** Use `speech_recognition` to recognize the speech in the WAV file. This involves:
    * Initializing the recognizer.
    * Reading audio data from the file.
    * Using `recognize_google` (Google Speech Recognition) to convert audio to text. Handles potential errors.
5. **Return:** Return the recognized text or an error message.


**Text-to-Speech:**

1. **Input:** `text` to be converted, optional `lang` parameter.
2. **Generate Speech:** Use `gTTS` to convert the text into speech in the specified language.
3. **Save Audio:** Save the generated audio to a temporary MP3 file.
4. **Convert to WAV:** Convert the generated MP3 to WAV using `pydub` for compatibility.
5. **Return:** Return the path to the generated WAV file or an error message.


**Data Flow between Functions:**

* `speech_recognizer`: Takes audio input (URL or file), downloads and converts it to WAV. Passes the WAV to speech recognition. Returns recognized text.
* `text2speech`: Takes text input. Generates and saves speech to a WAV file in a temporary directory. Returns the path of the generated file.


```

```explanation
**Imports:**

* `pathlib`: Provides Path objects for handling file paths in a more object-oriented and platform-independent way.
* `tempfile`: Used to create temporary files, crucial for handling downloaded audio and temporary results.
* `asyncio`: Enables asynchronous operations; useful for handling background tasks.
* `requests`: Used to download audio files from URLs.
* `speech_recognition`: The core library for speech recognition, using Google Speech Recognition. Note the Russian comment, `Библиотека для распознавания речи`
* `pydub`: Used for audio file manipulation (conversion between formats).
* `gtts`: Used for text-to-speech conversion.
* `src.utils.jjson`:  Likely for JSON handling (loading, dumping). This implies a package for JSON-related utilities.
* `src.logger`: Import for logging, possibly part of a logging system for the project.


**Classes:**

No classes are defined in this code.


**Functions:**

* `speech_recognizer(audio_url=None, audio_file_path=None, language='ru-RU')`: Takes optional audio URL or file path. Downloads audio if URL. Converts to WAV. Initializes `speech_recognition` recognizer, and uses `recognize_google`. Handles errors with `try-except` blocks and logs appropriately. Returns recognized text or error messages.
* `text2speech(text, lang='ru')`: Takes text to be converted and optional language. Uses `gTTS` for text-to-speech conversion. Saves audio to a temporary MP3 file, and then converts it to a WAV file, using `pydub`. Returns path to the WAV file or error message.  Note the use of `async` which makes this function awaitable.


**Variables:**

* `MODE`: A string variable likely for configuration purposes.
* `audio_url`, `audio_file_path`, `language`, `text`, `lang`: Variables used as arguments to functions and for data flow.
* `wav_file_path`, `audio_file_path`, `audio`: Variables for managing intermediate files.


**Potential Errors/Improvements:**

* Error Handling: The `try-except` blocks are good, but consider adding more specific exception types where possible (e.g., `requests.exceptions.RequestException`). This would make debugging easier.
* Language Support: The code handles a default language (`ru-RU` for speech recognition, `ru` for TTS). Add more options for languages and allow users to provide the language string (e.g., `en-US`).
* Input Validation: Implement checks on the audio file type and potentially input parameters (e.g., audio_url is a valid URL).
* Temporary File Management:  The code creates temporary files.  Adding cleanup (removing the temporary files) would be a crucial improvement.  Consider using `with tempfile.NamedTemporaryFile(...)` to automatically manage temporary files.
* Asynchronous Operations (speech_recognizer):  While the `text2speech` function is asynchronous, the `speech_recognizer` function is not. It could be improved if it is anticipated that multiple speech recognition tasks may be running concurrently.



**Relationships with Other Parts of the Project:**

* `src.utils.jjson`: Likely used for interacting with JSON data or for configurations.
* `src.logger`:  Indicates a central logging system for the application, used to track the execution flow and report errors.  The logger would likely be configured and used throughout the Hypotez project. This suggests this file is part of a larger application.