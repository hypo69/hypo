# app.js Documentation

## Overview

This JavaScript file defines a React component (`App`) for a simple chat application. It allows users to input messages, sends them to a server (at `http://localhost:8000/api/chat`), receives responses, and displays both user and AI messages in a chat window. The component uses `fetch` API for making HTTP requests.


## Table of Contents

* [App](#app)
* [sendMessage](#sendMessage)


## Components

### `App`

**Description**: This functional component represents the main chat application. It handles user input, sends messages to the server, receives responses, and updates the chat display.


**State**:

* `input`: String representing the current user input.
* `messages`: Array of objects, each representing a message with `role` (user/assistant) and `content`.

**Methods**:

- `sendMessage()`: Sends the user's input to the server and updates the chat messages.
- `setInput()`: Updates the user input state.
- `map`: Iterates over the messages array, and renders each message in the chat window, dynamically adding styling for user/AI messages.
- `return`: Renders the chat window, input field, and send button using JSX elements.


## Functions

### `sendMessage`

**Description**: Sends the user's message to the server and updates the chat messages.


**Parameters**:

- None


**Returns**:
- None


**Raises**:
- `Error`: An error during the fetch operation (network issues, server errors, etc.).


```javascript
  const sendMessage = async () => {
    if (input.trim() === "") return;

    const userMessage = { role: "user", content: input };
    setMessages([...messages, userMessage]);

    try {
      const response = await fetch("http://localhost:8000/api/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt: input })
      });

      const data = await response.json();
      const aiMessage = { role: "assistant", content: data.response };
      setMessages([...messages, userMessage, aiMessage]);
    } catch (error) {
      console.error("Error:", error);
    }

    setInput("");
  };