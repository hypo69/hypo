App Component
============

This file defines the `App` component for a chat application using React.  It handles user input, sends messages to a backend API, and displays the conversation history.

.. autofunction:: App
   :members:
   :undoc-members:
   :show-inheritance:

Functions
--------

.. autofunction:: App.sendMessage
   :members:
   :undoc-members:
   :show-inheritance:

Explanation
----------

This component utilizes React to create a chat interface.  The `App` component manages the state of user input, messages, and the conversation history.  The `sendMessage` function handles the process of sending user input to the backend API (`http://localhost:8000/api/chat`) and updating the displayed conversation.