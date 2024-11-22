```rst
Generative AI Module
=====================

This module provides an interface for interacting with Google's Generative AI models,
specifically Gemini. It allows for question-answering, image description, and
dialogue logging.  The module includes handling for API keys, model selection,
and dialogue history management, including both text and JSON formats for
persistence.

.. toctree::
   :maxdepth: 2
   :caption: Modules

   ../logger
   ../utils/file
   ../utils/date_time
   ../utils/jjson
   ../gs

.. automodule:: hypotez.src.ai.gemini.generative_ai
    :members:
    :undoc-members:
    :show-inheritance:

Functions
--------

.. autofunction:: hypotez.src.ai.gemini.generative_ai.chat
.. autofunction:: hypotez.src.ai.gemini.generative_ai.GoogleGenerativeAI.__init__
.. autofunction:: hypotez.src.ai.gemini.generative_ai.GoogleGenerativeAI.__post_init__
.. autofunction:: hypotez.src.ai.gemini.generative_ai.GoogleGenerativeAI._save_dialogue
.. autofunction:: hypotez.src.ai.gemini.generative_ai.GoogleGenerativeAI.ask
.. autofunction:: hypotez.src.ai.gemini.generative_ai.GoogleGenerativeAI.describe_image


Class Documentation
-------------------

.. autoclass:: hypotez.src.ai.gemini.generative_ai.GoogleGenerativeAI
    :members:
    :undoc-members:
    :show-inheritance:

```
