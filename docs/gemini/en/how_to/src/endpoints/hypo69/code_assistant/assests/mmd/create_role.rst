rst
How to Create a New Role
========================================================================================

Description
-------------------------
This code block defines the steps to create a new role within the system, specifically detailing the necessary updates to various configuration files.  It uses a graph representation to visualize the sequence of actions, from modifying the `code_assistant.json` file to adding entries in translation files, prompts, and instruction sets.

Execution steps
-------------------------
1. **Identify the role details:**  Gather all information required to define the new role. This includes the role's name, permissions, associated actions, and any other relevant properties.

2. **Update `code_assistant.json`:** Add the newly identified role to the list of roles defined within the `code_assistant.json` file.  This file likely acts as a central repository of role information. The specific format and structure of this file should be referred to in the relevant documentation for `code_assistant.json`.

3. **Add the role to `translations/translations.json`:** Ensure the new role is included in the translation files. Update `translations/translations.json` to include any necessary translations associated with this role. This ensures correct language support for the role-related text.

4. **Generate system prompt (ai/prompts/developer):** Create a dedicated system prompt in the `ai/prompts/develpoper` directory. This prompt should be tailored to handle the tasks and specific instructions for the newly defined role.

5. **Create command instruction (instructions/...):**  Generate a command instruction file, located within the `instructions/...` directory. This file provides instructions for using the role within the system. The format and content of these instructions should be consistent with existing examples within the `instructions/...` directory.

Usage example
-------------------------
.. code-block:: text

    # This is a textual representation of the process.  The actual code would be using a scripting language
    # to manipulate the JSON files and create the prompts and instructions.

    # Example of updating code_assistant.json (pseudocode)
    # ... (load code_assistant.json)
    # ... (add new role with properties)
    # ... (save updated code_assistant.json)

    # Example of adding to translations.json (pseudocode)
    # ... (load translations.json)
    # ... (add translation strings for the new role)
    # ... (save updated translations.json)