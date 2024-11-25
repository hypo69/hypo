# openai.js Documentation

## Overview

This module provides a wrapper for the OpenAI API, enabling interaction with various models, including chat and transcription.  It utilizes the `openai` JavaScript library for seamless integration.

## Table of Contents

* [Classes](#classes)
    * [OpenAI](#openai)
* [Functions](#functions)
    * [openai](#openai-1)


## Classes

### OpenAI

**Description**: This class acts as an interface for interacting with the OpenAI API. It handles API key configuration and facilitates communication with the models.

**Constructor**:
```javascript
constructor(apiKey)
```

**Parameters**:
- `apiKey` (string): The API key for authentication with the OpenAI API.

**Methods**:

#### `chat`

**Description**: Sends a chat message to an OpenAI model.

```javascript
async chat(messages)
```

**Parameters**:
- `messages` (array): An array of message objects, each with a `role` and `content`.  Example:
```javascript
[
  { role: 'user', content: 'Hello!' },
  { role: 'assistant', content: 'Hi there!' },
]
```


**Returns**:
- `message` (object): The message object returned by the OpenAI API.  Returns `undefined` upon error.


**Raises**:
- `Error`: An error occurred during the API call.


#### `transcription`

**Description**: Performs transcription of audio files using the OpenAI API.

```javascript
async transcription(filepath)
```

**Parameters**:
- `filepath` (string): The path to the audio file to be transcribed.

**Returns**:
- `text` (string): The transcribed text.  Returns `undefined` upon error.

**Raises**:
- `Error`: An error occurred during the API call.



## Functions

### `openai`

**Description**: An instance of the `OpenAI` class, pre-configured with the API key retrieved from the `config` module.

```javascript
const openai = new OpenAI(config.get('OPENAI_KEY'))
```

**Parameters**:
- None.  It is initialized with an API key retrieved from the `config` module


**Returns**:
- `OpenAI` object instance.


```