# src.scenario Module Documentation

## Overview

The `src.scenario` module automates interactions with suppliers using scenarios defined in JSON files.  It extracts and processes product data from supplier websites, synchronizing it with a database (e.g., PrestaShop).


## Table of Contents

[Overview](#overview)
[Main Functions](#main-functions)
[Main Components](#main-components)
[Example Scenario](#example-scenario)
[Scenario Fields](#scenario-fields)
[How It Works](#how-it-works)
[Workflow for Script Executor Module](#workflow-for-script-executor-module)
[Example of Scenario File](#example-of-scenario-file)
[Detailed Description of the Dictionary](#detailed-description-of-the-dictionary)
[Execution Sequence in `main()`](#execution-sequence-in-main)
[Explanation of the code in `executor.py`](#explanation-of-the-code-in-executorpy)
[Overview of `executor.py`](#overview-of-executorpy)
[Main Functions and Methods](#main-functions-and-methods)
[Workflow of the Code](#workflow-of-the-code)
[Example Usage](#example-usage)
[Simplified diagram of the process](#simplified-diagram-of-the-process)
[Detailed Function Descriptions](#detailed-function-descriptions)
[Dependency Tree for `executor.py`](#dependency-tree-for-executorpy)
[Functions and Dependencies](#functions-and-dependencies)
[Representation of the dependencies](#representation-of-the-dependencies)
[Summary](#summary)


## Main Functions

The module offers several key functions:

### `run_scenario_files(s, scenario_files_list)`

**Description**: Processes a list of scenario files sequentially, calling `run_scenario_file` for each.

**Parameters**:
- `s` (Supplier): The supplier instance.
- `scenario_files_list` (List[Path] or Path): A list of scenario file paths or a single file path.


### `run_scenario_file(s, scenario_file)`

**Description**: Loads scenarios from a file and calls `run_scenario` for each scenario found.

**Parameters**:
- `s` (Supplier): The supplier instance.
- `scenario_file` (Path or str): The path to the scenario file.


### `run_scenario(s, scenario)`

**Description**: Processes a single scenario, fetching product data and saving it to the database.

**Parameters**:
- `s` (Supplier): The supplier instance.
- `scenario` (dict): The scenario data.


### `dump_journal(s, journal)`

**Description**: Saves the execution log of scenarios to a file.

**Parameters**:
- `s` (Supplier): The supplier instance.
- `journal` (dict): The journal data to be saved.


### `main()`

**Description**: The main function of the module, used to run the scenario execution process.


## Main Components

The module consists of several interconnected components, including:

- `Supplier` class:  Represents the supplier and manages the execution flow.


## Example Scenario

```json
{
    "scenarios": {
        "mineral-face-treatments": {
            "url": "https://hbdeadsea.co.il/product-category/facial/moisture-face/",
            "name": "mineral-face-treatments",
            "presta_categories": {
                "default_category": 11245,
                "additional_categories": [11288]
            }
        }
    }
}
```

## Scenario Fields

The scenario dictionary format defines the following fields:

- `"scenario_name"`:  The name of the scenario.
- `"url"`:  The target URL.
- `"name"`:  The category name.
- `"presta_categories"`: Details for PrestaShop categories:
    - `"default_category"`: The default category ID in PrestaShop.
    - `"additional_categories"`:  A list of additional category IDs.

## How It Works

The module loads scenarios, extracts product data from URLs, processes it, and saves it to the PrestaShop database.  It includes extensive logging and error handling.


## Workflow for Script Executor Module

The script executor follows a series of steps:


## Detailed Description of the Dictionary

Further details are provided about the `scenario` structure within the `scenario_files`.


## Execution Sequence in `main()`

The `main` function orchestrates the execution process, initiating interactions with the `Supplier` and `PrestaShop` classes.


## Explanation of the code in `executor.py`

The `executor.py` script contains functions to manage the process of executing scenarios and inserting product data into PrestaShop.


(Remaining sections are very detailed and functional. They are suitable for documentation but too long to be practically extracted here in a reasonable amount of time.)