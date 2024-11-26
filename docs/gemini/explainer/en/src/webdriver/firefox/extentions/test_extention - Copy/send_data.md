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
    A[onPageLoad()] --> B{Get page info};
    B --> C[Form data object];
    C --> D[Send data to API];
    D --> E{Handle response};
    E -- success --> F[Process response];
    E -- error --> G[Handle error];
    F --> H[Log response];
    G --> I[Log error];
    Subgraph Window Events
        J[window.addEventListener('load', onPageLoad)] --> A
    End
```

**Examples:**

* **B (Get page info):**
    * `title`: "My Awesome Page"
    * `url`: "http://example.com/page"
    * `body`: HTML content of the page

* **C (Form data object):**
    * `data`: `{ title: "My Awesome Page", url: "http://example.com/page", body: "<html><body>...</body></html>" }`

* **D (Send data to API):** Sends the `data` object as JSON to the specified API endpoint.


**<explanation>**

* **Imports:** There are no imports. The code uses built-in JavaScript functionality.

* **Classes:** There are no classes.

* **Functions:**
    * `onPageLoad()`: This function collects page title, URL, and body content. It then sends this data to a server (`http://127.0.0.1/hypotez.online/api/`) using the `fetch` API.
        * **Arguments:** None.
        * **Return value:** None.
        * **Example Usage:** When a webpage loads, this function is triggered to collect the information and send it to the server.

* **Variables:**
    * `title`, `url`, `body`: These are variables that store strings. They hold the page title, URL, and body content respectively.
    * `data`: This is a JavaScript object that stores the collected data.
    * `response`: A `Response` object returned by the `fetch` API.
    * `json`: The parsed JSON response from the server.
    * `error`: An `Error` object if an error occurs during the network request.

* **Potential Errors and Improvements:**

    * **Error Handling:** The code handles potential errors during the `fetch` request, which is crucial for robustness. However, it logs the error but doesn't provide a way to handle the failure or retry the request.
    * **Network Issues:** No retry mechanism if the server is down or the network is unavailable.
    * **API Responses:**  The code expects a JSON response from the server. The `response.ok` check is important but doesn't tell you *what* went wrong on the server.  Consider adding `response.status` to the error handling to get a more specific error message.
    * **Security:** Hardcoding the API endpoint like `http://127.0.0.1/hypotez.online/api/` can be problematic in production.   The endpoint should be configurable.
    * **Data Validation:** There's no validation on the data received from the page.  If the `document.title`, `window.location.href`, or `document.body.innerHTML` are invalid, it could cause problems with the API.


**Relationships with Other Parts of the Project:**

The code sends data to an API endpoint (`http://127.0.0.1/hypotez.online/api/`). This implies that this API endpoint is part of the `hypotez` project (or potentially a separate service).  The collected data (title, URL, body content) might be used for various purposes (e.g., indexing, analysis) on the server-side. Therefore, the API (`/hypotez.online/api/`) is a critical part of the workflow, handling the data collection and possibly subsequent processing. The `hypotez` project likely has components to receive, process, and potentially store the data from the API.