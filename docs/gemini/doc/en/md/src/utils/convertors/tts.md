# hypotez/src/utils/convertors/tts.py

## Overview

This module provides functions for speech recognition (converting audio to text) and text-to-speech (converting text to audio) using various libraries. It includes error handling and logging for robust operation.

## Table of Contents

* [speech_recognizer](#speech_recognizer)
* [text2speech](#text2speech)


## Functions

### `speech_recognizer`

**Description**: Downloads an audio file (if provided by URL) or uses the specified file, converts it to WAV format, and then uses Google Speech Recognition to transcribe the audio.

**Parameters**:

* `audio_url` (str, optional): URL of the audio file to be downloaded. Defaults to `None`.
* `audio_file_path` (Path, optional): Local path to an audio file. Defaults to `None`.
* `language` (str): Language code for recognition (e.g., 'ru-RU'). Defaults to 'ru-RU'.


**Returns**:

* `str`: Recognized text from the audio or an error message.


**Raises**:

* `Exception`: Any other error during download, conversion, or recognition.


### `text2speech`

**Description**: Converts the input text to speech using gTTS and saves the audio as a WAV file in a temporary directory.

**Parameters**:

* `text` (str): The text to be converted into speech.
* `lang` (str, optional): Language code for the speech (e.g., 'ru'). Defaults to 'ru'.


**Returns**:

* `str`: Path to the generated audio file.


**Raises**:

* `Exception`: Any error during text-to-speech conversion, file saving, or conversion to WAV format.