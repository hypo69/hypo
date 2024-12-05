# Code Explanation: send_data.js

## <input code>

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

## <algorithm>

**Step 1:** `onPageLoad()` function is called when the page loads.

*   **Input:** The current document loaded in the browser.
*   **Output:** Sends data to the server (`http://127.0.0.1/hypotez.online/api/`). Logs success or error messages to the console.


**Step 2:** Collects page information.

*   **Input:** The current page's DOM (`document`).
*   **Output:** Extracts `title`, `url`, and `body` content.  *Example:* `title = "My Page Title"`, `url = "http://example.com/page"`, `body = "<html><body>...</body></html>"`.


**Step 3:** Formats data for transmission.

*   **Input:** Extracted `title`, `url`, and `body`.
*   **Output:** Creates a JavaScript object (`data`) with these properties. *Example:* `{ title: "My Page Title", url: "http://example.com/page", body: "<html><body>...</body></html>"}`.


**Step 4:** Sends data using `fetch`.

*   **Input:** Data object and API endpoint.
*   **Output:** Sends a POST request to the specified URL with the prepared data, formatted as JSON.


**Step 5:** Handles response.

*   **Input:** Server response.
*   **.Output:**
    *   Checks if the response is successful (status code 200-299). If not, throws an error.
    *   Parses the response body as JSON.
    *   Logs the parsed JSON to the console if the request is successful.


**Step 6:** Handles errors.

*   **Input:** Error during any of the previous steps.
*   **Output:** Logs the error to the console.



## <mermaid>

```mermaid
graph TD
    A[window.addEventListener('load', onPageLoad)] --> B(onPageLoad);
    B --> C{Collect Page Info};
    C --> D[title, url, body];
    D --> E{Format Data};
    E --> F(data);
    F --> G[fetch];
    G --> H{Server Response};
    H -- Success --> I[Parse JSON];
    I --> J{Log Response};
    H -- Failure --> K[Error Handling];
    K --> L[Log Error];
```

**Dependencies:**

The mermaid diagram shows a simple flow.  No significant external dependencies are visible within the code snippet itself. `fetch` is a native browser API, so no external modules are imported.


## <explanation>

**Imports:**

No explicit imports are used.  `fetch` is a standard browser API, so no external module is required for this script.


**Classes:**

There are no classes defined in the code.


**Functions:**

*   `onPageLoad()`: This function is the main entry point, triggered by the `load` event of the current window.
    *   **Arguments:** None.
    *   **Return Value:**  None.
    *   **Purpose:**  To gather data about the loaded page and send it to a server using `fetch`.


**Variables:**

*   `title`: Stores the title of the current page (string).
*   `url`: Stores the URL of the current page (string).
*   `body`: Stores the HTML content of the current page's body (string).
*   `data`: Stores a JavaScript object containing the collected data (object).


**Potential Errors/Improvements:**

*   **Error Handling:** While the code has error handling using `try...catch` and `response.ok`, it doesn't handle specific error cases like network failures or server errors gracefully. Adding more specific error messages (e.g., checking for a 404 Not Found response) would be beneficial.
*   **Security:** Hardcoding the API endpoint (`http://127.0.0.1/hypotez.online/api/`) is not ideal for production code. Using environment variables or configuration files is recommended for better security and maintainability.
*   **Input Validation:** The code assumes the server will handle invalid data gracefully.  Adding client-side validation (checking for the correct format of the data) might prevent sending corrupted or inappropriate data to the server.
*   **Asynchronous Operations:** `fetch` is asynchronous.  The code might benefit from better handling of asynchronous operations, particularly if there's a complex sequence of actions depending on the API call.


**Relationships with other parts of the project:**

This script likely interacts with a server-side component (`/hypotez.online/api/`) to process the collected data. The server-side component (not shown in this snippet) will be responsible for handling the POST request and the further processing of the collected page information.  There is a likely dependency on the browser's rendering engine (JavaScript engine) for the page operations.