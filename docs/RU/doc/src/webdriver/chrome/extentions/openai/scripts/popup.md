# Документация popup.js

## Обзор

Файл `popup.js` содержит JavaScript код для Angular приложения, взаимодействующего с сервером FastAPI для получения и обработки ответов от моделей. Приложение предоставляет интерфейс для выбора ассистента и отправки запросов.

## Оглавление

* [Обзор](#обзор)
* [Функции](#функции)
    * [`loadAssistants`](#loadassistants)
    * [`sendMessage`](#sendMessage)


## Функции

### `loadAssistants`

**Описание**: Функция загружает список ассистентов с сервера.

**Параметры**:
Нет.

**Возвращает**:
- Нет. Обновляет массив `$scope.assistants`.


**Вызывает исключения**:
- Любые ошибки при выполнении `$http.get` запроса. Сообщение об ошибке выводится в консоль.


### `sendMessage`

**Описание**: Функция отправляет сообщение модели на сервер для получения ответа.

**Параметры**:
- Нет.


**Возвращает**:
- Нет. Обновляет `$scope.response` с ответом от сервера.


**Вызывает исключения**:
- Любые ошибки при выполнении `$http.post` запроса. Сообщение об ошибке выводится в консоль и `$scope.response` устанавливается в сообщение об ошибке.

```
```javascript
// Инициализируем Angular приложение
const app = angular.module('openaiApp', []);
```

**Описание**:  Инициализация Angular модуля `openaiApp`.


```javascript
// Контроллер для обработки логики
app.controller('MainController', function ($scope, $http) {
```

**Описание**: Определение контроллера `MainController` для управления логикой приложения.


```javascript
    $scope.message = '';
    $scope.response = '';
    $scope.assistants = [];
    $scope.selectedAssistant = null;
```

**Описание**:  Инициализация свойств для хранения сообщения, ответа, списка ассистентов и выбранного ассистента.


```javascript
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
```

```javascript

    // Загружаем список ассистентов при инициализации
    loadAssistants();
```

**Описание**:  Вызов функции `loadAssistants` для загрузки списка ассистентов при загрузке страницы.


```javascript
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

**Описание**: Функция `sendMessage` отправляет POST запрос на сервер с данными сообщения, инструкции и идентификатора ассистента для получения ответа.


```
```


```
```
```
```
```