# Received Code

```javascript
// Инициализируем Angular приложение
const app = angular.module('openaiApp', []);

// Контроллер для обработки логики
app.controller('MainController', function ($scope, $http) {
    $scope.message = '';
    $scope.response = '';
    $scope.assistants = [];
    $scope.selectedAssistant = null;

    // Функция для получения списка ассистентов
    function loadAssistants() {
        const url = 'http://localhost:8000/assistants';  // Создай новый endpoint для получения списка ассистентов
        alert("ASST")
        $http.get(url)
            .then(function (response) {
                $scope.assistants = response.data;  // Список ассистентов
            })
            .catch(function (error) {
                console.error('Ошибка загрузки ассистентов:', error);
            });
    }

    // Загружаем список ассистентов при инициализации
    loadAssistants();

    // Функция для отправки сообщения модели
    $scope.sendMessage = function () {
        const url = 'http://localhost:8000/ask';  // Адрес FastAPI сервера

        const data = {
            message: $scope.message,
            system_instruction: "You are a helpful assistant.",
            assistant_id: $scope.selectedAssistant.id  // Добавляем ID ассистента
        };

        // Отправка POST-запроса через $http (AJAX)
        $http.post(url, data)
            .then(function (response) {
                $scope.response = response.data.response;  // Ответ от сервера
            })
            .catch(function (error) {
                console.error('Ошибка:', error);
                $scope.response = 'Произошла ошибка. Попробуйте позже.';
            });
    };
});
```

# Improved Code

```javascript
// Модуль для работы с интерфейсом OpenAI
// ========================================
// Этот модуль предоставляет функции для взаимодействия с OpenAI API через Angular.

// Инициализация Angular модуля
const app = angular.module('openaiApp', []);

// Контроллер для обработки логики приложения
app.controller('MainController', function ($scope, $http) {
    """
    Контроллер для взаимодействия с интерфейсом OpenAI.
    
    Атрибуты:
        message (str): Введенное сообщение.
        response (str): Ответ от модели.
        assistants (list): Список доступных ассистентов.
        selectedAssistant (object): Выбранный ассистент.
    """
    $scope.message = '';
    $scope.response = '';
    $scope.assistants = [];
    $scope.selectedAssistant = null;

    /**
     * Загрузка списка ассистентов.
     *
     * Запрашивает список ассистентов с сервера.
     * Обрабатывает ошибки с помощью логирования.
     */
    async function loadAssistants() {
        try {
            const url = 'http://localhost:8000/assistants';
            const response = await $http.get(url);
            $scope.assistants = response.data;
        } catch (error) {
            from src.logger import logger
            logger.error('Ошибка загрузки ассистентов:', error);
        }
    }

    // Вызов функции загрузки ассистентов при инициализации контроллера
    loadAssistants();


    /**
     * Отправка сообщения модели.
     *
     * Отправляет сообщение модели на сервер и обрабатывает ответ.
     * Выполняет проверку корректности выбранного ассистента.
     */
    $scope.sendMessage = function () {
        if (!$scope.selectedAssistant) {
            logger.error('Не выбран ассистент.');
            $scope.response = 'Необходимо выбрать ассистента.';
            return;
        }

        try {
            const url = 'http://localhost:8000/ask';
            const data = {
                message: $scope.message,
                system_instruction: "You are a helpful assistant.",
                assistant_id: $scope.selectedAssistant.id
            };
            const response = $http.post(url, data);
            $scope.response = response.data.response;
        } catch (error) {
            logger.error('Ошибка отправки сообщения:', error);
            $scope.response = 'Произошла ошибка. Попробуйте позже.';
        }
    };
});
```

# Changes Made

*   Добавлен импорт `logger` из `src.logger`.
*   Замена `$http.get` на `async/await`.
*   Добавлена обработка ошибок с помощью `try...catch` и `logger.error`.
*   Добавлены комментарии в формате RST ко всем функциям, методам и переменным.
*   Изменен способ обработки ошибок в `sendMessage`.
*   Добавлена проверка на выбор ассистента в функции `sendMessage`.
*   Улучшены комментарии.


# FULL Code

```javascript
// Модуль для работы с интерфейсом OpenAI
// ========================================
// Этот модуль предоставляет функции для взаимодействия с OpenAI API через Angular.

// Инициализация Angular модуля
const app = angular.module('openaiApp', []);

// Контроллер для обработки логики приложения
app.controller('MainController', function ($scope, $http) {
    """
    Контроллер для взаимодействия с интерфейсом OpenAI.
    
    Атрибуты:
        message (str): Введенное сообщение.
        response (str): Ответ от модели.
        assistants (list): Список доступных ассистентов.
        selectedAssistant (object): Выбранный ассистент.
    """
    $scope.message = '';
    $scope.response = '';
    $scope.assistants = [];
    $scope.selectedAssistant = null;

    /**
     * Загрузка списка ассистентов.
     *
     * Запрашивает список ассистентов с сервера.
     * Обрабатывает ошибки с помощью логирования.
     */
    async function loadAssistants() {
        try {
            const url = 'http://localhost:8000/assistants';
            const response = await $http.get(url);
            $scope.assistants = response.data;
        } catch (error) {
            from src.logger import logger
            logger.error('Ошибка загрузки ассистентов:', error);
        }
    }

    // Вызов функции загрузки ассистентов при инициализации контроллера
    loadAssistants();


    /**
     * Отправка сообщения модели.
     *
     * Отправляет сообщение модели на сервер и обрабатывает ответ.
     * Выполняет проверку корректности выбранного ассистента.
     */
    $scope.sendMessage = function () {
        if (!$scope.selectedAssistant) {
            from src.logger import logger
            logger.error('Не выбран ассистент.');
            $scope.response = 'Необходимо выбрать ассистента.';
            return;
        }

        try {
            const url = 'http://localhost:8000/ask';
            const data = {
                message: $scope.message,
                system_instruction: "You are a helpful assistant.",
                assistant_id: $scope.selectedAssistant.id
            };
            const response = $http.post(url, data);
            $scope.response = response.data.response;
        } catch (error) {
            from src.logger import logger
            logger.error('Ошибка отправки сообщения:', error);
            $scope.response = 'Произошла ошибка. Попробуйте позже.';
        }
    };
});