# `chat.html`

## Обзор

Файл `chat.html` представляет собой HTML-шаблон для веб-чата Kazarinov AI. Он включает в себя пользовательский интерфейс для ввода сообщений и отображения истории чата. Этот файл использует Bootstrap для стилизации и jQuery для обработки AJAX-запросов.

## Содержание

- [Обзор](#обзор)
- [HTML Структура](#html-структура)
- [Скрипты JavaScript](#скрипты-javascript)

## HTML Структура

### Основные элементы

- `<!DOCTYPE html>`: Объявление типа документа HTML5.
- `<html lang="en">`: Корневой элемент HTML документа, устанавливающий язык на английский.
- `<head>`: Контейнер для метаданных документа, таких как кодировка, viewport, заголовок страницы, подключение CSS.
- `<body>`: Основное содержание документа, которое отображается на странице.

### Метаданные

- `<meta charset="UTF-8">`: Установка кодировки символов UTF-8.
- `<meta name="viewport" content="width=device-width, initial-scale=1.0">`: Настройка viewport для корректного отображения на разных устройствах.
- `<title>Kazarinov Chat</title>`: Заголовок страницы, отображаемый во вкладке браузера.

### Стили и скрипты

-   `<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" ...>`: Подключение Bootstrap CSS для стилизации.
-   `<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>`: Подключение jQuery.
-   `<link rel="stylesheet" href="{{ url_for('static', path='css/styles.css') }}">`: Подключение дополнительных стилей из файла `styles.css`.

### Основные контейнеры

-   `<div class="container mt-5">`: Главный контейнер, содержащий все элементы чата.
-   `<h1 class="text-center">Kazarinov AI Chat</h1>`: Заголовок чата.
-   `<div class="chat-box border rounded p-3 mb-3" style="height: 400px; overflow-y: scroll;">`: Контейнер для истории чата, с прокруткой по вертикали.
    -   `<div id="chat-log">`: Контейнер, куда добавляются сообщения.
-   `<form id="chat-form">`: Форма для отправки сообщений.
    -   `<div class="input-group">`: Группа элементов ввода.
        -   `<input type="text" id="user-input" class="form-control" placeholder="Введите сообщение...">`: Поле ввода для сообщений пользователя.
        -   `<div class="input-group-append">`: Кнопка отправки сообщения.
            -   `<button class="btn btn-primary" type="submit">Отправить</button>`: Кнопка отправки сообщения.

## Скрипты JavaScript

### Обработчик отправки формы

-   `$(document).ready(function() { ... });`:  Функция, которая выполняется после загрузки DOM.
    -   `$('#chat-form').submit(function(event) { ... });`: Обработчик события отправки формы.
        -   `event.preventDefault();`: Отмена стандартного поведения отправки формы.
        -   `let userInput = $('#user-input').val();`: Получение текста сообщения из поля ввода.
        -   `$('#chat-log').append('<p><strong>Вы:</strong> ' + userInput + '</p>');`: Добавление сообщения пользователя в историю чата.
        -   `$.ajax({ ... });`: AJAX-запрос для отправки сообщения на сервер.
            -   `url: '/ask'`: URL для отправки запроса.
            -   `method: 'POST'`: HTTP метод запроса.
            -   `data: { user_input: userInput }`: Данные для отправки на сервер.
            -   `success: function(response) { ... }`: Обработчик успешного ответа от сервера.
                -   `$('#chat-log').append('<p><strong>AI:</strong> ' + response.response + '</p>');`: Добавление ответа от AI в историю чата.
                -   `$('#user-input').val('');`: Очистка поля ввода.