Bot Handlers Parser
===================

.. module:: hypotez.src.endpoints.kazarinov.bot_handlers_parser
    :platform: Windows, Unix
    :synopsis: This module contains classes and functions for handling bot commands.

Module Description
------------------

This module provides bot handlers for processing user input, primarily focusing on extracting data from OneTab URLs to generate price quotes. It integrates with various modules for logging, web driver management, AI interaction, and data processing. The core functionality involves receiving URLs, parsing their content to extract relevant data (price, product name, URLs), validating the data, and then forwarding it to a scenario processing function for the final step of generating the price quote and sending it through WhatsApp.  Error handling and logging are crucial aspects of this module.


Classes
-------

.. autoclass:: BotHandler
    :members:
    :undoc-members:
    :show-inheritance:

Functions
---------

.. autofunction:: BotHandler.handle_url
.. autofunction:: BotHandler.get_data_from_onetab
.. autofunction:: BotHandler.handle_next_command
.. autofunction:: BotHandler.fetch_target_urls_onetab


Module Variables
-----------------

.. autodata:: MODE