# Шаблон чата Gemini

## Обзор

Этот шаблон предоставляет HTML-код для веб-чата, использующего Gemini. Шаблон включает в себя отображение сообщений пользователя и ответа модели, а также форму для ввода сообщений пользователем.  Он использует Bootstrap для стилизации и jQuery для обработки событий.

## Структура

### HTML-код

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kazarinov Chat</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <!-- Дополнительные стили -->
    <link rel="stylesheet" href="{{ url_for('static', path='css/styles.css') }}">
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Kazarinov AI Chat</h1>
        <div class="chat-box border rounded p-3 mb-3" style="height: 400px; overflow-y: scroll;">
            <div id="chat-log">
                <!-- Здесь будут отображаться сообщения -->
            </div>
        </div>
        <form id="chat-form">
            <div class="input-group">
                <input type="text" id="user-input" class="form-control" placeholder="Введите сообщение...">
                <div class="input-group-append">
                    <button class="btn btn-primary" type="submit">Отправить</button>
                </div>
            </div>
        </form>
    </div>
    <script>
        $(document).ready(function() {
            $('#chat-form').submit(function(event) {
                event.preventDefault();

                let userInput = $('#user-input').val();
                $('#chat-log').append('<p><strong>Вы:</strong> ' + userInput + '</p>');

                $.ajax({
                    url: '/ask',
                    method: 'POST',
                    data: { user_input: userInput },
                    success: function(response) {
                        $('#chat-log').append('<p><strong>AI:</strong> ' + response.response + '</p>');
                        $('#user-input').val('');  // Очистка поля ввода
                    },
                    error: function(ex) {
                        console.error("Ошибка:", ex);
                        $('#chat-log').append('<p><strong>Ошибка:</strong> Произошла ошибка при отправке запроса.</p>');
                    }
                });
            });
        });
    </script>
</body>
</html>
```

### Скрипт JavaScript

Обрабатывает отправку запросов к серверу и обновление чата. Обработка ошибок.

###  Обработка AJAX запросов

Используется jQuery для выполнения AJAX запросов к серверу `/ask` с данными из поля ввода.  Успешный ответ добавляет ответ модели в чат-лог.  Обработка ошибок позволяет отображать сообщения об ошибках пользователю.

## Использование

Для использования шаблона необходимо:

- Настроить маршрут `/ask` на сервере, который обрабатывает POST запросы с параметром `user_input`.
- Сервер должен возвращать JSON-объект с ключом `response` содержащим ответ модели.
- Подключить необходимые библиотеки (Bootstrap и jQuery).


```
```
```