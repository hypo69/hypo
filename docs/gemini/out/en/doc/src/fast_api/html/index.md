# HTML Form for Data Submission

## Overview

This HTML file creates a form for collecting user data (first name and last name) and submitting it to a FastAPI endpoint.  It utilizes Bootstrap for styling and jQuery for AJAX requests.  The submitted data is serialized as JSON and sent to the `/process_data` endpoint.


## HTML Structure

The HTML file is structured to include a form with input fields for first name and last name, and a submit button.  It utilizes Bootstrap for styling.


## JavaScript Functionality

The JavaScript code handles the form submission using AJAX:

### Form Submission Handler

```javascript
// Обработчик события отправки формы
$('#dataForm').submit(function(event) {
    // Предотвращаем стандартное поведение формы
    event.preventDefault();

    // Получаем данные из полей ввода
    var firstName = $('#firstName').val();
    var lastName = $('#lastName').val();

    // Отправляем данные на сервер
    $.ajax({
        type: 'POST',
        url: '/process_data',  // Замените '/process_data' на URL вашего FastAPI эндпоинта
        contentType: 'application/json',
        data: JSON.stringify({first_name: firstName, last_name: lastName}), // Преобразуем данные в формат JSON
        success: function(response) {
            // Обработка успешного ответа от сервера
            console.log('Ответ от сервера:', response);
            // Дополнительные действия по необходимости
        },
        error: function(xhr, status, error) {
            // Обработка ошибки
            console.error('Ошибка при отправке данных:', error);
        }
    });
});
```

**Description**: This function handles the form submission. It prevents the default form submission behavior, retrieves the input values, and sends the data to the specified API endpoint via AJAX.


**Parameters**:
- `event` (object): The event object associated with the form submission.


**Returns**:
- None


**Raises**:
- None (errors handled within the `$.ajax` call).



## API Interaction

The JavaScript code expects a `POST` request to `/process_data` with a JSON payload containing the user's first and last names. This endpoint should be defined in your FastAPI application.


##  Bootstrap and jQuery Integration


The HTML file utilizes Bootstrap's CSS for styling and jQuery for AJAX communication.  These external resources are linked to the HTML file.

**Description**: The file utilizes external libraries to style the webpage (Bootstrap) and handle AJAX interactions (jQuery).


**Dependencies**:
- Bootstrap CSS
- jQuery


**Notes**:
Replace `/process_data` with the actual URL of your FastAPI endpoint.  Proper error handling and response processing are essential for production code.


##  Example Usage


1.  Fill in the first name and last name fields.
2.  Click the "Отправить" button.
3.  The form's data will be sent to the `/process_data` endpoint in your FastAPI app. The response (if successful) will be logged in the console.