# System Instruction: mexiron

## Overview

This system instruction describes how to generate documentation for Python files related to computer component assembly. The documentation will include a detailed description of the build, translations of component names, and the creation of a JSON response.

## Classes

### `ComputerBuilderAssistant`

**Description**: This class is responsible for assembling a computer based on provided components. It determines the build type, generates descriptive titles and detailed descriptions in Hebrew and Russian, translates component names, and returns a JSON response in the specified format.

**Methods**:

- `generate_documentation(components)`:  Generates documentation based on the input components.

## Functions


### `determine_build_type(components)`

**Description**: Analyzes the provided components to determine the most suitable build type, considering the importance of each component (e.g., gaming, workstation, office). It returns a dictionary with build types and their associated confidence scores.

**Parameters**:
- `components (list):` A list of dictionaries, where each dictionary represents a component with its details (e.g., `product_title`, `product_description`).


**Returns**:
- `dict`: A dictionary containing build types and their confidence scores (e.g., `{"gaming": 0.9, "workstation": 0.1}`).


**Raises**:
- `TypeError`: if input is not a list of dictionaries.
- `ValueError`: if components list is empty.


### `translate_component(component, language)`

**Description**: Translates the name and description of a component into the specified language (Hebrew or Russian).

**Parameters**:
- `component (dict):` The component dictionary containing the name and description.
- `language (str):` The target language ("he" for Hebrew, "ru" for Russian).


**Returns**:
- `dict`: The translated component dictionary.

**Raises**:
- `TypeError`: if input is not a dictionary.
- `ValueError`: if language is invalid ("he" or "ru").



### `generate_build_description(components, build_type)`

**Description**: Generates a descriptive title and a detailed description of the computer build, tailored to the specified build type, in Hebrew and Russian.

**Parameters**:
- `components (list):` A list of dictionaries describing the computer components.
- `build_type (str)`: The build type (e.g., "gaming").


**Returns**:
- `dict`: A dictionary containing the generated title and descriptions in Hebrew and Russian.

**Raises**:
- `TypeError`: if input is not a list of dictionaries.
- `ValueError`: if build_type is invalid.




### `assemble_build_json(components, build_type)`

**Description**:  Assembles the JSON response for the computer build, including translations, descriptions, and build types.

**Parameters**:
- `components (list):` A list of dictionaries describing the computer components.
- `build_type (str)`: The build type (e.g., "gaming").


**Returns**:
- `dict`: A JSON-formatted dictionary containing the computer build data.


**Raises**:
- `TypeError`: if input is not a list of dictionaries.
- `ValueError`: if build_type is invalid.



## Table of Contents

- [Overview](#overview)
- [Classes](#classes)
    - [`ComputerBuilderAssistant`](#computerbuilderassistant)
- [Functions](#functions)
    - [`determine_build_type`](#determine-build-type)
    - [`translate_component`](#translate-component)
    - [`generate_build_description`](#generate-build-description)
    - [`assemble_build_json`](#assemble-build-json)