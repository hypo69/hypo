# hypotez/src/fast_api/gemini.py

## Overview

This module defines a FastAPI application for interacting with a Google Generative AI model.  It exposes an endpoint `/ask` that accepts a prompt as input and returns a generated response from the AI model.

## Table of Contents

* [Overview](#overview)
* [Functions](#functions)
    * [`ask`](#ask)


## Functions

### `ask`

**Description**: This function handles incoming requests to the `/ask` endpoint. It extracts the prompt from the request body, validates its presence, and then calls the `ai_model.ask()` method to generate a response.

**Parameters**:
- `data` (dict): The JSON data from the request body.

**Returns**:
- `jsonify({"reply": reply})` (dict): A JSON response containing the generated reply if successful.

**Raises**:
- `Exception`:  An exception is raised during the `ai_model.ask()` call and this method returns an error message wrapped in a JSON response.


```
```python
def ask():
    """
    Handles incoming requests to the /ask endpoint.

    Args:
        data (dict): The JSON data from the request body.

    Returns:
        jsonify({"reply": reply}): A JSON response containing the generated reply if successful.

    Raises:
        Exception: An exception is raised during the ai_model.ask() call. This method returns an error message wrapped in a JSON response.
    """
    data = request.get_json()
    prompt = data.get('prompt')

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        reply = ai_model.ask(prompt)
        return jsonify({"reply": reply})
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
```
```