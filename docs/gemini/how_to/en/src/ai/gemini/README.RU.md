How to use the `gemini` model's system and command instructions.

The `gemini` model allows you to provide both system-wide and per-request instructions.  This helps maintain consistency and context throughout interactions.

**System Instructions (`system_instruction`):**

These instructions are provided at initialization and remain constant for the entire lifetime of the model instance.  They cannot be changed once set.  Think of this as the core guiding principles for the model.  These are generally placed in a global configuration file, and are often used for initializing the model with specific contexts or tasks.

**Example (Python):**

```python
def __init__(self,
                 api_key: str,
                 model_name: Optional[str] = None,
                 generation_config: Optional[Dict] = None,
                 system_instruction: Optional[str] = None,
                 **kwargs):

                 ...
```

The `system_instruction` parameter is part of the initialization process, taking a string as input, outlining the model's fundamental role and expected behavior.

**Command Instructions (`command_instruction`):**

These instructions are provided *before* each request to the model.  They are typically extensions or modifications to the system-level instruction.  Critically, these instructions are *changeable* for each request. This allows for tailoring the model's behavior to specific prompts and contexts.

**Where to find instructions:**

* **Global instructions:**  Located in the `src/ai/prompts` directory.  These are the default instructions.
* **Per-request instructions:** Often found in the `instruction` folder for individual clients. The client's specific instructions are prioritized over the global instructions, ensuring that your interaction with the model is relevant to the client's task.
* **Client Configuration (src.endpoints):**  The `src.endpoints` directory lists the available clients, each potentially having its own set of global instructions.
* **Client-Specific Global Instructions:** Clients can have their own global instructions files (e.g., within a `prompt` folder) to override the default instructions.

**File Naming Conventions:**

Instructions are typically stored in files.  Use a consistent naming convention for clarity:

```
instruction_doc_writer_html_en.md  // English instructions for a document writer
instruction_code_checker_en.md     // English instructions for a code checker
instruction_code_checker_he.md     // Hebrew instructions for a code checker
instruction_code_explainer_en.md  // English instructions for a code explainer
instruction_code_explainer_ru.md  // Russian instructions for a code explainer
```

**How to use:**

1. **Configure the `system_instruction`** during model instantiation with the desired global parameters for the model.
2. **Provide `command_instruction`** before each API call with a prompt tailored to the specific request. This override the global system instructions on a per-request basis. Choose appropriate instructions files based on the tasks.

By leveraging both system and command instructions, you can maintain a consistent model while providing specific instructions for each interaction, thus increasing the relevance and accuracy of the results.