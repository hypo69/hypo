# `index.html`

## Обзор

Данный файл представляет собой HTML-страницу с формой для отправки имени и фамилии на сервер через AJAX-запрос. Используется Bootstrap для стилизации и jQuery для обработки формы и AJAX-запросов.

## Оглавление

- [Обзор](#обзор)
- [HTML Структура](#html-структура)
- [JavaScript](#javascript)

## HTML Структура

### Структура

HTML-страница содержит следующие элементы:
- Заголовок `<title>`: "Форма для отправки данных".
- Подключение Bootstrap CSS для стилизации.
- Контейнер `<div>` с классом `container`, содержащий заголовок `<h2>` и форму `<form>`.
- Форма с полями ввода для имени (`firstName`) и фамилии (`lastName`).
- Кнопка `<button>` для отправки формы.
- Подключение jQuery.
- JavaScript-код для обработки отправки формы через AJAX.

### Подключение CSS

```html
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
```
- Подключает Bootstrap CSS для стилизации страницы.

### Форма

```html
<form id="dataForm">
  <div class="form-group">
    <label for="firstName">Имя:</label>
    <input type="text" class="form-control" id="firstName" placeholder="Введите имя" required>
  </div>
  <div class="form-group">
    <label for="lastName">Фамилия:</label>
    <input type="text" class="form-control" id="lastName" placeholder="Введите фамилию" required>
  </div>
  <button type="submit" class="btn btn-primary">Отправить</button>
</form>
```

-   `id="dataForm"`: Идентификатор формы для взаимодействия с JavaScript.
-   `firstName` и `lastName`: Поля ввода для имени и фамилии соответственно.
-   Кнопка `Отправить`: Тип submit, отправляет форму.

## JavaScript

### Обработчик отправки формы
```javascript
$('#dataForm').submit(function(event) {
    event.preventDefault();

    var firstName = $('#firstName').val();
    var lastName = $('#lastName').val();
        
    $.ajax({
        type: 'POST',
        url: '/process_data',
        contentType: 'application/json',
        data: JSON.stringify({first_name: firstName, last_name: lastName}),
        success: function(response) {
             console.log('Ответ от сервера:', response);
             // Дополнительные действия по необходимости
        },
        error: function(xhr, status, error) {
             console.error('Ошибка при отправке данных:', error);
        }
    });
});
```
-  `$('#dataForm').submit(function(event) { ... });`: Обработчик события отправки формы.
-   `event.preventDefault()`: Предотвращает стандартное поведение отправки формы.
-   Извлекает данные из полей ввода `firstName` и `lastName`.
-   Отправляет AJAX-запрос типа POST на URL `/process_data`.
-   Данные отправляются в формате JSON.
-   В случае успешного ответа от сервера выводит ответ в консоль.
-   В случае ошибки выводит сообщение об ошибке в консоль.