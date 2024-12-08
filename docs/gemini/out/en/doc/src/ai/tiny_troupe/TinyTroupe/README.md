# TinyTroupe 🤠🤓🥸🧐

## Overview

LLM-powered multiagent persona simulation for imagination enhancement and business insights.  This library allows for the simulation of people with specific personalities, interests, and goals, leveraging LLMs to generate realistic behavior.  The focus is on understanding human behavior within simulated environments, enabling various applications like advertisement evaluation, software testing, synthetic data generation, product/project feedback, and brainstorming.

## Table of Contents

- [Examples](#examples)
- [Pre-requisites](#pre-requisites)
- [Installation](#installation)
- [Principles](#principles)
- [Project Structure](#project-structure)
- [Using the Library](#using-the-library)
    - [TinyPerson](#tinyperson)
    - [TinyWorld](#tinyworld)
    - [Utilities](#utilities)
    - [Caching](#caching)
        - [Caching Simulation State](#caching-simulation-state)
        - [Caching LLM API Calls](#caching-llm-api-calls)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)
- [Citing TinyTroupe](#how-to-cite-tinytroupe)
- [Legal Disclaimer](#legal-disclaimer)
- [Trademarks](#trademarks)


## Examples

Examples of TinyTroupe's use, available in the `./examples/` folder.  These are primarily Jupyter notebooks showcasing interactive simulations.  Dark themes are recommended for optimal visualization of simulation outputs.

### Example 1 (Interview with Customer)

Simulates an interview scenario between a business consultant and a banker.

### Example 2 (Advertisement Evaluation)

Evaluates TV ad options with a simulated audience.

### Example 3 (Product Brainstorming)

Simulates a focus group brainstorming new AI features for Microsoft Word.


## Pre-requisites

- Python 3.10 or higher (Anaconda recommended).
- Access to Azure OpenAI Service or OpenAI GPT-4 APIs.  Set environment variables:
    - `AZURE_OPENAI_KEY` and `AZURE_OPENAI_ENDPOINT` for Azure OpenAI Service.
    - `OPENAI_API_KEY` for OpenAI.
- Config.ini file (optional, defaults provided).

**IMPORTANT:**  Utilize content filters if available (especially with Azure OpenAI) to prevent generation of harmful content.


## Installation

1. Create a new Python environment:
   ```bash
   conda create -n tinytroupe python=3.10
   ```
2. Activate the environment:
   ```bash
   conda activate tinytroupe
   ```
3. Set API keys as environment variables (see [Pre-requisites](#pre-requisites)).
4. Clone the repository:
   ```bash
   git clone https://github.com/microsoft/tinytroupe
   cd tinytroupe
   ```
5. Install from the local repository:
   ```bash
   pip install .
   ```

### Local Development

For modifying TinyTroupe, install in editable mode:
```bash
pip install -e .
```


## Principles

TinyTroupe prioritizes:

1. **Programmatic**: Defines agents and environments programmatically (Python and JSON).
2. **Analytical**: Designed to enhance understanding of people and interactions (Jupyter notebooks recommended).
3. **Persona-based**: Agents represent archetypal personas with customizable attributes.
4. **Multiagent**: Facilitates interaction between multiple agents within defined environments.
5. **Utilities-heavy**: Provides tools for simulation setup, extraction, validation and reporting.
6. **Experiment-oriented**: Allows iterative exploration and refinement of simulations.


## Project Structure

- `/tinytroupe`: Python library source.
- `/tests`: Unit tests.
- `/examples`: Jupyter notebook examples.
- `/data`: Data for examples.
- `/docs`: Documentation.


## Using the Library

### TinyPerson

Represents a simulated person with specific personality traits.

### TinyWorld

Represents the environment in which agents interact.

### Utilities

- `TinyPersonFactory`: Generates new `TinyPerson`s using LLMs.
- `TinyTool`: Simulated tools for agents.
- `TinyStory`: Manages the simulated narrative.
- `TinyPersonValidator`: Validates agent behavior.
- `ResultsExtractor`/`ResultsReducer`: Extract and reduce simulation results.


### Caching

#### Caching Simulation State

Manages simulation state changes for efficient reruns of specific segments.

#### Caching LLM API Calls

Caches LLM API responses for reduced costs when identical requests are made.


### Config.ini

Customizable parameters (e.g., API type, model parameters, logging level) are stored here.


## Contributing

See the contributing guidelines within the repository.


## Acknowledgements

Lists the core team and contributors.


## Citing TinyTroupe

Follow the provided citation instructions for TinyTroupe.


## Legal Disclaimer

TinyTroupe is for research and simulation only.  Do not use for direct decision-making.  Generated outputs are not endorsements from Microsoft.


## Trademarks

Adheres to Microsoft's trademark and brand guidelines.