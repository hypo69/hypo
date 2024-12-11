# TinyTroupe 🤠🤓🥸🧐

## <input code>

```
# TinyTroupe 🤠🤓🥸🧐
*LLM-powered multiagent persona simulation for imagination enhancement and business insights.*

<p align="center">
  <img src="./docs/tinytroupe_stage.png" alt="A tiny office with tiny people doing some tiny jobs.">
</p>

... (rest of the README content)
```

## <algorithm>

A detailed algorithm for TinyTroupe is difficult to represent in a simple flowchart because the core functionality relies heavily on the interaction and responses from Large Language Models (LLMs).  The process essentially involves defining personas (TinyPersons), environments (TinyWorlds), and then interacting with those personas through a series of prompts.  The LLM then produces the simulated conversations and actions.  There's no clear step-by-step calculation; instead, the flow is guided by the experimenter's instructions.


**Example Interaction Flow:**

1. Experimenter defines a TinyPerson (e.g., Lisa, a data scientist) with specific characteristics (age, occupation, personality traits).
2. Experimenter defines a TinyWorld (e.g., a "chat room").
3. Experimenter prompts a TinyPerson to interact with another TinyPerson (e.g., "Ask Oscar about his project").
4. The TinyWorld sends the prompt to the LLM.
5. LLM processes the prompt and persona data, generating a simulated response from the TinyPerson.
6. The TinyWorld relays the response to the experimenter.
7. The experimenter analyzes the simulated response and can provide further prompts.

This cycle repeats until the desired level of interaction is achieved.  The crucial part is the LLM's role in generating realistic and contextually appropriate responses.


## <mermaid>

```mermaid
graph TD
    A[Experimenter] --> B{Define TinyPerson};
    B -- Lisa, Data Scientist -- C[Define TinyWorld];
    C -- Chat Room -- D{Prompt TinyPerson};
    D --> E[LLM];
    E -- Simulated Response -- F[TinyWorld];
    F --> G[Display to Experimenter];
    G --> D;
    subgraph LLM Processing
        E -- Persona Data -- E1;
        E -- Prompt -- E2;
        E1 -.-> E2 -.-> E;
    end;
```


## <explanation>

**1. Imports:**

The README, not the code, describes dependencies.  It mentions a dependency on the Azure OpenAI Service or the OpenAI API (GPT-4) to interact with LLMs.  This implies Python libraries to interact with these services.  No explicit import statements are given.  A `config.ini` file is mentioned, presumably for configuration details, such as API keys, model types, etc. The existence of `.ipynb` files suggests an intent to use Jupyter Notebooks.

**2. Classes:**

The README describes two key abstractions: `TinyPerson` and `TinyWorld`.

*   **`TinyPerson`:** Represents simulated people with personalities, interests, and goals. Methods like `listen`, `see`, `act` allow interaction with the environment and other `TinyPerson`s.  The README provides examples of defining attributes like "age", "occupation," and "personality traits". This suggests methods to define these and other aspects of the persona and its behavior. The `TinyPersonFactory` class is described, implying a method to automatically generate `TinyPerson` instances using LLMs.

*   **`TinyWorld`:** Represents the environment where `TinyPerson`s interact. Methods likely exist to manage interactions (e.g., `make_everyone_accessible()`), initiate conversations, and keep track of interactions.

**3. Functions:**

The README details how to use these classes, but the actual code for these classes is missing. The provided examples showcase functions that use and create `TinyPerson` and `TinyWorld` objects.

**4. Variables:**

The variables in the examples are likely instances of the `TinyPerson`, `TinyWorld`, or other custom objects, as implied by the example code using `create_lisa_the_data_scientist()` which constructs the `TinyPerson` instance and other similar functions.

**5. Possible Errors/Improvements:**

*   **LLM Dependency:** The library's functionality is highly dependent on the availability and reliability of the LLM API.  Issues with API rate limits, errors in responses, or lack of API key availability could cause failures.  Error handling and robust retry mechanisms would be beneficial.
*   **Consistency in API Usage:**  The README explicitly warns about the library being under development, with frequent API changes. Providing more stable APIs for interacting with `TinyPerson` and `TinyWorld` would improve the usability of the library.
*   **Detailed Documentation:**  A lack of code provided makes it hard to assess the internal implementation details, making it difficult to understand how the simulation works in depth.  More thorough documentation of the classes, functions, and parameters would enhance the library's accessibility.
*   **Caching Startegies:** While caching is mentioned, the exact implementation is missing.  More detail about caching Startegies, implementation details, and how to configure them would greatly benefit users.
*   **Content Filtering:** The README emphasizes the importance of content filters for ethical and safe simulations.  The code, lacking concrete implementations of this, needs to be explicitly demonStarted.


**Relationships with other parts of the project:**

The examples (`examples/` folder), config file (`config.ini`), and testing framework (`tests/`) are all crucial parts of the project supporting the core library, which interacts with LLMs through the Azure OpenAI or OpenAI API.  The simulation relies on the definitions provided in `.ipynb` files.  The testing and examples are used to demonStarte and validate the library's functionality in various scenarios, and provide further insight into how it could be utilized within these scenarios.