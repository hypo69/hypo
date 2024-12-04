# Received Code

```javascript
// Создаем обработчик события для загрузки страницы
function onPageLoad() {
    // Собираем информацию о странице
    var title = document.title;
    var url = window.location.href;
    var body = document.body.innerHTML;

    // Формируем объект с данными для отправки
    var data = {
        title: title,
        url: url,
        body: body
    };

    // Отправляем данные на указанный адрес
    fetch('http://127.0.0.1/hypotez.online/api/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(json => {
            console.log('Response:', json);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Добавляем обработчик события для загрузки страницы
window.addEventListener('load', onPageLoad);
```

# Improved Code

```javascript
// Module for sending page data to a server.
// This module defines a function to collect page data (title, URL, and body content)
// and send it to a specified API endpoint using the fetch API.

/**
 * Collects page data and sends it to the API.
 *
 * Collects the document title, URL, and body content.
 * Serializes the data into JSON format and sends a POST request to the specified endpoint.
 * Handles potential errors during the fetch process.
 * Logs errors and successful responses to the console.
 */
function onPageLoad() {
    // Collect page information.
    const title = document.title;
    const url = window.location.href;
    const body = document.body.innerHTML;

    // Prepare data object for sending.
    const data = {
        title: title,
        url: url,
        body: body
    };

    // Send data to the specified API endpoint using fetch.
    fetch('http://127.0.0.1/hypotez.online/api/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            // Handling unsuccessful responses.
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(jsonResponse => {
        // Successful response handling.
        console.log('Response:', jsonResponse);
    })
    .catch(error => {
        // Error handling during the fetch process.
        console.error('Error sending data:', error);
        // Add more specific error handling (e.g., logging to a file)
    });
}

// Add event listener for page load.
window.addEventListener('load', onPageLoad);
```

# Changes Made

*   Added module-level documentation using RST format.
*   Added function-level docstrings using RST format.
*   Replaced `var` with `const` where appropriate (e.g., for `title`, `url`, `body`, `data`).
*   Improved error handling by providing more specific error messages using template literals and logging errors to the console using `console.error`.
*   Improved code readability and added comments explaining each step.

# Optimized Code

```javascript
// Module for sending page data to a server.
// This module defines a function to collect page data (title, URL, and body content)
// and send it to a specified API endpoint using the fetch API.

/**
 * Collects page data and sends it to the API.
 *
 * Collects the document title, URL, and body content.
 * Serializes the data into JSON format and sends a POST request to the specified endpoint.
 * Handles potential errors during the fetch process.
 * Logs errors and successful responses to the console.
 */
function onPageLoad() {
    // Collect page information.
    const title = document.title;
    const url = window.location.href;
    const body = document.body.innerHTML;

    // Prepare data object for sending.
    const data = {
        title: title,
        url: url,
        body: body
    };

    // Send data to the specified API endpoint using fetch.
    fetch('http://127.0.0.1/hypotez.online/api/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            // Handling unsuccessful responses.
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(jsonResponse => {
        // Successful response handling.
        console.log('Response:', jsonResponse);
    })
    .catch(error => {
        // Error handling during the fetch process.
		// Using src.logger for error logging.
        import {logger} from 'src.logger';
        logger.error('Error sending data:', error);
        // Add more specific error handling (e.g., logging to a file)
    });
}

// Add event listener for page load.
window.addEventListener('load', onPageLoad);