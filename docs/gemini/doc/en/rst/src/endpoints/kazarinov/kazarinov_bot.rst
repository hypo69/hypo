KazarinovTelegramBot Module
===========================

.. module:: hypotez.src.endpoints.kazarinov.kazarinov_bot
   :platform: Windows, Unix
   :synopsis: KazarinovTelegramBot

Description:
This module implements a Telegram bot for the Kazarinov project, supporting various command and message handling scenarios. The bot interacts with the Mexiron parser and the Google Generative AI model, and supports handling of text messages, documents, and URLs.

Key Features:
1. Initialization and configuration of the Telegram bot based on a configuration JSON file.
2. Registration of commands and message handlers.
3. Routing of text messages based on URLs, with the ability to handle links to OneTab and suppliers.
4. Use of the Mexiron object to parse product data from suppliers and generate price lists.
5. Generating responses to messages through Google Generative AI.
6. Logging of user messages and their subsequent processing.

Functions
---------

.. autofunction:: hypotez.src.endpoints.kazarinov.kazarinov_bot.KazarinovTelegramBot
.. autofunction:: hypotez.src.endpoints.kazarinov.kazarinov_bot.KazarinovTelegramBot.__init__
.. autofunction:: hypotez.src.endpoints.kazarinov.kazarinov_bot.KazarinovTelegramBot.handle_message

Classes
-------

.. autoclass:: hypotez.src.endpoints.kazarinov.kazarinov_bot.KazarinovTelegramBot
   :members:
   :undoc-members:
   :show-inheritance: