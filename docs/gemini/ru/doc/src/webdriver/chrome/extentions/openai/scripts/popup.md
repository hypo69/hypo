# Документация для popup.js

## Обзор

Файл `popup.js` содержит JavaScript-код, реализующий пользовательский интерфейс и логику взаимодействия с API для выбора и отправки запросов к модели OpenAI через сервер FastAPI.  Код использует AngularJS для управления DOM и AJAX запросы для взаимодействия с сервером.

## Оглавление

* [Функции](#функции)


## Функции

### `loadAssistants`

**Описание**: Функция загружает список доступных ассистентов с сервера.

**Параметры**:
Нет.

**Возвращает**:
-  Нет (выполняет асинхронный запрос).


**Вызывает исключения**:
-  Любые ошибки при отправке или обработке запроса к серверу. Ошибка обрабатывается в блоке `catch`.

### `sendMessage`

**Описание**: Функция отправляет сообщение модели OpenAI на сервер.

**Параметры**:
- Нет.

**Возвращает**:
-  Нет (выполняет асинхронный запрос).


**Вызывает исключения**:
-  Любые ошибки при отправке или обработке запроса к серверу.  Ошибка обрабатывается в блоке `catch`.  Возможные ошибки включают проблемы с подключением к серверу или неправильный формат ответа.

```
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