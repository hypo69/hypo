rst
How to use PrestaShop API for different websites
==========================================================================================

Description
-------------------------
This document describes how to interact with PrestaShop websites using their APIs. It outlines the structure, how to store API keys securely, and provides examples of API calls.

Execution steps
-------------------------
1. **Identify the website:** Determine which PrestaShop website's API you need to interact with (e.g., e-cat.co.il, emil-design.com).

2. **Obtain API key:** Retrieve the API key for the selected website from the `credentials.kdbx` file.  This file is a password database; use a password manager that supports `.kdbx` format (like KeePass or KeePassXC) to access and securely manage the keys.

3. **Encode API key:** Convert the retrieved API key into Base64 format.  This encoding is crucial for including the API key in the `Authorization` header of the API request.  

4. **Construct the API request:** Use the `curl` command-line tool to send the API request. The template below provides a general format.

    - Replace `<URL_сайта>` with the specific URL of the target website (e.g., `e-cat.co.il`).
    - Replace `<endpoint>` with the desired API endpoint (e.g., `products`, `customers`).
    - Replace `<base64(API_KEY)>` with the Base64-encoded API key.

5. **Execute the request:** Execute the constructed `curl` command.


Usage example
-------------------------
.. code-block:: bash

    curl -X GET 'https://e-cat.co.il/api/products' \
    -H 'Authorization: Basic <base64(API_KEY)>'

**Explanation:**

This example retrieves the list of products from the `e-cat.co.il` website. The `-X GET` specifies a GET request, while `-H 'Authorization: Basic <base64(API_KEY)>'` sets the authorization header with the encoded API key.  Replace `<base64(API_KEY)>` with the actual Base64 encoded API key for the website.


Additional notes
-------------------------
- **Security:** Never share the `credentials.kdbx` file with anyone else.  Store it securely and update API keys regularly.  

- **Troubleshooting:** Consult the PrestaShop API documentation (https://devdocs.prestashop.com/) for details on endpoints and available methods if you encounter problems.