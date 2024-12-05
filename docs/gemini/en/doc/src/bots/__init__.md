# bots

## Overview

This module provides basic bot functionalities, currently including a Telegram bot.

## Table of Contents

* [TelegramBot](#telegram-bot)

## Classes

### `TelegramBot`

**Description**: Implements a Telegram bot.


**Methods**

*  **`__init__(self, token: str, chat_id: str)`**:
    **Description**: Initializes the Telegram bot with the given token and chat ID.
    **Parameters**:
        - `token` (str): The Telegram bot token.
        - `chat_id` (str): The chat ID to send messages to.
    **Raises**:
        - `ValueError`: If `token` is empty or invalid.
        - `ValueError`: If `chat_id` is invalid.

*  **`send_message(self, message: str)`**:
    **Description**: Sends a message to the specified chat ID.
    **Parameters**:
        - `message` (str): The message to send.
    **Raises**:
        - `TelegramError`: If there's an error sending the message.  (e.g., network issue, invalid message)


## Functions

(No functions found in the provided code)