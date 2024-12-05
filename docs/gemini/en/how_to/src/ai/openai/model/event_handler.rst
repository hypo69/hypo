rst
How to use this code block
=========================================================================================

Description
-------------------------
This Python code defines a custom `EventHandler` class that handles events during an OpenAI Assistant interaction. It extends the `AssistantEventHandler` class and overrides methods to handle text updates and tool calls, particularly for code interpreter tool calls.  It prints the events to the console as they occur, including text updates, tool call types, and code interpreter input and output logs.

Execution steps
-------------------------
1. **Import necessary modules:** The code imports necessary modules from the `openai` library, including `AssistantEventHandler`, `OpenAI`, `Text`, `TextDelta`, `ToolCall`, and `ToolCallDelta`.

2. **Define the `EventHandler` class:** This class extends `AssistantEventHandler` and overrides several methods.

3. **Override `on_text_created`:** This method prints the text message sent by the assistant to the console.

4. **Override `on_text_delta`:** This method handles incremental updates to text messages, appending the delta to the console output.

5. **Override `on_tool_call_created`:** This method prints the type of tool call (e.g., "code_interpreter") to the console.

6. **Override `on_tool_call_delta`:** This method handles incremental updates to tool calls, focusing on code interpreter tool calls.  
    - If the tool call is a `code_interpreter` type, it prints the input provided to the code interpreter to the console.
    - It then prints "output >" to signal the start of the output.
    - It iterates through the outputs of the code interpreter.
    - If an output's type is "logs", it prints the logs to the console.

7. **Usage (not directly in the code block):** To use this `EventHandler`, you would typically instantiate it and provide it to the `OpenAI` client when making an API call to an assistant. The assistant's response will be streamed to the console using the methods in the `EventHandler` class.  This handling is essential for applications that require real-time updates during a conversation with an AI assistant.


Usage example
-------------------------
.. code-block:: python

    import openai
    from openai import OpenAI
    from hypotez.src.ai.openai.model.event_handler import EventHandler

    # Replace with your OpenAI API key
    openai.api_key = "YOUR_API_KEY"

    client = OpenAI()
    event_handler = EventHandler()

    response = client.beta.threads.runs.create(
        thread_id="YOUR_THREAD_ID",
        messages=[
            {"role": "user", "content": "Write a Python function to calculate the factorial of a number."},
        ],
        model="gpt-3.5-turbo-1106",
        assistant_event_handler=event_handler,
        # add other run parameters
        )


    #Example with streaming output
    for event in response.stream():
        if 'delta' in event:
          if isinstance(event['delta'],dict) and 'role' in event['delta']:
              # handle event
              #  handle other events...