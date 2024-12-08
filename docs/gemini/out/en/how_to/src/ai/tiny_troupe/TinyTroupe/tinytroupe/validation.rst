rst
How to use the TinyPersonValidator class
========================================================================================

Description
-------------------------
This code defines a `TinyPersonValidator` class that validates a `TinyPerson` instance using OpenAI's Large Language Model (LLM).  It generates a series of questions based on a template, sends them to the `TinyPerson` instance for responses, and then uses the LLM to evaluate the responses.  The validation process is driven by a conversation between the LLM and the `TinyPerson` instance. It returns a confidence score (0.0 to 1.0) and a justification for that score.  The validation process can be customized using optional arguments for expectations and whether to include the agent specification in the prompt.


Execution steps
-------------------------
1. **Initialization**: The `validate_person` method initializes an empty list `current_messages` to store the conversation history.

2. **Prompt generation**: It reads a template for the prompt from a file (`check_person.mustache`) and renders it with optional input `expectations` using the `chevron` library.  A user prompt is also generated, asking the LLM to interview the `TinyPerson` based on given characteristics.  If `include_agent_spec` is True, the `TinyPerson`'s agent specification is included in the user prompt; otherwise, a mini-biography is included.

3. **LLM interaction**: The `current_messages` list is populated with the system and user prompts.  The `openai_utils.client().send_message()` method sends these messages to OpenAI's LLM.

4. **Interactive conversation**: The code enters a loop.  In each iteration:
   - It extracts the LLM's generated question from the `message["content"]`.
   - It appends the question to the `current_messages` list.
   - It sends the question to the `TinyPerson` instance using `person.listen_and_act()`.
   - It gathers the `TinyPerson`'s responses.
   - It appends the responses to `current_messages`.
   - It sends the updated `current_messages` to the LLM.
   - The loop continues until the LLM's response contains a specific termination mark ("```json").

5. **Validation Result**: If the LLM's response contains the termination mark and the validation is successful:
   - The code extracts the validation score and justification from the JSON part of the LLM's response.
   - It logs the score and justification.
   - It returns the score and justification.

6. **Validation Failure**: If no termination mark is found or if the LLM interaction fails, it returns `None` for both the score and the justification.


Usage example
-------------------------
.. code-block:: python

    from tinytroupe import TinyPerson  # Assuming TinyPerson is defined elsewhere
    from tinytroupe.validation import TinyPersonValidator

    # Create a TinyPerson instance (replace with your actual TinyPerson creation)
    my_person = TinyPerson("My Person", "some bio")

    # Validate the TinyPerson instance.  No expectations are passed.
    validation_result = TinyPersonValidator.validate_person(my_person)

    if validation_result:
        score, justification = validation_result
        print(f"Validation score: {score:.2f}")
        print(f"Justification: {justification}")
    else:
        print("Validation failed.")


    # Validate with expectations
    validation_result = TinyPersonValidator.validate_person(my_person, expectations = "be friendly and informative")
    if validation_result:
        score, justification = validation_result
        print(f"Validation score (with expectations): {score:.2f}")
        print(f"Justification (with expectations): {justification}")
    else:
        print("Validation failed (with expectations).")