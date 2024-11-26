```
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

**<algorithm>**

```mermaid
graph TD
    A[Page Loads] --> B{Get Page Info};
    B --> C[Form Data Object];
    C --> D[Send POST Request];
    D --> E{Handle Response};
    E --Success--> F[Process JSON Response];
    E --Error--> G[Error Handling];
    F --> H[Log Response];
    G --> I[Log Error];

    subgraph "Get Page Info"
        B -- title --> J[document.title];
        B -- url --> K[window.location.href];
        B -- body --> L[document.body.innerHTML];
    end
    
    subgraph "Form Data Object"
        C --> M[data = {title, url, body}];
    end
    
    subgraph "Send POST Request"
        D --> N[fetch('http://127.0.0.1/hypotez.online/api/')];
        N --> O[JSON.stringify(data)];
    end
    subgraph "Handle Response"
        E --response.ok--> P[Return response.json()];
        E --!response.ok--> Q[Throw Error];

    end

    subgraph "Process JSON Response"
        F --> R[JSON parsed result];
    end
```

**Example Data Flow:**

*   **Page Load:** User navigates to a webpage.
*   **Get Page Info:** `document.title` = "My Page Title", `window.location.href` = "https://example.com/page", `document.body.innerHTML` = "<p>Page content</p>".
*   **Form Data Object:** `data` = `{title: "My Page Title", url: "https://example.com/page", body: "<p>Page content</p>"}`.
*   **Send POST Request:** The script sends a POST request to `http://127.0.0.1/hypotez.online/api/` with the `data` object in the request body.
*   **Handle Response:** If successful, the server response is parsed as JSON.
*   **Process JSON Response:**  The parsed JSON is stored in the `json` variable.
*   **Log Response:** The script prints the parsed JSON response to the console.


**<explanation>**

*   **Imports:** There are no explicit imports. This script relies on built-in JavaScript objects and functions (`document`, `window`, `fetch`).

*   **Classes:** There are no classes.

*   **Functions:**
    *   **`onPageLoad()`**: This function handles the page load event.
        *   **Arguments:** None.
        *   **Return Value:** None.
        *   **Purpose:** Collects page title, URL, and body content, serializes it into a JSON object, and sends the request to the server.
        *   **Example Usage:** When the page loads, this function automatically executes.

*   **Variables:**
    *   **`title`, `url`, `body`**: These variables are strings and hold page information.
    *   **`data`**: This is a JavaScript object containing the collected information.
    *   **`response`**:  Represents the response from the `fetch` call.
    *   **`json`**: Represents the parsed JSON from the response.


*   **Potential Errors/Improvements:**
    *   **Error Handling:** The `fetch` call includes error handling, which is good.  However, it would be beneficial to include more specific error handling for the `JSON.parse` part as well, just in case the server returns something unexpected.
    *   **Robustness:** Consider adding a check for the existence of `document.title`, `window.location.href`, and `document.body` in case the page is not fully loaded yet. This could prevent errors if the page is loading.
    *   **API Specificity:**  Hardcoding the API endpoint (`http://127.0.0.1/hypotez.online/api/`) makes the code less reusable; consider using a configuration file or environment variables.


**Relationships with Other Parts of the Project:**

This JavaScript code likely communicates with a backend API (`/hypotez.online/api/`) hosted on a server.  The server-side code would handle the POST request and process the received data.  The `hypotez/src/` hierarchy suggests that the server-side logic and data processing are likely implemented within other parts of the project, and this client-side JavaScript code is designed to interact with it. A clear understanding of the server-side API structure and expected input/output is crucial for this code's proper function.