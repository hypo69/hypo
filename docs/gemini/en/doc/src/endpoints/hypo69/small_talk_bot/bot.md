# hypotez/src/endpoints/hypo69/small_talk_bot/bot.py

## Overview

This module defines the `PsychologistTelgrambot` class, a custom Telegram bot designed for psychological support. It utilizes the Google Gemini API for generating responses to user messages and integrates with other modules for file handling, URL routing, and logging.

## Table of Contents

* [Overview](#overview)
* [Classes](#classes)
    * [PsychologistTelgrambot](#psychologisttelgrambot)
        * [register_handlers](#register_handlers)
        * [start](#start)
        * [handle_message](#handle_message)
        * [get_handler_for_url](#get_handler_for_url)
        * [handle_suppliers_response](#handle_suppliers_response)
        * [handle_onetab_response](#handle_onetab_response)
        * [handle_next_command](#handle_next_command)
        * [handle_document](#handle_document)
* [Functions](#functions)
    * [handle_suppliers_response](#handle_suppliers_response)
    * [handle_onetab_response](#handle_onetab_response)
    * [handle_next_command](#handle_next_command)


## Classes

### `PsychologistTelgrambot`

**Description**: A custom Telegram bot for psychological support, inheriting from `TelegramBot`.  This class handles bot commands, messages, and documents.

**Attributes**:

* `token` (str): Telegram bot API token. Initialized in `__post_init__`.
* `d` (Driver): WebDriver instance. Initialized in `__post_init__`.
* `model` (GoogleGenerativeAI): Instance of the Google Gemini API. Initialized in `__post_init__`.
* `system_instruction` (str): System instruction for the Gemini model. Initialized in `__post_init__`.
* `questions_list` (list): List of questions for the bot. Initialized in `__post_init__`.
* `timestamp` (str): Current timestamp. Initialized to the current time using `gs.now`.


**Methods**:

#### `__post_init__`

**Description**: Initializes the bot, setting up the API token, WebDriver, Gemini model, system instruction, and question list.

#### `register_handlers`

**Description**: Registers bot commands and message handlers.

#### `start`

**Args:**
- `update` (Update): The update containing the message.
- `context` (CallbackContext): The context object.

**Description**: Handles the `/start` command, sending a greeting message.


#### `handle_message`

**Args:**
- `update` (Update): The update containing the message.
- `context` (CallbackContext): The context object.

**Description**: Handles incoming text messages.  It logs the message, sends a response from the Gemini model, and updates a chat log.

**Returns**:
- `None`:

#### `get_handler_for_url`

**Args:**
- `response` (str): The incoming message.

**Description**: Maps URLs to specific handlers.

#### `handle_suppliers_response`

**Args:**
- `update` (Update): The update containing the message.
- `response` (str): The response string.


**Description**: Handles URLs associated with suppliers' websites, potentially using the `mexiron` module.

#### `handle_onetab_response`


**Args:**
- `update` (Update): The update containing the message.
- `response` (str): The response string.

**Description**: Handles URLs related to OneTab.


#### `handle_next_command`

**Description**: Handles the command `--next` by picking a random question from the `questions_list` and generating a response using the Gemini model.

#### `handle_document`

**Args:**
- `update` (Update): The update containing the message.
- `context` (CallbackContext): The context object.

**Description**: Handles document uploads, receiving the file content and responding.


## Functions


### `handle_suppliers_response`


**Description:** (Defined in `PsychologistTelgrambot`)
Handles URLs from suppliers, attempting a scenario execution via `mexiron`.

### `handle_onetab_response`

**Description:** (Defined in `PsychologistTelgrambot`)
Handles URLs from OneTab, attempting a scenario execution via `mexiron`.


### `handle_next_command`

**Description:** (Defined in `PsychologistTelgrambot`)
Handles the `--next` command to retrieve a random question and generate a response.