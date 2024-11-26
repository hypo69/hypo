# Usage Guide for `bully.py`

This guide explains how to use the `bully.py` script, which interacts with the OpenAI API to generate responses mimicking a bully's intimidation tactics.  **Caution:** This script is intended for educational and demonstration purposes only.  **Do not use this script to generate harmful or offensive content.**

## File: `hypotez/src/ai/openai/bully.py`

This Python script leverages the OpenAI API to craft intimidating messages.  It leverages the `gpt-3.5-turbo` model.

## Prerequisites

1. **Install the OpenAI Python library:**
   ```bash
   pip install openai
   ```

2. **Set your OpenAI API key:**
   The script requires your OpenAI API key.  Replace `"YOUR_API_KEYS_OPENAI"` with your actual key in the script.


## How to Use

The script defines a function `bully` that takes an optional `user_message` and a list of `messages`.


```python
def bully(user_message="Hello!", messages=[{"system": "user", "content": system_prompt}]):
    # ... (rest of the function)
```

* **`user_message` (optional):**  A string representing the user's input. Defaults to "Hello!".  This input can be any statement.
* **`messages` (optional):** A list of messages for the chat history.  The initial `messages` list sets the system prompt for the model.  This is crucial for guiding the response to match a bullying persona.  It's highly recommended not to modify this.


**Example Usage:**


```python
import src.ai.openai  # Assuming your import path is correct

# Replace with your API key
openai.API_KEY = "YOUR_API_KEY"

# Example usage.  Important: do not use this with inappropriate or hateful input.
user_message = "I'm having a bad day."
response = src.ai.openai.bully(user_message=user_message)

# Process the response
print(response)  # Prints a list of messages
```

**Crucial Considerations:**

* **Ethical Concerns:** Be extremely cautious and responsible when using this script.  It can generate harmful content.  Use it only for educational or demonstration purposes.
* **Response Structure:** The script expects a specific JSON structure as a response. Check the structure of the response carefully to ensure it matches the intended output.  Examine the script's definition of `system_prompt` to understand what kind of response it anticipates.
* **Error Handling:**  The example lacks error handling.  A production-level script needs `try...except` blocks to gracefully manage potential API issues or incorrect input.


**Important Note:** The `messages` parameter is crucial in setting the context for the model.  The current setup uses a fixed `system_prompt` to guide the generation of bullying responses. Modifying this significantly will affect the output and may lead to responses that are not as expected.  It is vital to review and understand the system prompt.


This guide provides a basic understanding of the `bully.py` script.  Always prioritize ethical considerations and responsible use of AI tools.