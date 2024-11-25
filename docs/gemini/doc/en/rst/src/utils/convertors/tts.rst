TTS Conversion Utilities
=========================

.. module:: hypotez.src.utils.convertors.tts
   :platform: Windows, Unix
   :synopsis: speech recognition and text-to-speech conversion


This module provides functions for speech recognition from audio and text-to-speech conversion.


Speech Recognition
------------------

.. autofunction:: hypotez.src.utils.convertors.tts.speech_recognizer
   :noindex:

   :param audio_url: URL of the audio file.
   :type audio_url: str
   :param audio_file_path: Path to the local audio file.
   :type audio_file_path: pathlib.Path
   :param language: Language code for speech recognition (e.g., 'ru-RU').
   :type language: str
   :returns: Recognized text or an error message.
   :rtype: str
   :raises requests.exceptions.RequestException: An error occurred during the request.
   :raises speech_recognition.UnknownValueError: Google Speech Recognition could not understand the audio.
   :raises speech_recognition.RequestError: Could not request results from the Google Speech Recognition service.
   :raises Exception: A general error occurred during speech recognition.


Text-to-Speech Conversion
------------------------

.. autofunction:: hypotez.src.utils.convertors.tts.text2speech
   :noindex:

   :param text: The text to convert to speech.
   :type text: str
   :param lang: Language code for the speech (e.g., 'ru').
   :type lang: str
   :returns: Path to the generated audio file.
   :rtype: str
   :raises Exception: A general error occurred during text-to-speech conversion.