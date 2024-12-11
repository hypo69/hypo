# Received Code

```html
## \file hypotez/src/fast_api/html/openai/index.html
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
""" module: src.fast_api.html.openai """
MODE = 'debug'
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

                vm.askModel = function() {
                    # Отправка запроса на сервер для получения ответа модели
                    $http.post('/ask', {
                        message: vm.message,
                        system_instruction: vm.systemInstruction
                    }).then(function(response) {
                        # Обработка успешного ответа
                        vm.response = response.data.response;
                    }, function(error) {
                        # Обработка ошибок
                        console.error('Error:', error);
                        # Обработка ошибки от сервера
                        vm.response = 'Error: ' + error.data.detail;
                        logger.error('Ошибка при запросе к модели:', error);
                    });
                };

                vm.trainModel = function() {
                    # Отправка запроса на сервер для обучения модели
                    $http.post('/train', {
                        data: vm.trainingData,
                        positive: true
                    }).then(function(response) {
                        # Обработка успешного ответа
                        vm.jobId = response.data.job_id;
                    }, function(error) {
                        # Обработка ошибок
                        console.error('Error:', error);
                        # Обработка ошибки от сервера
                        vm.jobId = 'Error: ' + error.data.detail;
                        logger.error('Ошибка при обучении модели:', error);
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

# Improved Code

```html
<!-- ... (HTML часть остается без изменений) -->

<script>
    angular.module('openaiApp', [])
        .controller('MainController', ['$http', 'logger', function($http, logger) {
            # Внедрение logger для обработки ошибок
            var vm = this;
            # ... (Другие переменные)
            vm.askModel = function() {
                $http.post('/ask', {
                    message: vm.message,
                    system_instruction: vm.systemInstruction
                }).then(function(response) {
                    # Обработка успешного ответа от сервера
                    vm.response = response.data.response;
                }).catch(function(error) {
                    # Обработка ошибок с использованием logger
                    logger.error('Ошибка при запросе к модели:', error);
                    vm.response = 'Error: ' + (error.data && error.data.detail ? error.data.detail : 'Unknown error');
                });
            };

            vm.trainModel = function() {
                $http.post('/train', {
                    data: vm.trainingData,
                    positive: true
                }).then(function(response) {
                    vm.jobId = response.data.job_id;
                }).catch(function(error) {
                    logger.error('Ошибка при обучении модели:', error);
                    vm.jobId = 'Error: ' + (error.data && error.data.detail ? error.data.detail : 'Unknown error');
                });
            };
        }]);
</script>
```

# Changes Made

*   Добавлен импорт `logger` из `src.logger.logger`:
    ```javascript
    angular.module('openaiApp', []).controller('MainController', ['$http', 'logger', function($http, logger) {
    ```
*   Заменены `console.error` на `logger.error` для логирования ошибок.
*   Добавлены обработчики ошибок `catch` вместо `then/catch` для более компактного кода и лучшей читаемости.
*   Добавлены более информативные сообщения об ошибках. Теперь они содержат информацию из `error.data.detail`, если она доступна, или сообщение 'Unknown error' в противном случае.
*   Изменены комментарии для лучшей ясности.

# FULL Code

```html
<!-- ... (HTML часть остается без изменений) -->

<script>
    angular.module('openaiApp', []).controller('MainController', ['$http', 'logger', function($http, logger) {
        var vm = this;
        vm.message = '';
        vm.systemInstruction = '';
        vm.trainingData = '';
        vm.response = '';
        vm.jobId = '';

        vm.askModel = function() {
            # Отправка запроса на сервер для получения ответа модели
            $http.post('/ask', {
                message: vm.message,
                system_instruction: vm.systemInstruction
            }).then(function(response) {
                # Обработка успешного ответа от сервера
                vm.response = response.data.response;
            }).catch(function(error) {
                # Обработка ошибок с использованием logger
                logger.error('Ошибка при запросе к модели:', error);
                vm.response = 'Error: ' + (error.data && error.data.detail ? error.data.detail : 'Unknown error');
            });
        };

        vm.trainModel = function() {
            # Отправка запроса на сервер для обучения модели
            $http.post('/train', {
                data: vm.trainingData,
                positive: true
            }).then(function(response) {
                vm.jobId = response.data.job_id;
            }).catch(function(error) {
                # Обработка ошибок с использованием logger
                logger.error('Ошибка при обучении модели:', error);
                vm.jobId = 'Error: ' + (error.data && error.data.detail ? error.data.detail : 'Unknown error');
            });
        };
    }]);
</script>
```