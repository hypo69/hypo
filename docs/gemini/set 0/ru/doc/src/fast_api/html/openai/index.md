# Документация для файла hypotez/src/fast_api/html/openai/index.html

## Обзор

Файл `index.html` представляет собой страницу взаимодействия с моделью OpenAI, реализованную с использованием AngularJS и FastAPI.  Страница предоставляет интерфейс для отправки запросов к модели, а также для обучения модели с помощью CSV данных.


## Оглавление

- [Доступные элементы](#доступные-элементы)
- [Функциональность](#функциональность)
  - [Запрос модели](#запрос-модели)
  - [Обучение модели](#обучение-модели)
- [Использование](#использование)
- [Примеры](#примеры)


## Доступные элементы

Страница содержит следующие элементы:

- Форму для ввода сообщения
- Форму для ввода инструкций для модели (необязательно)
- Кнопку "Запросить модель"
- Текстовую область для ввода данных CSV (для обучения модели)
- Кнопку "Обучить модель"
- Область для вывода ответа модели
- Область для вывода ID задачи обучения.


## Функциональность

### Запрос модели

Пользователь может ввести сообщение и (необязательно) инструкцию для модели и нажать кнопку "Запросить модель".  Это вызывает POST запрос к `/ask` endpoint FastAPI, который отправляет запрос к модели OpenAI и возвращает ответ.

### Обучение модели

Пользователь может ввести данные в формате CSV в текстовую область и нажать кнопку "Обучить модель". Это вызывает POST запрос к `/train` endpoint FastAPI, который использует эти данные для обучения модели. Возвращаемый ID задачи указывает на текущий процесс обучения.


## Использование

1. Откройте страницу `index.html` в браузере.
2. Введите сообщение в поле "Сообщение".
3. (Необязательно) Введите инструкции в поле "Инструкция для системы".
4. Нажмите кнопку "Запросить модель".
5. Для обучения модели, введите данные в формате CSV в текстовую область "Данные для обучения".
6. Нажмите кнопку "Обучить модель".

## Примеры

**Пример запроса модели:**

Пользователь вводит сообщение "Привет, мир!".  Система отправляет этот запрос на сервер FastAPI, который отправляет запрос к модели OpenAI и возвращает ответ.  Ответ отображается в области "Ответ".


**Пример обучения модели:**

Пользователь вводит данные CSV в формате:

```
Название;Описание
Книга;Текстовая информация о книге.
Статья;Текстовая информация об статье.
```

Система обучает модель на основе этих данных. ID задачи обучения будет отображен в соответствующей области.


## AngularJS Контроллер (MainController)

Файл `index.html` использует AngularJS для управления данными и взаимодействием с сервером.  Контроллер `MainController` обрабатывает события:

- `vm.askModel`: Отправляет POST запрос к `/ask` с сообщением и инструкцией. Обрабатывает ответ и выводит его. Обрабатывает ошибки, отображая соответствующие сообщения об ошибках.
- `vm.trainModel`: Отправляет POST запрос к `/train` с данными CSV для обучения. Обрабатывает ответ и выводит ID задачи обучения. Обрабатывает ошибки, отображая сообщения об ошибках.

```javascript
angular.module('openaiApp', [])
    .controller('MainController', ['$http', function($http) {
        // ... (Остальной код контроллера)
    }]);
```

**Замечание:**  Данная документация фокусируется на HTML-части.  Документирование FastAPI endpoints (`/ask` и `/train`) должно быть сделано в соответствующей документации для Python-файлов, которые реализуют эти эндопоинты.