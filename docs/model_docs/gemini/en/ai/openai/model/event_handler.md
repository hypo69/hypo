```rst
Module event_handler
====================

.. module:: hypotez.src.ai.openai.model.event_handler
    :platform: Windows, Unix
    :synopsis:  Handles events for OpenAI assistant responses.


Description
-----------

This module defines an `EventHandler` class to handle events from OpenAI's assistant responses in a streaming fashion. It utilizes the `openai` Python library's `AssistantEventHandler` for event handling.  The handler allows for output of assistant generated text, tool calls, and code interpreter outputs, all in a streaming manner.


Classes
-------

.. autoclass:: hypotez.src.ai.openai.model.event_handler.EventHandler
    :members:
    :undoc-members:
    :show-inheritance:


Functions
---------

(No functions in this file)


Methods
-------

.. automethod:: hypotez.src.ai.openai.model.event_handler.EventHandler.on_text_created
.. automethod:: hypotez.src.ai.openai.model.event_handler.EventHandler.on_text_delta
.. automethod:: hypotez.src.ai.openai.model.event_handler.EventHandler.on_tool_call_created
.. automethod:: hypotez.src.ai.openai.model.event_handler.EventHandler.on_tool_call_delta
```
