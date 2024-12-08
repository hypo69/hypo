# openai.js

## Overview

This JavaScript file defines the `OpenAI` class for interacting with the OpenAI API. It includes methods for chat completion and transcription. It utilizes the `openai` library and `config` for API key retrieval and file handling.

## Table of Contents

- [OpenAI](#openai)
    - [chat](#chat)
    - [transcription](#transcription)


## Classes

### `OpenAI`

**Description**: This class handles interactions with the OpenAI API. It manages API calls for chat completion and transcription.


**Properties**:

- `roles`: An object containing predefined roles for messages in a chat context.
- `openai`: An instance of `OpenAIApi` for executing OpenAI API calls.


**Constructor**:

```javascript
constructor(apiKey)
```

**Parameters**:

- `apiKey` (string): The API key for authentication with the OpenAI API.


**Methods**:

#### `chat`

```javascript
async chat(messages)
```

**Description**: This method sends a chat completion request to the OpenAI API.

**Parameters**:

- `messages` (array): An array of chat messages, where each message object has a `role` and `content` property.


**Returns**:

- `object | null`: The response from the OpenAI API, containing the bot's reply, or `null` if an error occurs.


**Raises**:

- `Error`: An error occurs during the API call.


#### `transcription`

```javascript
async transcription(filepath)
```

**Description**: This method transcribes audio from a file using the OpenAI Whisper API.

**Parameters**:

- `filepath` (string): The path to the audio file to transcribe.


**Returns**:

- `string | null`: The transcribed text, or `null` if an error occurs.


**Raises**:

- `Error`: An error occurs during the API call.



## Variables

### `openai`

**Description**: An instance of the `OpenAI` class, initialized with the API key from the `config` module.


**Type**: `OpenAI` object.