rst
How to use the KazarinovTelegramBot
========================================================================================

Description
-------------------------
This code block describes the `KazarinovTelegramBot` and its `BotHandler`, which handles incoming URLs and executes a scenario. The `BotHandler` parses the incoming links to determine if they originate from specific domains (e.g., one-tab.co.il).  If the URL is from a valid domain, it fetches data, validates it, and if successful, runs a Mexiron scenario. This diagram outlines the process.

Execution steps
-------------------------
1. The bot receives a URL from a Telegram message.
2. The `BotHandler` checks if the URL's domain is from one of the specified domains (e.g., one-tab.co.il).
3. If the URL is from a specified domain:
    - It retrieves data from the associated service (e.g., OneTab).
    - It validates the retrieved data.
4. If the retrieved data is valid:
    - It executes a Mexiron scenario.
5. If the Mexiron scenario is successful:
    - It sends a "Done!" message and the link to WhatsApp.
6. If the Mexiron scenario fails:
    - It sends an error message.
7. If the URL's domain is not one of the specified domains or data validation fails:
    - It sends an appropriate message (e.g., "Try again" or "Incorrect data").


Usage example
-------------------------
.. code-block:: python
    # Example usage (Illustrative; actual implementation depends on the framework)
    # Assuming you have a Telegram bot setup and the BotHandler class defined
    import telegram
    from your_module import BotHandler # Replace with your actual module

    # Create a BotHandler instance.  Replace with any needed configuration.
    bot_handler = BotHandler(one_tab_api_key='your_api_key', mexiron_credentials={'username': '...', 'password':'...' })


    def handle_message(update: telegram.Update, context: telegram.ext.CallbackContext):
        # Extract the message.
        message_text = update.message.text

        # Check for the presence of URL within a message
        if not message_text.startswith('http'):
           return context.bot.send_message(chat_id=update.effective_chat.id, text="Invalid input. Please provide a URL.")


        try:
           # Attempt to process the URL
           result = bot_handler.process_url(message_text)
           if result:
              context.bot.send_message(chat_id=update.effective_chat.id, text=result)
        except Exception as e:
           context.bot.send_message(chat_id=update.effective_chat.id, text=f"Error: {str(e)}")