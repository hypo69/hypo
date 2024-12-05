rst
How to use this HTML file for a Generative AI Chat Interface
========================================================================================

Description
-------------------------
This HTML file (`index.html`) creates the front-end structure for a chat application that interacts with a generative AI model.  It sets up the basic page layout, including a title, styles for the page, and a designated area (`chat-app`) for the chat content.  The application is expected to use JavaScript (`app.js`) to dynamically update the chat display.

Execution steps
-------------------------
1. **Load the HTML file:** The `index.html` file is served by a web server. A user will open this file in a web browser.
2. **Include external resources:** The HTML file links to a CSS stylesheet (`/static/bootstrap.min.css`) for styling the application, and a JavaScript file (`/static/app.js`) containing the application logic.  These files must be accessible from the web server.
3. **Create the page layout:** The file creates a basic HTML page structure.  A `div` with the ID `chat-app` is reserved for rendering the conversation.  The `<h1>` tag displays the page title.
4. **Load the JavaScript file:** The HTML file includes the `<script>` tag with `type="text/babel"`. This references a JavaScript file (`/static/app.js`).   The use of the `src` attribute indicates that the file is expected to contain client-side JavaScript application code. This JavaScript code will be responsible for handling user interaction, updating the chat content in the `chat-app` div, and communicating with the backend for AI responses. The `babel` type suggests that the JavaScript code might be compiled with Babel.


Usage example
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