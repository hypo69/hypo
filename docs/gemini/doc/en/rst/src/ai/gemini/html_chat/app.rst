hypotez/src/ai/gemini/html_chat/app.py
=========================================

.. module:: hypotez.src.ai.gemini.html_chat.app
   :platform: Windows, Unix
   :synopsis: This module provides a web-based chat application using FastAPI, interacting with the Kazarinov model.


Module Contents
---------------

This module contains the FastAPI application for a chat interface. It handles user input, interacts with the Kazarinov model for responses, and dynamically displays the conversation in an HTML template.  The module initializes the FastAPI app, configures templates and static files paths, and integrates with the Kazarinov model for generating responses.  It also includes functionality for loading a list of chat prompts from a file, providing a random question option, and opening the web application in a browser.

Classes
-------

.. autoclass:: FastAPI
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: Jinja2Templates
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: StaticFiles
   :members:
   :undoc-members:
   :show-inheritance:


.. autoclass:: BaseModel
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: Question
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autofunction:: open_browser
   :noindex:

.. autofunction:: get_chat
   :noindex:

.. autofunction:: ask_question
   :noindex:


Dependencies
------------

.. automodule:: header
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: webbrowser
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: threading
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: fastapi.templating
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: fastapi.staticfiles
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: pydantic
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: src.ai.gooogle_generativeai.kazarinov
   :members:
   :undoc-members:
   :show-inheritance:


.. automodule:: random
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: pathlib
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: src.gs
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: uvicorn
   :members:
   :undoc-members:
   :show-inheritance:



Global Variables
----------------
.. autovariable:: MODE
   :noindex: