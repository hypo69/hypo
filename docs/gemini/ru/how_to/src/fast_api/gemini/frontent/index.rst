Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код представляет собой шаблон HTML-страницы для веб-приложения, взаимодействующего с генеративным ИИ. Страница содержит заголовок "AI Chat Interface" и пустой div-контейнер с id "chat-app".  HTML также подключает CSS-стили из файла `/static/bootstrap.min.css` и JavaScript-код из `/static/app.js` для динамической работы с чатом.  Он устанавливает переменную `MODE` со значением 'debug'.

Шаги выполнения
-------------------------
1. **Определяет константу `MODE`:**  Устанавливается переменная `MODE` со значением 'debug'.  Это, вероятно, используется для настройки поведения приложения в разных режимах (например, для отладки).
2. **Создаёт структуру HTML-документа:**  Определяет стартовую HTML-структуру с тегами `<html>`, `<head>`, `<body>`.  Устанавливает кодировку UTF-8.
3. **Настраивает заголовок и метаданные:**  Добавляет тег `<title>` и метатеги `<meta>` для корректного отображения страницы.
4. **Подключает CSS:** Подключает внешний CSS-файл `/static/bootstrap.min.css`. Это, вероятно, для использования стандартной стилизации Bootstrap.
5. **Создаёт стили:** Добавляет стили для тела страницы (`body`) - отступ в 2rem.
6. **Создаёт контент страницы:** Создаёт div-контейнер `container` с заголовком `<h1>AI Chat Interface</h1>`. Также включает пустой div-контейнер с id `chat-app`.
7. **Подключает JavaScript:**  Подключает JavaScript-код из `/static/app.js` с помощью тега `<script>`. Этот скрипт, вероятно, отвечает за динамическое взаимодействие с чатом.  `<script type="text/babel">` указывает, что JavaScript-код написан на Babel.

Пример использования
-------------------------
.. code-block:: html+xml

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Chat with Generative AI</title>
        <link rel="stylesheet" href="/static/bootstrap.min.css">
        <style>
            body {
                padding: 2rem;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>AI Chat Interface</h1>
            <div id="chat-app"></div>
        </div>

        <script type="text/babel" src="/static/app.js"></script>
    </body>
    </html>