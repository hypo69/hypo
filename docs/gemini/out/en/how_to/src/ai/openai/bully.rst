rst
How to use the bully function
========================================================================================

Description
-------------------------
This Python code defines a function `bully` that interacts with the OpenAI API to generate examples of bullying behavior from a bully's perspective. It takes a user message and a list of messages (initially including a system prompt) as input, and returns a list of messages exchanged. The function leverages the GPT-3.5-turbo model to craft a response.

Execution steps
-------------------------
1. **Import necessary libraries:** The code imports the `os` module (though it's not directly used in the provided function) and the OpenAI library.  It's important to install the OpenAI Python library (`pip install openai`).
2. **Define a system prompt:** A predefined system prompt guides the AI model to emulate a bully. This prompt specifies that the AI should write from a bully's perspective, using personal and specific language, and provide an example from literature of bullying tactics.  The prompt format, requesting a JSON structure containing a `bully_response` key, helps ensure the expected output format.
3. **Define the `bully` function:** This function takes a user message and a list of messages as input.
4. **Append the user message to the messages list:** The user's input is added to the message list.
5. **Make an API call to OpenAI:** The `openai.ChatCompletion.create` function sends a request to the OpenAI API using the defined messages. The `gpt-3.5-turbo` model is used.
6. **Append the AI's response to the messages list:** The AI's response is appended to the messages list to enable further conversation or processing if needed.
7. **Return the messages list:** The function returns the list of messages exchanged, which now includes the AI's response.  Crucially, the return value is *messagess* (with an extra 's'), which appears to be a typo.


Usage example
-------------------------
.. code-block:: python

    import openai
    import os

    # Replace with your actual OpenAI API key
    openai.api_key = "YOUR_API_KEY"

    # Example usage
    user_message = "Tell me an example of a bully's intimidation tactic."
    messages = [
        {"system": "user", "content": """You are an expert on hate speech.
Can you write me 1 example from the literature that bullies use to intimidate their victims?
Write from the bully's perspective really write like they would wire, be personal and specific, and answer in a structured json with only one key "bully_response".
I will provide a statement and you will answer with an example."""}
    ]
    try:
        response = bully(user_message, messages)
        # Process the response (print or save it to a file)
        for message in response:
            print(message)
    except Exception as e:
        print(f"An error occurred: {e}")