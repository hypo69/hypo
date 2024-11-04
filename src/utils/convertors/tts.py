## \file src/utils/convertors/tts.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! Module for speech recognition and text-to-speech conversion. """

import header
from pathlib import Path
import tempfile
import asyncio
import speech_recognition as sr  # Библиотека для распознавания речи
from pydub import AudioSegment  # Library for audio conversion
from gtts import gTTS  # Библиотека для текстового воспроизведения

from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger import logger



def speech_recognizer(audio_url: str = None, audio_file_path: Path = None, language: str = 'ru-RU') -> str:
    """! Download an audio file and recognize speech in it.

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
    if audio_url:
        # Download the audio file
        response = requests.get(audio_url)
        audio_file_path = Path(tempfile.gettempdir()) / "recognized_audio.ogg"

        with open(audio_file_path, 'wb') as f:
            f.write(response.content)

    # Convert OGG to WAV
    wav_file_path = audio_file_path.with_suffix('.wav')
    audio = AudioSegment.from_ogg(audio_file_path)  # Load the OGG file
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
            logger.error("Google Speech Recognition could not understand audio")
            return "Sorry, I could not understand the audio."
        except sr.RequestError as e:
            logger.error(f"Could not request results from Google Speech Recognition service; {e}")
            return "Could not request results from the speech recognition service."

async def text2speech(text: str, lang: str = 'ru') -> str:
    """! Convert text to speech and save it as an audio file.

    Args:
        text (str): The text to be converted into speech.
        lang (str, optional): Language code for the speech (e.g., 'ru'). Defaults to 'ru'.

    Returns:
        str: Path to the generated audio file.

    Example:
        .. code::

            audio_path = await text_to_speech("Привет", lang='ru')
            print(audio_path)  # Output: "/tmp/response.mp3"
    """
    tts = gTTS(text=text, lang=lang)  # Replace 'ru' with the desired language code
    audio_file_path = f"{tempfile.gettempdir()}/response.mp3"  # Path to the temporary file
    tts.save(audio_file_path)  # Save the audio file
    return audio_file_path
