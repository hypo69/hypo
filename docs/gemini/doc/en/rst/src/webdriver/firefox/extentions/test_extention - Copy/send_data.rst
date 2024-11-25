send_data.js
==========

This JavaScript file defines a function `onPageLoad` to collect page information (title, URL, body content) and send it via a POST request to a specified API endpoint.

Functions
---------

.. autofunction:: onPageLoad
   :noindex:

.. autofunction:: fetch
   :noindex:

Explanation
-----------

^ onPageLoad
~~~~~~~~~~~

This function collects data from the current webpage:

- It retrieves the page title using `document.title`.
- It gets the current URL using `window.location.href`.
- It extracts the HTML content of the page body using `document.body.innerHTML`.

- It creates a JavaScript object `data` containing the collected information.

- It sends a POST request to the API endpoint `http://127.0.0.1/hypotez.online/api/` using the `fetch` API.
    - The request includes the collected data as JSON.

- It handles potential errors during the request and response processing using `.then()` and `.catch()`.
    - If the server returns a non-2xx status code, an error is thrown.
    - If the response is successful, the returned JSON data is processed and logged to the console.
    - If any error occurs during the request or processing, the error is logged to the console.


^ window.addEventListener
~~~~~~~~~~~~~~~~~~~~~~~~~

This line of code adds the `onPageLoad` function as an event listener to the `load` event of the `window`. This ensures that `onPageLoad` is executed when the entire page has finished loading.