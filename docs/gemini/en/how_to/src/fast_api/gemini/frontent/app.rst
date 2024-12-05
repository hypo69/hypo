rst
How to use this code block
=========================================================================================

Description
-------------------------
This JavaScript code, likely using React and ReactDOM, renders a simple chat application. It handles user input, sends it to a server API endpoint (at `http://localhost:8000/api/chat`), receives a response from the API, and displays both the user's message and the AI's response in a chat box.  The code manages the state of the chat messages and input field using React hooks.


Execution steps
-------------------------
1. **Initial state:** The application initializes with an empty input field and an empty message array.


2. **Input handling:** The code listens for user input changes in the input field and stores it in the `input` state variable.


3. **Message submission:** When the user presses Enter or clicks "Send," the `sendMessage` function is triggered.


4. **Validation:**  It checks if the input is empty after trimming whitespace.  If empty, the function returns without further action.


5. **Message creation:** A `userMessage` object is created, containing the user's role and message content. This object is added to the `messages` state array.


6. **API request:**  An asynchronous `fetch` request is made to the `/api/chat` endpoint on the server. The request's body includes the user's input as a `prompt` in JSON format.


7. **Response handling:** The response from the server is parsed as JSON, and the content is extracted. An `aiMessage` object is created, containing the AI's role and the response content.


8. **Message display:** Both the user's and AI's messages are added to the `messages` state array, updating the display on the screen. Error handling is included; if there's a problem during the fetch, an error message is logged to the console.


9. **Input clearing:** The input field is cleared after sending the message.


10. **Rendering:**  The application updates the display by rerendering the chat box with the new message content. The mapping ensures each message is displayed properly.


11. **Rendering the UI:** React renders the chat box UI, displaying the messages chronologically and formatting them based on the role.


Usage example
-------------------------
.. code-block:: javascript

    // This is not executable code in this context,
    // but shows how to include the component.

    import React from 'react';
    import ReactDOM from 'react-dom';
    import App from './App'; // Assuming App.js is your component

    ReactDOM.render(<App />, document.getElementById('chat-app'));

    // Example of a possible backend API response:
    //
    // {
    //   "response": "Hello, how can I help you?"
    // }