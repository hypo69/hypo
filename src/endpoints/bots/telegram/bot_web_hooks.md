
# Telegram Bot with FastAPI Integration

This document provides a detailed explanation of the code for a Telegram bot that integrates with a FastAPI server. The code is designed to handle webhook updates and also supports polling as a fallback.

## Project Structure

The project is structured as follows:

-   `src/fast_api/fast_api.py`: Contains the `FastApiServer` class which provides a singleton FastAPI application.
-   `src/endpoints/bots/telegram/bot_web_hooks.py`: This file, which you've provided, includes:
    -   `TelegramBot`: A class for handling Telegram bot interactions, and
    -   Integration of the bot with a FastAPI application.
-   `src/endpoints/bots/telegram/bot_handlers.py`: (Not shown in the code) contains the `BotHandler` class that manages message handling logic.
- `src/utils/jjson.py`: Provides utility functions for loading JSON files into namespaces
- `src/utils/get_free_port.py`: A utility method for getting a free port in a given range.
- `src/logger/logger.py`: A utility class to log events to the application log.
-  `src/config.json`: The configuration of the application.
-   `src/endpoints/bots/telegram/telegram.json`: Bot settings.

## `TelegramBot` Class

This class is responsible for setting up and handling the Telegram bot.

### `__init__` Method

```python
    def __init__(self,
                 token: str,
                 port: int,
                 webhook_url: Optional[str] = None,
                 bot_handler: Optional[BotHandler] = None,
                 fast_api: FastApi = None):
```

-   **`token` (str):** The Telegram bot token obtained from BotFather.
-   **`port` (int):** The port on which the FastAPI server will run.
-   **`webhook_url` (Optional[str], default='/telegram_webhook'):** The URL path for the webhook endpoint. If not provided, defaults to '/telegram_webhook'.
-   **`bot_handler` (Optional[BotHandler], default=None):** An instance of the `BotHandler` class to delegate message handling to. If `None`, a default `BotHandler` is created.
-   **`fast_api` (FastApi, default=None):** An instance of the `FastApi` class to run the server.

**Functionality:**

- Initializes the Telegram bot using the provided `token`.
- Creates a `BotHandler` instance if one is not passed.
- Sets the `webhook_url`.
- Calls `_register_handlers()` to set up message handlers.
- Creates a task for running the `FastApi` server with `fast_api.run(port=port)`.

### `_register_handlers` Method

```python
    def _register_handlers(self):
```

This method registers various command and message handlers with the Telegram bot application.

**Functionality:**
- Sets up handlers for `/start`, `/help`, and `/sendpdf` commands, each of which will use methods in the provided `bot_handler` to process the logic.
-  Sets up a handler for regular text messages using the `_handle_message` method.
-  Sets up handlers for voice messages, documents and logs using the provided `bot_handler`.

### `_handle_message` Method

```python
    async def _handle_message(self, update: Update, context: CallbackContext) -> None:
```

-   **`update` (Update):** An object containing the incoming update from Telegram.
-   **`context` (CallbackContext):** A context object for the current update, providing bot-specific information and utilities.

**Functionality:**

-   Delegates text message handling to the `bot_handler.handle_message` method.

## `telegram_webhook` Function

```python
async def telegram_webhook(request: Request):
```

-   **`request` (Request):** An object representing the incoming HTTP request from Telegram.

**Functionality:**

-   Handles incoming webhook requests from Telegram.
-   Checks if the bot instance has been initialized.
-   Parses the incoming JSON data from the request body.
-   Processes the incoming update from Telegram, and returns a response with status code 200 to indicate success.
- Returns error with status code 500 if processing fails.

## `initialize_bot` Function

```python
async def initialize_bot(token: str, port: int):
```

-   **`token` (str):** The Telegram bot token.
-   **`port` (int):** The port number for the FastAPI server.

**Functionality:**

-   Initializes the `TelegramBot` instance using the provided `token` and `port`.
-  Sets the webhook URL for the bot instance.
-  Starts polling if no webhook URL is defined.

## `@app.on_event("startup")` Decorator

```python
@app.on_event("startup")
async def startup_event():
```
**Functionality:**

-   This decorator registers the `startup_event` function to be executed when the FastAPI application starts.
-   Retrieves the Telegram bot token from the environment variable `TELEGRAM_BOT_TOKEN`.
-   Retrieves the port number for the FastAPI server from the environment variable `PORT`, defaulting to 8000.
-   Calls `initialize_bot` with the retrieved token and port.

## `@app.on_event("shutdown")` Decorator

```python
@app.on_event("shutdown")
async def shutdown_event():
```

**Functionality:**

-   This decorator registers the `shutdown_event` function to be executed when the FastAPI application shuts down.
-   Deletes the bot's webhook.

## `@app.add_route("/telegram_webhook", telegram_webhook, methods=["POST"])` Decorator

```python
app.add_route("/telegram_webhook", telegram_webhook, methods=["POST"])
```

**Functionality:**

-   Registers the `telegram_webhook` function to handle requests sent to the `/telegram_webhook` path, only accepting POST methods.
-  This function is what Telegram calls when a webhook event is dispatched.

## `app.register_router()`
This method adds the router with all the routes to the application.

## `app.run()`
Starts the application on the address and port set in `FastApi` class.

## `if __name__ == "__main__":` Block

This block executes when the script is run directly.

**Functionality:**

-   Sets the bot_instance as `None`.
-   Creates an instance of the `FastApi` class.
-   Sets the bot webhook route using `add_route`
-   Registers the router with the app.
-  Starts the FastAPI application using `app.run()`.

## Configuration

-   The bot's configuration (like the webhook URL, telegram port) is loaded from `src/endpoints/bots/telegram/telegram.json`.
-   The FastAPI configuration (like host and port) is loaded from `src/fast_api/fast_api.json`

## Environment Variables

-   **`TELEGRAM_BOT_TOKEN`**: The Telegram bot token.
-   **`PORT`**: The port number on which the FastAPI server should run.

## Running the Bot

To run the bot:

1.  Ensure you have Python 3.7+ installed.
2.  Install the required packages using `pip install -r requirements.txt`
3.  Create a `.env` file or set the environment variables `TELEGRAM_BOT_TOKEN` and `PORT`.
4.  Run the script with `python src/endpoints/bots/telegram/bot_web_hooks.py`.

