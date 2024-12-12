## Улучшенный код
```html
<!--  
    Модуль для интерактивного взаимодействия с OpenAI моделями через веб-интерфейс.
    ================================================================================
    
    Этот модуль представляет собой HTML-страницу с использованием AngularJS для создания
    интерактивного веб-интерфейса, позволяющего отправлять запросы к моделям OpenAI и
    обучать модели с предоставленными данными.
    
    Используется Bootstrap для стилизации и AngularJS для управления взаимодействием с пользователем.
    
    Пример использования
    --------------------
    
    Откройте `index.html` в веб-браузере. Используйте текстовые поля и кнопки для взаимодействия с OpenAI.
    
    .. code-block:: html
    
        <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>OpenAI Model Interaction</title>
            </head>
            <body>
                <!-- ... -->
            </body>
        </html>
-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OpenAI Model Interaction</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://code.angularjs.org/1.8.2/angular.min.js"></script>
</head>
<body ng-app="openaiApp" ng-controller="MainController as ctrl">
    <div class="container mt-5">
        <h1 class="text-center">OpenAI Model Interaction</h1>

        <div class="form-group">
            <label for="message">Message</label>
            <input type="text" class="form-control" id="message" ng-model="ctrl.message" placeholder="Enter your message">
        </div>

        <div class="form-group">
            <label for="instruction">System Instruction (optional)</label>
            <input type="text" class="form-control" id="instruction" ng-model="ctrl.systemInstruction" placeholder="Enter system instruction">
        </div>

        <button class="btn btn-primary" ng-click="ctrl.askModel()">Ask Model</button>

        <div class="mt-4">
            <h5>Response:</h5>
            <pre>{{ ctrl.response }}</pre>
        </div>

        <hr>

        <h2>Train Model</h2>
        <div class="form-group">
            <label for="data">Training Data (CSV string)</label>
            <textarea class="form-control" id="data" ng-model="ctrl.trainingData" rows="3" placeholder="Enter CSV data"></textarea>
        </div>

        <button class="btn btn-success" ng-click="ctrl.trainModel()">Train Model</button>

        <div class="mt-4">
            <h5>Training Job ID:</h5>
            <pre>{{ ctrl.jobId }}</pre>
        </div>
    </div>

    <script>
        angular.module('openaiApp', [])
            .controller('MainController', ['$http', function($http) {
                var vm = this;
                vm.message = '';
                vm.systemInstruction = '';
                vm.trainingData = '';
                vm.response = '';
                vm.jobId = '';
                
                /**
                 * Отправляет запрос к OpenAI модели и отображает ответ.
                 *
                 *  Отправляет POST-запрос на эндпоинт '/ask' с сообщением пользователя и системной инструкцией.
                 *  В случае успеха обновляет поле `response` для отображения ответа модели.
                 *  В случае ошибки выводит сообщение об ошибке в консоль и устанавливает поле `response` на сообщение об ошибке.
                 */
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
                
                /**
                 *  Отправляет данные для обучения OpenAI модели и отображает идентификатор задания.
                 *
                 *  Отправляет POST-запрос на эндпоинт '/train' с данными обучения.
                 *  В случае успеха обновляет поле `jobId` для отображения идентификатора задания.
                 *  В случае ошибки выводит сообщение об ошибке в консоль и устанавливает поле `jobId` на сообщение об ошибке.
                 */
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
            }]);
    </script>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```
## Внесённые изменения
*   Добавлены docstring в формате reStructuredText к модулю, функциям.
*   Добавлены комментарии к блокам кода.
*   Удалено неиспользуемое `MODE = 'debug'`.

## Оптимизированный код
```html
<!--  
    Модуль для интерактивного взаимодействия с OpenAI моделями через веб-интерфейс.
    ================================================================================
    
    Этот модуль представляет собой HTML-страницу с использованием AngularJS для создания
    интерактивного веб-интерфейса, позволяющего отправлять запросы к моделям OpenAI и
    обучать модели с предоставленными данными.
    
    Используется Bootstrap для стилизации и AngularJS для управления взаимодействием с пользователем.
    
    Пример использования
    --------------------
    
    Откройте `index.html` в веб-браузере. Используйте текстовые поля и кнопки для взаимодействия с OpenAI.
    
    .. code-block:: html
    
        <html>
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>OpenAI Model Interaction</title>
            </head>
            <body>
                <!-- ... -->
            </body>
        </html>
-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OpenAI Model Interaction</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <script src="https://code.angularjs.org/1.8.2/angular.min.js"></script>
</head>
<body ng-app="openaiApp" ng-controller="MainController as ctrl">
    <div class="container mt-5">
        <h1 class="text-center">OpenAI Model Interaction</h1>

        <div class="form-group">
            <label for="message">Message</label>
            <input type="text" class="form-control" id="message" ng-model="ctrl.message" placeholder="Enter your message">
        </div>

        <div class="form-group">
            <label for="instruction">System Instruction (optional)</label>
            <input type="text" class="form-control" id="instruction" ng-model="ctrl.systemInstruction" placeholder="Enter system instruction">
        </div>

        <button class="btn btn-primary" ng-click="ctrl.askModel()">Ask Model</button>

        <div class="mt-4">
            <h5>Response:</h5>
            <pre>{{ ctrl.response }}</pre>
        </div>

        <hr>

        <h2>Train Model</h2>
        <div class="form-group">
            <label for="data">Training Data (CSV string)</label>
            <textarea class="form-control" id="data" ng-model="ctrl.trainingData" rows="3" placeholder="Enter CSV data"></textarea>
        </div>

        <button class="btn btn-success" ng-click="ctrl.trainModel()">Train Model</button>

        <div class="mt-4">
            <h5>Training Job ID:</h5>
            <pre>{{ ctrl.jobId }}</pre>
        </div>
    </div>

    <script>
        angular.module('openaiApp', [])
            .controller('MainController', ['$http', function($http) {
                var vm = this;
                vm.message = '';
                vm.systemInstruction = '';
                vm.trainingData = '';
                vm.response = '';
                vm.jobId = '';
                
                /**
                 * Отправляет запрос к OpenAI модели и отображает ответ.
                 *
                 *  Отправляет POST-запрос на эндпоинт '/ask' с сообщением пользователя и системной инструкцией.
                 *  В случае успеха обновляет поле `response` для отображения ответа модели.
                 *  В случае ошибки выводит сообщение об ошибке в консоль и устанавливает поле `response` на сообщение об ошибке.
                 */
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
                
                /**
                 *  Отправляет данные для обучения OpenAI модели и отображает идентификатор задания.
                 *
                 *  Отправляет POST-запрос на эндпоинт '/train' с данными обучения.
                 *  В случае успеха обновляет поле `jobId` для отображения идентификатора задания.
                 *  В случае ошибки выводит сообщение об ошибке в консоль и устанавливает поле `jobId` на сообщение об ошибке.
                 */
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
            }]);
    </script>

    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>