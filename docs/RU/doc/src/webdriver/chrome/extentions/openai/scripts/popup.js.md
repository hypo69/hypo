# Документация для `popup.js`

## Обзор

Этот файл содержит JavaScript-код для Angular-приложения, которое взаимодействует с FastAPI-сервером для отправки сообщений и получения ответов от языковой модели, а также для загрузки списка ассистентов.

## Оглавление
- [Обзор](#обзор)
- [Angular-модуль](#angular-модуль)
- [Контроллер `MainController`](#контроллер-maincontroller)
    - [Переменные контроллера](#переменные-контроллера)
    - [Функция `loadAssistants`](#функция-loadassistants)
    - [Функция `sendMessage`](#функция-sendmessage)

## Angular-модуль

### `openaiApp`

**Описание**: Инициализация Angular-модуля с именем `openaiApp`. Этот модуль используется для управления компонентами и функциональностью приложения.

```javascript
const app = angular.module('openaiApp', []);
```

## Контроллер `MainController`

**Описание**: Angular-контроллер `MainController` управляет логикой взаимодействия с пользовательским интерфейсом, отправкой сообщений и обработкой ответов от FastAPI-сервера.

```javascript
app.controller('MainController', function ($scope, $http) {
    // ...
});
```

### Переменные контроллера

**Описание**: Переменные, используемые в контроллере `MainController`, которые связаны с моделью данных Angular.

- `$scope.message` (string): Содержит сообщение, введенное пользователем. Изначально пусто.
- `$scope.response` (string): Содержит ответ от сервера. Изначально пусто.
- `$scope.assistants` (Array): Массив объектов, представляющих доступных ассистентов. Изначально пуст.
- `$scope.selectedAssistant` (Object): Объект выбранного ассистента. Изначально `null`.

### Функция `loadAssistants`

**Описание**: Функция отправляет GET-запрос к серверу для загрузки списка ассистентов.

```javascript
function loadAssistants() {
    const url = 'http://localhost:8000/assistants'; // URL для запроса списка ассистентов
    alert("ASST")
    $http.get(url)
        .then(function (response) {
            $scope.assistants = response.data;  // Установка списка ассистентов в scope
        })
        .catch(function (error) {
            console.error('Ошибка загрузки ассистентов:', error); // Обработка ошибок
        });
}
```

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет явного возврата. Изменяет `$scope.assistants` при успешном запросе.

**Вызывает исключения**:
- В случае ошибки выводит сообщение в консоль.

### Функция `sendMessage`

**Описание**: Функция отправляет POST-запрос к серверу с сообщением пользователя и данными ассистента для получения ответа.

```javascript
$scope.sendMessage = function () {
    const url = 'http://localhost:8000/ask';  // URL для отправки сообщения
    const data = {
        message: $scope.message,
        system_instruction: "You are a helpful assistant.", // Инструкция для системы
        assistant_id: $scope.selectedAssistant.id // ID выбранного ассистента
    };

    $http.post(url, data)
        .then(function (response) {
            $scope.response = response.data.response; // Установка ответа сервера в scope
        })
        .catch(function (error) {
            console.error('Ошибка:', error); // Вывод ошибки в консоль
            $scope.response = 'Произошла ошибка. Попробуйте позже.'; // Сообщение об ошибке пользователю
        });
};
```

**Параметры**:
- Нет параметров.

**Возвращает**:
- Нет явного возврата. Изменяет `$scope.response` при успешном или неудачном запросе.

**Вызывает исключения**:
- В случае ошибки выводит сообщение в консоль и отображает сообщение об ошибке пользователю.