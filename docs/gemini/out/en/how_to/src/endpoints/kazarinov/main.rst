rst
How to use the Kazarinov Telegram Bot CLI
=========================================================================================

Description
-------------------------
This Python script (`hypotez/src/endpoints/kazarinov/main.py`) provides a command-line interface (CLI) for running the Kazarinov Telegram bot.  It allows launching the bot in different modes (test or production) and optionally loads settings from a JSON configuration file.  The script parses command-line arguments, loads settings, instantiates the bot object, and then starts the bot's asynchronous polling loop. Error handling is included for graceful failure during execution.

Execution steps
-------------------------
1. **Import necessary libraries:** The script imports libraries like `argparse`, `asyncio`, `json`, `pathlib`, `pydantic`, the custom `logger` module, and the `KazarinovTelegramBot` class.

2. **Define `parse_args()` function:** This function creates an `argparse` parser to define command-line arguments.  It allows users to specify a JSON settings file (`--settings`) and the bot's mode (`--mode`).  The function parses these arguments and returns a dictionary containing the values.

3. **Define `main()` function:** The `main` function is the entry point of the program.  It first prints a startup message.

4. **Check for and load settings file (if provided):** If the `--settings` argument is provided, the script attempts to load settings from the specified JSON file.  It verifies the file's existence and handles potential errors during file reading. Importantly, it merges the command-line mode (`--mode`) with the settings.

5. **Instantiate KazarinovTelegramBot:** If a settings file was not provided, the bot is created using default or command-line mode. Otherwise, the loaded settings are used to initialize the `KazarinovTelegramBot` object.

6. **Run bot's asynchronous loop:** The script calls `asyncio.run(bot.application.run_polling())` to start the bot's asynchronous event loop, which polls for incoming updates and processes them.

7. **Error Handling:** A `try...except` block catches potential exceptions during the bot's operation, logging any errors to the custom `logger` module.

8. **Run the script:** The `if __name__ == "__main__":` block ensures that the `main()` function is only executed when the script is run directly.


Usage example
-------------------------
.. code-block:: bash

    # Run the bot with default settings (test mode):
    python main.py

    # Run the bot using a configuration file:
    python main.py --settings bot_settings.json

    # Run the bot in production mode:
    python main.py --mode prod --settings bot_settings.json

.. code-block:: json
    # Example bot_settings.json file:
    {
        "api_token": "YOUR_TELEGRAM_BOT_TOKEN",
        "chat_id": 123456789,
        "mode": "prod"
    }