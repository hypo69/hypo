# <input code>

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

# <algorithm>

**Шаг 1:** Инициализация Angular приложения.
   - Создается модуль `openaiApp`.
**Пример:** `const app = angular.module('openaiApp', []);`

**Шаг 2:** Определение контроллера `MainController`.
   - Объявляются переменные `$scope.message`, `$scope.response`, `$scope.assistants`, `$scope.selectedAssistant`.
   - Эти переменные будут хранить данные для ввода пользователя, ответа модели и списка ассистентов соответственно.
**Пример:** `$scope.message = '';`
**Шаг 3:** Функция `loadAssistants`.
   - Запрос GET на `http://localhost:8000/assistants`.
   - Обработка ответа:
      - `$scope.assistants` заполняется данными из ответа сервера.
   - Обработка ошибок: выводит ошибки в консоль.
**Пример:**
`$http.get(url).then(...).catch(...)`

**Шаг 4:** Загрузка списка ассистентов.
   - Вызывается функция `loadAssistants()` при инициализации контроллера.
**Пример:** `loadAssistants();`

**Шаг 5:** Функция `sendMessage`.
   - Создание объекта `data` с данными для отправки на сервер.
      - `message`: Текст сообщения пользователя.
      - `system_instruction`: Настройка для модели.
      - `assistant_id`: ID выбранного ассистента.
   - POST-запрос на `http://localhost:8000/ask` с данными `data`.
   - Обработка ответа:
      - `$scope.response` заполняется данными из ответа сервера.
   - Обработка ошибок: выводит ошибки в консоль, устанавливает сообщение об ошибке для пользователя.
**Пример:**
`$http.post(url, data).then(...).catch(...)`


# <mermaid>

```mermaid
graph TD
    A[angular.module('openaiApp')] --> B{MainController};
    B --> C{loadAssistants()};
    C --> D{$http.get('/assistants')};
    D --success--> E[$scope.assistants = response.data];
    D --error--> F[console.error];
    B --> G{$scope.sendMessage()};
    G --> H{$http.post('/ask', data)};
    H --success--> I[$scope.response = response.data.response];
    H --error--> J[console.error, $scope.response = 'Произошла ошибка'];

    subgraph FastAPI
        O[http://localhost:8000/assistants] --> D;
        P[http://localhost:8000/ask] --> H;
    end

    style B fill:#ccf;
    style C fill:#ccf;
    style G fill:#ccf;
```

# <explanation>

**Импорты:**  Нет явных импортов из других модулей, но подразумевается использование AngularJS и `$http` для запросов.  Подразумевается подключение `$http` к AngularJS.

**Классы:** Нет классов в строгом смысле слова. Есть только контроллер `MainController`, определяемый в контексте AngularJS.

**Функции:**

*   `loadAssistants()`: Загружает список ассистентов с сервера.
    *   Аргументы: нет.
    *   Возвращаемое значение: нет.
    *   Примеры: Запрос на `http://localhost:8000/assistants`
*   `$scope.sendMessage()`: Отправляет сообщение модели.
    *   Аргументы: нет.
    *   Возвращаемое значение: нет.
    *   Примеры: Создание объекта данных `data` для `http://localhost:8000/ask`.

**Переменные:**

*   `$scope.message`: Хранит введенное сообщение пользователя. Тип - строка.
*   `$scope.response`: Хранит ответ модели. Тип - строка.
*   `$scope.assistants`: Список доступных ассистентов. Тип - массив.
*   `$scope.selectedAssistant`: Выбранный ассистент. Тип - объект.
*   `url`: Адрес API-эндпоинтов. Тип - строка.

**Возможные ошибки и улучшения:**

*   **Отсутствие валидации:** Код не проверяет корректность данных, получаемых от сервера. Необходимо добавить обработку различных вариантов ответов сервера (например, код ошибки, некорректный формат данных).
*   **Хэндлинг ошибок:** Обработка ошибок `$http`-запросов могла бы быть более подробной.
*   **Переменные окружения:** Использование `'http://localhost:8000'` для адресов API — не лучший подход. Лучше использовать переменные окружения, чтобы избежать жёсткой привязки к локальному серверу.
*   **Обработка `selectedAssistant`:** Предполагается, что `$scope.selectedAssistant` содержит объект с `id` свойством. Если это не так, код может вызвать ошибку.


**Взаимосвязи с другими частями проекта:**

Код взаимодействует с сервером (FastAPI), который отвечает за получение списка ассистентов и обработку сообщений. Поэтому, для работы, необходима корректная работа серверной части проекта, которая обрабатывает запросы `http://localhost:8000/assistants` и `http://localhost:8000/ask`.