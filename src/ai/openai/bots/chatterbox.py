## \file ../src/ai/openai/bots/chatterbox.py
from pathlib import Path
import tempfile
import asyncio
import header
from src.utils import j_loads, j_loads_ns, j_dumps
from src.logger import logger
import speech_recognition as sr  # Библиотека для распознавания речи
import requests  # Для скачивания файлов
from pydub import AudioSegment  # Библиотека для конвертации аудио
from gtts import gTTS  # Библиотека для текстового воспроизведения

def recognizer(audio_url: str = None, audio_file_path:Path = None, language: str = 'ru-RU') -> str:
    """Download an audio file and recognize speech in it."""
    if audio_url:  
    # Download audio file
        response = requests.get(audio_url)
        audio_file_path = Path(tempfile.gettempdir()) / "recognized_audio.ogg"

        with open(audio_file_path, 'wb') as f:
            f.write(response.content)

    # Convert OGG to WAV
    wav_file_path = audio_file_path.with_suffix('.wav')
    audio = AudioSegment.from_ogg(audio_file_path)  # Load OGG file
    audio.export(wav_file_path, format='wav')  # Export as WAV

    # Initialize recognizer
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
        
async def text_to_speech(text:str, lang:str='ru'):
    """Convert text to speech and play it in a voice channel."""
    tts = gTTS(text=text, lang='ru')  # Замените 'ru' на нужный язык
    audio_file_path = f"{tempfile.gettempdir()}/response.mp3"  # Путь к временно созданному файлу
    tts.save(audio_file_path)  # Сохраняем аудиофайл
    return audio_file_path