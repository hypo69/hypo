## File hypotez/src/endpoints/hypo69/psychologist_bot/bot.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe\n#! venv/bin/python/python3.12\n\n"""\n.. module: src.endpoints.hypo69.psychologist_bot \n\t:platform: Windows, Unix\n\t:synopsis:\n\n"""\nMODE = \'dev\'\n\n"""\n\t:platform: Windows, Unix\n\t:synopsis:\n\n"""\n\n"""\n\t:platform: Windows, Unix\n\t:synopsis:\n\n"""\n\n"""\n  :platform: Windows, Unix\n\n"""\n"""\n  :platform: Windows, Unix\n  :platform: Windows, Unix\n  :synopsis:\n"""MODE = \'dev\'\n  \n""" module: src.endpoints.hypo69.psychologist_bot """\n\n\n...\n""" t.me/hypo69_psychologist_bot_bot\'s specific bot with customized behavior."""\n\nimport asyncio\nfrom pathlib import Path\nfrom typing import Optional\nfrom dataclasses import dataclass, field\nimport random\nfrom telegram import Update\nfrom telegram.ext import CommandHandler, MessageHandler, filters, CallbackContext\n\nfrom src import gs\nfrom src.bots.telegram import TelegramBot\nfrom src.webdriver import Driver, Chrome\nfrom src.ai.gemini import GoogleGenerativeAI\nfrom src.utils.file import read_text_file, recursively_read_text_files, save_text_file\nfrom src.utils.url import is_url\nfrom src.logger import logger\n\n@dataclass\nclass PsychologistTelgrambot(TelegramBot):\n    """Telegram bot with custom behavior for Kazarinov."""\n\n    token: str = field(init=False)\n    d: Driver = field(init=False)\n    model: GoogleGenerativeAI = field(init=False)\n    system_instruction: str = field(init=False)\n    questions_list: list = field(init=False)\n    timestamp: str = field(default_factory=lambda: gs.now)\n\n    def __post_init__(self):\n        mode = \'test\'\n        #self.token = gs.credentials.telegram.hypo69_test_bot if mode == \'test\' else gs.credentials.telegram.hypo69_psychologist_bot\n        self.token = gs.credentials.telegram.hypo69_psychologist_bot\n        super().__init__(self.token)\n\n        self.d = Driver(Chrome)\n        \n        self.system_instruction = read_text_file(\n            gs.path.google_drive / \'hypo69_psychologist_bot\' / \'prompts\' / \'chat_system_instruction.txt\'\n        )\n        self.questions_list = recursively_read_text_files(\n            gs.path.google_drive / \'hypo69_psychologist_bot\' / \'prompts\' / \'train_data\' / \'q\', [\'*.*\'], as_list=True\n        )\n\n        self.model = GoogleGenerativeAI(\n            api_key=gs.credentials.gemini.hypo69_psychologist_bot,\n            system_instruction=self.system_instruction,\n            generation_config={"response_mime_type": "text/plain"}\n        )\n        \n        self.register_handlers()\n\n    def register_handlers(self):\n        """Register bot commands and message handlers."""\n        self.application.add_handler(CommandHandler(\'start\', self.start))\n        self.application.add_handler(CommandHandler(\'help\', self.help_command))\n        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))\n        self.application.add_handler(MessageHandler(filters.VOICE, self.handle_voice))\n        self.application.add_handler(MessageHandler(filters.Document.ALL, self.handle_document))\n\n    # ... (rest of the code)
```

```
<algorithm>
```
**Step 1: Initialization**

*   The `PsychologistTelgrambot` class is initialized.
*   The bot token, `Driver` object, `GoogleGenerativeAI` model, `system_instruction`, and `questions_list` are loaded.
*   File paths for loading data are dynamically constructed using `gs.path.google_drive`.
*   `TelegramBot`'s initialization is called.

**Example:** 
If `gs.path.google_drive` points to `/tmp/google_drive`, loading the `system_instruction` might involve reading `/tmp/google_drive/hypo69_psychologist_bot/prompts/chat_system_instruction.txt`.


**Step 2: Handling Telegram Events**

*   `register_handlers` is called to set up handlers for different Telegram events.
*   Handlers are registered for `/start`, `/help`, text messages, voice messages, and document uploads.


**Step 3: Handling `/start` Command**

*   The `start` function responds to `/start` with a greeting.
*   It also calls the parent `TelegramBot`'s `start` method.

**Example:**  The bot sends a message like "Hi! I am a smart assistant psychologist."


**Step 4: Handling Text Messages**

*   The `handle_message` function parses the received text message.
*   It logs the user's message to a file using `save_text_file` (in a dynamically generated file path)
*   It uses the `model` to generate a response based on the message and a history file.
*   The generated response is sent back to the user.


**Step 5: URL Routing**

*   The `get_handler_for_url` function maps URLs to specific response handlers (`handle_suppliers_response`, `handle_onetab_response`).
*   If a URL is recognized, the appropriate handler is called.
*   Handlers use `mexiron.run_scenario` to determine if the action was successful and reply accordingly (Success/Error).


**Step 6: Handling  `--next` Command**

*   The `handle_next_command` function picks a random question from `questions_list` and asks the model for an answer.
*   Both the question and the answer are sent to the user.


**Step 7: Handling Document Uploads**

*   The `handle_document` function calls the parent `TelegramBot`'s handling method to handle document uploads and then sends a confirmation message to the user.

**Step 8: Running the Bot**

*   The `if __name__ == "__main__":` block creates a `PsychologistTelgrambot` instance and starts the bot using `asyncio.run(kt.application.run_polling())`.

```
<explanation>

**Imports:**

*   `asyncio`: For asynchronous operations in the bot.
*   `pathlib`: For working with file paths.
*   `typing`: For type hinting.
*   `dataclasses`: For creating data classes (like `PsychologistTelgrambot`).
*   `random`: For selecting random questions.
*   `telegram`: For interacting with the Telegram API.
*   `telegram.ext`: For handling Telegram commands and messages.
*   `src.gs`: Likely a custom module for accessing global configuration/credentials.
*   `src.bots.telegram`: Contains the base class for Telegram bots.
*   `src.webdriver`: Contains classes related to web drivers (likely for automating tasks).
*   `src.ai.gemini`: For using the Gemini AI model.
*   `src.utils.file`: Provides functions for file reading/writing.
*   `src.utils.url`: Contains functions for checking URLs.
*   `src.logger`: For logging.

**Classes:**

*   `PsychologistTelgrambot(TelegramBot)`: Inherits from the base `TelegramBot` class to handle Telegram interactions.
    *   `token`, `d`, `model`, `system_instruction`, `questions_list`, `timestamp`: Attributes to store crucial data and configurations for the bot.  These are initialized in the `__post_init__` method.
    *   `__post_init__`: Initializes bot-specific attributes, overrides the token with a specific bot token, initializes the WebDriver object, and loads system instruction, questions, and the AI model.
    *   `register_handlers`: Registers handlers for Telegram commands and messages.
    *   `start`, `handle_message`, `handle_next_command`, `handle_document`, `handle_suppliers_response`, `handle_onetab_response`:  Methods that respond to specific commands, messages, and other interactions from Telegram users.

**Functions:**

*   `start`: Responds to `/start` command.
*   `handle_message`: Handles text messages, logs them, asks the AI model for a response, and sends it back.
*   `get_handler_for_url`: Maps URLs to specific handlers (`handle_suppliers_response`, `handle_onetab_response`).  This allows for different responses based on the incoming URL.
*   `handle_suppliers_response`: Handles URLs related to suppliers, likely using external functions (`mexiron`).
*   `handle_onetab_response`: Handles URLs related to OneTab, likely using external functions (`mexiron`).
*   `handle_next_command`: Retrieves a random question from the question list and prompts the model for a response.
*   `handle_document`: Handles document uploads.

**Potential Errors/Improvements:**

*   **`mexiron` dependency:** The code relies on a `mexiron` module for handling URLs and scenarios. This module is not defined within the provided code, so there might be a dependency problem, or its functionality might need to be clearly defined and documented.

*   **Missing error handling:** While `handle_next_command` has a `try-except` block, other functions might lack such error handling for critical operations like file reading, API calls, or interactions with `mexiron`.

*   **`mode` variable:**  The `mode = 'test'` variable is used, but never used to distinguish between test and production. The commented-out lines show this was meant to change the token based on the mode, but should be used consistently.

*   **`handle_onetab_response`:** Missing `price`, `mexiron_name`, `urls` parameters for the `run_scenario` call.  This function is incomplete.

*   **Logging:** While `logger` is used, the code benefits from more structured logging for different event types and error details.  Consider adding logging levels and descriptive log messages.

*   **Security:**  Avoid hardcoding API keys directly into the code.  Consider using environment variables or a secure configuration system to manage sensitive information.

**Chain of Relationships:**

*   `PsychologistTelgrambot` relies on the `TelegramBot` class for basic Telegram functionality.
*   `PsychologistTelgrambot` uses `GoogleGenerativeAI` for generating responses based on user input.
*   `PsychologistTelgrambot` uses `Driver` and `Chrome` (likely from `webdriver`) for web automation tasks if needed.
*   Functions within `PsychologistTelgrambot` use utilities provided by `src.utils.file`, `src.utils.url`, and potentially other utilities within `src`.  The `src` directory structure likely defines a modular application architecture.