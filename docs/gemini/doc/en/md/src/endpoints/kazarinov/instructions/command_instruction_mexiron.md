# command_instruction_mexiron.md

## Overview

This module provides instructions for generating documentation for Python files related to computer building. It focuses on creating detailed documentation for functions, classes, and methods, adhering to Markdown formatting standards, including a table of contents (TOC) for navigation.  The documentation is designed to be comprehensive and easily understandable, providing clear explanations of parameters, return values, and potential exceptions.


## Table of Contents

* [Introduction](#introduction)
* [Prompt for Gemini AI: Assembling a Computer](#prompt-for-gemini-ai-assembling-a-computer)
* [Improving Prompt for More Accurate Build Classification](#improving-prompt-for-more-accurate-build-classification)
* [Example Output](#example-output)
* [Key Considerations](#key-considerations)

## Introduction

This module aims to improve the quality of documentation for computer building prompts by leveraging accurate classification of build types and providing comprehensive descriptions in multiple languages (Hebrew and Russian). It leverages component-specific weighting, hierarchical classification, and user preference considerations to enhance accuracy.


## Prompt for Gemini AI: Assembling a Computer

### Description

This prompt section defines the role of a computer builder assistant. It specifies the input and output formats, including example JSON structures, and emphasizes the need for accurate translation into Hebrew and Russian.


### Example Input

```json
[
  {
    "product_id": "<leave as is>",
    "product_title": "<component name>",
    "product_description": "<description and specs>",
    "image_local_saved_path": "<leave as is>"
  },
  {
    "product_id": "<leave as is>",
    "product_title": "<component name>",
    "product_description": "<description and specs>",
    "image_local_saved_path": "<leave as is>"
  }
]
```


### Example Output

```json
{
  "he": {
    "build_types": {
      "gaming": 0.9,
      "workstation": 0.1
    },
    "title": "️ <Your build title>",
    "description": " <Your build description>",
    // ... rest of the structure
  },
  "ru": {
    "build_types": {
      "gaming": 0.9,
      "workstation": 0.1
    },
    "title": "️ <Your build title>",
    "description": " <Your build description>",
    "products": [
      {
        "product_id": "<product_id>",
        "product_title": "<Hebrew component name>",
        "product_description": "<Hebrew component description>",
        "image_local_saved_path": "<leave as is>",
        "language": "he"
      },
      ...
    ]
  }
}
```



## Improving Prompt for More Accurate Build Classification

### Description

This section refines the prompt, focusing on accurate build type determination by providing multiple options with associated confidence scores. Component-specific weighting, hierarchical classification, and contextual understanding are emphasized for enhanced accuracy.


### Example Input

```json
// ... (same as previous example)
```


### Example Output

```json
{
  "build_types": {
    "gaming": 0.8,
    "content_creation": 0.15,
    "workstation": 0.05
  },
  // ... rest of the output
}
```


## Example Output

### Description

Provides sample output demonstrating the expected JSON structure, including translated titles, descriptions, and product details.


## Key Considerations

### Description

Outlines critical factors for accurate build classification, including understanding component specifications, generating comprehensive descriptions, accurate translations, adhering to formatting, and handling different component combinations.


## Functions


### `generate_documentation`

**Description**: This function generates documentation for the given Python file.

**Parameters**:
- `input_file_path` (str): The path to the Python file.
- `output_file_path` (str, optional): The path to save the generated documentation. Defaults to `None`.

**Returns**:
- `str`: The generated documentation in Markdown format.

**Raises**:
- `FileNotFoundError`: If the input file does not exist.
- `TypeError`: If input is not a string.



```
```
```
```


```
```
```
```

```
```


```