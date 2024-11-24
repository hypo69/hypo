grab_lilnks_to_chats.py
=======================

.. module:: hypotez.src.suppliers.chat_gpt.scenarios.grab_lilnks_to_chats
    :platform: Windows, Unix
    :synopsis: This module contains functions for grabbing links to chats.


Module Description
------------------

This module provides a function for extracting links to individual chat conversations. It utilizes a pre-defined locator from a JSON file to locate and retrieve these links. The function also demonstrates usage within a `if __name__ == \'__main__\':` block, showcasing how to instantiate a WebDriver (in this case, Firefox) and use the `get_links` function to retrieve the chat links.


Functions
---------

.. autofunction:: hypotez.src.suppliers.chat_gpt.scenarios.grab_lilnks_to_chats.get_links