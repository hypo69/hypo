# hypotez/src/fast_api/html/openai/index.html

## Overview

This HTML file provides a user interface for interacting with an OpenAI model.  It allows users to input messages and system instructions, and displays the model's response.  It also includes functionality to train the model with custom data.

## Table of Contents

* [Overview](#overview)
* [HTML Structure](#html-structure)
* [JavaScript Functionality](#javascript-functionality)
    * [`askModel()`](#askmodel)
    * [`trainModel()`](#trainmodel)


## HTML Structure

The HTML structure utilizes Bootstrap for styling and AngularJS for managing the user interface and data binding.

### Input Fields

The page includes input fields for:

*   `Message`:  The user's input.
*   `System Instruction (optional)`:  Optional instructions to the model.
*   `Training Data (CSV string)`: Data used to train the model.


### Buttons

Buttons for:

*   `Ask Model`: Submits the message and system instruction to the backend.
*   `Train Model`: Submits the training data to the backend.


### Output Display

The page displays the following:

*   `Response`:  Displays the model's response.
*   `Training Job ID`:  Displays the training job ID if a training request is successful.



## JavaScript Functionality

This section describes the JavaScript functions responsible for interacting with the backend.


### `askModel()`

```javascript
vm.askModel = function() {
    $http.post('/ask', {
        message: vm.message,
        system_instruction: vm.systemInstruction
    }).then(function(response) {
        vm.response = response.data.response;
    }, function(error) {
        console.error('Error:', error);
        vm.response = 'Error: ' + error.data.detail;
    });
};
```

**Description**: This function sends a POST request to the `/ask` endpoint with the user's message and optional system instruction.  It handles success and error responses.

**Parameters**:
*   `vm.message` (str): The user's message to be sent to the model.
*   `vm.systemInstruction` (str, optional): Optional system instructions for the model. Defaults to empty string.


**Returns**:
*   N/A


**Raises**:
*   Error: If the backend request encounters an error, it displays an appropriate error message.


### `trainModel()`

```javascript
vm.trainModel = function() {
    $http.post('/train', {
        data: vm.trainingData,
        positive: true
    }).then(function(response) {
        vm.jobId = response.data.job_id;
    }, function(error) {
        console.error('Error:', error);
        vm.jobId = 'Error: ' + error.data.detail;
    });
};
```

**Description**: This function sends a POST request to the `/train` endpoint with the training data.

**Parameters**:
*   `vm.trainingData` (str): The training data as a CSV string.
*   `positive` (bool, optional):  A boolean indicating that the data should be used for training. Defaults to true.


**Returns**:
*   N/A


**Raises**:
*   Error: If the backend request encounters an error, it displays an appropriate error message.