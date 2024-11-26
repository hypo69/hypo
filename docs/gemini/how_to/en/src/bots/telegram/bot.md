How to use the Telegram bot (hypotez/src/bots/telegram/bot.py)

This guide explains how to use the Telegram bot implemented in the `hypotez/src/bots/telegram/bot.py` file.

**1. Prerequisites:**

*   **Python:** Ensure Python 3.12 is installed.
*   **Telegram Bot API:**  A Telegram bot with a valid token.  You'll need to configure the `gs.credentials.telegram.bot.kazarinov` variable in your application's configuration to the actual token.
*   **Dependencies:**  The necessary libraries (`telegram`, `requests`, etc.) are assumed to be installed. If not, install them using:
    ```bash
    pip install -r requirements.txt  # Assuming you have a requirements.txt file
    ```

**2. Understanding the Code:**

The `TelegramBot` class is the core of the bot.

*   `__init__(self, token: str)`: Initializes the Telegram bot application with the provided token.  Crucially, it registers the message handlers.
*   `register_handlers()`: This method adds command handlers (`/start`, `/help`) and message handlers for text, voice, and document messages.
*   `start()`, `help_command()`: These handle the corresponding commands.
*   `handle_message()`: Processes any text message.
*   `handle_voice()`: Processes voice messages and attempts transcription.  Critically, it downloads the voice message to a temporary file.  The `transcribe_voice()` method is a placeholder that needs to be implemented using a speech-to-text service (e.g., Google Cloud Speech-to-Text).
*   `handle_document()`: Processes documents (e.g., text files) and returns their content.
*   `transcribe_voice(self, file_path: Path) -> str`: This function is a placeholder. You must replace it with your actual speech-to-text implementation.


**3. Key Functionality:**

*   **Command Handling:** The bot responds to `/start` and `/help` commands.
*   **Message Handling:** It can handle text, voice, and document messages.
*   **Voice Message Transcription:** The `handle_voice()` method downloads the voice message, attempts to transcribe it, and sends the transcribed text back to the user.  **IMPORTANT:**  The `transcribe_voice()` function is currently empty.  You MUST fill in this placeholder using a speech recognition API such as Google Cloud Speech-to-Text.
*   **Document Processing:** The `handle_document()` function downloads and extracts the text content from received documents.

**4. Implementing Speech Recognition (Crucial):**

Replace the `transcribe_voice()` method with your implementation using a speech recognition service (e.g., Google Cloud Speech-to-Text, Amazon Transcribe).  This requires authentication with the API and proper handling of the voice file.

**Example of how to use Google Cloud Speech-to-Text (Illustrative):**

```python
from google.cloud import speech
import io

... (other imports)

def transcribe_voice(self, file_path: Path) -> str:
    client = speech.SpeechClient()
    with io.open(file_path, "rb") as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.OGG,
        sample_rate_hertz=44100,  # Adjust to your audio format
        language_code="en-US"  # or your language
    )

    response = client.recognize(config=config, audio=audio)
    for result in response.results:
        alternative = result.alternatives[0]
        return alternative.transcript
    return "No speech recognized."
```


**5. Running the Bot:**

The `main()` function starts the bot.  Ensure your `gs.credentials.telegram.bot.kazarinov` variable is correctly set with your bot token.

```bash
python hypotez/src/bots/telegram/bot.py
```

This will start the bot and listen for incoming messages.


**6. Error Handling:**

The `handle_voice()` method includes error handling to catch potential exceptions during voice message processing.  You should expand this error handling to cover other parts of the bot as necessary.


This guide provides a structured approach to using the Telegram bot.  Remember to adapt the speech-to-text implementation to your specific needs.