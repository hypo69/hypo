# Kazarinov's Telegram Bot CLI

## Overview

This module provides the command-line interface (CLI) for launching the Kazarinov's Telegram Bot. It allows users to specify settings from a JSON configuration file or via command-line arguments.  The script handles loading settings, creating a bot instance, and launching the bot's asynchronous application. Error handling is implemented to catch and log any exceptions during the bot's execution.


## Table of Contents

* [parse_args](#parse-args)
* [main](#main)


## Functions

### `parse_args`

**Description**: Parses command-line arguments for the bot.  Allows specifying a settings file and the bot's mode (test or prod).

**Parameters**:
- None

**Returns**:
- `dict`: A dictionary containing the parsed command-line arguments.  Includes the `settings` file path (if provided) and the `mode` ('test' or 'prod').

**Raises**:
- `None`: No exceptions explicitly raised.


### `main`

**Description**: The main function for launching the Kazarinov's Telegram Bot.  It handles loading settings from a file if provided, creates a `KazarinovTelegramBot` instance, and runs the bot's asyncio application.

**Parameters**:
- None

**Returns**:
- `None`

**Raises**:
- `Exception`:  Any exception caught during the asyncio application run will be logged using the `logger`.