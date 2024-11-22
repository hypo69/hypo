```rst
hypo69 Small Talk Bot
=======================

.. automodule:: hypotez.src.endpoints.hypo69.small_talk_bot.bot
    :members:
    :undoc-members:
    :show-inheritance:

Bot Configuration
-----------------

* **MODE**:  `development`

Classes
-------

.. autoclass:: hypotez.src.endpoints.hypo69.small_talk_bot.bot.PsychologistTelgrambot
    :members:
    :undoc-members:
    :show-inheritance:
    :special-members: __init__

Functions
---------

.. autofunction:: hypotez.src.endpoints.hypo69.small_talk_bot.bot.PsychologistTelgrambot.__post_init__
.. autofunction:: hypotez.src.endpoints.hypo69.small_talk_bot.bot.PsychologistTelgrambot.register_handlers
.. autofunction:: hypotez.src.endpoints.hypo69.small_talk_bot.bot.PsychologistTelgrambot.start
.. autofunction:: hypotez.src.endpoints.hypo69.small_talk_bot.bot.PsychologistTelgrambot.handle_message
.. autofunction:: hypotez.src.endpoints.hypo69.small_talk_bot.bot.PsychologistTelgrambot.get_handler_for_url
.. autofunction:: hypotez.src.endpoints.hypo69.small_talk_bot.bot.PsychologistTelgrambot.handle_suppliers_response
.. autofunction:: hypotez.src.endpoints.hypo69.small_talk_bot.bot.PsychologistTelgrambot.handle_onetab_response
.. autofunction:: hypotez.src.endpoints.hypo69.small_talk_bot.bot.PsychologistTelgrambot.handle_next_command
.. autofunction:: hypotez.src.endpoints.hypo69.small_talk_bot.bot.PsychologistTelgrambot.handle_document


Module Details
--------------

This module defines a custom Telegram bot for psychological support, `PsychologistTelgrambot`.  It leverages the `GoogleGenerativeAI` model for generating responses based on user input and utilizes a dedicated file structure for prompts and training data. The bot also features URL-based routing and document handling capabilities.  The `__post_init__` method is crucial for initializing the bot's dependencies, such as setting up the API key and loading prompts from file.

.. note::

   The bot's functionality relies on external libraries like `telegram`, `asyncio`, and the `google-generative-ai` Python package.  Ensure these dependencies are installed before running.
```
