rst
How to use this code block
=========================================================================================

Description
-------------------------
This code defines a Telegram bot using the Telegraf library.  It handles incoming voice and text messages.  For voice messages, it converts the voice file to an MP3, transcribes it using OpenAI's API, sends the transcription to OpenAI's chat model for a response, and then sends that response back to the user.  For text messages, it calls a `processTextToChat` function (which is not defined in the provided code) to process the input and send a response. It also includes error handling for both message types.


Execution steps
-------------------------
1. **Import necessary modules:** The code imports libraries like `Telegraf`, `filters`, `format`, `config`, `ogg`, `openai`, and `utils`. These libraries provide functionalities for Telegram bot creation, message handling, formatting, configuration, audio processing, OpenAI integration, and file management, respectively.

2. **Initialize the bot:** It creates a Telegraf bot instance using the Telegram API token retrieved from the `config` file.

3. **Define bot commands:** A command (`/start`) is defined to respond to the `/start` command by sending the message object back to the user as JSON.

4. **Handle voice messages:**
    - The code checks for incoming voice messages.
    - It sends a confirmation message to the user.
    - It retrieves the voice file's download link.
    - It extracts the user ID.
    - It converts the voice file to OGG format and then to MP3.
    - It removes the temporary OGG file.
    - It uses the OpenAI API to transcribe the MP3 file to text.
    - It sends the transcription as a formatted message.
    - It sends a message to OpenAI's chat model with the transcription as user input and waits for the response.
    - It sends the received OpenAI response back to the user.
    - Includes error handling to catch and log potential errors during the process.

5. **Handle text messages:**
    - It checks for incoming text messages.
    - It sends a confirmation message to the user.
    - It calls the `processTextToChat` function to process the text message.
    - Includes error handling to catch and log potential errors during the process.


6. **Launch the bot:** The `bot.launch()` method starts the Telegram bot and listens for incoming messages.

7. **Handle termination signals:** The `process.once` handlers ensure the bot gracefully stops when receiving SIGINT (Ctrl+C) or SIGTERM signals.


Usage example
-------------------------
.. code-block:: javascript
    
    // Example usage (requires setup of config file with TELEGRAM_TOKEN)
    // ... (import necessary modules)
    
    const bot = new Telegraf(process.env.TELEGRAM_TOKEN); // Use environment variables or config file for security
    
    bot.command('start', async (ctx) => {
        //Handle /start command as shown in the example.
    });

    bot.on('voice', async (ctx) => {
        // Handle voice message as shown in the example
        // ... (add your voice message processing)
    });

    bot.on('text', async (ctx) => {
        // Handle text message as shown in the example
        // ... (add your text message processing, including the call to processTextToChat)
    });

    bot.launch();
    // Add error handling and termination signal handling as shown in the example.