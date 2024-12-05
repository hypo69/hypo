rst
How to use the OpenAI Model Interaction HTML Page
=========================================================================================

Description
-------------------------
This code creates an HTML page for interacting with an OpenAI model.  It allows users to submit messages and (optionally) system instructions to the model and display the response.  Additionally, it provides a feature to train the model using CSV training data. The page utilizes AngularJS for client-side handling and makes API calls to the backend (`/ask` and `/train`) to perform the model interaction and training.

Execution steps
-------------------------
1. **Load the HTML page:** Open the `index.html` file in a web browser.

2. **Enter a message:**  Type a message into the "Message" input field.

3. **(Optional) Enter a system instruction:** If needed, type a system instruction into the "System Instruction (optional)" input field.

4. **Click "Ask Model":**  Click the "Ask Model" button.  This sends the message and system instruction (if provided) to the backend for processing by the OpenAI model.

5. **View the response:** The response from the OpenAI model will be displayed in the "Response" section below the input fields.  If there's an error during the API call, an error message will be displayed.

6. **Train the model:**
   a. Enter training data (CSV) into the "Training Data" textarea.
   b. Click "Train Model."  This sends the training data to the backend for model training.
   c. The training job ID will be displayed in the "Training Job ID" section.  If there's an error, an error message will be displayed.

Usage example
-------------------------
.. code-block:: html+javascript
    
    <!-- HTML part of the interaction -->
    <div class="form-group">
        <label for="message">Message</label>
        <input type="text" class="form-control" id="message" ng-model="ctrl.message" placeholder="Enter your message">
    </div>
    
    <button class="btn btn-primary" ng-click="ctrl.askModel()">Ask Model</button>

    <!-- JavaScript part (AngularJS controller) -->
    <script>
        angular.module('openaiApp', []).controller('MainController', ['$http', function($http) {
            var vm = this;
            vm.message = '';
            vm.response = '';
            
            vm.askModel = function() {
                $http.post('/ask', {
                    message: vm.message,
                }).then(function(response) {
                    vm.response = response.data.response;
                }, function(error) {
                    vm.response = 'Error: ' + error.data.detail;
                });
            };
        }]);
    </script>

**Explanation of the example:**

This code snippet shows a part of the HTML for message input and the corresponding JavaScript code (AngularJS controller).
It demonstrates how to use the `ng-model` directive to bind the input field with a controller variable (`vm.message`), and the `ng-click` directive to trigger a function (`vm.askModel`) on button click. The `$http.post` function sends a POST request to `/ask` (backend API endpoint) with the user's message and handles the response or any errors that may occur.